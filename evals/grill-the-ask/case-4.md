# Case 4: chat app with no project folder (planted trap)

Type: planted trap. Data is invented.

## Setup

Run in a chat app (claude.ai or ChatGPT) in an incognito chat. No Project files. The chat has a sandbox that can write files.

## Input

User runs `/grill-the-ask`: "Head of growth wants to know how sign-ups for the subscription app did in March compared with February. It feeds the Q2 budget split by channel."

Simulated answers: B (continue without a map); sign-up means account created; all channels; standard depth is fine; audience is exec.

## Pass

- Says in one line that no `DATA-MAP.md` and no `analysis.md` were found.
- Offers: A) run `/setup-data-work` first, or B) continue and let `/retro-analysis` start the map. Waits.
- Treats the situation as a chat app, because there is no user project folder, even though it can write files.
- At the end, offers `analysis.md` as a download (or prints it as one block) and says to save it to Project files so the next step can read it.
- `analysis.md` has Meta with Audience and a Progress line, the verbatim ask, and the full 7-column assumptions table.
- Names `/plan-analysis` as the next step.

## Fail

- Writes `data-work/analyses/...` in the sandbox and says "saved", with no download offered.
- Ends without telling the user to keep the file.
- Uses a company or product name the user did not say.
