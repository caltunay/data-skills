# Case 5: zero-day logging gap in the daily series (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/run-analysis` in a coding agent with the data connected. `analysis.md` asks: "Why did first orders drop in March?" Standard depth, descriptive then exploratory. Plan: monthly first orders February against March, then a segment scan by channel, platform and country.

The `orders` table has no rows at all for 11 and 12 March (an event logging break). Every other day has 380 to 450 first orders. March is down 6% on February.

## Simulated answers

Round 1 (the agent asks what happened on 11 and 12 March): "Engineering confirms the order event pipeline was down those two days. The orders happened but were not logged."
Round 2 (the agent proposes how to handle it): "Exclude the two days and compare per logged day. Log it as a plan revision."
Round 3 (go-ahead): "A."

## Pass

- Runs the daily series floor check across the full window before any segment scan.
- Finds the two zero days, records the check as fail, and stops the climb.
- Says a logging break is a likely cause of a drop, and asks the user before choosing a fix.
- Adds a dated Plan revisions row for the change and an assumption row if the fix is a choice.
- Recomputes the comparison per logged day and says how much of the 6% drop the gap explains (two missing days of about 410 is about 820 orders).
- Runs the segment scan only after that, and frames it on the corrected numbers.

## Fail

- Runs the segment scan first.
- Reports a 6% drop and explains it by segments without finding the zero days.
- Fills the two days with an estimate without asking or logging it.
