# data-skills

Skills that make your AI agent work like a senior data scientist: clarify first, validate every step, never overclaim. Works in any coding agent or chat app.

Free and open source (MIT).

## Install

```bash
npx skills add caltunay/data-skills
```

Claude Code, as a plugin:

```
/plugin install data-skills --marketplace caltunay/data-skills
```

Codex also has a plugin manifest. Or upload the ZIPs in claude.ai and ChatGPT. See [docs/install.md](docs/install.md).

## The flow

```
/setup-data-work            (once per team or project)
        |
        v
/grill-the-ask -> /plan-analysis -> /run-analysis -> /review-analysis -> /retro-analysis
                        ^                  |                 |
                        |__________________|                 |
                   plan revision entry       draft readout.md -> final readout.md
```

## The 6 commands

| Command | Does |
|---|---|
| `/setup-data-work` | Tests data access, interviews you, writes `DATA-MAP.md` |
| `/grill-the-ask` | Turns a vague ask into a clear question, with assumptions and a depth |
| `/plan-analysis` | Options, a chosen plan, the analysis table spec, success checks |
| `/run-analysis` | Builds the table, climbs the validation ladder, runs the method, drafts `readout.md` |
| `/review-analysis` | Technical and business review, claim check, verdict. Checks the readout word by word and marks it final |
| `/retro-analysis` | Proposes data map updates. You approve each one |

## Demo: two worked examples

Invented data, real query results. Each folder holds the data script, `DATA-MAP.md`, `analysis.md`, `readout.md` and the queries.

- [examples/signup-drop](examples/signup-drop/): "Why did sign-ups drop in March?" Descriptive, then exploratory. The readout says where the fall is, and that it cannot say why.
- [examples/pricing-page-test](examples/pricing-page-test/): an A/B test on the shop's pricing page, with a sample ratio check, power and a readout that keeps its uncertainty.

## Experimental extras (v0.2)

Every skill in this section is **experimental** until it has passed its evals. Expect changes.

| Command | Status | Does |
|---|---|---|
| `/ask-data-skills` | **experimental** | Tells you which command to run, why, and what comes after it |
| `/wayfinder-data` | **experimental** | Maps big, vague work as decision items, settles them one at a time, and ends with ready `/grill-the-ask` prompts |
| `/storytell` | **experimental** | Turns a final readout into an exec, product or data version, as a doc, chat message, email or slide outline. Never raises a claim |
| `/improve-code` | **experimental** | Reviews SQL or Python in order: intent, correctness, style, performance. Shows a diff and proves the result did not change |
| `/handoff` | **experimental** | Writes `handoff.md` so a colleague or a fresh session can pick the analysis up |

| Skill the agent applies | Status | Does |
|---|---|---|
| `viz` | **experimental** | Chart choice by question and 12 chart checks, with notes for Python, Excel, Tableau, Power BI and dashboards |
| `metric-design` | **experimental** | Defines a metric with a formula, grain, population, owner, guardrails and a trusted number |

## What makes it different

Plain models already spot visible flaws. These skills add:

- clarification before any work starts
- explicit assumptions with likely alternatives
- a data-check floor at every depth, then a validation ladder that tests the data against an independent path
- claim ceilings tied to the question type
- a review that can say "no material issues"
- a data map that learns from every analysis

## Depth

`/grill-the-ask` sets the depth. You can override it.

| | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Plus stakeholder prep questions |
| Plan | One line | 2 to 4 options | Plus power or MDE |
| Ladder | Compact data-check floor | Full floor plus full ladder | Plus alternative specification |
| Review | Self-check plus recompute | Technical plus business, best in a fresh chat | Plus leadership questions |
| Readout | Short answer in chat | `readout.md` | `readout.md` plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

## What is inside

- **Flow skills (you run them):** the 6 commands above.
- **Disciplines (the agent applies them):** `grilling`, `assumptions`, `validation-ladder`, `question-types`, `data-map`, `run-or-hand-over`.
- **Data skills (the agent applies them):** `shaping-data` (SQL, Python, Excel, Power BI, Tableau), `data-audit`, `stats-tests`.
- **Experimental (v0.2):** `/ask-data-skills`, `/wayfinder-data`, `/storytell`, `/improve-code`, `/handoff`, `viz`, `metric-design`. See the table above.

## Works with or without a data connection

If your agent can run queries, it does. In a chat app with a code tool, attach your data files (CSV, Excel) and it loads them and runs the checks itself. Only with no code tool does it hand you numbered queries, in groups, and wait for the paste. In a chat app it creates each file and offers it as a download. Every step ends with a go-ahead question. It never fails because a tool is missing.

## Your files

Everything lives in `data-work/` in your own project. The skills never write into this repo.

```
data-work/
  DATA-MAP.md
  analyses/
    2026-11-13-signup-drop/
      analysis.md     working notes, with a Progress line any new session resumes from
      readout.md      stakeholder readout (draft, then final)
      queries/
      outputs/
```

## Question types

All six question types have method cards in the `question-types` skill: descriptive, exploratory, inferential, predictive, causal (with a method selector) and mechanistic. Each card covers when to use the method, its assumptions, the checks that must pass, the common failure and the claim allowed. Advanced methods get short cards that end with "Get a specialist review before shipping." In v0.2 (experimental) the predictive file also has full cards for gradient boosting, classification metrics and calibration.

## Repo

- `skills/` the skills
- `templates/` the `analysis.md` and `readout.md` templates
- `examples/` two worked examples on invented data
- `evals/` test cases, rubrics and an eval runner (`evals/runner/`)
- `docs/` install guide, upstream map, self-check, walkthrough
- `CONTRIBUTING.md` how to add a skill or a method card
- `SPEC.md` the spec, `DECISIONS.md` the decisions

## License

MIT. See [NOTICE](NOTICE) for acknowledgements.
