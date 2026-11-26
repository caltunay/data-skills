format: v1
updated: 2026-04-07 09:00

# Analysis: why did sign-ups drop in March?

Invented example. Every number below comes from `outputs/results.txt`, produced by running the files in `scripts/`.

## Where it stands

- Status: retro done
- Answer so far: Sign-ups fell 17% in March (about 25% per day), almost all of it in paid social. The data shows where, not why.
- Open risks: Channel attribution rule unchecked (A4). No data for March last year.
- Next step: Decide on a spend test before the Q2 channel split.
- How to resume: Open `data-work/analyses/2026-04-07-signup-drop/`; the work is complete, start the next ask with `/grill-the-ask`.

## 1. Meta

- Title: Sign-up drop, March 2026
- Requester: Head of growth
- Audience: exec
- Date: 2026-04-07
- Depth: standard
- Question type: descriptive, then exploratory (the "why" is not reachable with this data)
- Status: retro done
- Progress: retro done, 6 data map changes accepted. Readout final.
- Setup choice: A (ran `/setup-data-work`)
- Goal link: target, lift monthly sign-ups
- Files: download

## 2. Ask

- Original ask (verbatim): "Why did sign-ups drop in March?"
- Clarified question: How many sign-ups did the subscription app get in March 2026 compared with February 2026, and where is the fall concentrated?
- Decision it feeds: where the growth team looks first, before the Q2 budget split by channel.
- Metric, population, time window: sign-ups = accounts created, test accounts excluded, counted on `signup_ts` in UTC. February and March 2026, with January for context.
- Constraints: data from `signups`, `daily_spend` and the growth dashboard export only. No data from 2025.
- Deadline: 2026-04-09.

Grilling notes: one round, 3 questions (what counts as a sign-up, which periods to compare, what the answer is for), then one question on audience. Depth proposed: "standard, because it feeds a budget decision but is not a test readout". The requester agreed that "why" starts as "where": a cause needs a design, and none exists here.

## 3. Assumptions

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | A sign-up is an account created, counted on `signup_ts` in UTC | The ask did not define it | First payment date; local time | High: shifts sign-ups between months | Asked the requester | confirmed |
| A2 | For duplicated `signup_id` rows, keep the row with the latest `updated_ts` | The table owner was not reachable | Keep the earliest row; count distinct ids only | Low: only `updated_ts` differs between the rows (Q1.3b), so counts are the same either way | Q1.3b | confirmed |
| A3 | The growth dashboard is the trusted number for monthly sign-ups | Needed for rung 5 | The finance subscriber report | High: no reconcile without it | Asked the requester | confirmed |
| A4 | `channel` on a sign-up is assigned by the same attribution rule in February and March | The rule is not documented and marketing operations did not reply in time | The rule changed in March; a tracking tag broke on paid social | High: would move sign-ups between channels on paper. It cannot change the total | Ask marketing operations whether attribution or tagging changed around 2 March | open |
| A5 | No comparison with March 2025 is possible | The data starts in January 2026 | n/a | Medium: a seasonal pattern cannot be ruled out from history | Load 2025 data when available | open |

Status: open, confirmed or rejected. Alternatives are required for high-impact rows only. Always keep all 7 columns.

## 4. Plan

### Options considered

| option | method | trade-offs | verdict |
|---|---|---|---|
| 1 | Month totals, February against March (card: counts and rates) | Simplest. Misleads: March has 3 more days | Used for the headline only, next to the daily average |
| 2 | Daily averages and full weeks (cards: counts and rates; rolling windows; week-on-week), then a segment scan over dimensions listed in advance (card: segment scan) | Shows size, timing and where. Ceiling: "we see", not "because" | Chosen |
| 3 | Year-on-year comparison (card: week-on-week and year-on-year) | Would show the usual season | Not possible: no 2025 data (A5) |
| 4 | Causal design for "did the spend cut cause it" | Would answer "why" | Not possible: one series, and the causal method selector ends at "none fits" with 8 weeks of history. Offered as a follow-up test |

### Chosen plan

Method cards: counts and rates; week-on-week with like-for-like periods; segment scan.

1. Audit `signups`.
2. Build one row per sign-up, test accounts excluded. Climb the ladder.
3. Headline: February against March, as totals and per day.
4. Weekly series on full weeks, to date the change.
5. Segment scan over 4 dimensions fixed now: channel, platform, country, plan. A second cut to confirm the top pattern.
6. Line up timing with paid spend. Timing is a lead, not a cause.

### Success checks

- Monthly sign-ups within 1% of the growth dashboard (1,171 for February).
- `signup_id` unique in the analysis table.
- Counts are distinct sign-ups, same filters in both months (card: counts and rates).
- Full periods compared with full periods (card: week-on-week).
- Dimensions listed before the scan, contributions sum to 100%, top pattern holds in a second cut (card: segment scan).

### Plan revisions

| date | what changed | why |
|---|---|---|
| 2026-04-07 | Added a dedupe step before counting | Rung 3 failed: 40 `signup_id` values have two rows |
| 2026-04-07 | Headline reports the daily average next to the total | Rung 4 showed 28 against 31 days. The total alone hides a third of the fall |

## 5. Analysis table spec

- Grain (one row means): one sign-up.
- Keys: `signup_id`.
- Measures: count of sign-ups.
- Dimensions: channel, platform, country, plan.
- Time column and window: `signup_ts`, UTC, 2026-01-01 to 2026-03-31. Derived: `signup_date`, `signup_month`.
- Filters and exclusions (from the data map): `is_test = 0`.
- Joins: none for the table. Spend is joined only after sign-ups are aggregated to week.
- Tidy (long) or wide, and why: long, one row per sign-up, so any split is a group-by.
- Context columns needed to interpret results: days in month.
- Expected row count or range: about 3,400 to 3,500 (3,582 raw rows less test accounts).

## 6. Results

### Ladder log

| rung | expected | actual | pass or fail |
|---|---|---|---|
| 0 audit (Q0.1) | About 3,500 rows, 1 Jan to 31 Mar, no null keys | 3,582 rows, 3,542 distinct ids, dates as expected, no nulls, 66 test rows | pass, with a flag: rows exceed distinct ids by 40 |
| F4 daily series (Q0.2, added in v0.3) | 90 days, no zero day, no single-day spike | 90 days, 1 Jan to 31 Mar, lowest day 21, highest 56. No gap or zero day | pass |
| 1 one entity (Q1.1) | Sign-up 101005: one row, paid_search, mobile, monthly, GB, 24 Jan 21:32:27 | As expected | pass |
| 2 one entity-day (Q1.2) | Rows before midnight UTC on 1 March fall in February, later rows in March | 1 row at 22:06 in February, 7 rows from 00:44 in March | pass |
| 3 many entities (Q1.3) | No `signup_id` with more than one row | 40 ids with 2 rows each | **fail** |
| 3 again (Q1.3b, Q1.3c) | After keeping the latest row per id and removing test accounts: rows equal distinct ids | The duplicate rows differ only in `updated_ts`. Clean table: 3,478 rows, 3,478 ids (3,542 less 64 test ids) | pass |
| 4 aggregates (Q1.4) | Three full months, no day without sign-ups, total 3,478 | Jan 1,330 (31 days), Feb 1,175 (28), Mar 973 (31). Sum 3,478 | pass |
| 5 reconcile (Q1.5) | Each month within 1% of the dashboard | Gaps of +4, +4 and +1: 0.30%, 0.34%, 0.10% | pass |

### Method checks

Method cards used: counts and rates; week-on-week with like-for-like periods; segment scan.

| check | pass or fail | note |
|---|---|---|
| Count distinct keys, not rows | pass | Table is one row per `signup_id` after the dedupe |
| Same filters, dates and time zone in both periods | pass | One table, one filter set, UTC |
| Total reconciles to a trusted number | pass | Within 0.34% |
| Full periods compared with full periods | pass | Full calendar months, and full Monday to Sunday weeks. Months differ in length, so the daily average is reported |
| Definition and tracking the same in both periods | not confirmed | A4 is open |
| Both week-on-week and year-on-year shown | fail | No 2025 data (A5). Stated as a caveat |
| Dimensions listed before the scan, and counted | pass | 4 dimensions, 12 segments, fixed in the plan |
| Each segment shows size, change and contribution | pass | Q3.1 to Q3.4 |
| Contributions sum to 100% | pass | In each dimension |
| Mix shift separated from rate change | n/a | The metric is a count, not a rate |
| Top pattern holds in a second cut | pass | Q3.5: paid social fell on mobile (-66%) and on desktop (-58%) |

### Findings

Each finding: direction, magnitude, uncertainty, claim ceiling applied.

1. **Sign-ups fell.** February 1,175, March 973: down 17.2%. Per day: 41.96 to 31.39, down 25.2%. Exact counts for the months. Ceiling: descriptive ("was").
2. **The fall was a step, in the week starting 2 March.** Eight full weeks before it ranged from 266 to 325 sign-ups. The four full weeks from 2 March ranged from 209 to 218. Ceiling: descriptive.
3. **We see the fall concentrated in paid social.** Per day: 15.32 to 5.42, down 64.6%, which is 93.6% of the total fall. The other four channels together: 26.64 to 25.96, down 2.6%. Ceiling: exploratory ("we see", a pattern worth testing). Depends on A4.
4. **Platform, country and plan do not add a second pattern.** Mobile shows 93.8% of the fall, but inside paid social both platforms fell (mobile -65.7%, desktop -58.0%), and mobile in other channels moved -8.8% on about 13 sign-ups a day. Paid social is mostly mobile, which explains the platform view. Countries fell by different amounts (GB -33%, DE -21%, FR -9%); with 4 dimensions scanned this is noted, not claimed. Ceiling: exploratory.
5. **Paid social spend fell in the same week.** About 2,750 to 2,810 a week in February, about 980 to 990 a week from 2 March. Ceiling: descriptive for each series. The match in timing is a lead, not a cause.

Hypotheses to test, cheapest first:
- H1: the spend cut reduced paid social sign-ups. Test: restore spend in some markets, hold it in others, compare (difference-in-differences or a randomised geo test).
- H2: attribution or tagging changed on paid social around 2 March. Test: ask marketing operations (A4). If true, the "lost" sign-ups would show up in another channel. They do not: other channels are flat.

Open high-impact assumptions next to these findings: A4.

## 7. Review

- Verdict: ready with caveats.
- Technical issues: no material issues. Optional checks: (1) confirm A4 with marketing operations; (2) re-run with 2025 data when it exists; (3) the country differences rest on small daily counts and were not tested.
- Business issues: the ask was "why". The analysis answers "how much, when and where", and says so. The recommendation covers only what was measured.
- Leadership questions, with answers:
  1. "Is it the spend cut?" Not supported yet. Spend and paid social sign-ups fell in the same week. That is timing, not proof. A market test would answer it.
  2. "Are we losing customers everywhere?" No. The other four channels together were down 2.6% per day.
  3. "Is this just the season?" Cannot be checked: no 2025 data. A seasonal dip across the board is not what the data shows, since four of five channels held.
  4. "How sure are the numbers?" The counts are exact and agree with the growth dashboard within 0.4%.
  5. "What should we do?" Look at paid social first. Decide whether a spend test is worth running before the Q2 split.
- Independent recompute (Q4.1, from the raw table, without `signups_clean`): Jan 1,330, Feb 1,175, Mar 973; paid social per day 15.32 and 5.42. Same as Q1.4 and Q3.1. No gap.
- Spot-check of the ladder: rung 4 (Q1.4) summed `signups_clean`, the table it was checking, so it tested the aggregation only. Q4.1 above covers the data. The readout Method line says so.
- Readout: every sentence changed, as a "was" and "now" pair, and why. Readout status: FINAL
  - was: "The fall was driven by paid social." now: "Almost all of the fall is in one channel, paid social." Why: "driven by" is above the exploratory ceiling.
  - was: "Sign-ups fell 17% in March." now: "down 17%. Per day the fall was 25%, because March is three days longer." Why: the total alone understates the fall.
  - was: "The spend cut explains the timing." now: "That timing is a lead worth following, not a proven cause." Why: causal wording with no design.
  - was: "Checks passed: all five rungs of the validation ladder, after one failed rung was fixed." now: "Checks passed: daily series with no gaps or zero days; rungs 1 to 3 on raw rows (...); rung 4 summed the cleaned table and the review recomputed the headline numbers from the raw table, with no gap; ..." Why: the Method line claimed more than ran (v0.3 re-review).
  - was: a key numbers table with 7 rows. now: 5 rows, the other 2 in the Appendix, and a chart for the weekly step. Why: an exec readout has at most 5 key numbers (v0.3).

## 8. Retro

| proposed data map change | accepted (yes or no) |
|---|---|
| Gotchas: `signups` has a second row for about 1% of sign-ups from late updates | yes |
| Rules: keep one row per `signup_id`, latest `updated_ts` | yes |
| Gotchas: compare daily averages or full weeks when months differ in length | yes |
| Gotchas: the growth dashboard runs up to 0.4% under the table; use a 1% tolerance | yes |
| Metrics: new trusted number, 972 sign-ups for March 2026 | yes |
| Joins: aggregate `signups` before joining to `daily_spend` | yes |
| Glossary: "paid social sign-ups fell because of the spend cut" | no: not a fact the data supports |

## 9. Decisions

### Round 1 (2026-04-02)

| # | question | user's answer (verbatim) |
|---|---|---|
| 1 | What counts as a sign-up? | "Accounts created. Leave out test accounts." |
| 2 | Which periods to compare? | "March against February. January for context." |
| 3 | What is the answer for? | "The Q2 budget split by channel." |

### Round 2 (2026-04-02)

| # | question | user's answer (verbatim) |
|---|---|---|
| 1 | Who reads the result? | "Exec." |

## 10. Hypotheses

| id | hypothesis | would support it | would refute it | leads to | status |
|---|---|---|---|---|---|
| H1 | The fall is concentrated in one channel | One channel's per-day sign-ups fall far more than the others | Every channel falls by about the same share | H1.1 | supported (Q3.1: paid social 15.32 to 5.42 per day) |
| H1.1 | The fall in that channel follows the spend cut | Sign-ups fall in the week spend falls | Sign-ups fall before spend does | none (needs a market test) | parked (timing matches, no design to test a cause) |
| H2 | A logging break explains the drop | Zero or missing days in the daily series | A full daily series with no gaps | none | refuted (Q0.2: no gaps, no zero days) |
| H3 | The whole app dipped (season) | All channels fall together | Most channels hold | none | refuted (four of five channels held) |

## 11. Appendix: Review pack

The code behind each headline number. Every query file is in `scripts/`; results are in `outputs/results.txt`.

### Sign-ups per month (February 1,175; March 973) and per day (41.96; 31.39)

- Source: `signups`, January to March 2026, test accounts out, latest row per `signup_id` (`signups_clean`, built by `q1-3c-clean-view.sql`).
- Code: `q1-4-aggregates.sql`

```sql
select
    signup_month
  , count(*)                                        as signups
  , count(distinct signup_date)                     as days_with_signups
  , round(count(*) * 1.0 / count(distinct signup_date), 2) as signups_per_day
from
    signups_clean
where true
group by 1
order by 1
;
```

### Paid social per day (15.32 to 5.42) and share of the fall (93.6%)

- Source: `signups_clean`, February and March 2026.
- Code: `q3-1-scan-channel.sql`. Recomputed from the raw table in `q4-1-review-recompute-from-raw.sql`:

```sql
select
    substr(signup_ts, 1, 7)                                                as signup_month
  , count(distinct signup_id)                                              as signups
  , count(distinct case when channel = 'paid_social' then signup_id end)   as paid_social_signups
  , round(count(distinct case when channel = 'paid_social' then signup_id end) * 1.0
        / count(distinct substr(signup_ts, 1, 10)), 2)                     as paid_social_per_day
from
    signups
where true
    and is_test = 0
group by 1
order by 1
;
```

### Reconcile to the growth dashboard (gaps 0.30%, 0.34%, 0.10%)

- Source: `signups_clean` against `dashboard_monthly`. The cleaned count is compared: the dashboard counts sign-ups, not rows, so duplicate rows and test accounts must be out first.
- Code: `q1-5-reconcile.sql`.
