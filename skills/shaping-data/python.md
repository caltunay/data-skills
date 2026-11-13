# Python (pandas or polars)

Ask which library if the data map does not say. Follow PEP 8 unless the data map Conventions say otherwise.

## Style

- 4-space indent, snake_case names, lines under 88 characters.
- Small functions with one job. Named steps, not one long chain.
- Type hints on function signatures where it helps.
- No hidden state. Pass data in, return data out.
- Set a random seed when any step is random.

## Pattern (pandas)

```python
import pandas as pd

orders = pd.read_csv("orders.csv", parse_dates=["order_ts"])
customers = pd.read_csv("customers.csv")

paid_orders = orders.loc[
    (orders["status"] == "paid")
    & (orders["order_ts"] >= "2026-01-01")
    & (orders["order_ts"] < "2026-02-01")
]

joined = paid_orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
assert len(joined) == len(paid_orders), "join changed the row count"
```

## Checks

- `validate="many_to_one"` (pandas) or an explicit uniqueness check (polars: `df.select(pl.col("id").is_duplicated().any())`).
- Row count before and after every merge.
- `df.isna().sum()` for nulls, `df.duplicated(subset=keys).sum()` for duplicates.
- `df.describe()` and a look at the top and bottom rows.
- Check dtypes after reading. Dates read as strings are a common bug.

## Long vs wide

- pandas: `melt` for long, `pivot_table` for wide.
- polars: `unpivot` for long, `pivot` for wide.

## Do not

- Do not mutate input frames in place.
- Do not use `inplace=True`.
- Do not loop over rows when a vector operation works.
- Do not save row-level output without asking the user.
