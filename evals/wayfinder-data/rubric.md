# Rubric: /wayfinder-data

| Check | Pass means |
|---|---|
| Start check | Says in one line whether `DATA-MAP.md` and a wayfinder file were found. With no map, offers setup (A) or continue (B). Resumes from the Progress line |
| Items | 5 to 12 decision items, each with options, a recommended default, status, dependencies and who decides |
| Confirm the map | Shows the list and asks what is missing before resolving |
| One at a time | Resolves one item per round, in dependency order, and waits |
| Never silent | No item is `decided` without the user's choice, or an explicit "you choose" that is reported back |
| Other people | An item the user cannot decide stays `open`, with who to ask and the question |
| File | `data-work/wayfinder/<slug>.md` in the stated layout, Progress line updated after each item |
| Output | Analyses to run, each as a ready `/grill-the-ask` prompt that carries the decisions |
| No work started | No analysis, no query |
| Precision | A single clear ask is sent to `/grill-the-ask`. No map is built |
| No early tool call | No connector or data tool call before the user names the source |
| Chat-app hand-back | With no project folder, hands back the wayfinder file at `data-work/wayfinder/<slug>.md`, in one of the three save forms (v0.5 item 2) |
| No invented names | No company, product, table, source, person or team name the user did not say |
| Fast path | When the whole ask is one design item, skips the decision map and the project file and goes to the spec (v0.4 item 12) |
| Experiment spec | `experiment-spec.md` has hypothesis, unit of randomisation, feature gate or assignment, primary metric, guardrails, MDE, power, runtime, seasonality, SRM check plan and decision rule. No invented number (v0.4 item 12) |
| Metric spec | `metric-spec.md` has definition, formula, grain, population, data source or what must be collected, proxies with how to check them, benchmark or target with its source, and owner (v0.4 item 12) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>`" (never a request to move it into a Project folder), or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Flags missing data (v0.5 item 15) | An option that needs data the map says is missing or unknown says so in the option text, and is not recommended without that flag |
| Go-ahead question (v0.5 item 18) | Ends with "Go ahead? A) the next step (recommended) B) Change something (say what) C) Add an item, a check or a question", with A naming the real next step |
| Spec in its own folder (v0.5 item 19) | The spec is saved at `data-work/analyses/<YYYY-MM-DD>-<slug>/experiment-spec.md` or `metric-spec.md`, never as a bare file name |
| No move requests (v0.6 item 4) | Never asks the user to move a file or add it to a Project folder. When it cannot write a file it says "Download `<file>`" and, if it matters, where a later step expects it |
| Business limits first (v0.6 item 31) | Before any sizing, asks how long the test can run, what the change is expected to gain, what it costs to be wrong and whether it is easy to reverse. Invents no constraint |
| Shows what the limits buy (v0.6 items 32 and 35) | Sizes for the user's limits and says plainly what that can and cannot detect. Derives the margin or minimum effect from the expected gain against the loss that would cancel it, not from the timeline. States the sizing assumptions and flags when the data breaks them |
| Other designs offered (v0.6 item 33) | When an A/B test is too weak, offers other designs in the first round of options (before and after, time series, difference-in-differences, synthetic control, matched cohorts, a reversible switch with an alert, no test), each with pros, cons, data needed, the check that would break it and its claim ceiling. The spec becomes an evaluation spec when the chosen design is not an experiment |
| Options checked against the map (v0.6 item 36) | Unit counts, missing fields and known breaks in a comparison series are said in the option, or the option is dropped with the evidence |
| Decision hygiene (v0.6 items 34 and 37 to 42) | Never invents a constraint. Raises a goal conflict when the choice is made. Records choices a tool or another owner makes as "to confirm with <owner>". Writes the one sound option as a requirement. Explains overlapping tests. Names likely owners. Next step after a spec is sign-off and open items |
