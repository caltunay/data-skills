---
name: data-map
description: Read or update the team's DATA-MAP.md, the shared record of sources, tables, joins, metrics, rules, gotchas, glossary and conventions. Applies inside the data-skills flow, when a DATA-MAP.md file is present, or when the user mentions their data map. Stays silent when there is no map and no flow step is running.
---

# Data map

`DATA-MAP.md` is the team's shared memory of the data. It lives in the user's project at `data-work/DATA-MAP.md`. In a chat app it lives in the Project files at the same path, `data-work/DATA-MAP.md`. Never save it under a bare name.

The template is `DATA-MAP.template.md` in this skill's folder.

## Core rule

Outside the flow, stay silent if there is no map. Read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask. Change it only through approved retro changes. Check the format version and offer a migration if old.

## Reading

1. Look for `data-work/DATA-MAP.md` in the current folder, then upward. A team map can sit above project maps: the nearest map wins for conflicts, and you say which map you read. Open `DATA-MAP.md` if it exists. The map is optional and partial.
   - **Inside the flow** (a flow command is running): say in one line which map you found and read. If there is none, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." If not, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: I ask about the data inline, and `/retro-analysis` starts the map." Offer it once per analysis.
   - **Outside the flow:** if there is no map, stay silent. Do not mention the map, and do not suggest setup.
2. Use these sections: Goals (mission, north star, targets and their horizon), Funnels (steps, events, definitions), Key queries (3 to 5 reusable queries, each saved as SQL text in the team's conventions with its columns checked against Tables, plus what it returns and when to use it), Sources (dialect, access mode), Tables (grain, keys), Joins (safe joins and fan-out traps, each with a check status: `unverified` until a query measured its match rate and fan-out, then `checked`), Metrics (definitions, trusted numbers), Rules (mandatory filters), Gotchas, Glossary, Conventions (style only: SQL, Python, naming; analysis rules go in Rules or Gotchas), Ways of working (where work lives: chat Projects or a repo layout; file hand-back: downloads, Project files or a named document tool). Never ask the user about hand-back when this section answers it.
3. Apply Rules filters in every query. Say which ones you applied.
4. Use Conventions over the default styles.

## Staleness

Every entry has `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.

- Older than 90 days: say so and ask whether it still holds before relying on it.
- Contradicted by data (a trusted number does not reconcile, a key is not unique): say so, show the evidence, ask.
- Never silently fix or drop an entry.

## Format version

Line 1 is `format: v1` and line 2 is `updated: YYYY-MM-DD HH:MM`. A map without the Goals, Funnels, Key queries or Ways of working sections is still valid: add them as empty tables at the next update. A map without an `updated:` line gets one at the next update. Two copies of the map: use the newest `updated:` and say so. If the format line is missing or older, tell the user, show the exact changes a migration would make, and apply them only after approval.

## Tidy

When setup or a retro extends a map, normalise it to the template: one entry per source (a bullet that lists several files is several entries or one table, never one source), grain and keys under Tables, table layout instead of loose bullets, key queries as SQL text, a Ways of working section. Show the tidy as a diff. Apply it only after approval.

## Updating

Only the retro step changes the map. It proposes dated changes, shows a diff, and the user approves each one. Good entries:

- a new safe join, or a fan-out trap
- a mandatory filter that was missing
- a confirmed metric definition or a new trusted number
- a gotcha from a mistake that cost time
- a glossary term
- a funnel, or a key query worth keeping (3 to 5 in all), saved as SQL text

Not a memory dump. Do not add one-off details of a single analysis.

Each new entry gets today's date and `source: analyses/<slug>`. In a chat app, save the full updated map at `data-work/DATA-MAP.md` and say exactly what happened: "Saved to `data-work/DATA-MAP.md` in your Project files", "Download `DATA-MAP.md` and add it to your Project at `data-work/DATA-MAP.md`", or "Printed below; save it as `data-work/DATA-MAP.md`". Name any stale older copy. In a coding agent, edit the file in place.

## Safety

- Never put credentials, keys or row-level data in the map.
- The map is shared, so keep entries factual and neutral.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
