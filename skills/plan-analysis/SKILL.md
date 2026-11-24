---
name: plan-analysis
description: Turn a clarified ask into a chosen plan, an analysis table spec and success checks. Use only when the user runs /plan-analysis or explicitly asks to plan a data analysis.
---

# /plan-analysis

Record decisions already made. Do not invent new ones.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Exception: if the ask is small and already clear (quick depth), make the offer in one line and continue with B without waiting. Meta records the choice as `Setup choice`. Never offer setup again once it is set. If Meta has no choice (an older file), write it there now.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. Quick depth has no file: work from the clarified question in the chat. If there is no clarified question at all, say so and suggest `/grill-the-ask`.
4. Read the Progress line in Meta and resume from it. Then read Meta, Ask and Assumptions.

## Rules from the disciplines (in case they do not load)

- Hypotheses (part of this step, not a separate skill): each node needs a support condition, a refute condition and a status (open, supported, refuted, parked). At most 3 levels and about 12 nodes.
- `assumptions`: every new assumption goes in the table. High-impact rows need 1 to 3 likely alternatives. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.
- `question-types`: name the type and its claim ceiling. Choose a method that can reach the claim the decision needs. If it cannot, say so now. One file per question type holds the method cards; the `question-types` skill holds a compact line per method as a fallback. Copy the card's checks into the success checks at plan time. For a causal question, go down the causal method selector: randomised test, then difference-in-differences, regression discontinuity, synthetic control, interrupted time series, instrumental variables, matching or weighting, uplift. If none fits, say so and offer the best descriptive path.
- `shaping-data`: design the analysis table spec before any query, without reference to a tool. Grain first.
- Easy solution first: try the simplest method that could answer the question.

## Steps

1. Confirm the question type and the decision. State the claim ceiling in one line. Check Meta: Requester and Date are filled. If not, fill them now (ask for the requester if it is unknown).
2. **Hypothesis tree (standard and deep), before the method options.** Write the hypotheses the work will test, as a tree: H1, H2, and so on. Each has children (H1.1, H1.2, then H1.2.1). Three levels at most and about 12 nodes in all. For each node write: what finding would **support** it, what would **refute** it, and which child it **leads to**. A pure count with nothing to explain has one hypothesis: the expected range, and the check that would break it. Show the tree as a table (id, hypothesis, would support it, would refute it, leads to, status). Ask which paths to follow (recommend one, with a reason) and mark the rest `parked`. Write it to the "Hypotheses" section of `analysis.md` with a status per node: `open`, `supported`, `refuted` or `parked`. `/run-analysis` updates the statuses. `/review-analysis` checks them. Quick depth: a flat list of up to 3 hypotheses, in the chat.
3. **Load the method cards.** Open the `question-types` file for the question type. If it will not open (for example, a chat with no file access), use the compact cards in the `question-types` skill itself: one line each for when to use, checks that must pass, and claim allowed. For each candidate method, check the card's "When to use" and "Data needed" against what the user has. Ask the user about the data. Do not query it. Drop candidates the data does not fit, and say why.
4. List the options that remain (see depth table). For each: method, trade-offs, effort, and the strongest claim it can support. Start from each card's "Simplest version first".
5. Recommend one. Say why in two lines. Confirm with the user. A short card means an advanced method: tell the user it needs a specialist review before shipping.
   - If no method can reach the claim the decision needs, say so now. Lower the question type in Meta, add a dated row to Plan revisions (what changed, why), and state the new ceiling.
6. Write the **chosen plan**: the method card by name, then the steps, in order.
7. Write the **analysis table spec**:
   - grain (what one row means)
   - keys
   - measures and dimensions
   - time column and window, and the comparison window. If periods are compared, use one that handles seasonality (the same weeks last year, or the same weekdays) or write in the plan that it does not
   - filters and exclusions (from the Rules section of `DATA-MAP.md`)
   - joins: use the safe joins in the map, and name every fan-out trap the spec must avoid
   - tidy (long) or wide, and why
   - context columns
   - expected row count or range
8. Set **success checks** up front: what must be true for the result to be trusted. Include the trusted number to reconcile to and the tolerance. Say which count must match it, raw or cleaned, and why. Example: "Raw paid orders within 1% of 120,400 (finance report), because the report counts before our dedup." Copy every item under the card's "Checks that must pass" into the success checks now, word for word. Never defer them to the run ("checks from the card" is not a success check). If the card file will not open, copy the line from the compact cards.
9. Add any new assumptions to the table. Each "Key assumption" on the card that the data cannot confirm becomes a row.
10. **Readout skeleton (optional, standard and deep).** Offer it: "Draft the readout skeleton now, to check that the story would answer the decision?" If yes, write `readout.md` from the readout template with placeholders only (XX%, [segment], [date]). Never an invented number. Set the status line to `**Status: SKELETON**`. Read it against the decision in Ask: would this layout answer it? Change the plan if not. `/run-analysis` replaces the skeleton with the draft.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Hypotheses | Flat list, up to 3 | Tree, about 12 nodes at most | Tree, about 12 nodes at most |
| Plan | One line: method plus success check | 2 to 4 options, chosen plan | Options, chosen plan, power or MDE where relevant |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

Quick: skip the tree (give a flat list of up to 3 hypotheses in the chat) and the options. Give one line: the method card by name, plus the success check. No spec table, no file.

For experiments at deep depth, state the MDE, the power, the runtime and the unit of randomisation.

## Output

- Write Hypotheses, Plan and Analysis table spec into `analysis.md`. Log each question you asked and the user's answer word for word in Decisions, and echo the answers back exactly after each round. Set status `planned` and update the Progress line.
- Quick: print the one-line plan and success check. No file.
- Apply `run-or-hand-over` for saving. Chat app: see End.

## End (every flow step)

Quick depth has no files: skip steps 1, 3, 4 and 5, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a generic name is overwritten by the next analysis): `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md` (and `readout.md` in the same folder when it exists). Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Start each file with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch. Never ask the user to edit a saved file by hand.
4. Stale copies: if an older copy of a file exists elsewhere in the Project (for example `analysis (6).md` at the top level, or a file in `claude/`), name it and say it is stale. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are already saved under `data-work/`. Name each path.
6. End with the go-ahead question, at every depth, quick included. Use this fixed form:

   > Go ahead?
   > A) Yes, run `/run-analysis` (recommended)
   > B) Change something (say what)
   > C) Add a check, segment or question

   Wait for the answer. A means start the next step. B or C means make the change in this step, hand back the updated file, and ask again.

## Plan revisions

When this step or a later step finds the plan cannot hold, or a spec item was wrong (for example, "6 channels expected, 5 found"), add a dated row to the Plan revisions log: date, what changed, why. Every correction is a row. Never write "(none)" and then add notes below it. When the user comes back here after a revision, read the log, change only what the revision touches, and keep the rest of the plan. No restart.

## Done when

The user has agreed the plan, the spec and the success checks. Next step: `/run-analysis`.

## Do not

- Do not run queries.
- Do not offer options that cannot support the claim the decision needs, unless you say so.
- Do not choose a complex method when a simple one answers the question.
