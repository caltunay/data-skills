---
name: handoff
description: Write handoff.md for an analysis so a colleague or a fresh session can pick it up, covering where it stands, what is done, decisions made, open assumptions, the next step and how to resume. Use only when the user runs /handoff or explicitly asks to hand an analysis over or to write a handoff note.
---

# /handoff

Someone else continues from here. Give them what they need, and nothing they must guess.

Experimental (v0.2).

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. This step calls none.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own `DATA-MAP.md` or `analysis.md` count as said by the user.
- Report only what the files and this conversation show. Do not write "validated" for a rung with no logged result. Do not write "done" for a step whose section is empty.
- No row-level data, no credentials, no raw chat transcript in the handoff.

## Start (every flow step)

1. Check for `DATA-MAP.md`, `analysis.md` and `readout.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached), and list the files in `queries/` and `outputs/` if you can see them. Say in one line what you found.
2. No `DATA-MAP.md`: say so in the same line, and note it in the handoff. Do not offer setup here.
3. If `analysis.md` is expected but not found (for example, a new chat), ask the user to attach it before asking anything else. If there truly is none (quick depth, or work done outside the flow), build the handoff from the conversation and say that it has no `analysis.md` behind it.
4. Read the Progress line in Meta. It is the starting point of the handoff.

## Rules from the disciplines (in case they do not load)

- `assumptions`: list every high-impact row still `open`, with its alternatives and how to check it.
- `question-types`: state the question type and its claim ceiling, so the next person does not overclaim.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, create each file and offer it as a download; print it only if that fails. Never ask the user to edit a saved file by hand.

## Steps

1. Read every section of `analysis.md`, and `readout.md` if it exists.
2. Compare the Progress line with the sections. If they disagree (Progress says "run done" but the ladder log has empty rungs), say so and ask which is right. One question, then continue.
3. Ask who the handoff is for, only if it matters and is not known: A) a colleague, B) myself in a fresh session, C) both. Default: C.
4. Write `handoff.md` in the analysis folder, in the layout below.
5. Read it back as the receiver: could they continue without asking the author anything? Fix what fails that test.

## Layout of `handoff.md`

```
# Handoff: <analysis title>

Date:
From:           <role or name the user gave, else "the author">
For:            a colleague | a fresh session | both

## 1. Where things stand
Progress: <the Progress line, verbatim>
Status: <status from Meta>   Depth: <depth>   Question type: <type, with its claim ceiling in one line>
One paragraph: the ask, the clarified question, and the decision it feeds.

## 2. What is done
Per step (grill, plan, run, review, retro): done, part done, or not started. For "part done", say exactly where it stopped.
Ladder: each rung run, with pass or fail.
Method card checks: each, with pass or fail.

## 3. Decisions made
Each decision that shaped the work, with its reason: definitions, the chosen plan, depth, cleaning choices, plan revisions (with dates).

## 4. Open high-impact assumptions
The full 7-column rows for every high-impact assumption still open. Then other open rows, one line each.

## 5. Next step
The one next action, as a command to run or a check to make. Then what follows it.
Anything being waited for: a paste (which query), an answer (from whom, which question).

## 6. Files and their state
| file | state | note |
analysis.md, readout.md (draft or final), each file in queries/ (run or not run), each file in outputs/, DATA-MAP.md (present or not).

## 7. How to resume in a fresh session
1. Attach or open: <the files>.
2. Run: <the command from the Progress line>.
3. First thing it will need: <the paste or answer being waited for>.
Chat app: put the files in the Project files first.
```

Keep it to about one page. Link to `analysis.md` for detail. Do not copy it.

## End (every flow step)

1. Add the handoff to the Progress line in `analysis.md` Meta, for example `Progress: run step 3 of 7, waiting for Q3.1 paste; handoff written 2026-11-16`. Do not change the step it points to.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Chat app: create `handoff.md`, `analysis.md` (and `readout.md` when it exists) as files and offer them as downloads. Print one block only if creating a file fails. Never ask the user to edit a saved file by hand: hand back the updated file. Say: "Save these to your Project files, or send them together to your colleague."
4. Coding agent: `handoff.md` is saved in the analysis folder. Say where.
5. Name the next step: the command in section 5 of the handoff.

## Done when

`handoff.md` is written, matches the files, and the user has it.

## Do not

- Do not continue the analysis. This step only writes the handoff.
- Do not tidy up results or wording in `analysis.md` or `readout.md`.
- Do not hide a failed rung or an open assumption to make the handoff look clean.
