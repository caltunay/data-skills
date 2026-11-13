# Evals

Pre-release check, run by hand by the maintainer.

- Each flow skill has 3 cases and a rubric: 2 with planted flaws or ambiguities, 1 clean case that tests precision.
- Run each case in Claude Code, Codex, Gemini CLI and claude.ai. Record results in `results/<date>-<agent>.md`.
- Then run 3 real asks on public data, end to end.
- Also check triggering: user-invoked skills must not fire on their own, and disciplines must fire when they should.
- All data in this folder is invented.

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
| "Run my planned analysis" with no command | Flow skills do not fire on their own |
| "Is this join safe?" | `shaping-data` and `validation-ladder` may apply |
| "Which test for two conversion rates?" | `stats-tests` applies |
| A pasted analysis with the word "caused" | `question-types` applies. `/review-analysis` does not fire |
