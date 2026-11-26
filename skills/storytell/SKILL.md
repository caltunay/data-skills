---
name: storytell
description: The storytelling discipline of the readout. Applied inside /run-analysis and /review-analysis: the first drafts the readout as a story, the second checks the story and fixes it before the readout is marked final. Run directly it rewrites a final readout for one audience (exec, product, data or mixed) and one format (doc, chat message, email, slide pack). Use only when the user runs /storytell or explicitly asks to turn a finished readout into an audience version.
---

# /storytell

Same facts, new shape. The audience changes the words, never the claim.

Experimental (v0.2).

## Two uses

1. **Applied inside the flow.** `/run-analysis` uses it to draft `readout.md` as a story. `/review-analysis` uses it to check the story and fix it before marking the readout final. No command is typed and no question is asked.
2. **Run directly.** The user runs `/storytell`, or asks for an audience version (exec email, chat message, slide pack). The steps below apply. Audience versions are offered at the end of `/review-analysis`, not required.

## The story discipline

A readout is a story, not a form. It is the decision layer. `analysis.md` is the evidence layer.

- **TL;DR first:** 2 to 3 lines covering the answer, what it means and the ask.
- **Story sections,** top down, then drilling in. Each section header is a takeaway sentence. The chart or number under it proves the header. One message per section. Read in order, the headers alone tell the story. Never a label-only header ("Answer", "Key numbers", "Charts", "What it means").
- **Lead with the insight a decision needs.** If a number tells the reader what it would take to change the answer (the gap to a target, the size of change needed), it goes in the story, not the appendix.
- **Callouts only where a decision or attention is needed.** At most 3.
- **Then caveats, a short method, and the appendix.** Analyst-only figures (raw-count checks, intervals of robustness cuts, recompute detail) go to the appendix or `analysis.md`.
- **Caps:** at most 5 headline numbers, 3 charts, 3 callouts. Pick each chart from the message it must prove (`viz`).
- **Plain words.** Round numbers for exec audiences. Plain phrases over jargon: "almost double the target", not "85% above"; "we are 95% sure it fell", not "interval below zero". This applies to readouts, decks and question cards.
- **Never raise a claim to make the story cleaner.** Every number keeps its uncertainty, in plain words, and no sentence goes above the claim ceiling.

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
- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default with its reason. A hedge is not a default: never "recommended if you have one", "TBC" or "C if unknown". Pick a real option and say why. Show any tree, table or draft a question refers to before you ask it (never ask "which hypothesis paths?" before the tree is on screen). Each option says what it means in a few words (for example "H1.1: holds in each month"). An option that needs data the map says is missing says so in the option text (for example "needs the visit marker; the map says it is unknown"). Use the environment's multiple-choice question tool for every round if it has one (one card per question, recommended option first, room for the user's own answer); otherwise list the options as text. Card counters show the position out of the full total across rounds (for example "2 of 5"), never a count that restarts each round. Wait for answers. Never assume silently. When an answer conflicts with an earlier one or the data map, or does not make sense, say so plainly and ask one question at a time until it is clear. Never ask the same question twice.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, save each file at its full `data-work/` path in the Project files if you can, otherwise create it and offer a download, and say which; print it only if that fails. Never ask the user to edit a saved file by hand.

## Steps

1. **Ask audience and format**, in one round. Skip a question the user already answered. The audience in `analysis.md` Meta is the recommended default.
   - Audience: A) exec, B) product, C) data, D) mixed.
   - Format: A) doc, B) chat message, C) email, D) slide pack (`readout.pptx`, or a markdown outline when no library can build it).
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
| Exec | No jargon. No method names, no "p-value", no "confidence interval": say "likely between X and Y" or "we are 95% sure". Round numbers. Under 150 words before the appendix | The answer, 1 to 3 numbers with their range, the recommendation, the main caveat | Method, ladder, segment detail |
| Product | Plain words, product terms the user already uses | The answer, numbers with ranges, what it means for the product, what to test next | Statistical detail |
| Data | Precise terms are welcome | Method, checks passed, intervals, assumptions with ids, the ceiling by name | Nothing. Keep it tight anyway |
| Mixed | Exec version first, then a "Detail" section for product and data readers | Both | Nothing |

Uncertainty in plain words: an interval becomes "likely between X and Y". An exact count stays "exact for the period". A caveat about the ceiling becomes "this shows what happened, not why" (descriptive), "this is a pattern to test, not a finding" (exploratory), or "this holds for the customers and period tested" (experiment).

## Layout by format

- **Doc:** the story layout above: TL;DR, takeaway-header sections, callouts only where needed, caveats, method (3 lines), appendix if needed, link to `analysis.md`.
- **Chat message:** 3 to 6 lines. Line 1 is the answer. Then the key number with its range, the recommendation, the main caveat, and where the full readout is.
- **Email:** a subject line that states the answer. Then the chat-message content in short paragraphs, and a closing line with the ask or the decision needed.
- **Slide pack:** see "Slide pack" below.

The exec limit applies to every format: under 150 words before the appendix. For a slide pack, count titles and body text.

## Slide pack

Offered at the end of `/review-analysis` as one card: "Also make a slide pack?" The answer is saved under Ways of working in the map, so later analyses do not ask again unless the user changes it. When yes:

- Build `readout.pptx` from the final `readout.md`. No new claims. Nobody edits the deck on its own: `readout.md` stays the source.
- Titles are takeaways. Read in order, the titles alone tell the story. Each slide proves its title.
- One message and at most one chart per slide, about 20 words of body text at most. Evidence goes on appendix slides.
- The same claim ceiling as the readout. No slide repeats another.
- Charts embedded in the deck may be PNG (a binary output). The same charts stay SVG in the Project files.
- In a chat app it is a download, like `readout.docx`. If no library can build `.pptx`, fall back to a slide outline in markdown (title, one line, chart suggestion per slide) and say so.
- Check the deck against the readout: every number matches, and no title claims more than the readout does.

## End (every flow step)

1. Update the Progress line and the "Where it stands" block in `analysis.md`, for example `Progress: storytell done, readout-exec.md written`.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name: `data-work/analyses/<YYYY-MM-DD>-<slug>/readout-<audience>.md` (and its `.docx` or `.pptx` when made) and the updated `analysis.md` in the same folder. Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>`" (you could not write to Project files; never ask the user to move a file into a Project folder, chat apps do not allow it), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Hand back whole files, never patches. Never ask the user to edit a saved file by hand.
4. Stale copies: list each older copy of a file this step handles by its full path, never a bare name beside the live full path. One rule every time: a copy is stale when it has the same file name at another path, or an older `updated:` line. If this step replaced a file it created, remove or overwrite the old one where you can, and list only the files you cannot remove. Coding agent: the file is saved next to `readout.md`. Name the path.
5. Say which files changed only if this step changed files. Name the next step: `/retro-analysis` if it has not run, or another audience version.

## Done when

`readout-<audience>.md` is written, passes the sentence check in step 5, and the user has it.

## Do not

- Do not strengthen a claim to make the story cleaner.
- Do not drop a caveat to save words. Shorten it.
- Do not add a number, a reason or a recommendation that the readout does not hold.
- Do not round a number so that it changes the message (14.6% may become "about 15%", not "nearly 20%").
- Do not create a new readout from an unfinished analysis. Suggest `/run-analysis` or `/review-analysis`.
