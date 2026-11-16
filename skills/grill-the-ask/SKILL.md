---
name: grill-the-ask
description: Turn a vague stakeholder ask into a clear, scoped question with stated assumptions before any analysis. Use only when the user runs /grill-the-ask or explicitly asks to clarify or grill a data request.
---

# /grill-the-ask

Clarification is the most important part of data work. Ask before you assume.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Exception: if the ask is small and already clear (quick depth), make the offer in one line and continue with B without waiting.
3. A new ask needs no `analysis.md`. If the user is resuming an ask and `analysis.md` is not found (for example, a new chat), ask them to attach it before re-asking anything.
4. If `analysis.md` exists, read the Progress line in Meta and resume from it. Skip every question the file or the data map already answers.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and a recommended default. Wait for answers. Never assume silently.
- `assumptions`: write each assumption in the assumptions table. High-impact rows need 1 to 3 likely alternatives. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.
- `question-types`: six types: descriptive, exploratory, inferential, predictive, causal, mechanistic. Each has a claim ceiling. No "caused" without a randomised experiment or a credible causal design. A "why" question starts as descriptive or exploratory. It is causal only when a design fits. Say so when you propose the type.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Never call a data tool before the user names the source.
- `data-map`: read `DATA-MAP.md` before writing queries. Flag entries older than 90 days or contradicted by data, then ask.

## Steps

1. Take the ask verbatim. Store it unchanged.
2. Run rounds of questions covering: goal, the decision it feeds, question type, metric, population, time window, constraints, deadline, and audience (who reads the result: exec, product, data or mixed).
3. **Never ask the same question twice in a session.** Before each round, list what is already answered: in the ask, in `analysis.md`, in the data map, and in earlier answers. A reworded question is the same question. If an answer was unclear, quote it and ask only about the unclear part.
4. Propose the question type with its ceiling. Confirm it with the user. For an ask that wants a cause ("did X work", "prove", "impact of"), ask what comparison exists: a randomised holdout, an untreated group, a cut-off rule, or only a before and after. The answer decides whether a causal claim is reachable.
5. Choose the depth after round 1 and propose it with a one-line reason: **quick**, **standard** or **deep**. If the depth is quick, stop asking: what is still unknown becomes an inline assumption. Example: "Depth: standard, because the number feeds a budget decision but is not a test readout." The user can override.
   - Quick: a small, low-risk ask, one number or one chart.
   - Standard: the usual ask.
   - Deep: high stakes, a decision with real cost, or a test readout.
6. Write down every assumption you have to make. At standard and deep depth, show the full 7-column assumptions table.
7. Restate the clarified question in one or two sentences. Ask the user to confirm it.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Rounds until clear, plus stakeholder prep questions |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

The Files row covers the whole flow. This step writes `analysis.md` only. `readout.md` comes from `/run-analysis`.

Stakeholder prep questions (deep): who else will read this, what will they push back on, what would change their mind, what is the cost of a wrong answer.

## Output

- **Quick:** no files. Print the clarified question, depth and an inline assumption list. Suggest `/plan-analysis`, or just do the work if the path is obvious.
- **Standard and deep:** build `analysis.md` from `analysis.template.md` (in this skill's folder). Fill Meta (including audience and the Progress line), Ask and Assumptions. Set status to `grilling`.
  - Coding agent: save it as `data-work/analyses/<yyyy-mm-dd>-<slug>/analysis.md`. Create `queries/` and `outputs/` for deep.
  - Chat app: do not report a sandbox path as "saved". Hand the file over (see End).
- Apply `run-or-hand-over` for saving.

## End (every flow step)

Quick depth has no files: skip steps 1, 3 and 4, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta.
2. Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app, even if you can write files in a sandbox.
3. Chat app: offer the updated `analysis.md` (and `readout.md` when it exists) as a download. If you cannot, print it as one block. Say: "Save this to your Project files so the next step, in any chat, can read it."
4. Coding agent: the files are already saved under `data-work/`. Say where.
5. Name the next step: `/plan-analysis`.

## Done when

The clarified question, question type, audience, depth (with its reason) and assumptions are written, and the user confirmed them. Then name the next step: `/plan-analysis`.

## Do not

- Do not start any analysis or query.
- Do not ask more than 3 questions per round.
- Do not ask a question the data map or the user already answered. Do not ask any question twice.
- If the ask is already clear, say "No questions needed", write it up and move on. Do not invent questions.
