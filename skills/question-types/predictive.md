# Predictive questions

Ceiling: "predicts", with out-of-sample performance. Not why. Not "causes". A feature that predicts well is not a lever.

## Before any card

- **What is predicted, for whom, and when?** Write the prediction time. Only data known before that time may be used.
- **What does an error cost?** A missed churner and a false alarm rarely cost the same.
- **What is the baseline?** A model must beat the naive baseline on held-out data, or it is not worth shipping.

## Card: naive and seasonal-naive baselines

- **When to use:** always, first. Before any model, and as the bar every model must beat.
- **Data needed:** the history of the target. For seasonal-naive, at least two full seasons.
- **Key assumptions:** the near future looks like the recent past (naive) or like the same point last season (seasonal-naive).
- **Checks that must pass:**
  1. The baseline is scored on the same held-out periods as any model.
  2. The error metric is stated (MAE, MAPE, or one tied to the cost of an error).
  3. For classification, the baseline is "predict the base rate" and "the simple rule the business uses today".
- **Common failure:** skipping the baseline, so a model with 85% accuracy looks good when the base rate is 90%.
- **Claim allowed:** "Seasonal-naive predicts weekly sign-ups with a mean absolute error of 6%. Any model must beat that."
- **Simplest version first:** this is the simplest version.
- **Tool notes:** SQL: `lag(x, 1)` or `lag(x, 52)` as the forecast, then the error. Python: `shift(1)`, `shift(52)`; `sklearn.dummy.DummyClassifier`. Excel: reference the cell one season back.

## Card: linear and logistic regression

- **When to use:** predict a number (linear) or a yes or no outcome (logistic) from a modest set of features. The first real model to try.
- **Data needed:** one row per unit at prediction time, features known at that time, the outcome observed later.
- **Key assumptions:** the relation is roughly additive. The future units look like the past units.
- **Checks that must pass:**
  1. Split by time: fit on earlier periods, score on later ones.
  2. The leakage checks card passes.
  3. Beats the baseline on held-out data, by a margin that matters.
  4. For logistic: report precision and recall at the chosen threshold, not only accuracy. Choose the threshold from the cost of each error.
  5. Coefficients are not read as effects.
- **Common failure:** random split on time-ordered data; accuracy on an unbalanced outcome; "tenure drives churn" from a coefficient.
- **Claim allowed:** "The model predicts 30-day churn with held-out ROC-AUC 0.74, against 0.61 for the current rule. It does not tell us why customers churn."
- **Simplest version first:** 5 to 10 features a domain expert would pick, no interactions.
- **Tool notes:** SQL: build the feature table as of the prediction date. Python: `sklearn.linear_model.LogisticRegression`, `LinearRegression`, inside a `Pipeline` with scaling; `statsmodels` when you need intervals. Excel: `LINEST` for a first look only.

## Card: forecasting (ETS, ARIMA)

- **When to use:** predict a regular time series (daily or weekly orders) several periods ahead.
- **Data needed:** a complete, evenly spaced series. At least two full seasonal cycles, more is better. Known events (sales, outages) marked.
- **Key assumptions:** the patterns in the history (level, trend, season) continue. No structural break is coming that the model cannot know.
- **Checks that must pass:**
  1. Backtest with a rolling origin (see the next card), at the horizon the decision needs.
  2. Beats seasonal-naive on the backtest.
  3. Residuals show no leftover pattern (plot them, check autocorrelation).
  4. The forecast comes with a prediction interval, and the interval's coverage was checked on the backtest.
  5. Outliers and one-off events were handled in writing, not silently.
- **Common failure:** fitting on a series with a gap or a tracking change; a point forecast with no interval; judging the fit on the same data it was fitted to.
- **Claim allowed:** "We forecast 48,000 orders for December (80% interval 44,000 to 52,500). On the last 8 backtests the error at this horizon averaged 5%."
- **Simplest version first:** seasonal-naive, then ETS with automatic selection. ARIMA only if ETS fails the checks.
- **Tool notes:** SQL: build the clean, gap-free series. Python: `statsmodels.tsa.holtwinters.ExponentialSmoothing`, `statsmodels.tsa.arima.model.ARIMA`, `statsmodels.tsa.statespace.SARIMAX`. Excel: `FORECAST.ETS` and `FORECAST.ETS.CONFINT`.

## Card: backtesting and cross-validation

- **When to use:** every time a model's performance is reported.
- **Data needed:** enough history to hold out several periods or folds.
- **Key assumptions:** the held-out data plays the role of the future. It was never used to make any choice.
- **Checks that must pass:**
  1. Time-ordered data uses time-ordered splits: a rolling origin or expanding window. Never a random shuffle.
  2. Rows from the same customer stay on one side of a split (group split).
  3. Every preprocessing step (scaling, imputation, feature selection) is fitted inside each fold, on the fitting part only.
  4. A final holdout is touched once, at the end. Tuning uses the other folds.
  5. Report the spread across folds, not only the average.
- **Common failure:** tuning on the holdout until it looks good; the same customer on both sides of the split; scaling before splitting.
- **Claim allowed:** "Across 6 rolling monthly backtests, MAE was 4% to 7% (mean 5.2%)."
- **Simplest version first:** one split by date: fit before, score after.
- **Tool notes:** SQL: add a `fold` or `period` column by date. Python: `sklearn.model_selection.TimeSeriesSplit`, `GroupKFold`, `Pipeline`. Excel: not a good fit beyond one holdout period.

## Card: leakage checks

- **When to use:** before trusting any model score. Always when a score looks too good.
- **Data needed:** for every feature: when its value becomes known, and how it is built.
- **Key assumptions:** none. This card is a set of checks.
- **Checks that must pass:**
  1. **Target leakage:** no feature is a result or a restatement of the outcome (a cancellation reason in a churn model, a "last active date" that stops at churn).
  2. **Time leakage:** every feature is computed only from data dated before the prediction time. Check snapshot tables: do they hold today's value or the value at that time?
  3. **Split by time:** the scoring period is after the fitting period.
  4. **Group leakage:** the same customer is not on both sides of the split.
  5. **Preprocessing leakage:** nothing was fitted on the full data before the split.
  6. **Smell test:** list the top features. If one feature carries the model, or the score is far above anything seen before, assume leakage until shown otherwise.
  7. **Feature importance is not causal.** After the checks pass, importance still only says what the model uses. Changing a top feature for a customer may change nothing.
- **Common failure:** a current-state column used to predict the past; an ID or a row order that encodes the outcome.
- **Claim allowed:** none by itself. Passing this card allows the model's held-out score to be reported.
- **Simplest version first:** write the prediction time, then check every feature's date against it.
- **Tool notes:** SQL: build features with `where event_ts < prediction_ts` in every feature CTE. Python: assert max feature date < min scoring date; `Pipeline` for preprocessing. Excel: add an "as of" date column and filter on it.

## Card: gradient boosting

- **When to use:** tabular data, many features, likely interactions and non-linear effects, and the simple regression already beats the baseline but leaves value on the table. Not the first model.
- **Data needed:** one row per unit at prediction time, features known at that time, the outcome observed later. Thousands of rows or more. A time-ordered holdout.
- **Key assumptions:** future rows come from the same process as the rows the model was fitted on. The holdout was never used for any choice.
- **Checks that must pass:**
  1. The leakage checks card passes. Boosted trees find leaks that simple models miss.
  2. Beats the simple regression on a time-ordered holdout, by a margin that matters for the decision. If not, ship the simple model.
  3. Tuning (depth, learning rate, rounds) used cross-validation folds or a validation period. The final holdout was scored once.
  4. Early stopping used a validation set, not the holdout.
  5. The gap between the score on fitted data and on held-out data is reported. A large gap means overfitting.
  6. Performance is checked by segment and by period, not only overall.
  7. Feature importance is reported as "what the model uses", never as cause. Importance splits between correlated features and favours features with many distinct values. Use permutation importance on held-out data.
- **Common failure:** a near-perfect score from a leaked feature; hundreds of tuning runs judged on the holdout; "the top feature drives churn".
- **Claim allowed:** "The model predicts 30-day churn with held-out PR-AUC 0.41, against 0.29 for logistic regression and a base rate of 0.08. Feature importance shows what the model relies on, not what causes churn."
- **Simplest version first:** default settings, modest depth, early stopping on a validation period. Tune only if the default already wins.
- **Tool notes:** SQL: build the feature table as of the prediction date. Python: `sklearn.ensemble.HistGradientBoostingClassifier` (or the regressor), LightGBM or XGBoost; `sklearn.inspection.permutation_importance`. Excel: not a fit.

## Card: classification metrics

- **When to use:** any model that predicts a yes or no outcome. Before a threshold is chosen, and whenever a single score is reported.
- **Data needed:** held-out predictions (scores, not only labels) with the true outcomes. The base rate. The cost of a false positive and of a false negative, in the business's own units.
- **Key assumptions:** the held-out data has the same base rate and mix as the data the model will be used on.
- **Checks that must pass:**
  1. The base rate is stated next to every metric. Accuracy is never reported alone.
  2. Precision and recall are reported at the chosen threshold, with the confusion matrix counts.
  3. ROC-AUC is reported for ranking quality. With a rare outcome (under about 10%), PR-AUC is reported too, against its baseline (the base rate). ROC-AUC alone looks good on rare outcomes.
  4. The threshold is chosen by cost, not left at 0.5. Write the cost of each error, then pick the threshold that minimises expected cost, or the best recall at the capacity the team has (for example, 500 calls a week).
  5. The threshold is chosen on validation data and then scored on the holdout.
  6. Metrics carry uncertainty: a bootstrap interval, or the spread across backtests.
  7. Metrics are shown by key segment. A model can be good overall and useless for new customers.
- **Common failure:** 92% accuracy with an 8% base rate (predicting "no" for everyone scores the same); a threshold of 0.5 on a rare outcome that flags nobody; ROC-AUC 0.85 sold as "85% accurate".
- **Claim allowed:** "At the chosen threshold the model flags 6% of subscribers. 38% of those flagged churn (precision), and it catches 29% of all churners (recall). The base rate is 8%."
- **Simplest version first:** the confusion matrix at one threshold, with precision, recall and the base rate.
- **Tool notes:** SQL: a confusion matrix is four counts with `case when`. Python: `sklearn.metrics.precision_recall_curve`, `roc_auc_score`, `average_precision_score`, `confusion_matrix`. Excel: `COUNTIFS` for the four cells.

## Card: calibration

- **When to use:** the predicted probability itself is used: expected revenue, a risk score shown to a person, a threshold set by cost. Not needed when only the ranking matters.
- **Data needed:** held-out predicted probabilities and outcomes. Enough cases per bin (a few hundred).
- **Key assumptions:** the base rate when the model is used matches the base rate where it was calibrated.
- **Checks that must pass:**
  1. A reliability curve on held-out data: group predictions into bins and compare the mean prediction with the observed rate in each bin. In the bin that says 20%, about 20% of cases happen.
  2. A summary number is reported (Brier score, or expected calibration error), next to the same number for the base-rate baseline.
  3. If calibration is fixed after fitting (Platt scaling or isotonic regression), the fix is fitted on separate data from both the model and the final holdout.
  4. Calibration is checked again whenever the base rate shifts (a new market, a price change, resampled fitting data).
  5. Calibration is checked by key segment.
- **Common failure:** boosted trees and resampled data give scores that rank well but are not probabilities; calibrating and scoring on the same rows.
- **Claim allowed:** "A score of 0.3 means about a 30% chance of churn", only after the reliability curve passes on held-out data.
- **Simplest version first:** a 10-bin reliability table.
- **Tool notes:** SQL: `ntile(10) over (order by score)`, then mean score and mean outcome per bin. Python: `sklearn.calibration.calibration_curve`, `CalibratedClassifierCV`, `sklearn.metrics.brier_score_loss`. Excel: a PivotTable on score bins.

## Allowed wording

- "predicts", "forecast", "expected", with held-out performance and an interval.

## Not allowed

- "because", "drives", "the main cause of churn is" (from feature importance or coefficients).
- Accuracy alone, or any metric with no base rate beside it.
- A score from the data the model was fitted on.
- A forecast with no interval.
