# Example: A/B test on the shop's pricing page

A worked example on invented data for an invented online shop. It follows the flow in order, at deep depth: `/setup-data-work`, `/grill-the-ask`, `/plan-analysis` (before the test), `/run-analysis`, `/review-analysis`, `/retro-analysis`.

## Files

| File | Written by | Holds |
|---|---|---|
| `generate_data.py` | hand | Seeded script that writes the CSVs in `data/` |
| `DATA-MAP.md` | setup, then retro | The data map, with 5 entries added by the retro |
| `analysis.md` | grill, plan, run, review, retro | Ask, assumptions, the plan with power, ladder log, the 10 method card checks, findings, review, retro |
| `readout.md` | run (draft), review (final) | The stakeholder readout |
| `queries/` | run | Numbered check queries, one purpose each, expected result stated first |
| `stats.py` | run | The sample ratio check, power, test and intervals, from the query results |
| `outputs/` | scripts | `results.txt` and `stats.txt`: the real results |

## What to look for

- The plan is written before the test: one primary metric, guardrails, sample size from the smallest effect worth shipping, fixed run length.
- The sample ratio check comes first in the readout checks.
- The join from visitors to orders fans out. The analysis table is built per visitor, the unit of randomisation.
- The readout gives the effect in points with its interval, says the second week was weaker, and does not promise revenue.
- A mobile-only gain shows up after slicing. It is labelled a pattern to test.
- The review changes three sentences in the draft readout and records each as "was" and "now".

## Run it again

```bash
python3 examples/pricing-page-test/generate_data.py
```

```bash
python3 examples/run_queries.py examples/pricing-page-test
```

```bash
python3 examples/pricing-page-test/stats.py
```

Python standard library only. The queries run in SQLite.
