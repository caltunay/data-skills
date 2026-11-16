#!/usr/bin/env python3
"""Run an example's queries with SQLite and print the results.

Usage: python3 examples/run_queries.py examples/signup-drop

Loads every CSV in <example>/data into an in-memory SQLite database (table name = file name),
runs every .sql file in <example>/queries in name order, and writes the results to
<example>/outputs/results.txt. Standard library only.
"""
import csv
import sqlite3
import sys
from pathlib import Path


def load(conn, path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    cols = ", ".join(f'"{c}"' for c in header)
    conn.execute(f'create table "{path.stem}" ({cols})')
    marks = ", ".join("?" for _ in header)
    conn.executemany(f'insert into "{path.stem}" values ({marks})', rows)
    # let SQLite treat numbers as numbers
    for c in header:
        try:
            [float(r[header.index(c)]) for r in rows[:200] if r[header.index(c)] != ""]
        except ValueError:
            continue
        conn.execute(f'update "{path.stem}" set "{c}" = cast("{c}" as real) where "{c}" <> \'\'')
        if all(float(r[header.index(c)]).is_integer() for r in rows[:200] if r[header.index(c)] != ""):
            conn.execute(f'update "{path.stem}" set "{c}" = cast("{c}" as integer) where "{c}" <> \'\'')


def fmt(value):
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return "" if value is None else str(value)


def main():
    example = Path(sys.argv[1])
    conn = sqlite3.connect(":memory:")
    for path in sorted((example / "data").glob("*.csv")):
        load(conn, path)
    lines = []
    for path in sorted((example / "queries").glob("*.sql")):
        sql = path.read_text()
        lines.append(f"=== {path.name}")
        for line in sql.splitlines():
            if line.startswith("--"):
                lines.append(line)
        # a file may hold setup statements (views) before the final select
        body = "\n".join(line for line in sql.splitlines() if not line.startswith("--"))
        statements = [s.strip() for s in body.split(";") if s.strip()]
        cursor = None
        for statement in statements:
            cursor = conn.execute(statement)
        if cursor is not None and cursor.description:
            header = [d[0] for d in cursor.description]
            rows = [[fmt(v) for v in row] for row in cursor.fetchall()]
            widths = [max(len(header[i]), *(len(r[i]) for r in rows)) if rows else len(header[i]) for i in range(len(header))]
            lines.append(" | ".join(h.ljust(w) for h, w in zip(header, widths)))
            lines.append("-|-".join("-" * w for w in widths))
            for r in rows:
                lines.append(" | ".join(v.ljust(w) for v, w in zip(r, widths)))
            lines.append(f"({len(rows)} rows)")
        lines.append("")
    (example / "outputs").mkdir(exist_ok=True)
    (example / "outputs" / "results.txt").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
