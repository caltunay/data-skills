---
name: run-analysis
description: Build the analysis table from the plan, climb the validation ladder, run the method and log results. Use only when the user runs /run-analysis or explicitly asks to run a planned data analysis.
---

# /run-analysis

Build from the spec. Trust nothing until it has climbed the ladder.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Wait for the choice. Do not offer it again if the user already chose B for this analysis.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. Quick depth has no file: work from the one-line plan in the chat. If the plan or the spec is missing, say so and suggest `/plan-analysis`.
4. Read the Progress line in Meta and resume from it. Do not redo rungs the ladder log shows as passed. Then read Ask, Assumptions, Plan and Analysis table spec.

## Rules from the disciplines (in case they do not load)

- `validation-ladder`: one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each rung. Record actual and pass or fail.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Numbered queries (`Q2.1`), one purpose line, expected result first, "Paste the result here." Never call a data tool before the user names the source.
- `shaping-data`: grain first. Count rows before and after every join. Apply filters from the data map. Named steps.
- `data-audit`: check shape, nulls, duplicates, outliers, date coverage, and validate against a trusted number. Write cleaning choices down.
- `stats-tests`: choose the test by data type and design. Report direction, magnitude and uncertainty. Correct for multiple comparisons.
- `question-types`: word every claim at or below the ceiling. Descriptive and experiment method notes live in that skill.
- `data-map`: read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask.
- `assumptions`: ask instead of assuming. When you must assume, add a row.

## Steps

1. **Audit** each new table or extract (apply `data-audit`).
2. **Build** the analysis table from the spec, using the tool file in `shaping-data` for the tool in use. Save queries as numbered files in `queries/` (`q1-1-one-entity.sql`, `q1-2-one-entity-day.sql`, and so on).
3. **Climb the ladder.** Before each rung, write the expected result. Run the check. Write the actual and pass or fail. A fail means find the cause before going up.
4. **Run the method** for the question type. Load the method notes from `question-types`.
5. **Reconcile** to the trusted number from the plan. Explain any gap above the stated tolerance.
6. **Write findings.** Each finding gets direction, magnitude, uncertainty, and the claim ceiling applied.
7. **Update assumptions.** Set status as evidence arrives. List high-impact rows still `open` beside the findings.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Ladder | One entity check plus reconcile | Full ladder | Full ladder plus alternative specification |
| Files | None | `analysis.md` | Full analysis folder |

Deep: rebuild the result with one different specification (another filter, join path or definition) and compare. A gap means a fragile result. Report it.

## Ask, do not assume

If a definition, filter, date or population is unclear, ask (a round of at most 3 questions). If you cannot ask now, add an assumption row and carry on.

## When the plan cannot hold

Examples: no clean control group, a metric that is not available, a sample ratio mismatch, a source that does not reconcile. Do not push on. Add a dated row to the Plan revisions log in `analysis.md`: what changed and why. If the change lowers the question type, say what claim is no longer allowed. Then continue from the right step (usually the plan).

## Data safety

Show aggregates by default. Ask before saving row-level data anywhere. Put charts and tables in `outputs/` only when asked. Never store credentials.

## Output

- Standard and deep: update Results in `analysis.md` (ladder log, findings). Set status `running`, then `reviewed` is set by the review step.
- Quick: print the answer, the one check and its result, the ceiling, and open assumptions. No file.
- Chat app: see End.

## End (every flow step)

1. Update the Progress line in `analysis.md` Meta.
2. Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app, even if you can write files in a sandbox.
3. Chat app: offer the updated `analysis.md` and `readout.md` as a download. If you cannot, print it as one block. Say: "Save this to your Project files so the next step, in any chat, can read it."
4. Coding agent: the files are already saved under `data-work/`. Say where.
5. Name the next step: `/review-analysis`.

## Done when

The ladder is complete for the depth, the reconcile passed or its gap is explained, and findings are written with the ceiling applied. Next step: `/review-analysis`.

## Do not

- Do not jump to the final query.
- Do not report a number that failed a rung.
- Do not write causal wording without a causal design.
- Do not clean data silently.
