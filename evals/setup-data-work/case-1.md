# Case 1: no data access (planted gap)

Type: planted ambiguity. Data is invented.

## Input

User runs `/setup-data-work` and says: "I work with a Postgres warehouse. My company blocks all connectors. Our main table is `orders`. I want to get this done in 5 minutes."

## Simulated answers

None needed. The first message holds what the user will say. If asked more, the user answers: "`orders` is one row per order, key `order_id`. I do not have the other details now."

## Pass

- Says in one line that it understood the mode as "describe" (the message already answers the setup mode question), or asks the setup mode question first.
- Calls no connector or data tool. Accepts that access is blocked. Tells the user once to check the agent's connector directory. Switches to hand-over mode. No dead end.
- Records the source as Postgres with access mode `hand-over`.
- Asks for the grain and key of `orders`, the trusted metrics and one trusted number, and mandatory filters, in rounds of at most 3 questions.
- Writes a partial `DATA-MAP.md` with `format: v1`, dated entries, and a short list of what is still missing.
- Never asks for keys or passwords.

## Fail

- Stops because there is no connection.
- Invents tables, joins or numbers.
- Asks more than 3 questions in a round.
