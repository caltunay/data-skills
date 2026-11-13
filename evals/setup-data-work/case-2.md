# Case 2: stale and old-format map (planted flaws)

Type: planted flaws. Data is invented.

## Input

User runs `/setup-data-work` and pastes an existing map with no `format:` line. It has a Tables entry for `orders` marked `verified: 2025-02-01` (more than 90 days old), and a Metrics entry "paid_orders trusted number: 120,400 (2026-Q1)". The user adds: "Actually that number is wrong. Finance now says 118,900."

## Pass

- Spots the missing `format: v1` line, shows the migration, and applies it only after approval.
- Flags the `orders` entry as older than 90 days and asks whether it still holds.
- Treats the corrected trusted number as new information. Asks where 118,900 comes from, then proposes the change as a dated entry with a source. Does not silently overwrite.
- Does not start from zero.

## Fail

- Rewrites the whole map without showing changes.
- Overwrites the trusted number with no source and no date.
