# Evals

Pre-release check, run by hand by the maintainer.

- Each flow skill has at least 3 cases and a rubric: 2 with planted flaws or ambiguities, 1 clean case that tests precision.
- Extra cases: `setup-data-work` case 4 (several connectors visible), `grill-the-ask` case 4 (chat app, no project folder), `review-analysis` case 4 (draft readout with one overclaiming sentence), `grilling` case 1 (a non-data vague ask: must not fire).
- `question-types` has 6 method-choice cases. They grade the method chosen and the checks named, not calculations.
- Every flow rubric also checks: no connector call before the source is named, the data map check is announced, the chat-app download is offered, and no names the user did not say.
- Run each case in Claude Code, Codex, Gemini CLI and claude.ai. Record results in `results/<date>-<agent>.md`.
- Then run 3 real asks on public data, end to end.
- Also check triggering: user-invoked skills must not fire on their own, and disciplines must fire when they should.
- All data in this folder is invented. One domain only: an online shop and a subscription app.

## Chat-app tests

Run every chat-app test in an incognito (temporary) chat, with a neutral profile: no memory, no custom instructions, no personal preferences. Otherwise names and habits from your profile leak into the answers and hide real failures of the "no invented names" check. Connect two or three data tools you do not plan to name, so the "no early tool call" check has something to catch.

## Result file format

```
# Results: <date>, <agent>

| skill | case | pass or fail | notes |
|---|---|---|---|
```

## Trigger checks

| Prompt (no slash command) | Expected |
|---|---|
| "Here is a vague ask: why are sign-ups down?" | `grilling` may apply. `/grill-the-ask` does not fire |
| "Write a SQL query for monthly sign-ups" | None of our skills fire. A built-in data skill may |
| "Can you help me sort out the team offsite? Not sure where to start." | `grilling` does not fire (not a data ask). See `grilling/case-1.md` |
| "Run my planned analysis" with no command | Flow skills do not fire on their own |
| "Is this join safe?" (inside a flow step) | `shaping-data` and `validation-ladder` apply |
| "Which test for two conversion rates?" (inside a flow step) | `stats-tests` applies |
| A pasted analysis with the word "caused" | `question-types` applies. `/review-analysis` does not fire |
