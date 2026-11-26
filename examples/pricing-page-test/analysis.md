format: v1
updated: 2026-02-24 09:00

# Analysis: did the new pricing page increase orders?

Invented example. Every number below comes from `outputs/results.txt` and `outputs/stats.txt`, produced by running the files in `scripts/` and `stats.py`.

## Where it stands

- Status: retro done
- Answer so far: The new page raised 7-day paid conversion from 10.2% to 11.8% (95% interval +0.2 to +3.1 points). Week 2 was weaker.
- Open risks: Week 2 was weaker; revenue per visitor not clearly up.
- Next step: Roll out to 95% and hold 5% for four weeks.
- How to resume: Open `data-work/analyses/2026-02-25-pricing-page-test/`; the work is complete, start the next ask with `/grill-the-ask`.

## 1. Meta

- Title: Pricing page test, February 2026
- Requester: Product manager, shop checkout
- Audience: product
- Date: 2026-02-24 (plan written 2026-01-27, before the test)
- Depth: deep
- Question type: causal (randomised experiment)
- Status: retro done
- Progress: retro done, 5 data map changes accepted. Readout final.
- Setup choice: A (ran `/setup-data-work`)
- Goal link: target, lift order conversion on the shop
- Files: download

## 2. Ask

- Original ask (verbatim): "We are testing a new layout for the shop's pricing page. Tell us if it works and whether we should ship it."
- Clarified question: Does the new pricing page layout change the share of external visitors who place a paid order within 7 days of first seeing the page, compared with the current layout?
- Decision it feeds: roll out the new layout, or keep the current one.
- Metric, population, time window: conversion within 7 days, per visitor. External visitors to the pricing page. Assignment from 2 to 15 February 2026, orders read after 22 February.
- Constraints: about 530 visitors a day. Two weeks is the longest run the team will accept.
- Deadline: 2026-02-26.

Grilling notes: two rounds. Round 1: what "works" means (one primary metric), the unit of assignment, the smallest effect worth shipping. Round 2: guardrails, who reads it, and what happens if the result is flat. Depth proposed: "deep, because it is a test readout that decides a rollout". Stakeholder prep: finance will ask about revenue, so revenue per visitor is a guardrail.

## 3. Assumptions

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | Assignment is random and 50/50 by visitor | Taken from the platform's setup page | Assignment by session; an uneven split | High: breaks the test | Sample ratio check (Q2.1); `visitor_id` unique in assignments (Q1.3) | confirmed |
| A2 | One visitor cannot affect another | Cannot be seen in the data | Shared discount codes; stock running out for one arm | High: biases the effect | Asked the requester: no codes on the page, no stock limits in the period | confirmed |
| A3 | A 7-day window captures the orders the page influences | Agreed with the requester before the test | 14 days; same session only | Medium: changes the size, not the sign | Could be re-run with 14 days once the data exists | confirmed |
| A4 | The baseline conversion is about 10% | Needed for the sample size | 8%; 12% | Medium: changes the sample needed | Control arm result: 10.15% | confirmed |
| A5 | No sale, holiday or release hit one arm more than the other | Cannot be seen in the data | n/a | Medium | Asked the requester: none in the period. Random assignment protects against it | confirmed |

Status: open, confirmed or rejected. Alternatives are required for high-impact rows only. Always keep all 7 columns.

## 4. Plan

Written on 2026-01-27, before the test started.

### Options considered

| option | method | trade-offs | verdict |
|---|---|---|---|
| 1 | Randomised experiment, 50/50 by visitor, fixed horizon (card: randomised experiment) | Supports a causal claim. Needs two weeks of traffic | Chosen |
| 2 | Ship to everyone and compare before with after (card: interrupted time series) | No wait. Weak: no comparison group, and February differs from January | Rejected: a randomised test is possible, and it is the first step of the causal method selector |
| 3 | Sequential test with early stopping | Could end sooner | Rejected: the simplest version answers the question in the time available |

### Chosen plan

Method card: randomised experiment (A/B).

- Unit of randomisation and of analysis: visitor.
- Primary metric: share of visitors with a paid order within 7 days of assignment. One primary metric.
- Guardrails: revenue per visitor must not be clearly lower. Return rate per paid order must not be clearly higher. "Clearly" means the whole 95% interval is on the bad side.
- Power: baseline 10%, smallest effect worth shipping (MDE) 2.0 points, alpha 5%, power 80%. Sample: 16 x 0.10 x 0.90 / 0.02^2 = 3,600 visitors per arm.
- Runtime: 14 days, 2 to 15 February 2026, two full weekly cycles. Expected traffic: about 7,400 visitors. No look at results before 23 February.
- Test: two-proportion z-test, 95% interval for the difference.
- Segments: none planned. Any slice is exploratory.

### Success checks

- Visitor counts per arm within 0.5% of the experiment platform's counts.
- `visitor_id` unique in the analysis table.
- From the method card: no sample ratio mismatch (p above 0.001); design held; no peeking; at least 3,600 visitors per arm; analysis per visitor; full weekly cycles; one primary metric; guardrails not clearly worse; effect by week looked at; no overlap with an event that hit one arm.

### Plan revisions

| date | what changed | why |
|---|---|---|
| | none | The plan held |

## 5. Analysis table spec

- Grain (one row means): one external visitor.
- Keys: `visitor_id`.
- Measures: converted (0 or 1), paid orders in window, revenue in window, returned orders in window.
- Dimensions: arm, device, test week.
- Time column and window: `assigned_ts`, UTC, 2026-02-02 to 2026-02-15. Orders from `assigned_ts` up to, but not including, 7 days later.
- Filters and exclusions (from the data map): `is_internal = 0`; `status = 'paid'`.
- Joins: orders are aggregated to the visitor before the join. The raw join is a fan-out trap.
- Tidy (long) or wide, and why: one row per visitor, so every rate is a mean over visitors, the unit of randomisation.
- Context columns needed to interpret results: assigned date.
- Expected row count or range: about 7,300 (about 7,400 visitors less about 1.5% internal).

## 6. Results

### Ladder log

| rung | expected | actual | pass or fail |
|---|---|---|---|
| 0 audit (Q0.1, Q0.2) | About 7,400 assignment rows, one per visitor, two arms. `order_id` unique, no negative amounts | 7,506 rows, 7,506 visitors, 2 arms, 109 internal. 1,128 orders, all unique: 1,049 paid, 79 cancelled, amounts 8.04 to 167.18 | pass |
| 1 one entity (Q1.1) | Visitor 500060: variant, mobile, assigned 2 Feb 09:19:51, two paid orders of 34.09 and 42.47 inside 7 days | As expected, at 0.89 and 2.18 days | pass |
| 2 one entity-day (Q1.2) | An order at 6.85 days counts. An order at 7.23 days does not | 502836: inside. 504088: outside | pass |
| 3 many entities (Q1.3, Q1.3b, Q1.3c) | `visitor_id` unique. A raw join to orders returns more rows than ordering visitors. The view has one row per external visitor | 7,506 unique. Join gives 1,128 rows for 961 visitors (166 have more than one order). View: 7,397 rows, 7,397 visitors. The three visitors followed by hand come out right | pass |
| 4 aggregates (Q1.4) | 14 days in both arms, no empty day | control 3,675, variant 3,722, 14 days each, 2 to 15 Feb | pass |
| 5 reconcile (Q1.5) | Visitor counts per arm within 0.5% of the platform | control 3,727 and variant 3,779 on both sides. Gap 0 | pass |
| Alternative specification (deep) | Counting any paid order with no 7-day limit should give the same sign | Not run: see Review, optional check 1 | not run |

### Method checks

Method card used: randomised experiment (A/B). Each item under "Checks that must pass".

| check | pass or fail | note |
|---|---|---|
| 1 Sample ratio mismatch | pass | 3,675 against 3,722, planned 50/50. Chi-square 0.299, p = 0.585 |
| 2 Design held | pass | Primary metric, sample size and run length as written on 27 January |
| 3 No peeking | pass | Ran the full 14 days. Results first read on 24 February |
| 4 Power | pass | 3,675 and 3,722 per arm against 3,600 planned. Detectable effect at this size: 1.96 points |
| 5 Unit of analysis equals unit of randomisation | pass | Both are the visitor |
| 6 Full weekly cycles | pass | Two, Monday 2 to Sunday 15 February |
| 7 Multiple comparisons | pass | One primary metric. Two guardrails, named in advance. The device slice is labelled exploratory |
| 8 Guardrails | pass | Revenue per visitor +0.70 (95% interval -0.14 to +1.54): not clearly lower. Return rate -1.00 points (-4.46 to +2.45): not clearly higher |
| 9 Novelty and primacy | pass, with a caveat | Week 1 +2.67 points, week 2 +0.59. Same sign. The weeks do not differ clearly (p = 0.152), but the drop is reported |
| 10 No overlap with an event | pass | None in the period (A5) |

### Findings

Each finding: direction, magnitude, uncertainty, claim ceiling applied.

1. **The new page increased conversion.** Control 10.15% (373 of 3,675), variant 11.79% (439 of 3,722). Difference +1.65 points, 95% interval +0.22 to +3.07, p = 0.024. Relative lift +16.2%. Ceiling: causal, for external visitors to the pricing page, 2 to 15 February, orders within 7 days.
2. **The size is uncertain, and below the planned 2.0 points at its centre.** The interval includes 2.0 and also includes effects too small to matter. Ceiling: same.
3. **The effect was smaller in week 2.** +2.67 points (0.63 to 4.71) then +0.59 (-1.39 to 2.58). The difference between weeks is -2.08 points, p = 0.152. Two weeks cannot tell chance from a fading effect. Ceiling: descriptive for the weekly numbers. No claim about novelty.
4. **Guardrails held.** Revenue per visitor 5.17 to 5.87 (+0.70, interval -0.14 to +1.54). Return rate 8.64% to 7.64%. Neither is clearly worse. A revenue gain is not shown. Ceiling: causal, with intervals that include zero.
5. **Exploratory: the gain appears on mobile only.** Mobile +2.79 points (0.93 to 4.64), desktop -0.03 (-2.26 to 2.20). Found after slicing, one slice looked at. Ceiling: exploratory, a pattern worth testing.
6. **Context: average order value was lower in the variant.** 40.68 against 43.15. Not a planned measure, not tested.

Open high-impact assumptions next to these findings: none.

## 7. Review

- Verdict: ready with caveats.
- Technical issues: no material issues. Optional checks: (1) the alternative specification from the deep ladder was not run: repeat with no 7-day limit and with a 14-day window; (2) bootstrap the revenue per visitor interval, since order values are skewed; (3) confirm with the platform owner that no visitor changed arm.
- Business issues: the effect's centre is under the 2.0 points the team called worth shipping. Shipping is still reasonable: the change costs little, the guardrails held, and the interval is all above zero. The readout says so plainly and does not promise revenue.
- Leadership questions, with answers:
  1. "Does it work?" Yes, in this test: +1.65 points, with a 95% interval of +0.22 to +3.07.
  2. "How much revenue is that?" Not supported yet. Revenue per visitor leaned up (+0.70) but the interval includes zero.
  3. "Will it last?" Not known. Week 2 was weaker than week 1. A 5% holdout for four weeks will show it.
  4. "Should we ship to mobile only?" No. That pattern was found by slicing. Test it if it matters.
  5. "Could the test be broken?" The checks that catch a broken test passed: the split, the visitor counts against the platform, and the fixed design.
- Readout: every sentence changed, as a "was" and "now" pair, and why. Readout status: FINAL
  - v0.3 re-review: was "Checks passed: ..., validation ladder, ..." now "Checks passed: ..., ladder rungs 1 to 5 as logged in `analysis.md`, ... The deep-depth alternative specification was not run." Why: the Method line claimed a full ladder at deep depth, but one deep check did not run.
  - v0.3 re-review: was a key numbers table with 8 rows. now: 5 rows, the week and return-rate rows in the Appendix. Why: at most 5 key numbers.
  - was: "The new page lifts conversion by 16%." now: "+1.65 points (+16% relative)", with its interval. Why: a relative lift alone hides the size and the uncertainty.
  - was: "The new page works best on mobile." now: "The gain appeared on mobile (+2.8 points) and not on desktop (0.0). This was found by slicing after the test, so it is a pattern to test, not a result." Why: a slice is exploratory.
  - was: "It also raises revenue per visitor by 0.70." now: "Revenue per visitor leaned up, but the test cannot confirm a revenue gain." Why: the interval includes zero.

## 8. Retro

| proposed data map change | accepted (yes or no) |
|---|---|
| Joins: assignments to orders is a fan-out trap (166 of 961 ordering visitors have more than one order) | yes |
| Gotchas: build one row per visitor before joining orders | yes |
| Gotchas: do not read a test before the last 7-day window has closed | yes |
| Rules: analyse a test at the unit it was randomised on | yes |
| Metrics: trusted visitor counts per arm from the experiment platform | yes |
| Metrics: "the new page lifts conversion by 1.65 points" as a trusted number | no: a test result with a wide interval is not a reference value |

## 9. Decisions

### Round 1 (2026-01-20)

| # | question | user's answer (verbatim) |
|---|---|---|
| 1 | What does "works" mean? | "More visitors place a paid order within 7 days." |
| 2 | What is the unit of assignment? | "The visitor." |
| 3 | What is the smallest effect worth shipping? | "Two points of conversion." |

### Round 2 (2026-01-20)

| # | question | user's answer (verbatim) |
|---|---|---|
| 1 | Which guardrails? | "Revenue per visitor and return rate." |
| 2 | Who reads the result? | "The product team." |

## 10. Hypotheses

| id | hypothesis | would support it | would refute it | leads to | status |
|---|---|---|---|---|---|
| H1 | The new layout raises 7-day conversion | Variant conversion above control, interval above zero | Interval includes zero or below | H1.1 | supported (+1.65 points, interval +0.22 to +3.07) |
| H1.1 | The difference has the same sign in both weeks | Both weekly differences have the same sign as the overall difference | A weekly difference has the opposite sign or is zero | none | supported (week 1 +2.67, week 2 +0.59: same sign. Week 2 interval includes zero, so the size in week 2 is not settled) |
| H2 | The gain appears on mobile only | Mobile difference above zero, desktop near zero | Both devices move together | none | parked (one exploratory slice, a pattern to test) |

## 11. Appendix: Review pack

The code behind each headline number. Every query file is in `scripts/`; results are in `outputs/results.txt` and `outputs/stats.txt`.

### Conversion by arm (control 10.15%, variant 11.79%)

- Source: `visitor_outcomes`, one row per external visitor, built by `q1-3b-outcomes-view.sql` from `assignments` and `orders`, 2 to 15 February 2026.
- Code: `q2-2-primary-metric.sql`

```sql
select
    arm
  , count(*)                                   as visitors
  , sum(converted)                             as converters
  , round(sum(converted) * 100.0 / count(*), 2) as conversion_pct
from
    visitor_outcomes
where true
group by 1
order by 1
;
```

### Effect (+1.65 points, 95% interval +0.22 to +3.07) and split (p = 0.59)

- Source: the counts above and `q2-1-srm-counts.sql`.
- Code: `stats.py` (two-proportion test, normal approximation, standard library only).

### Revenue per visitor (5.17 to 5.87)

- Source: `visitor_outcomes`.
- Code: `q2-4-guardrails.sql`, interval in `stats.py`.
