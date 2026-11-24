---
name: grill-the-ask
description: Turn a vague stakeholder ask into a clear, scoped question with stated assumptions before any analysis. Use only when the user runs /grill-the-ask or explicitly asks to clarify or grill a data request.
---

# /grill-the-ask

Clarification is the most important part of data work. Ask before you assume.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.
- **Never analyse in this step.** When files are attached, note only what they contain: the columns, possible duplicate keys, the date range. Never report early findings: no patterns, trends, drops, spend, segments or "I noticed". Do not put an observed pattern in an answer option, the clarified question or the claim line. It anchors the analysis. Findings come from `/run-analysis`.
- **Log every answer word for word** in the Decisions section of `analysis.md`. After each round, echo the answers back exactly, then move on. Never paraphrase: "this week" must not become "later".

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Exception: if the ask is small and already clear (quick depth), make the offer in one line and continue with B without waiting. Record the answer in Meta as `Setup choice` (A, B, or map found). Never offer setup again once Meta shows a choice: skip this step.
3. **Match the ask to its analysis.** Look at the folders in `data-work/analyses/<YYYY-MM-DD>-<slug>/`, by folder name and slug. If an analysis of the same ask already exists, ask, as a clickable card with the folder as the first option: "Continue `<folder>`, or start a new analysis?" Recommend continue when its status is not `retro done`, with that reason, and start new when it is. **Never resume silently.** A new ask needs no `analysis.md`. If the user is resuming an ask and `analysis.md` is not found (for example, a new chat), ask them to attach it before re-asking anything.
4. If the user continues, read the Progress line in Meta and resume from it. Skip every question the file or the data map already answers. When resuming, refresh every line that is now out of date before you go on, and show each as a "was" and "now" pair. Examples: "no DATA-MAP.md, so inline" in Meta after a map now exists, an old hint in the claim ceiling line, a Progress line that points at a finished step. If the user starts a new analysis, make a new folder and a new `analysis.md`, and grill it from the start.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default (never a hedge such as "C if unknown"). Wait for answers. Never assume silently. When an answer conflicts with an earlier one or the data map, or does not make sense, say so plainly and ask one question at a time until it is clear. Use the environment's multiple-choice question tool for each round if it has one (one question per card, recommended option first); otherwise list the options as text.
- `assumptions`: write each assumption in the assumptions table. Only real assumptions: claim rules go in the ceiling. Rate impact honestly: anything that moves the headline by about 5% or more is High (a month-length difference of about 10% is never Low). High-impact rows need 1 to 3 likely alternatives. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.
- `question-types`: six types: descriptive, exploratory, inferential, predictive, causal, mechanistic. Each has a claim ceiling. No "caused" without a randomised experiment or a credible causal design. A "why" question starts as descriptive or exploratory. It is causal only when a design fits. Say so when you propose the type.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand. Never call a data tool before the user names the source.
- `data-map`: read `DATA-MAP.md` before writing queries. Flag entries older than 90 days or contradicted by data, then ask.

## Steps

1. Take the ask verbatim. Store it unchanged. Then check the route, before any question:
   - The whole ask is a design with no data needed yet ("design an A/B test", "define how we measure X"): send it to `/wayfinder-data` (fast path) with one line why. Stop.
   - The ask is project-sized (several questions, unknowns, weeks of work): send it to `/wayfinder-data` with one line why. Stop. One question with a decision attached stays here.
2. Run rounds of questions, each with options and one real recommended default (never a hedge, the deadline included). After each round, write the questions and the user's answers word for word into Decisions, and echo the answers back exactly before the next round. If the data map has a Goals section, ask how the ask links to a goal (mission, north star metric or a target metric) and record it in Meta as `Goal link`. In a chat app, if no earlier answer is visible, ask once: "Hand files to you as downloads, or save them to a document tool you use (for example a drive, a wiki or a notes app)?" Use only a tool the user names. Record it in Meta as `Files`. Cover: goal, the decision it feeds, requester, question type, metric, population, time window (and the comparison window, see step 5), constraints, deadline, and audience (who reads the result: exec, product, data or mixed).
3. **Never ask the same question twice in a session.** Before each round, list what is already answered: in the ask, in `analysis.md`, in the data map, and in earlier answers. A reworded question is the same question. If an answer was unclear, quote it and ask only about the unclear part.
   **When an answer does not fit.** If an answer conflicts with an earlier one, contradicts the data map, or does not make sense, say so plainly ("This does not fit X because Y"). Switch to one question at a time until it is clear. Then return to rounds.
4. Propose the question type with its ceiling. Confirm it with the user. For an ask that wants a cause ("did X work", "prove", "impact of"), ask what comparison exists: a randomised holdout, an untreated group, a cut-off rule, or only a before and after. The answer decides whether a causal claim is reachable.
5. **Comparison windows and seasonality.** When the ask compares periods ("down this month", "last 30 days against the 30 before"), recommend a comparison that handles seasonality: the same weeks last year, or the same weekdays in both windows. If you recommend a plain back-to-back comparison (for example, because there is no year of history), flag in the option itself that it ignores seasonality, and what that could hide (a holiday, a month-end, a 28-day against a 31-day month).
6. Choose the depth after round 1 and propose it with a one-line reason: **quick**, **standard** or **deep**. If the depth is quick, stop asking: what is still unknown becomes an inline assumption. Example: "Depth: standard, because the number feeds a budget decision but is not a test readout." The user can override.
   - Quick: a small, low-risk ask, one number or one chart.
   - Standard: the usual ask.
   - Deep: high stakes, a decision with real cost, or a test readout.
7. Write down every assumption you have to make. At standard and deep depth, show the full 7-column assumptions table. Only real assumptions go in the table: a choice that could be wrong and that the work depends on. Claim rules ("spend is a hypothesis, not a cause") are not assumptions: they go in the claim ceiling line in Meta. Rate impact by size, honestly (see the `assumptions` rule below).
8. Fill Meta in full, including `Setup choice`, `Goal link` and `Files`. Requester and Date are never blank: Requester is the person or role the user names (ask in round 1 if the ask does not say; a role is fine, and never guess a name). Date is today. Also fill the claim ceiling in one line.
9. Restate the clarified question in one or two sentences. Ask the user to confirm it.

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
- **Standard and deep:** build `analysis.md` from `analysis.template.md` (in this skill's folder). Fill Meta (including audience and the Progress line), Ask, Decisions and Assumptions. Start the file with `format: v1` and `updated: YYYY-MM-DD HH:MM`. Set status to `grilling`.
  - The analysis folder is `data-work/analyses/<YYYY-MM-DD>-<slug>/` (today's date, a short slug). Write it in Meta as `Folder`. Coding agent: save `analysis.md` there and create `queries/` and `outputs/` for deep.
  - Chat app: never report a sandbox path as "saved". Hand the file over with the full path (see End).
- Apply `run-or-hand-over` for saving.

## End (every flow step)

Quick depth has no files: skip steps 1, 3, 4 and 5, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a generic name is overwritten by the next analysis): `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md` (and `readout.md` in the same folder when it exists). Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Start each file with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch. Never ask the user to edit a saved file by hand.
4. Stale copies: if an older copy of a file exists elsewhere in the Project (for example `analysis (6).md` at the top level, or a file in `claude/`), name it and say it is stale. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are already saved under `data-work/`. Name each path.
6. End with the go-ahead question, at every depth, quick included. Use this fixed form:

   > Go ahead?
   > A) Yes, run `/plan-analysis` (recommended)
   > B) Change something (say what)
   > C) Add a check, segment or question

   Wait for the answer. A means start the next step. B or C means make the change in this step, hand back the updated file, and ask again.

## Done when

The clarified question, question type, claim ceiling, requester, date, audience, depth (with its reason) and assumptions are written, and the user confirmed them. Then name the next step: `/plan-analysis`.

## Do not

- Do not start any analysis or query. Do not report what the files show.
- Do not ask more than 3 questions per round.
- Do not ask a question the data map or the user already answered. Do not ask any question twice.
- If the ask is already clear, say "No questions needed", write it up and move on. Do not invent questions.
