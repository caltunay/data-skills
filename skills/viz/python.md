# Python charts (matplotlib or plotly)

Use matplotlib for static files in `outputs/`. Use plotly when the reader needs hover or zoom. Ask which if it is not clear. Follow PEP 8 unless the data map Conventions say otherwise.

## Pattern (matplotlib)

```python
import matplotlib.pyplot as plt
import pandas as pd

OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]

weekly = pd.read_csv("outputs/weekly_signups.csv", parse_dates=["week_start"])

fig, ax = plt.subplots(figsize=(8, 4.5))
for colour, (channel, part) in zip(OKABE_ITO, weekly.groupby("channel")):
    ax.plot(part["week_start"], part["signups"], color=colour, marker="o", markersize=3)
    ax.annotate(channel, (part["week_start"].iloc[-1], part["signups"].iloc[-1]),
                xytext=(5, 0), textcoords="offset points", color=colour, va="center")

ax.set_title("Paid social sign-ups fell 41% in March; other channels held", loc="left")
ax.set_xlabel("Week starting (UTC)")
ax.set_ylabel("Sign-ups per week")
ax.set_ylim(bottom=0)
ax.spines[["top", "right"]].set_visible(False)
fig.text(0.01, 0.01, "Source: signups table, Feb to Mar, test accounts excluded.", fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig("outputs/signups-by-channel-feb-mar.png", dpi=200)
```

## Notes by check

- **Title:** `ax.set_title(takeaway, loc="left")`. Put the neutral description in a subtitle if needed.
- **Bars at zero:** `ax.bar` starts at zero by default. Never set `ylim` above zero on a bar chart.
- **Uncertainty:** `ax.errorbar(x, y, yerr=...)` or `ax.fill_between(x, low, high, alpha=0.2)`. Say what the band is in the caption.
- **No dual axes:** do not use `ax.twinx()`. Use `plt.subplots(2, 1, sharex=True)`.
- **Small multiples:** `plt.subplots(rows, cols, sharex=True, sharey=True)`. In plotly: `facet_col` with `facet_col_wrap`.
- **Colour:** set the cycle once: `plt.rcParams["axes.prop_cycle"] = plt.cycler(color=OKABE_ITO)`. Ordered data: `cmap="viridis"`. plotly: `color_discrete_sequence=OKABE_ITO`.
- **Direct labels** instead of a legend, as in the pattern.
- **Partial periods:** drop the unfinished period before plotting, or draw it dashed and say so.
- **Dates:** parse them as dates. A string axis sorts by text and spaces unevenly.
- **Money and percent:** `matplotlib.ticker.PercentFormatter(1.0)` or `StrMethodFormatter("{x:,.0f}")`.

## Pattern (plotly)

```python
import plotly.express as px

fig = px.line(
    weekly, x="week_start", y="signups", color="channel", markers=True,
    color_discrete_sequence=OKABE_ITO,
    title="Paid social sign-ups fell 41% in March; other channels held",
    labels={"week_start": "Week starting (UTC)", "signups": "Sign-ups per week"},
)
fig.update_yaxes(rangemode="tozero")
fig.write_html("outputs/signups-by-channel-feb-mar.html", include_plotlyjs="cdn")
```

## Do not

- Do not ship the library defaults without the checks.
- Do not save a chart that shows one point per named customer without asking.
- Do not smooth a line without saying how.
