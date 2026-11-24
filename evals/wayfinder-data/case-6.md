# Case 6: design ask in a chat Project, spec saved in its own folder, go-ahead question

Type: standard case. Data is invented.

## Input

User runs `/wayfinder-data` in a chat app, in a normal chat inside a Project. The Project files hold `data-work/DATA-MAP.md` and an older spec at the top level of the Project, `experiment-spec.md`, from a different test (a checkout button test). The chat can write to the Project files.

"Design an A/B test for a new free-delivery banner on the shop. I want to know if it lifts paid orders."

## Simulated answers

Round 1: "For the product team. Baseline is 10% of visitors paying within 7 days. About 800 visitors a day. Two weeks at most."
Round 2: "Randomise by visitor. The experiment platform holds the flag. The smallest lift worth shipping is 1.5 points. Guardrails are revenue per visitor and return rate."
Round 3: "Ship if the interval is above zero and guardrails hold. Otherwise keep the current page."
Round 4 (go-ahead): "A."

## Pass

- Takes the fast path: says this is one design item, builds no decision map.
- Questions come as clickable cards where a tool exists, each option says what it means, every default is real.
- Fills `experiment-spec.md` section by section, with the sample size shown as a calculation from the user's inputs, and "to confirm" for any number the user did not give.
- Saves the spec at `data-work/analyses/<YYYY-MM-DD>-<slug>/experiment-spec.md` (for example `data-work/analyses/2026-11-24-free-delivery-banner/experiment-spec.md`), never as a bare `experiment-spec.md`. Says "Saved to `<path>` in your Project files".
- Names the older top-level `experiment-spec.md` as a different, older file and says it is stale there. Does not overwrite it.
- Ends with the go-ahead question: "Go ahead? A) Yes, share the spec for sign-off, then run `/grill-the-ask` for the readout analysis (recommended) B) Change something (say what) C) Add an item, a check or a question".

## Fail

- Saves or overwrites a bare `experiment-spec.md`.
- Says the file is saved and also asks the user to replace the old one.
- Ends with "Let me know if you want changes" and no go-ahead question.
- Invents a baseline or a power figure.
