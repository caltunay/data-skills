# Self-check

Run with `scripts/self-check`. Last run: 2026-11-18, v0.3 fix pass, with the private `.blocklist` present. Result: all pass (28 checks). It also runs on every pull request and push (`.github/workflows/self-check.yml`).

| # | Check |
|---|---|
| 1 | Every SKILL.md frontmatter has only `name` and `description` |
| 2 | No links between skill folders (no `../`, no `skills/<name>/` paths) |
| 3 | No em dashes anywhere |
| 4 | The reserved product name appears only in SPEC.md and DECISIONS.md |
| 5 | No text telling the agent to use a named tool of one agent |
| 6 | Every user-invoked description says "Use only when the user runs /<name> or explicitly asks to" |
| 7 | Skill `name` matches its folder |
| 8 | Every required file exists (SPEC section 16, the v0.1 additions, and the v0.2 skills, examples, runner, workflows and templates) |
| 9 | Every SKILL.md is under 500 lines |
| 10 | Both copies of `analysis.template.md` and of `readout.template.md` match |
| 11 | The skill folders match the catalogue |
| 12 | No credentials in any file |
| 13 | Every skill holds the "no names the user has not said" rule |
| 14 | Every user-invoked skill holds the "name the source first" rule |
| 15 | Flow skills and flow-style v0.2 skills have the start check, the end handoff, the chat-app definition and the Progress line. Setup asks the setup mode question |
| 16 | Each flow skill restates the core rule of every discipline it calls |
| 17 | Method cards: full cards have all 8 fields. Short cards have 4 fields and end with the specialist line |
| 18 | The method catalogue matches SPEC sections 10.2 and 20.7 (card counts per type file) |
| 19 | The assumptions table has all 7 columns |
| 20 | Every eval case is marked as invented data and has a "Simulated answers" section |
| 21 | Private blocklist: no banned word anywhere outside `.git` (skipped when `.blocklist` is absent) |
| 22 | Private files are not tracked by git |
| 23 | The four plugin manifest files are valid JSON with one name and one version |
| 24 | Every v0.2 skill is marked experimental in the README and in its own file |
| 25 | Every flow skill ends with the go-ahead question (A, B and C) |
| 26 | `validation-ladder` lists the 8 data-check floor checks, and no skill or SPEC line says quick depth skips them |
| 27 | `question-types/SKILL.md` has a compact fallback row for every method card, with 4 filled cells |
| 28 | The templates carry the Review pack, the bold status label, at most 3 callouts (Answer, Caveat, Ask) and the Appendix |
| 29 | The analysis template has Decisions, Hypotheses, Setup choice, Goal link and Files |
| 30 | The data map template has Goals, Funnels, Key queries (as SQL) and Ways of working |
| 31 | Every template starts with `format: v1` and an `updated:` line |
| 32 | The experiment spec and metric spec templates hold their required fields |
| 33 | The routing guide is in the README and in `ask-data-skills` |
| 34 | The v0.4 rules are in the skills: retro never offers setup, the stuck rule, no analysis in the grill, the hypothesis tree, the skeleton, the `.docx`, the three save forms |
| 35 | v0.5 files: every flow skill has the three save forms, the bare-name rule and the stale copies rule; no v0.4 file names or save wording anywhere |
| 36 | `/wayfinder-data` ends with the go-ahead question and saves specs in their own analysis folder |
| 37 | The hypothesis status rule is in `plan-analysis`, `run-analysis` and `review-analysis`, and the review fixes statuses with a "was" and "now" pair |
| 38 | The README has the chat-app section, and the Project instructions block matches in the setup skill and `docs/where-to-run.md` |
| 39 | Question cards, the continue-or-new question and the earlier-work hint are in the skills |

## Private blocklist

`.blocklist` is gitignored. It holds one banned word per line. The check is whole-word and ignores case. The words are never written in this repo. Without the file the check prints SKIP, so a public clone still passes.

## Manual checks done

- Every eval case was walked through its skill. See `docs/walkthrough.md`.
- `scripts/package-zips` builds one ZIP per skill into `dist/` (gitignored): 22 ZIPs.
- `claude plugin validate .` passes for the plugin and the marketplace file.
- Both worked examples were produced by running their queries. The eval runner was run in dry-run mode (56 cases after v0.4).
- v0.5: checks 35 to 39 were added, and each was tested by breaking its rule once. The eval runner was run in dry-run mode (61 cases after v0.5).
- v0.4: checks 29 to 34 were added. Each needs the template copies to match, so `scripts/package-zips` and check 10 compare the two spec templates too.
- v0.3: checks 25 to 28 were tested by breaking each rule once (a removed compact row, a renamed floor check, a missing go-ahead line); each failed as expected, then passed after the restore. The sign-up example queries were re-run; `outputs/results.txt` changed by additions only.

## Not checked (needs the maintainer)

- Running the evals by hand in Claude Code, Codex, Gemini CLI and claude.ai, in normal chats (not incognito) with a neutral profile.
- The 3 real asks on public data.
- Trigger checks (user-invoked skills must not fire on their own; a generic SQL ask must not trigger ours).
- Whether `npx skills add` installs the flat layout.
- sqlstyle.guide license.
- A real run of the eval runner (needs an API key).
- The two GitHub workflows on GitHub itself. The release workflow needs a published release to fire.
- The Codex install command.
