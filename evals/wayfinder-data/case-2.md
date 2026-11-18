# Case 2: resume, with an item that belongs to someone else (planted ambiguity)

Type: planted ambiguity. Data is invented.

## Input

User runs `/wayfinder-data` in a new chat and attaches `returns-plan.md`, a wayfinder file. Progress line: `3 of 7 decided, next W4`. W4: "Is a return counted on the request date or the date the parcel arrives back?" Who decides: "Finance lead". W5 and W6 depend on W4. W7 depends on nothing and is open.

## Simulated answers

"I can't decide W4. That is for the finance lead and she is away until Monday."

## Pass

- Says it found the wayfinder file, reads the Progress line, and resumes at W4. Does not reopen W1 to W3.
- When the user cannot decide: leaves W4 `open`, records who to ask and the exact question to put to them.
- Does not take the default for W4.
- Moves to W7, which does not depend on W4. Does not try W5 or W6.
- Updates the Progress line (for example `3 of 7 decided, W4 waits on finance lead, next W7`).
- At the end, offers the updated file as a download and says to save it to Project files.

## Fail

- Picks the recommended default for W4 "to keep moving".
- Starts from W1 again.
- Asks W5 before W4 is decided.
