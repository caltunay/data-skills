# Case 2: readout is still a draft (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/storytell`: "Turn this into a 5-slide outline for the product team."

Attached `readout.md` has `Status: draft`. It holds an A/B readout for the shop's pricing page: conversion up 0.6 points (95% interval 0.1 to 1.1). The `analysis.md` Progress line says `run done, draft readout written, next /review-analysis`.

## Simulated answers

"Go ahead anyway, the meeting is in an hour."

## Pass

- Says the readout is not final and has not been checked against the claim ceiling. Suggests `/review-analysis` first. Waits.
- After the answer, continues and marks the output `Status: draft, from an unreviewed readout`.
- Slide outline: at most 5 slides. Each title states a takeaway. One chart suggestion per slide, each with chart type, axes with units, and how the interval is shown.
- The lift keeps its interval on every slide that shows it.
- The claim stays "in this test, for these visitors, in this period".
- The last slide holds caveats and next steps.

## Fail

- Treats the draft as final without a word.
- Refuses to continue after the user says go ahead.
- More than 5 slides, or titles like "Results".
- A dual-axis chart or a bar chart that does not start at zero is suggested.
