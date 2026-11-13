---
name: grilling
description: Ask clarifying questions before any data work starts or when a step is ambiguous. Applies in the clarification steps of the data-skills flow, or when an ask is vague, has no decision attached, or has no metric or time window.
---

# Grilling

Clarification is the most important part of data work. Ask before you assume.

## Core rule

Ask in rounds of at most 3 questions. Give each question 2 to 4 options and a recommended default. Wait for the answers. Never assume silently.

## How to run a round

1. Read what you already know: the ask, the data map if present, earlier answers. Never ask twice.
2. Pick the 3 questions whose answers would change the work the most.
3. Write each question like this:

   **Q1. Which refund date do you mean?**
   - A. Refund request date (recommended: matches the finance report)
   - B. Payment settlement date
   - C. Booking date
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

## Rules

- Skip anything already answered or visible in the data map.
- If the user says "you choose", take the recommended default and record it as an assumption.
- If the user answers only some questions, ask the rest next round. Do not guess.
- Ask about the most uncertain thing first, not the easiest.
- Critique the work, never the person. A weak ask is a gap to fill, not a mistake.
- If no questions are needed, say so in one line and move on. Do not invent questions.
- For deep depth, add stakeholder prep questions: who else will read this, what will they push back on, what would change their mind.
