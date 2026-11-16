# Case 8: weekly order forecast (clean)

Type: method choice, predictive, clean. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"We need a forecast of weekly orders for the next 8 weeks, for warehouse staffing. We have 3 years of weekly orders with no gaps. Promotions are marked. Which method, and how do we know it is any good?"

## Pass

- Question type: predictive.
- Method: seasonal-naive baseline first, then ETS. ARIMA only if ETS fails its checks. No machine learning model proposed as the first step.
- Names the checks: rolling-origin backtests at the 8-week horizon, must beat seasonal-naive, residuals show no leftover pattern, a prediction interval whose coverage was checked on the backtests, promotions handled in writing.
- Asks what an error costs (too few staff against too many), to pick the error metric and the interval to plan to.
- States the claim allowed: a forecast with an interval and the backtest error.
- Invents no problem with the data described.

## Fail

- Jumps to gradient boosting or a neural model.
- Gives a point forecast with no interval.
- Judges the fit on the data the model was fitted to.
