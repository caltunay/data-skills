# Evals

Pre-release check, run by hand by the maintainer. A runner (`runner/run.py`, see `runner/README.md`) automates a first pass. It approximates skill loading and does not test triggering, so the manual trigger checks below are still needed.

- Each flow skill has at least 3 cases and a rubric: 2 with planted flaws or ambiguities, 1 clean case that tests precision.
- Extra cases: `setup-data-work` case 4 (several connectors visible), `grill-the-ask` case 4 (chat app, no project folder), `review-analysis` case 4 (draft readout with one overclaiming sentence), `grilling` case 1 (a non-data vague ask: must not fire).
- v0.3 cases: `run-analysis` case 4 (chat app with a code tool and attached CSVs: must run the checks itself), `run-analysis` case 5 (a zero-day logging gap: must find it before any segment scan), `grill-the-ask` case 5 (a period comparison across a seasonal boundary: must flag seasonality), `retro-analysis` case 4 (must not put analysis rules under Conventions).
- v0.4 cases: `grill-the-ask` case 6 (an answer contradicts an earlier one: must switch to one question at a time), `grill-the-ask` case 7 (files attached with an obvious pattern: must report no findings), `plan-analysis` case 4 ("why did X drop" at standard depth: must write a hypothesis tree), `wayfinder-data` case 4 (design an A/B test: fast path, `experiment-spec.md`, no project map), `wayfinder-data` case 5 (define customer health: `metric-spec.md` with proxies and how to check them), `setup-data-work` case 5 (chat app: goals, funnels, key queries, an existing map first, the Project instructions block), `ask-data-skills` case 4 (a design ask routes to `/wayfinder-data`).
- `reference/signup-drop-claude-ai.md`: what a good manual run of the sign-up example caught, and what v0.3 fixed. Not graded by the runner.
- `question-types` has 8 method-choice cases (6 causal, 2 predictive). They grade the method chosen and the checks named, not calculations.
- Every flow rubric also checks: no connector call before the source is named, the data map check is announced, the chat-app download is offered, no names the user did not say, the go-ahead question at the end, no manual file edits, and downloads before printed blocks.
- Run each case in Claude Code, Codex, Gemini CLI and claude.ai. Record results in `results/<date>-<agent>.md`.
- Then run 3 real asks on public data, end to end.
- Also check triggering: user-invoked skills must not fire on their own, and disciplines must fire when they should.
- Every case has a "Simulated answers" section: what the user says in later turns, or "None needed". The runner plays them. By hand, use them as your replies.
- All data in this folder is invented. One domain only: an online shop and a subscription app.

## Chat-app tests

Run chat-app tests in normal chats, not incognito: Projects, saved files and downloads do not work the same in an incognito chat, so the v0.4 storage rules cannot be tested there. Keep the profile neutral where you can: no memory, no custom instructions, a test Project with no other files. Otherwise names and habits from your profile leak into the answers and hide real failures of the "no invented names" check. Connect two or three data tools you do not plan to name, so the "no early tool call" check has something to catch.

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
