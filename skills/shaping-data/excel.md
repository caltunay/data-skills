# Excel

Always hand-over mode. Give numbered steps. Ask the user to paste back what they see.

## Principles

- One tab per source, untouched. Work on copies.
- Put the data in an Excel Table (Ctrl+T). Use structured references.
- One header row. No merged cells. One value per cell.
- Keep inputs, calculations and outputs on separate tabs.

## Building the analysis table

- **Join:** `XLOOKUP(key, other_table[key], other_table[value], "missing")`. Count rows before and after. XLOOKUP returns the first match, so a one-to-many join hides fan-out. Check key uniqueness with `=COUNTIF(other_table[key], [@key])` and flag any result above 1.
- **Filter:** `FILTER(table, (table[status]="paid")*(table[date]>=DATE(2026,1,1)))`.
- **Dedupe:** `UNIQUE()` or Data, Remove Duplicates on a copy.
- **Aggregate:** a PivotTable. Set grain as the row field. Check the grand total against the source.
- **Long vs wide:** Power Query, Unpivot Columns for long. PivotTable for wide.

## Power Query

Use it for anything repeatable. Each applied step is a named step, visible and re-runnable. Merge queries with the right join kind. Check the row count in the preview after each merge.

## Checks to hand over

1. Row count of the source Table (status bar or `=ROWS(table)`).
2. Count of unique keys: `=COUNTA(UNIQUE(table[key]))`.
3. Sum of the measure compared to the source total.
4. Blank cells in key columns: `=COUNTBLANK(table[key])`.

## Traps

- Numbers stored as text. Dates stored as text.
- Hidden rows and filters that change totals.
- Volatile formulas that slow large files.
- Copy-paste of values that breaks the audit trail. Keep formulas.
