# Causal questions

Ceiling: "caused", "effect of", only with a randomised experiment or a credible causal design that passed its checks. Observational data with no design gets no causal wording.

Pick the method with the causal method selector in this skill's `SKILL.md`. A randomised test is always the first choice: its card is in `experiment.md`.

## Before any card

- **What is the treatment, and when did each unit get it?**
- **What is the comparison?** Every design is a way to build one. No comparison, no causal claim.
- **What else changed at the same time?** List it. Ask the user. Do not guess.
- If a card's checks fail, the claim drops to descriptive: "Y changed after X". Add a plan revision.

## Card: difference-in-differences

- **When to use:** a change rolled out to some units (regions, customer groups, plans) and not others, and you have data from before and after for both.
- **Data needed:** the outcome per unit and period, for treated and comparison units. Several pre-periods (6 or more is good). The rollout date per unit.
- **Key assumptions:**
  - Parallel trends: without the change, treated and comparison units would have moved in the same way.
  - Nothing else hit only the treated units at the same time.
  - No spillover: the comparison units were not affected by the rollout.
  - The make-up of each group did not change because of the rollout.
- **Checks that must pass:**
  1. **Pre-trends.** Plot both groups over the pre-period. They move together. An event-study plot shows pre-period effects near zero.
  2. **Placebo date.** Pretend the rollout happened earlier, inside the pre-period. The estimate is near zero.
  3. **Placebo outcome.** An outcome the change could not affect shows no effect.
  4. **Other events.** A written list of what else changed for the treated units, checked with the user.
  5. **Standard errors clustered by unit** (the level the rollout was assigned at). With few units (under about 10), say the interval is rough.
  6. **Staggered rollout** (units treated at different times): do not use one two-way fixed effects number. Compare each treated cohort to not-yet-treated units, or get a specialist.
- **Common failure:** treated units were chosen because they were already trending differently; only one pre-period, so the trend cannot be checked; row-level standard errors with three regions.
- **Claim allowed:** "The rollout increased weekly orders in the treated regions by about 4% (95% interval 1% to 7%), assuming the regions would otherwise have followed the comparison regions, as they did in the 12 weeks before."
- **Simplest version first:** the 2 x 2 table: (treated after - treated before) - (comparison after - comparison before). Then the regression for an interval.
- **Tool notes:**
  - SQL: one row per unit and period with `treated` and `post` flags; the 2 x 2 means are four averages.
  - Python: `statsmodels.formula.api.ols("y ~ treated * post", data).fit(cov_type="cluster", cov_kwds={"groups": data["unit"]})`. The interaction is the estimate. Use period dummies for the event-study plot.
  - Excel: the 2 x 2 table by PivotTable. No valid interval from Excel alone.

## Card: interrupted time series

- **When to use:** one series, a known change date, no comparison group. For example, a price change for all customers on one day.
- **Data needed:** a long, evenly spaced series: at least 12 points before and 8 after, more with seasonality (a full year before is good). The exact change date.
- **Key assumptions:**
  - The pre-period trend and season would have continued.
  - Nothing else changed at or near the date.
  - The definition and tracking of the metric did not change at the date.
- **Checks that must pass:**
  1. **Plot it.** The series, the change date, and the projected pre-trend.
  2. **Other events.** A written list of what else happened within a few periods of the date, checked with the user. If there is a rival event, stop: the claim drops to descriptive.
  3. **Seasonality** is modelled, or the same weeks last year show no similar jump.
  4. **Autocorrelation** is handled (Newey-West errors or an ARIMA error term). Plain regression intervals are too narrow.
  5. **Placebo date.** A fake date in the pre-period shows no jump.
  6. **Anticipation and lag.** Say whether the effect should be instant or gradual, before looking.
- **Common failure:** a marketing push in the same week; a seasonal rise read as the effect; three points before and two after.
- **Claim allowed:** weaker than difference-in-differences. "Weekly sign-ups rose by about 9% at the launch (95% interval 3% to 15%) against the pre-launch trend. We found no other change that week. With no comparison group, another cause cannot be ruled out."
- **Simplest version first:** segmented regression: `y ~ time + post + time_since_change`. `post` is the level change, `time_since_change` the slope change.
- **Tool notes:**
  - SQL: build the gap-free series with `time`, `post` and `time_since_change` columns.
  - Python: `statsmodels` OLS with `cov_type="HAC", cov_kwds={"maxlags": k}`, or `SARIMAX` with the step as an exogenous variable.
  - Excel: `LINEST` on the three columns for a first look. The interval will be too narrow.

## Short card: regression discontinuity

- **When to use:** treatment is given by a cut-off on a score: free delivery above a basket value, an offer for customers above a spend threshold.
- **Key assumption:** units just above and just below the cut-off are alike, and nobody can steer their own score across it.
- **Key check:** plot the outcome against the score with the cut-off marked. Check for bunching of units just on one side (a density test). Check that pre-treatment covariates do not jump at the cut-off. The estimate holds across a few bandwidths.
- **Claim allowed:** "caused", for units near the cut-off only. Not for units far from it.

Get a specialist review before shipping.

## Short card: synthetic control

- **When to use:** one treated unit (a region, a market) and several untreated ones, with a long pre-period.
- **Key assumption:** a weighted mix of untreated units tracks what the treated unit would have done. No untreated unit was hit by the change or by its own shock.
- **Key check:** the synthetic unit fits the treated unit closely over the pre-period. Placebo runs, giving the "treatment" to each untreated unit in turn, show the real gap is unusual. Dropping the top-weighted unit does not change the story.
- **Claim allowed:** "caused", for that one unit, with the placebo rank as the uncertainty ("larger than in 19 of 20 placebo runs"). No classical interval.

Get a specialist review before shipping.

## Short card: instrumental variables

- **When to use:** treatment was not random, but something else nudged it at random or as good as random: a randomised reminder email that raises app installs, when the question is the effect of the install.
- **Key assumption:** the instrument moves the treatment, and affects the outcome only through the treatment. The second part cannot be tested. It must be argued.
- **Key check:** the instrument is strong (first-stage F well above 10). Write the argument for why it has no other path to the outcome, and have a domain expert attack it.
- **Claim allowed:** "caused", only for units whose treatment the instrument changed (the compliers). Say this in plain words.

Get a specialist review before shipping.

## Short card: propensity score matching and inverse probability weighting

- **When to use:** observational data, no natural experiment, but rich covariates measured before treatment.
- **Key assumption:** no unmeasured confounding: every factor that affects both treatment and outcome is in the covariates. This cannot be tested.
- **Key check:** after matching or weighting, covariates balance (standardised mean differences under 0.1). Overlap holds: both groups have units across the range of scores. No extreme weights. A sensitivity analysis says how strong a hidden confounder would need to be to remove the effect. Only pre-treatment covariates are used.
- **Claim allowed:** "estimated effect, assuming no unmeasured confounding", never a bare "caused". Name the most likely missing confounder.
- **Tool notes:** Python: DoWhy or EconML; `sklearn` for the score.

Get a specialist review before shipping.

## Short card: uplift and heterogeneous treatment effects

- **When to use:** the question is who to treat, not whether it works. Which customers should get the win-back offer?
- **Key assumption:** the data comes from a randomised experiment (or a design that passed its checks). Uplift models on observational data inherit all its bias.
- **Key check:** the average effect is established first. The uplift model is scored on a held-out randomised sample with an uplift or Qini curve. Segments found by the model are confirmed in a fresh test before a rollout.
- **Claim allowed:** "The model ranks customers by predicted response to the offer. In the held-out test, the top 20% showed 3 times the average effect." Segment effects are hypotheses until re-tested.
- **Tool notes:** Python: EconML or CausalML.

Get a specialist review before shipping.

## None fits

Say so plainly. Give the ceiling the data supports ("orders changed after the launch"). Offer the best descriptive path, and the cheapest design that would support a causal claim next time (usually a holdout).

## Not allowed

- "caused", "impact of", "thanks to", "due to" without a card whose checks passed.
- "Proved."
- An effect for all customers from a design that covers only some (near a cut-off, compliers, one region).
