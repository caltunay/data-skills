---
name: retro-analysis
description: Propose dated, approved updates to DATA-MAP.md after an analysis, such as new joins, traps, filters, definitions and trusted numbers. Use only when the user runs /retro-analysis or explicitly asks to run a retro on an analysis.
---

# /retro-analysis

The data map should get better with every analysis. This is not a memory dump.

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user. A source listed in the map counts as named. If it is not clear which connected tool is that source, ask.

## Start (every flow step)

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/`, in the Project files, or attached). Say in one line what you found.
2. If there is no `DATA-MAP.md`, offer: "A) Run `/setup-data-work` first (recommended if you will analyse this data again). B) Continue: this retro starts the map from the template, with only the entries you approve." The template is `DATA-MAP.template.md` in the `data-map` skill. If it is not available, start with `format: v1` on line 1 and these sections: Sources, Tables, Joins, Metrics, Rules, Gotchas, Glossary, Conventions.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. At quick depth there is no file: ask for a short summary of what was learned.
4. Read the Progress line in Meta and resume from it. Then read all sections, especially Assumptions, Results and Review.

## Rules from the disciplines (in case they do not load)

- `data-map`: change the map only through approved retro changes. Conventions hold style only; analysis rules go in Rules or Gotchas; no duplicates across sections. Each entry has `verified: YYYY-MM-DD` and `source: analyses/<slug>`. Flag entries older than 90 days or contradicted by data, then ask. Check the format version and offer a migration if old.

## Steps

1. Scan the analysis for things the next analyst would want to know:
   - a new **safe join**, with keys
   - a **fan-out trap** that bit
   - a **filter or rule** that was missing
   - a **metric definition** that was confirmed or corrected
   - a new **trusted number** (value, period, where it comes from)
   - a **gotcha** from a mistake that cost time
   - a **glossary** term
   - a **convention** the team settled (style only: SQL, Python, naming)
   - a join that this run **checked** by query: propose changing its status from `unverified` to `checked`, with what the query found
2. Check existing entries: did the data contradict any? Is any older than 90 days and re-confirmed by this work? Propose updating its `verified` date.
3. Put each entry in the right section:
   - Conventions hold style only: SQL style, Python style, naming. Nothing else.
   - Analysis rules (a filter, an exclusion, a dedup rule, a time zone rule) go in Rules. Mistakes and traps go in Gotchas.
   - One fact goes in one section. No duplicate entries across sections. If a fact fits two, pick one and leave the other out.
4. Propose changes as a short numbered list. Each one: section, the exact entry, and why it is worth keeping. The reason must be true for this run: quote the line in `analysis.md` that shows it (a failed rung, a Plan revisions row, a review issue). If nothing in this run shows it cost time or changed a number, do not say it did.
5. Show a diff (old and new text) for each change.
6. The user approves each change: yes, no or edit. Do not apply unapproved changes.
7. Apply the approved changes, with today's date as `verified` and `source: analyses/<slug>`.
8. Record the proposals and the decisions in the Retro section of `analysis.md`. Set status `retro done` and update the Progress line.

## Keep out

- One-off details of a single analysis.
- Row-level data, credentials, personal data.
- Opinions. Entries are facts the data supports.
- Reasons that did not happen in this run. "This cost a rung" only if the ladder log shows a failed rung for it.

## Output

- Coding agent: edit `data-work/DATA-MAP.md` in place with approved changes only.
- Chat app: create the full updated `DATA-MAP.md` as a file and offer it as a download, to replace the Project file. Print one block only if creating the file fails. Never ask the user to edit the map by hand.
- If the map is not `format: v1`, show the migration first and apply it only after approval.

## End (every flow step)

Quick depth has no files: skip steps 1, 3 and 4, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Chat app: create the updated `analysis.md` (and `readout.md` when it exists) as files and offer them as downloads. Print one block only if creating a file fails. Never ask the user to edit a saved file by hand: hand back the updated file. Say: "Save this to your Project files so the next step, in any chat, can read it."
4. Coding agent: the files are already saved under `data-work/`. Say where.
5. In a chat app, also hand back the full updated `DATA-MAP.md` to replace the Project file.
6. The flow is complete. End with the go-ahead question, at every depth, quick included, adapted to this last step:

   > Go ahead?
   > A) Yes, close this analysis. Run `/grill-the-ask` for the next ask (recommended)
   > B) Change something (say what)
   > C) Add a map entry, a check or a question

   Wait for the answer. B or C means make the change, hand back the updated file, and ask again.

## Depth

The retro is the same at every depth. At quick depth with no `analysis.md`, work from what the user tells you.

## Done when

Every proposal has a decision, and approved changes are applied or handed back.

## Do not

- Do not write to the map without approval.
- Do not propose more than the analysis earned. Zero changes is a valid result: say "No data map changes needed."
