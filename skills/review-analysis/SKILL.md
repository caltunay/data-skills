---
name: review-analysis
description: Review a finished analysis, yours or anyone's, for technical soundness, business fit and claim wording, and give a verdict. Use only when the user runs /review-analysis or explicitly asks for a review of an analysis.
---

# /review-analysis

Be a sceptical colleague. Critique the work, never the person. Say "no material issues" when that is true.

## Read first

Read `analysis.md`, or the analysis pasted into the chat. If there is no ladder log or spec, review the claim and the method anyway and note what is missing.

## Rules from the disciplines (in case they do not load)

- `question-types`: name the type. Every claim is checked against its ceiling. No "caused" without a randomised experiment or a credible causal design that passed its checks.
- `assumptions`: flag any high-impact row still `open` when results are reported. Alternatives are required for high-impact rows.
- `validation-ladder`: check the ladder log. Each rung has an expected result, an actual result and pass or fail. Reconcile to a trusted number.

## Steps

1. **State the claim** in one sentence: what is said to be true, and what should be done about it.
2. **Name the question type** and its ceiling.
3. **Technical review.** Ask each item only if the analysis gives a reason.
   - Grain: what is one row after each join? Can a join fan out and double count?
   - Join type: does a left join become an inner join through a where filter?
   - Denominator: who is in it? Does it match the numerator population?
   - Filters and windows: same dates, time zone and status filters on both sides of a comparison?
   - Dedup: unique ids, test or internal users, bots, refunds, cancelled rows.
   - Definitions: same metric definition in both periods or arms?
   - Nulls: how treated? Do they drop rows silently?
   - Sample: size, selection, survivorship, who is missing.
   - Stats: is there an interval or test? Is the number practically big, not only significant?
   - Spec match: do the results match the analysis table spec (grain, filters, row count)?
   - Ladder: was each rung run and logged? Can one number be recomputed independently?
   - Method notes: apply the branch notes in `question-types` (descriptive or experiment: SRM, power, peeking, novelty, mix shift).
4. **Business review.** Ask what leadership will ask.
   - Decision: what will be done differently because of this? If nothing, why was it run?
   - Size: the effect in money, users or orders per month. Big enough to act on?
   - Baseline: compared with what, and is that right?
   - Cause: does the story fit the numbers, or was it added afterwards?
   - Segments: who gains and who loses? Does a total hide a bad segment?
   - Cost and risk: what does acting cost, and what if the finding is wrong?
   - Durability: lasting, or a launch spike or seasonal blip?
   - Next step: what one extra check would change the decision?
   - Scope: does the recommendation cover only what was measured (population, period, metric, place)?
   - Ask match: does the headline answer the question that was asked, or a nearby easier one?
5. **Claims check.** Quote every sentence whose wording is above the ceiling, and give the allowed wording.
6. **Assumptions check.** List high-impact rows still `open`.
7. **Leadership questions.** Write the 3 to 5 questions a sceptical leader will ask, with the best answer the analysis supports. Mark an answer "not supported yet" when it is.
8. **Verdict:** `ready`, `ready with caveats`, or `needs rework`, with reasons.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Review | Self-check against the claim ceiling | Technical plus business review | Full review plus leadership questions |

Quick: run steps 1, 2 and 5 only, in a few lines.

## Output format (scan-first)

1. One verdict line.
2. Claim (1 line) and ceiling (1 line).
3. Issues, most important first, as many as earned, up to 8. Fewer is fine. Each issue:

   **N. Short title** `[MUST]` (only if the decision changes when it is answered)
   - Claim it hits: the exact statement or number.
   - Why it matters: one line, with the size if computable from the numbers given.
   - Check: the exact query, split or calculation to run.

4. Leadership questions with answers.

## Precision

- Only raise an issue if the analysis shows a reason. A sound step is not an issue.
- If the analysis is sound, say "No material issues" and give at most 3 optional checks, labelled optional. Do not invent must-answers.
- Do not criticise wording that already matches the evidence.
- No praise. No generic checklist.
- Never do arithmetic in your head. Compute it, and show the numbers.

## Writing

Standard and deep: write the Review section of `analysis.md` and set status `reviewed`. Chat app: print it and offer a download. Apply `run-or-hand-over`.

## Plan revisions

If the review finds the plan cannot hold (for example, an experiment with no clean control), add a dated row to the Plan revisions log, say what changed and why, and name the step to resume from. No restart.

## Done when

A verdict is given. Next step: `/retro-analysis`.
