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
| Chat-app handoff | With no project folder, offers `analysis.md` (and `readout.md` when it exists) as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Right section | Conventions hold style only (SQL, Python, naming). Analysis rules go in Rules or Gotchas. No entry in two sections |
| True reasons | Every reason quotes a line in `analysis.md` that shows it. No "this cost a rung" unless the ladder log shows it |
| Never offers setup | With no map, asks for a map from another project, then builds the map itself. Never offers `/setup-data-work` (v0.4 item 4) |
| Map layout | One entry per source. Grain and key facts under Tables. The template's table layout, no loose bullets (v0.4 item 5) |
| Funnels and key queries | Proposes additions to Funnels and Key queries when the analysis earned them (v0.4 item 9) |
| Stable names and versions | In a chat app, files are named `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md`, start with `format:` and `updated:`, are handed back whole, and the step says "Replace the old one in your Project files." If two copies exist, uses the newest `updated:` and says so (v0.4 item 15) |
