# data-skills: spec (v0.4)

v0.1 adds: connector rules, data map check, chat-app handoff, readout, progress tracker, method cards for all question types, neutral example domain. See section 19, decisions 21 to 32.

v0.2 adds the experimental skills in section 20. v0.3 is a fix pass from a full manual run: see section 21 and decisions 47 onward. v0.4 fixes the v0.3 live run and adds a hypothesis tree, strategy context, design asks, routing and chat-first storage: see section 22 and decisions 65 onward.

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
4. **Validation ladder.** A data-check floor at every depth, then one entity, one entity-day, many entities, aggregates, and reconcile to a trusted number. Every check tests the data against an independent path. Never jump straight to the final query.
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
- **One neutral example domain:** an invented online shop and subscription app (orders, customers, subscriptions, sign-ups, returns). Use no other domain in examples or evals.
- **Private blocklist:** `scripts/self-check` also reads banned words from a gitignored `.blocklist` file, so the banned words never appear in the public repo.
- **Never touch a data tool before the user names the source.** No connector or data tool call until the user has named the source it applies to. Never build answer options from the connectors you can see. Use generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- **Never fill in names the user has not said.** No company, product, table or source name that the user has not said in this conversation, even if you know it from elsewhere (memory, profile, connectors). Ask instead.
- **Skills never write into the skills repo.** All user files live in `data-work/` in the user's own project, or are handed over in chat.
- **Writing style for all skill text:** plain English, short sentences, active verbs, no em dashes.
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
                        ^                  |                 |
                        |__________________|                 |
                   plan revision entry       draft readout.md -> final readout.md
```

### Every flow step starts the same way

1. Check for `DATA-MAP.md` and `analysis.md`. Say in one line what was found.
2. Look for `data-work/` in the current folder, then upward. If more than one map is found, the nearest one wins for conflicts. Say which map you read.
3. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Record the choice in Meta as `Setup choice`. Never offer setup again once it is set. `/retro-analysis` never offers setup: it builds the map itself.
4. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything.
5. Read the Progress line and resume from it.

### Every flow step ends the same way

At every depth, quick included, each flow step ends with a go-ahead question in a fixed form, adapted to the step:

> Go ahead?
> A) Yes, run `<next command>`
> B) Change something (say what)
> C) Add a check, segment or question

B or C means the step makes the change, hands back the updated file, and asks again. `/retro-analysis` adapts A to close the analysis and start the next ask.

### Every question has a real default

Every question in every step has one real recommended default with a one-line reason. No hedges such as "C if unknown". The deadline question gets a default too.

### Goal-driven run

`/run-analysis` states its goal at the start: "Done when the success checks in the plan pass and a draft readout is written." It then keeps working step after step, and stops only to wait for a paste or an answer. This needs no agent-specific goal feature.

### Branches

One main flow. `/grill-the-ask` and `/plan-analysis` set the **question type**. Later steps load that type's method notes and checks from the `question-types` skill.

- v0: **descriptive** and **experiment**.
- v0.1: all six types have method cards (section 10). Advanced causal methods get short cards with a specialist-review flag.
- v1: ML beyond baselines.

### Cycling back

When `/run-analysis` or `/review-analysis` finds the plan cannot hold (for example, an experiment with no clean control), it does not push on. It adds a dated entry to the **Plan revisions** log in `analysis.md`, states what changed and why, and continues from the right step. Every spec correction found during the run (for example, "6 channels expected, 5 found") is also a dated row. No "(none)" line followed by notes.

### Depth

`/grill-the-ask` sets the depth: **quick**, **standard** or **deep**. The user can override it.

| Step | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Rounds until clear, plus stakeholder prep questions |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Hypotheses | Flat list, up to 3 | Tree, at most 3 levels and about 12 nodes | Same as standard |
| Plan | One line: method + success check | 2 to 4 options, chosen plan | Options, chosen plan, power or MDE where relevant |
| Ladder | Compact data-check floor (never skipped) | Full floor + full ladder | Full floor + full ladder + alternative specification |
| Review | Self-check against claim ceiling | Technical + business review | Full review + leadership questions |
| Readout | Short answer in chat | `readout.md` | `readout.md` plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

---

## 5. Environments: one path for all

Three environments, one behaviour:

| Environment | Queries | Files |
|---|---|---|
| Coding agent with data connected | Runs them | Writes to `data-work/` |
| Coding agent, no data connection | Hands them over, waits for the paste | Writes to `data-work/` |
| Chat app with a code tool and attached data files | Loads the files and runs the checks (DuckDB, SQLite or pandas) | Creates the file, offers a download |
| Chat app, data in a source with no connection | Hands them over, waits for the paste | Creates the file, offers a download |
| Chat app with no code tool | Hands them over, says so in one line | Prints a block to copy |

The `run-or-hand-over` discipline defines this. It asks two separate questions.

- **Can I run things here?** Always try first. A code tool or sandbox with attached files counts: load them and run SQL (DuckDB or SQLite) or pandas. Only hand over when no code tool exists, and say so in one line. Never say "I can't run code" when a code tool exists.
- **Where do files persist?** In a chat app, create each file in the sandbox and offer it as a download. Print it as a block only if creating the file fails. Never say "I can't save files" when a download can be made.

Never fail because a tool is missing.

**What counts as a chat app:** decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), it is a chat app. This decides where files persist, not whether the agent can run checks.

**Chat-app handoff:** at the end of every flow step, create the updated `analysis.md` (and `readout.md` when it exists) as files and offer them as downloads; print one block only if that fails. Tell the user to save them to their Project files so the next step, in any chat, can read them.

**No manual file edits:** after the user confirms something, never ask them to edit a saved file by hand. Hand back the updated file.

**Method cards without file access:** `question-types/SKILL.md` holds a compact line per method (when to use, checks that must pass, claim allowed), so the cards work even when the type files cannot be opened. `/plan-analysis` copies the card's checks into the success checks at plan time and never defers them.

**Progress tracker:** `analysis.md` Meta keeps one line, for example `Progress: run step 3 of 7, waiting for Q3.1 paste`. Every step updates it. Any new session resumes from it.

Copy-paste form for queries: numbered (`Q2.1`, `Q2.2`), each with one purpose line, the expected result stated before it runs, and "Paste the result here." Keep each check query small. Batch several checks into numbered groups so the user pastes once per group.

---

## 6. Skill catalogue

### 6.1 Flow skills (user-invoked, v0)

| Skill | Trigger | Inputs | Does | Writes | Calls |
|---|---|---|---|---|---|
| `/setup-data-work` | User runs it, once per team or project | Nothing, or an existing `DATA-MAP.md` | First asks for a map from another project on the same data, then asks how the user wants to set up the map (section 8). Tests access only against a source the user named. Points to the agent's connector directory if there is none. Interviews the user, including goals, funnels, key queries and how the team organises its files. In a chat app ends with a block to paste into the Project instructions. Can be partial; the map fills in over time. Target: under 20 minutes. | `data-work/DATA-MAP.md`, `.gitignore` entry | grilling, data-map, run-or-hand-over |
| `/grill-the-ask` | User runs it with a stakeholder ask | The ask, `DATA-MAP.md` if present | Rounds of max 3 questions, each with options and a recommended default. Covers goal, the decision it feeds, requester, question type, metric, population, time window, constraints, deadline, and who reads the result (audience). When periods are compared, recommends a comparison that handles seasonality (year on year, or the same weekdays), or flags that the recommended option ignores it. Sets the depth with a one-line reason. Never asks the same question twice. Never analyses: with files attached it notes only columns, possible duplicates and the date range. Logs every answer word for word in Decisions and echoes it back. On a conflicting or senseless answer, says so and asks one question at a time. Asks how the ask links to a goal. Sends design asks and project-sized asks to `/wayfinder-data` with one line why. | `analysis.md`: Meta, Ask, Decisions, Assumptions | grilling, assumptions, question-types, data-map |
| `/plan-analysis` | User runs it after grilling | `analysis.md` | Writes a hypothesis tree (section 7.9) before the method options. 2 to 4 options with trade-offs, then the chosen plan. Writes the analysis table spec. Sets success checks. Optionally drafts a readout skeleton with placeholders only. Records decisions already made; does not invent new ones. | `analysis.md`: Hypotheses, Plan, Analysis table spec; `readout.md` (skeleton, optional) | assumptions, question-types, shaping-data |
| `/run-analysis` | User runs it after the plan | `analysis.md`, `DATA-MAP.md` | Builds the analysis table from the spec, climbing the validation ladder. States the expected result before each query. Audits the data. Runs the method for the question type. Asks instead of assuming. Adds plan revisions when needed. States its goal up front and keeps going until it is met. Updates hypothesis statuses. Writes a draft readout (replacing any skeleton) and a `.docx` copy. | `analysis.md`: Results, Hypotheses, Progress; `readout.md` (draft); `readout.docx`; `queries/`; `outputs/` | validation-ladder, run-or-hand-over, shaping-data, data-audit, stats-tests, question-types, data-map, assumptions |
| `/review-analysis` | User runs it on a finished analysis (theirs or anyone's) | `analysis.md` or any pasted analysis | Technical review and business review. Checks claims against the ceiling. Checks assumption status. Gives a verdict. Writes questions leadership will ask, with answers. Says "no material issues" when that is true. Checks the hypothesis statuses and the decisions log. Reviews the draft readout word by word, fixes claims above the ceiling, marks it final and rebuilds the `.docx`. | `analysis.md`: Review; `readout.md` (final); `readout.docx` | question-types, assumptions, validation-ladder |
| `/retro-analysis` | User runs it at the end | `analysis.md`, `DATA-MAP.md` | Proposes dated changes to the data map: new joins, traps, filters, definitions, trusted numbers, gotchas. Puts each in the right section (Conventions are style only) with no duplicates. Each reason must be true for this run, shown by a line in `analysis.md`. Shows a diff. The user approves each change. Proposes additions to Funnels and Key queries. One entry per source; grain under Tables. Never offers setup: it builds the map itself. Not a memory dump. | `DATA-MAP.md` (approved changes only) | data-map |

### 6.2 Disciplines (model-invoked, v0)

| Skill | Applies when | Core rule (restate in each caller) |
|---|---|---|
| `grilling` | Clarification of a data ask only (analysis, metric, query, report, experiment). Never fires on non-data asks. | Rounds of at most 3 questions, each with 2 to 4 options and one real recommended default (never a hedge, the deadline included). Wait for answers. Never assume silently. |
| `assumptions` | An assumption is about to be made | Write it in the assumptions table. High-impact rows need 1 to 3 likely alternatives. |
| `validation-ladder` | Before trusting any query or analysis result | One entity -> one entity-day -> many entities -> aggregates -> reconcile to a trusted number. State the expected result before each rung. |
| `question-types` | Framing, planning, choosing a method, writing claims, reviewing | Six question types and their claim ceilings. `SKILL.md` holds the type selector and the causal method selector. One file per type holds that type's method cards (section 10). Load only the file for the type in use. |
| `data-map` | Reading or updating `DATA-MAP.md` | Outside the flow, stay silent if there is no map. Read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask. Updates only through approved retro changes. Check the format version and offer a migration if old. |
| `run-or-hand-over` | Any query to run or file to save | Two questions. Can I run it here? Always try first; a code tool with attached files counts. Where do files persist? In a chat app, create the file and offer a download; print only if that fails. Numbered queries in copy-paste form, batched in groups. Never call a data tool before the user names the source. |

### 6.3 Data skills (model-invoked, v0; our own versions)

| Skill | Applies when | Contents |
|---|---|---|
| `shaping-data` | Getting data into shape for an analysis, in any tool | `SKILL.md`: the tool-agnostic part. First design the **analysis table spec** (section 7.4). Then: grain first, join fan-out checks with row-count asserts, filters from `DATA-MAP.md`, tidy (long) vs wide and why, explicit named steps. Tool files: `sql.md` (dialect from `DATA-MAP.md`, sqlstyle.guide defaults), `python.md` (pandas or polars, PEP 8), `excel.md` (formulas, pivots, Power Query), `powerbi.md` (DAX, relationships), `tableau.md` (calculated fields, LOD expressions). Read only the file for the tool in use. Excel, Power BI and Tableau always run in hand-over mode. |
| `data-audit` | A new table, file or extract | Source inventory, shape and n, top and bottom rows, missingness, cardinality, duplicates, outliers, date coverage, external validation against a trusted number. Cleaning choices are written down, not silent. |
| `stats-tests` | Choosing or interpreting a statistical test | Test choice by data type and design, assumptions of the test, power and MDE, multiple comparisons, interpretation as direction, magnitude and uncertainty. Practical vs statistical significance. |

### 6.4 v1 and later

- **Off-flow (v1):** `/ask-data-skills` (router), `/wayfinder-data` (map big, ambiguous work as decision items), `/handoff`, `/improve-code` (review and refactor SQL or Python), `/storytell` (narrative by audience), `/viz`.
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
    2026-11-13-signup-drop/
      analysis.md     working notes
      readout.md      stakeholder readout (source; skeleton, draft, then final)
      readout.docx    the same text with charts embedded, for Word and Google Docs
      queries/        numbered ladder steps (q1-1-one-entity.sql ...)
      outputs/        charts, tables, notebooks
```

- **Coding agents:** the skills write here. They look for `data-work/` in the current folder, then upward. A team map can sit above project maps. The nearest map wins for conflicts, and the skill says which map it read.
- **Chat users:** keep `DATA-MAP.md`, `analysis-<slug>.md` and `readout-<slug>.md` in the chat app's Project files (see section 7.8). Each flow step creates the updated files and offers them as downloads at its end. `/retro-analysis` hands back a full updated `DATA-MAP.md` to replace the Project file. The user never edits a saved file by hand.
- **Quick depth:** no files.
- **No raw chat transcripts are stored.** `analysis.md` is the record.

### 7.2 `DATA-MAP.md`

One file with fixed sections. The first line is the format version: `format: v1`. The second line is `updated: YYYY-MM-DD HH:MM`, set to now at every change. When a skill finds an older format, it offers a migration and shows the changes first. A v1 map that lacks the Goals, Funnels or Key queries sections is still valid: the sections are added as empty tables at the next update.

Sections:
1. **Sources:** name, type (warehouse, lake, sheet, file, API, cube), dialect (Postgres, SQL Server, BigQuery, Snowflake...), access mode (connected or hand-over).
2. **Tables:** table, what one row means (grain), primary key, key columns, notes.
3. **Joins:** safe joins with keys, fan-out traps, and a check status: `unverified` until a query checks the join, then `checked`.
4. **Metrics:** canonical definition, logic, trusted numbers (value, period, where it comes from).
5. **Rules:** mandatory filters, business rules, exclusions.
6. **Gotchas:** past mistakes and how to avoid them.
7. **Glossary:** business terms and what they map to in the data.
8. **Conventions:** style only: SQL style, Python style, naming, team overrides of the defaults. Analysis rules go in Rules or Gotchas. No entry appears in two sections.
9. **Goals:** mission, north star metric, target metrics, each with a horizon (this quarter, this year, 3 years). `/grill-the-ask` asks how an ask links to a goal and records it in Meta.
10. **Funnels:** one row per step: the funnel, the step, its event or table, and the step definition.
11. **Key queries:** 3 to 5 reusable queries: name, what it returns, when to use it, the query. `/retro-analysis` proposes additions to Funnels and Key queries.

Sources hold one entry per source. Grain and key facts go under Tables. Every section is a table with the template's columns, never loose bullets (Conventions is the one list).

Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.

**Staleness:** when a skill relies on an entry older than 90 days, or one the data contradicts, it says so and asks before using it.

Shared by the team: committed to git where there is a repo, so every retro improves it for everyone.

### 7.3 `analysis.md`

First line: `format: v1`. Second line: `updated: YYYY-MM-DD HH:MM`. Sections, filled by step:

1. **Meta:** title, requester, audience, date, depth, question type, claim ceiling, status, progress line, setup choice (A, B or map found; setup is never offered again once set), goal link (the goal in the map's Goals section the ask serves), files (download, or a document tool the user named). Requester (a person or role the user names) and date are never blank.
2. **Ask:** the original ask verbatim, the clarified question, the decision it feeds, constraints, deadline. *(grill)*
3. **Assumptions:** table, see 7.5. *(grill, then any step)*
4. **Plan:** options considered, chosen plan, success checks (the method card's checks copied in at plan time; the reconcile check says whether the raw or the cleaned count must match the trusted number, and why). **Plan revisions** log: date, what changed, why, one row per correction. *(plan)*
5. **Analysis table spec:** see 7.4. *(plan)*
6. **Results:** ladder log (the floor checks, then each rung: expected, actual, pass or fail), findings as direction, magnitude, uncertainty, and the claim ceiling applied. Aggregates only by default. *(run)*
7. **Review:** verdict, technical issues, business issues, leadership questions with answers. *(review)*
8. **Retro:** proposed data map changes and which were accepted. *(retro)*
9. **Decisions:** every question and the user's answer, word for word, per round. After each round the skill echoes the answers back exactly before moving on. *(every step that asks)*
10. **Hypotheses:** the hypothesis tree with a status per node (section 7.9). *(plan, updated by run, checked by review)*
11. **Appendix: Review pack:** for each headline number, the exact SQL or Python that produced it and its data source. In chat apps `queries/` does not persist, so this is how a fresh reviewer sees the code. *(run)*

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
| A1 | Orders are counted on order date, not dispatch date | Stakeholder unavailable until Friday | Dispatch date; payment date | High: shifts monthly totals by about 10% | Ask finance; compare both definitions for one month | open |

- Status: `open`, `confirmed` or `rejected`.
- Alternatives are required for high-impact rows only.
- Standard and deep depth always show all 7 columns. Never drop columns. Only quick depth uses an inline list.
- `/review-analysis` flags any high-impact row still `open` when results are reported.
- Only real assumptions go in the table. Claim rules ("spend is a hypothesis, not a cause") go in the claim ceiling line in Meta.
- Rate impact by size: about 5% or more on the headline is High. A month-length difference that moves a headline by about 10% is never below Medium.

### 7.6 Readout (`readout.md`)

The stakeholder-facing result. Portable markdown, ready to paste into Confluence, Notion or a doc, with no app-specific macros. One layout; wording adapts to the audience set in grilling. The default readout respects that audience. `/storytell` is for other audiences and formats. App-specific exports (Confluence, Notion) are v0.4, in `/storytell`.

1. **Answer** in 2 lines.
2. **Key numbers**, each with its uncertainty. At most 5 (strict for an exec audience). The rest go to the Appendix.
3. **Charts** (the `viz` rules): at most 3 in an exec readout; each title states the takeaway; one annotation on the key moment (for example, a marker on the day a step happened). Charts replace number rows where they say the same thing. Charts are image files in `outputs/` (offered as downloads in chat apps), linked from the readout with alt text. Hand-over mode gives the chart spec plus ready-to-run code.
4. **What it means** and the recommendation.
5. **Caveats:** open high-impact assumptions, and the claim ceiling in plain words.
6. **Method** in 3 lines. Claims only what ran: no "full validation ladder" if the review found rungs weaker than that.
7. **Link** to `analysis.md`.
8. **Appendix:** other numbers, segment tables, the ladder summary.

Formatting:
- Callouts are blockquotes with a bold label: `> **Answer:** ...`, `> **Caveat:** ...`, `> **Ask:** ...`. At most 3 per readout.
- Status is a bold label at the top: `**Status: DRAFT**` or `**Status: FINAL**`.
- Bold only for the one takeaway per section.

`/run-analysis` writes the draft. `/review-analysis` checks every sentence against the claim ceiling, fixes it, and marks it final. Quick depth: a short answer in the chat, no file.

**Word and Google Docs copy.** `readout.md` is the source. `/run-analysis` also produces `readout.docx` from the same text with the charts embedded, using whatever document library the sandbox has. `/review-analysis` edits `readout.md`, then rebuilds the `.docx`. Nobody edits the `.docx` by hand. With no code tool: `readout.md` plus the chart code only. `/storytell` makes a `.docx` for its doc and email formats.

**Status line values:** `SKELETON` (placeholders only, from `/plan-analysis`, section 7.9), `DRAFT`, `FINAL`.

### 7.7 Data safety

- `/run-analysis` shows aggregates by default and asks before saving row-level data anywhere.
- `/setup-data-work` asks whether `outputs/` should be committed, in coding agents only. The default adds `data-work/analyses/*/outputs/` to `.gitignore`. Chat apps get no git advice.

### 7.8 Chat-first storage and surfaces

- **Workspace.** In chat apps, one Claude or ChatGPT Project per team or area, and one chat per analysis. `/setup-data-work` ends by writing a short block to paste into the Project's instructions, for example: "Read DATA-MAP.md before any data work. Use the data-skills commands. Save updated files back to the Project files."
- **Stable names and versions.** Fixed names: `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md` (and `readout-<slug>.docx`). A coding agent keeps `analysis.md` and `readout.md` inside the analysis folder. Every file starts with `format:` and `updated: YYYY-MM-DD HH:MM`. Skills hand back the whole file and say "Replace the old one in your Project files." If two copies exist, the skill uses the newest `updated:` and says so.
- **Optional save to a document tool.** Ask once, generically: "Hand files to you as downloads, or save them to a document tool you use (for example a drive, a wiki or a notes app)?" Use only a tool the user names, never one picked from visible connectors. Never required. The answer is the `Files` line in Meta.
- **Surface guide.** `docs/where-to-run.md`, linked from the README: coding agents (`data-work/` in the repo, files saved automatically, commit `DATA-MAP.md` so the team shares it); chat apps (a Project per team or area, the instructions block, files replaced by hand or saved to a document tool).
- **A new project, or a new Project, on the same data.** Carry over `DATA-MAP.md` and the Project instructions block. Start a fresh map only for entirely different data sources. When no map is found, `/setup-data-work` and `data-map` first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." Only then do they offer a fresh setup.

### 7.9 Hypotheses and the readout skeleton

**Hypothesis tree.** `/plan-analysis` at standard and deep depth writes it before the method options: H1, H2 and so on, each with children (H1.1, H1.2, then H1.2.1). At most 3 levels and about 12 nodes. For each node: what finding would support it, what would refute it, and which child it leads to. The user picks the paths to follow; the rest are `parked`. Quick depth: a flat list of up to 3 hypotheses, in the chat.

| id | hypothesis | would support it | would refute it | leads to | status |
|---|---|---|---|---|---|
| H1 | Sign-ups fell because of one channel | One channel falls far more than the others | All channels fall by a similar share | H1.1, H1.2 | open |

Status: `open`, `supported`, `refuted` or `parked`. `/run-analysis` updates it, naming the result that shows it. `/review-analysis` checks that every node has a status, that `supported` and `refuted` nodes have a result behind them, and that no `open` or `parked` node is worded as a finding.

**Readout skeleton.** Optional at standard and deep depth, in `/plan-analysis`. It drafts `readout.md` with placeholders only (XX%, [segment]), never an invented number, to check that the story would answer the decision. Status line `**Status: SKELETON**`. `/run-analysis` replaces it. `/review-analysis` and `/storytell` refuse to treat it as a result.

**Stuck rule.** When an answer conflicts with an earlier one, contradicts the data map, or does not make sense, the skill says so plainly ("This does not fit X because Y") and asks one question at a time until it is clear. Then it returns to rounds.

---

## 8. Onboarding: `/setup-data-work`

Rounds of max 3 questions. Partial answers are fine; the map grows through retros.

0. **Setup mode (always first, before touching any tool):** "How do you want to set up your data map? A) Connect: I list the data tools you have connected and you pick one or none. B) Describe it in your own words. C) Paste a schema: table list, CREATE statements, dbt file or doc. D) A mix."
1. **Access test (only for a source the user named):** if the user chose to connect, run a trivial test (`select 1`) against that source only. If no, tell the user once to check their agent's connector directory for their source; if it is missing or blocked by company policy, continue in hand-over mode. No dead ends.
2. **Sources:** which sources, type, and dialect for each. The dialect question offers one real option per engine: Postgres, SQL Server, BigQuery, Snowflake, Databricks, other. Never one option holding many names.
3. **Key tables:** the 3 to 10 tables used most, grain and keys for each.
4. **Joins:** the joins they trust, and any known fan-out traps. Every join starts as `unverified` until a query checks its match rate and fan-out. Never mark a join trusted from a schema alone.
5. **Metrics:** the 3 to 5 most-used metrics, their definitions, and one trusted number each (for reconciling).
6. **Goals:** the mission, the north star metric, the target metrics and the horizon of each (this quarter, this year, 3 years). Written to the Goals section.
7. **Funnels:** the main funnels: each step, the event or table that marks it, and the step definition. Written to the Funnels section.
8. **Key queries:** 3 to 5 reusable queries, what each returns and when to use it. Written to the Key queries section.
9. **Rules:** mandatory filters (test accounts, cancelled orders, time zones).
10. **Conventions:** "Does your team have SQL or Python conventions? If not, I'll use sqlstyle.guide and PEP 8."
11. **Where the files live:** "A) One repo with a folder per project. B) A repo per project. C) A team repo. D) Chat Projects." Skills look for `data-work/` in the current folder, then upward. A team map can sit above project maps: the nearest map wins for conflicts, and the skill says which map it read. For chat apps, recommend one Project per team or area and one chat per analysis (section 7.8).
12. **Git policy (coding agents only):** commit `outputs/` or not (default: not). No git advice in chat apps.
13. **Save to a document tool (chat apps, ask once):** "Hand files to you as downloads, or save them to a document tool you use (for example a drive, a wiki or a notes app)?" Only a tool the user names. Never required.

Before step 0, when no map is found: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If yes, extend it. Start a fresh map only for entirely different data sources.

Then write `DATA-MAP.md` and show a short summary of what is still missing. In a chat app, end with the Project instructions block (section 7.8).

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

Reuse the existing question-type ceilings and must-answer questions from the author's earlier repo where they fit, rewritten in this repo's style.

### 10.1 Method cards

Plain models know what each method is. They fail at choosing the method, checking its assumptions and overclaiming. Every card covers exactly that, in this format:

- **When to use:** the situation and data shape
- **Data needed**
- **Key assumptions**
- **Checks that must pass**
- **Common failure**
- **Claim allowed**
- **Simplest version first**
- **Tool notes:** SQL, Python (statsmodels, scipy, scikit-learn, DoWhy or EconML), and Excel where it applies

**Full cards** for common methods. **Short cards** (when to use, key assumption, key check, claim allowed) for advanced methods, ending with: "Get a specialist review before shipping."

### 10.2 Method catalogue

| Type file | Full cards | Short cards |
|---|---|---|
| `descriptive.md` | counts and rates; means and medians; rolling windows (7-day, 28-day); week-on-week and year-on-year with seasonality; cohort tables; funnels; segment breakdowns; mix-shift decomposition; index to baseline | |
| `exploratory.md` | segment scan; metric decomposition (driver tree); correlation | clustering; anomaly detection |
| `inferential.md` | confidence intervals; t-test and Mann-Whitney; proportion and chi-square tests; bootstrap; regression for association; multiple-comparison correction | |
| `predictive.md` | naive and seasonal-naive baselines; linear and logistic regression; forecasting (ETS, ARIMA); backtesting and cross-validation; leakage checks | gradient boosting; calibration |
| `causal.md` (plus `experiment.md` for A/B) | randomised experiment (A/B); difference-in-differences; interrupted time series | regression discontinuity; synthetic control; instrumental variables; propensity score matching and inverse probability weighting; uplift and heterogeneous treatment effects |
| `mechanistic.md` | | one short note: rarely reachable in business work; flag it and fall back to the highest type the data supports |

Exploratory outputs are hypotheses, never findings.

### 10.3 Causal method selector (in `question-types/SKILL.md`)

- Randomised assignment? -> A/B (`experiment.md`)
- Rollout to some units, with a comparison group and a pre-period? -> difference-in-differences
- Assignment by a cut-off on a score or threshold? -> regression discontinuity
- One treated unit (a region, a market) and several untreated ones? -> synthetic control
- One time series with a known change date and no comparison group? -> interrupted time series
- A variable that moves treatment but not the outcome directly? -> instrumental variables
- Observational data with rich pre-treatment covariates? -> matching or weighting
- The question is who to treat, not whether it works? -> uplift
- None fits? -> say so, give the ceiling the data supports, and offer the best descriptive path.

---

## 11. Validation ladder

### 11.1 Data-check floor (every depth)

Quick depth gets a compact version (one small query per check, results in one table) but never skips it. Each check states its expected result first.

1. **Table audit** for each table used: row count; distinct keys vs rows (duplicates); null rate of every column used; min and max dates (coverage, future dates); distinct values of every category column used (flag unexpected labels).
2. **One real entity across tables:** pick a specific id and show its rows in every table used. Check the values make sense (for example, sign-up before first order).
3. **One day, all entities:** the total for one day, in a plausible range.
4. **Daily series across the full window:** gaps, spikes, zero days. Mandatory for any "X dropped" question, before any segment scan, because a logging break is the most common cause of a drop.
5. **Join checks:** row counts before and after each join, key match rate (orphans), fan-out.
6. **Category totals** sum to the overall total.
7. **Assumption checks:** every assumption a query can test gets one (for example, an hour-of-day distribution for a time zone assumption).
8. **Reconcile** to the trusted number, saying whether the raw or the cleaned count should match, and why.

In hand-over mode, batch the checks into numbered groups so the user pastes once per group, not once per query.

### 11.2 Ladder rungs (standard and deep)

1. **One entity:** follow one customer, order or account end to end. Check every column by hand against its raw rows.
2. **One entity-day:** recompute one entity's value for one day or period from the raw rows and compare. Check the time logic.
3. **Many entities:** a sample of 10 to 100. Recompute each from the source with a separate query and compare. Check duplicates, nulls and join fan-out (row counts before and after each join).
4. **Aggregates:** compute the headline totals a second way, from the source tables without the analysis table, and compare. Check distributions and edge periods.
5. **Reconcile:** compare to a trusted number from `DATA-MAP.md` or the stakeholder. Explain any gap above a stated tolerance.

Rungs 2 to 4 must test the data, not only the aggregation. A rung that compares the analysis table with the frame it was built from is not a pass.

Before each check, state the expected result. After it, record the actual result and pass or fail in `analysis.md`. Quick depth runs the compact floor; its checks 2, 3 and 8 stand in for rungs 1, 2 and 5. Standard runs the full floor and all five rungs. Deep adds an alternative specification.

---

## 12. Review standard (`/review-analysis`)

- **Technical:** data, joins, filters, method, tests, ladder log, analysis table spec match, uncertainty.
- **Independent recompute (every depth):** recompute the 3 to 5 headline numbers by a route the analysis did not use, and spot-check 1 or 2 rungs. The review checks; it does not rebuild the analysis.
- **Business:** does it answer the decision? Is the effect practically meaningful? Guardrails, cost and risk, what a sceptical leader will ask.
- **Claims:** every claim checked against the question-type ceiling.
- **Assumptions:** any high-impact open row flagged.
- **Leadership questions:** each answer marked "not supported yet" names the cheapest way to answer it.
- **Readout:** every sentence the review changes is shown as a "was" and "now" pair.
- **Verdict:** `ready`, `ready with caveats`, or `needs rework`, with the reasons.
- **Fresh context:** the review works from the files only (`analysis.md`, `readout.md`, `DATA-MAP.md`, the data), never from chat memory. If the agent can start a subagent with fresh context, it may run the review there, passing only the files; this is optional and never relied on (section 3). Otherwise, at standard and deep depth, the go-ahead question at the end of `/run-analysis` recommends: "Start `/review-analysis` in a new chat. In a Claude or ChatGPT Project, save the data, `DATA-MAP.md`, `analysis.md` and `readout.md` to the Project files first, then open a new chat in that Project; nothing needs attaching." A same-chat review stays allowed, with the files-only stance. Quick depth: a same-chat review is fine.
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
- Also check triggering: user-invoked skills must not fire on their own, and disciplines must fire when they should. A generic ask ("write a SQL query for monthly sign-ups") must not trigger our skills over built-in data skills, and a non-data vague ask must not trigger `grilling`.
- Every flow skill rubric also checks: no connector call before the source is named; the data map check is announced; in chat apps, `analysis.md` is offered at the end; no names the user did not say.
- Extra cases: `setup-data-work` with several connectors visible (must ask first); `grill-the-ask` in a chat app with no project folder (must offer a download); `question-types` method choice, 6 cases (for example "rollout to 3 regions, which method?"), testing the choice and the checks named, not calculations.
- Run all chat-app tests in incognito chats, and with a neutral profile, so memory and profile preferences do not leak in.
- v0.3 rubric rows: the go-ahead question, no manual file edits and downloads first in every flow rubric; real defaults in setup, grill, plan and `grilling`; the data-check floor, run first, 5 key numbers, fresh review, review pack, readout visuals and portable callouts in run and review.
- v0.3 cases: `run-analysis` on attached CSVs in a chat app with a code tool (must run the checks itself); `run-analysis` on data with a zero-day logging gap (must find it before any segment scan); `grill-the-ask` with a period comparison across a seasonal boundary (must flag seasonality); `retro-analysis` (must not put analysis rules under Conventions).
- Reference case: `evals/reference/signup-drop-claude-ai.md` summarises what a good manual run caught on the sign-up example. Neutral domain only.

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
    question-types/SKILL.md, descriptive.md, exploratory.md, inferential.md, predictive.md, causal.md, experiment.md, mechanistic.md
    data-map/SKILL.md, DATA-MAP.template.md
    run-or-hand-over/SKILL.md
    shaping-data/SKILL.md, sql.md, python.md, excel.md, powerbi.md, tableau.md
    data-audit/SKILL.md
    stats-tests/SKILL.md
  templates/
    analysis.template.md, readout.template.md, experiment-spec.template.md, metric-spec.template.md
  evals/
    <skill>/case-1.md, case-2.md, case-3.md, rubric.md
    results/
  docs/
    install.md         Claude Code, Codex, Gemini CLI, Cursor, Copilot, claude.ai, ChatGPT
    upstream-map.md
    where-to-run.md    coding agents and chat Projects: where files live (v0.4)
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

### v0.1 (fix pass)
Everything in decisions 21 to 32: connector rules, data map check, chat-app handoff, readout, progress tracker, method cards for all question types, neutral domain, private blocklist, eval additions.

### v1
Router, wayfinder, handoff, improve-code, storytell (audience-specific layouts), viz; ML beyond baselines; rest of the upstream inventory; automated eval runner; split Conventions into its own file if it grows.

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
21. Never call a connector or data tool before the user names the source. Never build options from visible connectors.
22. Never fill in company, product, table or source names the user has not said in this conversation.
23. Setup asks first how to set up the map: connect, describe, paste a schema, or a mix.
24. Every flow step checks for `DATA-MAP.md` and `analysis.md`, says what it found, and offers setup if there is no map. Outside the flow, no map means silence.
25. Chat app is defined by situation (no user project folder), not by file access. Each flow step offers its files as downloads and tells the user to save them to Project files.
26. Standard and deep depth always show the full 7-column assumptions table.
27. `/run-analysis` is goal-driven: it states its goal and keeps going until the success checks pass, stopping only for pastes or answers.
28. Readout: `/run-analysis` drafts `readout.md`; `/review-analysis` checks it word by word and marks it final. One layout, wording adapted to the audience set in grilling.
29. Progress line in `analysis.md` Meta; every new session resumes from it.
30. `question-types` covers all six types: one skill, a selector in `SKILL.md`, one file per type with method cards. Full cards for common methods, short cards plus a specialist-review flag for advanced ones. In v0.1, with method-choice evals.
31. One neutral example domain: an invented online shop and subscription app. A private gitignored `.blocklist` is checked by `scripts/self-check`.
32. `grilling` fires on data asks only. Descriptions are tuned so generic data asks do not trigger ours over built-in data skills.

---

## 20. v0.2 experimental

Built on branch `v0.2`. Every new skill here is **experimental** until it has passed its evals. All section 3 hard rules apply.

Rules for every new skill:
- Frontmatter is `name` and `description` only.
- User-invoked descriptions say "Use only when the user runs /<name> or explicitly asks to ...".
- Flow-style skills (they read or write files in `data-work/`) open with the 4-step start from section 4 and end with the chat-app handoff from section 5.
- Each new user-invoked skill has 3 eval cases (2 flawed, 1 clean) and a rubric.

### 20.1 `/storytell` (user-invoked, off-flow)

- Input: the final `readout.md` and `analysis.md`. If the readout is not final, it says so and suggests `/review-analysis` first.
- Asks the audience (exec, product, data, mixed) and the format (doc, chat message, email, slide outline).
- Writes `readout-<audience>.md` next to the readout.
- Rules: answer first. Every number keeps its uncertainty. No claim above the ceiling recorded in `analysis.md`. Caveats in plain words. Exec version: no jargon, under 150 words before the appendix. Slide outline: at most 5 slides, each title states the takeaway, one chart suggestion per slide.
- Calls: `question-types`, `viz`.

### 20.2 `viz` (model-invoked data skill)

- Applies when a chart is chosen, built or reviewed inside the flow.
- `SKILL.md`: chart choice by question (trend, comparison, distribution, part of whole, relationship, funnel, cohort), and checks: the title states the takeaway; axes labelled with units; bars start at zero; uncertainty shown where it exists; no dual axes; colour-blind safe; no 3D; small multiples over cluttered legends; same scale when comparing.
- Tool files: `python.md` (matplotlib, plotly), `excel.md`, `tableau.md`, `powerbi.md`, and `dashboard.md` (see 20.8). Excel, Tableau and Power BI run in hand-over mode.
- Called by `/run-analysis` (charts in `outputs/`), `/review-analysis` (chart check) and `/storytell`.

### 20.3 `/improve-code` (user-invoked, off-flow)

- Input: SQL or Python, pasted or as a file path.
- Order: understand intent (ask if unclear), then correctness (grain, join fan-out, filters, nulls, time zones, dedup), then style (sqlstyle.guide or PEP 8; team Conventions win), then performance (dialect-aware: partition filters, needed columns only, avoid repeated scans).
- Surgical: change only what is needed. Show a diff. One line per change saying why.
- Prove equivalence where behaviour should not change: before and after row counts and totals, as check queries through `run-or-hand-over`. If behaviour changes on purpose (a bug fix), say so and show the difference.
- Calls: `shaping-data`, `validation-ladder`, `run-or-hand-over`, `data-map`.

### 20.4 `/ask-data-skills` (user-invoked router)

- Asks what the user is trying to do: one round, at most 3 questions.
- Recommends one command, with one line why, and the next one after it.
- Knows the full catalogue. Does not do the work itself.
- **Routing guide (v0.4).** The same table sits in the README and in this skill. Self-check tests both.

| The ask looks like | Use |
|---|---|
| A project: several questions, unknowns, weeks of work | `/wayfinder-data` |
| A design with no data needed yet (experiment, measurement) | `/wayfinder-data` (fast path) |
| One question with a decision attached | `/grill-the-ask` and the flow |
| Not sure | `/ask-data-skills` |

`/grill-the-ask` sends project-sized asks and design asks to `/wayfinder-data` with one line why.

### 20.5 `/wayfinder-data` (user-invoked, off-flow)

- For big, vague work (for example "build a metrics framework for the subscription app").
- Writes `data-work/wayfinder/<slug>.md`: a list of decision items, each with options, a recommended default, status (open, decided), dependencies, and who decides.
- Resolves items one at a time using `grilling`. Never resolves an item silently.
- When the map is done, lists the analyses to run, each as a ready `/grill-the-ask` prompt.
- **Design items (v0.4).** Also handles asks that need a design, not data: "design an A/B test", "define how we measure X". The output is a spec file, from templates in the skill folder and in `templates/`:
  - `experiment-spec.md`: hypothesis, unit of randomisation, feature gate or assignment, primary metric, guardrails, MDE, power, runtime, seasonality, SRM check plan, decision rule.
  - `metric-spec.md`: definition, formula, grain, population, data source or what must be collected, candidate proxies and how to check they track the true metric, a benchmark or target and where it comes from, owner.
  - Uses the `experiment` card, `stats-tests` and `metric-design`. Never invents a number: baselines, targets and benchmarks come from the user or the data map, or stay "to confirm".
  - **Fast path:** when the whole ask is one design item, it skips the decision map and goes straight to that spec.
  - `/grill-the-ask` sends design asks and project-sized asks to `/wayfinder-data` with one line why.

### 20.6 `/handoff` (user-invoked, off-flow)

- Writes `handoff.md` in the analysis folder: where things stand (the Progress line), what is done, decisions made, open high-impact assumptions, the next step, files and their state, and how to resume in a fresh session.
- For a colleague or a fresh session. Chat apps: offered as a download.

### 20.7 Predictive cards upgrade

- `question-types/predictive.md`: gradient boosting and calibration become full cards. New full card: classification metrics (precision, recall, ROC-AUC, PR-AUC, choosing a threshold by cost). The leakage card covers target leakage, time leakage and split by time. Feature importance is not causal.
- 2 more method-choice eval cases, for predictive questions.

### 20.8 Rest of the upstream inventory

- Every "v1 backlog" item in `docs/upstream-map.md` is absorbed into an existing skill, built, or dropped with a reason. At most 4 new skills.
- Built: `metric-design` (model-invoked data skill): define a metric or KPI with its formula, grain, owner, guardrails and a trusted number.
- Absorbed: dashboards into `viz` (`dashboard.md`); charts into `viz`; reports and KPI readouts into `/storytell`; metric diagnostics into the exploratory method cards; routing into `/ask-data-skills`.
- The Anthropic `data` plugin is Apache-2.0: reuse with attribution in `NOTICE`. The OpenAI `data-analytics` plugin is proprietary: ideas only, no text.

### 20.9 Plugin manifests

- Claude Code: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
- Codex: `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`.
- `docs/install.md` gives the install line for each.

### 20.10 Worked examples

- `examples/signup-drop/`: "Why did sign-ups drop in March?" for the invented subscription app. Descriptive, then exploratory, with the ceiling stated.
- `examples/pricing-page-test/`: an A/B test on the shop's pricing page, with an SRM check, power, and a clean readout.
- Each has invented data as small CSVs from a seeded script (`generate_data.py`), `DATA-MAP.md`, `analysis.md`, `readout.md` and `queries/`. Produced by following the skills in order, with the queries really run.

### 20.11 GitHub Actions

- `self-check.yml`: runs `scripts/self-check` on every pull request and push. If the repository secret `DATA_SKILLS_BLOCKLIST` exists, the job writes it to `.blocklist` first and never prints it.
- `release.yml`: when a release is published, runs `scripts/package-zips` and uploads every ZIP as a release asset.

### 20.12 Eval runner

- `evals/runner/run.py`: Python standard library, plus the official Anthropic and OpenAI SDKs as optional imports.
- Builds context from the skill's `SKILL.md` plus the files of the disciplines it calls. Sends the case input. Multi-turn cases use a "Simulated answers" section.
- A judge prompt grades against the rubric: pass, partial or fail, with reasons. Writes `evals/results/<date>-<provider>-<model>.md`.
- Keys from environment variables only. Never logged or stored. `--dry-run` prints what it would send and an estimated cost, with no API call. A real run prints the estimate and asks for confirmation.
- It approximates skill loading and does not test triggering. Manual triggering tests are still needed.

### 20.13 Contributor docs

- `CONTRIBUTING.md`: how to add a skill or a method card, the neutral domain rule, the hard rules, running the self-check and evals, release steps.
- `.github/ISSUE_TEMPLATE/`: skill bug, method card request, new skill proposal.
- `.github/pull_request_template.md`: checklist.

### 20.14 Catalogue after v0.2

22 skills: the 15 from v0, plus user-invoked `storytell`, `improve-code`, `ask-data-skills`, `wayfinder-data`, `handoff`, and model-invoked `viz`, `metric-design`.

---

## 21. v0.3 fix pass

Found by a full manual run of the flow in claude.ai on the `examples/signup-drop` data. Built on branch `v0.2`. All section 3 hard rules apply. Decisions 47 to 64.

| Area | Change | Where in this spec |
|---|---|---|
| Validation | Data-check floor at every depth (quick in compact form); rungs 2 to 4 test the data against an independent path; the review recomputes headline numbers | 2, 4 (depth), 11, 12 |
| Running and files | Two questions: can I run things here (always try first; a code tool with attached files counts) and where do files persist (create and offer a download; print only if that fails); no manual file edits; compact method cards for chats without file access | 5 |
| Every flow step | Fixed go-ahead question at the end, at every depth; every question has a real recommended default | 4 |
| Grill and plan | Seasonality in period comparisons; only real assumptions in the table, claim rules in the ceiling, impact rated by size; reconcile names raw or cleaned count; one Plan revisions row per correction; requester and date never blank | 4, 6.1, 7.3, 7.5 |
| Readout and review | At most 5 key numbers plus an Appendix; Method claims only what ran; "was" and "now" pairs; cheapest way to answer each open leadership question | 7.6, 12 |
| Setup and retro | No git advice in chat apps; joins start `unverified`; one option per SQL dialect; Conventions hold style only; true reasons only | 7.2, 7.7, 8, 6.1 |
| Fresh review, visuals, callouts | Files-only review, fresh context recommended; Review pack appendix in `analysis.md`; at most 3 charts with one annotation; portable callouts and a bold status label | 7.3, 7.6, 12 |
| Evals | Rubric rows for the changes, four new cases, and a reference run summary | 15 |
| Self-check | Checks 25 to 28: go-ahead question, floor checks, compact cards, template format | `docs/self-check.md` |

App-specific readout exports (Confluence, Notion) are v0.4, in `/storytell`. Plugin version: `0.3.0`.
