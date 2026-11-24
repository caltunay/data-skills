# Install

The skills use plain `SKILL.md` files with standard frontmatter. Any agent that reads them works.

## Quick path (most agents)

```bash
npx skills add caltunay/data-skills
```

Pick your agent when asked. This copies the skills into the agent's skills folder.

## Claude Code

As a plugin, in one line inside Claude Code (version 2.1.275 or later):

```
/plugin install data-skills --marketplace caltunay/data-skills
```

Or in two steps from your shell:

```bash
claude plugin marketplace add caltunay/data-skills
```

```bash
claude plugin install data-skills@data-skills
```

Installed as a plugin, the commands carry the plugin name: `/data-skills:grill-the-ask`, `/data-skills:plan-analysis`, and so on. They are the same commands.

Without the plugin: `npx skills add caltunay/data-skills`, or copy the folders in `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project). Then the commands have no prefix.

The manifests are `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. Check them with `claude plugin validate .`.

## Codex

The repo ships a Codex plugin manifest (`.codex-plugin/plugin.json`) and a marketplace file (`.agents/plugins/marketplace.json`), in the same shape as the plugins in the public `openai/plugins` repo.

1. Add this repo as a plugin marketplace in Codex.
2. Install `data-skills` from it.

The likely one-line form is below. It was not verified from the build session, because the Codex docs site was not reachable. Check `codex plugin --help` or the current Codex docs if it fails.

```bash
codex plugin marketplace add caltunay/data-skills
```

Without the plugin: use the `npx` command and pick Codex, or copy the folders in `skills/` into your Codex skills folder (for example `~/.codex/skills/` or `.agents/skills/`). Check the current Codex docs for the exact folder.

## Gemini CLI

Use the `npx` command and pick Gemini CLI, or copy the folders into the skills folder your Gemini CLI version reads. Check its current docs for the exact folder.

## Cursor

Use the `npx` command and pick Cursor, or copy the skills into the folder Cursor reads for agent skills. If your version has no skills folder, paste the `SKILL.md` text into a project rule.

## GitHub Copilot

Use the `npx` command and pick Copilot, or copy the skills into the folder Copilot reads for agent skills. If your version has no skills folder, paste the `SKILL.md` text into custom instructions.

## claude.ai

1. Get the ZIPs: download them from the latest release on GitHub (one ZIP per skill is attached to every release). Or build them: run `scripts/package-zips`, and one ZIP per skill appears in `dist/`.
2. In claude.ai, open Settings, then Capabilities (or Skills), and upload each ZIP.
3. Upload all of them. The flow skills call the others by name.
4. Create a Project for your data work. Put your `DATA-MAP.md` in the Project files at `data-work/DATA-MAP.md`.

## ChatGPT

1. Get the ZIPs from the latest release, or build them with `scripts/package-zips`, as above.
2. Upload each ZIP where your ChatGPT plan supports skills.
3. If your plan has no skill upload, paste the `SKILL.md` of the skill you need into a Project's instructions, or the chat itself.
4. Put `DATA-MAP.md` in the Project files at `data-work/DATA-MAP.md`.

## Chat apps: how files work

- A chat has no project folder, so the skills treat it as a chat app for files.
- Running is a separate question. If the chat has a code tool and you attach data files (CSV, Excel), the skills load them and run the checks themselves (DuckDB, SQLite or pandas). They hand queries over only when there is no code tool, and say so.
- Every flow step ends by saving the files it changed at their full paths under `data-work/`, and says exactly what happened to each. If it cannot write to the Project files, it offers a download and tells you where to add it. A block to copy is the fallback only if a file cannot be made.
- You never edit a saved file by hand. After you confirm a change, the skill hands back the updated file.
- Add each download to your Project at the path the skill names. The next step, in any chat, reads it from there.
- If a step cannot find `analysis.md`, it asks you to attach it before asking anything again.
- `/retro-analysis` gives you a full updated `DATA-MAP.md` for `data-work/DATA-MAP.md`.

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

## For maintainers: releases and checks

- Create a release on GitHub. The ZIPs attach themselves. The `release` workflow builds one ZIP per skill and uploads each as a release asset.
- The `self-check` workflow runs `scripts/self-check` on every pull request and push.
- Private blocklist: add a repository secret named `DATA_SKILLS_BLOCKLIST` (Settings, Secrets and variables, Actions) with one word per line. The workflow writes it to a gitignored `.blocklist` inside the job and never prints it. Without the secret, that one check is skipped. See `CONTRIBUTING.md`.

## Where your files live

See [where-to-run.md](where-to-run.md): `data-work/` in a coding agent, or one Project per team or area in a chat app, with the instructions block `/setup-data-work` writes for you.
