# Rubric: /review-analysis

| Check | Pass means |
|---|---|
| Claim and ceiling | One-line claim, question type and ceiling named |
| Verdict | `ready`, `ready with caveats` or `needs rework`, with reasons |
| Planted flaws | Every planted flaw is found, and each has an exact check |
| Wording | Every claim above the ceiling is quoted with the allowed wording |
| Method card | The analysis is checked against the "Checks that must pass" of the card for the method used |
| Readout | A draft `readout.md` is checked sentence by sentence. Each fix is shown as "was" and "now". Marked final only if the verdict is `ready` or `ready with caveats` |
| Assumptions | High-impact `open` rows flagged |
| Business | Decision, size, baseline, segments, scope and ask match covered where relevant |
| Leadership questions | 3 to 5, with answers, or "not supported yet" |
| Precision | The clean case gets "No material issues" and at most 3 optional checks |
| False alarms | No flaws raised that the analysis does not show |
| Tone | No praise, no personal criticism |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether `DATA-MAP.md` and `analysis.md` were found. With no map, offers setup (A) or continue (B) |
| Chat-app handoff | With no project folder, offers `analysis.md` (and `readout.md` when it exists) as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
