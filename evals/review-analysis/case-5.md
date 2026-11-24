# Case 5: wrong hypothesis statuses on robustness children (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/review-analysis` in a coding agent. `analysis.md` is a sound descriptive analysis: sign-ups, March against February 2026, all rungs passed, reconcile within tolerance. Finding: sign-ups were 36,500 in March against 36,900 in February, down 1.1%. The weekly differences are -0.8%, -1.3%, -1.0%, -1.2% (all four weeks the same sign). The raw count and the count without test accounts differ by 0.2%.

The Hypotheses section reads:

| id | hypothesis | would support it | would refute it | leads to | status |
|---|---|---|---|---|---|
| H1 | Sign-ups fell by more than 5% in March | A fall above 5%, interval above 5% | A fall below 5% | H1.1, H1.2 | refuted (Q2.1: down 1.1%) |
| H1.1 | The result holds in each week | Each weekly difference has the same sign and a similar size as the overall difference | A weekly difference with the opposite sign, or far larger | none | refuted (no fall above 5% in any week) |
| H1.2 | The result holds on the raw count | Raw and cleaned counts differ by less than 1% | They differ by 1% or more | none | refuted (no fall above 5% on the raw count) |

The readout is a draft and correct.

## Simulated answers

None needed.

## Pass

- Checks every hypothesis status against the node's own support and refute conditions.
- Finds that H1.1 and H1.2 are wrong: both were judged against H1's direction. The result held in each week and on the raw count, so both are `supported`.
- Leaves H1 as `refuted`: it is right.
- Fixes the two statuses in `analysis.md` and shows each as a "was" and "now" pair with one line why. Example: was "H1.1 refuted"; now "H1.1 supported: the weekly differences all have the same sign (-0.8% to -1.3%)".
- Notes that the child wording leans on the parent's direction and rewords it ("the difference has the same sign in each week").
- Raises no invented issues with the analysis. Verdict `ready` or `ready with caveats`.

## Fail

- Leaves H1.1 or H1.2 as `refuted`.
- Flips H1 to `supported`.
- Reports the fix as a summary with no "was" and "now" pair.
