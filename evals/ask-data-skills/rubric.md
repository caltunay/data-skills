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
| Clickable question cards (v0.5 item 12) | Uses the environment's multiple-choice question tool when it has one: one card per question, at most 3 per round, recommended option first. Otherwise lists the options as text |
| Cards explain themselves (v0.5 item 13) | Each option says what it means in a few words (for example "H1.1: holds in each month"). Any tree, table or draft the question refers to is shown before the question is asked |
| No hedged defaults (v0.5 item 14) | No default reads "recommended if you have one", "TBC" or "C if unknown". Each default is a real option with a reason |
