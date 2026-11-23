---
name: wayfinder-data
description: Map big, vague data work as a list of decision items, resolve them one at a time with the user, and end with ready prompts for the analyses to run. Use only when the user runs /wayfinder-data or explicitly asks to map out or break down a large, ambiguous piece of data work.
---

# /wayfinder-data

Big work is a set of decisions. Find them, order them, settle them one at a time.

Experimental (v0.2).

For work too big for one `/grill-the-ask`: "build a metrics framework for the subscription app", "work out what we should measure for the new loyalty scheme", "plan this quarter's analysis of returns".

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or wayfinder file count as said by the user.
- **Never resolve an item silently.** An item is `decided` only when the user chose it, or said "you choose" and you told them what you chose.
- This step runs no analysis and no query. It maps decisions.

## Start (every flow step)

1. Check for `DATA-MAP.md` and for an existing wayfinder file `data-work/wayfinder/<slug>.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found. This step needs no `analysis.md`.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice.
3. If the user is resuming and the wayfinder file is not found (for example, a new chat), ask them to attach it before asking anything else.
4. If a wayfinder file exists, read its Progress line and resume from it. Do not reopen decided items unless the user asks.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default (never a hedge such as "C if unknown"). Wait for answers. Never assume silently. Never ask the same question twice.
- `assumptions`: when something must be assumed, write it down with likely alternatives and the impact if wrong.
- `question-types`: six question types, each with a claim ceiling. Name the type of each analysis you list.
- `metric-design` (experimental): a metric needs a formula, a grain, a population, an owner, guardrails and a trusted number.
- `data-map`: read `DATA-MAP.md` first. Flag entries older than 90 days or contradicted by data, then ask.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand.

## Steps

1. **Take the work verbatim.** Store it unchanged.
2. **One framing round** (at most 3 questions): what outcome is wanted, who it is for, and by when. Skip what is already known.
3. **Draft the map.** List the decision items: every choice that must be made before the work can be done well. Aim for 5 to 12. Fewer than 4 means this is one analysis: say so and suggest `/grill-the-ask` instead. For each item write:
   - **id** (W1, W2, ...) and a one-line question
   - **options** (2 to 4), each with its main trade-off
   - **recommended default**, with one line why
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

1. Update the Progress line in the wayfinder file.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Chat app: create the wayfinder file and offer it as a download. Print one block only if creating a file fails. Never ask the user to edit a saved file by hand: hand back the updated file. Say: "Save this to your Project files so the next session, in any chat, can read it."
4. Coding agent: the file is saved under `data-work/wayfinder/`. Say where.
5. Name the next step: the next open item, or the first `/grill-the-ask` prompt.

## Done when

Every item is decided or waits on a named role, and the analyses to run are listed as ready prompts.

## Do not

- Do not decide for the user without telling them.
- Do not start any of the analyses.
- Do not invent owners, teams or deadlines.
- Do not turn one clear ask into a map. Send it to `/grill-the-ask`.
