# Tableau charts

Always hand-over mode. Give numbered steps. Ask the user to say or paste what they see.

## Steps to hand over

1. Check the grain of the data source first (apply the `shaping-data` skill; core rule: know what one row means before you aggregate).
2. Drag the dimension to Columns (time for a trend) and the measure to Rows. Pick the mark type on the Marks card: Line, Bar, Circle.
3. Double-click the title. Type the takeaway.
4. Right-click each axis, Edit Axis. Set the title with its unit. For bars, keep "Include zero" ticked.
5. Sort bars: the sort button on the axis, or sort by the measure, descending.
6. Add the caption (Worksheet, Show Caption): source, period, filters.

## Notes by check

- **No dual axes:** do not use Dual Axis to mix two measures with different units. Put two measures on Rows to get two stacked panes with a shared time axis.
- **Same scale when comparing:** panes from one measure share an axis by default. If "Independent axis ranges" is on, turn it off or say so in the title.
- **Small multiples:** put the series dimension on Rows or Columns to split into panels. Remove it from Colour if the panels are labelled.
- **Uncertainty:** Analytics pane, then a reference band or distribution band on computed lower and upper fields. Say what the band is.
- **Colour-blind safe:** Colour, Edit Colours, pick the "Color Blind" palette. Add labels (Label on the Marks card, line ends).
- **Partial periods:** filter out the unfinished period, or use a calculated field to flag it and put the flag on Detail with a dashed style.
- **Funnel:** one bar per step with the step dimension sorted by step order. Label with count and step conversion (a table calculation: this step divided by the previous step).
- **Cohort heatmap:** cohort month on Rows, age on Columns, the rate on Colour and Label, mark type Square. Unreached cells stay empty.
- **Continuous or discrete dates:** a continuous (green) date gives an even time axis. A discrete (blue) date gives categories. Use continuous for a trend.

## Traps

- Averages of averages. Compute the rate as SUM over SUM at the right level.
- A filter on the view that the reader cannot see. Show filters, or put them in the caption.
- An extract that is out of date. Say when it was last refreshed.
