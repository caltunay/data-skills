#!/usr/bin/env python3
"""Eval runner for data-skills.

Approximates skill loading: it puts the skill's files, and the files of the skills it calls,
into the system prompt, plays the case as the user, then asks a judge model to grade the
transcript against the rubric. It does NOT test triggering.

Standard library, plus the official `anthropic` or `openai` SDK (imported only when used).
Keys are read from the environment by the SDKs (ANTHROPIC_API_KEY, OPENAI_API_KEY).
This script never reads, prints or stores a key.

Examples:
    python3 evals/runner/run.py --dry-run
    python3 evals/runner/run.py --provider anthropic --skills grill-the-ask
    python3 evals/runner/run.py --provider openai --model <model id> --price-in 1.25 --price-out 10
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
EVALS = ROOT / "evals"

# US dollars per million tokens (input, output). Anthropic list prices, cached 2026-11-03.
# Check current prices before a large run. Override with --price-in and --price-out.
PRICES = {
    "claude-fable-5-2": (8.00, 40.00),
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
}
DEFAULT_MODEL = {"anthropic": "claude-opus-5-5"}
# Models that can decline a request and take the server-side fallback parameter.
FALLBACK_MODELS = {"claude-fable-5-2", "claude-opus-5-5", "claude-sonnet-5-5"}

CHARS_PER_TOKEN = 4          # rough estimate
EST_REPLY_TOKENS = 1500      # per assistant turn
EST_JUDGE_TOKENS = 500

PREAMBLE = """You are an AI agent with the data-skills installed. The skill files are below.
Follow them exactly, as you would if your agent had loaded them.
The user's message may run a slash command: that means "apply the skill of that name".
Environment for this test: {environment}
You have no data connection in this test. Hand queries over and wait, as the skills say.
"""
DEFAULT_ENV = ("a coding agent with a user project folder. Unless the case says otherwise, "
               "there is no DATA-MAP.md and no analysis.md yet.")

JUDGE_SYSTEM = """You grade one test of an AI skill. You are strict and fair.
You get: the case (input, what a pass looks like, what a fail looks like), the rubric, and the transcript.
Grade only what the transcript shows. Do not reward length. Do not invent failures.
- pass: every "Pass" point that the transcript had the chance to show is met, and no "Fail" point occurs.
- partial: most "Pass" points are met, no "Fail" point occurs, but something is missing or weak.
- fail: a "Fail" point occurs, or a core "Pass" point is missed.
The transcript may end before the skill is finished. Do not mark down steps it had no turn to reach.
Answer in exactly this form:
VERDICT: pass|partial|fail
REASONS:
- <one line each, at most 6>
"""


def sections(text):
    """Split a markdown file into {heading: body} on '## ' headings."""
    out, name, buf = {}, "_top", []
    for line in text.splitlines():
        if line.startswith("## "):
            out[name] = "\n".join(buf).strip()
            name, buf = line[3:].strip().lower(), []
        else:
            buf.append(line)
    out[name] = "\n".join(buf).strip()
    return out


def skill_files(name):
    folder = SKILLS / name
    files = [folder / "SKILL.md"] + sorted(p for p in folder.glob("*.md") if p.name != "SKILL.md")
    return [p for p in files if p.exists()]


def called_skills(name):
    """Model-invoked skills named in backticks in the skill's SKILL.md."""
    text = (SKILLS / name / "SKILL.md").read_text()
    # only model-invoked skills (disciplines and data skills). Commands named as a next step are not loaded.
    names = {p.name for p in SKILLS.iterdir()
             if p.is_dir() and "Use only when the user runs /" not in (p / "SKILL.md").read_text()}
    found = set(re.findall(r"`/?([a-z][a-z-]+)`", text))
    return sorted((found & names) - {name})


def build_system(skill, environment):
    parts = [PREAMBLE.format(environment=environment)]
    for s in [skill] + called_skills(skill):
        for path in skill_files(s):
            parts.append(f"\n===== skill: {s} / file: {path.name} =====\n{path.read_text()}")
    return "\n".join(parts)


def user_turns(case):
    """First turn is the Input. Later turns come from 'Simulated answers'."""
    turns = [case.get("input", "").strip()]
    sim = case.get("simulated answers", "").strip()
    if not sim or sim.lower().startswith("none"):
        return turns
    rounds = re.split(r"(?m)^(?:Round|Turn) \d+[^:\n]*:\s*", sim)
    rounds = [r.strip().strip('"') for r in rounds if r.strip()]
    return turns + rounds


def discover(skill_filter, case_filter):
    cases = []
    for folder in sorted(p for p in EVALS.iterdir() if p.is_dir() and (p / "rubric.md").exists()):
        if skill_filter and folder.name not in skill_filter:
            continue
        if not (SKILLS / folder.name).exists():
            continue
        for path in sorted(folder.glob("case-*.md"), key=lambda p: int(re.findall(r"\d+", p.stem)[0])):
            if case_filter and path.stem not in case_filter:
                continue
            cases.append((folder.name, path))
    return cases


def tokens(text):
    return len(text) // CHARS_PER_TOKEN


class Anthropic:
    def __init__(self, model, max_tokens, use_fallbacks):
        import anthropic  # optional import
        self.client = anthropic.Anthropic()
        self.model, self.max_tokens = model, max_tokens
        self.use_fallbacks = use_fallbacks and model in FALLBACK_MODELS

    def reply(self, system, messages):
        """Return (text, assistant content to send back unchanged, usage)."""
        if self.use_fallbacks:
            response = self.client.beta.messages.create(
                model=self.model, max_tokens=self.max_tokens, system=system, messages=messages,
                betas=["server-side-fallback-2026-07-01"], fallbacks="default",
            )
        else:
            response = self.client.messages.create(
                model=self.model, max_tokens=self.max_tokens, system=system, messages=messages,
            )
        text = "".join(block.text for block in response.content if block.type == "text")
        if response.stop_reason == "refusal":
            text += "\n[the model declined this request]"
        elif response.stop_reason == "max_tokens":
            text += "\n[reply cut off at max_tokens]"
        return text, response.content, (response.usage.input_tokens, response.usage.output_tokens)


class OpenAI:
    def __init__(self, model, max_tokens):
        import openai  # optional import
        self.client = openai.OpenAI()
        self.model, self.max_tokens = model, max_tokens

    def reply(self, system, messages):
        response = self.client.chat.completions.create(
            model=self.model, max_completion_tokens=self.max_tokens,
            messages=[{"role": "system", "content": system}] + messages,
        )
        text = response.choices[0].message.content or ""
        return text, text, (response.usage.prompt_tokens, response.usage.completion_tokens)


def run_case(client, system, turns):
    messages, transcript, used = [], [], [0, 0]
    for turn in turns:
        messages.append({"role": "user", "content": turn})
        text, content, usage = client.reply(system, messages)
        messages.append({"role": "assistant", "content": content})
        transcript.append(("USER", turn))
        transcript.append(("AGENT", text))
        used[0] += usage[0]
        used[1] += usage[1]
    return transcript, used


def judge_prompt(case_text, rubric, transcript):
    lines = "\n\n".join(f"[{who}]\n{text}" for who, text in transcript)
    return f"# Case\n{case_text}\n\n# Rubric\n{rubric}\n\n# Transcript\n{lines}"


def parse_verdict(text):
    m = re.search(r"VERDICT:\s*(pass|partial|fail)", text, re.I)
    verdict = m.group(1).lower() if m else "unparsed"
    reasons = [l.strip("- ").strip() for l in text.split("REASONS:")[-1].splitlines() if l.strip().startswith("-")]
    return verdict, reasons


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", choices=["anthropic", "openai"], default="anthropic")
    ap.add_argument("--model", help="model under test. Default for anthropic: claude-opus-5-5. Required for openai.")
    ap.add_argument("--judge-model", help="model that grades. Default: the model under test.")
    ap.add_argument("--skills", nargs="*", help="only these skills (folder names in evals/)")
    ap.add_argument("--cases", nargs="*", help="only these cases, for example case-1 case-4")
    ap.add_argument("--max-tokens", type=int, default=4000, help="cap per reply")
    ap.add_argument("--max-turns", type=int, default=4, help="cap on user turns per case")
    ap.add_argument("--price-in", type=float, help="US dollars per million input tokens")
    ap.add_argument("--price-out", type=float, help="US dollars per million output tokens")
    ap.add_argument("--no-fallbacks", action="store_true", help="anthropic: do not send the refusal fallback parameter")
    ap.add_argument("--dry-run", action="store_true", help="print what would be sent and the estimated cost. No API call.")
    ap.add_argument("--yes", action="store_true", help="skip the confirmation question")
    args = ap.parse_args()

    model = args.model or DEFAULT_MODEL.get(args.provider)
    if not model:
        sys.exit("--model is required for this provider")
    judge_model = args.judge_model or model
    price = (args.price_in, args.price_out) if args.price_in is not None and args.price_out is not None else PRICES.get(model)
    judge_price = price if judge_model == model else PRICES.get(judge_model, price)

    cases = discover(args.skills, args.cases)
    if not cases:
        sys.exit("no cases found")

    plan, est_in, est_out, est_jin = [], 0, 0, 0
    for skill, path in cases:
        text = path.read_text()
        case = sections(text)
        env = case.get("setup", "").strip() or DEFAULT_ENV
        system = build_system(skill, env)
        turns = user_turns(case)[: args.max_turns]
        rubric = (EVALS / skill / "rubric.md").read_text()
        plan.append((skill, path, text, system, turns, rubric))
        # every turn resends the system prompt and the conversation so far
        for i, _ in enumerate(turns):
            est_in += tokens(system) + sum(tokens(t) for t in turns[: i + 1]) + i * EST_REPLY_TOKENS
            est_out += EST_REPLY_TOKENS
        est_jin += tokens(JUDGE_SYSTEM) + tokens(text) + tokens(rubric) + len(turns) * EST_REPLY_TOKENS + sum(tokens(t) for t in turns)

    print(f"Provider: {args.provider}   model: {model}   judge: {judge_model}")
    print(f"Cases: {len(plan)}   user turns: {sum(len(p[4]) for p in plan)}")
    print(f"Estimated tokens: {est_in + est_jin:,} in, {est_out + len(plan) * EST_JUDGE_TOKENS:,} out (rough: {CHARS_PER_TOKEN} characters per token)")
    if price:
        cost = (est_in * price[0] + est_out * price[1]) / 1e6
        cost += (est_jin * judge_price[0] + len(plan) * EST_JUDGE_TOKENS * judge_price[1]) / 1e6
        print(f"Estimated cost: about ${cost:.2f} at ${price[0]} in and ${price[1]} out per million tokens. Check current prices.")
    else:
        print("Estimated cost: unknown for this model. Pass --price-in and --price-out.")

    if args.dry_run:
        for skill, path, _, system, turns, _ in plan:
            print(f"\n--- {skill}/{path.name}")
            print(f"    system prompt: {len(system):,} characters. Skills loaded: {', '.join([skill] + called_skills(skill))}")
            for i, turn in enumerate(turns, 1):
                print(f"    user turn {i}: {turn[:160].replace(chr(10), ' ')}{'...' if len(turn) > 160 else ''}")
        print("\nDry run. Nothing was sent.")
        return

    if not args.yes:
        if input("Run for real? This calls the API and costs money. Type yes to continue: ").strip().lower() != "yes":
            sys.exit("Stopped. Nothing was sent.")

    def make(m):
        if args.provider == "anthropic":
            return Anthropic(m, args.max_tokens, not args.no_fallbacks)
        return OpenAI(m, args.max_tokens)

    client, judge = make(model), make(judge_model)
    rows, details, total = [], [], [0, 0]
    for skill, path, text, system, turns, rubric in plan:
        label = f"{skill}/{path.stem}"
        try:
            transcript, used = run_case(client, system, turns)
            graded, _, jused = judge.reply(JUDGE_SYSTEM, [{"role": "user", "content": judge_prompt(text, rubric, transcript)}])
            verdict, reasons = parse_verdict(graded)
            total[0] += used[0] + jused[0]
            total[1] += used[1] + jused[1]
        except Exception as error:  # report the failure and carry on with the next case
            verdict, reasons, transcript = "error", [f"{type(error).__name__}: {str(error)[:200]}"], []
        print(f"{label}: {verdict}")
        rows.append(f"| {skill} | {path.stem} | {verdict} | {'; '.join(reasons)[:300].replace('|', '/')} |")
        body = "\n\n".join(f"**{who}**\n\n{t}" for who, t in transcript)
        details.append(f"## {label}: {verdict}\n\n" + "\n".join(f"- {r}" for r in reasons) + f"\n\n<details><summary>Transcript</summary>\n\n{body}\n\n</details>\n")

    today = datetime.date.today().isoformat()
    out = EVALS / "results" / f"{today}-{args.provider}-{re.sub(r'[^A-Za-z0-9._-]', '-', model)}.md"
    counts = {v: sum(1 for r in rows if f"| {v} |" in r) for v in ("pass", "partial", "fail", "error", "unparsed")}
    summary = ", ".join(f"{n} {v}" for v, n in counts.items() if n)
    out.write_text(
        f"# Results: {today}, {args.provider}, {model}\n\n"
        f"Run by `evals/runner/run.py`. Judge: {judge_model}. Tokens used: {total[0]:,} in, {total[1]:,} out.\n"
        "This approximates skill loading and does not test triggering.\n\n"
        f"Summary: {summary}.\n\n| skill | case | verdict | notes |\n|---|---|---|---|\n" + "\n".join(rows) + "\n\n" + "\n".join(details)
    )
    print(f"\n{summary}\nWrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
