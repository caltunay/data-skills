# Case 6: review pack that reads and writes a temp path (planted flaw, v0.6)

Type: planted flaw. Data is invented.

## Input

User runs `/review-analysis` in a new chat in the Project. `analysis.md` is a sound descriptive analysis of March sign-ups (31,200 against 36,900 in February). Its "Appendix: Review pack" lists `scripts/q4-1-recompute.py`, which reads `/tmp/signups_clean.csv` and writes `/tmp/recompute.csv`. The script is saved, and the code is there. The attached `signups.csv` in the data folder matches the analysis.

## Simulated answers

Round 1 (go-ahead, after the review): "A."

## Pass

- Runs the script from the data folder, as a fresh reader would, and finds that it reads a temp path that does not exist for the reader and writes its output outside the analysis folder.
- Raises it as an issue: any temp path, absolute path or missing input means the number cannot be rerun. "Code is present" is not a pass.
- Recomputes the headline numbers by an independent route from the attached file, so the numbers themselves are still checked.
- Names the fix: the script takes the data folder as an argument and writes into the analysis folder.
- Verdict: `ready with caveats` or `needs rework` until the script is fixed.

## Fail

- Marks the review pack as fine because the code is present.
- Does not run the script, and does not say it was not checked.
