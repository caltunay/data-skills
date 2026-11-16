# Case 6: randomised test (clean)

Type: method choice, clean. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"We randomly assigned 50% of new visitors to a new pricing page for 14 days, by visitor ID. Primary metric: paid sign-up within 7 days. The sample size was fixed in advance. How should we analyse it?"

## Pass

- Question type: causal.
- Method: randomised experiment (A/B), the first step of the causal method selector. No fancier method.
- Names the checks, with the sample ratio mismatch check first, then: design held, no peeking, power, analysis at visitor level, guardrails.
- Proposes a two-proportion test with an interval for the difference.
- States the claim allowed: causal, for this population, period and metric.
- Invents no problem with the design.

## Fail

- Proposes difference-in-differences, matching or a model where a simple test is enough.
- Skips the sample ratio check.
