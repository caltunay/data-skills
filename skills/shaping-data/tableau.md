# Tableau

Always hand-over mode. Give numbered steps. Ask the user to paste back what they see.

## Principles

- Know the grain of every data source. Tableau shows aggregates, so a wrong grain gives wrong numbers quietly.
- Prefer relationships (logical layer) over joins when tables have different grains. They avoid duplicate rows from fan-out.
- Use a join only when you want a single flat table at a known grain.
- Use extracts for speed, and say when the extract was last refreshed.

## Calculated fields

```
Paid Orders: COUNTD(IF [Status] = "paid" THEN [Order ID] END)
Conversion: [Paid Orders] / COUNTD([Session ID])
```

## LOD expressions

Use them to fix the grain of a calculation.

```
{ FIXED [Customer ID] : COUNTD([Order ID]) }              orders per customer
{ FIXED [Customer ID] : MIN([Order Date]) }               first order date
{ INCLUDE [Product] : SUM([Amount]) }                     add a level
{ EXCLUDE [Product] : SUM([Amount]) }                     remove a level
```

Filters order matters: context filters, then FIXED LODs, then dimension filters. A FIXED LOD ignores normal dimension filters unless they are context filters.

## Checks to hand over

1. Row count: Analysis, View Data, or a `COUNT([Number of Records])` text table.
2. Distinct key count: `COUNTD([Order ID])` next to `[Number of Records]`. They must match at order grain.
3. A total compared to the source system.

## Traps

- Averages of averages. Use `SUM` over `COUNT` at the right level.
- Duplicated measures after a join to a one-to-many table.
- Dual axis charts that hide scale differences.
- Date handling: continuous vs discrete dates change what the chart shows.
