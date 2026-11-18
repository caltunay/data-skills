# Case 5: observational with rich covariates

Type: method choice. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"Some customers installed our mobile app and some did not. Nobody was assigned. For each customer we have sign-up date, plan, country, acquisition channel, and orders in the 6 months before they installed. Does the app increase orders?"

## Simulated answers

None needed.

## Pass

- Question type: causal, but only an estimate under a strong assumption.
- Method: propensity score matching or inverse probability weighting (observational, rich pre-treatment covariates, no natural experiment).
- Says it is a short card: needs a specialist review before shipping.
- Names the key checks: covariate balance after matching, overlap, pre-treatment covariates only, a sensitivity analysis for a hidden confounder.
- Names the likely hidden confounder: keen customers both install the app and order more.
- States the claim allowed: "estimated effect, assuming no unmeasured confounding", never a bare "caused".
- Offers the stronger option: a randomised nudge to install (then an experiment, or instrumental variables).

## Fail

- Runs a regression and reports the coefficient as the effect.
- Says "the app increases orders by X".
