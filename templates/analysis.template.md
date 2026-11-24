format: v1
updated: YYYY-MM-DD HH:MM

# Analysis: <title>

## 1. Meta

- Title:
- Requester: <person or role the user named; never blank>
- Audience: exec | product | data | mixed
- Date: <YYYY-MM-DD; never blank>
- Depth: quick | standard | deep
- Question type: descriptive | exploratory | inferential | predictive | causal | mechanistic
- Claim ceiling: <one line: the strongest wording allowed, and claim rules such as "X is a lead, not a cause">
- Status: grilling | planned | running | reviewed | retro done
- Progress: <step, where it stopped, what it waits for. Example: run step 3 of 7, waiting for Q3.1 paste>
- Setup choice: A (ran `/setup-data-work`) | B (inline, `/retro-analysis` builds the map) | map found. Never offer setup again once this is set.
- Goal link: <the goal in the data map's Goals section this ask serves, or "none">
- Files: download | <the document tool the user named>

## 2. Ask

- Original ask (verbatim):
- Clarified question:
- Decision it feeds:
- Metric, population, time window:
- Constraints:
- Deadline:

## 3. Assumptions

| id | assumption | why unavoidable | likely alternatives (1-3) | impact if wrong | how to check | status |
|---|---|---|---|---|---|---|
| A1 | | | | | | open |

Status: open, confirmed or rejected. Alternatives are required for high-impact rows only. Always keep all 7 columns.

## 4. Plan

### Options considered

| option | method | trade-offs | verdict |
|---|---|---|---|

### Chosen plan

### Success checks

Copy every "Checks that must pass" item of the method card here, word for word. The reconcile check says which count must match the trusted number (raw or cleaned) and why.

-

### Plan revisions

Every spec correction found in any step is a dated row (for example, "6 channels expected, 5 found"). Notes about changes go in rows, never under a "(none)" line.

| date | what changed | why |
|---|---|---|

## 5. Analysis table spec

- Grain (one row means):
- Keys:
- Measures:
- Dimensions:
- Time column and window:
- Filters and exclusions (from the data map):
- Tidy (long) or wide, and why:
- Context columns needed to interpret results:
- Expected row count or range:

## 6. Results

### Ladder log

Data-check floor first (every depth), then the rungs. Rungs 2 to 4 compare against an independent path (raw rows or a separate query).

| check | expected | actual | pass or fail |
|---|---|---|---|
| F1 table audit (rows, duplicate keys, nulls, date range, category labels) | | | |
| F2 one real entity across tables | | | |
| F3 one day, all entities | | | |
| F4 daily series (gaps, spikes, zero days) | | | |
| F5 join checks (row counts, match rate, fan-out) | | | |
| F6 category totals sum to overall | | | |
| F7 assumption checks | | | |
| 1 one entity | | | |
| 2 one entity-day | | | |
| 3 many entities | | | |
| 4 aggregates | | | |
| 5 reconcile (F8): raw or cleaned count, and why | | | |

### Method checks

Method card used: <name>. Each item under "Checks that must pass": pass or fail.

| check | pass or fail | note |
|---|---|---|

### Findings

Each finding: direction, magnitude, uncertainty, claim ceiling applied. Aggregates only unless the user approved saving row-level data.

## 7. Review

- Verdict: ready | ready with caveats | needs rework
- Technical issues:
- Business issues:
- Leadership questions, with answers:
- Independent recompute: each headline number, the route used, the value, and the gap.
- Readout: every sentence changed, as a "was" and "now" pair, and why. Readout status: DRAFT | FINAL

## 8. Retro

| proposed data map change | accepted (yes or no) |
|---|---|

## 9. Decisions

Every question asked and the user's answer, word for word, per round. After each round, echo the answers back exactly before moving on. Never paraphrase an answer: "this week" is not "later".

### Round 1 (<YYYY-MM-DD>)

| # | question | user's answer (verbatim) |
|---|---|---|
| 1 | | |

## 10. Hypotheses

Written by `/plan-analysis` at standard and deep depth, before the method options. At most 3 levels and about 12 nodes. Children are numbered H1.1, H1.2, then H1.2.1. `/run-analysis` updates the status. `/review-analysis` checks every node has one.

| id | hypothesis | would support it | would refute it | leads to | status |
|---|---|---|---|---|---|
| H1 | | | | H1.1, H1.2 | open |

Status: `open`, `supported`, `refuted` or `parked`. A node is `supported` or `refuted` only with a result in section 6 that shows it. Quick depth: a flat list of up to 3 hypotheses, no file.

## 11. Appendix: Review pack

For each headline number: the exact SQL or Python that produced it, and its data source. In a chat app `queries/` does not persist, so this is how a fresh reviewer sees the code.

### <headline number 1>: <value>

- Source: <table or file, filters, period>
- Code:

```sql
-- the exact query or script that produced the number
```
