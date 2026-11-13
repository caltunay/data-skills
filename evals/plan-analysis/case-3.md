# Case 3: simple ask (clean)

Type: clean. Data is invented.

## Input

`analysis.md` holds a grilled ask: "Number of paid orders per week, last 8 weeks, UTC, test accounts excluded." Quick depth. Question type: descriptive.

## Pass

- Gives a one-line plan: group paid orders by week, plus the success check (reconcile to the trusted weekly number or total).
- No options table, no extra methods, no power calculation.
- Writes no files.

## Fail

- Over-builds: multiple options, models, tests.
- Adds invented assumptions.
