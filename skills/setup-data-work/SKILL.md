---
name: setup-data-work
description: Set up a team or project for the data-skills flow by testing data access and building DATA-MAP.md. Use only when the user runs /setup-data-work or explicitly asks to set up their data map.
---

# /setup-data-work

Run once per team or project. Target: under 20 minutes. Partial answers are fine. The map grows through retros.

## Read first

If `data-work/DATA-MAP.md` already exists (or the user pasted one), read it. Offer to extend it. Do not start from zero.

## Rules from the disciplines (in case they do not load)

- `grilling`: rounds of at most 3 questions, each with 2 to 4 options and a recommended default. Wait for answers. Never assume silently.
- `data-map`: one file, fixed sections, `format: v1` on line 1. Every entry has `verified: YYYY-MM-DD` and `source: setup`. Template is `DATA-MAP.template.md` in the `data-map` skill.
- `run-or-hand-over`: run or save if you can, else offer a download, else print it and wait. Never fail because a tool is missing.

## Steps

Ask in rounds of at most 3 questions. Skip what the user already told you.

1. **Access test.** "Can you run a query from here?" If yes, run a trivial test (`select 1`). If no, tell the user once to check their agent's connector directory for their source. If it is missing or blocked by company policy, continue in hand-over mode. No dead ends. Never ask for keys or passwords.
2. **Sources.** Which sources, what type (warehouse, lake, sheet, file, API, cube), and which dialect for each.
3. **Key tables.** The 3 to 10 tables used most. For each: what one row means (grain) and the key.
4. **Joins.** The joins they trust, and any known fan-out traps.
5. **Metrics.** The 3 to 5 most-used metrics: definition, and one trusted number each (value, period, where it comes from) for reconciling.
6. **Rules.** Mandatory filters: test accounts, cancelled orders, time zones.
7. **Conventions.** "Does your team have SQL or Python conventions? If not, I'll use sqlstyle.guide and PEP 8."
8. **Git policy.** Commit `outputs/` or not. Default: not.

Optional line: "If you have a web search or docs lookup tool, check the current setup steps for your agent and source." Never required.

## Output

1. Write `data-work/DATA-MAP.md` from the template. Fill what you know. Leave unknown sections as empty tables. Date every entry today.
2. Add `data-work/analyses/*/outputs/` to `.gitignore` unless the user chose to commit outputs.
3. Show a short summary of what is still missing, as a list.

Where files cannot be written (chat app): print the full `DATA-MAP.md` in one block, and tell the user to save it in the chat app's Project files.

## Depth

This step has no depth levels. It is the same for every project.

## Do not

- Do not invent tables, joins or numbers. Leave a gap and say it is a gap.
- Do not store credentials.
- Do not write into the skills repo. Files go in the user's own project.
- Do not force a long interview. Stop when the user stops.
