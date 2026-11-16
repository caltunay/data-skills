# Upstream map

Checked 2026-11-13. Verdicts updated 2026-11-16 for v0.2: no item is left on the backlog. We read the licenses and skill descriptions. We copy no text. Every skill here is written from scratch.

## Licenses

| Repo | License | What it means for us |
|---|---|---|
| `anthropics/knowledge-work-plugins` (`data` plugin) | Apache-2.0 (`LICENSE` at repo root and in `data/`) | Reuse is allowed with attribution. We copy nothing, but credit it in `NOTICE` as a courtesy. |
| `openai/plugins` (`plugins/data-analytics`) | No license file in the repo. `plugin.json` says `"license": "Proprietary"`. | No reuse of text or code. We took ideas only (workflows are not copyrightable). Not listed in `NOTICE` as a source of text. |

## Anthropic `data` plugin

| Upstream skill | What it does | Overlaps | Verdict |
|---|---|---|---|
| `analyze` | Answers data questions, quick to formal | `/run-analysis` | absorbed into `run-analysis` |
| `explore-data` | Profiles a dataset: shape, nulls, distributions | `data-audit` | absorbed into `data-audit` |
| `validate-data` | QA before sharing: method, accuracy, bias | `/review-analysis`, `validation-ladder` | absorbed into `review-analysis` and `validation-ladder` |
| `statistical-analysis` | Descriptive stats, tests, outliers | `stats-tests` | absorbed into `stats-tests` |
| `sql-queries` | Dialect-aware SQL | `shaping-data` (`sql.md`) | absorbed into `shaping-data` |
| `write-query` | NL to optimised SQL | `shaping-data` (`sql.md`) | absorbed into `shaping-data` |
| `data-context-extractor` | Builds a company data skill from analyst interviews | `/setup-data-work`, `data-map` | absorbed into `setup-data-work` and `data-map` |
| `build-dashboard` | Interactive HTML dashboards | `viz` | absorbed into `viz` (`dashboard.md`) in v0.2. Not a skill of its own: a dashboard is charts plus layout rules |
| `create-viz` | Charts with Python | `viz` | built as `viz` (`python.md`) in v0.2 |
| `data-visualization` | Chart choice and design | `viz` | built as `viz` (`SKILL.md`: chart choice and 12 checks) in v0.2 |

## OpenAI `data-analytics` plugin (ideas only)

| Upstream skill | What it does | Overlaps | Verdict |
|---|---|---|---|
| `analyze-data-quality` | Is the data trustworthy | `data-audit` | absorbed into `data-audit` |
| `validate-data` | Is the analysis ready to share | `/review-analysis` | absorbed into `review-analysis` |
| `gather-business-context` | Frames the question first | `/grill-the-ask` | absorbed into `grill-the-ask` |
| `create-data-context` | Saves a semantic layer | `data-map`, `/retro-analysis` | absorbed into `data-map` |
| `metric-diagnostics` | Why did a metric move | `question-types` | absorbed into `question-types` in v0.1: the segment scan and metric decomposition cards (`exploratory.md`) and the mix-shift card (`descriptive.md`) |
| `design-kpis` | KPI and guardrail design | `metric-design` | built as `metric-design` in v0.2 (the one new skill from this inventory) |
| `product-business-analysis` | Analysis for a decision | `/plan-analysis` | absorbed into `plan-analysis` |
| `index` | Routes broad requests | `/ask-data-skills` | built as `/ask-data-skills` in v0.2 |
| `jupyter-notebooks` | Reproducible notebooks | `shaping-data` (`python.md`) | drop: a notebook is an output format, not a skill. `/run-analysis` may save one in `outputs/` |
| `build-dashboard`, `visualize-data` | Dashboards and charts | `viz` | absorbed into `viz` in v0.2 (ideas only) |
| `build-report`, `kpi-reporting` | Reports and KPI readouts | `/storytell`, `readout.md` | absorbed into `/storytell` and the readout layout in v0.2 (ideas only). A recurring KPI report is a dashboard: see `viz` (`dashboard.md`) |
| `market-sizing` | TAM, SAM, SOM | out of flow | drop: not a DSA flow need |
| `publish-artifact-to-sites` | Publishes to a vendor hosting product | vendor specific | drop: harness specific |

## v0.2 summary

| Backlog item | Verdict |
|---|---|
| Charts (3 upstream skills) | built: `viz` |
| Dashboards (2) | absorbed into `viz` |
| KPI design (1) | built: `metric-design` |
| Routing (1) | built: `/ask-data-skills` |
| Reports and KPI readouts (2) | absorbed into `/storytell` |
| Metric diagnostics (1) | absorbed into `question-types` |

New skills built from this inventory: 1 (`metric-design`), under the limit of 4. `viz` and `/ask-data-skills` were already on the v0.2 list.

Reuse: the Anthropic plugin is Apache-2.0 and may be reused with attribution. We still copied no text from it. The OpenAI plugin is proprietary: ideas only, no text.

## Narrow descriptions

Our descriptions name the data-skills flow, our own files (`analysis.md`, `DATA-MAP.md`) or the skill's own name. Flow skills say "Use only when the user runs /<name>". Disciplines are called by name inside the flow. A generic ask such as "write a SQL query for monthly sign-ups" should go to a built-in skill (`write-query`, `sql-queries`), not ours. `DECISIONS.md` B35 logs the before and after wording.
