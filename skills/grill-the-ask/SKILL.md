---
name: grill-the-ask
description: Turn a vague stakeholder ask into a clear, scoped question with stated assumptions before any analysis. Use only when the user runs /grill-the-ask or explicitly asks to clarify or grill a data request.
---

# /grill-the-ask

Clarification is the most important part of data work. Ask before you assume.

## Read first

Read `analysis.md` if one exists for this ask (a fresh session must be able to resume without re-asking). Read `DATA-MAP.md` if present. Skip questions they already answer.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and a recommended default. Wait for answers. Never assume silently.
- `assumptions`: write each assumption in the assumptions table. High-impact rows need 1 to 3 likely alternatives.
- `question-types`: six types: descriptive, exploratory, inferential, predictive, causal, mechanistic. Each has a claim ceiling. No "caused" without a randomised experiment or a credible causal design.
- `data-map`: read `DATA-MAP.md` before writing queries. Flag entries older than 90 days or contradicted by data, then ask.

## Steps

1. Take the ask verbatim. Store it unchanged.
2. Run rounds of questions covering: goal, the decision it feeds, question type, metric, population, time window, constraints, deadline.
3. Propose the question type with its ceiling. Confirm it with the user.
4. Choose the depth and propose it: **quick**, **standard** or **deep**. The user can override.
   - Quick: a small, low-risk ask, one number or one chart.
   - Standard: the usual ask.
   - Deep: high stakes, a decision with real cost, or a test readout.
5. Write down every assumption you have to make.
6. Restate the clarified question in one or two sentences. Ask the user to confirm it.

## Depth table

| | Quick | Standard | Deep |
|---|---|---|---|
| Grill | 1 round, max 3 questions | Rounds until clear | Rounds until clear, plus stakeholder prep questions |
| Assumptions | Inline list | Table | Table, alternatives for every high-impact row |
| Files | None | `analysis.md` | Full analysis folder |

Stakeholder prep questions (deep): who else will read this, what will they push back on, what would change their mind, what is the cost of a wrong answer.

## Output

- **Quick:** no files. Print the clarified question, depth and an inline assumption list. Suggest `/plan-analysis`, or just do the work if the path is obvious.
- **Standard and deep:** create `data-work/analyses/<yyyy-mm-dd>-<slug>/analysis.md` from `analysis.template.md` (in this skill's folder). Fill Meta, Ask and Assumptions. Set status to `grilling`. Create `queries/` and `outputs/` for deep.
- **No file access:** print the filled sections in one block and offer them as a download.

Apply `run-or-hand-over` for saving.

## Done when

The clarified question, question type, depth and assumptions are written, and the user confirmed them. Then name the next step: `/plan-analysis`.

## Do not

- Do not start any analysis or query.
- Do not ask more than 3 questions per round.
- Do not ask a question the data map or the user already answered.
- If the ask is already clear, say "No questions needed", write it up and move on. Do not invent questions.
