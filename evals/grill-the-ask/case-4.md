# Case 4: chat app with no project folder (planted trap)

Type: planted trap. Data is invented.

## Setup

Run in a chat app (claude.ai or ChatGPT) in a normal chat (not incognito). No Project files. The chat has a sandbox that can write files.

## Input

User runs `/grill-the-ask`: "Head of growth wants to know how sign-ups for the subscription app did in March compared with February. It feeds the Q2 budget split by channel."

## Simulated answers

Round 1: "B, continue without a map. A sign-up is an account created. All channels."
Round 2: "Standard depth is fine. The audience is exec."

## Pass

- Says in one line that no `DATA-MAP.md` and no `analysis.md` were found.
- Offers: A) run `/setup-data-work` first, or B) continue and let `/retro-analysis` start the map. Waits.
- Treats the situation as a chat app for files, because there is no user project folder.
- At the end, saves `analysis.md` at `data-work/analyses/<YYYY-MM-DD>-<slug>/analysis.md` and says what happened, in one of three forms. With no Project files and a sandbox, the form is "Download `analysis.md`". A block only if creating the file fails.
- `analysis.md` has Meta with Audience and a Progress line, the verbatim ask, and the full 7-column assumptions table.
- Ends with the go-ahead question, A) being `/plan-analysis`.

## Fail

- Writes `data-work/analyses/...` in the sandbox and says "saved", with no download offered.
- Ends without telling the user to keep the file.
- Uses a company or product name the user did not say.
