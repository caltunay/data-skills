# Experiment questions

Ceiling: a valid randomised test supports a causal claim for the tested population, period and metric. Anything else does not.

## Before the test

- **One primary metric**, fixed in advance. Guardrail metrics listed too.
- **Unit of randomisation**: user, session, device, account, store. Analyse at that unit. Analysing at a finer unit (sessions when users were randomised) makes intervals too narrow.
- **Power and MDE**: the smallest effect that matters, and the sample needed to detect it. State the numbers.
- **Runtime**: fixed in advance, at least one full weekly cycle. Two cycles is better when behaviour differs by weekday.
- **A/A test** where the setup is new: do two identical arms show no difference?

## Readout checks, in order

1. **Sample ratio mismatch (SRM).** Do arm sizes match the planned split? A chi-square test with p < 0.001 means the test is broken. Do not read results until it is explained.
2. **Design held?** Metric, sample size and run length fixed before the test.
3. **Peeking.** Was it stopped early because it looked good? Early stopping inflates false positives.
4. **Power.** Was the sample big enough for the effect that matters? A flat result from an underpowered test says nothing.
5. **Multiple comparisons.** One primary metric. Many metrics or many segments checked means some will look good by chance. Correct or label as exploratory.
6. **Novelty and primacy.** Does the effect shrink or grow over time? Plot the effect by day or week.
7. **Seasonality.** Did the run overlap a holiday, a sale or a release?
8. **Guardrails.** Did revenue, errors, latency or support contacts get worse?
9. **Segments.** A win found only after slicing is a hypothesis, not a result.
10. **Interference.** Can one arm affect the other (shared inventory, social effects, shared drivers)?

## Reporting

Give direction, magnitude and uncertainty: "Variant raised conversion by 0.4 points (95% interval 0.1 to 0.7)." Then say whether the size is practically meaningful, in money or users per month.

## Allowed wording

- "The variant increased conversion by about 0.4 points in this test."
- "No detectable effect. The test could detect a 1 point change, not smaller."

## Not allowed

- "No effect." (when underpowered)
- "The variant works for mobile users." (found after slicing)
- "This will add 2M a year." (extrapolation without stated assumptions)

## When the plan cannot hold

No clean control, SRM, broken assignment, or a contaminated arm: add a plan revision entry to `analysis.md`. The question may drop to a lower type with a lower ceiling.
