---
name: plan-analysis
description: Turn a clarified ask into a chosen plan, an analysis table spec and success checks. Use only when the user runs /plan-analysis or explicitly asks to plan a data analysis.
---

# /plan-analysis

Record decisions already made. Do not invent new ones.

## Read first

Read `analysis.md`: Meta, Ask and Assumptions. If it is missing or the ask is unclear, say so and suggest `/grill-the-ask`. Read `DATA-MAP.md` if present.

## Rules from the disciplines (in case they do not load)

- `assumptions`: every new assumption goes in the table. High-impact rows need 1 to 3 likely alternatives.
- `question-types`: name the type and its claim ceiling. Choose a method that can reach the claim the decision needs. If it cannot, say so now. v0 branches: descriptive and experiment.
- `shaping-data`: design the analysis table spec before any query, without reference to a tool. Grain first.
- Easy solution first: try the simplest method that could answer the question.

## Steps

1. Confirm the question type and the decision. State the claim ceiling in one line.
2. List the options (see depth table). For each: method, trade-offs, effort, and the strongest claim it can support.
3. Recommend one. Say why in two lines. Confirm with the user.
4. Write the **chosen plan**: the steps, in order.
5. Write the **analysis table spec**:
   - grain (what one row means)
   - keys
   - measures and dimensions
   - time column and window
   - filters and exclusions (from `DATA-MAP.md`)
   - tidy (long) or wide, and why
   - context columns
   - expected row count or range
6. Set **success checks** up front: what must be true for the result to be trusted. Include the trusted number to reconcile to and the tolerance. Example: "Total paid orders within 1% of 120,400 (finance report)."
7. Add any new assumptions to the table.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Plan | One line: method plus success check | 2 to 4 options, chosen plan | Options, chosen plan, power or MDE where relevant |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Files | None | `analysis.md` | Full analysis folder |

For experiments at deep depth, state the MDE, the power, the runtime and the unit of randomisation.

## Output

- Write Plan and Analysis table spec into `analysis.md`. Set status `planned`.
- Quick: print the one-line plan and success check. No file.
- Chat app: print the sections and offer a download. Apply `run-or-hand-over`.

## Plan revisions

When a later step finds the plan cannot hold, it adds a dated row to the Plan revisions log: date, what changed, why. This step handles that entry too. No restart.

## Done when

The user has agreed the plan, the spec and the success checks. Next step: `/run-analysis`.

## Do not

- Do not run queries.
- Do not offer options that cannot support the claim the decision needs, unless you say so.
- Do not choose a complex method when a simple one answers the question.
