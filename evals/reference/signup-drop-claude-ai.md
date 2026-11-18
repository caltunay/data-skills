# Reference run: sign-up drop, claude.ai

A summary of a full manual run of the flow in claude.ai (setup, grill, plan, run, review, retro) on the `examples/signup-drop` data, in incognito and normal chats. Data is invented. It is a reference for what a good run catches, not a graded case: the runner skips this folder because it has no rubric.

Use it to judge a new run of the same example. A new run should catch at least what is listed under "Caught", and should not repeat what is listed under "Fixed in v0.3".

## The ask

"Why did sign-ups drop in March?" for the invented subscription app. Data: `signups.csv`, `daily_spend.csv`, `dashboard_monthly.csv`, attached to the chat.

## Caught

| What | Where in the flow | Why it matters |
|---|---|---|
| Duplicate rows: 40 `signup_id` values with two rows each, from late updates | Run, rung 3 (many entities) | Counting rows instead of ids inflates every month. The run stopped, found the cause (only `updated_ts` differs), proposed "keep the latest row", logged it and re-ran the rung |
| Month length: March has 31 days, February 28 | Grill (assumptions) and run (findings) | The monthly total falls 17%; per day it falls 25%. Reporting only the total understates the fall by about a third |
| Spend as a lead, not a cause | Run (segment scan), review (claims) | Paid social spend fell in the same week as paid social sign-ups. The readout calls the timing a lead worth testing and names the test (restore spend in some markets), not a cause |
| Reconcile to the trusted number | Run, rung 5 | Cleaned monthly counts are within 0.4% of the growth dashboard. The run said which count was compared and why |
| Independent recompute | Review | The reviewer recomputed the headline numbers from the raw table, without the cleaned table, and got the same values |
| Readout rewrites | Review | "Driven by paid social" became "almost all of the fall is in one channel"; "the spend cut explains the timing" became "a lead worth following, not a proven cause"; the total-only headline gained the per-day fall. Each change was shown as "was" and "now" |

## Fixed in v0.3 (seen in this run, should not happen again)

| Seen | Fix |
|---|---|
| Quick depth skipped most data checks | The data-check floor runs at every depth, quick in compact form |
| Rungs 2 to 4 compared the table with the frame it was built from | Rungs 2 to 4 compare against raw rows or a separate query |
| The agent said "I can't run code" and "I can't save files" in a chat with a code tool | `run-or-hand-over` asks "can I run things here?" and "where do files persist?" separately |
| The user was asked to edit a saved file by hand | The step hands back the updated file |
| In an incognito chat the method card files could not be opened | Compact cards in `question-types/SKILL.md` |
| No go-ahead question at quick depth; the deadline question had no default | Fixed go-ahead question at every depth; every question has a real default |
| "Last 30 vs prior 30 days" recommended with no seasonality flag | Grill recommends a seasonal comparison or flags the gap |
| A claim rule sat in the assumptions table; month length rated Low | Claim rules go in the ceiling; impact rated by size |
| The reconcile check did not say which count should match | It names raw or cleaned, and why |
| Spec corrections written as notes under "(none)" | Each is a dated Plan revisions row |
| Exec readout with 7 key numbers; Method said "full validation ladder" | At most 5 numbers plus an Appendix; Method claims only what ran |
| Retro put an analysis rule under Conventions, and said "the grain trap cost a rung" when it had not | Conventions hold style only; every reason quotes a line in `analysis.md` |

## How to use it

1. Run the flow on `examples/signup-drop` in a chat app with a code tool, attaching the three CSVs.
2. Compare the run with "Caught". A miss is a regression.
3. Compare with "Fixed in v0.3". A repeat is a regression.
4. Record the result in `evals/results/<date>-<agent>.md`.
