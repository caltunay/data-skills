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
21. Never call a connector or data tool before the user names the source. Never build options from visible connectors.
22. Never fill in company, product, table or source names the user has not said in this conversation.
23. Setup asks first how to set up the map: connect, describe, paste a schema, or a mix.
24. Every flow step checks for `DATA-MAP.md` and `analysis.md`, says what it found, and offers setup if there is no map. Outside the flow, no map means silence.
25. Chat app is defined by situation (no user project folder), not by file access. Each flow step offers its files as downloads and tells the user to save them to Project files.
26. Standard and deep depth always show the full 7-column assumptions table.
27. `/run-analysis` is goal-driven: it states its goal and keeps going until the success checks pass, stopping only for pastes or answers.
28. Readout: `/run-analysis` drafts `readout.md`; `/review-analysis` checks it word by word and marks it final. One layout, wording adapted to the audience set in grilling.
29. Progress line in `analysis.md` Meta; every new session resumes from it.
30. `question-types` covers all six types: one skill, a selector in `SKILL.md`, one file per type with method cards. Full cards for common methods, short cards plus a specialist-review flag for advanced ones. In v0.1, with method-choice evals.
31. One neutral example domain: an invented online shop and subscription app. A private gitignored `.blocklist` is checked by `scripts/self-check`.
32. `grilling` fires on data asks only. Descriptions are tuned so generic data asks do not trigger ours over built-in data skills.

## Build decisions

Format: decision, options, reason.

B1. Branch: use `spec/v0` as asked, not the session default branch. Options: session branch or `spec/v0`. Reason: the task names it and the PR is from it.
B2. Upstream access: cloned both upstream repos and `caltunay/datafolx` read-only via the git proxy. Options: skip or clone. Reason: needed for licenses and reuse.
B3. Upstream licenses: Anthropic `data` plugin is Apache-2.0. OpenAI `data-analytics` has no license file and `plugin.json` says "Proprietary". Options: reuse text, or ideas only. Reason: we copy no text from either. NOTICE credits Anthropic as a courtesy plus other inspirations. OpenAI is ideas only.
B4. Nested skill discovery (open item 1): use flat `skills/<name>/`. Options: flat or nested. Reason: SPEC says flat if unsure, and I could not test the installer here.
B5. Template location (open item 2): `DATA-MAP.template.md` lives in `skills/data-map/`. `analysis.template.md` lives in `templates/` (SPEC 16) and a copy sits in `skills/grill-the-ask/`, because that skill creates the file and an installer may copy only skill folders. `scripts/package-zips` and the self-check verify both copies match. Each skill also lists the section names inline as fallback.
B6. sqlstyle.guide (open item 4): the site was unreachable from this session. From memory it is CC BY-SA 3.0, which is share-alike. Decision: quote nothing, summarise rules in our own words, link to it. Options: quote, or paraphrase. Reason: avoids a license obligation I could not verify.
B7. Plugin manifests (open item 5): not added. Options: add or v1. Reason: not trivial to verify without the tools. Deferred to v1.
B8. Descriptions (open item 6): each starts with the situation, flow skills say "Use only when the user runs /<name> or explicitly asks to ...", disciplines name concrete triggers and say they are called by the flow. See each SKILL.md.
B9. datafolx reuse: adapted the review protocol, technical and business review, methods, and the planted-flaw case designs. Rewrote all text. The word is never used outside SPEC.md and DECISIONS.md. Invented data only.
B10. Eval cases live in `evals/<skill>/case-N.md` with `rubric.md`. Each case holds an input and a pass description. Planted-flaw cases for `review-analysis` are adapted from the earlier cases.
B11. Added `scripts/self-check`, not in SPEC 16. Options: manual checks only or a script. Reason: repeatable, and the PR can show the output. It is not packaged into any skill.
B12. Em dash check skips `SPEC.md` because it must stay unchanged. It has none anyway.
B13. Skill commands are named in descriptions with a trailing space check ("Use only when the user runs /<name> or explicitly asks to ..."), which the self-check matches.
B14. Install docs for Codex, Gemini CLI, Cursor and Copilot give the `npx skills add` route and say to check each agent's current docs for the exact folder. I could not verify folder paths from this session, so I avoided stating them as fact.
B15. Chat-app ZIP upload steps in `docs/install.md` describe the general route. Exact menu names change, so they are not pinned.
B16. The eval cases are written as inputs plus pass and fail descriptions. They are run by hand (SPEC 15), so there is no runner. Results go in `evals/results/`, which is empty until the maintainer runs them.
B17. No manual run of the evals in the four agents was possible from this session. The manual test checklist in the PR is for the maintainer.
### v0.1 fix pass

B18. SPEC.md replaced with v0.1. Design decisions 21 to 32 appended above. One wording change in SPEC section 3: the style rule now says "active verbs". Options: exempt SPEC.md from the private blocklist check, or change one word. Reason: the check must hold for every file, and the meaning is the same.
B19. Neutral domain (fix H). Rewrote every example outside the online shop and subscription app: the README folder name, the `assumptions` example row, the `grilling` example question, the `review-analysis` dedup line, `validation-ladder` rung 1, two eval cases, and three lines in `question-types/experiment.md`. Reason: SPEC section 3.
B20. Private blocklist (fix H). `scripts/self-check` reads `.blocklist` (gitignored, one word per line) and fails on any whole-word, case-insensitive match outside `.git`. The file itself is skipped. With no file, the check prints SKIP. The words are not listed anywhere in the repo. `.gitignore` also ignores the two private brief file names.
B21. Connector rules (fix A, items 6 to 8). Every flow skill has a "Hard rules" block: no connector or data tool call before the user names the source, generic source options only, no names the user has not said. Every discipline and data skill has a short "Names and sources" section with the same rule. Options: state it once in `run-or-hand-over`, or in every skill. Reason: a skill must hold the rule even when the others do not load.
B22. `setup-data-work` rewritten (fix A, item 7). Step 0 is the setup mode question from SPEC section 8, before any tool. If the user's own message already makes the mode clear, the skill says which mode it understood and continues. It never infers the mode from visible connectors. Connected tools are listed by name only after the user picks "Connect". The access test runs only against the source the user named.
B23. `run-or-hand-over` rewritten (fix A and C). It now holds the source rule, the generic options, the chat-app definition by situation, the end-of-step download, and the attach-first rule. The access test runs only after the source is named and never tests other connectors.
B24. Data map check (fix B, items 9 and 10). Every flow skill opens with a "Start (every flow step)" block: the 4 steps from SPEC section 4. The A or B setup offer is made once per analysis, not at every step. `data-map` now splits inside the flow (announce and offer) from outside the flow (silent). Root cause fixed: the old text said "say so once and continue" and "read it if present".
B25. Start block per step. `/grill-the-ask` does not expect `analysis.md` for a new ask. `/review-analysis` accepts a pasted analysis from outside the flow and then only notes the missing map in one line. `/retro-analysis` option B starts the map from the template with approved entries only. Reason: the 4 steps must not create dead ends.
B26. Chat apps and handoff (fix C, items 11 and 12). "Chat app" is decided by situation: no user project folder means chat app, even with a sandbox that can write files. Every flow skill has an "End (every flow step)" block: update Progress, offer `analysis.md` (and `readout.md`) as a download, tell the user to save it to Project files, name the next step. Root cause fixed: the old branch was "no file access", which never fired in a sandbox. `docs/install.md` explains the same.

## Questions for Cenan

Short yes/no or A/B. Default is used until answered.

Q1. Is `anthropics/knowledge-work-plugins` credit in `NOTICE` wanted even though no text was copied? Default: yes, keep it (A: keep, B: remove).
Q2. Should the plugin manifests for Claude Code and Codex be added in v1? Default: yes, v1 (A: v1, B: add now).
Q3. sqlstyle.guide could not be reached to confirm its license. Default: we paraphrase only and link. OK? (A: yes, B: check and quote some)
Q4. SPEC section 3 style rule now says "active verbs" so the private word check passes on SPEC.md. OK? Default: yes (A: keep, B: exempt SPEC.md from the check and restore the wording).
