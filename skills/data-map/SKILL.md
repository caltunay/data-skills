---
name: data-map
description: Read or update the team's DATA-MAP.md, the shared record of sources, tables, joins, metrics, rules, gotchas, glossary and conventions. Applies before writing any query, when a table or metric is named, and when a retro proposes changes.
---

# Data map

`DATA-MAP.md` is the team's shared memory of the data. It lives in the user's project at `data-work/DATA-MAP.md`. In a chat app it lives in the Project files.

The template is `DATA-MAP.template.md` in this skill's folder.

## Core rule

Read it before writing queries. Flag entries older than 90 days or contradicted by data, then ask. Change it only through approved retro changes. Check the format version and offer a migration if old.

## Reading

1. Open `DATA-MAP.md` if it exists. If not, say so once and continue. The map is optional and partial.
2. Use these sections: Sources (dialect, access mode), Tables (grain, keys), Joins (safe joins and fan-out traps), Metrics (definitions, trusted numbers), Rules (mandatory filters), Gotchas, Glossary, Conventions.
3. Apply Rules filters in every query. Say which ones you applied.
4. Use Conventions over the default styles.

## Staleness

Every entry has `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.

- Older than 90 days: say so and ask whether it still holds before relying on it.
- Contradicted by data (a trusted number does not reconcile, a key is not unique): say so, show the evidence, ask.
- Never silently fix or drop an entry.

## Format version

Line 1 is `format: v1`. If it is missing or older, tell the user, show the exact changes a migration would make, and apply them only after approval.

## Updating

Only the retro step changes the map. It proposes dated changes, shows a diff, and the user approves each one. Good entries:

- a new safe join, or a fan-out trap
- a mandatory filter that was missing
- a confirmed metric definition or a new trusted number
- a gotcha from a mistake that cost time
- a glossary term

Not a memory dump. Do not add one-off details of a single analysis.

Each new entry gets today's date and `source: analyses/<slug>`. In a chat app, hand back the full updated `DATA-MAP.md` to replace the Project file. In a coding agent, edit the file in place.

## Safety

- Never put credentials, keys or row-level data in the map.
- The map is shared, so keep entries factual and neutral.
