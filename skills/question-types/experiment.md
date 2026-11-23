# Experiment questions (A/B tests)

Ceiling: a valid randomised test supports a causal claim for the tested population, period and metric. Anything else does not.

## Card: randomised experiment (A/B)

- **When to use:** you can assign the change at random to some units (customers, sessions, accounts) and hold it back from others. First choice in the causal method selector.
- **Data needed:** one row per randomised unit: arm, assignment time, primary metric, guardrail metrics, pre-period covariates if any. The planned split and sample size.
- **Key assumptions:**
  - Assignment is random and was not changed during the run.
  - One unit cannot affect another (no interference: shared stock, referrals, shared discount codes).
  - The metric, sample size and run length were fixed before the test.
- **Checks that must pass:**
  1. **Sample ratio mismatch (SRM).** Arm sizes match the planned split. A chi-square test with p < 0.001 means the test is broken. Do not read results until it is explained.
  2. **Design held.** Primary metric, sample size and run length are the ones fixed in advance.
  3. **No peeking.** The test was not stopped early because it looked good. Early stopping inflates false positives.
  4. **Power.** The sample was big enough for the effect that matters (the MDE). A flat result from an underpowered test says nothing.
  5. **Unit of analysis equals unit of randomisation.** Analysing sessions when customers were randomised makes intervals too narrow.
  6. **Full weekly cycles.** At least one, better two.
  7. **Multiple comparisons.** One primary metric. Many metrics or segments get a correction or the label exploratory.
  8. **Guardrails.** Revenue, error rate, page speed and returns did not get worse.
  9. **Novelty and primacy.** Plot the effect by day or week. Does it shrink or grow?
  10. **No overlap** with a holiday, a sale or a release that hit one arm more than the other.
- **Common failure:** reading a win with an SRM; stopping at the first p < 0.05; presenting a segment found after slicing as the result; "no effect" from an underpowered test.
- **Claim allowed:** "The variant increased conversion by 0.4 points (95% interval 0.1 to 0.7) in this test, for these customers, in this period." A win found only after slicing is a hypothesis.
- **Simplest version first:** two arms, one primary metric, a two-proportion z-test or Welch's t-test, a fixed horizon. Add variance reduction or sequential methods only when needed.
- **Tool notes:**
  - SQL: count units per arm for the SRM check; aggregate the metric per randomised unit before comparing.
  - Python: `scipy.stats.chisquare` for SRM; `statsmodels.stats.proportion.proportions_ztest` and `confint_proportions_2indep`; `statsmodels.stats.power.NormalIndPower` for sample size.
  - Excel: `CHISQ.TEST` for SRM; a z-test by hand from the two rates and counts.

## Before the test

- **One primary metric**, fixed in advance. Guardrail metrics listed too.
- **Unit of randomisation:** customer, session, device or account. Analyse at that unit.
- **Power and MDE:** the smallest effect that matters, and the sample needed to detect it. State the numbers. Rough sample per arm for a rate: n = 16 x p x (1 - p) / delta^2.
- **Runtime:** fixed in advance, at least one full weekly cycle.
- **A/A test** where the setup is new: do two identical arms show no difference?

## Reporting

Give direction, magnitude and uncertainty: "Variant raised conversion by 0.4 points (95% interval 0.1 to 0.7)." Then say whether the size is practically meaningful, in money or customers per month.

## Allowed wording

- "The variant increased conversion by about 0.4 points in this test."
- "No detectable effect. The test could detect a 1 point change, not smaller."

## Not allowed

- "No effect." (when underpowered)
- "The variant works for mobile users." (found after slicing)
- "This will add 2M a year." (extrapolation without stated assumptions)

## When the plan cannot hold

No clean control, SRM, broken assignment, or a contaminated arm: add a plan revision entry to `analysis.md`. The question may drop to a lower type with a lower ceiling.
