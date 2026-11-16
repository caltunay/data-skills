---
name: run-analysis
description: Build the analysis table from the plan, climb the validation ladder, run the method, log results and draft the readout. Use only when the user runs /run-analysis or explicitly asks to run a planned data analysis.
---

# /run-analysis

Build from the spec. Trust nothing until it has climbed the ladder.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Exception: if the ask is small and already clear (quick depth), make the offer in one line and continue with B without waiting. Do not offer it again if the user already chose B for this analysis.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. Quick depth has no file: work from the one-line plan in the chat. If the plan or the spec is missing, say so and suggest `/plan-analysis`.
4. Read the Progress line in Meta and resume from it. Do not redo rungs the ladder log shows as passed. Then read Ask, Assumptions, Plan and Analysis table spec.

## Goal

State the goal before any work, in these words: "Goal: done when the success checks in the plan pass and a draft readout is written." List the success checks from the plan under it. At quick depth say: "Goal: done when the success check passes and the short answer is given."

Then keep going, step after step, until the goal is met. Do not stop to ask "shall I continue?". Stop only for:

- a paste you are waiting for (a handed-over query), or
- an answer you need (an unclear definition, a failed rung that needs a choice, row-level data to save).

When you stop, say what you are waiting for and set the Progress line, for example `Progress: run step 3 of 7, waiting for Q3.1 paste`. When the paste or answer arrives, carry on from that point.

## Rules from the disciplines (in case they do not load)

- `validation-ladder`: one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each rung. Record actual and pass or fail.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Numbered queries (`Q2.1`), one purpose line, expected result first, "Paste the result here." Never call a data tool before the user names the source.
- `shaping-data`: grain first. Count rows before and after every join. Apply filters from the data map. Named steps.
- `data-audit`: check shape, nulls, duplicates, outliers, date coverage, and validate against a trusted number. Write cleaning choices down.
- `stats-tests`: choose the test by data type and design. Report direction, magnitude and uncertainty. Correct for multiple comparisons.
- `question-types`: word every claim at or below the ceiling. One file per question type holds the method cards. Load the card for the chosen method and apply its "Checks that must pass". No "caused" without a randomised experiment or a credible causal design that passed its checks.
- `data-map`: read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask.
- `viz` (experimental): choose the chart by the question. The title states the takeaway, axes carry units, bars start at zero, uncertainty is shown, no dual axes, no 3D, colour-blind safe, same scale when comparing.
- `assumptions`: ask instead of assuming. When you must assume, add a row. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.

## Steps

Set status `running`. Number the steps in the Progress line (step 1 of 7, and so on). Quick depth runs rung 1, the query, and step 5, then gives the short answer. No step 7.

1. **Audit** each new table or extract (apply `data-audit`).
2. **Build** the analysis table from the spec, using the tool file in `shaping-data` for the tool in use. Save queries as numbered files in `queries/` (`q1-1-one-entity.sql`, `q1-2-one-entity-day.sql`, and so on).
3. **Climb the ladder, rungs 1 to 4.** Before each rung, write the expected result. Run the check. Write the actual and pass or fail. A fail means find the cause before going up. If the fix needs a choice (for example, a rule for duplicates), propose it, add an assumption row, and ask.
4. **Run the method.** Open the `question-types` file for the question type and load the method card named in the plan. Apply every item under "Checks that must pass" and log each as pass or fail in Results. If a check fails, the claim allowed drops: say to what.
5. **Reconcile (rung 5).** Compare the headline number to the trusted number from the plan. Compute the gap and compare it with the stated tolerance. Above tolerance: record rung 5 as fail, do not report the number as final, and test likely causes one small check at a time. Never explain a gap with an untested story.
6. **Write findings.** Each finding gets direction, magnitude, uncertainty, and the claim ceiling applied. Update assumption statuses as evidence arrives. List high-impact rows still `open` beside the findings.
7. **Draft the readout.** Write `readout.md` next to `analysis.md`, from `readout.template.md` in this skill's folder. Mark it `Status: draft`.

## Draft readout

One layout. Wording adapts to the audience in Meta (exec: no jargon; data: method detail is welcome).

1. **Answer** in 2 lines.
2. **Key numbers**, each with its uncertainty.
3. **What it means** and the recommendation.
4. **Caveats:** open high-impact assumptions, and the claim ceiling in plain words.
5. **Method** in 3 lines.
6. **Link** to `analysis.md`.

Every sentence stays at or below the claim ceiling. The draft is not final: `/review-analysis` checks it word by word and marks it final. Say so when you hand it over.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Ladder | One entity check plus reconcile | Full ladder | Full ladder plus alternative specification |
| Readout | Short answer in chat | `readout.md` | `readout.md` plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

Deep: rebuild the result with one different specification (another filter, join path or definition) and compare. A gap means a fragile result. Report it. The readout appendix holds the ladder log and the alternative specification.

## Ask, do not assume

If a definition, filter, date or population is unclear, ask (a round of at most 3 questions). If you cannot ask now, add an assumption row and carry on.

## When the plan cannot hold

Examples: no clean control group, a metric that is not available, a sample ratio mismatch, a source that does not reconcile, a method card check that fails. Do not push on. Add a dated row to the Plan revisions log in `analysis.md`: what changed and why. If the change lowers the question type, say what claim is no longer allowed. Then continue from the right step (usually the plan).

## Data safety

Show aggregates by default. Ask before saving row-level data anywhere. Put charts and tables in `outputs/` only when asked or when the plan names one. Apply the `viz` skill to every chart before saving it. Never store credentials.

## Output

- Standard and deep: update Results in `analysis.md` (ladder log, method checks, findings) and write the draft `readout.md`. This step sets status `running` when it starts and leaves it at `running`. Only `/review-analysis` sets `reviewed`.
- Quick: print the answer, the one check and its result, the ceiling, and open assumptions. No file.
- Apply `run-or-hand-over` for saving. Chat app: see End.

## End (every flow step)

Quick depth has no files: skip steps 1, 3 and 4, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta, for example `Progress: run done, draft readout written, next /review-analysis`.
2. Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app, even if you can write files in a sandbox.
3. Chat app: offer the updated `analysis.md` and `readout.md` as downloads. If you cannot, print each as one block. Say: "Save these to your Project files so the next step, in any chat, can read them."
4. Coding agent: the files are already saved under `data-work/`. Say where.
5. Name the next step: `/review-analysis`.

## Done when

The goal is met: the ladder is complete for the depth, the success checks pass (or a gap is explained and logged), findings are written with the ceiling applied, and the draft readout is written.

## Do not

- Do not jump to the final query.
- Do not report a number that failed a rung.
- Do not write causal wording without a causal design.
- Do not clean data silently.
- Do not stop between steps unless you are waiting for a paste or an answer.
