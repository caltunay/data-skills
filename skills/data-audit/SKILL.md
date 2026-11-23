---
name: data-audit
description: Audit a table, file or extract before an analysis in the data-skills flow relies on it: shape, missing values, duplicates, outliers, date coverage and a check against a trusted number, with every cleaning choice written down. Applies when /run-analysis first touches a source, or when the user asks for a data audit by name.
---

# Data audit

Know the data before you trust it. Audit first, analyse second.

## Core rule

Inventory the source, check its shape, nulls, duplicates, outliers and dates, and validate against a trusted number. Write down every cleaning choice. Never clean silently.

## Checklist

1. **Source inventory.** Where did it come from? Who owns it? When was it last refreshed? Which query or export produced it? Check the data map for the table.
2. **Shape and n.** Rows, columns. Does the row count match what the analysis table spec expected?
3. **Look at rows.** Top and bottom rows, and a random few. Check they make sense by eye.
4. **Types.** Dates stored as text, numbers stored as text, IDs stored as numbers that lose leading zeros.
5. **Missingness.** Nulls per column. Are they random or patterned (all missing for one segment, one week)? Are empty strings, zeros or 9999 standing in for null?
6. **Cardinality.** Distinct count per column. Is the key unique? Does a low-cardinality column have unexpected values?
7. **Duplicates.** On the key, and on the whole row. Decide the rule for which to keep.
8. **Outliers.** Min, max, percentiles. Negative amounts, future dates, impossible values. Check before removing. An outlier can be the story.
9. **Date coverage.** First and last date, gaps, partial first or last periods, late-arriving data. Time zone. Plot or list the daily series across the full window: a zero day or a gap is often a logging break, not a real change.
10. **Distribution.** Counts by category, a histogram for numbers. Look for spikes and cliffs.
11. **External validation.** Compare a total with a trusted number from the data map or the stakeholder. State the tolerance. Explain gaps above it.

## Output

A short table: check, what you found, what you did about it.

| check | finding | action |
|---|---|---|
| duplicates on order_id | 214 of 120,400 rows | kept the latest row by updated_ts (assumption A3) |

## Cleaning rules

- Write every cleaning choice down: what, how many rows affected, why.
- If a choice could change the headline, record it as an assumption (apply the `assumptions` skill).
- Keep the raw data untouched. Clean in a named step.
- Never drop outliers only because they are inconvenient.
- If something is odd and you cannot explain it, ask the user. Do not guess.

## Running the checks

Give small, numbered check queries with the expected result stated first. Apply the `run-or-hand-over` skill when the user must run them. In hand-over mode, batch them into numbered groups so the user pastes once per group, not once per query. Apply the `validation-ladder` skill for the order of checks on a built table.

## Floor at every depth

The data-check floor from the `validation-ladder` skill runs at every depth, quick included. Its first check is this audit in short form, for each table used: row count; distinct keys against rows (duplicates); null rate of every column used; min and max dates (coverage, future dates); distinct values of every category column used (flag unexpected labels). Then: one real entity across tables, one day for all entities, the daily series across the full window (gaps, spikes, zero days), join checks, category totals against the overall total, a check for every testable assumption, and the reconcile. State the expected result first for each.

## Depth

- Quick: the compact floor (one small query per check, results in one table). Never skipped.
- Standard: the full checklist above plus the floor.
- Deep: the full checklist and the floor, plus a second extract or source to cross-check.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
