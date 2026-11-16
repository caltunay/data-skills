# Self-check

Run with `scripts/self-check`. Last run: 2026-11-16, v0.1 fix pass, with the private `.blocklist` present. Result: all pass.

| # | Check |
|---|---|
| 1 | Every SKILL.md frontmatter has only `name` and `description` |
| 2 | No links between skill folders (no `../`, no `skills/<name>/` paths) |
| 3 | No em dashes anywhere |
| 4 | The reserved product name appears only in SPEC.md and DECISIONS.md |
| 5 | No text telling the agent to use a named tool of one agent |
| 6 | Every user-invoked description says "Use only when the user runs /<name> or explicitly asks to" |
| 7 | Skill `name` matches its folder |
| 8 | Every required file exists (SPEC section 16 plus the v0.1 additions) |
| 9 | Every SKILL.md is under 500 lines |
| 10 | Both copies of `analysis.template.md` and of `readout.template.md` match |
| 11 | The skill folders match the catalogue |
| 12 | No credentials in any file |
| 13 | Every skill holds the "no names the user has not said" rule |
| 14 | Every user-invoked skill holds the "name the source first" rule |
| 15 | Flow skills have the start check, the end handoff, the chat-app definition and the Progress line. Setup asks the setup mode question |
| 16 | Each flow skill restates the core rule of every discipline it calls |
| 17 | Method cards: full cards have all 8 fields. Short cards have 4 fields and end with the specialist line |
| 18 | The method catalogue matches SPEC section 10.2 (card counts per type file) |
| 19 | The assumptions table has all 7 columns |
| 20 | Every eval case is marked as invented data |
| 21 | Private blocklist: no banned word anywhere outside `.git` (skipped when `.blocklist` is absent) |
| 22 | Private files are not tracked by git |

## Private blocklist

`.blocklist` is gitignored. It holds one banned word per line. The check is whole-word and ignores case. The words are never written in this repo. Without the file the check prints SKIP, so a public clone still passes.

## Manual checks done

- Every eval case was walked through its skill. See `docs/walkthrough.md`.
- `scripts/package-zips` builds one ZIP per skill into `dist/` (gitignored).

## Not checked (needs the maintainer)

- Running the evals by hand in Claude Code, Codex, Gemini CLI and claude.ai, in incognito with a neutral profile.
- The 3 real asks on public data.
- Trigger checks (user-invoked skills must not fire on their own; a generic SQL ask must not trigger ours).
- Whether `npx skills add` installs the flat layout.
- sqlstyle.guide license.
