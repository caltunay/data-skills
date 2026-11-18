# Power BI charts

Always hand-over mode. Give numbered steps. Ask the user to say or paste what they see.

## Steps to hand over

1. Use explicit measures, not dragged columns (apply the `shaping-data` skill; core rule: know the grain and write the measure on purpose).
2. Pick the visual from the `viz` chart table: Line chart for a trend, Clustered bar chart for a comparison, Scatter chart for a relationship, Funnel for a funnel, Matrix with conditional formatting for a cohort heatmap.
3. Put the dimension on the axis and the measure on values.
4. Format visual, Title: type the takeaway. Turn on the axis titles and type label and unit.
5. Bars: Format visual, the value axis, Range, set Minimum to 0.
6. Sort: the three dots on the visual, Sort axis, by the measure, descending.

## Notes by check

- **No dual axes:** do not use "Line and clustered column chart" to mix two units. Use two visuals with the same width and the same date axis.
- **Same scale when comparing:** set the same axis minimum and maximum on each visual by hand, or use Small multiples with a shared y-axis.
- **Small multiples:** drag the series field to "Small multiples". Keep the shared axis on.
- **Uncertainty:** on a line chart, Format visual, Error bars, and point Upper bound and Lower bound at measures. Say what the band is in the subtitle.
- **Colour-blind safe:** View, Themes, pick the colour-blind safe theme, or set data colours by hand. Turn on data labels or series labels so colour is not the only signal.
- **No 3D:** do not add shadow or glow effects under Format, Effects.
- **Partial periods:** add a measure or a filter that drops the unfinished period. Put the cut-off date in the subtitle.
- **Slicers change every number.** State the slicer settings a chart was read with. For a chart that must not move, set "Edit interactions" to none.

## Traps

- A measure changes with the filter context of every visual. A total can differ from the sum of the bars.
- Implicit measures (sum of a column by default) on a rate column.
- A date axis set to Categorical spaces months unevenly. Use Continuous.
