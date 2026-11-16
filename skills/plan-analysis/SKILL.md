---
name: plan-analysis
description: Turn a clarified ask into a chosen plan, an analysis table spec and success checks. Use only when the user runs /plan-analysis or explicitly asks to plan a data analysis.
---

# /plan-analysis

Record decisions already made. Do not invent new ones.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Do not offer it again if the user already chose B for this analysis (the Progress line or the chat shows it).
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. Quick depth has no file: work from the clarified question in the chat. If there is no clarified question at all, say so and suggest `/grill-the-ask`.
4. Read the Progress line in Meta and resume from it. Then read Meta, Ask and Assumptions.

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
- Apply `run-or-hand-over` for saving. Chat app: see End.

## End (every flow step)

1. Update the Progress line in `analysis.md` Meta.
2. Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app, even if you can write files in a sandbox.
3. Chat app: offer the updated `analysis.md` (and `readout.md` when it exists) as a download. If you cannot, print it as one block. Say: "Save this to your Project files so the next step, in any chat, can read it."
4. Coding agent: the files are already saved under `data-work/`. Say where.
5. Name the next step: `/run-analysis`.

## Plan revisions

When a later step finds the plan cannot hold, it adds a dated row to the Plan revisions log: date, what changed, why. This step handles that entry too. No restart.

## Done when

The user has agreed the plan, the spec and the success checks. Next step: `/run-analysis`.

## Do not

- Do not run queries.
- Do not offer options that cannot support the claim the decision needs, unless you say so.
- Do not choose a complex method when a simple one answers the question.
