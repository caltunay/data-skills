# Decisions

## Design decisions

1. Build our own data skills, phased. Flow skills call ours by name. Descriptions avoid clashing with built-ins.
2. One main flow. The plan sets the question type; later steps load its checks. v0 branches: descriptive and experiment.
3. Cycling back adds a dated plan revision entry, no restart.
4. Upstream: inventory both repos and check licenses first. v0 rebuilds only what the flow needs.
5. One path for connected and copy-paste use: `run-or-hand-over` covers queries and files.
6. Productionisation and monitoring: out of scope until v2+.
7. Connectors: rely on each agent's marketplace. No recipes. Hand-over mode covers gaps and admin blocks.
8. One `DATA-MAP.md` with fixed sections, including Conventions. Format version on line 1, with migrations.
9. Every data map entry has a verified date and source. Retro proposes, the user approves. Flag entries older than 90 days or contradicted by data.
10. User files live in `data-work/` in the user's project, committed and shared by the team. Never in the skills repo.
11. One folder per analysis: `analysis.md`, `queries/`, `outputs/`. No raw chat transcripts.
12. Assumptions: a table with alternatives required for high-impact rows.
13. `outputs/` git policy chosen at setup, default excluded. Aggregates by default; ask before saving row-level data.
14. Chat apps are first-class: skills install by upload in claude.ai and ChatGPT. `DATA-MAP.md` lives in the chat app's Project files.
15. Depth (quick, standard, deep) set by `/grill-the-ask`.
16. `shaping-data`: one skill, a tool-agnostic core (analysis table spec) plus one file per tool. All five tools in v0.
17. Style: sqlstyle.guide and PEP 8 by default; team overrides in Conventions; dialect per source in `DATA-MAP.md`.
18. v0 is 15 skills. Router and other off-flow skills in v1.
19. Testing: 3 eval cases per flow skill (2 flawed, 1 clean), run by hand in 4 agents, plus 3 real asks on public data.
20. Names: repo `caltunay/data-skills`; commands `/setup-data-work`, `/grill-the-ask`, `/plan-analysis`, `/run-analysis`, `/review-analysis`, `/retro-analysis`. "datafolx" is reserved for another product.

## Build decisions

Format: decision, options, reason.

B1. Branch: use `spec/v0` as asked, not the session default branch. Options: session branch or `spec/v0`. Reason: the task names it and the PR is from it.
B2. Upstream access: cloned both upstream repos and `caltunay/datafolx` read-only via the git proxy. Options: skip or clone. Reason: needed for licenses and reuse.
B3. Upstream licenses: Anthropic `data` plugin is Apache-2.0. OpenAI `data-analytics` has no license file and `plugin.json` says "Proprietary". Options: reuse text, or ideas only. Reason: we copy no text from either. NOTICE credits Anthropic as a courtesy plus other inspirations. OpenAI is ideas only.
B4. Nested skill discovery (open item 1): use flat `skills/<name>/`. Options: flat or nested. Reason: SPEC says flat if unsure, and I could not test the installer here.
B5. Template location (open item 2): `DATA-MAP.template.md` in `skills/data-map/` (SPEC 16). `analysis.template.md` is kept in `templates/` (SPEC 16) AND copied into `skills/run-analysis/` and `skills/grill-the-ask/` is not needed: `grill-the-ask` creates the file, so the template is copied into `skills/grill-the-ask/analysis.template.md`. Options: templates only in `templates/`, or also inside a skill folder. Reason: the installer may copy only skill folders. The skill also embeds the section list inline as fallback. `scripts/` checks both copies match.
B6. sqlstyle.guide (open item 4): the site was unreachable from this session. From memory it is CC BY-SA 3.0, which is share-alike. Decision: quote nothing, summarise rules in our own words, link to it. Options: quote, or paraphrase. Reason: avoids a license obligation I could not verify.
B7. Plugin manifests (open item 5): not added. Options: add or v1. Reason: not trivial to verify without the tools. Deferred to v1.
B8. Descriptions (open item 6): each starts with the situation, flow skills say "Use only when the user runs /<name> or explicitly asks to ...", disciplines name concrete triggers and say they are called by the flow. See each SKILL.md.
B9. datafolx reuse: adapted the review protocol, technical and business review, methods, and the planted-flaw case designs. Rewrote all text. The word is never used outside SPEC.md and DECISIONS.md. Invented data only.
B10. Eval cases live in `evals/<skill>/case-N.md` with `rubric.md`. Each case holds an input and a pass description. Planted-flaw cases for `review-analysis` are adapted from the earlier cases.

## Questions for Cenan

Short yes/no or A/B. Default is used until answered.
