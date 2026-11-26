format: v1
updated: YYYY-MM-DD HH:MM

# Experiment spec: <title>

Status: draft | agreed
Owner: <a role the user names, or "to confirm">
Date:

Fill every line. If a line cannot be filled, write what is missing and who can supply it. Never invent a number: a number comes from the user, the data map or a stated calculation.

## 0. Business limits

Asked before any sizing. Never invent a limit the user did not give.

- How long the test can run:
- Expected gain if the change works (value, period, where the figure comes from):
- Cost of being wrong:
- Easy to reverse? (and the guardrail that makes reversal safe):
- Designs considered (A/B, before and after, time series, difference-in-differences, synthetic control, matched cohorts, reversible switch with alert, no test), and why this one. If the chosen design is not an experiment, this file is an evaluation spec: replace section 2 with the design, its breaking check and its claim ceiling.

## 1. Hypothesis

- Change being tested:
- Hypothesis (one sentence, with the direction and the metric):
- Decision it feeds (what is shipped or not, by whom):

## 2. Design

- Unit of randomisation: <customer | session | device | account, and why>
- Feature gate or assignment: <how a unit is assigned, who or what holds the flag, and that the split is fixed for the whole run>
- Arms and split: <for example control and variant, 50/50>
- Population: <who is in, who is out (staff, test accounts)>
- Interference risk: <can one unit affect another: shared stock, referrals, shared codes>

## 3. Metrics

- Primary metric: <one, with its definition. See the `metric-spec.md` if it is new>
- Guardrails: <each with the level that stops a rollout>
- Unit of analysis: <must equal the unit of randomisation>

## 4. Size and time

- Baseline rate or mean: <value, period, where it comes from>
- MDE (smallest effect worth shipping): <value, and why that size>
- Power and significance level: <for example 80% power, 5% two-sided>
- Sample per arm: <from the calculation, with the formula or tool used>
- Runtime: <days, fixed in advance, at least one full weekly cycle>
- Seasonality: <holidays, sales, month-end, releases that overlap the run, and what is done about them>
- What this size can and cannot detect: <in plain words>
- Sizing assumptions, and whether the data breaks them:
- Overlapping tests: <does an independent split keep the comparison fair, what interaction risk remains, start date after the other test ends as an option>

## 5. Checks and decision rule

- SRM check plan: <the planned split, the test (chi-square), and the rule: p < 0.001 means stop and explain before reading results>
- Other checks that must pass: <from the experiment method card: design held, no peeking, full weekly cycles, multiple comparisons, novelty, no overlap>
- Decision rule (written before the test): <what result ships, what result stops, what result means run longer or test again>
- Claim allowed: <the wording a valid result supports, for this population, period and metric>

## 6. Open items

| item | likely owner (role) | by when (only if a meeting or launch sets one) |
|---|---|---|
