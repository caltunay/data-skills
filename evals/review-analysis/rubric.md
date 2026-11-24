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
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Files only | Reviews from `analysis.md`, `readout.md`, `DATA-MAP.md` and the data, not from chat memory. Recomputes the 3 to 5 headline numbers by an independent route and spot-checks 1 or 2 rungs. Does not rebuild the analysis (v0.3 item 28) |
| Run first | With a code tool and the data attached, runs the recompute itself. Hands over only with no code tool (v0.3 item 3) |
| Key numbers | Moves key numbers beyond 5 to the Appendix for an exec readout. Rewrites a Method line that claims more than ran (v0.3 item 13) |
| Review pack | Flags a headline number with no entry in the Review pack (v0.3 item 29) |
| Readout visuals | Checks at most 3 charts for exec, takeaway titles, one annotation, linked images with alt text (v0.3 item 30) |
| Portable callouts | Checks at most 3 bold-labelled blockquote callouts, sets `**Status: FINAL**` only when the verdict allows (v0.3 item 31) |
| Was and now | Every changed readout sentence is shown as a "was" and "now" pair. Every "not supported yet" leadership answer names the cheapest way to answer it |
| Hypotheses check | Every node has a status. Each `supported` or `refuted` node has a result behind it. No `open` or `parked` node is worded as a finding (v0.4 item 6) |
| Decisions check | Compares the Decisions answers with what the analysis used. A mismatch is an issue (v0.4 item 3) |
| Readout .docx | Rebuilds `readout.docx` from the corrected `readout.md`. Never edits the `.docx` by hand (v0.4 item 1) |
| Stable names and versions | In a chat app, files are named `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md`, start with `format:` and `updated:`, are handed back whole, and the step says "Replace the old one in your Project files." If two copies exist, uses the newest `updated:` and says so (v0.4 item 15) |
