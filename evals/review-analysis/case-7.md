# Case 7: review in the same chat that ran the analysis (v0.6)

Type: standard. Data is invented.

## Input

In one chat, the user ran `/run-analysis` on March sign-ups (standard depth) and the draft readout was written. In the same chat the user types `/review-analysis`. The files are in the Project files.

## Simulated answers

Round 1 (the agent asks "A new chat gives a fresher review. Continue here anyway?"): "A, open a new chat." (Variant: "B, continue here." Then it reviews from the files only.)

## Pass

- Shows the card first, before any review work: "A new chat gives a fresher review. Continue here anyway?" with "Open a new chat" recommended.
- On A, tells the user to open a new chat in the same Project (nothing needs attaching) and stops.
- On B, reviews from the files only and says so. It does not lean on what was said earlier in the chat.
- Quick depth skips the card.

## Fail

- Starts the review without asking.
- Asks after it has already reviewed.
