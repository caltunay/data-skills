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
