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

1. Check for `DATA-MAP.md` and `analysis.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line what you found, and which map you read. A team map can sit above project maps: the nearest map wins for conflicts.
2. If there is no `DATA-MAP.md`, first ask: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." If the Project holds earlier analyses but no map, make the first option "Yes, attach it (recommended: earlier analyses are here)", never "No", and say: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." If yes, extend that map. If not, this retro builds the map itself from the template, with only the entries you approve. Never offer `/setup-data-work` here, whatever Meta says. The template is `DATA-MAP.template.md` in the `data-map` skill. If it is not available, start with `format: v1` on line 1 and these sections: Sources, Tables, Joins, Metrics, Rules, Gotchas, Glossary, Conventions.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before re-asking anything. At quick depth there is no file: ask for a short summary of what was learned. Match the analysis to the ask by its folder or slug (`data-work/analyses/<YYYY-MM-DD>-<slug>/`). If more than one analysis could be the one, ask which. Never resume one silently.
4. Read the Progress line in Meta and resume from it. Then read all sections, especially Assumptions, Results and Review. When resuming, refresh every line that is now out of date before you go on, and show each as a "was" and "now" pair. Examples: "no DATA-MAP.md, so inline" in Meta after a map now exists, an old hint in the claim ceiling line, a Progress line that points at a finished step.

## Rules from the disciplines (in case they do not load)

- `data-map`: change the map only through approved retro changes. Tidy a messy map to the template as one approved change. Key queries are saved as SQL text. One entry per source; grain and keys under Tables; the template's table layout, never loose bullets. Conventions hold style only; analysis rules go in Rules or Gotchas; no duplicates across sections. Each entry has `verified: YYYY-MM-DD` and `source: analyses/<slug>`. Flag entries older than 90 days or contradicted by data, then ask. Check the format version and offer a migration if old.

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
   - a **funnel** (each step, its event or table, the step definition) or a **key query** (what it returns and when to use it) that the next analyst would reuse. Propose additions to the Funnels and Key queries sections. Save each key query as SQL text (the exact query from the Review pack, in the team's SQL conventions, with its columns checked against the Tables section), with what it returns and when to use it. A description alone is not a key query. Keep key queries to 3 to 5 in total
   - a join that this run **checked** by query: propose changing its status from `unverified` to `checked`, with what the query found
2. **Tidy the map.** If the map is not in the template's layout, propose one change called "Tidy" and show it as a diff: one entry per source (split a bullet that lists several files or tables as one source), grain and keys under Tables for every table this analysis used (take them from `analysis.md`; if they are not there, leave the cell empty and say so, never guess), the template's tables instead of loose bullets, and a Ways of working section. The user approves it like any other change.
3. Check existing entries: did the data contradict any? Is any older than 90 days and re-confirmed by this work? Propose updating its `verified` date.
4. Put each entry in the right section:
   - Conventions hold style only: SQL style, Python style, naming. Nothing else.
   - Analysis rules (a filter, an exclusion, a dedup rule, a time zone rule) go in Rules. Mistakes and traps go in Gotchas.
   - Sources: one entry per source, one row each. Grain, keys and key facts go under Tables, not Sources.
   - Follow the template's table layout (the same columns, one row per entry). Never write loose bullets in place of a table row. When this retro builds the map, copy the template's sections and columns exactly.
   - One fact goes in one section. No duplicate entries across sections. If a fact fits two, pick one and leave the other out.
5. Propose changes as a short numbered list. Each one: section, the exact entry, and why it is worth keeping. The reason must be true for this run: quote the line in `analysis.md` that shows it (a failed rung, a Plan revisions row, a review issue). If nothing in this run shows it cost time or changed a number, do not say it did.
6. Show a diff (old and new text) for each change.
7. The user approves each change: yes, no or edit. Do not apply unapproved changes.
8. Apply the approved changes, with today's date as `verified` and `source: analyses/<slug>`.
9. Record the proposals and the decisions in the Retro section of `analysis.md`. Set status `retro done` and update the Progress line.

## Keep out

- One-off details of a single analysis.
- Row-level data, credentials, personal data.
- Opinions. Entries are facts the data supports.
- Reasons that did not happen in this run. "This cost a rung" only if the ladder log shows a failed rung for it.

## Output

- Coding agent: edit `data-work/DATA-MAP.md` in place with approved changes only.
- Chat app: save the full updated map at `data-work/DATA-MAP.md` (with `format: v1` and a fresh `updated:` line), never under a bare name, and say exactly what happened to it (the three forms in End step 3). Name any stale older copy of the map. Never ask the user to edit the map by hand.
- If the map is not `format: v1`, show the migration first and apply it only after approval.

## End (every flow step)

Quick depth has no files: skip steps 1, 3, 4 and 5, give the result in the chat, and name the next step.

1. Update the Progress line in `analysis.md` Meta.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Save each file at its full path, never a bare file name (a bare name lands in a `claude/` folder in claude.ai, and a generic name is overwritten by the next analysis): `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md` (and `readout.md` in the same folder when it exists). Then say exactly what happened to each file, in one of three forms: "Saved to `<path>` in your Project files" (you wrote it there), "Download `<file>` and add it to your Project at `<path>`" (you could not write to Project files), or "Printed below; save it as `<path>`" (creating the file failed). Never claim a save that did not happen. Never say "replace the old one, it is already saved there". Start each file with `format:` and `updated: YYYY-MM-DD HH:MM` (now). Hand back the whole file, never a patch. Never ask the user to edit a saved file by hand.
4. Stale copies: if an older copy of a file exists elsewhere in the Project (for example `analysis (6).md` at the top level, or a file in `claude/`), name it and say it is stale. Once per Project, suggest moving old analyses into the `data-work/` layout. If two copies exist, use the newest `updated:` and say so.
5. Coding agent: the files are already saved under `data-work/`. Name each path.
6. In a chat app, also hand back the full updated `data-work/DATA-MAP.md` in one of the three forms (step 3).
7. The flow is complete. End with the go-ahead question, at every depth, quick included, adapted to this last step:

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
