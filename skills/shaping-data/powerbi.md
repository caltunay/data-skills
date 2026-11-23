# Power BI

Always hand-over mode. Give numbered steps. Ask the user to paste back what they see.

## Principles

- Model first: a star schema. Fact tables (events, orders) in the middle, dimension tables (customer, date, product) around them.
- Relationships are one-to-many, single direction by default. Avoid many-to-many unless you must.
- Use a proper date table, marked as the date table.
- Do shaping in Power Query. Do calculations in DAX measures.

## Analysis table spec in Power BI

- Grain is the fact table's row. Write it down.
- Dimensions are the columns you slice by, from the dimension tables.
- Measures are DAX measures, not calculated columns, unless the value is needed as a row-level filter or axis.

## DAX patterns

```
Paid Orders = CALCULATE ( DISTINCTCOUNT ( Orders[order_id] ), Orders[status] = "paid" )

Paid Orders Share = DIVIDE ( [Paid Orders], DISTINCTCOUNT ( Orders[order_id] ) )
```

- Use `DIVIDE` not `/` to handle zero.
- Use variables (`VAR`) to name steps.
- Remember filter context: a measure changes with every slicer and visual.

## Fan-out checks

- Check relationship cardinality in Model view.
- In a table visual, show a key count next to the total: `Rows = COUNTROWS ( Orders )` and `Keys = DISTINCTCOUNT ( Orders[order_id] )`. They must match at the expected grain.
- Compare a visual total to the source table's total.

## Traps

- Bi-directional filters that create ambiguity.
- Blank rows from broken relationships (a blank member in a slicer).
- Implicit measures from dragging columns. Write explicit measures.
- Row-level security changing totals for the viewer.
