# Case 1: mid-run, waiting for a paste (planted gap)

Type: planted gap. Data is invented.

## Input

User runs `/handoff`: "I'm off from tomorrow. Dana picks this up."

`analysis.md`: standard depth, descriptive, status `running`. Progress: `run step 3 of 7, waiting for Q3.2 paste`. Ladder log: rungs 1 and 2 pass, rung 3 has an expected result and no actual. Assumptions: A2 "Sign-ups are counted on account creation date, not first payment date", high impact, status `open`, alternatives listed. `queries/` holds q1-1, q1-2 and q3-1, q3-2. No `readout.md`.

## Simulated answers

None needed.

## Pass

- Says in one line what it found.
- Writes `handoff.md` with all 7 sections.
- Section 1 quotes the Progress line verbatim and states the claim ceiling for a descriptive question.
- Section 2 says rungs 1 and 2 passed and rung 3 is waiting. It does not say the ladder is done.
- Section 4 shows A2 as a full 7-column row.
- Section 5: the next action is to run Q3.2 and paste the result, then `/run-analysis` continues.
- Section 6 lists each query file and whether it was run. `readout.md`: not written yet.
- Section 7 gives the resume steps, including Project files for a chat app.
- Uses "Dana" only because the user said it.

## Fail

- Says "validation complete" or implies results exist.
- Leaves out the open assumption.
- Runs Q3.2 or continues the analysis.
