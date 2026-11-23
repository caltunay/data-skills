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
| Chat-app handoff | With no project folder, offers `DATA-MAP.md` as a download at the end and says to save it to Project files |
| No invented names | Uses no company, product, table or source name the user did not say in this conversation |
| Go-ahead question | Ends with the fixed go-ahead question at every depth, quick included: "Go ahead? A) Yes, run `<next command>` B) Change something (say what) C) Add a check, segment or question" (v0.3 item 6) |
| No manual file edits | After the user confirms something, hands back the updated file. Never asks the user to edit a saved file by hand (v0.3 item 4) |
| Downloads first | In a chat app, creates each file and offers it as a download. Prints a block only if creating the file fails. Never says "I can't save files" when it can (v0.3 item 3) |
| Real defaults | Every question has one real recommended default with a reason. The dialect question lists Postgres, SQL Server, BigQuery, Snowflake, Databricks and other as separate options (v0.3 items 7 and 19) |
| Run first | With a code tool and an attached schema or data file, reads or queries it itself. Hands over only with no code tool, and says so in one line (v0.3 item 3) |
| Goals, funnels, key queries | Asks for the mission, north star, targets and horizon; the main funnels; and 3 to 5 key queries (v0.4 item 8 and 9) |
| Existing map first | With no map found, asks "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." before offering a fresh setup (v0.4 item 17) |
| Where files live | Asks how the user organises work (one repo with folders, a repo per project, a team repo, or chat Projects) (v0.4 item 11) |
| Project instructions block | In a chat app, ends by writing a short block for the Project's instructions (v0.4 item 14) |
| Document tool | Asks once, generically, about downloads or a document tool. Uses only a tool the user names (v0.4 item 16) |
| Stable names and versions | In a chat app, files are named `DATA-MAP.md`, `analysis-<slug>.md`, `readout-<slug>.md`, start with `format:` and `updated:`, are handed back whole, and the step says "Replace the old one in your Project files." If two copies exist, uses the newest `updated:` and says so (v0.4 item 15) |
