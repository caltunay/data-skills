# Rubric: /setup-data-work

Score each case pass or fail.

| Check | Pass means |
|---|---|
| No dead end | Missing or blocked access leads to hand-over mode, with one pointer to the connector directory |
| Rounds | At most 3 questions per round |
| Map format | `format: v1` on line 1, fixed sections, every entry has `verified` and `source: setup` |
| No invention | Unknown items are left as gaps and listed |
| Staleness | Entries older than 90 days or contradicted are flagged and asked about |
| Approval | Migrations and changes to existing entries are shown first |
| Git | Outputs path added to `.gitignore` unless the user chose to commit |
| No keys | Never asks for credentials |
| Precision | The clean case gets no needless questions |
| No early tool call | No connector or data tool call before the user names the source. No answer options built from visible connectors |
| Start check | Says in one line whether a `DATA-MAP.md` was found. Asks the setup mode question first (A connect, B describe, C paste a schema, D a mix), unless the user's own message already answers it |
| Chat-app hand-back | With no project folder, offers `DATA-MAP.md` at its full `data-work/` path at the end, in one of the three save forms (v0.5 item 2) |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, writes each file to the Project files at its full path if it can, otherwise creates it and offers a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3, v0.5 item 2) |
| Real defaults | Every question has one real recommended default with a reason. The dialect question lists Postgres, SQL Server, BigQuery, Snowflake, Databricks and other as separate options (v0.3 items 7 and 19) |
| Run first | With a code tool and an attached schema or data file, reads or queries it itself. Hands over only with no code tool, and says so in one line (v0.3 item 3) |
| Goals, funnels, key queries | Asks for the mission, north star, targets and horizon; the main funnels; and 3 to 5 key queries (v0.4 item 8 and 9) |
| Existing map first | With no map found, asks "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." before offering a fresh setup (v0.4 item 17) |
| Where files live | Asks how the user organises work (one repo with folders, a repo per project, a team repo, or chat Projects) (v0.4 item 11) |
| Project instructions block | In a chat app, ends by writing a short block for the Project's instructions (v0.4 item 14) |
| Document tool | Asks once, generically, about downloads or a document tool. Uses only a tool the user names (v0.4 item 16) |
| Stable names and versions | In a chat app, files use the `data-work/` layout at full paths (`data-work/DATA-MAP.md`, `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md`), start with `format:` and `updated:`, and are handed back whole. If two copies exist, uses the newest `updated:` and says so (v0.5 item 1) |
| Say what happened to each file (v0.5 items 1 to 4) | Names every file by its full `data-work/` path, never a bare name. Each save uses one of three forms: "Saved to `<path>` in your Project files", "Download `<file>` and add it to your Project at `<path>`", or "Printed below; save it as `<path>`". Never claims a save that did not happen. Never says "replace the old one, it is already saved there". Names a stale older copy of the same file and says it is stale. Chart links point to the chart's real path, never `outputs/` in a chat app |
| Earlier work, no map (v0.5 item 7) | When the Project holds earlier analyses but no `DATA-MAP.md`, the first option is "Yes, attach it", not "No", and it says: "If an earlier analysis ended with a retro, the map is in that chat. Download it and add it to `data-work/DATA-MAP.md`." |
| Key queries as SQL (v0.5 item 8) | Each key query is saved as SQL text in the team's conventions, with what it returns and when to use it, and its columns are checked against the Tables section. A description alone fails |
| Tidy the map (v0.5 item 9) | When extending a messy map, normalises it to the template as one approved change with a diff: one entry per source, grain and keys under Tables, table layout instead of bullets |
| Ways of working (v0.5 item 10) | Records in the map how the user works (chat Projects or a repo layout) and the file hand-back choice (downloads, Project files, or a named document tool). Asks about hand-back once per Project, not at every grill |
| Instructions block (v0.5 items 11 and 21) | In a chat app, ends with the Project instructions block in the exact words: "Read data-work/DATA-MAP.md before any data work. Use the data-skills commands. Keep files in data-work/ as the skills lay them out. At the end of each step, tell me which files changed and where they are." Then walks the user through the chat-app steps in 3 to 5 short lines |
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
| Flags missing data (v0.5 item 15) | An option that needs data the map says is missing or unknown says so in the option text, and is not recommended without that flag |
