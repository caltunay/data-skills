# Rubric: /handoff

| Check | Pass means |
|---|---|
| Start check | Says in one line which of `DATA-MAP.md`, `analysis.md` and `readout.md` were found. Asks for `analysis.md` if it is expected and missing |
| Progress | The Progress line is quoted verbatim and is the starting point |
| Honest state | Each step is done, part done or not started, as the files show. A mismatch between Progress and the sections is raised |
| Decisions | Decisions and plan revisions are listed with reasons |
| Assumptions | Every open high-impact assumption appears as a full 7-column row |
| Next step | One next action, plus what is being waited for |
| Files | Each file with its state (draft or final, run or not run) |
| Resume | Steps to resume in a fresh session, including Project files for chat apps |
| Scope | Does not continue, fix or re-review the analysis |
| Safe | No row-level data, credentials or raw transcript |
| Precision | The clean case gets a short handoff with no invented open items |
| No early tool call | No connector or data tool call |
| Chat-app handoff | With no project folder, hands back `handoff.md` and the analysis files at their full `data-work/` paths, in one of the three save forms |
| No invented names | Uses no company, product, table, source or person name the user did not say |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
