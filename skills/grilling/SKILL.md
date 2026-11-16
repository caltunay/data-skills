---
name: grilling
description: Ask clarifying questions about a data ask (an analysis, metric, query, report or experiment) in rounds of at most 3, each with options and a recommended default. Applies in the clarification steps of the data-skills flow, or when a flow step meets an unclear definition, metric, population or time window. Not for non-data asks, and not for a data ask that is already specific.
---

# Grilling

Clarification is the most important part of data work. Ask before you assume.

## When this applies

Only for data asks: an analysis, a metric, a query, a report, an experiment. If the ask is not about data (a vague request to plan an offsite, write an email, fix a bug), this skill does not apply. Do not run rounds of questions from it.

## Core rule

Ask in rounds of at most 3 questions. Give each question 2 to 4 options and a recommended default. Wait for the answers. Never assume silently.

## How to run a round

1. Read what you already know: the ask, the data map if present, `analysis.md` if present, earlier answers. Never ask the same question twice in a session, even reworded.
2. Pick the 3 questions whose answers would change the work the most.
3. Write each question like this:

   **Q1. Which date should an order be counted on?**
   - A. Order date (recommended: matches the finance report)
   - B. Payment date
   - C. Dispatch date
   - D. Something else

4. Stop. Wait for the reply.
5. Repeat until the work is clear, or until the depth limit is reached (quick: 1 round).

## What to cover, in this order of priority

1. Goal: what outcome does the stakeholder want?
2. Decision: what will they decide or do differently with the answer? If nothing, say so.
3. Question type: what happened, what patterns, does it hold, what will happen, what if we change X, how does it work?
4. Metric: exact definition, and who counts in numerator and denominator.
5. Population: who or what is in scope, and what is excluded.
6. Time window: dates, time zone, and whether the latest days are final.
7. Constraints: tools, privacy, data access, people.
8. Deadline: when, and why then.
9. Audience: who reads the result (exec, product, data, mixed).

## Rules

- Skip anything already answered or visible in the data map.
- If the user says "you choose", take the recommended default and record it as an assumption.
- If the user answers only some questions, ask the rest next round. Do not guess.
- Ask about the most uncertain thing first, not the easiest.
- Critique the work, never the person. A weak ask is a gap to fill, not a mistake.
- If no questions are needed, say so in one line and move on. Do not invent questions.
- For deep depth, add stakeholder prep questions: who else will read this, what will they push back on, what would change their mind.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
