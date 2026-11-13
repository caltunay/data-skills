# Self-check

Run on 2026-11-13 with `scripts/self-check`. Result: all pass.

| Check | Result |
|---|---|
| Every SKILL.md frontmatter has only `name` and `description` | PASS |
| No links between skill folders (no `../`, no `skills/<name>/` paths) | PASS |
| No em dashes anywhere (SPEC.md excluded: it is kept unchanged as the source of truth) | PASS |
| The reserved product name appears only in SPEC.md and DECISIONS.md | PASS |
| No text telling the agent to use a named tool of one agent | PASS |
| Every flow skill description says "Use only when the user runs /<name>" | PASS |
| Skill `name` matches its folder | PASS |
| Every file in SPEC section 16 exists | PASS |
| Every SKILL.md is under 500 lines | PASS |
| The two copies of `analysis.template.md` match | PASS |
| 15 skills exist | PASS |
| No credentials in any file | PASS |

## Manual checks done

- Each flow skill restates the core rule of every discipline it calls, per the call lists in SPEC 6.1.
- Each flow skill reads `analysis.md` first and follows the depth table in SPEC section 4.
- Evals: 3 cases and a rubric for each of the 6 flow skills. Each skill has 1 clean case.
- `scripts/package-zips` builds 15 ZIPs into `dist/` (gitignored).

## Not checked (needs the maintainer)

- Running the evals by hand in Claude Code, Codex, Gemini CLI and claude.ai.
- The 3 real asks on public data.
- Trigger checks (user-invoked skills must not fire on their own).
- Whether `npx skills add` installs the flat layout. Not testable from this session.
- sqlstyle.guide license (site not reachable from this session).
