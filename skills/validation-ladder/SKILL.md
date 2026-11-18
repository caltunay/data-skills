---
name: validation-ladder
description: Climb the data-skills validation ladder (one entity, one entity-day, many entities, aggregates, reconcile to a trusted number) and log each rung, on top of the data-check floor that runs at every depth. Applies inside the data-skills flow when /run-analysis builds an analysis table or /review-analysis checks a ladder log, or when the user asks to validate a result with the ladder. Not for writing a one-off query.
---

# Validation ladder

Never jump straight to the final query. Check the data first, then climb the ladder one rung at a time.

## Core rule

Run the data-check floor at every depth, quick included. Then climb: one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each check. Record the actual result and pass or fail after it. Every check compares against an independent path (raw rows or a separate query), never against the frame the result was built from.

## Data-check floor (every depth)

Quick depth gets a compact version (one small query per check, results in one table). It never skips the floor. State the expected result first for each check.

1. **Table audit,** for each table used:
   - row count
   - distinct keys against rows (duplicates)
   - null rate of every column used
   - min and max dates (coverage, future dates)
   - distinct values of every category column used (flag unexpected labels)
2. **One real entity across tables.** Pick a specific id. Show its rows in every table used. Check the values make sense together (for example, sign-up before first order).
3. **One day, all entities.** The total for one day. Is it in a plausible range?
4. **Daily series across the full window.** Look for gaps, spikes and zero days. For any "X dropped" question this check is mandatory and runs before any segment scan, because a logging break is the most common cause of a drop.
5. **Join checks.** Row counts before and after each join, key match rate (orphans), fan-out.
6. **Category totals sum to the overall total.** A gap means nulls, unexpected labels or double counting.
7. **Assumption checks.** Every assumption a query can test gets one. Example: an hour-of-day distribution for a time zone assumption.
8. **Reconcile to the trusted number.** Say which count must match (raw or cleaned) and why. State the tolerance first.

## Ladder rungs (on the built analysis table)

1. **One entity.** Follow one customer, order or account end to end. Check every column by hand against its raw rows.
2. **One entity-day.** Recompute that entity's value for one day or period straight from the raw rows. Compare with the analysis table row. Check the time logic, time zones and cut-offs.
3. **Many entities.** A sample of 10 to 100 entities. Recompute each from the raw source with a separate query. Compare row by row. Check duplicates, nulls and join fan-out. Count rows before and after every join.
4. **Aggregates.** Compute the headline totals a second way, straight from the source tables, without the analysis table. Compare with the analysis table totals. Check distributions and edge periods (first and last day, partial periods, holidays).
5. **Reconcile.** Compare to a trusted number from the data map or the stakeholder. Same rule as floor check 8.

A rung that compares the analysis table with the frame or query it was built from tests only the aggregation, not the data. That is not a pass. Use an independent path.

## Per check

- **Expected:** write what you expect before you look. Example: "Order 1042 has 3 items, total 57.40."
- **Actual:** the real result.
- **Pass or fail:** a mismatch is a finding, not noise. Find the cause before moving up.

Log the floor and each rung in `analysis.md` under Results, in the ladder log table. In chat, print the same table.

## Depth

- Quick: the compact floor. Floor checks 2, 3 and 8 stand in for rungs 1, 2 and 5.
- Standard: the full floor, then all five rungs.
- Deep: the full floor, all five rungs, plus rebuild the result with one alternative specification (different filter, join path or definition) and compare.

## Hand-over mode: batch the checks

When the user runs the queries, batch them into numbered groups, so the user pastes once per group, not once per query. Example: group G1 holds the table audit (Q1.1 to Q1.5), group G2 holds the entity, day and daily series checks. Each query in a group keeps its own number, purpose line and expected result. Apply the `run-or-hand-over` skill.

## Pitfalls to check on the way up

- A left join that becomes an inner join through a where filter.
- Fan-out: a one-to-many join that multiplies order-level amounts.
- A denominator that does not match the numerator population.
- Late-arriving data in the last days.
- Time zone shifts that move rows across a day boundary.
- Duplicates in a key that should be unique.
- A zero day or a gap in the daily series that looks like a real drop.

## Small check queries

Keep each check query small. Give each a number (`Q2.1`, `Q2.2`), one purpose line, and the expected result. When the user must run it, apply the `run-or-hand-over` skill.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
