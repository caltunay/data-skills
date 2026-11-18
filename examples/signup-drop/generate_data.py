#!/usr/bin/env python3
"""Generate invented data for the sign-up drop example.

Everything here is made up. Fixed seed, standard library only.
Writes data/signups.csv, data/daily_spend.csv and data/dashboard_monthly.csv.

Planted on purpose, for the skills to find:
- paid social sign-ups fall by about 65% from 2 March 2026
- paid social spend is cut on the same day (timing only, no proof of cause)
- about 1.5% of sign-up rows are duplicated by a late update
- about 2% of rows are test accounts
- March has 3 more days than February
"""
import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 20260316
START = date(2026, 1, 1)
END = date(2026, 3, 31)
CUT_DATE = date(2026, 3, 2)

# channel: (mean sign-ups per weekday, share on mobile)
CHANNELS = {
    "organic": (14.0, 0.50),
    "paid_search": (9.0, 0.45),
    "paid_social": (16.0, 0.85),
    "referral": (4.0, 0.60),
    "email": (3.0, 0.40),
}
COUNTRIES = [("GB", 0.5), ("DE", 0.3), ("FR", 0.2)]
PLANS = [("monthly", 0.7), ("annual", 0.3)]
SPEND = {"paid_search": 300.0, "paid_social": 400.0}


def pick(rng, weighted):
    r = rng.random()
    total = 0.0
    for value, weight in weighted:
        total += weight
        if r < total:
            return value
    return weighted[-1][0]


def poisson(rng, mean):
    # Knuth's method. Fine for small means.
    limit = 2.718281828459045 ** (-mean)
    k, p = 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


def main():
    rng = random.Random(SEED)
    out = Path(__file__).parent / "data"
    out.mkdir(exist_ok=True)

    rows = []
    spend_rows = []
    next_id = 100001
    day = START
    while day <= END:
        weekend = day.weekday() >= 5
        for channel, (mean, mobile_share) in CHANNELS.items():
            rate = mean * (0.8 if weekend else 1.0)
            if channel == "paid_social" and day >= CUT_DATE:
                rate *= 0.35
            for _ in range(poisson(rng, rate)):
                ts = datetime(day.year, day.month, day.day) + timedelta(seconds=rng.randrange(86400))
                rows.append({
                    "signup_id": next_id,
                    "account_id": f"A{next_id}",
                    "signup_ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                    "channel": channel,
                    "platform": "mobile" if rng.random() < mobile_share else "desktop",
                    "plan": pick(rng, PLANS),
                    "country": pick(rng, COUNTRIES),
                    "is_test": 1 if rng.random() < 0.02 else 0,
                    "updated_ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                })
                next_id += 1
        for channel, base in SPEND.items():
            amount = base
            if channel == "paid_social" and day >= CUT_DATE:
                amount = 140.0
            amount *= rng.uniform(0.95, 1.05)
            spend_rows.append({"spend_date": day.isoformat(), "channel": channel, "spend": round(amount, 2)})
        day += timedelta(days=1)

    # late updates: a second row for the same signup_id, with a later updated_ts
    duplicates = []
    for row in rows:
        if rng.random() < 0.015:
            late = dict(row)
            updated = datetime.strptime(row["signup_ts"], "%Y-%m-%d %H:%M:%S") + timedelta(hours=rng.randrange(2, 48))
            late["updated_ts"] = updated.strftime("%Y-%m-%d %H:%M:%S")
            duplicates.append(late)
    all_rows = rows + duplicates
    rng.shuffle(all_rows)

    with open(out / "signups.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(all_rows)

    with open(out / "daily_spend.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["spend_date", "channel", "spend"])
        writer.writeheader()
        writer.writerows(spend_rows)

    # the "growth dashboard": the trusted number. It counts real accounts once.
    # It closes each month a few minutes early, so it runs a little under the table.
    monthly = {}
    for row in rows:
        if row["is_test"] == 0:
            month = row["signup_ts"][:7]
            monthly[month] = monthly.get(month, 0) + 1
    with open(out / "dashboard_monthly.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "signups"])
        for month in sorted(monthly):
            writer.writerow([month, monthly[month] - rng.randrange(1, 5)])

    print(f"signups.csv: {len(all_rows)} rows ({len(duplicates)} late-update duplicates)")
    print(f"daily_spend.csv: {len(spend_rows)} rows")
    print("dashboard_monthly.csv:", {m: monthly[m] for m in sorted(monthly)})


if __name__ == "__main__":
    main()
