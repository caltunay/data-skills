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
