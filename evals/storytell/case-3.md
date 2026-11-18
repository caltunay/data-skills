# Case 3: clean data-audience version (clean)

Type: clean. Data is invented.

## Input

User runs `/storytell`: "Data team version, as a doc."

Attached `readout.md` is `Status: final`: win-back email test, randomised holdout of 20,000 customers per arm, difference in revenue per customer +0.31 (95% interval -0.12 to +0.74), recommendation not to roll out, caveats complete. `analysis.md`: question type causal (randomised experiment), all method card checks passed, no open high-impact assumptions.

## Simulated answers

None needed.

## Pass

- Says which files it found and that the readout is final. Asks nothing.
- Writes `readout-data.md` in the doc layout: answer, key numbers, what it means, caveats, method, link.
- Uses precise terms: the interval, the unit of randomisation, the checks passed.
- Changes no number and no claim. The interval that includes zero is stated as such.
- Raises no concerns about the analysis. That is the review's job.

## Fail

- Rewrites the conclusion ("the email works" or "the email does not work").
- Invents a caveat or asks needless questions.
- Strips the method detail the data audience wants.
