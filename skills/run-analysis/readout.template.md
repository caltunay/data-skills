format: v1
updated: YYYY-MM-DD HH:MM

# Readout: <title>

**Status: DRAFT**

Audience: exec | product | data | mixed
Date:

<!-- Portable markdown only: no app-specific macros. At most 3 callouts in the whole readout, as blockquotes with a bold label (Answer, Caveat, Ask). Bold only the one takeaway per section. The status line is SKELETON (placeholders only, from /plan-analysis), then DRAFT (from /run-analysis), then FINAL (set by /review-analysis). A readout.docx is built from this text with the charts embedded: edit this file, then rebuild the .docx. -->

## 1. Answer

> **Answer:** two lines. The answer first.

## 2. Key numbers

| number | value | uncertainty |
|---|---|---|
| | | |

At most 5 numbers. Every number carries its uncertainty: an interval, a tolerance, or "exact count for the period". Other numbers go to the Appendix. A chart replaces a number row when it says the same thing.

## 3. Charts

At most 3 charts for an exec audience. Each title states the takeaway. One annotation marks the key moment (for example, a marker on the day a step happened). Charts are image files in the analysis folder, linked here by their real path relative to this file, with alt text. A coding agent keeps them in `outputs/`. A chat app keeps them beside this file. Never link `outputs/` in a chat app:

![Alt text: what the chart shows and its takeaway](<chart-name>.png)

No chart is fine when a number says it better.

## 4. What it means

What it means for the decision, and the recommendation. **One bold takeaway.**

> **Ask:** the one thing you need from the reader, if any.

## 5. Caveats

> **Caveat:** the caveat that most changes how the answer should be read.

- Open high-impact assumptions:
- What this analysis can and cannot say (the claim ceiling, in plain words):

## 6. Method

Three lines: data, method, checks passed. Claim only what ran. Do not write "full validation ladder" unless every rung ran against an independent path and passed.

## 7. Link

Working notes: `analysis.md` (its Review pack holds the code behind each headline number).

## 8. Appendix

Numbers beyond the 5 key numbers, segment tables, the ladder summary. Optional at standard depth.
