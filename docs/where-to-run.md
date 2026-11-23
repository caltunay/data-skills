# Where to run data-skills

Pick the row that matches how you work. The skills behave the same. Only where the files live changes.

## Coding agents (Claude Code, Codex, Gemini CLI)

- Files live in `data-work/` in your repo. The skills save them for you.
- The skills look for `data-work/` in the current folder, then upward. A team map can sit above project maps. The nearest map wins for conflicts, and the skill says which one it read.
- Commit `DATA-MAP.md` so the team shares it. Keep `outputs/` out of git unless you chose otherwise.
- Ways to organise: one repo with a folder per project, a repo per project, or a team repo.

## Chat apps (claude.ai, ChatGPT)

- Make one **Project per team or area**, and one **chat per analysis**.
- Run `/setup-data-work` once. It ends with a short block to paste into the Project's instructions. Example:

  ```
  Read DATA-MAP.md before any data work. Use the data-skills commands.
  Keep files named DATA-MAP.md, analysis-<slug>.md and readout-<slug>.md.
  Save updated files back to the Project files. If two copies exist, use the newest `updated:` line.
  ```

- Fixed file names: `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md`. Every file starts with `format:` and `updated: YYYY-MM-DD HH:MM`.
- Each step hands back the whole file and says "Replace the old one in your Project files." You never edit a file by hand. If two copies exist, the skill uses the newest `updated:` line and says so.
- Optional: save files to a document tool you use (for example a drive, a wiki or a notes app) instead of downloads. The skill asks once, and only uses a tool you name.
- The readout comes as `readout-<slug>.md` and as a `.docx` with the charts embedded, if the chat has a code tool. It opens in Word and Google Docs.
- Start the review in a new chat in the same Project. Everything it needs is in the Project files.

## Starting a new project, or a new Project, on the same data

Carry over `DATA-MAP.md` and the Project instructions block. Start a fresh map only for entirely different data sources.

When no map is found, `/setup-data-work` and the flow steps ask first: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." Only then do they offer a fresh setup.

## Which command first?

See the routing guide in the [README](../README.md#which-command-do-i-start-with).
