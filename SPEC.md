# data-skills: spec (v0)

- Repo: `caltunay/data-skills`
- License: MIT, unless an upstream license we borrow from requires otherwise.
- Pitch: *Skills that make your AI agent work like a senior data scientist: clarify first, validate every step, never overclaim. Works in any coding agent or chat app.*
- Install: `npx skills add caltunay/data-skills`, or upload ZIPs in claude.ai and ChatGPT.

The name "datafolx" is reserved for a separate future product. Do not use it anywhere in this repo.

---

## 1. What it is

A free, open-source set of SKILL.md skills for data scientists and analysts (DSA). It is agent-agnostic. It follows one flow, from a vague stakeholder ask to a reviewed result. Some skills are slash commands the user runs (flow steps). Others are disciplines the agent applies on its own. Flow steps call disciplines by name.

The edge is not "find more flaws". Plain models already spot visible flaws. The edge is:
- clarification and grilling before any work starts
- explicit assumptions with likely alternatives
- a validation ladder before any number is trusted
- claim ceilings tied to the question type
- a business-side review that can also say "no material issues"
- a data map that learns from every analysis

Inspired by `mattpocock/skills` (structure, flow, user-invoked vs model-invoked), *The Art of Data Science* by Peng and Matsui (epicycle of analysis, question types, interpretation), and Karpathy-style working rules.

---

## 2. Principles

1. **Clarify first.** Clarification is the most important part of DSA work. Ask before you assume.
2. **Assume as little as possible.** When an assumption is unavoidable, state it, and give the most likely alternatives and their impact.
3. **Epicycle at every step.** Set an expectation, collect information, compare the expectation to the data, revise.
4. **Validation ladder.** One entity, then one entity-day, then many entities, then aggregates, then reconcile to a trusted number. Never jump straight to the final query.
5. **Claim ceilings.** A claim never goes above what its method supports. No "caused" without a causal design.
6. **Easy solution first.** Try the simplest method that could answer the question.
7. **Simplicity and surgical changes.** Minimum code. Touch only what you must.
8. **Goal-driven.** Define success checks up front. Loop until they pass.
9. **Critique the work, never the person.**
10. **Files are save points, never requirements.** Every skill works in a plain chat.
11. **Scale to the ask.** Quick asks get a quick path. Not every question needs the full flow.

---

## 3. Constraints (hard rules for every skill)

- **Standard frontmatter only:** `name` and `description`. No agent-specific keys.
- **Plain markdown.** No agent-specific tool names (no "use the Bash tool"). Say what to do, not which tool to call.
- **No reliance on subagents.**
- **Cross-skill references by name, never by path.** Installers may flatten or move folders. Write "apply the `grilling` skill", never `../grilling/SKILL.md`. Relative links are fine only inside a skill's own folder.
- **Graceful fallback.** Each flow skill restates, in one or two lines, the core rule of every discipline it calls. It must still work if that discipline does not load.
- **User-invoked skills:** the description says "Use only when the user runs /<name> or explicitly asks to <do X>." This stops accidental triggering.
- **Model-invoked skills:** the description names the concrete situations they apply to. Keep descriptions narrow so they do not clash with built-in data skills in Claude or Codex.
- **No keys or credentials.** The user's agent handles data access through its own connectors.
- **No employer material, ever.** Examples and evals use public or invented data only.
- **Skills never write into the skills repo.** All user files live in `data-work/` in the user's own project, or are handed over in chat.
- **Writing style for all skill text:** plain English, short sentences, active voice, no em dashes.
- Must work in at least: Claude Code, Codex, Gemini CLI, claude.ai chat, ChatGPT chat.

---

## 4. Lifecycle and flow

### Lifecycle (from the book plus interview-case frameworks)

| # | Stage | Covered by |
|---|---|---|
| 1 | Context and problem framing | `/grill-the-ask`, `/plan-analysis` |
| 2 | Data ingestion, auditing, pre-processing | `/run-analysis` + `data-audit`, `shaping-data` |
| 3 | Exploratory analysis | `/run-analysis` + `data-audit` |
| 4 | Modelling and estimation (branches) | `/run-analysis` + `question-types`, `stats-tests` |
| 5 | Validation and sanity checks | `/run-analysis` (ladder) + `/review-analysis` |
| 6 | Interpretation, decision, delivery | `/review-analysis` (v0); `/storytell` (v1) |
| 7 | Productionisation and monitoring | Out of scope until v2+ |

### Flow

```
/setup-data-work            (once per team or project)
        |
        v
/grill-the-ask -> /plan-analysis -> /run-analysis -> /review-analysis -> /retro-analysis
                        ^                  |
                        |__________________|
                   plan revision entry (no restart)
```

### Branches

One main flow. `/grill-the-ask` and `/plan-analysis` set the **question type**. Later steps load that type's method notes and checks from the `question-types` skill.

- v0 branches: **descriptive** and **experiment**.
- v1: causal (diff-in-diff, interrupted time series, matching), then ML.

### Cycling back

When `/run-analysis` or `/review-analysis` finds the plan cannot hold (for example, an experiment with no clean control), it does not push on. It adds a dated entry to the **Plan revisions** log in `analysis.md`, states what changed and why, and continues from the right step.

### Depth

`/grill-the-ask` sets the depth: **quick**, **standard** or **deep**. The user can override it.

| Step | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Rounds until clear, plus stakeholder prep questions |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Plan | One line: method + success check | 2 to 4 options, chosen plan | Options, chosen plan, power or MDE where relevant |
| Ladder | One entity check + reconcile | Full ladder | Full ladder + alternative specification |
| Review | Self-check against claim ceiling | Technical + business review | Full review + leadership questions |
| Files | None | `analysis.md` | Full analysis folder |

---

## 5. Environments: one path for all

Three environments, one behaviour:

| Environment | Queries | Files |
|---|---|---|
| Coding agent with data connected | Runs them | Writes to `data-work/` |
| Coding agent, no data connection | Hands them over, waits for the paste | Writes to `data-work/` |
| Chat app (claude.ai, ChatGPT) | Hands them over, waits for the paste | Offers a download, else prints a block to copy |

The `run-or-hand-over` discipline defines this. **Rule:** run it or save it if you can; otherwise offer a download; otherwise print it and wait. Never fail because a tool is missing.

Copy-paste form for queries: numbered (`Q2.1`, `Q2.2`), each with one purpose line, the expected result stated before it runs, and "Paste the result here." Keep each check query small.

---

## 6. Skill catalogue

### 6.1 Flow skills (user-invoked, v0)

| Skill | Trigger | Inputs | Does | Writes | Calls |
|---|---|---|---|---|---|
| `/setup-data-work` | User runs it, once per team or project | Nothing, or an existing `DATA-MAP.md` | Tests data access. Points to the agent's connector directory if there is none. Interviews the user (see section 8). Can be partial; the map fills in over time. Target: under 20 minutes. | `data-work/DATA-MAP.md`, `.gitignore` entry | grilling, data-map, run-or-hand-over |
| `/grill-the-ask` | User runs it with a stakeholder ask | The ask, `DATA-MAP.md` if present | Rounds of max 3 questions, each with options and a recommended default. Covers goal, the decision it feeds, question type, metric, population, time window, constraints, deadline. Sets the depth. | `analysis.md`: Meta, Ask, Assumptions | grilling, assumptions, question-types, data-map |
| `/plan-analysis` | User runs it after grilling | `analysis.md` | 2 to 4 options with trade-offs, then the chosen plan. Writes the analysis table spec. Sets success checks. Records decisions already made; does not invent new ones. | `analysis.md`: Plan, Analysis table spec | assumptions, question-types, shaping-data |
| `/run-analysis` | User runs it after the plan | `analysis.md`, `DATA-MAP.md` | Builds the analysis table from the spec, climbing the validation ladder. States the expected result before each query. Audits the data. Runs the method for the question type. Asks instead of assuming. Adds plan revisions when needed. | `analysis.md`: Results; `queries/`; `outputs/` | validation-ladder, run-or-hand-over, shaping-data, data-audit, stats-tests, question-types, data-map, assumptions |
| `/review-analysis` | User runs it on a finished analysis (theirs or anyone's) | `analysis.md` or any pasted analysis | Technical review and business review. Checks claims against the ceiling. Checks assumption status. Gives a verdict. Writes questions leadership will ask, with answers. Says "no material issues" when that is true. | `analysis.md`: Review | question-types, assumptions, validation-ladder |
| `/retro-analysis` | User runs it at the end | `analysis.md`, `DATA-MAP.md` | Proposes dated changes to the data map: new joins, traps, filters, definitions, trusted numbers, gotchas. Shows a diff. The user approves each change. Not a memory dump. | `DATA-MAP.md` (approved changes only) | data-map |

### 6.2 Disciplines (model-invoked, v0)

| Skill | Applies when | Core rule (restate in each caller) |
|---|---|---|
| `grilling` | Any clarification step | Rounds of at most 3 questions, each with 2 to 4 options and a recommended default. Wait for answers. Never assume silently. |
| `assumptions` | An assumption is about to be made | Write it in the assumptions table. High-impact rows need 1 to 3 likely alternatives. |
| `validation-ladder` | Before trusting any query or analysis result | One entity -> one entity-day -> many entities -> aggregates -> reconcile to a trusted number. State the expected result before each rung. |
| `question-types` | Framing, planning, writing claims, reviewing | Six question types and their claim ceilings. Holds method notes per branch: `descriptive.md` and `experiment.md` in v0 (SRM, A/A, novelty, power, MDE, runtime, seasonality, unit of randomisation). |
| `data-map` | Reading or updating `DATA-MAP.md` | Read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask. Updates only through approved retro changes. Check the format version and offer a migration if old. |
| `run-or-hand-over` | Any query to run or file to save | Run or save if you can, else offer a download, else print it and wait. Numbered queries in copy-paste form. |

### 6.3 Data skills (model-invoked, v0; our own versions)

| Skill | Applies when | Contents |
|---|---|---|
| `shaping-data` | Getting data into shape for an analysis, in any tool | `SKILL.md`: the tool-agnostic part. First design the **analysis table spec** (section 7.4). Then: grain first, join fan-out checks with row-count asserts, filters from `DATA-MAP.md`, tidy (long) vs wide and why, explicit named steps. Tool files: `sql.md` (dialect from `DATA-MAP.md`, sqlstyle.guide defaults), `python.md` (pandas or polars, PEP 8), `excel.md` (formulas, pivots, Power Query), `powerbi.md` (DAX, relationships), `tableau.md` (calculated fields, LOD expressions). Read only the file for the tool in use. Excel, Power BI and Tableau always run in hand-over mode. |
| `data-audit` | A new table, file or extract | Source inventory, shape and n, top and bottom rows, missingness, cardinality, duplicates, outliers, date coverage, external validation against a trusted number. Cleaning choices are written down, not silent. |
| `stats-tests` | Choosing or interpreting a statistical test | Test choice by data type and design, assumptions of the test, power and MDE, multiple comparisons, interpretation as direction, magnitude and uncertainty. Practical vs statistical significance. |

### 6.4 v1 and later

- **Off-flow (v1):** `/ask-data-skills` (router), `/wayfinder-data` (map big, ambiguous work as decision tickets), `/handoff`, `/improve-code` (review and refactor SQL or Python), `/storytell` (narrative by audience), `/viz`.
- **Branches (v1):** causal, then ML.
- **Rest of the upstream inventory (v1).**
- **Automated eval runner (v1).**
- **Productionisation and monitoring (v2+).**

---

## 7. Workspace files

### 7.1 Layout

All user-owned files live in the user's own project, never in the skills repo. Updating the skills never touches them.

```
<user project>/data-work/
  DATA-MAP.md
  analyses/
    2026-11-13-refund-drop/
      analysis.md
      queries/        numbered ladder steps (q1-1-one-entity.sql ...)
      outputs/        charts, tables, notebooks
```

- **Coding agents:** the skills write here.
- **Chat users:** keep `DATA-MAP.md` in the chat app's Project files. The analysis lives in the chat; `analysis.md` is offered as a download at the end, not forced. `/retro-analysis` hands back a full updated `DATA-MAP.md` to replace the Project file.
- **Quick depth:** no files.
- **No raw chat transcripts are stored.** `analysis.md` is the record.

### 7.2 `DATA-MAP.md`

One file with fixed sections. The first line is the format version: `format: v1`. When a skill finds an older format, it offers a migration and shows the changes first.

Sections:
1. **Sources:** name, type (warehouse, lake, sheet, file, API, cube), dialect (Postgres, SQL Server, BigQuery, Snowflake...), access mode (connected or hand-over).
2. **Tables:** table, what one row means (grain), primary key, key columns, notes.
3. **Joins:** safe joins with keys, fan-out traps.
4. **Metrics:** canonical definition, logic, trusted numbers (value, period, where it comes from).
5. **Rules:** mandatory filters, business rules, exclusions.
6. **Gotchas:** past mistakes and how to avoid them.
7. **Glossary:** business terms and what they map to in the data.
8. **Conventions:** SQL style, Python style, team overrides of the defaults.

Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.

**Staleness:** when a skill relies on an entry older than 90 days, or one the data contradicts, it says so and asks before using it.

Shared by the team: committed to git where there is a repo, so every retro improves it for everyone.

### 7.3 `analysis.md`

First line: `format: v1`. Sections, filled by step:

1. **Meta:** title, requester, date, depth, question type, status.
2. **Ask:** the original ask verbatim, the clarified question, the decision it feeds, constraints, deadline. *(grill)*
3. **Assumptions:** table, see 7.5. *(grill, then any step)*
4. **Plan:** options considered, chosen plan, success checks. **Plan revisions** log: date, what changed, why. *(plan)*
5. **Analysis table spec:** see 7.4. *(plan)*
6. **Results:** ladder log (each rung: expected, actual, pass or fail), findings as direction, magnitude, uncertainty, and the claim ceiling applied. Aggregates only by default. *(run)*
7. **Review:** verdict, technical issues, business issues, leadership questions with answers. *(review)*
8. **Retro:** proposed data map changes and which were accepted. *(retro)*

Every skill reads `analysis.md` first, so a fresh session can pick up without re-asking.

### 7.4 Analysis table spec

Designed before any query or code, without reference to a tool:
- what one row means (grain)
- keys
- measures and dimensions
- time column and window
- filters and exclusions (from `DATA-MAP.md`)
- tidy/long vs wide, and why for this question
- context columns needed to interpret results
- expected row count or range

`/run-analysis` builds from it. `/review-analysis` checks results against it.

### 7.5 Assumptions table

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | Refunds are counted on refund date, not booking date | Stakeholder unavailable until Friday | Booking date; payment settlement date | High: shifts monthly totals by about 10% | Ask finance; compare both definitions for one month | open |

- Status: `open`, `confirmed` or `rejected`.
- Alternatives are required for high-impact rows only.
- `/review-analysis` flags any high-impact row still `open` when results are reported.

### 7.6 Data safety

- `/run-analysis` shows aggregates by default and asks before saving row-level data anywhere.
- `/setup-data-work` asks whether `outputs/` should be committed. The default adds `data-work/analyses/*/outputs/` to `.gitignore`.

---

## 8. Onboarding: `/setup-data-work`

Rounds of max 3 questions. Partial answers are fine; the map grows through retros.

1. **Access test:** "Can you run a query from here?" If yes, run a trivial test (`select 1`). If no, tell the user once to check their agent's connector directory for their source; if it is missing or blocked by company policy, continue in hand-over mode. No dead ends.
2. **Sources:** which sources, type, and dialect for each.
3. **Key tables:** the 3 to 10 tables used most, grain and keys for each.
4. **Joins:** the joins they trust, and any known fan-out traps.
5. **Metrics:** the 3 to 5 most-used metrics, their definitions, and one trusted number each (for reconciling).
6. **Rules:** mandatory filters (test accounts, cancelled orders, time zones).
7. **Conventions:** "Does your team have SQL or Python conventions? If not, I'll use sqlstyle.guide and PEP 8."
8. **Git policy:** commit `outputs/` or not (default: not).

Then write `DATA-MAP.md` and show a short summary of what is still missing.

---

## 9. Connectors

- We ship no connector code and no connector recipes.
- Rely on each agent's own connector marketplace (Claude connectors directory, ChatGPT and Codex connectors, and others).
- Admin gates are company policy, not our problem. Hand-over mode covers every case where a connector is missing or blocked.
- Setup may suggest: "If you have a web search or docs lookup tool, check the current setup steps for your agent and source." Optional, never required.

---

## 10. Question types and claim ceilings

| Type | Asks | Allowed claims | Not allowed |
|---|---|---|---|
| Descriptive | What happened? | "was", "is", counts, rates for the data observed | Generalising beyond the data; "why" |
| Exploratory | What patterns are there? | "we see", "pattern worth testing" | "drives", "causes", confirmed findings |
| Inferential | Does it hold beyond this sample? | "associated with", with uncertainty | "causes" |
| Predictive | What will happen for a new case? | "predicts", with out-of-sample performance | Explaining why; "causes" |
| Causal | What happens if we change X? | "caused", "effect of" only with a randomised experiment or a credible causal design that passed its checks | Causal language from observational data without a design |
| Mechanistic | How exactly does it work? | Rarely reachable in business DSA; flag it | Most claims |

Reuse the existing question-type ceilings and must-answer questions from `caltunay/datafolx` where they fit, rewritten in this repo's style.

---

## 11. Validation ladder

1. **One entity:** follow one customer, order or ticket end to end. Check every column by hand.
2. **One entity-day:** one entity over one day or period. Check the time logic.
3. **Many entities:** a small sample. Check duplicates, nulls and join fan-out (row counts before and after each join).
4. **Aggregates:** the full query. Check totals, distributions and edge periods.
5. **Reconcile:** compare to a trusted number from `DATA-MAP.md` or the stakeholder. Explain any gap above a stated tolerance.

Before each rung, state the expected result. After it, record the actual result and pass or fail in `analysis.md`. Quick depth runs rung 1 and rung 5 only.

---

## 12. Review standard (`/review-analysis`)

- **Technical:** data, joins, filters, method, tests, ladder log, analysis table spec match, uncertainty.
- **Business:** does it answer the decision? Is the effect practically meaningful? Guardrails, cost and risk, what a sceptical leader will ask.
- **Claims:** every claim checked against the question-type ceiling.
- **Assumptions:** any high-impact open row flagged.
- **Verdict:** `ready`, `ready with caveats`, or `needs rework`, with the reasons.
- **Precision matters:** if there are no material issues, say so plainly. Do not invent issues.
- Reuse the review protocol, technical review, business review and methods files from `caltunay/datafolx` where they fit.

---

## 13. Style defaults

- **SQL:** sqlstyle.guide (Simon Holywell) by default. Summarise its rules in our own words with a link; check its license before quoting. Dialect comes from `DATA-MAP.md`.
- **Python:** PEP 8.
- **Team overrides:** the Conventions section of `DATA-MAP.md` wins over the defaults.

---

## 14. Upstream reuse

Build our own versions of data skills so the repo works in every agent. Do not depend on built-in data skills.

1. Read the licenses of:
   - `anthropics/knowledge-work-plugins` (the `data` plugin)
   - `openai/plugins` (`plugins/data-analytics`)
2. Write `docs/upstream-map.md`: for each upstream skill, what it does, source repo, overlaps, verdict (`absorbed into <our skill>`, `v1 backlog`, `drop`) and why.
3. Add attribution in `NOTICE` if any license requires it.
4. v0 rebuilds only what the flow needs. Strip all harness-specific references (shared skills, tool names, connector placeholders).
5. Descriptions stay narrow so ours and the built-ins do not fire on the same generic ask. Inside the flow, ours are called by name.

---

## 15. Testing

Pre-release check, run by the maintainer:

- Each flow skill gets **3 eval cases**: 2 with planted flaws or ambiguities, 1 clean case (to test precision: "no material issues" or "no questions needed").
- A written rubric per case in `evals/`: what a pass looks like.
- Run by hand in Claude Code, Codex, Gemini CLI and claude.ai. Record results in `evals/results/<date>-<agent>.md`.
- Plus 3 real asks on public data, end to end.
- Reuse the existing planted-flaw cases from `caltunay/datafolx` where they fit. Public or invented data only.
- Also check triggering: user-invoked skills must not fire on their own, and disciplines must fire when they should.

---

## 16. Repo layout

```
data-skills/
  README.md            pitch, the flow, the 6 commands, install, depth
  LICENSE              MIT
  NOTICE               upstream attribution, if required
  SPEC.md              this file
  DECISIONS.md         design decisions + build decisions
  skills/
    setup-data-work/SKILL.md
    grill-the-ask/SKILL.md
    plan-analysis/SKILL.md
    run-analysis/SKILL.md
    review-analysis/SKILL.md
    retro-analysis/SKILL.md
    grilling/SKILL.md
    assumptions/SKILL.md
    validation-ladder/SKILL.md
    question-types/SKILL.md, descriptive.md, experiment.md
    data-map/SKILL.md, DATA-MAP.template.md
    run-or-hand-over/SKILL.md
    shaping-data/SKILL.md, sql.md, python.md, excel.md, powerbi.md, tableau.md
    data-audit/SKILL.md
    stats-tests/SKILL.md
  templates/
    analysis.template.md
  evals/
    <skill>/case-1.md, case-2.md, case-3.md, rubric.md
    results/
  docs/
    install.md         Claude Code, Codex, Gemini CLI, Cursor, Copilot, claude.ai, ChatGPT
    upstream-map.md
  scripts/
    package-zips       one ZIP per skill for chat-app upload
```

Flat `skills/<name>/` unless the installer handles nesting well (see section 18). `templates/analysis.template.md` may move inside a skill folder if the installer only copies skill folders; log the choice.

---

## 17. Release cut

### v0 (this build): 15 skills
- Flow: `setup-data-work`, `grill-the-ask`, `plan-analysis`, `run-analysis`, `review-analysis`, `retro-analysis`
- Disciplines: `grilling`, `assumptions`, `validation-ladder`, `question-types`, `data-map`, `run-or-hand-over`
- Data: `shaping-data` (5 tool files), `data-audit`, `stats-tests`
- Plus: templates, `docs/upstream-map.md`, `docs/install.md`, evals for the 6 flow skills, ZIP packaging, README.

### v1
Router, wayfinder, handoff, improve-code, storytell, viz; causal and ML branches; rest of the upstream inventory; automated eval runner; split Conventions into its own file if it grows.

### v2+
Productionisation and monitoring, as off-flow skills.

---

## 18. Open items for the builder

Decide these, then log each choice and reason in `DECISIONS.md`:
1. Does `npx skills add` discover nested skill folders? If unsure, use flat `skills/<name>/`.
2. Where do templates live so they install with the skills? (Likely inside the `data-map` and `run-analysis` skill folders.)
3. Exact upstream license terms and attribution needed.
4. sqlstyle.guide license and how much can be quoted.
5. Plugin manifests for Claude Code and Codex: add only if trivial; otherwise v1.
6. Exact wording of each skill description, tuned to avoid clashes with built-in data skills.

---

## 19. Design decisions (seed for `DECISIONS.md`)

1. Build our own data skills, phased. Flow skills call ours by name. Descriptions avoid clashing with built-ins.
2. One main flow. The plan sets the question type; later steps load its checks. v0 branches: descriptive and experiment.
3. Cycling back adds a dated plan revision entry, no restart.
4. Upstream: inventory both repos and check licenses first. v0 rebuilds only what the flow needs.
5. One path for connected and copy-paste use: `run-or-hand-over` covers queries and files.
6. Productionisation and monitoring: out of scope until v2+.
7. Connectors: rely on each agent's marketplace. No recipes. Hand-over mode covers gaps and admin blocks.
8. One `DATA-MAP.md` with fixed sections, including Conventions. Format version on line 1, with migrations.
9. Every data map entry has a verified date and source. Retro proposes, the user approves. Flag entries older than 90 days or contradicted by data.
10. User files live in `data-work/` in the user's project, committed and shared by the team. Never in the skills repo.
11. One folder per analysis: `analysis.md`, `queries/`, `outputs/`. No raw chat transcripts.
12. Assumptions: a table with alternatives required for high-impact rows.
13. `outputs/` git policy chosen at setup, default excluded. Aggregates by default; ask before saving row-level data.
14. Chat apps are first-class: skills install by upload in claude.ai and ChatGPT. `DATA-MAP.md` lives in the chat app's Project files.
15. Depth (quick, standard, deep) set by `/grill-the-ask`.
16. `shaping-data`: one skill, a tool-agnostic core (analysis table spec) plus one file per tool. All five tools in v0.
17. Style: sqlstyle.guide and PEP 8 by default; team overrides in Conventions; dialect per source in `DATA-MAP.md`.
18. v0 is 15 skills. Router and other off-flow skills in v1.
19. Testing: 3 eval cases per flow skill (2 flawed, 1 clean), run by hand in 4 agents, plus 3 real asks on public data.
20. Names: repo `caltunay/data-skills`; commands `/setup-data-work`, `/grill-the-ask`, `/plan-analysis`, `/run-analysis`, `/review-analysis`, `/retro-analysis`. "datafolx" is reserved for another product.
