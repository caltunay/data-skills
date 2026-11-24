# Case 5: robustness child hypotheses whose result held (planted trap)

Type: planted trap. Data is invented.

## Input

User runs `/plan-analysis` in a coding agent. `analysis.md` holds a grilled ask: "Did sign-ups fall in March against February?" Standard depth, descriptive. `DATA-MAP.md` lists `signups` (one row per sign-up, `signup_ts`, `channel`, `is_test`).

The user adds: "A quick earlier check, run by a colleague, found the March figure was about the same as February, down 1%. It was the same in each of the four weeks, and the same on the raw count and with test accounts removed."

## Simulated answers

Round 1: "Follow H1 and its children. Park the rest."
Round 2: "No skeleton. Go with your recommended method."

## Pass

- Writes the hypothesis tree before the method options, shown first, then asks which paths to follow in a card whose options say what each path means (for example "H1.1: the difference has the same sign in each week").
- Child nodes are worded without the parent's direction: "the difference has the same sign in each week" and "the difference is the same on the raw count and with test accounts removed", not "the fall holds in each week".
- Each node has its own support and refute condition.
- Sets the statuses from the colleague's result, judged against each node's own conditions: H1 ("sign-ups fell") is `refuted` (down 1% is no fall, within the stated tolerance), and the robustness children H1.1 and H1.2 are `supported`, because the result held in each week and on the raw count. Names the result behind each status.
- Does not mark H1.1 or H1.2 `refuted` because H1 was refuted.
- Ends with the go-ahead question, A) being `/run-analysis`.

## Fail

- Marks both children `refuted` because the parent went the other way.
- Writes children as "the fall holds in each week", which depends on the parent's direction.
- Asks which paths to follow before the tree is shown.
- Uses a hedge such as "recommended if you have one" for the path default.
