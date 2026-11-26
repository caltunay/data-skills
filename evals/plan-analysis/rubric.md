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
| Chat-app hand-back | With no project folder, offers `analysis.md` (and `readout.md` when it exists) at its full `data-work/` path at the end, in one of the three save forms (v0.5 item 2) |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, writes each file to the Project files at its full path if it can, otherwise creates it and offers a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3, v0.5 item 2) |
| Real defaults | Every option list has one real recommended choice with a reason (v0.3 item 7) |
| Card checks copied | The method card's "Checks that must pass" are copied into the success checks at plan time, from the type file or the compact cards. Never deferred to the run |
| Hypothesis tree | At standard and deep depth, a tree before the method options: H1, H1.1 and so on, at most 3 levels and about 12 nodes. Each node has a support condition, a refute condition and the child it leads to. The user picks the paths. Quick depth: a flat list of up to 3 (v0.4 item 6) |
| Hypotheses section | `analysis.md` has a Hypotheses section with a status per node (open, supported, refuted, parked) (v0.4 item 6) |
| Readout skeleton | Offered as optional at standard and deep depth. Placeholders only (XX%, [segment]), never an invented number, `**Status: SKELETON**` (v0.4 item 10) |
| Decisions log | Questions and the user's answers word for word, echoed back after each round (v0.4 item 3) |
| Stable names and versions | In a chat app, files use the `data-work/` layout at full paths (`data-work/DATA-MAP.md`, `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`), start with `format:` and `updated:`, and are handed back whole. If two copies exist, uses the newest `updated:` and says so (v0.5 item 1) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Refreshes stale lines (v0.5 item 6) | When resuming, lines that are now out of date (for example "no DATA-MAP.md, so inline" after a map exists) are refreshed and shown as "was" and "now" pairs |
| Earlier work, no map (v0.5 item 7) | When the Project holds earlier analyses but no `DATA-MAP.md`, the first option is "Yes, attach it", not "No", and it says: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Flags missing data (v0.5 item 15) | An option that needs data the map says is missing or unknown says so in the option text, and is not recommended without that flag |
| Hypothesis status logic (v0.5 item 16) | Each node is judged against its own support and refute conditions, not the parent's direction. A robustness child whose result held is `supported`, whatever the result was. Child nodes are worded without the parent's direction |
