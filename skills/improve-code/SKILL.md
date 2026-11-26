---
name: improve-code
description: Review and improve SQL or Python used for data work, in a fixed order (intent, correctness, style, performance), with a surgical diff and a proof that results did not change. Use only when the user runs /improve-code or explicitly asks to improve, review or refactor a data query or analysis script.
---

# /improve-code

Correct first, clear second, fast third. Change only what is needed, and prove nothing else moved.

Experimental (v0.2).

## Hard rules

- Never call a connector or data tool until the user has named the source it applies to. Never build answer options from the connectors you can see. Offer generic options: warehouse or database, data lake, product analytics tool, spreadsheet or file, API, not sure, other.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead. Names in the user's own code or `DATA-MAP.md` count as said by the user.
- Never run the user's code against a source the user has not named. Once the user has attached the data or named the source in this chat, running the checks is part of the job: do not stop to ask first (see "Prove equivalence").
- **Stay in scope.** Report on the code only. Make no findings about the data or the business, and never word a claim above the claim ceiling. If the analysis behind the code says no trend can be claimed, a comment or a summary of yours must not say a number "rose each month". The claim ceiling applies in every skill, not only in the flow.

## Start

1. Take the code: pasted, or a file path. Read all of it before saying anything.
2. Check for `DATA-MAP.md` (in `data-work/` in the current folder, then upward; in the Project files; or attached). Say in one line whether you found it. If found, read Tables (grain, keys), Joins (traps), Rules (mandatory filters) and Conventions. If not found, continue without it and ask about grain and style when you need them. Do not offer setup here.
3. **Use what is already known.** Read the map and, when the code belongs to an analysis, `analysis.md`. Facts already checked there (nulls, ties, grain, join match rates) are used, not reported as "not checked". Say where each fact came from.
4. This step needs no `analysis.md`. If the code belongs to an analysis folder (it sits in `scripts/`), say so and read the Analysis table spec for the intended grain.

## Rules from the disciplines (in case they do not load)

- `shaping-data`: grain first. Count rows before and after every join. A left join followed by a filter on the right table becomes an inner join. Decide nulls and duplicates on purpose. Half-open date ranges, one time zone.
- `validation-ladder`: one entity, one entity-day, many entities, aggregates, reconcile to a trusted number. State the expected result before each check.
- `run-or-hand-over`: two separate questions. Can I run things here? Always try first: a code tool or sandbox with attached files counts (load them and run SQL with DuckDB or SQLite, or pandas). Hand over only when no code tool exists, and say so in one line. Where do files persist? In a chat app, save each file at its full `data-work/` path in the Project files if you can, otherwise create it and offer a download, and say which; print it only if that fails. Never ask the user to edit a saved file by hand. Numbered queries (`Q1.1`), one purpose line, expected result first, "Paste the result here." Never call a data tool before the user names the source.
- `data-map`: use the map's grain, keys, traps, mandatory filters and Conventions. Flag entries older than 90 days or contradicted by data, then ask.

## Order of work

Do the four passes in this order. Do not start a later pass while an earlier one has an open question.

### 1. Intent

- Say in one or two lines what the code is meant to produce: the grain of the output, the measures, the period.
- If you cannot tell, ask (one round, at most 3 questions, each with options and one real recommended default). Do not guess the intent and then "fix" the code toward your guess.
- Ask the dialect or the library if the code and the map do not show it.

### 2. Correctness

Check each of these. Raise one only if the code gives a reason.

- **Grain:** what is one row after each step? Does the final grain match the intent?
- **Join fan-out:** is any join one-to-many, with a sum or count taken after it? Is the key unique on the "one" side?
- **Join type and filters:** does a `where` on the right table of a left join turn it into an inner join?
- **Filters:** are the mandatory filters from the map applied? Do both sides of a comparison use the same filters?
- **Nulls:** `not in` with nulls, `count(column)` against `count(*)`, null in a join key, null in arithmetic, averages that skip nulls.
- **Time zones and dates:** one time zone. Half-open ranges. `between` on a timestamp drops most of the last day. Truncation in the right zone.
- **Dedup:** `distinct` hiding a fan-out; `row_number` with no tie-break; duplicates in a key that should be unique.
- **Division:** integer division, divide by zero.
- **Python:** a merge with no `validate`, chained assignment, mutation of an input frame, a random step with no seed, dates read as strings.

For each bug: say what it does to the result, and how big the effect could be if you can tell.

**Surface problems, do not hide them.** Prefer a check that makes a mismatch visible (for example the row count and match rate per side of a join, shown in the output) over a filter that quietly masks it. A filter that drops unmatched rows is a change of result: say so and show how many rows it drops.

### 3. Style

- The Conventions section of `DATA-MAP.md` wins. Otherwise sqlstyle.guide for SQL and PEP 8 for Python.
- **Keep reusable code reusable.** Do not pin fixed dates, windows or one-off values into a shared query. Use a parameter or a named input, and keep the default open. A quarter written into a reusable map query is a bug in waiting.
- Only fix style that hurts reading: unclear names, nested subqueries where a named step is clearer, `select *` in a final query, magic numbers.
- Do not reformat lines you are not otherwise changing, unless the user asks for a full restyle. A restyle goes in its own diff, separate from logic changes.

### 4. Performance

Only after correctness. Dialect-aware. Ask the dialect if unknown.

- Filter on the partition or date column, as early as possible.
- Select only the columns needed.
- Avoid repeated scans of the same large table: compute once in a named step and reuse it.
- Aggregate before joining when the grain allows it.
- Python: vector operations over row loops; read only the needed columns; avoid repeated full copies.
- Do not trade clarity for speed unless the user says the code is too slow. Say what you expect to gain. Do not promise a number you have not measured.

## Show the change

1. **A diff.** Unified format, only the lines that change, with enough context to place them.
2. **One line per change, saying why.** Tag each: `[bug]`, `[style]` or `[perf]`.
3. **Surgical.** Do not rename, reorder or restructure beyond what a listed change needs. If a larger rewrite is worth it, propose it separately and wait for a yes.
4. Keep the user's dialect, library and conventions.

## Prove equivalence

For every `[style]` and `[perf]` change, behaviour must not change. Prove it with check queries, through `run-or-hand-over`:

- Row count before and after.
- Totals of each measure before and after.
- For a keyed result: rows in one version and not in the other (both directions). Expected: zero.

**Verify by running when you can.** If you can run code and reach the data (attached files, or a source the user named), run the old and the new version yourself and show that they give the same result, in the same reply. Do not stop to ask first. Only when you cannot run them (no code tool, or the data is not reachable), hand the checks over.

State the expected result first ("Expect: equal row counts, equal totals, zero rows in the difference"). If you cannot run them, hand them over numbered and wait for the paste. Do not say "equivalent" before the checks pass. Until then say "not yet verified".

For a `[bug]` change, behaviour changes on purpose. Say so plainly. Show the difference: the same checks, with the expected direction and, if you can, the size ("Expect: order count falls, because cancelled orders no longer count"). The user confirms the new behaviour is the intended one.

Keep bug fixes and behaviour-preserving changes apart, so each can be checked on its own.

## End

1. Coding agent: if the user asked you to edit the file, save it and say where. Save check queries next to it, or in `scripts/` when the code lives in an analysis folder. If the code belongs to an analysis, add a line to its Progress line.
2. Where do files persist? Decide by situation, not by file access. If there is no user project folder (no `data-work/` and no repo), you are in a chat app. This is only about files: a chat app with a code tool still runs checks itself.
3. Chat app: give the improved code as one block, and create it as a file. Name its full path (for an analysis: `data-work/analyses/<YYYY-MM-DD>-<slug>/scripts/<file>`) and say what happened to it: "Saved to `<path>` in your Project files", "Download `<file>`", or "Printed below; save it as `<path>`". Never claim a save that did not happen.
4. If the change fixed a trap worth remembering (a fan-out, a missing mandatory filter), suggest `/retro-analysis` to add it to the data map. Do not edit the map here.
5. **Close the loop.** When a check changes what is known about shared code (it was untested, tested only on a translation of the data, or it failed), offer to record that where the team keeps the code: the Key queries entry in the map (through `/retro-analysis`), or the team's own place. Say what the new status would be.
6. **Offer candidates.** If the code or an analysis folder holds a script that other people would reuse, offer it as a candidate for the map's Key queries, not only the queries the map already lists. The user decides. Do not edit the map here.

## Done when

The user has the diff, the reason for each change, and either passed equivalence checks or numbered checks to run.

## Precision

- If the code is sound, say "No changes needed" and give at most 2 optional suggestions, labelled optional.
- Do not invent bugs. Do not restyle for taste.
- Critique the code, never the person.
