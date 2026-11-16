# Example: why did sign-ups drop in March?

A worked example on invented data for an invented subscription app. It follows the flow in order: `/setup-data-work`, `/grill-the-ask`, `/plan-analysis`, `/run-analysis`, `/review-analysis`, `/retro-analysis`.

The ask is a "why". The data supports "how much, when and where". The example shows the ceiling being stated instead of crossed.

## Files

| File | Written by | Holds |
|---|---|---|
| `generate_data.py` | hand | Seeded script that writes the CSVs in `data/` |
| `DATA-MAP.md` | setup, then retro | The data map, with 6 entries added by the retro |
| `analysis.md` | grill, plan, run, review, retro | The working notes: ask, assumptions, plan, ladder log, findings, review, retro |
| `readout.md` | run (draft), review (final) | The stakeholder readout |
| `queries/` | run | Numbered check queries, one purpose each, expected result stated first |
| `outputs/results.txt` | `run_queries.py` | The real result of every query |

## What to look for

- Rung 3 of the ladder fails (duplicate rows). The run stops, finds the cause, fixes it and logs a plan revision.
- The month totals understate the fall, because March is three days longer. The readout gives both numbers.
- The segment scan lists its 4 dimensions before looking, and confirms the top pattern in a second cut.
- Spend fell in the same week. The readout calls that a lead, not a cause.
- The review changes three sentences in the draft readout and records each as "was" and "now".

## Run it again

```bash
python3 examples/signup-drop/generate_data.py
```

```bash
python3 examples/run_queries.py examples/signup-drop
```

Python standard library only. The queries run in SQLite.
