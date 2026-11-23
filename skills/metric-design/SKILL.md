---
name: metric-design
description: Define a metric or KPI for the data-skills flow so it can be computed, reconciled and trusted, with a formula, grain, population, owner, guardrails and a trusted number. Applies when /wayfinder-data or /setup-data-work settles a metric definition, or when a flow step finds that a metric in the ask has no agreed definition. Not for computing a metric that is already defined.
---

# Metric design

A metric is a decision about what counts. Write the decision down before anyone computes it.

Experimental (v0.2).

## Core rule

A metric is not defined until it has: a plain-words meaning, a formula, a grain, a population, a time rule, an owner, at least one guardrail, and a trusted number to reconcile to. Every choice the user has not made is asked, not assumed.

## The metric card

Fill one per metric. Ask the user for each line you cannot fill from what they said or from the data map. Do not guess.

| Field | What to write |
|---|---|
| Name | Short, and the same everywhere it is used |
| Decision it serves | What someone will do differently when it moves. If nothing, question the metric |
| Meaning | One sentence a new joiner would understand |
| Formula | Numerator and denominator in words, then in logic. A count, a sum, a rate or a ratio of sums |
| Grain and unit | What is counted: customers, subscriptions, orders, sessions. One only |
| Population | Who is in, who is out: test accounts, staff, free plans, cancelled orders, returned orders |
| Time rule | Which timestamp, which time zone, which window (calendar month, rolling 28 days), and when a period is final |
| Direction | Is up good, bad, or does it depend? |
| Segments | The cuts it must support (plan, channel, country), and whether segment values are as-at-the-time or current |
| Owner | The role that decides the definition. A role the user names. Otherwise "to confirm" |
| Guardrails | The metrics that must not get worse when this one is pushed (see below) |
| Trusted number | One value, its period, and where it comes from, for reconciling |
| Known traps | Fan-out joins, late data, a definition change on a date |

## Choices that hide in common metrics

Ask about each one that applies. Give 2 to 4 options and one real recommended default, never a hedge.

- **Active:** paid and not cancelled, or used the product in the last N days? Which N?
- **Churn:** counted on the cancellation request date or the date access ends? Is a pause churn? Is a downgrade churn? Rate over subscribers at the start of the period, or the average?
- **Conversion:** per visitor or per session? Within what window? First order only?
- **Revenue:** gross or net of returns and discounts? With or without tax and delivery? On the order date, payment date or dispatch date?
- **Retention:** active in period n, or still active by period n? Cohort by sign-up or by first order?
- **Average order value:** per order or per customer? Mean or median?
- **New customer:** first order ever, or first in the last 12 months?

## Guardrails

Every target metric gets at least one guardrail: a metric that would show the cost of gaming or over-pushing it.

| Push this | Watch this |
|---|---|
| Conversion | Return rate, average order value, margin |
| Sign-ups | Activation rate, 30-day retention, cost per sign-up |
| Average order value | Conversion, order count |
| Churn rate (down) | Discount depth, support cost, reactivation quality |
| Email click rate | Unsubscribe rate |

State for each guardrail the level that would stop a rollout ("return rate must not rise by more than 0.5 points").

## Good metric tests

- **Computable:** from tables that exist, at the stated grain. If not, say what is missing.
- **Reconcilable:** it can be checked against a trusted number.
- **Movable:** the owner's team can move it, and within a period they can act on.
- **Hard to game:** the guardrails cover the cheap ways to move it.
- **Stable:** the definition does not change with a filter or a dashboard default.
- A ratio shows its numerator and denominator alongside. A rate change is given in points.

## A set of metrics (a framework)

- One primary metric per goal. A few inputs under it that multiply or add up to it (a driver tree: see the metric decomposition card in the `question-types` skill, file `exploratory.md`). Guardrails beside it.
- Fewer is better. If two metrics always move together, keep one.
- Leading metrics (move early, weaker link to the goal) are labelled as such. The link to the goal is a hypothesis until tested.
- No causal wording between metrics without a design. Apply the `question-types` skill. Core rule if it does not load: a claim never goes above what its method supports.

## Where it goes

- A settled definition belongs in the Metrics and Glossary sections of `DATA-MAP.md`. This skill does not write there. `/setup-data-work` writes it at setup; after that, `/retro-analysis` proposes it and the user approves. Core rule of the `data-map` skill: the map changes only through approved changes, each with a `verified` date and a source.
- Inside `/wayfinder-data`, each open choice on a metric card is a decision item.
- An unsettled choice that work must go ahead with is an assumption. Apply the `assumptions` skill: write it in the table with alternatives and impact.

## Do not

- Do not define a metric by its SQL alone. Meaning first.
- Do not pick a definition because it is easiest to compute. Say what the easy one would miss.
- Do not invent an owner, a target or a trusted number.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
