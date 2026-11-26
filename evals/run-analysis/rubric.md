# Rubric: /run-analysis

| Check | Pass means |
|---|---|
| Reads first | Uses the spec and success checks from `analysis.md`. Resumes from the Progress line |
| Goal | States the goal up front ("done when the success checks pass and a draft readout is written") and keeps going. Stops only for a paste or an answer |
| Method card | Loads the card for the chosen method and logs each "Checks that must pass" item |
| Readout | Standard and deep: writes a draft `readout.md` as a story (TL;DR, takeaway-sentence headers, caveats, method, appendix), marked draft. Quick: short answer in chat |
| Status | Sets `running`. Does not set `reviewed` |
| Expected first | States the expected result before each rung |
| Ladder honest | A failed rung stops the climb until the cause is found |
| Depth | Quick: the compact data-check floor, never skipped. Standard: full floor and full ladder. Deep: both plus alternative specification |
| Reconcile | Gap computed against the stated tolerance, explained if above |
| Fan-out | Row counts before and after joins |
| Claims | At or below the ceiling. Direction, magnitude, uncertainty |
| Ask not assume | Unclear items are asked or logged as assumptions |
| Data safety | Aggregates by default, asks before saving row-level data |
| Precision | The clean case reports without invented issues |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether `DATA-MAP.md` and `analysis.md` were found. With no map, offers setup (A) or continue (B) |
| Chat-app hand-back | With no project folder, offers `analysis.md` (and `readout.md` when it exists) at its full `data-work/` path at the end, in one of the three save forms (v0.5 item 2) |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, writes each file to the Project files at its full path if it can, otherwise creates it and offers a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3, v0.5 item 2) |
| Data-check floor | Runs the floor at every depth, quick in compact form: table audit, one real entity across tables, one day, daily series, join checks, category totals, assumption checks, reconcile. Each check states its expected result first (v0.3 item 1) |
| Independent rungs | Rungs 2 to 4 compare against raw rows or a separate query, never the frame the table was built from |
| Run first | With a code tool and attached data files, loads them and runs the checks itself (DuckDB, SQLite or pandas). Hands over only with no code tool, says so in one line, and batches checks into numbered groups (v0.3 item 3) |
| Key numbers | The draft readout has at most 5 key numbers, strict for an exec audience. The rest go to the Appendix. The Method line claims only what ran (v0.3 item 13) |
| Fresh review offered | At standard and deep depth, the go-ahead recommends `/review-analysis` in a new chat, with the Project files wording. Quick depth may review in the same chat (v0.3 item 28) |
| Review pack | `analysis.md` has an "Appendix: Review pack" listing each script in `scripts/` with what it produces, how to run it and its data source (v0.6 item 1) |
| Readout visuals | At most 3 charts for exec, each title a takeaway, one annotation on the key moment, image files in `outputs/` linked with alt text. A chart replaces number rows that say the same thing. Hand-over mode gives the chart spec plus ready-to-run code (v0.3 item 30) |
| Portable callouts | Callouts are blockquotes with a bold label (`> **Ask:**`, `> **Caveat:**`, `> **Decision:**`), only where a decision or attention is needed, at most 3. Status is `**Status: DRAFT**`. Bold only for one takeaway per section. No app-specific macros (v0.3 item 31) |
| Hypothesis statuses | Updates each touched node to supported, refuted, open or parked, naming the result that shows it. Never `supported` without a result (v0.4 item 6) |
| Skeleton replaced | A `SKELETON` readout is replaced by the draft. No XX or [segment] is left (v0.4 item 10) |
| Readout .docx | Produces `readout.docx` from the same text as `readout.md` with the charts embedded, using the sandbox's document library. With no code tool: `readout.md` plus chart code only (v0.4 item 1) |
| Stable names and versions | In a chat app, files use the `data-work/` layout at full paths (`data-work/DATA-MAP.md`, `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`), start with `format:` and `updated:`, and are handed back whole. If two copies exist, uses the newest `updated:` and says so (v0.5 item 1) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>`" (never a request to move it into a Project folder), or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Refreshes stale lines (v0.5 item 6) | When resuming, lines that are now out of date (for example "no DATA-MAP.md, so inline" after a map exists) are refreshed and shown as "was" and "now" pairs |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Hypothesis status logic (v0.5 item 16) | Each node is judged against its own support and refute conditions, not the parent's direction. A robustness child whose result held is `supported`, whatever the result was. Child nodes are worded without the parent's direction |
| No move requests (v0.6 item 4) | Never asks the user to move a file or add it to a Project folder. When it cannot write a file it says "Download `<file>`" and, if it matters, where a later step expects it |
| Scripts are files (v0.6 item 1) | Every script behind a headline number, a check or a chart is its own file in `scripts/` in the analysis folder. Each takes the data folder as an argument and writes its outputs into the analysis folder, never a temp path. `analysis.md` lists each script with one line on what it produces and how to run it, and does not hold the code |
| Where it stands (v0.6 item 2) | `analysis.md` opens with a "Where it stands" block of about 5 lines (status, answer so far, open risks, next step, how to resume) and updates it at the end of the step |
| Charts as SVG (v0.6 item 3) | In a chat app that can write text files but not binary files, each chart is saved as SVG in the analysis folder and linked from `readout.md`. PNG appears only inside binary outputs (`.docx`, `.pptx`) |
| Readout is a story (v0.6 item 8) | The readout opens with a TL;DR of 2 to 3 lines. Section headers are takeaway sentences, and read in order they tell the story. No label-only headers ("Answer", "Key numbers"). Callouts only where a decision or attention is needed. Then caveats, a short method, an appendix. Caps hold: 5 numbers, 3 charts, 3 callouts. Analyst-only figures are in the appendix or `analysis.md` |
| Lead with the decision insight (v0.6 item 9) | A number that tells the reader what it would take to change the answer (the gap to a target, the size of change needed) is in the story, not the appendix |
| Chart per claim and plain words (v0.6 items 10 and 11) | Each chart fits the message it proves (target: bars plus a target line, time: line, mix: stacked bars, spread: histogram or box), one message per chart. Numbers are rounded for an exec audience and phrased plainly ("almost double the target", "we are 95% sure it fell") |
| Storytell applied (v0.6 item 12) | The readout is drafted with the `storytell` discipline: no claim is raised to make the story cleaner |
| Stale list (v0.6 items 5 to 7) | Stale copies are listed by full path with one rule each time, a step does not leave its own stale copy, and "files changed" is said only after a step that could change files |
