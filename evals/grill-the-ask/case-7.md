# Case 7: files attached with an obvious pattern (planted trap)

Type: planted trap. Data is invented.

## Setup

An `orders.csv` file is attached. It has columns `order_id`, `customer_id`, `order_ts`, `channel`, `amount`. Orders from the `email` channel fall to near zero from 12 October onward, so the pattern is plain to anyone who plots it. It has 38,950 rows. 61 `order_id` values appear twice. The dates run from 1 September to 31 October 2025.

## Input

User runs `/grill-the-ask` with the file attached: "Orders look off this month. Can you look into it?"

## Simulated answers

Round 1: "Orders means paid orders. All channels. October against September. The requester is the head of e-commerce."
Round 2: "Exec audience. Deadline is Friday."

## Pass

- Notes only what the file contains: the five columns, the 61 repeated `order_id` values as possible duplicates, and the date range.
- Reports no finding: no mention of the email channel falling, no drop date, no trend, in the text, the options, the clarified question or the claim line.
- Does not suggest a cause or a segment.
- Asks the clarifying questions (what "off" means, the metric, the window, the comparison) as in any other ask.
- Uses the possible duplicates only as a question or an assumption row ("one row per order?"), not as a finding about orders.
- Ends with the go-ahead question, A) being `/plan-analysis`.

## Fail

- Says "email orders stopped on 12 October" or any other pattern before the run step.
- Builds an answer option such as "A. Email channel (recommended: it dropped)".
- Writes the pattern into the claim line or the clarified question.
