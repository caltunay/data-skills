# Rubric: /improve-code

| Check | Pass means |
|---|---|
| Intent first | States what the code is meant to produce. Asks if unclear, and does not fix toward a guess |
| Order | Correctness before style, style before performance |
| Correctness | Grain, join fan-out, filters, nulls, time zones and dedup are checked. Every planted bug is found, with its effect on the result |
| Surgical | Only needed lines change. No rewrite, rename or restyle beyond the listed changes unless asked |
| Diff | A diff is shown, with one tagged line per change saying why |
| Conventions | Team Conventions from the data map win over the defaults |
| Performance | Dialect-aware. Partition filters, needed columns only, no repeated scans. No promised speed-up without a measurement |
| Equivalence | Style and performance changes come with before and after row counts and totals as check queries. Not called "equivalent" before they pass |
| Bug fixes | A behaviour change is stated as such, with the expected difference |
| Precision | The clean case gets "No changes needed" and at most 2 optional suggestions |
| Start check | Says in one line whether a `DATA-MAP.md` was found |
| No early tool call | No connector or data tool call before the user names the source |
| Chat-app hand-back | With no project folder, gives the code as one block and offers a download |
| No invented names | Uses no company, product, table or source name the user did not say |
| No move requests (v0.6 item 4) | Never asks the user to move a file or add it to a Project folder. When it cannot write a file it says "Download `<file>`" and, if it matters, where a later step expects it |
| Verify by running (v0.6 item 24) | With a code tool and the data attached or named, runs the old and the new version itself and shows the same result. Does not stop to ask first. Hands the checks over only when it cannot run them |
| Problems stay visible (v0.6 item 25) | Prefers a check that shows a mismatch (for example coverage per side of a join) over a filter that hides it |
| Reusable stays reusable (v0.6 item 26) | Pins no fixed date, window or one-off value into a shared query. Suggests a parameter |
| Uses what is known (v0.6 item 27) | Facts already in the map or the analysis (nulls, ties, grain) are used, not reported as "not checked" |
| Closes the loop and offers candidates (v0.6 items 28 and 30) | Offers to record a changed status of shared code (untested, tested on a translation, failed) where the team keeps it. Offers analysis scripts as candidates for Key queries, not only queries the map lists |
| Stays in scope (v0.6 item 29) | Reports on the code only. No findings, and no claim above the ceiling (for example "rose each month" where the analysis says no trend can be claimed) |
