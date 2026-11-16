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
