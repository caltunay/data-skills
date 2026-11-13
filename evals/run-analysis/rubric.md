# Rubric: /run-analysis

| Check | Pass means |
|---|---|
| Reads first | Uses the spec and success checks from `analysis.md` |
| Expected first | States the expected result before each rung |
| Ladder honest | A failed rung stops the climb until the cause is found |
| Depth | Quick: rung 1 and reconcile. Standard: full. Deep: full plus alternative specification |
| Reconcile | Gap computed against the stated tolerance, explained if above |
| Fan-out | Row counts before and after joins |
| Claims | At or below the ceiling. Direction, magnitude, uncertainty |
| Ask not assume | Unclear items are asked or logged as assumptions |
| Data safety | Aggregates by default, asks before saving row-level data |
| Precision | The clean case reports without invented issues |
