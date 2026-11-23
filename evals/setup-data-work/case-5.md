# Case 5: chat app setup with goals, funnels and an existing map (v0.4)

Type: standard case. Data is invented.

## Setup

A chat app with no code tool and no project folder. No `DATA-MAP.md` is attached.

## Input

User runs `/setup-data-work`: "We are a small team that runs an online shop and a subscription app."

## Simulated answers

Round 0: "No, I do not have a map from another project."
Mode: "B. I will describe it."
Round 1: "One Postgres warehouse. Tables: `orders` (one row per order, key `order_id`), `customers` (one row per customer, key `customer_id`), `subscriptions` (one row per subscription, key `subscription_id`)."
Round 2: "Mission: make good home goods easy to buy. North star: repeat customers. Target this quarter: raise paid orders per active customer. Main funnel: visit, add to basket, checkout, paid order. Events are in `web_events`."
Round 3: "Key queries: paid orders by day, new customers by week, active subscriptions by plan. Chat Projects are how we work. Downloads are fine."

## Pass

- Before the mode question, asks: "Do you have a DATA-MAP.md from another project on the same data? Attach or copy it in." Offers a fresh setup only after the answer.
- Asks the setup mode question and waits. Calls no data tool.
- Asks about goals: mission, north star metric, target metrics and their horizon (this quarter, this year, 3 years).
- Asks for the main funnels with each step, its event or table and the step definition.
- Asks for 3 to 5 key queries, what they return and when to use them.
- Asks how the user organises work (one repo with folders, a repo per project, a team repo, or chat Projects). Recommends one Project per team or area and one chat per analysis for the chat Projects answer.
- Asks once, generically, about downloads or a document tool. Names no tool the user did not say.
- Joins start `unverified`. No invented table, number or name.
- Hands over the whole `DATA-MAP.md` as a file with `format: v1` and `updated:` lines, with Goals, Funnels and Key queries sections.
- Ends with a short block to paste into the Project's instructions that says: read `DATA-MAP.md` before any data work, use the data-skills commands, save updated files back to the Project files.
- Ends with the go-ahead question, A) being `/grill-the-ask`.

## Fail

- Offers a fresh setup before asking for an existing map.
- Skips goals, funnels or key queries.
- Invents a funnel step or a key query the user did not give.
- Ends with no Project instructions block.
- Names a document tool or connector the user did not say.
