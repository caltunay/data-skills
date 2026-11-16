---
name: run-or-hand-over
description: Decide whether to run a query or save a file yourself, or hand it to the user, inside the data-skills flow. Applies when a flow step (setup, grill, plan, run, review, retro) has a check query to run or an analysis file to save, in a coding agent, a chat app, or with no data connection.
---

# Run or hand over

Never fail because a tool is missing.

## Core rule

Run it or save it if you can. Otherwise offer a download. Otherwise print it and wait for the user. Never call a data tool before the user names the source.

## Sources and names

- Never call a connector or data tool until the user has named the source it applies to. Seeing a connector is not permission to use it.
- Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.
- Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Which environment am I in?

Decide by situation, not by file access.

- **Coding agent:** there is a user project folder (a repo, or a `data-work/` folder).
- **Chat app:** there is no user project folder. Behave as a chat app even if you can write files in a sandbox. A sandbox file is not the user's file until they download it.

## Decide per action

| Situation | Queries | Files |
|---|---|---|
| Coding agent, the user named a connected source | Run them | Save under `data-work/` |
| Coding agent, no data connection | Hand the query over, wait for the paste | Save under `data-work/` |
| Chat app | Hand the query over, wait for the paste. Run only against a source the user named | Offer a download. If you cannot, print one block to copy |

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
- While waiting, set the Progress line in `analysis.md`, for example `Progress: run step 3 of 7, waiting for Q3.1 paste`.

## Files

- Coding agent: write to the user's own project in `data-work/`. Never write into the skills repo.
- Chat app: at the end of every flow step, offer the updated `analysis.md` (and `readout.md` when it exists) as a download. If you cannot, print it as one block. Tell the user to save it to their Project files so the next step, in any chat, can read it.
- If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything.
- Quick depth: write no files.
- Ask before saving row-level data anywhere. Aggregates are the default.
- Do not store raw chat transcripts. `analysis.md` is the record.

## Access test

Only after the user has named the source. Try a trivial query (`select 1`) against that source only. If it fails, say so once, switch to hand-over mode, and carry on. Do not retry in a loop. Do not test other connectors.

## Credentials

Never ask for keys or passwords. Data access comes from the user's own connectors.
