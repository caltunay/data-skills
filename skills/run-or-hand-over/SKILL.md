---
name: run-or-hand-over
description: Decide whether to run a query or save a file yourself, or hand it to the user, inside the data-skills flow. Applies when a flow step (setup, grill, plan, run, review, retro) has a check query to run or an analysis file to save, in a coding agent, a chat app, or with no data connection.
---

# Run or hand over

Never fail because a tool is missing.

## Core rule

Two separate questions. Can I run things here? Always try first. Where do files persist? In a chat app, save the file at its full `data-work/` path in the Project files if you can, otherwise create it and offer a download, and say which. Print it only if that fails. Never call a data tool before the user names the source.

## Sources and names

- Never call a connector or data tool until the user has named the source it applies to. Seeing a connector is not permission to use it.
- Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.
- Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Question 1: can I run things here?

Always try first. Decide by the tools you have, not by the app you are in.

- A connected source the user named: run the query against it.
- A code tool or sandbox, with data files the user attached or uploaded: load the files and run the checks yourself. Use SQL (DuckDB or SQLite) or pandas. This counts as running, even in a chat app.
- Only when no code tool exists, or the data is not reachable from it (it sits in the user's warehouse with no connection): hand the query over. Say why in one line, for example "No code tool here, so I hand the queries over."
- Never say "I can't run code" when a code tool exists. Never hand over a check you could run on an attached file.

## Question 2: where do files persist?

Decide by situation, not by file access.

- **Coding agent:** there is a user project folder (a repo, or a `data-work/` folder). Save files under `data-work/`.
- **Chat app:** there is no user project folder. A sandbox file is not the user's file until it is in their Project files or they download it. If you can write to the Project files, write each file there at its full path. If you cannot, create each file in the sandbox and offer it as a download. Print it as one block only if creating the file fails.
- Never say "I can't save files" when you can create a download.

## Decide per action

| Situation | Queries | Files |
|---|---|---|
| Coding agent, the user named a connected source | Run them | Save under `data-work/` |
| Coding agent, no data connection | Hand the query over, wait for the paste | Save under `data-work/` |
| Chat app with a code tool and attached data files | Load the files and run the checks (DuckDB, SQLite or pandas) | Write it to the Project files, or create it and offer a download |
| Chat app, data only in a source with no connection | Hand the query over, wait for the paste | Write it to the Project files, or create it and offer a download |
| Chat app with no code tool | Hand the query over. Say so in one line | Print one block to copy |

Excel, Power BI and Tableau work always runs in hand-over mode. You give steps, the user does them and pastes the result.

## Copy-paste form for queries

Use this only when you cannot run the query yourself (see question 1). Number each query. Give it one purpose line and the expected result. End with the paste request. When there are several checks, batch them into numbered groups so the user pastes once per group, not once per query.

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

### One layout

All user files live under `data-work/`, in a coding agent and in a chat app:

```
data-work/DATA-MAP.md
data-work/wayfinder/<slug>.md
data-work/analyses/<YYYY-MM-DD>-<slug>/
    analysis.md
    readout.md
    readout.docx
    scripts/        every script behind a number, a check or a chart
    <charts>        SVG in a chat app that can write text but not binary files
    experiment-spec.md or metric-spec.md   (design asks)
```

- **Never save with a bare file name.** In claude.ai a bare name lands in a `claude/` folder, and a generic name such as `experiment-spec.md` is overwritten by the next spec. Always use the full path.
- The analysis folder is `<YYYY-MM-DD>-<slug>`: the date the ask was grilled, and a short slug. Meta holds it as `Folder`. Every script is its own file in `scripts/`, in any environment (scripts are text). Each script takes the data folder as an argument and writes its outputs into the analysis folder, never a temp path. Coding agents also keep `outputs/`. In a chat app, charts sit in the analysis folder itself, saved as SVG when the agent can write text files but not binary files. PNG stays inside binary outputs (`.docx`, `.pptx`).
- A coding agent writes the files under `data-work/` in the repo.

### Say exactly what happened to each file

After a save, name the path. Use one of three forms and no others:

1. "Saved to `<path>` in your Project files" (you wrote it there).
2. "Download `<file>`" (you could not write to Project files). If it matters, say where a later step expects it ("the next step reads it from `<path>`"). Never ask the user to move a file or add it to a Project folder: chat apps do not let users place uploads in folders.
3. "Printed below; save it as `<path>`" (creating the file failed).

Never claim a save that did not happen. Never say "replace the old one, it is already saved there": it is saved, or the user must add it, never both. Coding agent: name the path you wrote.

### Stale copies

List stale copies by full path, never a bare name next to the live full path (never `DATA-MAP.md` beside `data-work/DATA-MAP.md`). One rule every time: a copy is stale when it has the same file name as a live file but sits at another path, or has an older `updated:` line. The list changes only when files change, so it does not shrink or grow between steps for no reason.

A step never leaves its own stale copy. If it renames or replaces a file it created, it removes or overwrites the old one where it can, and lists only the files it cannot remove. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` line and say so.

### Other rules

- Chat app: at the end of every flow step that could change files, hand back each file the step changed (for example `analysis.md`, and `readout.md` and `readout.docx` when they exist), in one of the three forms above. Say which files changed and where they are. A question turn changes no files: add no "Files changed" line.
- Every file starts with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch.
- Document tool (optional). Ask once per Project, generically: "Hand files to you as downloads, as files in your Project, or save them to a document tool you use (for example a drive, a wiki or a notes app)?" Use only a tool the user names, never one picked from the connectors you can see. Never required. The answer goes in Meta as `Files` and in the data map under Ways of working. If the map already holds the answer, never ask again.
- Charts: when you can write text files to the Project files but not binary files, save each chart as SVG in the analysis folder and link it from `readout.md`. SVG is text, so it saves and renders there. Keep PNG only inside binary outputs (`.docx`, `.pptx`).
- A readout `.docx` needs a document library in the sandbox. Use whatever it has. With no code tool, give `readout.md` plus the chart code only, and say so in one line.
- No manual file edits. After the user confirms something, never ask them to edit a saved file by hand. Make the change yourself and hand back the updated file.
- If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything.
- Quick depth: write no files.
- Ask before saving row-level data anywhere. Aggregates are the default.
- Do not store raw chat transcripts. `analysis.md` is the record.

## Access test

Only after the user has named the source. Try a trivial query (`select 1`) against that source only. If it fails, say so once, switch to hand-over mode, and carry on. Do not retry in a loop. Do not test other connectors.

## Credentials

Never ask for keys or passwords. Data access comes from the user's own connectors.
