---
name: assumptions
description: Record an assumption in the assumptions table of analysis.md, with likely alternatives, impact and a way to check it. Applies inside the data-skills flow when a definition, filter, date, population or method choice in an analysis is not confirmed by the user or the data.
---

# Assumptions

Assume as little as possible. When an assumption is unavoidable, state it, name the likely alternatives, and say what happens if it is wrong.

## Core rule

Write every assumption in the assumptions table. High-impact rows need 1 to 3 likely alternatives.

## Table

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | Orders are counted on order date, not dispatch date | Stakeholder unavailable until Friday | Dispatch date; payment date | High: shifts monthly totals by about 10% | Ask finance; compare both definitions for one month | open |

- Status is `open`, `confirmed` or `rejected`.
- Ids run A1, A2, A3 and never get reused.
- Alternatives are required for high-impact rows. Optional for low-impact rows: write "n/a".
- Standard and deep depth always show all 7 columns: id, assumption, why unavoidable, likely alternatives (1-3), impact if wrong, how to check, status. Never drop, merge or rename a column. An empty cell gets "n/a".
- Only quick depth uses an inline list.

## Before you add a row

1. Can you ask instead? If yes, ask (apply the `grilling` skill). Only assume when asking is not possible now.
2. Can the data answer it? Run a small check first.
3. Is it already in the data map? Use that entry.

## What belongs in the table

- Only real assumptions: a definition, filter, date, population or method choice that could be wrong and that the work depends on.
- Claim rules are not assumptions. "Spend is a hypothesis, not a cause" or "this cannot show why" go in the claim ceiling (Meta in `analysis.md`), not in the table.
- Known facts are not assumptions. If the data or the user confirmed it, it is a fact or a rule.

## Impact levels

Rate by the size of the effect on the headline, not by how comfortable the assumption feels.

- High: could change the headline number by about 5% or more, flip a conclusion, or change who is in scope.
- Medium: changes a detail or a segment, not the headline.
- Low: cosmetic or negligible.

Example: comparing a 31-day month with a 28-day month moves a monthly total by about 10%. That is High by the rule above, and never lower than Medium.

## Rules

- Write the assumption in the same turn it is made. Never after.
- Update status when evidence arrives. Keep the row, do not delete it.
- When results are reported, list every high-impact row still `open` next to the findings.
- Depth: quick uses an inline list (one line per assumption). Standard uses the full 7-column table. Deep uses the full 7-column table with alternatives for every high-impact row, and a check for each.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
