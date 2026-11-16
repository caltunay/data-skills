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

## What makes it different

Plain models already spot visible flaws. These skills add:

- clarification before any work starts
- explicit assumptions with likely alternatives
- a validation ladder before any number is trusted
- claim ceilings tied to the question type
- a review that can say "no material issues"
- a data map that learns from every analysis

## Depth

`/grill-the-ask` sets the depth. You can override it.

| | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Plus stakeholder prep questions |
| Plan | One line | 2 to 4 options | Plus power or MDE |
| Ladder | One entity plus reconcile | Full | Full plus alternative specification |
| Review | Self-check | Technical plus business | Plus leadership questions |
| Readout | Short answer in chat | `readout.md` | `readout.md` plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

## What is inside

- **Flow skills (you run them):** the 6 commands above.
- **Disciplines (the agent applies them):** `grilling`, `assumptions`, `validation-ladder`, `question-types`, `data-map`, `run-or-hand-over`.
- **Data skills (the agent applies them):** `shaping-data` (SQL, Python, Excel, Power BI, Tableau), `data-audit`, `stats-tests`.

## Works with or without a data connection

If your agent can run queries, it does. If not, it hands you numbered queries and waits for the paste. It never fails because a tool is missing.

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
- `evals/` test cases and rubrics
- `docs/` install guide, upstream map, self-check
- `SPEC.md` the spec, `DECISIONS.md` the decisions

## License

MIT. See [NOTICE](NOTICE) for acknowledgements.
