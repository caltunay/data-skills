#!/usr/bin/env python3
"""Generate invented data for the pricing page A/B test example.

Everything here is made up. Fixed seed, standard library only.
Writes data/assignments.csv, data/orders.csv and data/platform_counts.csv.

Built in on purpose:
- random 50/50 assignment by visitor, 2 to 15 February 2026 (two full weeks)
- control converts at about 10%, variant at about 12.4% (paid order within 7 days)
- some visitors place more than one order (a join fan-out trap)
- some orders are cancelled, some fall after the 7-day window
- about 1.5% of visitors are internal staff
- order value and return rate are the same in both arms
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 20260202
START = datetime(2026, 2, 2)
DAYS = 14
VISITORS_PER_DAY = 560
RATE = {"control": 0.100, "variant": 0.124}


def main():
    rng = random.Random(SEED)
    out = Path(__file__).parent / "data"
    out.mkdir(exist_ok=True)

    assignments, orders = [], []
    visitor_id, order_id = 500001, 900001
    for day in range(DAYS):
        weekend = (START + timedelta(days=day)).weekday() >= 5
        n = int(rng.gauss(VISITORS_PER_DAY * (0.85 if weekend else 1.0), 20))
        for _ in range(n):
            assigned = START + timedelta(days=day, seconds=rng.randrange(86400))
            arm = "variant" if rng.random() < 0.5 else "control"
            device = "mobile" if rng.random() < 0.6 else "desktop"
            internal = 1 if rng.random() < 0.015 else 0
            assignments.append({
                "visitor_id": visitor_id,
                "arm": arm,
                "assigned_ts": assigned.strftime("%Y-%m-%d %H:%M:%S"),
                "device": device,
                "is_internal": internal,
            })
            if rng.random() < RATE[arm]:
                # first paid order, usually soon after the visit
                gap = min(rng.expovariate(1 / 18.0), 7 * 24 - 0.1)
                first = assigned + timedelta(hours=gap)
                n_orders = 1 + (1 if rng.random() < 0.18 else 0) + (1 if rng.random() < 0.04 else 0)
                for k in range(n_orders):
                    ts = first + timedelta(hours=k * rng.uniform(20, 90))
                    orders.append({
                        "order_id": order_id,
                        "visitor_id": visitor_id,
                        "order_ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                        "amount": round(rng.lognormvariate(3.6, 0.5), 2),
                        "status": "paid",
                        "is_returned": 1 if rng.random() < 0.08 else 0,
                    })
                    order_id += 1
            elif rng.random() < 0.012:
                # an order that was cancelled: must not count
                ts = assigned + timedelta(hours=rng.uniform(0.2, 60))
                orders.append({
                    "order_id": order_id, "visitor_id": visitor_id,
                    "order_ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                    "amount": round(rng.lognormvariate(3.6, 0.5), 2),
                    "status": "cancelled", "is_returned": 0,
                })
                order_id += 1
            elif rng.random() < 0.01:
                # a paid order after the 7-day window: must not count
                ts = assigned + timedelta(days=rng.uniform(7.2, 12))
                orders.append({
                    "order_id": order_id, "visitor_id": visitor_id,
                    "order_ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                    "amount": round(rng.lognormvariate(3.6, 0.5), 2),
                    "status": "paid", "is_returned": 0,
                })
                order_id += 1
            visitor_id += 1

    rng.shuffle(orders)
    with open(out / "assignments.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(assignments[0].keys()))
        writer.writeheader()
        writer.writerows(assignments)
    with open(out / "orders.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(orders[0].keys()))
        writer.writeheader()
        writer.writerows(orders)

    # the experiment platform's own exposure counts: the trusted number
    counts = {"control": 0, "variant": 0}
    for row in assignments:
        counts[row["arm"]] += 1
    with open(out / "platform_counts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["arm", "visitors_assigned"])
        for arm in ("control", "variant"):
            writer.writerow([arm, counts[arm]])

    print(f"assignments.csv: {len(assignments)} rows {counts}")
    print(f"orders.csv: {len(orders)} rows")


if __name__ == "__main__":
    main()
