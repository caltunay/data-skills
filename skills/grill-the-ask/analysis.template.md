format: v1

# Analysis: <title>

## 1. Meta

- Title:
- Requester:
- Audience: exec | product | data | mixed
- Date:
- Depth: quick | standard | deep
- Question type: descriptive | exploratory | inferential | predictive | causal | mechanistic
- Status: grilling | planned | running | reviewed | retro done
- Progress: <step, where it stopped, what it waits for. Example: run step 3 of 7, waiting for Q3.1 paste>

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

-

### Plan revisions

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
- Readout: sentences changed, and why. Readout status: draft | final

## 8. Retro

| proposed data map change | accepted (yes or no) |
|---|---|
