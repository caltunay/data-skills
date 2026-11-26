# Case 6: standard run in a chat app, scripts as files and a story readout (v0.6)

Type: standard. Data is invented.

## Input

User, in a normal chat inside a Project, runs `/run-analysis`. The Project files hold `data-work/DATA-MAP.md` and `data-work/analyses/2026-03-09-march-signups/analysis.md` (standard depth, descriptive, plan and spec written). The user attached `signups.csv` (one row per account, 36,900 rows in February and 31,200 in March, columns `account_id`, `signup_date`, `channel`, `is_test`). The chat has a code tool. It can write text files to the Project files but not binary files.

## Simulated answers

Round 1 (the agent asks whether to save row-level data): "No, aggregates only."
Round 2 (go-ahead): "A."

## Pass

- Saves every script behind a number, a check or a chart as its own file in `data-work/analyses/2026-03-09-march-signups/scripts/`, takes the data folder as an argument, and writes outputs into the analysis folder, never a temp path. Runs each from the data folder before citing its number.
- `analysis.md` lists each script with one line on what it produces and how to run it, and does not paste the code. It opens with a "Where it stands" block.
- Saves the chart as SVG in the analysis folder (text files can be written, binary files cannot) and links it from `readout.md` by its real path. PNG appears only inside `readout.docx`.
- `readout.md` opens with a TL;DR of 2 to 3 lines. Section headers are takeaway sentences ("Sign-ups fell about 15% in March, almost all of it in one channel"). No label-only headers. At most 5 numbers, 3 charts, 3 callouts. The chart fits its message (change over time: a line).
- Numbers are rounded and phrased in plain words for the exec audience. Raw-count checks sit in the appendix or `analysis.md`.
- Says "Download `<file>`" for anything it cannot write, and never asks the user to move a file into a Project folder.
- Says which files changed only at the end of the step.

## Fail

- Pastes the queries into `analysis.md` or leaves a script that reads or writes a temp path.
- Saves the chart as PNG in the Project files, or asks the user to move a file into a Project folder.
- Writes a readout with the headers "Answer", "Key numbers", "Charts", "What it means".
