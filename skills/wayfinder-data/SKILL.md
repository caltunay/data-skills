---
name: wayfinder-data
description: Map big, vague data work as a list of decision items, resolve them one at a time with the user, and end with ready prompts for the analyses to run. Also handles asks that need a design, not data (design an A/B test, define how to measure something) by writing an experiment spec or a metric spec. Use only when the user runs /wayfinder-data or explicitly asks to map out or break down a large, ambiguous piece of data work, or to design an experiment or a metric.
---

# /wayfinder-data

Big work is a set of decisions. Find them, order them, settle them one at a time.

Experimental (v0.2).

Two kinds of ask come here. First, work too big for one `/grill-the-ask`: "build a metrics framework for the subscription app", "work out what we should measure for the new loyalty scheme", "plan this quarter's analysis of returns".

Second, asks that need a design and no data yet: "design an A/B test for the new pricing page", "define how we measure customer health". These end in a spec file, not an analysis.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or wayfinder file count as said by the user.
- **Never resolve an item silently.** An item is `decided` only when the user chose it, or said "you choose" and you told them what you chose.
- This step runs no analysis and no query. It maps decisions.

## Start (every flow step)

1. Check for `DATA-MAP.md` and for an existing wayfinder file `data-work/wayfinder/<slug>.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts. This step needs no `analysis.md`.
2. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice.
3. If the user is resuming and the wayfinder file is not found (for example, a new chat), ask them to attach it before asking anything else.
4. If a wayfinder file exists, read its Progress line and resume from it. Do not reopen decided items unless the user asks. If a spec for the same design already sits in an analysis folder, ask "Continue `<folder>`, or start a new spec?" Never resume silently.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default with its reason. A hedge is not a default: never "recommended if you have one", "TBC" or "C if unknown". Pick a real option and say why. Show any tree, table or draft a question refers to before you ask it (never ask "which hypothesis paths?" before the tree is on screen). Each option says what it means in a few words (for example "H1.1: holds in each month"). An option that needs data the map says is missing says so in the option text (for example "needs the visit marker; the map says it is unknown"). Use the environment's multiple-choice question tool for every round if it has one (one card per question, recommended option first, room for the user's own answer); otherwise list the options as text. Wait for answers. Never assume silently. When an answer conflicts with an earlier one or the data map, or does not make sense, say so plainly and ask one question at a time until it is clear. Never ask the same question twice.
- `assumptions`: when something must be assumed, write it down with likely alternatives and the impact if wrong.
- `question-types`: six question types, each with a claim ceiling. Name the type of each analysis you list.
- `metric-design` (experimental): a metric needs a formula, a grain, a population, an owner, guardrails and a trusted number.
- `stats-tests`: size an experiment with a baseline, an MDE, power and a significance level. Fix the primary metric and the runtime in advance. One primary metric; extra metrics get a correction or the label exploratory.
- `experiment` card (in `question-types`): randomise a unit, hold the split fixed, check the sample ratio, no peeking, full weekly cycles, guardrails, one decision rule written before the test.
- `data-map`: read `DATA-MAP.md` first. Flag entries older than 90 days or contradicted by data, then ask.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand.

## Steps

0. **Fast path for a single design item.** If the whole ask is one design item ("design an A/B test for X", "define how we measure Y"), skip the decision map and the project file. Go straight to the spec: an experiment spec for a test, a metric spec for a measure. Do one framing round (at most 3 questions), then fill the template one section at a time with the user (see "Design items"). Do not make the user sit through a project map for a single design. If the ask turns out to hold several designs or analyses, say so and switch to the full map.
1. **Take the work verbatim.** Store it unchanged.
2. **One framing round** (at most 3 questions): what outcome is wanted, who it is for, and by when. Skip what is already known.
3. **Draft the map.** List the decision items: every choice that must be made before the work can be done well. Aim for 5 to 12. Fewer than 4 means this is one analysis: say so and suggest `/grill-the-ask` instead. For each item write:
   - **id** (W1, W2, ...) and a one-line question
   - **options** (2 to 4), each with its main trade-off
   - **recommended default:** a real option with one line why. "Recommended if you have one" or "TBC" is not a default. Flag an option that needs data the map says is missing
   - **status:** `open`
   - **depends on:** ids that must be decided first, or none
   - **who decides:** a role the user names. If unknown, write "to confirm" and ask. Do not guess a person or a team.
4. **Show the map and confirm it.** Ask: is anything missing, and is anything not really open? Fix the list.
5. **Order the items.** Items with no open dependencies come first. Among those, the one that changes the most other items comes first.
6. **Resolve one item at a time.** For the next item: restate the question, the options and the default, and ask (apply `grilling`). Wait. Then:
   - The user chooses: set `status: decided`, record the choice, the date and who decided.
   - The user says "you choose": take the default, say so, record it as decided "by default, at the user's request".
   - The user cannot decide (it belongs to someone else): leave it `open`, record who to ask and the question to put to them. Move on to an item that does not depend on it.
   - A decision changes other items: update them, and say which ones changed.
   Update the Progress line after every item.
7. **Stop when** every item is `decided`, or the only open items wait on other people. Do not push the user through all of them in one sitting if they want to stop: the file holds the state.
8. **List the analyses to run.** When the map is done (or far enough), write "Analyses to run": each as a ready prompt the user can paste, in dependency order. Each prompt carries the decisions that scope it, so `/grill-the-ask` does not have to re-ask them. Say which analyses are blocked by an open item.

## Design items

An item in a map can be a design item (an experiment or a metric to define). So can a whole fast-path ask. The output is a spec file, from the templates in this skill's folder: `experiment-spec.template.md` and `metric-spec.template.md`.

- **`experiment-spec.md`:** hypothesis, unit of randomisation, feature gate or assignment, primary metric, guardrails, MDE, power, runtime, seasonality, SRM check plan, decision rule. Use the `experiment` card in `question-types` for the checks, `stats-tests` for the sample size and MDE, and `metric-design` for the primary metric if it is not yet defined.
- **`metric-spec.md`:** definition, formula, grain, population, data source or what must be collected, candidate proxies and how to check they track the true metric, a benchmark or target and where it comes from, owner. Use `metric-design`.

Save each spec in its own analysis folder, `data-work/analyses/<YYYY-MM-DD>-<slug>/experiment-spec.md` or `metric-spec.md`, never as a bare `experiment-spec.md` (the next spec would overwrite it). Make the folder if it does not exist, and name the path when you save.

Rules for both:

- Go one section at a time. Each question has one real recommended default. Log answers word for word and echo them back.
- Never invent a number. Baselines, targets and benchmarks come from the user, the data map or a stated calculation. If missing, write "to confirm" and who can supply it. Do not look one up from memory and present it as theirs.
- A proxy is a guess until a check shows it tracks the true metric. The spec says how to check, with data that holds both, and the check result stays `not run` until someone runs it. Running it is a `/grill-the-ask` analysis, not this step.
- A power or sample size is a calculation: show the inputs and the formula. Do not do the arithmetic in your head.
- Experiment spec and metric spec end with open items: what is still to confirm, with who and by when.

## The wayfinder file

Path: `data-work/wayfinder/<slug>.md`. Layout:

```
format: v1

# Wayfinder: <title>

- Work (verbatim):
- Outcome wanted:
- For whom:
- By when:
- Date started:
- Progress: <for example: 4 of 9 decided, next W5, W7 waits on finance lead>

## Decision items

| id | question | options | recommended default | status | depends on | who decides | decision (what, date, by whom) |
|---|---|---|---|---|---|---|---|
| W1 | | | | open | none | | |

## Assumptions

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|

## Specs to write

- <experiment-spec.md or metric-spec.md, and the item it settles>

## Analyses to run

1. `/grill-the-ask <ready prompt>` (question type: <type>; depends on: W1, W3)
```

Status is `open` or `decided`. Keep decided rows. Never delete an item: if it turns out not to matter, mark it `decided: not needed` with the reason.

## Example item (invented)

| id | question | options | recommended default | status | depends on | who decides | decision |
|---|---|---|---|---|---|---|---|
| W2 | What counts as an active subscriber? | A) Paid and not cancelled. B) Paid and used the app in the last 30 days. C) Any login in the last 30 days | A: matches the finance report, simplest to reconcile | open | W1 | Head of product | |

Example ready prompt: `/grill-the-ask Monthly churn rate for the subscription app, last 12 months, by plan. Active subscriber means paid and not cancelled (W2). Churn is counted on the cancellation effective date (W4). For the product leadership review.`

## End (every flow step)

1. Update the Progress line in the wayfinder file (if there is one).
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a bare `experiment-spec.md` is overwritten by the next spec): the wayfinder file at `data-work/wayfinder/<slug>.md`, and each spec in its own analysis folder, `data-work/analyses/<YYYY-MM-DD>-<slug>/experiment-spec.md` or `metric-spec.md`. Start each with `format: v1` and `updated: YYYY-MM-DD HH:MM`. Hand back the whole file. Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Never ask the user to edit a saved file by hand.
4. Stale copies: if an older copy of a file exists elsewhere in the Project (for example a spec at the top level, or a file in `claude/`), name it and say it is stale. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are saved under `data-work/`. Name each path.
6. End with the go-ahead question, in this fixed form:

   > Go ahead?
   > A) Yes, <the next step> (recommended)
   > B) Change something (say what)
   > C) Add an item, a check or a question

   Fill in A with the real next step: the next open item ("resolve W5"), the first `/grill-the-ask` prompt, or, for a fast-path spec, "share the spec for sign-off, then run `/grill-the-ask` for the analysis that will read the test out". Wait for the answer. A means start that step. B or C means make the change, hand back the updated file, and ask again.

## Done when

Every item is decided or waits on a named role, and the analyses to run are listed as ready prompts. For a fast-path ask: the spec is filled and its open items are named.

## Do not

- Do not decide for the user without telling them.
- Do not start any of the analyses.
- Do not invent owners, teams or deadlines.
- Do not turn one clear data question into a map. Send it to `/grill-the-ask`. A single design item is not a map either: take the fast path.
- Do not run any test or query. A spec says what to run.
