---
name: run-analysis
description: Build the analysis table from the plan, climb the validation ladder, run the method and log results. Use only when the user runs /run-analysis or explicitly asks to run a planned data analysis.
---

# /run-analysis

Build from the spec. Trust nothing until it has climbed the ladder.

## Read first

Read `analysis.md` (Ask, Assumptions, Plan, Analysis table spec) and `DATA-MAP.md`. If the plan or spec is missing, say so and suggest `/plan-analysis`. At quick depth with no file, work from the one-line plan in the chat.

## Rules from the disciplines (in case they do not load)

- `validation-ladder`: one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each rung. Record actual and pass or fail.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Numbered queries (`Q2.1`), one purpose line, expected result first, "Paste the result here."
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
- Chat app: print Results, offer a download.

## Done when

The ladder is complete for the depth, the reconcile passed or its gap is explained, and findings are written with the ceiling applied. Next step: `/review-analysis`.

## Do not

- Do not jump to the final query.
- Do not report a number that failed a rung.
- Do not write causal wording without a causal design.
- Do not clean data silently.
