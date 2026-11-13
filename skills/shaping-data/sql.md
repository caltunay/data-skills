# SQL

Dialect comes from the Sources table in the data map. If unknown, ask once.

## Style defaults

Based on the sqlstyle.guide by Simon Holywell (https://www.sqlstyle.guide/), summarised in our own words. The data map Conventions section overrides these.

- Lowercase keywords and names. Snake case for names.
- One clause per line. Indent the body of each clause.
- Use `where true` then one condition per line starting with `and`. Easy to comment out.
- Leading commas in select lists, aligned.
- Use CTEs, not subqueries, wherever possible. Name each CTE for what it holds.
- Use the full table name. Avoid short aliases.
- Qualify every column with its table name when there is more than one table.
- Use `as` for column aliases. Use clear names, not abbreviations.
- Prefer explicit `join` types over comma joins. Put the `on` conditions on a new line.
- Comment the why, not the what.
- End the statement with a semicolon on its own line.

## Pattern

```sql
with
    paid_orders as (
        select
            order_id
          , customer_id
          , order_ts
        from
            orders
        where true
            and status = 'paid'
            and order_ts >= date '2026-01-01'
            and order_ts <  date '2026-02-01'
    )

select
    customers.segment
  , count(distinct paid_orders.order_id) as order_count
from
    paid_orders
join
    customers
    on customers.customer_id = paid_orders.customer_id
where true
group by 1
;
```

## Checks

- Row count before and after each join:

```sql
select count(*) as row_count from paid_orders;
```

- Key uniqueness on the "one" side:

```sql
select
    customer_id
  , count(*) as row_count
from
    customers
where true
group by 1
having count(*) > 1
;
```

## Dialect notes

Check the dialect for these, they differ most:

- Date truncation and date arithmetic.
- String and array functions.
- Integer division (cast to decimal before dividing).
- Null ordering and `distinct` behaviour.
- Time zone conversion.
- Limits on query size or partition filters (large warehouses often require a date filter on partitioned tables).

## Performance

- Filter early, on partition or date columns.
- Select only the columns you need.
- Aggregate before joining when you can.
- Do not use `select *` in final queries.
