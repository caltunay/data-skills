# Case 1: fan-out and a silent inner join (planted flaws)

Type: planted flaws. Data is invented.

## Input

User runs `/improve-code`: "Can you tidy this up? It gives revenue per customer segment for January. Postgres. `orders` is one row per order, `order_items` is one row per item, `customers` is one row per customer."

```sql
select c.segment, sum(o.amount) revenue, count(distinct o.order_id) orders
from orders o
left join order_items i on i.order_id = o.order_id
left join customers c on c.customer_id = o.customer_id
where o.order_ts between '2026-01-01' and '2026-01-31'
and o.status = 'paid'
and c.is_test = false
group by 1
```

## Simulated answers

"Yes, fix the bugs. I don't need the items table."

## Pass

- States the intent first: paid revenue and orders per segment, January.
- Finds the fan-out: the join to `order_items` multiplies `o.amount` by the number of items. Says revenue is overstated. Removes the join (it is not used).
- Finds the date bug: `between` on a timestamp drops 31 January after midnight. Proposes a half-open range.
- Notes that the filter on `c.is_test` turns the left join into an inner join, and asks or states whether orders with no customer row should drop.
- Shows a diff, one tagged line per change. Bug fixes are separate from style changes.
- Says the bug fixes change the result on purpose, with the expected direction (revenue falls, orders may rise slightly for the 31st).
- Hands over numbered check queries with expected results. Does not claim "equivalent".
- Calls no data tool: the user named no connected source.

## Fail

- Only reformats.
- Rewrites the whole query in a new structure without being asked.
- Says the result is unchanged.
