# Case 1: vague ask (planted ambiguity)

Type: planted ambiguity. Data is invented.

## Input

User runs `/grill-the-ask`: "Our CEO wants to know why sign-ups are down. Can you look into it?"

## Pass

- First round has at most 3 questions, each with 2 to 4 options and a recommended default. Waits for answers.
- Covers: the decision it feeds, the metric definition (what counts as a sign-up), the time window and comparison period.
- Does not run any query or start analysis.
- Proposes a question type (descriptive first, since "why" is not reachable yet) and a depth, and says why.
- Writes Meta, Ask (verbatim) and Assumptions into `analysis.md`.

## Fail

- Starts querying.
- Asks 5 or more questions at once.
- Accepts "why" as answerable with no design.
