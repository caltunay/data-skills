# Case 2: one market treated

Type: method choice. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"We launched the subscription app's family plan in one country only, on 1 March. We have monthly sign-ups for that country and for 14 other countries, 3 years back. What was the effect on sign-ups?"

## Simulated answers

None needed.

## Pass

- Question type: causal.
- Method: synthetic control (one treated unit, several untreated units, long pre-period).
- Says it is a short card: an advanced method that needs a specialist review before shipping.
- Names the key checks: close pre-period fit, placebo runs on the untreated countries, drop the top-weighted country.
- Asks whether any other country had its own launch or shock.
- States the claim allowed: for that one country, with the placebo rank as the uncertainty.

## Fail

- Picks difference-in-differences with one treated unit and reports a normal interval without comment.
- Leaves out the specialist-review line.
