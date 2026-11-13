---
name: question-types
description: Name the question type and apply its claim ceiling when framing, planning, writing claims or reviewing a data analysis. Holds method notes for descriptive and experiment questions. Applies whenever a conclusion is being worded.
---

# Question types and claim ceilings

A claim never goes above what its method supports.

## Core rule

Six question types, each with a ceiling. Name the type early. Word every claim at or below the ceiling. Say "caused" only with a randomised experiment or a credible causal design that passed its checks.

## The six types

| Type | Asks | Allowed claims | Not allowed |
|---|---|---|---|
| Descriptive | What happened? | "was", "is", counts, rates for the data observed | Generalising beyond the data; "why" |
| Exploratory | What patterns are there? | "we see", "pattern worth testing" | "drives", "causes", confirmed findings |
| Inferential | Does it hold beyond this sample? | "associated with", with uncertainty | "causes" |
| Predictive | What will happen for a new case? | "predicts", with out-of-sample performance | Explaining why; "causes" |
| Causal | What happens if we change X? | "caused", "effect of" only with a randomised experiment or a credible causal design that passed its checks | Causal language from observational data without a design |
| Mechanistic | How exactly does it work? | Rarely reachable in business work. Flag it. | Most claims |

## Pre-post with no control

At most: "Y changed after X". Not "X caused Y". Ask what else changed at the same time.

## Must-answer questions by type

Ask these before work starts, and check them in review.

- Descriptive: what is the exact definition and population? Is the period final? What is the trusted number to reconcile to?
- Exploratory: how many slices were tried? What would count as a pattern worth testing?
- Inferential: what is the population, and how was the sample drawn? What is the interval?
- Predictive: what is the holdout? What beats the simple baseline? What does an error cost?
- Causal: what is the control? Was assignment random? What else changed at the same time?
- Mechanistic: can the mechanism be observed directly, or only inferred? If only inferred, drop the claim.

## Branches in v0

Load only the file for the branch in use.

- Descriptive questions (what happened, where, when, metric movements): read `descriptive.md` in this folder.
- Experiment questions (A/B tests and other randomised tests): read `experiment.md` in this folder.

Causal designs without randomisation (difference-in-differences, interrupted time series, matching) and machine learning are not in v0. If the ask needs one, say so, state the ceiling the available data supports, and offer the best descriptive or experiment path.

## Using it in each step

- Grilling: confirm the type with the user. Write it into the Meta section of `analysis.md`.
- Planning: choose a method that can reach the claim the decision needs. If the type cannot support the decision, say so now, not at the end.
- Running: use the checks in the branch file.
- Writing claims: every finding gets direction, magnitude, uncertainty, and the ceiling applied.
- Reviewing: flag every sentence whose wording is above the ceiling, and quote it.

## Rule of thumb

If the decision needs "why" and the data only supports "what", say that plainly and propose the cheapest way to get a stronger answer, such as a test.
