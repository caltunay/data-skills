# Rubric: /grill-the-ask

| Check | Pass means |
|---|---|
| Round size | At most 3 questions per round, each with 2 to 4 options and a recommended default |
| Wait | Stops and waits for answers |
| Coverage | Goal, decision, question type, metric, population, time window, constraints, deadline, as needed |
| Ceiling | Question type named with its claim ceiling. For a "why" ask, descriptive or exploratory both pass if the ceiling is stated and "why" is not treated as causal |
| Depth | Depth proposed with a one-line reason |
| No repeats | No question asked twice in the session, even reworded |
| Audience | Asks who reads the result, unless already known |
| Assumptions | Written down. Standard and deep show all 7 columns. Alternatives for high-impact rows |
| No work started | No query or analysis |
| Precision | The clean case gets no invented questions |
| Files | None at quick. `analysis.md` at standard, with Audience and a Progress line in Meta. Full folder at deep |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether `DATA-MAP.md` and `analysis.md` were found. With no map, offers setup (A) or continue (B) |
| Chat-app hand-back | With no project folder, offers `analysis.md` (and `readout.md` when it exists) at its full `data-work/` path at the end, in one of the three save forms (v0.5 item 2) |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, writes each file to the Project files at its full path if it can, otherwise creates it and offers a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3, v0.5 item 2) |
| Real defaults | Every question, the deadline included, has one real recommended default with a reason. No hedges such as "C if unknown" (v0.3 item 7) |
| Does not analyse | With files attached, notes only what they contain (columns, possible duplicates, date range). No early finding in an option, the clarified question or the claim line (v0.4 item 2) |
| Decisions log | Every question and answer is in the Decisions section word for word, and each round's answers are echoed back exactly before moving on (v0.4 item 3) |
| One at a time when stuck | An answer that conflicts with an earlier one, the data map, or itself is named plainly, and the skill switches to one question at a time until clear, then returns to rounds (v0.4 item 7) |
| Setup choice | The A or B choice is recorded in Meta. Setup is never offered again once set (v0.4 item 4) |
| Routing | A design ask or a project-sized ask goes to `/wayfinder-data` with one line why (v0.4 item 12 and 13) |
| Stable names and versions | In a chat app, files use the `data-work/` layout at full paths (`data-work/DATA-MAP.md`, `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`), start with `format:` and `updated:`, and are handed back whole. If two copies exist, uses the newest `updated:` and says so (v0.5 item 1) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Continue or new (v0.5 item 5) | When an analysis of the same ask already exists, asks "Continue `<folder>`, or start a new analysis?" and never resumes silently. Matches the analysis to the ask by folder or slug |
| Refreshes stale lines (v0.5 item 6) | When resuming, lines that are now out of date (for example "no DATA-MAP.md, so inline" after a map exists) are refreshed and shown as "was" and "now" pairs |
| Earlier work, no map (v0.5 item 7) | When the Project holds earlier analyses but no `DATA-MAP.md`, the first option is "Yes, attach it", not "No", and it says: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Flags missing data (v0.5 item 15) | An option that needs data the map says is missing or unknown says so in the option text, and is not recommended without that flag |
| Ways of working (v0.5 item 10) | Records in the map how the user works (chat Projects or a repo layout) and the file hand-back choice (downloads, Project files, or a named document tool). Asks about hand-back once per Project, not at every grill |
