format: v1
updated: YYYY-MM-DD HH:MM

# Metric spec: <metric name>

Status: draft | agreed
Owner: <a role the user names, or "to confirm">
Date:

Fill every line. If a line cannot be filled, write what is missing and who can supply it. Never invent a number.

## 1. Purpose

- What we want to know or manage:
- Decision it serves (what someone does differently when it moves):

## 2. Definition

- Definition (one sentence a new joiner would understand):
- Formula: <numerator and denominator in words, then in logic>
- Grain and unit: <what is counted, one only>
- Population: <who is in, who is out>
- Time rule: <which timestamp, time zone, window, and when a period is final>
- Direction: <up is good | up is bad | depends>

## 3. Data

- Data source: <table or file, or "not collected yet">
- What must be collected if it does not exist: <event, field, system, and who builds it>

## 4. Proxies

Use a proxy only when the true metric cannot be measured now.

| candidate proxy | why it might track the true metric | how to check it tracks | check result |
|---|---|---|---|
| | | <for example: correlation across customers or periods, and whether it moves first, using data where both exist> | not run |

If no data holds both the proxy and the true metric, the proxy is a guess. Say so.

## 5. Benchmark or target

- Benchmark or target: <value and period, or "none yet">
- Where it comes from: <a trusted report, a past period, an industry source the user names, or "to confirm">

## 6. Guardrails and traps

- Guardrails: <metrics that must not get worse, each with a stop level>
- Known traps: <late data, fan-out joins, a definition change on a date>

## 7. Owner and review

- Owner (a role):
- Review date:
- Trusted number to reconcile to:

## 8. Open items

| item | who can answer | by when |
|---|---|---|
