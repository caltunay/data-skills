---
name: storytell
description: Rewrite a final analysis readout for one audience (exec, product, data or mixed) and one format (doc, chat message, email or slide outline), without raising any claim. Use only when the user runs /storytell or explicitly asks to turn a finished readout into an audience version.
---

# /storytell

Same facts, new shape. The audience changes the words, never the claim.

Experimental (v0.2).

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md`, `analysis.md` or `readout.md` count as said by the user.
- This step runs no queries and adds no numbers. Every number comes from `readout.md` or `analysis.md`.

## Start (every flow step)

1. Check for `DATA-MAP.md`, `analysis.md` and `readout.md` (in `data-work/` in the current folder, then upward; in the Project files; attached; or pasted). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. No `DATA-MAP.md` is fine here: this step does not need it. Say so in the same line. Do not offer setup.
3. If `readout.md` or `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before asking anything else. A readout pasted from outside the flow is fine: then ask for the question type or the claim ceiling if the paste does not state it.
4. Read the Progress line in Meta and the readout's `Status`.
   - `**Status: FINAL**` (or the older `Status: final`): continue.
   - `**Status: SKELETON**`: it holds placeholders, not results. Send the user to `/run-analysis`. Stop.
   - `**Status: DRAFT**` (or the older `Status: draft`), or no status: say "This readout is not final. It has not been checked against the claim ceiling." Suggest `/review-analysis` first. Continue only if the user says to, and then mark the output `Status: draft, from an unreviewed readout`.

## Rules from the disciplines (in case they do not load)

- `question-types`: six question types, each with a claim ceiling. A claim never goes above what its method supports. No "caused" without a randomised experiment or a credible causal design that passed its checks. Exploratory outputs are hypotheses, never findings.
- `viz` (experimental): choose the chart by the question. The title states the takeaway, axes carry units, bars start at zero, uncertainty is shown, no dual axes, no 3D, colour-blind safe, same scale when comparing.
- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default (never a hedge such as "C if unknown"). Wait for answers. Never ask twice.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand.

## Steps

1. **Ask audience and format**, in one round. Skip a question the user already answered. The audience in `analysis.md` Meta is the recommended default.
   - Audience: A) exec, B) product, C) data, D) mixed.
   - Format: A) doc, B) chat message, C) email, D) slide outline.
2. **Find the ceiling.** Read the question type and the "claim ceiling applied" in `analysis.md` Results, and the Caveats in the readout. Write the ceiling down in one line before you draft.
3. **List the facts you may use:** the answer, each key number with its uncertainty, the recommendation, each caveat, each open high-impact assumption. Nothing else goes in.
4. **Draft** in the layout for the format (below), in the words for the audience (below).
5. **Check the draft, sentence by sentence:**
   - Is the answer first?
   - Does every number carry its uncertainty, exactly as in the readout?
   - Is every claim at or below the ceiling? Shorter words must not become stronger words. "Is concentrated in" must not become "is driven by" or "because of".
   - Is every caveat from the readout still there, in plain words?
   - Is there any number, name or reason that is not in the source files? Remove it.
6. **Write** `readout-<audience>.md` next to `readout.md` (for example `readout-exec.md`). First lines: `format: v1`, `updated: YYYY-MM-DD HH:MM`, then the audience, the format, the date, and "Source: readout.md (final)". For the doc and email formats, also produce `readout-<audience>.docx` from the same text, with any charts embedded, using whatever document library the sandbox has. With no code tool, give the `.md` only.

## Words by audience

| Audience | Words | Keep | Cut or move to the appendix |
|---|---|---|---|
| Exec | No jargon. No method names, no "p-value", no "confidence interval": say "likely between X and Y". Under 150 words before the appendix | The answer, 1 to 3 numbers with their range, the recommendation, the main caveat | Method, ladder, segment detail |
| Product | Plain words, product terms the user already uses | The answer, numbers with ranges, what it means for the product, what to test next | Statistical detail |
| Data | Precise terms are welcome | Method, checks passed, intervals, assumptions with ids, the ceiling by name | Nothing. Keep it tight anyway |
| Mixed | Exec version first, then a "Detail" section for product and data readers | Both | Nothing |

Uncertainty in plain words: an interval becomes "likely between X and Y". An exact count stays "exact for the period". A caveat about the ceiling becomes "this shows what happened, not why" (descriptive), "this is a pattern to test, not a finding" (exploratory), or "this holds for the customers and period tested" (experiment).

## Layout by format

- **Doc:** Answer. Key numbers. What it means and the recommendation. Caveats. Method (3 lines). Appendix if needed. Link to `analysis.md`.
- **Chat message:** 3 to 6 lines. Line 1 is the answer. Then the key number with its range, the recommendation, the main caveat, and where the full readout is.
- **Email:** a subject line that states the answer. Then the chat-message content in short paragraphs, and a closing line with the ask or the decision needed.
- **Slide outline:** at most 5 slides. Each slide has a title that states the takeaway, 1 to 3 bullets, and one chart suggestion. For each chart suggestion apply `viz`: name the question, the chart type, the axes with units, and how uncertainty is shown. Slide 1 is the answer. The last slide is caveats and next steps. Do not build the slides or the charts unless asked.

The exec limit applies to every format: under 150 words before the appendix. For a slide outline, count titles and bullets.

## End (every flow step)

1. Update the Progress line in `analysis.md` Meta, for example `Progress: storytell done, readout-exec.md written`.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name: `data-work/analyses/<YYYY-MM-DD>-<slug>/readout-<audience>.md` (and its `.docx` when made) and the updated `analysis.md` in the same folder. Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Hand back whole files, never patches. Never ask the user to edit a saved file by hand.
4. Coding agent: the file is saved next to `readout.md`. Name the path. If an older copy of a file exists elsewhere in the Project, name it and say it is stale.
5. Name the next step: `/retro-analysis` if it has not run, or another audience version.

## Done when

`readout-<audience>.md` is written, passes the sentence check in step 5, and the user has it.

## Do not

- Do not strengthen a claim to make the story cleaner.
- Do not drop a caveat to save words. Shorten it.
- Do not add a number, a reason or a recommendation that the readout does not hold.
- Do not round a number so that it changes the message (14.6% may become "about 15%", not "nearly 20%").
- Do not create a new readout from an unfinished analysis. Suggest `/run-analysis` or `/review-analysis`.
