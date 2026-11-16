# Case 2: fan-out risk in the spec (planted flaw)

Type: planted flaw. Data is invented.

## Input

`analysis.md` holds a grilled ask: "Average order value by customer segment, September 2026." The data map lists `orders` (one row per order) and `order_items` (one row per item) with the join marked as a fan-out trap for order-level amounts. Standard depth.

## Pass

- Sets the grain as one row per order. Takes `amount` from `orders` and does not join `order_items` for the measure.
- Mentions the fan-out trap from the data map and how to avoid it.
- Success checks include a row count check and a reconcile to the trusted number.
- Offers 2 options at most, picks the simple one.

## Fail

- Joins items and sums the order amount.
- Ignores the data map.
