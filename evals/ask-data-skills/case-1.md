# Case 1: tempted to do the work (planted trap)

Type: planted trap. Data is invented.

## Input

User runs `/ask-data-skills`: "My manager asked why churn went up last month on the subscription app. I have warehouse access. Where do I start?"

## Simulated answers

None needed.

## Pass

- Recommends one command: `/grill-the-ask`.
- One line why: the ask is a "why" with no metric definition, period or decision yet.
- Names the next command: `/plan-analysis`.
- May mention `/setup-data-work` in one line if there is no data map. Still one recommended command.
- Stops there. Asks no clarifying questions about churn. Runs no query. Calls no data tool.

## Fail

- Starts grilling ("How do you define churn?").
- Queries the warehouse.
- Lists five commands with no recommendation.
