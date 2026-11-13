---
name: assumptions
description: Record an assumption in the assumptions table when one is about to be made in an analysis, with likely alternatives and impact. Applies whenever a definition, filter, date, population or method choice is not confirmed by the user or the data.
---

# Assumptions

Assume as little as possible. When an assumption is unavoidable, state it, name the likely alternatives, and say what happens if it is wrong.

## Core rule

Write every assumption in the assumptions table. High-impact rows need 1 to 3 likely alternatives.

## Table

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | Refunds are counted on refund date, not booking date | Stakeholder unavailable until Friday | Booking date; payment settlement date | High: shifts monthly totals by about 10% | Ask finance; compare both definitions for one month | open |

- Status is `open`, `confirmed` or `rejected`.
- Ids run A1, A2, A3 and never get reused.
- Alternatives are required for high-impact rows. Optional for low-impact rows.

## Before you add a row

1. Can you ask instead? If yes, ask (apply the `grilling` skill). Only assume when asking is not possible now.
2. Can the data answer it? Run a small check first.
3. Is it already in the data map? Use that entry.

## Impact levels

- High: could change the headline number by about 5% or more, flip a conclusion, or change who is in scope.
- Medium: changes a detail or a segment, not the headline.
- Low: cosmetic or negligible.

## Rules

- Write the assumption in the same turn it is made. Never after.
- Update status when evidence arrives. Keep the row, do not delete it.
- When results are reported, list every high-impact row still `open` next to the findings.
- Depth: quick uses an inline list (one line per assumption). Standard uses the table. Deep uses the table with alternatives for every high-impact row, and a check for each.
