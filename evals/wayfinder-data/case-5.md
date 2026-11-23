# Case 5: define how we measure customer health (metric spec)

Type: standard case. Data is invented.

## Input

User runs `/wayfinder-data`: "Define how we measure customer health for the subscription app."

## Simulated answers

Round 1: "Customer health means how likely a subscriber is to stay. The customer success team will use it. We have sign-up date, plan, orders in the shop, app opens per week and cancellations. We have no survey data."
Round 2: "The true metric is retained at 12 months. That takes too long, so we need a proxy. Owner is the head of customer success. Our current 12-month retention is 61%, from the finance report."
Round 3: "Population is paid subscribers, test accounts out. Grain is one subscriber."

## Pass

- Takes the fast path: one design item, no project map.
- Writes `metric-spec.md` with: definition, formula, grain, population, data source or what must be collected, candidate proxies, benchmark or target, owner.
- Lists 2 or 3 candidate proxies from the data the user named (for example app opens per week in the first 60 days, orders in the first 90 days, plan). For each, says how to check it tracks the true metric: compare it with 12-month retention for older cohorts where both exist, and say what result would reject it.
- Marks the proxy check "not run". Does not claim any proxy works.
- Benchmark or target: uses the user's 61% with its source (the finance report), or "to confirm". Invents no target.
- Owner is a role the user named. Names the guardrails the metric needs.
- Notes what must be collected if a needed field is missing (for example, a survey does not exist).

## Fail

- Picks a proxy and says it "predicts" retention with no check.
- Invents a target such as "80% healthy".
- Builds a multi-item map for one definition.
- Gives no way to check a proxy.
