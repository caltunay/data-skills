# Case 1: rollout to some regions with a pre-period

Type: method choice. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"The shop switched on free returns in 3 of our 12 delivery regions on 1 June. We have weekly orders per region for the last year. Did free returns increase orders? Which method should we use?"

## Simulated answers

None needed.

## Pass

- Question type: causal.
- Method: difference-in-differences, reached through the causal method selector (no randomisation, rollout to some units, comparison group and pre-period exist).
- Names these checks: pre-trends (plot or event study), a placebo date in the pre-period, what else changed in the 3 regions, standard errors clustered by region.
- Asks how the 3 regions were chosen.
- Notes that 12 regions are few clusters, so the interval is rough.
- States the claim allowed, with the parallel-trends condition.

## Fail

- Picks a plain before and after, or a t-test on treated regions only.
- Says "caused" with no pre-trend check.
