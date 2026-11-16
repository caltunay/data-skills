---
name: validation-ladder
description: Climb the data-skills validation ladder (one entity, one entity-day, many entities, aggregates, reconcile to a trusted number) and log each rung. Applies inside the data-skills flow when /run-analysis builds an analysis table or /review-analysis checks a ladder log, or when the user asks to validate a result with the ladder. Not for writing a one-off query.
---

# Validation ladder

Never jump straight to the final query. Climb the ladder one rung at a time.

## Core rule

One entity, then one entity-day, then many entities, then aggregates, then reconcile to a trusted number. State the expected result before each rung. Record the actual result and pass or fail after it.

## Rungs

1. **One entity.** Follow one customer, order or account end to end. Check every column by hand.
2. **One entity-day.** One entity over one day or period. Check the time logic, time zones and cut-offs.
3. **Many entities.** A small sample, 10 to 100 entities. Check duplicates, nulls, and join fan-out. Count rows before and after every join.
4. **Aggregates.** The full query. Check totals, distributions, and edge periods (first and last day, partial periods, holidays).
5. **Reconcile.** Compare to a trusted number from the data map or the stakeholder. State the tolerance first. Explain any gap above it.

## Per rung

- **Expected:** write what you expect before you look. Example: "Order 1042 has 3 items, total 57.40."
- **Actual:** the real result.
- **Pass or fail:** a mismatch is a finding, not noise. Find the cause before moving up.

Log each rung in `analysis.md` under Results, in the ladder log table. In chat, print the same table.

## Depth

- Quick: rung 1 and rung 5 only.
- Standard: all five rungs.
- Deep: all five rungs, plus rebuild the result with one alternative specification (different filter, join path or definition) and compare.

## Pitfalls to check on the way up

- A left join that becomes an inner join through a where filter.
- Fan-out: a one-to-many join that multiplies order-level amounts.
- A denominator that does not match the numerator population.
- Late-arriving data in the last days.
- Time zone shifts that move rows across a day boundary.
- Duplicates in a key that should be unique.

## Small check queries

Keep each check query small. Give each a number (`Q2.1`, `Q2.2`), one purpose line, and the expected result. When the user must run it, apply the `run-or-hand-over` skill.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
