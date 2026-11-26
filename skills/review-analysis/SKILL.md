---
name: review-analysis
description: Review a finished analysis, yours or anyone's, for technical soundness, business fit and claim wording, give a verdict, and check the draft readout and mark it final. Use only when the user runs /review-analysis or explicitly asks to review an analysis.
---

# /review-analysis

Be a sceptical colleague. Critique the work, never the person. Say "no material issues" when that is true.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Start (every flow step)

1. Check for `DATA-MAP.md`, `analysis.md` and `readout.md` (in `data-work/` in the current folder, then upward; in the Project files; attached; or pasted). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. If the review is of a flow analysis and there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and attach it to this chat." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Never offer it again if Meta shows a `Setup choice`. For an analysis pasted from outside the flow, say there is no map in one line and continue.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. A pasted analysis from anyone is also fine: review it as it is. If there is no ladder log or spec, review the claim and the method anyway and note what is missing. Match the analysis to the ask by its folder or slug (`data-work/analyses/<YYYY-MM-DD>-<slug>/`). If more than one analysis could be the one, ask which. Never resume one silently.
4. Read the Progress line in Meta, if there is one, and resume from it. A pasted analysis with no Meta is reviewed at standard depth unless the user says otherwise. When resuming, refresh every line that is now out of date before you go on, and show each as a "was" and "now" pair. Examples: "no DATA-MAP.md, so inline" in Meta after a map now exists, an old hint in the claim ceiling line, a Progress line that points at a finished step.

## Fresh context: review from the files only

A review in the same context as the analysis is biased by it. Review from the files only: `analysis.md`, `readout.md`, `DATA-MAP.md` and the data. Never from chat memory. If the chat holds something the files do not, it does not count until it is in a file.

- If you can start a subagent with fresh context, you may run the review there, passing only those files. This is optional: never rely on it.
- At standard and deep depth, the best route is a new chat. In a Claude or ChatGPT Project, the data, `DATA-MAP.md`, `analysis.md` and `readout.md` sit in the Project files, so a new chat in that Project needs nothing attached.
- A same-chat review is allowed. Keep the files-only stance: re-read the files, do not lean on what was said earlier.
- Quick depth: a same-chat review is fine.
- The review always recomputes the 3 to 5 headline numbers by an independent route and spot-checks 1 or 2 rungs (step 5). It checks; it does not rebuild the analysis. Use the code in the "Appendix: Review pack" of `analysis.md` to see how each number was made, then compute it another way.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default with its reason. A hedge is not a default: never "recommended if you have one", "TBC" or "C if unknown". Pick a real option and say why. Show any tree, table or draft a question refers to before you ask it (never ask "which hypothesis paths?" before the tree is on screen). Each option says what it means in a few words (for example "H1.1: holds in each month"). An option that needs data the map says is missing says so in the option text (for example "needs the visit marker; the map says it is unknown"). Use the environment's multiple-choice question tool for every round if it has one (one card per question, recommended option first, room for the user's own answer); otherwise list the options as text. Wait for answers. Never assume silently. When an answer conflicts with an earlier one or the data map, or does not make sense, say so plainly and ask one question at a time until it is clear. Never ask the same question twice.
- `question-types`: name the type. Every claim is checked against its ceiling. No "caused" without a randomised experiment or a credible causal design that passed its checks.
- `assumptions`: flag any high-impact row still `open` when results are reported. Alternatives are required for high-impact rows. Standard and deep depth always show the full 7-column table (id, assumption, why unavoidable, likely alternatives, impact if wrong, how to check, status). Never drop columns.
- `viz` (experimental): for each chart, check that the title states a takeaway at or below the ceiling, axes carry units, bars start at zero, uncertainty is shown, there are no dual axes and no 3D, colours are colour-blind safe, and compared panels share a scale. In a readout: at most 3 charts for exec, one annotation on the key moment, image files linked by their real path with alt text.
- Hypothesis status: Judge each node against its own "would support it" and "would refute it" conditions, never against the parent's direction. A child that tests robustness ("the result holds in each month", "holds on the raw count") is `supported` when the result held, whatever the result was, and `refuted` only when it did not hold. Check every status in the Hypotheses section against its own conditions and the named result, and fix a wrong one.
- `validation-ladder`: check the ladder log. The data-check floor ran at every depth. Each check and rung has an expected result, an actual result and pass or fail. Rungs 2 to 4 compare against an independent path (raw rows or a separate query), not the frame the table was built from. Reconcile to a trusted number.

## Steps

1. **State the claim** in one sentence: what is said to be true, and what should be done about it.
2. **Name the question type** and its ceiling.
3. **Technical review.** Ask each item only if the analysis gives a reason.
   - Grain: what is one row after each join? Can a join fan out and double count?
   - Join type: does a left join become an inner join through a where filter?
   - Denominator: who is in it? Does it match the numerator population?
   - Filters and windows: same dates, time zone and status filters on both sides of a comparison?
   - Dedup: unique ids, test or internal users, bots, returned or cancelled orders.
   - Definitions: same metric definition in both periods or arms?
   - Nulls: how treated? Do they drop rows silently?
   - Sample: size, selection, survivorship, who is missing.
   - Stats: is there an interval or test? Is the number practically big, not only significant?
   - Spec match: do the results match the analysis table spec (grain, filters, row count)?
   - Floor and ladder: did the data-check floor run (table audit, one entity across tables, one day, daily series, joins, category totals, assumption checks, reconcile)? Was each rung run and logged? Does each of rungs 2 to 4 compare against an independent path? A rung that compares the table with the frame it was built from tested only the aggregation: report it as weaker than logged.
   - Method card: open the `question-types` file for the question type and find the card for the method used (if the file will not open, use the compact cards in the `question-types` skill). Check the analysis against every item under "Checks that must pass". A check that was not run, or that failed, is an issue, and the claim allowed drops.
   - Hypotheses: does every node in the Hypotheses section have a status? Is each `supported` or `refuted` node backed by a named result in Results? **Check every status against the node's own "would support it" and "would refute it" conditions**, using the result: judge each node against its own conditions, never against the parent's direction. A robustness child ("holds in each month", "holds on the raw count") whose result held is `supported`, whatever the result was. Fix each wrong status in `analysis.md` and show it as a "was" and "now" pair with one line why (was: H1.1 refuted; now: H1.1 supported, because the sign held in all 3 months). If a node's wording depends on the parent's direction, reword it the same way. Is any `open` or `parked` node worded as a finding in the readout? A supported hypothesis still stays under the claim ceiling.
   - Decisions: do the Decisions answers match what the analysis used (for example, the window the user said)? A mismatch is an issue.
   - Charts: if the analysis or the readout has charts, apply the `viz` checks to each. Report only the fails.
   - Review pack: does the "Appendix: Review pack" hold the exact code and source for each headline number? A missing entry is an issue: the number cannot be traced.
4. **Business review.** Ask what leadership will ask.
   - Decision: what will be done differently because of this? If nothing, why was it run?
   - Size: the effect in money, users or orders per month. Big enough to act on?
   - Baseline: compared with what, and is that right?
   - Cause: does the story fit the numbers, or was it added afterwards?
   - Segments: who gains and who loses? Does a total hide a bad segment?
   - Cost and risk: what does acting cost, and what if the finding is wrong?
   - Durability: lasting, or a launch spike or seasonal blip?
   - Next step: what one extra check would change the decision?
   - Scope: does the recommendation cover only what was measured (population, period, metric, place)?
   - Ask match: does the headline answer the question that was asked, or a nearby easier one?
5. **Independent recompute.** Recompute the 3 to 5 headline numbers by a route the analysis did not use (raw rows, or a separate query from the source tables). Spot-check 1 or 2 rungs of the ladder log. Show the numbers side by side. A gap above the tolerance is an issue. This step checks; it does not rebuild the analysis.
6. **Claims check.** Quote every sentence whose wording is above the ceiling, and give the allowed wording.
7. **Assumptions check.** List high-impact rows still `open`.
8. **Leadership questions.** Write the 3 to 5 questions a sceptical leader will ask, with the best answer the analysis supports. Mark an answer "not supported yet" when it is, and name the cheapest way to answer it (one query, a split, a short test, or a person to ask), with its rough effort.
9. **Readout review.** If there is a draft `readout.md`, review it word by word (see below).
10. **Verdict:** `ready`, `ready with caveats`, or `needs rework`, with reasons.

## Readout review

`/run-analysis` writes `readout.md` as a draft. This step makes it final.

1. Read the readout one sentence at a time. For each sentence ask: is the wording at or below the claim ceiling? Does every number match Results and carry its uncertainty? Is every open high-impact assumption in Caveats?
2. Fix each sentence that fails. Show every change as a "was" and "now" pair, with one line why. No exceptions: a summary such as "tightened the wording" is not enough. Example: was "The new page caused the drop." now "Conversion fell after the new page went live. This analysis cannot say why."
3. Leave sentences that pass unchanged. Do not rewrite for taste.
4. Check the layout: Answer in 2 lines, Key numbers with uncertainty (at most 5; for an exec audience, move the rest to the Appendix), Charts (at most 3 for exec, each title a takeaway, one annotation, linked image with alt text), What it means, Caveats, Method in 3 lines, Link, Appendix. The readout must suit the audience in Meta. Portable markdown only: at most 3 callouts as blockquotes with a bold label (`> **Answer:**`, `> **Caveat:**`, `> **Ask:**`), bold only for the one takeaway per section, no app-specific macros.
5. Check the Method section claims only what ran. Compare it with the ladder log and with step 5 of this review. If it says "full validation ladder" or names a check that was weaker than claimed, rewrite it to say exactly what ran.
6. If the verdict is `ready` or `ready with caveats`, set the status line in `readout.md` to `**Status: FINAL**`. If the verdict is `needs rework`, leave it `**Status: DRAFT**` and say what must happen first.
7. Rebuild `readout.docx` from the corrected `readout.md` (same text, charts embedded, whatever document library the sandbox has). Never edit the `.docx` by hand: `readout.md` is the source. With no code tool, hand back `readout.md` and say the `.docx` is not rebuilt.
8. A readout with `**Status: SKELETON**` has no results in it. Say so and send the user to `/run-analysis`. Do not review it as a result.
9. No readout (quick depth, or a pasted analysis): check the pasted claims the same way. Do not create a readout unless asked.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Review | Self-check against the claim ceiling | Technical plus business review | Full review plus leadership questions |
| Readout | Short answer in chat, checked against the ceiling | `readout.md` checked and marked final | `readout.md` plus appendix, checked and marked final |

Quick: run steps 1, 2, 5 and 6 only, in a few lines. The recompute at quick depth covers the one headline number. Check the short answer given in the chat against the ceiling.

## Output format (scan-first)

1. One verdict line.
2. Claim (1 line) and ceiling (1 line).
3. Issues, most important first, as many as earned, up to 8. Fewer is fine. Each issue:

   **N. Short title** `[MUST]` (only if the decision changes when it is answered)
   - Claim it hits: the exact statement or number.
   - Why it matters: one line, with the size if computable from the numbers given.
   - Check: the exact query, split or calculation to run.

4. Leadership questions with answers. Each "not supported yet" names the cheapest way to answer it.
5. Readout changes: a "was" and "now" pair for every sentence changed, then the readout status (draft or final).

## Precision

- Only raise an issue if the analysis shows a reason. A sound step is not an issue.
- If the analysis is sound, say "No material issues" and give at most 3 optional checks, labelled optional. Do not invent must-answers.
- Do not criticise wording that already matches the evidence.
- No praise. No generic checklist.
- Never do arithmetic in your head. Compute it, and show the numbers.

## Writing

Standard and deep: write the Review section of `analysis.md`, save the corrected `readout.md` with its status, rebuild `readout.docx`, and set the analysis status `reviewed`. Apply `run-or-hand-over` for saving. Chat app: see End.

## End (every flow step)

Quick depth has no files: skip steps 1, 3, 4 and 5, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta and the "Where it stands" block at the top (status, answer so far, open risks, next step, how to resume).
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a generic name is overwritten by the next analysis): `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`, `readout.md` and `readout.docx`, and the charts in the same folder. Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>`" (you could not write to Project files; never ask the user to move a file into a Project folder, chat apps do not allow it), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Start each file with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch. Never ask the user to edit a saved file by hand. Say which files changed only after a step that could change files, never on a question turn. For a pasted analysis with no `analysis.md`, the review in the chat is the output. Do not create files unless asked.
4. Stale copies: list each older copy of a file this step handles by its full path, never a bare name beside the live full path (for example never `DATA-MAP.md` next to `data-work/DATA-MAP.md`). Apply one rule every time: a copy is stale when it has the same file name as a live file but sits at another path, or has an older `updated:` line. The list changes only when files change. If this step renamed or replaced a file it created, remove or overwrite the old one where you can, and list only the files you cannot remove. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are already saved under `data-work/`. Name each path.
6. End with the go-ahead question, at every depth, quick included. Use this fixed form:

   > Go ahead?
   > A) Yes, run `/retro-analysis` (recommended)
   > B) Change something (say what)
   > C) Add a check, segment or question

   Wait for the answer. A means start the next step. B or C means make the change in this step, hand back the updated file, and ask again.

## Plan revisions

If the review finds the plan cannot hold (for example, an experiment with no clean control), add a dated row to the Plan revisions log, say what changed and why, and name the step to resume from. No restart.

## Done when

A verdict is given, and the readout is final or the blockers are listed. Next step: `/retro-analysis`.
