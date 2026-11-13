# Case 1: plan cannot reach the claim (planted flaw)

Type: planted flaw. Data is invented.

## Input

`analysis.md` holds a grilled ask: "Did the new onboarding flow, launched 4 Feb, increase 30-day retention?" Standard depth. Question type was set to causal. Data: all users, before and after the launch. No holdout.

## Pass

- Says up front that the data cannot support a causal claim. States the ceiling: "retention changed after 4 Feb".
- Lists 2 to 4 options with trade-offs, for example before and after with a seasonality check, a comparison by signup cohort, a proposed future holdout.
- Records a plan revision or lowers the question type, with a reason.
- Writes an analysis table spec (grain, keys, window, filters, expected rows) and success checks.

## Fail

- Plans a causal claim from before and after data.
- Skips the table spec.
