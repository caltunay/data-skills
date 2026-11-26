format: v1
updated: 2026-02-24 09:00

# Readout: pricing page test, February 2026

**Status: FINAL**

Audience: product
Date: 2026-02-25

## TL;DR

The new pricing page lifted the share of visitors who ordered within a week, from about 10% to about 12%. The test was valid, but the size of the gain is uncertain and the second week was weaker. Roll it out to 95% of visitors and hold 5% back for four weeks.

## The new page lifted orders from 10.2% to 11.8% of visitors, and we are 95% sure the lift is real

The best estimate is 1.65 points. The true gain could be as small as 0.2 points or as large as 3.1. The split between arms was clean (49.7% and 50.3%), so the comparison is fair.

**In this test the new page caused more visitors to order.**

## The second week was weaker, so the gain may fade

Week 1 showed +2.7 points. Week 2 showed +0.6 points, and its range includes zero. The two weeks do not differ clearly, so this may be chance or early interest wearing off. Two weeks cannot tell the two apart. The holdout will.

> **Ask:** roll the new page out to 95% of visitors and keep 5% on the old page for four more weeks. That shows whether the gain holds at the week 1 level, the week 2 level, or in between. Revenue per visitor leaned up, but the test cannot confirm a revenue gain, so do not book one yet.

## Caveats

> **Caveat:** the effect was smaller in week 2. Two weeks cannot say if that is chance or a fade.

- Open high-impact assumptions: none.
- What this analysis can and cannot say: it shows the effect of the new page for external visitors to the pricing page between 2 and 15 February, on orders within 7 days. It does not show the effect for other pages, other periods or longer-term spend.
- The gain appeared on mobile (+2.8 points) and not on desktop (0.0). This was found by slicing after the test, so it is a pattern to test, not a result.
- Average order value was lower in the variant (40.68 against 43.15). This was not a planned measure and was not tested. Revenue per visitor, which was planned, covers it.

## Method

Data: 7,397 external visitors assigned at random, 50/50, by visitor, 2 to 15 February 2026. Paid orders within 7 days of assignment, read after the last window closed.
Method: randomised experiment, analysed per visitor with a two-proportion test. Primary metric, sample size (3,600 per arm for a 2.0 point effect) and run length were fixed before the test.
Checks passed: split, design held, no early stop, sample size, unit of analysis, two full weeks, guardrails, ladder rungs 1 to 5 as logged in `analysis.md`, and visitor counts equal to the experiment platform. The deep-depth alternative specification was not run. Working notes: `analysis.md` (its Review pack lists the scripts behind each headline number).

## Appendix

| number | value | uncertainty |
|---|---|---|
| Conversion, control | 10.15% (373 of 3,675 visitors) | exact for the test |
| Conversion, variant | 11.79% (439 of 3,722 visitors) | exact for the test |
| Effect of the new page | +1.65 points (+16% relative) | 95% interval +0.22 to +3.07 points. p = 0.024 |
| Revenue per visitor | 5.17 to 5.87, +0.70 | 95% interval -0.14 to +1.54. Not clearly up, not clearly down |
| Split between arms | 49.7% and 50.3% | planned 50/50. No sign of a mismatch (p = 0.59) |
| Effect, week 1 | +2.67 points | 95% interval +0.63 to +4.71 |
| Effect, week 2 | +0.59 points | 95% interval -1.39 to +2.58. The two weeks do not differ clearly (p = 0.15) |
| Return rate per paid order | 8.64% to 7.64% | 95% interval for the change -4.46 to +2.45 points. Not clearly higher |
