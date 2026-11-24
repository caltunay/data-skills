# Case 6: an answer contradicts an earlier one (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/grill-the-ask` in a coding agent with a `DATA-MAP.md` that holds an `orders` table and a `customers` table.

"Our head of e-commerce wants to know how many customers we lost last quarter."

## Simulated answers

Round 1: "A customer is lost if they have not ordered in 90 days. The window is last quarter, 1 July to 30 September 2025. The requester is the head of e-commerce."
Round 2: "Count anyone who ordered in the last 30 days as active. Everything else is lost."
One-at-a-time question: "The 90 days. Use 90 days."

## Pass

- After round 2, says plainly that the answer does not fit the earlier one: 90 days in round 1, 30 days in round 2. Names both.
- Switches to one question at a time until the number of days is settled, then returns to rounds.
- Echoes each round's answers back in the user's own words, and records them word for word in Decisions.
- Records the settled definition (90 days) and does not leave the 30-day answer in the clarified question.
- Ends with the go-ahead question, A) being `/plan-analysis`.

## Fail

- Picks one of the two numbers silently.
- Keeps asking three questions at a time after the conflict.
- Paraphrases an answer in Decisions.
