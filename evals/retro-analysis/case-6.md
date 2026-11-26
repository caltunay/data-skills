# Case 6: the only check was a repeat run (v0.6)

Type: planted flaw. Data is invented.

## Input

User runs `/retro-analysis` after an analysis of monthly orders. The reconcile rung compared the number to a figure produced by the same query and the same rules a month earlier. Both give 18,400 paid orders for September. No outside source (a finance report, a dashboard owned by another team) was used. The first retro also found that the scope of the order target (all channels, or web only) is unclear. The user answered during the run that work lives in chat Projects, files come back as Project files, and charts are SVG.

## Simulated answers

Round 1 (the agent proposes changes, the user approves each): "Yes to all."
Round 2 (go-ahead): "A."

## Pass

- Does not call 18,400 a trusted number. Records it as "repeat run, no outside check" and says what outside source would make it trusted.
- Proposes updates to Ways of working: where work lives, file hand-back (Project files), chart format (SVG). None is written as a gap.
- Records the unclear target scope as its own row in Open gaps, with what is unknown and who can answer, so the next grill asks about it.
- Writes each source as `analyses/<YYYY-MM-DD>-<slug>`.
- Reasons are true for this run, each shown by a line in `analysis.md`.

## Fail

- Writes "trusted number" for a repeat of the same rules.
- Leaves the target scope inside another line.
- Saves "where work lives: gap" after the user answered.
