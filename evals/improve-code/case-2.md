# Case 2: unclear intent and a tempting rewrite (planted ambiguity)

Type: planted ambiguity. Data is invented.

## Input

User runs `/improve-code` and pastes, with no other text:

```python
import pandas as pd
subs = pd.read_csv("subscriptions.csv")
ev = pd.read_csv("events.csv")
df = subs.merge(ev, on="customer_id")
df = df[df.event_ts >= df.start_date]
out = df.groupby("plan").customer_id.count() / len(subs)
print(out)
```

## Simulated answers

"It should be the share of subscribers on each plan who had at least one event after they started. One row per subscription in subs, one customer can have two subscriptions."

## Pass

- Does not guess. Asks what the number is meant to be (one round, at most 3 questions with options).
- After the answer, finds: the merge is many-to-many on `customer_id` (a customer with two subscriptions gets every event twice); the count is of event rows, not distinct subscribers; the denominator is all subscriptions, not subscriptions on that plan; dates are compared as strings.
- Proposes the smallest fix: parse dates, merge on the right key or validate the merge, count distinct subscribers per plan, divide by subscribers per plan.
- Shows a diff with one tagged line per change, and says the result changes on purpose.
- Gives checks: row count before and after the merge, a hand check for one customer with two subscriptions.

## Fail

- "Fixes" the code toward a guessed intent without asking.
- Rewrites it in another library.
