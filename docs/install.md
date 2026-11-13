# Install

The skills use plain `SKILL.md` files with standard frontmatter. Any agent that reads them works.

## Quick path (most agents)

```bash
npx skills add caltunay/data-skills
```

Pick your agent when asked. This copies the skills into the agent's skills folder.

## Claude Code

```bash
npx skills add caltunay/data-skills
```

Or copy the folders in `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

## Codex

Copy the folders in `skills/` into your Codex skills folder (for example `~/.codex/skills/` or `.agents/skills/`). Check the current Codex docs for the exact folder. Or use the `npx` command and pick Codex.

## Gemini CLI

Use the `npx` command and pick Gemini CLI, or copy the folders into the skills folder your Gemini CLI version reads. Check its current docs for the exact folder.

## Cursor

Use the `npx` command and pick Cursor, or copy the skills into the folder Cursor reads for agent skills. If your version has no skills folder, paste the `SKILL.md` text into a project rule.

## GitHub Copilot

Use the `npx` command and pick Copilot, or copy the skills into the folder Copilot reads for agent skills. If your version has no skills folder, paste the `SKILL.md` text into custom instructions.

## claude.ai

1. Build the ZIPs: run `scripts/package-zips`. One ZIP per skill appears in `dist/`.
2. In claude.ai, open Settings, then Capabilities (or Skills), and upload each ZIP.
3. Upload all 15. The flow skills call the others by name.
4. Create a Project for your data work. Put your `DATA-MAP.md` in the Project files.

## ChatGPT

1. Build the ZIPs with `scripts/package-zips` as above.
2. Upload each ZIP where your ChatGPT plan supports skills.
3. If your plan has no skill upload, paste the `SKILL.md` of the skill you need into a Project's instructions, or the chat itself.
4. Put `DATA-MAP.md` in the Project files.

## Chat apps: how files work

- Chat apps cannot write to your project. The analysis lives in the chat.
- At the end you get `analysis.md` as a download, or as one block to copy.
- `/retro-analysis` gives you a full updated `DATA-MAP.md`. Replace the Project file with it.

## First run

1. Run `/setup-data-work` once.
2. For each ask, run `/grill-the-ask`, then the rest of the flow.

## Updating

Skills never touch your `data-work/` files. Update by re-running the install command.

## Packaging ZIPs

```bash
scripts/package-zips
```

The ZIPs go in `dist/`, which is gitignored.
