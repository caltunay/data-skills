# Case 8: an analysis of the same ask already exists in the Project (planted trap)

Type: planted trap. Data is invented.

## Input

User runs `/grill-the-ask` in a chat app, in a normal chat inside a Project. The Project files hold `data-work/DATA-MAP.md` (set up last month) and `data-work/analyses/2026-11-23-signup-drop/analysis.md`. That analysis has status `running`, a Progress line "run step 3 of 8, waiting for Q3.1 paste", a full Decisions section and a hypothesis tree. Its Meta still says "Setup choice: B (no DATA-MAP.md, so inline)", although the map now exists.

The user writes: "Why did sign-ups drop in March? Same ask as yesterday, for the head of growth."

## Simulated answers

Round 1 (the continue or new question): "Continue it."
Round 2 (go-ahead): "A."

## Pass

- Finds the existing folder and asks, as a clickable card where a tool exists, "Continue `data-work/analyses/2026-11-23-signup-drop/`, or start a new analysis?" before any grilling question. Recommends continue, with the reason that the status is not `retro done`.
- Does not resume silently, and does not re-ask any question the Decisions section already answers.
- Resumes from the Progress line and says what step comes next. At this point the right next step is `/run-analysis`, not a new grill: says so.
- Refreshes the stale Meta line as a "was" and "now" pair: "was: no DATA-MAP.md, so inline" and "now: map found". Does not offer setup again.
- Says which files changed and where they are, with full paths and one of the three save forms. Names any stale copy (for example `analysis (2).md` at the top level) if one is mentioned.

## Fail

- Starts grilling the ask from the top, as if no analysis existed.
- Resumes the old analysis without asking.
- Leaves "no DATA-MAP.md, so inline" in Meta.
- Saves a file under a bare name such as `analysis.md`.
