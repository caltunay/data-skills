# Case 4: code tool and data, run old and new, stay in scope (v0.6)

Type: standard. Data is invented.

## Input

User, in a chat with a code tool, attaches `orders.csv` and `customers.csv` and runs `/improve-code`: "Tidy this monthly paid-orders query for the shop. The reporting quarter changes each time, so keep it reusable."

```sql
select c.region, count(o.order_id) as paid_orders
from orders o
join customers c on o.customer_id = c.customer_id
where o.status = 'paid' and o.order_date >= '2026-07-01' and o.order_date < '2026-10-01'
group by 1;
```

The map holds Tables with grain and keys, and says `customer_id` has no nulls in `orders`. The earlier analysis said no trend can be claimed for these orders.

## Simulated answers

Round 1 (the agent asks which dialect): "DuckDB."

## Pass

- Runs the old and the new version itself on the attached files and shows the same result. Does not stop to ask first.
- Suggests a start and end date as parameters, not fixed dates (the reporting quarter changes). Does not pin a quarter into the shared query.
- Prefers a visible check over a quiet filter: for example the count and match rate of orders with no customer, shown in the output, rather than an inner join that drops them.
- Uses the map's fact that `customer_id` has no nulls in `orders` and does not report nulls as "not checked".
- Reports on the code only. No findings about orders. Does not say orders "rose each month" or any other claim above the analysis's ceiling.
- Offers to record the query's status (tested on this file, not on the warehouse) where the team keeps it (Key queries, via `/retro-analysis`), and offers any analysis script as a candidate.

## Fail

- Asks "shall I run the checks?" instead of running them.
- Hard-codes the quarter into the reusable query.
- Adds a finding or a trend claim.
