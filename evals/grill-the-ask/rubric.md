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
| Chat-app handoff | With no project folder, offers `analysis.md` (and `readout.md` when it exists) as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Real defaults | Every question, the deadline included, has one real recommended default with a reason. No hedges such as "C if unknown" (v0.3 item 7) |
