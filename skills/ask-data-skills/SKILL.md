---
name: ask-data-skills
description: Route the user to the right data-skills command for what they are trying to do, with one line why and the command that comes after it. Use only when the user runs /ask-data-skills or explicitly asks to be told which data-skills command to use.
---

# /ask-data-skills

A signpost. It points to one command. It does not do the work.

Experimental (v0.2).

## Hard rules

- Do not start the work yourself: no clarifying the ask in depth, no plan, no query, no review. Recommend the command and stop.
- Never call a connector or data tool until the user has named the source it applies to. This step calls none. Never build answer options from the connectors you can see.
- Never fill in a company, product, table or source name the user has not said in this conversation, even if you know it from memory, a profile or a connector. Ask instead.

## Steps

1. If the user already said what they are trying to do, go to step 3.
2. Otherwise ask, in **one round of at most 3 questions**, each with options. Ask only what changes the route:
   - "What are you trying to do?" A) Answer one data question or a stakeholder ask. B) Check or share work that is already done. C) Set up or improve how the team works with its data. D) Fix or improve a query or script. E) Something big and vague, or a project of several questions. F) Design an experiment or define a measure. G) Not sure.
   - "Where are you in the work?" A) Not started. B) Clarified. C) Planned. D) Results exist. E) Reviewed.
   - "Is there an `analysis.md` for it?" A) Yes. B) No. C) Not sure.
   Use the environment's multiple-choice question tool if it has one (such tools take at most 4 options per card, so split the first question into two cards if needed); otherwise list the options as text.
   Then stop asking. One round only.
3. Recommend **one command**. Give **one line why**. Name **the next command after it**.
4. Stop. Do not run the command for them. Do not begin its questions.

Answer format:

```
Run: /<command>
Why: <one line>
Then: /<next command>
```

If the user has `analysis.md`, its Progress line beats their memory: read it and route from it.

## Routing guide

| The ask looks like | Use |
|---|---|
| A project: several questions, unknowns, weeks of work | `/wayfinder-data` |
| A design with no data needed yet (experiment, measurement) | `/wayfinder-data` (fast path) |
| One question with a decision attached | `/grill-the-ask` and the flow |
| Not sure | `/ask-data-skills` |

The table below is the detail.

## Routing table

| The user wants to | Run | Then |
|---|---|---|
| Describe their data once, so later work goes faster (no `DATA-MAP.md` yet) | `/setup-data-work` | `/grill-the-ask` |
| Answer a new ask that is vague, or has no decision, metric or time window | `/grill-the-ask` | `/plan-analysis` |
| Choose a method, or write down what the result table should look like, for a clear ask | `/plan-analysis` | `/run-analysis` |
| Build the numbers for a planned analysis | `/run-analysis` | `/review-analysis` |
| Check an analysis or a readout before sharing it (theirs or anyone's) | `/review-analysis` | `/retro-analysis` |
| Save what an analysis taught them about the data | `/retro-analysis` | none, the flow is complete |
| Turn a final readout into an exec, product or data version, an email or a slide outline | `/storytell` | `/retro-analysis` |
| Fix, check or speed up SQL or Python | `/improve-code` | `/retro-analysis` if a trap was found |
| Break down big, vague work (a metrics framework, a quarter of analysis) | `/wayfinder-data` | `/grill-the-ask` for the first analysis |
| Design an experiment, or define how to measure something, with no data needed yet | `/wayfinder-data` (fast path: one spec, no project map) | `/grill-the-ask` for the analysis that reads it out |
| Pass the work to a colleague, or to a fresh session | `/handoff` | the command named in the handoff |
| Resume and not sure where they stopped | The command named in the Progress line of `analysis.md` | the next one in the flow |

The flow, for reference: `/setup-data-work` (once), then `/grill-the-ask`, `/plan-analysis`, `/run-analysis`, `/review-analysis`, `/retro-analysis`.

## Tie-breaks

- A "why did X change" ask with nothing written down: `/grill-the-ask`, not `/run-analysis`.
- "Is this right?" about a result: `/review-analysis`. About a query: `/improve-code`.
- "Make a deck" from a readout that is not final: `/review-analysis` first, then `/storytell`.
- A quick, fully specified number ("paid orders in October, UTC, test accounts excluded"): `/grill-the-ask` still. It will set quick depth and move on in one step. Say so.
- "Design an A/B test" or "define how we measure X", with no data needed yet: `/wayfinder-data`, fast path. Not `/grill-the-ask`.
- A project (several questions, unknowns, weeks of work): `/wayfinder-data`, even if the first line sounds like one question.
- Two commands fit: pick the earlier one in the flow, and name the other as "Then".

## The full catalogue

User-invoked commands (the only things this step recommends):

- Flow: `/setup-data-work`, `/grill-the-ask`, `/plan-analysis`, `/run-analysis`, `/review-analysis`, `/retro-analysis`.
- Off-flow, experimental: `/storytell`, `/improve-code`, `/wayfinder-data`, `/handoff`, `/ask-data-skills`.

Skills the agent applies by itself inside those commands. Never tell the user to "run" these:

- Disciplines: `grilling`, `assumptions`, `validation-ladder`, `question-types`, `data-map`, `run-or-hand-over`.
- Data skills: `shaping-data`, `data-audit`, `stats-tests`, and experimental `viz` and `metric-design`.

If the user asks what one of these does, answer in one line and name the command that uses it.

## Not a data-skills job

If the ask is not data work, or no command fits, say so in one line. Do not force a route.

## Done when

The user has one command, one line why, and the next command.
