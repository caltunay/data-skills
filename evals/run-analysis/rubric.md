# Rubric: /run-analysis

| Check | Pass means |
|---|---|
| Reads first | Uses the spec and success checks from `analysis.md`. Resumes from the Progress line |
| Goal | States the goal up front ("done when the success checks pass and a draft readout is written") and keeps going. Stops only for a paste or an answer |
| Method card | Loads the card for the chosen method and logs each "Checks that must pass" item |
| Readout | Standard and deep: writes a draft `readout.md` in the 6-part layout, marked draft. Quick: short answer in chat |
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
| Chat-app handoff | With no project folder, offers `analysis.md` (and `readout.md` when it exists) as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Data-check floor | Runs the floor at every depth, quick in compact form: table audit, one real entity across tables, one day, daily series, join checks, category totals, assumption checks, reconcile. Each check states its expected result first (v0.3 item 1) |
| Independent rungs | Rungs 2 to 4 compare against raw rows or a separate query, never the frame the table was built from |
| Run first | With a code tool and attached data files, loads them and runs the checks itself (DuckDB, SQLite or pandas). Hands over only with no code tool, says so in one line, and batches checks into numbered groups (v0.3 item 3) |
| Key numbers | The draft readout has at most 5 key numbers, strict for an exec audience. The rest go to the Appendix. The Method line claims only what ran (v0.3 item 13) |
| Fresh review offered | At standard and deep depth, the go-ahead recommends `/review-analysis` in a new chat, with the Project files wording. Quick depth may review in the same chat (v0.3 item 28) |
| Review pack | `analysis.md` has an "Appendix: Review pack" with the exact code and data source for each headline number (v0.3 item 29) |
| Readout visuals | At most 3 charts for exec, each title a takeaway, one annotation on the key moment, image files in `outputs/` linked with alt text. A chart replaces number rows that say the same thing. Hand-over mode gives the chart spec plus ready-to-run code (v0.3 item 30) |
| Portable callouts | Callouts are blockquotes with a bold label (`> **Answer:**`, `> **Caveat:**`, `> **Ask:**`), at most 3. Status is `**Status: DRAFT**`. Bold only for one takeaway per section. No app-specific macros (v0.3 item 31) |
