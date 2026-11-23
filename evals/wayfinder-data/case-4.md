# Case 4: design an A/B test, fast path (single design item)

Type: standard case. Data is invented.

## Input

User runs `/wayfinder-data`: "Design an A/B test for the new pricing page on the shop."

## Simulated answers

Round 1: "The goal is to know if the new page lifts paid orders. For the product team. Baseline conversion is 10% within 7 days. About 500 visitors a day. We can run it for 2 weeks at most."
Round 2: "Randomise by visitor. The experiment platform holds the flag. The smallest effect worth shipping is 2 points. Guardrails are revenue per visitor and return rate."
Round 3: "Ship if the interval is above zero and guardrails hold. Otherwise keep the current page."

## Pass

- Takes the fast path: says this is one design item, builds no decision map and no wayfinder project file.
- Does one framing round of at most 3 questions, then fills `experiment-spec.md` section by section.
- `experiment-spec.md` has: hypothesis, unit of randomisation, feature gate or assignment, primary metric, guardrails, MDE, power, runtime, seasonality, SRM check plan, decision rule.
- Sample size is shown as a calculation with its inputs (baseline 10%, MDE 2 points, power, significance level). Checks that it fits 500 visitors a day over 2 weeks and says so if it does not.
- Seasonality: names weekly cycles and any sale or holiday in the window, or marks it "to confirm".
- Uses no number the user did not give. A missing number is "to confirm".
- Chat app: hands the file back whole, with `format:` and `updated:` lines.

## Fail

- Builds a 6-item decision map first.
- Invents a baseline or a power figure.
- Does the arithmetic in its head and states a sample with no inputs.
- Skips the SRM check plan or the decision rule.
