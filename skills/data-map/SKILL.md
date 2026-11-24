---
name: data-map
description: Read or update the team's DATA-MAP.md, the shared record of sources, tables, joins, metrics, rules, gotchas, glossary and conventions. Applies inside the data-skills flow, when a DATA-MAP.md file is present, or when the user mentions their data map. Stays silent when there is no map and no flow step is running.
---

# Data map

`DATA-MAP.md` is the team's shared memory of the data. It lives in the user's project at `data-work/DATA-MAP.md`. In a chat app it lives in the Project files.

The template is `DATA-MAP.template.md` in this skill's folder.

## Core rule

Outside the flow, stay silent if there is no map. Read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask. Change it only through approved retro changes. Check the format version and offer a migration if old.

## Reading

1. Look for `data-work/DATA-MAP.md` in the current folder, then upward. A team map can sit above project maps: the nearest map wins for conflicts, and you say which map you read. Open `DATA-MAP.md` if it exists. The map is optional and partial.
   - **Inside the flow** (a flow command is running): say in one line which map you found and read. If there is none, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Offer it once per analysis.
   - **Outside the flow:** if there is no map, stay silent. Do not mention the map, and do not suggest setup.
2. Use these sections: Goals (mission, north star, targets and their horizon), Funnels (steps, events, definitions), Key queries (3 to 5 reusable queries, what they return, when to use them), Sources (dialect, access mode), Tables (grain, keys), Joins (safe joins and fan-out traps, each with a check status: `unverified` until a query measured its match rate and fan-out, then `checked`), Metrics (definitions, trusted numbers), Rules (mandatory filters), Gotchas, Glossary, Conventions (style only: SQL, Python, naming; analysis rules go in Rules or Gotchas).
3. Apply Rules filters in every query. Say which ones you applied.
4. Use Conventions over the default styles.

## Staleness

Every entry has `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.

- Older than 90 days: say so and ask whether it still holds before relying on it.
- Contradicted by data (a trusted number does not reconcile, a key is not unique): say so, show the evidence, ask.
- Never silently fix or drop an entry.

## Format version

Line 1 is `format: v1` and line 2 is `updated: YYYY-MM-DD HH:MM`. A map without the Goals, Funnels or Key queries sections is still valid: add them as empty tables at the next update. A map without an `updated:` line gets one at the next update. Two copies of the map: use the newest `updated:` and say so. If the format line is missing or older, tell the user, show the exact changes a migration would make, and apply them only after approval.

## Updating

Only the retro step changes the map. It proposes dated changes, shows a diff, and the user approves each one. Good entries:

- a new safe join, or a fan-out trap
- a mandatory filter that was missing
- a confirmed metric definition or a new trusted number
- a gotcha from a mistake that cost time
- a glossary term
- a funnel, or a key query worth keeping (3 to 5 in all)

Not a memory dump. Do not add one-off details of a single analysis.

Each new entry gets today's date and `source: analyses/<slug>`. In a chat app, hand back the full updated `DATA-MAP.md` to replace the Project file. In a coding agent, edit the file in place.

## Safety

- Never put credentials, keys or row-level data in the map.
- The map is shared, so keep entries factual and neutral.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
