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
| Chat-app handoff | With no project folder, gives the code as one block and offers a download |
| No invented names | Uses no company, product, table or source name the user did not say |
