---
name: setup-data-work
description: Set up a team or project for the data-skills flow by building DATA-MAP.md from a connection, a description or a pasted schema. Use only when the user runs /setup-data-work or explicitly asks to set up their data map.
---

# /setup-data-work

Run once per team or project. Target: under 20 minutes. Partial answers are fine. The map grows through retros.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.
- Never ask for keys or passwords.

## Start

1. Check for `DATA-MAP.md` (in `data-work/` in the current folder, then upward; in the Project files; or pasted). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts. This step needs no `analysis.md`.
2. If a map exists, read it. Check its format line and stale entries (see the `data-map` rule below). Offer to extend it. Do not start from zero. Step 0 still applies to anything new: ask how the user wants to add it. **Tidy it when you extend it.** Normalise the map to the template: one entry per source (split a bullet that lists several files or tables as one source), grain and keys under Tables (fill them from what the user says, never guess), the template's table layout instead of loose bullets, key queries as SQL, and a Ways of working section. Show the tidy as a diff and apply it only after the user approves.
3. If there is no map, say so. First ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." If yes, read it and extend it (carry it over; start a fresh map only for entirely different data sources). If no, go to step 0.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and one real recommended default with its reason. A hedge is not a default: never "recommended if you have one", "TBC" or "C if unknown". Pick a real option and say why. Show any tree, table or draft a question refers to before you ask it (never ask "which hypothesis paths?" before the tree is on screen). Each option says what it means in a few words (for example "H1.1: holds in each month"). An option that needs data the map says is missing says so in the option text (for example "needs the visit marker; the map says it is unknown"). Use the environment's multiple-choice question tool for every round if it has one (one card per question, recommended option first, room for the user's own answer); otherwise list the options as text. Wait for answers. Never assume silently. When an answer conflicts with an earlier one or the data map, or does not make sense, say so plainly and ask one question at a time until it is clear. Never ask the same question twice.
- `data-map`: one file, fixed sections, `format: v1` on line 1 and `updated: YYYY-MM-DD HH:MM` on line 2 (set to now at every change). Sections include Goals, Funnels, Key queries (each as SQL text) and Ways of working. Joins start `unverified` until a query checks them. Conventions hold style only. Every entry has `verified: YYYY-MM-DD` and `source: setup`. Flag entries older than 90 days or contradicted by data, then ask. Show a migration before applying it. The template is `DATA-MAP.template.md` in the `data-map` skill.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand. Never fail because a tool is missing. Never call a data tool before the user names the source.

## Steps

Ask in rounds of at most 3 questions. Skip what the user already told you. Every question has a real recommended default with its reason, even a free-text one (for example, "Recommended: start with the 3 tables you used last week, because the map grows through retros"). Never "recommended if you have one" or "TBC".

0. **Setup mode. Always first, before touching any tool.** Ask: "How do you want to set up your data map? A) Connect: I list the data tools you have connected and you pick one or none. B) Describe it in your own words. C) Paste a schema: table list, CREATE statements, dbt file or doc. D) A mix." Wait for the answer.
   - If the user's own message already makes the mode clear (for example, they pasted a schema, or said connectors are blocked), say in one line which mode you understood and continue. Never work the mode out from the connectors you can see.
   - A: only now, list the connected data tools by name. Listing is not calling. The user picks one or none. This is the only place where connector names may be listed, and only after the user chose A.
   - B: interview the user with the steps below.
   - C: read the paste. Fill what it states. Ask the user to confirm grain and keys. Do not guess them.
   - D: combine the above, in the order the user prefers.
1. **Access test. Only for a source the user named.** If the user chose to connect, run a trivial test (`select 1`) against that source only. If it is not clear which connected tool is the named source, ask. If there is no connection, tell the user once to check their agent's connector directory for their source. If it is missing or blocked by company policy, continue in hand-over mode. No dead ends.
2. **Sources.** Which sources, what type (warehouse, lake, sheet, file, API, cube), and which dialect for each. Ask the dialect with one real option per engine, never one option holding many names:

   **Which SQL dialect does this source use?**
   - A. Postgres
   - B. SQL Server
   - C. BigQuery
   - D. Snowflake
   - E. Databricks
   - F. Other (say which)

   Recommend the one the user's own words point to (for example, they named the engine or pasted its syntax). If nothing points to one, recommend A (the most common default) and say the first check query will show if it is wrong.
3. **Key tables.** The 3 to 10 tables used most. For each: what one row means (grain) and the key.
4. **Joins.** The joins they trust, and any known fan-out traps. Every join starts as `unverified` in the map, even when the schema or the user says it is safe. A join becomes `checked` only after a query measured its key match rate and fan-out (in setup, only if a source is connected and the user agrees to run it). Never mark a join checked from a schema alone.
5. **Metrics.** The 3 to 5 most-used metrics: definition, and one trusted number each (value, period, where it comes from) for reconciling.
6. **Goals.** "What are the organisation's goals?" Ask for the mission, the north star metric, the target metrics, and the horizon of each (this quarter, this year, 3 years). Partial is fine. Write them to the Goals section. `/grill-the-ask` later asks how an ask links to one of them.
7. **Funnels.** "What are the main funnels?" For each: every step, the event or table that marks it, and the step definition (what counts as having reached it). Write them to the Funnels section.
8. **Key queries.** "Which 3 to 5 queries does the team reuse?" For each: what it returns and when to use it, and the query itself. Save each as SQL text under its name (a table row plus a SQL block), written in the team's SQL conventions (step 10; sqlstyle.guide if none) and checked against the columns the map knows from the Tables section. A column the map does not know goes in "columns used" marked `unchecked`. Never save a description without the SQL. If the user has no SQL to hand, write it from the Tables section and say it is untested. Keep to 5 at most.
9. **Rules.** Mandatory filters: test accounts, cancelled orders, time zones.
10. **Conventions.** "Does your team have SQL or Python conventions? If not, I'll use sqlstyle.guide and PEP 8."
11. **How you work.** "How do you organise your work? A) One repo with a folder per project. B) A repo per project. C) A team repo. D) Chat Projects (Claude or ChatGPT)." Recommend the one the user's own words point to. For A to C, the map goes in `data-work/` (skills look in the current folder, then upward, so a team map can sit above project maps and the nearest map wins for conflicts). For D, recommend one Project per team or area and one chat per analysis. Record the answer in the map under Ways of working (`where work lives`).
12. **Git policy (coding agent only).** Commit `outputs/` or not. Default: not. In a chat app there is no repo: skip this question and give no git advice. For a team repo, say the map is committed so the team shares it.
13. **File hand-back (chat app, ask once per Project).** "How should I hand files back? A) As downloads. B) As files in your Project. C) Save to a document tool you use (for example a drive, a wiki or a notes app)." Recommend B if this session can write to the Project files, otherwise A, and say why. Use only a tool the user names for C, never one picked from visible connectors. Never required. Record the answer in the map under Ways of working (`file hand-back`), so later steps never ask again.

Optional line: "If you have a web search or docs lookup tool, check the current setup steps for your agent and source." Never required.

## Output

1. Write `data-work/DATA-MAP.md` (full path) from the template (`updated:` line set to now). Fill what you know. Joins go in with check status `unverified` unless a query in this session checked them. Leave unknown sections as empty tables. Date every entry today, with `source: setup`.
2. Coding agent with a repo: add `data-work/analyses/*/outputs/` to `.gitignore` unless the user chose to commit outputs. Chat app: skip this. No git advice in a chat app.
3. Chat app: also write the **Project instructions block** (see End).
4. Show a short summary of what is still missing, as a list.

## End

- Chat app (no user project folder: no `data-work/` and no repo): save the full map at its full path, `data-work/DATA-MAP.md`, never as a bare `DATA-MAP.md`. Say exactly what happened, in one of three forms: "Saved to `data-work/DATA-MAP.md` in your Project files" (you wrote it there), "Download `DATA-MAP.md` and add it to your Project at `data-work/DATA-MAP.md`" (you could not write to Project files), or "Printed below; save it as `data-work/DATA-MAP.md`" (creating the file failed). Never claim a save that did not happen. Never ask the user to edit a saved file by hand. If an older copy of the map sits elsewhere in the Project (for example at the top level or in `claude/`), name it and say it is stale.
- Chat app: end the output with a short block to paste into the Project's instructions, in a fenced block, for example:

  ```
  Read data-work/DATA-MAP.md before any data work. Use the data-skills commands. Keep files in data-work/ as the skills lay them out. At the end of each step, tell me which files changed and where they are.
  ```

  Use these words exactly. Add a line for the document tool if the user named one. When they start another Project on the same data, they carry over `data-work/DATA-MAP.md` and this block.
- End with the go-ahead question in this fixed form:

  > Go ahead?
  > A) Yes, run `/grill-the-ask` with your first ask (recommended)
  > B) Change something in the map (say what)
  > C) Add a table, join, metric or rule

  Wait for the answer. B or C means make the change, hand back the updated `DATA-MAP.md`, and ask again.

## Depth

This step has no depth levels. It is the same for every project.

## Do not

- Do not invent tables, joins or numbers. Leave a gap and say it is a gap.
- Do not store credentials.
- Do not write into the skills repo. Files go in the user's own project.
- Do not force a long interview. Stop when the user stops.
