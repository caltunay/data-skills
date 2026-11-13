# Upstream map

Checked 2026-11-13. We read the licenses and skill descriptions. We copy no text. Every skill here is written from scratch.

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
| `build-dashboard` | Interactive HTML dashboards | none in v0 | v1 backlog |
| `create-viz` | Charts with Python | none in v0 | v1 backlog (`/viz`) |
| `data-visualization` | Chart choice and design | none in v0 | v1 backlog (`/viz`) |

## OpenAI `data-analytics` plugin (ideas only)

| Upstream skill | What it does | Overlaps | Verdict |
|---|---|---|---|
| `analyze-data-quality` | Is the data trustworthy | `data-audit` | absorbed into `data-audit` |
| `validate-data` | Is the analysis ready to share | `/review-analysis` | absorbed into `review-analysis` |
| `gather-business-context` | Frames the question first | `/grill-the-ask` | absorbed into `grill-the-ask` |
| `create-data-context` | Saves a semantic layer | `data-map`, `/retro-analysis` | absorbed into `data-map` |
| `metric-diagnostics` | Why did a metric move | `question-types` (descriptive) | v1 backlog (as a method note) |
| `design-kpis` | KPI and guardrail design | none in v0 | v1 backlog |
| `product-business-analysis` | Analysis for a decision | `/plan-analysis` | absorbed into `plan-analysis` |
| `index` | Routes broad requests | none in v0 | v1 backlog (`/ask-data-skills`) |
| `jupyter-notebooks` | Reproducible notebooks | `shaping-data` (`python.md`) | drop for v0: notebooks are an output format, not a skill |
| `build-dashboard`, `visualize-data` | Dashboards and charts | none in v0 | v1 backlog (`/viz`) |
| `build-report`, `kpi-reporting` | Reports and KPI readouts | none in v0 | v1 backlog (`/storytell`) |
| `market-sizing` | TAM, SAM, SOM | out of flow | drop: not a DSA flow need |
| `publish-artifact-to-sites` | Publishes to a vendor hosting product | vendor specific | drop: harness specific |

## Narrow descriptions

Our descriptions name concrete situations and the flow. Flow skills say "Use only when the user runs /<name>". Disciplines are called by name inside the flow. This keeps ours from firing on the same generic ask as a built-in `analyze` or `explore-data`.
