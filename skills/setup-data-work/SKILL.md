---
name: setup-data-work
description: Set up a team or project for the data-skills flow by building DATA-MAP.md from a connection, a description or a pasted schema. Use only when the user runs /setup-data-work or explicitly asks to set up their data map.
---

# /setup-data-work

Run once per team or project. Target: under 20 minutes. Partial answers are fine. The map grows through retros.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.
- Never ask for keys or passwords.

## Start

1. Check for `DATA-MAP.md` (in `data-work/`, in the Project files, or pasted). Say in one line what you found. This step needs no `analysis.md`.
2. If a map exists, read it. Check its format line and stale entries (see the `data-map` rule below). Offer to extend it. Do not start from zero.
3. If there is no map, say so and go to step 0.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and a recommended default. Wait for answers. Never assume silently.
- `data-map`: one file, fixed sections, `format: v1` on line 1. Every entry has `verified: YYYY-MM-DD` and `source: setup`. Flag entries older than 90 days or contradicted by data, then ask. Show a migration before applying it. The template is `DATA-MAP.template.md` in the `data-map` skill.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Never fail because a tool is missing. Never call a data tool before the user names the source.

## Steps

Ask in rounds of at most 3 questions. Skip what the user already told you.

0. **Setup mode. Always first, before touching any tool.** Ask: "How do you want to set up your data map? A) Connect: I list the data tools you have connected and you pick one or none. B) Describe it in your own words. C) Paste a schema: table list, CREATE statements, dbt file or doc. D) A mix." Wait for the answer.
   - If the user's own message already makes the mode clear (for example, they pasted a schema, or said connectors are blocked), say in one line which mode you understood and continue. Never work the mode out from the connectors you can see.
   - A: only now, list the connected data tools by name. Listing is not calling. The user picks one or none.
   - B: interview the user with the steps below.
   - C: read the paste. Fill what it states. Ask the user to confirm grain and keys. Do not guess them.
   - D: combine the above, in the order the user prefers.
1. **Access test. Only for a source the user named.** If the user chose to connect, run a trivial test (`select 1`) against that source only. If it is not clear which connected tool is the named source, ask. If there is no connection, tell the user once to check their agent's connector directory for their source. If it is missing or blocked by company policy, continue in hand-over mode. No dead ends.
2. **Sources.** Which sources, what type (warehouse, lake, sheet, file, API, cube), and which dialect for each.
3. **Key tables.** The 3 to 10 tables used most. For each: what one row means (grain) and the key.
4. **Joins.** The joins they trust, and any known fan-out traps.
5. **Metrics.** The 3 to 5 most-used metrics: definition, and one trusted number each (value, period, where it comes from) for reconciling.
6. **Rules.** Mandatory filters: test accounts, cancelled orders, time zones.
7. **Conventions.** "Does your team have SQL or Python conventions? If not, I'll use sqlstyle.guide and PEP 8."
8. **Git policy.** Commit `outputs/` or not. Default: not.

Optional line: "If you have a web search or docs lookup tool, check the current setup steps for your agent and source." Never required.

## Output

1. Write `data-work/DATA-MAP.md` from the template. Fill what you know. Leave unknown sections as empty tables. Date every entry today, with `source: setup`.
2. Add `data-work/analyses/*/outputs/` to `.gitignore` unless the user chose to commit outputs.
3. Show a short summary of what is still missing, as a list.

## End

- Chat app (no user project folder: no `data-work/` and no repo, even if you can write files in a sandbox): offer the full `DATA-MAP.md` as a download. If you cannot, print it as one block. Tell the user to save it to their Project files so every later step, in any chat, can read it.
- Name the next step: `/grill-the-ask` with the first ask.

## Depth

This step has no depth levels. It is the same for every project.

## Do not

- Do not invent tables, joins or numbers. Leave a gap and say it is a gap.
- Do not store credentials.
- Do not write into the skills repo. Files go in the user's own project.
- Do not force a long interview. Stop when the user stops.
