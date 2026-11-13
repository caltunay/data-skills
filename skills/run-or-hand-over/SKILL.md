---
name: run-or-hand-over
description: Decide whether to run a query or save a file yourself, or hand it to the user. Applies whenever a data query needs running or a file (analysis notes, queries, outputs) needs saving, in a coding agent, a chat app, or with no data connection.
---

# Run or hand over

Never fail because a tool is missing.

## Core rule

Run it or save it if you can. Otherwise offer a download. Otherwise print it and wait for the user.

## Decide per action

| Situation | Queries | Files |
|---|---|---|
| Data connected and you can run code | Run them | Save under `data-work/` |
| You can write files but have no data access | Hand the query over, wait for the paste | Save under `data-work/` |
| Chat app, can offer a download | Hand the query over, wait for the paste | Offer a download |
| Chat app, no download | Hand the query over, wait for the paste | Print one block to copy |

Excel, Power BI and Tableau work always runs in hand-over mode. You give steps, the user does them and pastes the result.

## Copy-paste form for queries

Number each query. Give it one purpose line and the expected result. End with the paste request.

```
Q2.1  Purpose: count rows per order_id in the joined table. Expect: every count is 1.
select
    order_id
  , count(*) as row_count
from
    joined_orders
where true
group by 1
having count(*) > 1
;
Paste the result here.
```

Rules:

- State the expected result before the user runs it.
- Keep each check query small. One question per query.
- Number them Q<step>.<n> so answers can be matched.
- Ask for aggregates, not row-level data, unless row-level data is needed. Say why when you ask.
- Wait for the paste. Do not carry on with invented numbers.

## Files

- Coding agent: write to the user's own project in `data-work/`. Never write into the skills repo.
- Chat app: keep the analysis in the chat. Offer `analysis.md` as a download at the end. If you cannot, print it as one block.
- Quick depth: write no files.
- Ask before saving row-level data anywhere. Aggregates are the default.
- Do not store raw chat transcripts. `analysis.md` is the record.

## Access test

To test whether you can run queries, try a trivial one (`select 1`). If it fails, say so once, switch to hand-over mode, and carry on. Do not retry in a loop.

## Credentials

Never ask for keys or passwords. Data access comes from the user's own connectors.
