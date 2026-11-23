# Contributing

Thanks for helping. This repo is a set of plain `SKILL.md` files. Most changes are words, so the rules below are about words.

## The hard rules

They come from `SPEC.md` section 3. `scripts/self-check` tests most of them.

- Frontmatter is `name` and `description` only.
- Plain markdown. No tool names that belong to one agent. Say what to do, not which tool to call.
- No reliance on subagents.
- Name other skills. Never link to them by path. Relative links are fine inside a skill's own folder.
- Graceful fallback: a skill that calls another restates that skill's core rule in one or two lines.
- User-invoked descriptions say "Use only when the user runs /<name> or explicitly asks to ...".
- Model-invoked descriptions name concrete situations, tied to the flow, and stay narrow.
- No keys, no credentials, no employer material.
- Never call a data tool before the user names the source. Never fill in names the user has not said.
- Skills never write into this repo. User files live in `data-work/` in the user's project.
- Plain English, short sentences, active verbs, no em dashes.

## The neutral domain rule

Every example, template and eval uses one invented domain: an online shop and a subscription app (orders, customers, subscriptions, sign-ups, returns). Use no other domain, and no real company, product or table names. Invented data only.

## Add a method card

Cards live in `skills/question-types/`, one file per question type.

1. Pick the file for the question type.
2. Full card (common methods), with all 8 fields in this order: When to use, Data needed, Key assumptions, Checks that must pass, Common failure, Claim allowed, Simplest version first, Tool notes. Start it with `## Card: <name>`.
3. Short card (advanced methods): When to use, Key assumption, Key check, Claim allowed. Start it with `## Short card: <name>`. End it with "Get a specialist review before shipping."
4. A card covers choice, assumptions, checks, failure and claim. It is not a tutorial.
5. Add the card to the index table in `skills/question-types/SKILL.md`. For a causal method, add it to the causal method selector too.
6. Update the card counts in `scripts/self-check` (check 18).
7. Add or update a method-choice case in `evals/question-types/`.

## Add a skill

1. Open a "New skill proposal" issue first. Fewer skills trigger more cleanly.
2. Create `skills/<name>/SKILL.md`. The folder name equals `name`. Keep `SKILL.md` under 500 lines. Put long reference text in extra files in the same folder.
3. A user-invoked skill needs the "Hard rules" block (source first, no invented names). If it reads or writes files in `data-work/`, it also needs the "Start" and "End" blocks. Copy them from an existing flow skill.
4. Every skill needs the naming rule. Model-invoked skills carry it in a "Names and sources" section.
5. Add 3 eval cases and a rubric in `evals/<name>/` for a user-invoked skill: 2 with a planted flaw or ambiguity, 1 clean. Mark each "Data is invented". Add a "Simulated answers" section so the runner can play the user.
6. Add the skill to the lists at the top of `scripts/self-check`, to the catalogue in `skills/ask-data-skills/SKILL.md`, and to the README. Mark it **experimental** until its evals pass.
7. Log design choices in `DECISIONS.md`.

## Run the self-check

```bash
scripts/self-check
```

It prints PASS or FAIL per check and exits 1 on any failure. `docs/self-check.md` lists the checks. It also runs on every pull request and push.

### The private blocklist

The maintainer keeps a private list of words that must never appear in the repo. The words are not written anywhere in it.

- Locally: put the words in a file named `.blocklist` at the repo root, one per line. The file is gitignored. Without it, the check prints SKIP.
- On GitHub: Settings, then Secrets and variables, then Actions, then New repository secret. Name: `DATA_SKILLS_BLOCKLIST`. Value: the words, one per line. The workflow writes it to `.blocklist` inside the job and never prints it. A failure shows the file and line, not the word.
- Pull requests from forks do not receive secrets, so the check is skipped there and runs again after merge.

## Run the evals

By hand: follow `evals/README.md`. Run chat-app tests in an incognito chat with a neutral profile.

With the runner (it approximates skill loading and does not test triggering):

```bash
python3 evals/runner/run.py --dry-run
```

See `evals/runner/README.md` for a real run. Keys come from environment variables only.

## Release steps

1. `scripts/self-check` passes on the branch.
2. Bump `version` in `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. They must match. A set version pins plugin users until it changes.
3. Merge.
4. Create a release on GitHub. The ZIPs attach themselves: the `release` workflow runs `scripts/package-zips` and uploads one ZIP per skill as release assets.
5. Remove "experimental" from a skill in the README only when its evals have passed.

## Style of review

Critique the work, never the person.
