# Rubric: /ask-data-skills

| Check | Pass means |
|---|---|
| One round | At most one round of at most 3 questions, each with options. None when the route is already clear |
| One command | Exactly one recommended command |
| Why | One line saying why |
| Next | The command that comes after it |
| Does not do the work | No clarifying in depth, no plan, no query, no review, no rewrite |
| Catalogue | Routes only to user-invoked commands. Never tells the user to "run" a model-invoked skill |
| Order | Does not route to `/storytell` before the readout is final, or to `/run-analysis` before a plan exists |
| Precision | The clean case gets three lines and no questions |
| No early tool call | No connector or data tool call |
| No invented names | Uses no company, product, table or source name the user did not say |
| Routing guide | Sends a project or a design ask to `/wayfinder-data`, one question with a decision to `/grill-the-ask` (v0.4 item 13) |
