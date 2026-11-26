# Case 7: design ask with low volume and a 4-week limit (v0.6)

Type: design ask. Data is invented.

## Input

User runs `/wayfinder-data`: "Design a test for the new free-shipping banner on the shop's checkout page." The map holds: about 180 paid orders a day, a baseline checkout conversion of about 3.2%, daily orders that swing more than a simple count model assumes, only 4 delivery regions, and no field that tags which arm a visitor saw. A past comparison series (orders from a partner site) has a logging change in March that broke it.

## Simulated answers

Round 1 (the business limits): "It can run 4 weeks at most. If it works we expect about 40,000 more in revenue a month. A wrong call would cost about 15,000 a month. We can switch it off in a day."
Round 2 (the design card): "Take the recommended one."
Round 3 (go-ahead): "A."

## Pass

- Asks the limits first, before any sizing: how long it can run, what it is expected to gain, what a wrong call costs, how easy it is to reverse. Invents no constraint.
- Sizes for 4 weeks, not for the weeks a textbook formula wants, and says plainly what that can and cannot detect (the smallest lift it can see at this volume, and that a smaller real lift looks like noise).
- Derives the margin from the trade-off (expected gain against the loss that would cancel it), and says why a reversible change can accept a looser bar.
- States the sizing assumptions and flags that the swings in daily orders break the simple count model, and what that does to the numbers.
- Offers other designs in the first round of options, because the A/B test is weak: before and after, interrupted time series, difference-in-differences, synthetic control, matched cohorts, a reversible switch with a guardrail alert, no test. Each with pros, cons, data needed, the check that would break it and the claim ceiling.
- Checks options against the map: 4 regions is too few to randomise by region, and no arm tag exists, both said in the option. Rejects the partner series, with the evidence of the March break.
- Raises a goal conflict at the time of choice if the allowed loss clashes with a growth goal.
- Writes an evaluation spec if the chosen design is not an experiment. Names owners for open items by role. Next step is sign-off and the open items.

## Fail

- Sizes a 17-week test first and learns the 4-week limit later.
- Never asks what the change is worth.
- Uses the partner series as the comparison.
