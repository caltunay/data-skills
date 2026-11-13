---
name: stats-tests
description: Choose or interpret a statistical test or interval in a data analysis. Applies when comparing groups, testing a difference, sizing a sample, handling many comparisons, or reporting uncertainty and practical significance.
---

# Stats tests

A test answers a narrow question. Pick it from the data and the design, then report size and uncertainty, not only a p-value.

## Core rule

Choose the test by data type and design. State its assumptions. Report direction, magnitude and uncertainty. Separate statistical from practical significance. Correct for multiple comparisons.

## Choosing a test

| Outcome | Groups | Test |
|---|---|---|
| Proportion or rate (converted or not) | 2 independent | Two-proportion z-test, or Fisher's exact when counts are small |
| Proportion | 3 or more | Chi-square test |
| Continuous, roughly symmetric | 2 independent | Welch's t-test |
| Continuous, skewed or ordinal | 2 independent | Mann-Whitney U |
| Continuous, paired (before and after on the same unit) | 2 | Paired t-test, or Wilcoxon signed-rank if skewed |
| Continuous | 3 or more | ANOVA, or Kruskal-Wallis if skewed |
| Two continuous variables | n/a | Correlation (Pearson, or Spearman if skewed) with an interval |
| Count of events per unit | 2 | Poisson or negative binomial model |
| Heavy-tailed money metric | 2 | Bootstrap the difference in means, or compare log values |

## Assumptions to check

- Independence of units. Repeated rows per user break it. Analyse at the unit of randomisation or sampling.
- Sample size big enough for the approximation.
- Spread: use Welch's version unless variances are clearly equal.
- Outliers: look before you test. Heavy tails can dominate a mean.

## Power and MDE

- MDE: the smallest effect that matters to the decision. Set it before looking at results.
- Power: usually 80%. Alpha: usually 5%.
- Sample size for a difference in proportions, per arm, roughly: n = 16 x p x (1 - p) / delta^2, where p is the baseline rate and delta the absolute MDE.
  Example: baseline 10%, delta 1 point: 16 x 0.1 x 0.9 / 0.0001 = 14,400 per arm.
- A flat result from an underpowered test is not "no effect". Say what size it could have detected.

## Multiple comparisons

- One primary metric. All others are secondary or exploratory.
- Many metrics or segments: correct (Bonferroni is simple and conservative, Benjamini-Hochberg controls the false discovery rate) or label them exploratory.
- A win found only after slicing is a hypothesis.

## Interpreting

Report three things:

1. **Direction.** Up, down, no clear change.
2. **Magnitude.** The effect in the metric's own units, and in money or users per period if possible.
3. **Uncertainty.** An interval (95% by default), not only a p-value.

Example: "Conversion rose 0.4 points (95% interval 0.1 to 0.7). That is about 800 extra orders a month."

- A p-value is not the probability the effect is real.
- p < 0.05 with a tiny effect can be statistically significant and practically irrelevant. Say which it is.
- A wide interval that includes zero and the MDE means the test cannot tell. Say so.
- Do not use causal wording unless the design supports it. Apply the `question-types` skill for the ceiling.

## Do not

- Do not test until something is significant.
- Do not stop a test early because it looks good.
- Do not run a test you cannot interpret. If the design does not match any test above, say so and ask.
