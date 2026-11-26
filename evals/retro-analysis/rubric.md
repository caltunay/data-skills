# Rubric: /retro-analysis

| Check | Pass means |
|---|---|
| Reads first | Uses `analysis.md` and `DATA-MAP.md` |
| Proposals | Specific, dated, with source `analyses/<slug>` |
| Diff | Old and new text shown for each change |
| Approval | Each change approved before it is applied |
| Staleness | Contradicted or old entries flagged and asked about |
| Not a dump | No row-level data, personal remarks or one-off detail |
| Chat apps | Full updated map handed back for the Project file |
| Precision | Zero changes is a valid result and is stated plainly |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether `DATA-MAP.md` and `analysis.md` were found. With no map, offers setup (A) or continue (B) |
| Chat-app hand-back | With no project folder, offers `analysis.md` (and `readout.md` when it exists) at its full `data-work/` path at the end, in one of the three save forms (v0.5 item 2) |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, writes each file to the Project files at its full path if it can, otherwise creates it and offers a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3, v0.5 item 2) |
| Right section | Conventions hold style only (SQL, Python, naming). Analysis rules go in Rules or Gotchas. No entry in two sections |
| True reasons | Every reason quotes a line in `analysis.md` that shows it. No "this cost a rung" unless the ladder log shows it |
| Never offers setup | With no map, asks for a map from another project, then builds the map itself. Never offers `/setup-data-work` (v0.4 item 4) |
| Map layout | One entry per source. Grain and key facts under Tables. The template's table layout, no loose bullets (v0.4 item 5) |
| Funnels and key queries | Proposes additions to Funnels and Key queries when the analysis earned them (v0.4 item 9) |
| Stable names and versions | In a chat app, files use the `data-work/` layout at full paths (`data-work/DATA-MAP.md`, `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`), start with `format:` and `updated:`, and are handed back whole. If two copies exist, uses the newest `updated:` and says so (v0.5 item 1) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Refreshes stale lines (v0.5 item 6) | When resuming, lines that are now out of date (for example "no DATA-MAP.md, so inline" after a map exists) are refreshed and shown as "was" and "now" pairs |
| Key queries as SQL (v0.5 item 8) | Each key query is saved as SQL text in the team's conventions, with what it returns and when to use it, and its columns are checked against the Tables section. A description alone fails |
| Tidy the map (v0.5 item 9) | When extending a messy map, normalises it to the template as one approved change with a diff: one entry per source, grain and keys under Tables, table layout instead of bullets |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
