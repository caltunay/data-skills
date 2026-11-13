---
name: retro-analysis
description: Propose dated, approved updates to DATA-MAP.md after an analysis, such as new joins, traps, filters, definitions and trusted numbers. Use only when the user runs /retro-analysis or explicitly asks for a retro on an analysis.
---

# /retro-analysis

The data map should get better with every analysis. This is not a memory dump.

## Read first

Read `analysis.md` (all sections, especially Assumptions, Results and Review) and `DATA-MAP.md`. If there is no `analysis.md`, ask the user for a short summary of what was learned.

## Rules from the disciplines (in case they do not load)

- `data-map`: change the map only through approved retro changes. Each entry has `verified: YYYY-MM-DD` and `source: analyses/<slug>`. Flag entries older than 90 days or contradicted by data, then ask. Check the format version and offer a migration if old.

## Steps

1. Scan the analysis for things the next analyst would want to know:
   - a new **safe join**, with keys
   - a **fan-out trap** that bit
   - a **filter or rule** that was missing
   - a **metric definition** that was confirmed or corrected
   - a new **trusted number** (value, period, where it comes from)
   - a **gotcha** from a mistake that cost time
   - a **glossary** term
   - a **convention** the team settled
2. Check existing entries: did the data contradict any? Is any older than 90 days and re-confirmed by this work? Propose updating its `verified` date.
3. Propose changes as a short numbered list. Each one: section, the exact entry, why it is worth keeping.
4. Show a diff (old and new text) for each change.
5. The user approves each change: yes, no or edit. Do not apply unapproved changes.
6. Apply the approved changes, with today's date as `verified` and `source: analyses/<slug>`.
7. Record the proposals and the decisions in the Retro section of `analysis.md`. Set status `retro done`.

## Keep out

- One-off details of a single analysis.
- Row-level data, credentials, personal data.
- Opinions. Entries are facts the data supports.

## Output

- Coding agent: edit `data-work/DATA-MAP.md` in place with approved changes only.
- Chat app: hand back the full updated `DATA-MAP.md` in one block, to replace the Project file.
- If the map is not `format: v1`, show the migration first and apply it only after approval.

## Depth

The retro is the same at every depth. At quick depth with no `analysis.md`, work from what the user tells you.

## Done when

Every proposal has a decision, and approved changes are applied or handed back.

## Do not

- Do not write to the map without approval.
- Do not propose more than the analysis earned. Zero changes is a valid result: say "No data map changes needed."
