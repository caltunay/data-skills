# Eval runner

`run.py` runs the eval cases against a model and grades them with a judge model.

**What it is not.** It approximates skill loading: it pastes the skill's files, and the files of the skills it calls, into the system prompt. A real agent loads skills by itself. So the runner does not test triggering: whether a skill fires when it should, and stays quiet when it should not. Manual triggering tests are still needed. See the "Trigger checks" table in `evals/README.md`. It also has no data connection and no file system, so it tests what the skill says and asks, not what it writes to disk.

## What it does

1. Reads each `evals/<skill>/case-N.md` and the skill's `rubric.md`.
2. Builds the context: the skill's `SKILL.md` and its other files, plus the files of every skill it names.
3. Sends the case's **Input** as the user. If the case has a **Setup** section, that describes the environment.
4. For multi-turn cases, plays the **Simulated answers** section as the next user turns. Split turns with `Round 1:`, `Round 2:`. "None needed" means one turn.
5. Sends the transcript, the case and the rubric to a judge prompt. The judge returns pass, partial or fail, with reasons.
6. Writes `evals/results/<date>-<provider>-<model>.md`.

## Run it

Dry run first. It prints what would be sent and an estimated cost, and makes no API call:

```bash
python3 evals/runner/run.py --dry-run
```

A real run prints the estimated cost and asks you to type `yes`:

```bash
python3 evals/runner/run.py --provider anthropic --skills grill-the-ask review-analysis
```

```bash
python3 evals/runner/run.py --provider openai --model <model id> --price-in <dollars> --price-out <dollars>
```

Useful flags: `--cases case-1 case-4`, `--judge-model <model id>`, `--max-turns 4`, `--max-tokens 4000`, `--yes` (skip the question, for scripts).

## Keys

Keys come from environment variables only, read by the official SDKs: `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`. The runner never reads, prints or stores a key. Do not put keys in files in this repo.

Install the SDK you need. Neither is needed for a dry run:

```bash
pip install anthropic
```

```bash
pip install openai
```

## Cost

The estimate is rough: 4 characters per token, 1,500 tokens per reply. The price table in `run.py` holds a few Anthropic list prices with the date they were cached. Check current prices before a large run, or pass `--price-in` and `--price-out`. With no known price the runner says so and still asks before it runs.

## Reading the results

- A judge model can be wrong. Read the transcript (it is in the results file) for every fail and for a sample of passes.
- A different judge model from the model under test is a fairer grader. Use `--judge-model`.
- One run is one sample. Run a case several times before calling a skill fixed or broken.
- Results files are the maintainer's record. Remove "experimental" from a skill only after its cases pass here and by hand.
