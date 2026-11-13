---
name: shaping-data
description: Get data into shape for an analysis in SQL, Python, Excel, Power BI or Tableau. Applies when designing the analysis table or building it from sources, including grain, joins, filters and long vs wide layout.
---

# Shaping data

Design the table first. Build it second. Tool choice comes last.

## Core rule

Write the analysis table spec before any query or code, with no reference to a tool. Then build it with named steps and check every join for fan-out.

## Step 1: analysis table spec

Fill in all of these:

- **Grain:** what does one row mean? Say it in one sentence.
- **Keys:** the column or columns that make a row unique.
- **Measures and dimensions:** what is counted or summed, and what it is sliced by.
- **Time column and window:** which timestamp, which range, which time zone.
- **Filters and exclusions:** from the data map (test accounts, cancelled orders, and so on). Say which came from the map.
- **Tidy (long) or wide, and why:** long suits grouping, plotting and tests. Wide suits side-by-side reading and some models. Pick for this question.
- **Context columns:** what a reader needs to interpret results (segment names, plan type, status).
- **Expected row count or range:** a guess you can check later.

## Step 2: build rules

1. **Grain first.** Decide the grain of each source before joining. Aggregate to the join grain before you join, not after.
2. **Join fan-out checks.** Count rows before and after every join. A many-to-one join must not change the row count of the "one" side's driving table. Assert it. Check key uniqueness on the "one" side.
3. **Join type.** A left join followed by a filter on the right table silently becomes an inner join. Filter in the join condition or handle nulls on purpose.
4. **Filters from the data map.** Apply mandatory rules. Say which you applied.
5. **Named steps.** One idea per step, each with a clear name. No nested mega-queries.
6. **Dedupe on purpose.** State the rule for choosing the row to keep.
7. **Nulls.** Decide how each null is treated. Write it down. Never drop rows silently.
8. **Dates.** One time zone. Half-open ranges (`>= start` and `< end`).
9. **Minimum code.** Touch only what you must. Reuse the step you already have.

## Step 3: use the tool file

Read only the file for the tool in use.

- SQL: `sql.md`
- Python (pandas or polars): `python.md`
- Excel: `excel.md`
- Power BI: `powerbi.md`
- Tableau: `tableau.md`

Excel, Power BI and Tableau always run in hand-over mode. Give steps, the user does them and pastes the result. Apply the `run-or-hand-over` skill.

## After building

Climb the validation ladder with the `validation-ladder` skill. The spec's expected row count is part of rung 4.

## Style

The Conventions section of the data map wins over these defaults. If the data map is absent, use the defaults in the tool file.
