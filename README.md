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

Codex also has a plugin manifest. Or upload the ZIPs in claude.ai and ChatGPT. See [docs/install.md](docs/install.md). Where your files live, in a coding agent or a chat Project: [docs/where-to-run.md](docs/where-to-run.md).

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

## Which command do I start with?

| The ask looks like | Use |
|---|---|
| A project: several questions, unknowns, weeks of work | `/wayfinder-data` |
| A design with no data needed yet (experiment, measurement) | `/wayfinder-data` (fast path) |
| One question with a decision attached | `/grill-the-ask` and the flow |
| Not sure | `/ask-data-skills` |

`/grill-the-ask` sends project-sized asks and design asks to `/wayfinder-data` with one line why.

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
| `/wayfinder-data` | **experimental** | Maps big, vague work as decision items, settles them one at a time, and ends with ready `/grill-the-ask` prompts. Also designs an experiment or a metric (`experiment-spec.md`, `metric-spec.md`) with no project map |
| `/storytell` | **experimental** | The story discipline of the readout: `/run-analysis` uses it to draft the readout as a story and `/review-analysis` uses it to check the story. Run directly, it turns a final readout into an exec, product or data version, as a doc, chat message, email or slide pack. Never raises a claim |
| `/improve-code` | **experimental** | Reviews SQL or Python in order: intent, correctness, style, performance. Shows a diff and proves the result did not change |

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
| Plan | One line, flat hypotheses | Hypothesis tree, 2 to 4 options | Plus power or MDE |
| Ladder | Compact data-check floor | Full floor plus full ladder | Plus alternative specification |
| Review | Self-check plus recompute | Technical plus business, best in a fresh chat | Plus leadership questions |
| Readout | Short answer in chat | `readout.md` and `readout.docx` | Plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

## What is inside

- **Flow skills (you run them):** the 6 commands above.
- **Disciplines (the agent applies them):** `grilling`, `assumptions`, `validation-ladder`, `question-types`, `data-map`, `run-or-hand-over`.
- **Data skills (the agent applies them):** `shaping-data` (SQL, Python, Excel, Power BI, Tableau), `data-audit`, `stats-tests`.
- **Experimental (v0.2):** `/ask-data-skills`, `/wayfinder-data`, `/storytell`, `/improve-code`, `viz`, `metric-design`. See the table above.

## Works with or without a data connection

If your agent can run queries, it does. In a chat app with a code tool, attach your data files (CSV, Excel) and it loads them and runs the checks itself. Only with no code tool does it hand you numbered queries, in groups, and wait for the paste. In a chat app it saves each file to your Project files at its full path, or offers a download and tells you where to add it. Every step ends with a go-ahead question. It never fails because a tool is missing.

## Your files

Everything lives in `data-work/` in your own project. The skills never write into this repo. In a chat app, use one Project per team or area and one chat per analysis. See [docs/where-to-run.md](docs/where-to-run.md).

```
data-work/
  DATA-MAP.md
  analyses/
    2026-11-13-signup-drop/
      analysis.md     working notes, with a Progress line any new session resumes from
      readout.md      stakeholder readout (skeleton, draft, then final)
      readout.docx    the same text with the charts, for Word and Google Docs
      experiment-spec.md or metric-spec.md   (design asks)
      scripts/        every script behind a number, a check or a chart (any environment)
      outputs/        (coding agents; in a chat app charts sit in the analysis folder as SVG)
```

## Using data-skills in a chat app

These steps are for claude.ai and ChatGPT. Coding agents need none of this: they save your files in the repo.

1. **Create a Project** per team or area.
2. **Upload the skills.** Add the ZIPs from the latest release (see [docs/install.md](docs/install.md)).
3. **Run `/setup-data-work`.** At the end it gives you a short block. Paste it into the Project instructions.
4. **Use one chat per analysis.** Start with `/grill-the-ask` and follow the go-ahead question at the end of each step.
5. **Your files live in `data-work/` in the Project files.** Every step ends by telling you which files changed and where they are. It says "Saved to `<path>` in your Project files" or "Download `<file>`".
6. **If the app cannot save to the Project,** it says "Download `<file>`". Download it and attach it to the next chat when a step needs it. The skill never asks you to move a file into a Project folder. Never edit a file by hand: the skill hands back the whole file.
7. **Many analyses in one Project are fine.** A new ask that matches an old one asks you: continue it, or start a new analysis.
8. **Old files at the top level or in a `claude/` folder** are stale. The skill names them by full path.

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
