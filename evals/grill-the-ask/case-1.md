# Case 1: vague ask (planted ambiguity)

Type: planted ambiguity. Data is invented.

## Input

User runs `/grill-the-ask`: "Our CEO wants to know why sign-ups are down. Can you look into it?"

## Pass

- First round has at most 3 questions, each with 2 to 4 options and a recommended default. Waits for answers.
- Covers: the decision it feeds, the metric definition (what counts as a sign-up), the time window and comparison period.
- Does not run any query or start analysis.
- Proposes a question type: descriptive or exploratory. Either passes if the ceiling is stated and "why" is not treated as causal. Says a causal answer needs a design.
- Proposes a depth with a one-line reason.
- Asks who reads the result, in this or a later round. Asks no question twice.
- Writes Meta, Ask (verbatim) and Assumptions into `analysis.md`.

## Fail

- Starts querying.
- Asks 5 or more questions at once.
- Accepts "why" as answerable with no design.
