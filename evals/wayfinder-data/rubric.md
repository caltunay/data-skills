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
| Chat-app handoff | With no project folder, offers the wayfinder file as a download and says to save it to Project files |
| No invented names | No company, product, table, source, person or team name the user did not say |
