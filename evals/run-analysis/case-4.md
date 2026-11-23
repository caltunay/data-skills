# Case 4: chat app with a code tool and attached CSVs (planted trap)

Type: planted trap. Data is invented.

## Setup

Run in a chat app (claude.ai or ChatGPT) with its code tool turned on, in an incognito chat. No Project files. The user attaches three files: `analysis.md` (standard depth, plan and spec done), `signups.csv` (about 3,500 rows, January to March) and `dashboard_monthly.csv` (the trusted monthly totals).

## Input

User runs `/run-analysis`: "Plan is in the attached analysis.md. Data is attached too."

## Simulated answers

Round 1 (only if the agent asks for a choice after a failed rung): "Keep the latest row per signup_id."
Round 2 (go-ahead): "A."

## Pass

- Says in one line what it found: `analysis.md` attached, no `DATA-MAP.md`. Offers setup or continue.
- States the goal up front.
- Loads the attached CSVs with its code tool and runs every floor check and rung itself (DuckDB, SQLite or pandas). Shows each expected result before the check and the actual after it.
- Does not hand any check over to the user, and never says "I can't run code".
- Creates `analysis.md` and `readout.md` as files and offers them as downloads. Does not print them as blocks unless creating a file failed.
- Ends with the go-ahead question. At standard depth, A recommends `/review-analysis` in a new chat, with the Project files wording.

## Fail

- Says it cannot run code, or hands numbered queries to the user to paste back.
- Says it cannot save files, or prints the files as blocks while a download was possible.
- Skips the data-check floor.
