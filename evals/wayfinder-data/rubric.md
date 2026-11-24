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
| Chat-app handoff | With no project folder, hands back the wayfinder file at `data-work/wayfinder/<slug>.md`, in one of the three save forms (v0.5 item 2) |
| No invented names | No company, product, table, source, person or team name the user did not say |
| Fast path | When the whole ask is one design item, skips the decision map and the project file and goes to the spec (v0.4 item 12) |
| Experiment spec | `experiment-spec.md` has hypothesis, unit of randomisation, feature gate or assignment, primary metric, guardrails, MDE, power, runtime, seasonality, SRM check plan and decision rule. No invented number (v0.4 item 12) |
| Metric spec | `metric-spec.md` has definition, formula, grain, population, data source or what must be collected, proxies with how to check them, benchmark or target with its source, and owner (v0.4 item 12) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Flags missing data (v0.5 item 15) | An option that needs data the map says is missing or unknown says so in the option text, and is not recommended without that flag |
| Go-ahead question (v0.5 item 18) | Ends with "Go ahead? A) the next step (recommended) B) Change something (say what) C) Add an item, a check or a question", with A naming the real next step |
| Spec in its own folder (v0.5 item 19) | The spec is saved at `data-work/analyses/<YYYY-MM-DD>-<slug>/experiment-spec.md` or `metric-spec.md`, never as a bare file name |
