# Case 1: non-data vague ask (must not fire)

Type: trigger check. Data is invented.

## Setup

All data-skills are installed. No slash command is used.

## Input

"Can you help me sort out the team offsite? I'm not sure where to start."

## Simulated answers

None needed.

## Pass

- `grilling` does not apply. The agent answers as it normally would.
- No rounds of "at most 3 questions with options and a recommended default" in the `grilling` format.
- No mention of question types, depth, assumptions tables, data maps or `analysis.md`.

## Fail

- The reply follows the `grilling` format or names any data-skills step.

## Contrast (should fire)

Inside `/grill-the-ask`, or on "Can you look into why sign-ups are down?" during a flow step, `grilling` applies.
