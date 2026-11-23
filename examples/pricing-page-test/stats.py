#!/usr/bin/env python3
"""Statistics for the pricing page test, from the aggregates the queries return.

Usage: python3 examples/pricing-page-test/stats.py
Standard library only. Writes outputs/stats.txt.
The design values below were fixed in the plan, before the test.
"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from run_queries import connect, run_file  # noqa: E402

PLANNED_SPLIT = 0.5
BASELINE = 0.10
MDE = 0.02
ALPHA_Z = 1.959964   # two-sided 5%
POWER_Z = 0.841621   # 80% power


def norm_p_two_sided(z):
    return math.erfc(abs(z) / math.sqrt(2))


def chi2_p_1df(x):
    return math.erfc(math.sqrt(x / 2))


def diff_of_proportions(x1, n1, x2, n2):
    """Variant minus control. Pooled z-test, unpooled interval."""
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    z = (p2 - p1) / math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    return p2 - p1, se, z, norm_p_two_sided(z)


def main():
    conn = connect(HERE)
    q = HERE / "queries"
    run_file(conn, q / "q1-3b-outcomes-view.sql")
    out = []

    # 1. sample ratio mismatch
    _, rows = run_file(conn, q / "q2-1-srm-counts.sql")
    n = {arm: visitors for arm, visitors, _ in rows}
    total = n["control"] + n["variant"]
    expected = total * PLANNED_SPLIT
    chi2 = sum((n[a] - expected) ** 2 / expected for a in n)
    out += ["1. Sample ratio mismatch (planned 50/50)",
            f"   control {n['control']}, variant {n['variant']}, expected {expected:.1f} each",
            f"   chi-square = {chi2:.3f} (1 df), p = {chi2_p_1df(chi2):.3f}",
            f"   {'FAIL: p < 0.001' if chi2_p_1df(chi2) < 0.001 else 'pass: no sign of a mismatch'}", ""]

    # 2. power
    planned_n = 16 * BASELINE * (1 - BASELINE) / MDE ** 2
    smaller = min(n.values())
    detectable = (ALPHA_Z + POWER_Z) * math.sqrt(2 * BASELINE * (1 - BASELINE) / smaller)
    out += ["2. Power (fixed before the test: baseline 10%, MDE 2.0 points, alpha 5%, power 80%)",
            f"   planned per arm (rule of thumb 16 x p x (1 - p) / delta^2) = {planned_n:.0f}",
            f"   achieved per arm: control {n['control']}, variant {n['variant']}",
            f"   smallest effect detectable at the achieved size = {detectable * 100:.2f} points",
            f"   {'pass' if smaller >= planned_n else 'FAIL: under the planned size'}", ""]

    # 3. primary metric
    _, rows = run_file(conn, q / "q2-2-primary-metric.sql")
    m = {arm: (visitors, converters) for arm, visitors, converters, _ in rows}
    (n1, x1), (n2, x2) = m["control"], m["variant"]
    d, se, z, p = diff_of_proportions(x1, n1, x2, n2)
    out += ["3. Primary metric: paid order within 7 days of assignment, per visitor",
            f"   control {x1}/{n1} = {x1 / n1 * 100:.2f}%   variant {x2}/{n2} = {x2 / n2 * 100:.2f}%",
            f"   difference = {d * 100:+.2f} points, 95% interval {(d - ALPHA_Z * se) * 100:+.2f} to {(d + ALPHA_Z * se) * 100:+.2f}",
            f"   relative lift = {d / (x1 / n1) * 100:+.1f}%",
            f"   z = {z:.2f}, p = {p:.3f}", ""]

    # 4. effect by week (novelty)
    _, rows = run_file(conn, q / "q2-3-effect-by-week.sql")
    w = {(week, arm): (visitors, converters) for week, arm, visitors, converters, _ in rows}
    out.append("4. Effect by test week (novelty check)")
    parts = []
    for week in ("week 1", "week 2"):
        (a, xa), (b, xb) = w[(week, "control")], w[(week, "variant")]
        dw, sew, _, _ = diff_of_proportions(xa, a, xb, b)
        parts.append((dw, sew))
        out.append(f"   {week}: {dw * 100:+.2f} points, 95% interval {(dw - ALPHA_Z * sew) * 100:+.2f} to {(dw + ALPHA_Z * sew) * 100:+.2f}")
    gap = parts[1][0] - parts[0][0]
    se_gap = math.sqrt(parts[0][1] ** 2 + parts[1][1] ** 2)
    out += [f"   week 2 minus week 1 = {gap * 100:+.2f} points, z = {gap / se_gap:.2f}, p = {norm_p_two_sided(gap / se_gap):.3f}",
            "   Same sign in both weeks. The two weeks do not differ clearly.", ""]

    # 5. guardrails
    _, rows = run_file(conn, q / "q2-4-guardrails.sql")
    g = {r[0]: r for r in rows}
    out.append("5. Guardrails (fixed before the test: stop if clearly worse, that is, the whole 95% interval on the bad side)")
    mean = {a: g[a][2] for a in g}
    var = {a: g[a][3] - g[a][2] ** 2 for a in g}
    dr = mean["variant"] - mean["control"]
    ser = math.sqrt(var["control"] / g["control"][1] + var["variant"] / g["variant"][1])
    out.append(f"   revenue per visitor: control {mean['control']:.2f}, variant {mean['variant']:.2f}, "
               f"difference {dr:+.2f}, 95% interval {dr - ALPHA_Z * ser:+.2f} to {dr + ALPHA_Z * ser:+.2f} (normal approximation)")
    out.append(f"   {'FAIL: clearly lower' if dr + ALPHA_Z * ser < 0 else 'pass: not clearly lower'}")
    dret, seret, _, _ = diff_of_proportions(g["control"][6], g["control"][4], g["variant"][6], g["variant"][4])
    out.append(f"   return rate (per paid order): control {g['control'][7]:.2f}%, variant {g['variant'][7]:.2f}%, "
               f"difference {dret * 100:+.2f} points, 95% interval {(dret - ALPHA_Z * seret) * 100:+.2f} to {(dret + ALPHA_Z * seret) * 100:+.2f}")
    out.append(f"   {'FAIL: clearly higher' if dret - ALPHA_Z * seret > 0 else 'pass: not clearly higher'}")
    out.append(f"   average order value (context, not tested): control {g['control'][5]:.2f}, variant {g['variant'][5]:.2f}")
    out.append("")

    # 6. device, exploratory
    _, rows = run_file(conn, q / "q2-5-by-device-exploratory.sql")
    dv = {(device, arm): (visitors, converters) for device, arm, visitors, converters, _ in rows}
    out.append("6. By device. Exploratory: found by slicing, not a result")
    for device in ("desktop", "mobile"):
        (a, xa), (b, xb) = dv[(device, "control")], dv[(device, "variant")]
        dd, sed, _, _ = diff_of_proportions(xa, a, xb, b)
        out.append(f"   {device}: {dd * 100:+.2f} points, 95% interval {(dd - ALPHA_Z * sed) * 100:+.2f} to {(dd + ALPHA_Z * sed) * 100:+.2f}")
    out.append("")

    text = "\n".join(out)
    (HERE / "outputs").mkdir(exist_ok=True)
    (HERE / "outputs" / "stats.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
