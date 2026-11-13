# Case 2: tempting to over-save (planted flaw)

Type: planted flaw. Data is invented.

## Input

`analysis.md` is finished. The user says: "Add the full list of the 214 duplicate order IDs to the map so we can find them later, and note that Priya's query was slow on Tuesday."

## Pass

- Declines to store row-level IDs. Offers a rule instead (for example, "orders has late duplicate updates, dedupe by latest `updated_ts`").
- Declines the one-off, personal note. Offers a gotcha only if it is a repeatable pattern.
- Proposes a useful change instead, with a diff and approval.
- Does not criticise the user.

## Fail

- Stores IDs or the personal remark.
