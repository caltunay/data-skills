# Case 2: vague request, needs one round (planted ambiguity)

Type: planted ambiguity. Data is invented.

## Input

User runs `/ask-data-skills`: "Not sure which one I need."

## Simulated answers

"B, I have results already. D. Yes there is an analysis.md, and I need to send something to the exec team tomorrow."

## Pass

- Asks one round of at most 3 questions, each with options. Waits.
- After the answer, asks nothing more.
- Recommends `/review-analysis` (results exist, not yet reviewed), with one line why.
- Names `/storytell` as the next command for the exec version.
- Uses the three-line answer format.

## Fail

- A second round of questions.
- Recommends `/storytell` first, on a readout that is not final.
- Starts the review itself.
