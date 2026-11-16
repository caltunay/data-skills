# Excel charts

Always hand-over mode. Give numbered steps. Ask the user to say or paste what they see.

## Steps to hand over

1. Put the chart data in its own small table on a tab named for the chart. One header row. Aggregated, not raw rows.
2. Select the table. Insert, then the chart type from the `viz` chart table: Line for a trend, Clustered Bar (sorted) for a comparison, Histogram for a distribution, Scatter for a relationship.
3. Click the title and type the takeaway.
4. Add axis titles: Chart Elements (the plus sign), Axis Titles. Type the label and the unit.
5. Bars: right-click the value axis, Format Axis, set Minimum to 0.
6. Remove clutter: delete gridlines you do not need, and the legend if you label the series directly (Chart Elements, Data Labels, or a text box at the end of each line).
7. Uncertainty: Chart Elements, Error Bars, More Options, Custom, and point it at the columns that hold the lower and upper distances.

## Notes by check

- **Sorted bars:** sort the source table. Excel plots in table order. For horizontal bars, tick "Categories in reverse order" so the largest is on top.
- **No dual axes:** do not use "Secondary Axis". Make two charts with the same width, one above the other.
- **No 3D:** never pick a 3-D chart type. Remove shadows and bevels under Format.
- **Colour-blind safe:** Page Layout, Colors, pick a palette without a red and green pair, or set each series by hand. Add data labels or markers so colour is not the only signal.
- **Small multiples:** one small chart per series, copied and pasted so the size matches. Set the same axis minimum and maximum on each by hand.
- **Funnel:** Insert, Waterfall or Funnel chart. Add data labels. Put the step conversion in the label text.
- **Cohort heatmap:** a PivotTable (cohort in rows, age in columns) with Conditional Formatting, Color Scales. Leave unreached cells blank.
- **Dates:** make sure the date column is a real date, so the axis spaces evenly.

## Traps

- PivotCharts change when someone changes a filter. Say which filters were set.
- A chart copied as a picture loses its link to the numbers. Keep the workbook.
- Hidden rows drop out of the chart by default.
