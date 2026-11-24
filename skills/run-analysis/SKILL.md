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

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Exception: if the ask is small and already clear (quick depth), make the offer in one line and continue with B without waiting. Meta records the choice as `Setup choice`. Never offer setup again once it is set. If Meta has no choice (an older file), write it there now.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. Quick depth has no file: work from the one-line plan in the chat. If the plan or the spec is missing, say so and suggest `/plan-analysis`. Match the analysis to the ask by its folder or slug (`data-work/analyses/<YYYY-MM-DD>-<slug>/`). If more than one analysis could be the one, ask which. Never resume one silently.
4. Read the Progress line in Meta and resume from it. Do not redo rungs the ladder log shows as passed. Then read Ask, Assumptions, Plan and Analysis table spec. When resuming, refresh every line that is now out of date before you go on, and show each as a "was" and "now" pair. Examples: "no DATA-MAP.md, so inline" in Meta after a map now exists, an old hint in the claim ceiling line, a Progress line that points at a finished step.

## Goal

State the goal before any work, in these words: "Goal: done when the success checks in the plan pass and a draft readout is written." List the success checks from the plan under it. At quick depth say: "Goal: done when the success check passes and the short answer is given."

Then keep going, step after step, until the goal is met. Do not stop to ask "shall I continue?". Stop only for:

- a paste you are waiting for (a handed-over query), or
- an answer you need (an unclear definition, a failed rung that needs a choice, row-level data to save).

When you stop, say what you are waiting for and set the Progress line, for example `Progress: run step 3 of 7, waiting for Q3.1 paste`. When the paste or answer arrives, carry on from that point.

## Rules from the disciplines (in case they do not load)

- `validation-ladder`: the data-check floor runs at every depth, quick included (table audit, one real entity across tables, one day, daily series, join checks, category totals, assumption checks, reconcile). Then one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each check. Record actual and pass or fail. Rungs 2 to 4 compare against an independent path (raw rows or a separate query), never against the frame the table was built from.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand. Numbered queries (`Q2.1`), one purpose line, expected result first, "Paste the result here." Never call a data tool before the user names the source.
- `shaping-data`: grain first. Count rows before and after every join. Apply filters from the data map. Named steps.
- `data-audit`: check shape, nulls, duplicates, outliers, date coverage (with the daily series), and validate against a trusted number. Write cleaning choices down.
- `stats-tests`: choose the test by data type and design. Report direction, magnitude and uncertainty. Correct for multiple comparisons.
- `question-types`: word every claim at or below the ceiling. One file per question type holds the method cards. Load the card for the chosen method and apply its "Checks that must pass" (the plan's success checks hold a copy; the compact cards in the `question-types` skill are the fallback). No "caused" without a randomised experiment or a credible causal design that passed its checks.
- `data-map`: read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask.
- `viz` (experimental): choose the chart by the question. The title states the takeaway, axes carry units, bars start at zero, uncertainty is shown, no dual axes, no 3D, colour-blind safe, same scale when comparing. In a readout: at most 3 charts for exec, one annotation on the key moment, saved as image files in the analysis folder and linked by their real path with alt text.
- `assumptions`: ask instead of assuming. When you must assume, add a row. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.

## Steps

Set status `running`. Number the steps in the Progress line (step 1 of 8, and so on). Quick depth runs the compact floor (step 1), the query, and step 5, then gives the short answer. No steps 7 to 9. The floor is never skipped.

1. **Data-check floor** for every table used (apply `data-audit` and `validation-ladder`). Each check states its expected result first:
   1. Table audit: row count; distinct keys against rows (duplicates); null rate of every column used; min and max dates (coverage, future dates); distinct values of every category column used (flag unexpected labels).
   2. One real entity across tables: pick a specific id and show its rows in every table used. Do the values make sense (for example, sign-up before first order)?
   3. One day, all entities: the total for one day, in a plausible range.
   4. Daily series across the full window: gaps, spikes, zero days. For any "X dropped" question this is mandatory and runs before any segment scan. A logging break is the most common cause of a drop.
   5. Join checks: row counts before and after each join, key match rate (orphans), fan-out.
   6. Category totals sum to the overall total.
   7. Assumption checks: every assumption a query can test gets one (for example, an hour-of-day distribution for a time zone assumption).
   8. Reconcile to the trusted number (done in step 5).
   Quick depth: the same checks in compact form, one small query each, results in one table. In hand-over mode, batch the checks into numbered groups so the user pastes once per group, not once per query.
2. **Build** the analysis table from the spec, using the tool file in `shaping-data` for the tool in use. Save queries as numbered files in `queries/` (`q1-1-one-entity.sql`, `q1-2-one-entity-day.sql`, and so on).
3. **Climb the ladder, rungs 1 to 4.** Before each rung, write the expected result. Run the check. Write the actual and pass or fail. Rungs 2 to 4 test the data, not only the aggregation: recompute from raw rows or with a separate query that does not use the analysis table or the frame it was built from, and compare. A fail means find the cause before going up. If the fix needs a choice (for example, a rule for duplicates), propose it, add an assumption row, and ask.
4. **Run the method.** Open the `question-types` file for the question type and load the method card named in the plan. Apply every item under "Checks that must pass" and log each as pass or fail in Results. If a check fails, the claim allowed drops: say to what.
5. **Reconcile (rung 5).** Compare the headline number to the trusted number from the plan. Say which count is compared (raw or cleaned) and why: a trusted number made before your cleaning matches the raw count. Compute the gap and compare it with the stated tolerance. Above tolerance: record rung 5 as fail, do not report the number as final, and test likely causes one small check at a time. Never explain a gap with an untested story.
6. **Write findings.** Each finding gets direction, magnitude, uncertainty, and the claim ceiling applied. Update the status of every hypothesis the finding touches in the Hypotheses section (`supported`, `refuted`, `open` or `parked`), and name the result that shows it. A node is never `supported` or `refuted` without a result. Tell the user which statuses changed. Update assumption statuses as evidence arrives. List high-impact rows still `open` beside the findings.
7. **Write the review pack.** In the "Appendix: Review pack" section of `analysis.md`, for each headline number: the exact SQL or Python that produced it, and its data source (table or file, filters, period). In a chat app `queries/` does not persist, so this is how a fresh reviewer sees the code.
8. **Draft the readout.** Write `readout.md` in the analysis folder next to `analysis.md`, from `readout.template.md` in this skill's folder. Set the status line to `**Status: DRAFT**`. If a skeleton exists (`**Status: SKELETON**`), replace it: keep its layout, fill every placeholder from Results, and leave no XX or [segment] behind.
9. **Build `readout.docx`.** Produce `readout.docx` from the same text as `readout.md`, with the charts embedded, so it opens in Word and Google Docs. Use whatever document library the sandbox has. `readout.md` stays the source: the review edits it, then rebuilds the `.docx`. If there is no code tool, give `readout.md` and the chart code only, and say so in one line.

## Draft readout

One layout. Wording adapts to the audience set in grilling (Meta). The default readout serves that audience. `/storytell` is for other audiences and formats, not a fix for a readout that ignored its audience.

1. **Answer** in 2 lines.
2. **Key numbers**, each with its uncertainty. At most 5. For an exec audience this limit is strict. Every other number goes to the Appendix.
3. **Charts** (apply `viz`). At most 3 in an exec readout. Each title states the takeaway. One annotation on the key moment (for example, a marker on the day a step happened). A chart replaces number rows that say the same thing, which keeps the 5-number limit. Charts are image files in the analysis folder (a coding agent uses its `outputs/` subfolder), saved at their full path. The link in `readout.md` is the chart's real path relative to the readout (`<chart>.png`, or `outputs/<chart>.png` only when that folder exists), never `outputs/` in a chat app. In a chat app, hand each chart over in one of the three forms. In hand-over mode, give the chart spec plus ready-to-run code. No chart is fine when a number says it better.
4. **What it means** and the recommendation.
5. **Caveats:** open high-impact assumptions, and the claim ceiling in plain words.
6. **Method** in 3 lines. Claim only what ran: name the checks that passed, as they were run. Never write "full validation ladder" if a rung was skipped, failed, or compared only against the frame the table was built from.
7. **Link** to `analysis.md`.
8. **Appendix:** the other numbers, segment tables, the ladder summary.

The `.docx` carries the same text and the charts. Portable markdown only for `readout.md`, no app-specific macros:

- Callouts are blockquotes with a bold label: `> **Answer:** ...`, `> **Caveat:** ...`, `> **Ask:** ...`. At most 3 in the whole readout, so they stand out.
- The status is a bold label at the top: `**Status: DRAFT**` or `**Status: FINAL**`.
- Bold only the one takeaway per section.

Every sentence stays at or below the claim ceiling. The draft is not final: `/review-analysis` checks it word by word and marks it final. Say so when you hand it over.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Ladder | Compact data-check floor (never skipped) | Full floor plus full ladder | Full floor, full ladder, plus alternative specification |
| Readout | Short answer in chat | `readout.md` | `readout.md` plus appendix |
| Files | None | `analysis.md`, `readout.md` | Full analysis folder |

Deep: rebuild the result with one different specification (another filter, join path or definition) and compare. A gap means a fragile result. Report it. The readout appendix holds the ladder log and the alternative specification.

## Ask, do not assume

If a definition, filter, date or population is unclear, ask (a round of at most 3 questions). If you cannot ask now, add an assumption row and carry on.

## Spec corrections

Every correction to the plan or the spec found while running is a dated row in the Plan revisions log, even a small one (for example, "6 channels expected, 5 found"; "expected about 40,000 rows, found 38,950"). Never write "(none)" and then add notes below it.

## When the plan cannot hold

Examples: no clean control group, a metric that is not available, a sample ratio mismatch, a source that does not reconcile, a method card check that fails. Do not push on. Add a dated row to the Plan revisions log in `analysis.md`: what changed and why. If the change lowers the question type, say what claim is no longer allowed. Then continue from the right step (usually the plan).

## Data safety

Show aggregates by default. Ask before saving row-level data anywhere. Put charts and tables in the analysis folder only when asked, when the plan names one, or when the readout uses one. Apply the `viz` skill to every chart before saving it. Never store credentials.

## Output

- Standard and deep: update Results in `analysis.md` (ladder log, method checks, findings), update Hypotheses, write the Review pack appendix, and write the draft `readout.md` and `readout.docx`. This step sets status `running` when it starts and leaves it at `running`. Only `/review-analysis` sets `reviewed`.
- Quick: print the answer, the compact floor table, the ceiling, and open assumptions. No file.
- Apply `run-or-hand-over` for saving. Chat app: see End.

## End (every flow step)

Quick depth has no files: skip steps 1, 3, 4 and 5, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta, for example `Progress: run done, draft readout written, next /review-analysis`.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a generic name is overwritten by the next analysis): `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`, `readout.md` and `readout.docx`, and the charts in the same folder. Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Start each file with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch. Never ask the user to edit a saved file by hand.
4. Stale copies: if an older copy of a file exists elsewhere in the Project (for example `analysis (6).md` at the top level, or a file in `claude/`), name it and say it is stale. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are already saved under `data-work/`. Name each path.
6. End with the go-ahead question, at every depth, quick included. Use this fixed form:

   > Go ahead?
   > A) Yes, run `/review-analysis` (recommended)
   > B) Change something (say what)
   > C) Add a check, segment or question

   At standard and deep depth, A recommends a fresh review, because a review in the same context is biased by it: "A) Yes: start `/review-analysis` in a new chat (recommended). In a Claude or ChatGPT Project, make sure the data, `data-work/DATA-MAP.md`, `analysis.md` and `readout.md` are in the Project files first, then open a new chat in that Project; nothing needs attaching." If you can start a subagent with fresh context, you may run the review there instead, passing only those files. This is optional: never rely on it. A same-chat review stays allowed. Quick depth: a same-chat review is fine.

   Wait for the answer. A means start the next step. B or C means make the change in this step, hand back the updated file, and ask again.

## Done when

The goal is met: the floor and the ladder are complete for the depth, the success checks pass (or a gap is explained and logged), findings are written with the ceiling applied, the review pack holds the code for each headline number, and the draft readout is written (`readout.md` and `readout.docx`).

## Do not

- Do not jump to the final query.
- Do not report a number that failed a rung.
- Do not skip the data-check floor, at any depth.
- Do not run a segment scan on a drop before the daily series check.
- Do not write causal wording without a causal design.
- Do not clean data silently.
- Do not leave a placeholder (XX%, [segment]) in a draft readout.
- When you stop for an answer, log it word for word in Decisions and echo it back before you carry on.
- Do not stop between steps unless you are waiting for a paste or an answer.
