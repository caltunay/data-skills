format: v1
updated: YYYY-MM-DD HH:MM

# Readout: <title>

**Status: DRAFT**

Audience: exec | product | data | mixed
Date:

<!-- Portable markdown only: no app-specific macros. The readout is the decision layer and analysis.md is the evidence layer. Read in order, the headers alone tell the story. Caps: at most 5 headline numbers, 3 charts, 3 callouts. A callout is a blockquote with a bold label (Ask, Caveat, Decision) and appears only where a decision or attention is needed. Bold only the one takeaway per section. The status line is SKELETON (placeholders only, from /plan-analysis), then DRAFT (from /run-analysis), then FINAL (set by /review-analysis). A readout.docx is built from this text with the charts embedded: edit this file, then rebuild the .docx. -->

## TL;DR

Two to three lines: the answer, what it means, and the ask. Plain words, rounded numbers for an exec audience.

## <Takeaway sentence: the first thing the reader must believe>

The chart or number under this header proves the header. If a number tells the reader what it would take to change the answer (the gap to a target, the size of change needed), it goes here, not in the appendix.

![Alt text: what the chart shows and its takeaway](<chart-name>.svg)

## <Takeaway sentence: the next thing, drilling in>

One message per section. One chart at most. Every number carries its uncertainty, in plain words ("we are 95% sure it fell").

> **Ask:** the one thing you need from the reader, if any.

## Caveats

> **Caveat:** the caveat that most changes how the answer should be read.

- Open high-impact assumptions:
- What this analysis can and cannot say (the claim ceiling, in plain words):

## Method

Three lines: data, method, checks passed. Claim only what ran. Do not write "full validation ladder" unless every rung ran against an independent path and passed. Working notes: `analysis.md` (its Review pack lists the scripts behind each headline number).

## Appendix

Analyst-only figures (raw-count checks, intervals of robustness cuts, recompute detail), other numbers, segment tables and the ladder summary. Optional at standard depth.
