# Rubric: /plan-analysis

| Check | Pass means |
|---|---|
| Reads first | Uses `analysis.md` and the data map, asks nothing already answered |
| Ceiling | States the claim ceiling and says if the plan cannot reach the decision |
| Options | Quick: one line. Standard: 2 to 4 options and a chosen plan. Deep: plus power or MDE where relevant |
| Spec | Analysis table spec has grain, keys, measures, dimensions, time, filters, tidy or wide, context columns, expected rows |
| Success checks | Set up front, with a trusted number and a tolerance |
| Easy first | Simplest method that answers the question |
| Method card | Names the method card. Its "Checks that must pass" are in the success checks. A short card comes with the specialist-review warning |
| Revisions | A plan that cannot hold gets a dated Plan revisions row |
| No invention | Does not invent decisions the user has not made |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether `DATA-MAP.md` and `analysis.md` were found. With no map, offers setup (A) or continue (B) |
| Chat-app handoff | With no project folder, offers `analysis.md` (and `readout.md` when it exists) as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Real defaults | Every option list has one real recommended choice with a reason (v0.3 item 7) |
| Card checks copied | The method card's "Checks that must pass" are copied into the success checks at plan time, from the type file or the compact cards. Never deferred to the run |
| Hypothesis tree | At standard and deep depth, a tree before the method options: H1, H1.1 and so on, at most 3 levels and about 12 nodes. Each node has a support condition, a refute condition and the child it leads to. The user picks the paths. Quick depth: a flat list of up to 3 (v0.4 item 6) |
| Hypotheses section | `analysis.md` has a Hypotheses section with a status per node (open, supported, refuted, parked) (v0.4 item 6) |
| Readout skeleton | Offered as optional at standard and deep depth. Placeholders only (XX%, [segment]), never an invented number, `**Status: SKELETON**` (v0.4 item 10) |
| Decisions log | Questions and the user's answers word for word, echoed back after each round (v0.4 item 3) |
| Stable names and versions | In a chat app, files are named `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md`, start with `format:` and `updated:`, are handed back whole, and the step says "Replace the old one in your Project files." If two copies exist, uses the newest `updated:` and says so (v0.4 item 15) |
