# Walkthrough (v0.1 self-review)

Done on 2026-11-16. Each of the 6 flow skills and `question-types` was read as an agent would read it, then every eval case was walked step by step. Each row is an ambiguity or contradiction found, and the fix made.

## /setup-data-work

| # | Case | Found | Fix |
|---|---|---|---|
| S1 | case 2 | A map already exists. It was unclear whether the setup mode question still applies | Start step 2: step 0 still applies to anything new |
| S2 | case 4 | Option A lists connectors, but the hard rule bans options built from visible connectors | Step 0 A: "the only place where connector names may be listed, and only after the user chose A" |
| S3 | case 1, 3 | The user's first message already answers the mode. Asking again would repeat a question | Step 0: say which mode was understood and continue. Never infer the mode from visible connectors |
| S4 | chat app | The `.gitignore` step has no repo to write to | Output step 2: give the user the line to add |

## /grill-the-ask

| # | Case | Found | Fix |
|---|---|---|---|
| G1 | case 3 | A clear, quick ask with no map would stall on the setup offer | Start step 2: at quick depth, make the offer in one line and continue with B |
| G2 | case 3 | The End block updates files that quick depth does not have | End: quick depth skips the file steps |
| G3 | case 1 | Depth sets the number of rounds, but depth was proposed after the rounds | Step 5: propose depth after round 1. Quick stops asking |
| G4 | case 2 | An ask that wants a cause gave no prompt to ask about the comparison | Step 4: ask what comparison exists |
| G5 | case 4 | Output said "create `data-work/...`", which a chat sandbox would follow and call saved | Output split: coding agent saves, chat app hands over |
| G6 | all | The depth table's Files row listed `readout.md`, which this step does not write | Note under the table |
| G7 | all | A stray line in Output was not a bullet | Fixed |

## /plan-analysis

| # | Case | Found | Fix |
|---|---|---|---|
| P1 | case 1 | The user confirmed a method before its card was checked against the data | Steps reordered: load cards, drop misfits, list options, recommend |
| P2 | case 1 | This step can find that the type cannot hold, but the revision log was only for later steps | Step 4 and Plan revisions: this step logs it too and lowers the type |
| P3 | case 2 | The fan-out trap is in the map, but the spec list had no place for joins | Spec list: joins line |
| P4 | case 3 | Quick depth versus the 8 steps | Quick: one line, no options, no file |
| P5 | all | "Check Data needed" could be read as "query the data", against "Do not run queries" | Step 2: ask the user, do not query |

## /run-analysis

| # | Case | Found | Fix |
|---|---|---|---|
| R1 | case 2 | "Reconcile" was both rung 5 and step 5 | Step 3 is rungs 1 to 4. Step 5 is rung 5 |
| R2 | case 2 | Nothing said what to do with a gap above tolerance | Step 5: record fail, do not report as final, test causes one at a time |
| R3 | case 1 | A failed rung that needs a choice: stop or go on? | Step 3: propose, add an assumption row, ask |
| R4 | case 3 | The goal sentence names a readout that quick depth does not write | Quick goal wording added |
| R5 | all | Is a source in `DATA-MAP.md` "named by the user"? | Hard rules: names in the user's own files count. Ask if the matching tool is unclear |
| R6 | all | Status wording said the run sets `reviewed` | Fixed in fix D |

## /review-analysis

| # | Case | Found | Fix |
|---|---|---|---|
| V1 | case 1 to 3 | A pasted analysis has no Meta, no depth and no Progress line | Start step 4: review at standard depth |
| V2 | case 1 to 3 | The End block would create files for a pasted analysis | End step 3: the review in chat is the output |
| V3 | case 4 | When may the readout be marked final? | Readout review step 5: only with `ready` or `ready with caveats` |
| V4 | case 3, 4 | A reviewer might rewrite a sound readout for taste | Readout review step 3: leave passing sentences unchanged |

## /retro-analysis

| # | Case | Found | Fix |
|---|---|---|---|
| T1 | no map | Option B starts a map, but the template may not load | Start step 2: section names listed inline |
| T2 | case 3 | The End block at quick depth | End: quick depth skips the file steps |

## question-types

| # | Case | Found | Fix |
|---|---|---|---|
| Q1 | case 2 | One treated market also fits "rollout with a comparison group", which comes first | Selector step 2 says "several units". Tie-break: one treated unit goes to step 4 |
| Q2 | case 3 | A cut-off rule also fits step 2 | Tie-break: a score cut-off goes to step 3 |
| Q3 | case 5 | Self-selected treatment with a pre-period also fits step 2 | Tie-break: self-selection goes to steps 6, 7 or 9 |
| Q4 | case 5 | A randomised nudge could be read as step 1 | Tie-break: the nudge is an instrument when the question is about what it nudges |
| Q5 | all | Two short cards carry a tool note, outside the stated short format | `SKILL.md`: a short card may add a one-line tool note |
| Q6 | case 4 | When a check fails, what is left? | `causal.md` "Before any card": the claim drops to descriptive, with a plan revision |

## Not fixed

- Triggering cannot be tested by reading. It needs the manual runs in `evals/README.md`.
- Whether a chat app offers a real download depends on the app. The skills fall back to one printed block.
