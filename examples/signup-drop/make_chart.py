#!/usr/bin/env python3
"""Draw the readout chart for the sign-up example as an SVG. Standard library only.

Usage: python3 examples/signup-drop/make_chart.py

Runs queries/q4-2-daily-series-feb-mar.sql (after the clean view in q1-3c) with SQLite and
writes outputs/signups-daily-feb-mar.svg.
"""
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
from run_queries import connect, run_file  # noqa: E402


def main():
    conn = connect(here)
    run_file(conn, here / "queries" / "q1-3c-clean-view.sql")
    _, rows = run_file(conn, here / "queries" / "q4-2-daily-series-feb-mar.sql")
    days = [r[0] for r in rows]
    values = [int(r[1]) for r in rows]

    width, height = 760, 400
    left, right, top, bottom = 60, 20, 70, 70
    plot_w, plot_h = width - left - right, height - top - bottom
    y_max = 60

    def x(i):
        return left + plot_w * i / (len(days) - 1)

    def y(v):
        return top + plot_h * (1 - v / y_max)

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
               f'viewBox="0 0 {width} {height}" font-family="sans-serif" font-size="12">')
    out.append('<title>Sign-ups per day stepped down from about 42 to about 31 on 2 March</title>')
    out.append(f'<rect width="{width}" height="{height}" fill="#ffffff"/>')
    out.append(f'<text x="{left}" y="28" font-size="16" font-weight="bold">'
               'Sign-ups per day stepped down on 2 March and stayed lower</text>')
    out.append(f'<text x="{left}" y="48" fill="#444444">Daily sign-ups, February and March 2026, UTC</text>')
    for v in range(0, y_max + 1, 10):
        out.append(f'<line x1="{left}" x2="{width - right}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="#e5e5e5"/>')
        out.append(f'<text x="{left - 8}" y="{y(v) + 4:.1f}" text-anchor="end" fill="#444444">{v}</text>')
    out.append(f'<text x="16" y="{top + plot_h / 2:.0f}" transform="rotate(-90 16 {top + plot_h / 2:.0f})" '
               'text-anchor="middle" fill="#444444">Sign-ups per day (count)</text>')
    for i, d in enumerate(days):
        if d.endswith("-01") or d.endswith("-15"):
            label = ("1 " if d.endswith("-01") else "15 ") + ("Feb" if d[5:7] == "02" else "Mar")
            out.append(f'<text x="{x(i):.1f}" y="{top + plot_h + 18}" text-anchor="middle" fill="#444444">{label}</text>')
    points = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(values))
    out.append(f'<polyline points="{points}" fill="none" stroke="#0072B2" stroke-width="2"/>')
    step = days.index("2026-03-02")
    out.append(f'<line x1="{x(step):.1f}" x2="{x(step):.1f}" y1="{top}" y2="{top + plot_h}" '
               'stroke="#D55E00" stroke-width="1.5" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{x(step) + 6:.1f}" y="{top + 12}" fill="#D55E00">2 March: paid social spend cut the same week</text>')
    out.append(f'<text x="{left}" y="{height - 20}" fill="#666666">Source: signups table, test accounts out, '
               'one row per sign-up after dedup. n = 2,148 sign-ups.</text>')
    out.append('</svg>')
    (here / "outputs").mkdir(exist_ok=True)
    path = here / "outputs" / "signups-daily-feb-mar.svg"
    path.write_text("\n".join(out) + "\n")
    print(path)


if __name__ == "__main__":
    main()
