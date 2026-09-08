#!/usr/bin/env python3
"""Numerical structure probe for affine retirement positive variation.

Research-only.  All reported sums are normalized by W_b and evaluated in
double precision after log-gamma normalization.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def logchoose(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def run(b: int, h: int) -> None:
    assert b % 2 == 1 and h < b // 4
    mult = (b - 1) // 2
    g = b // 4
    logw = logchoose(2 * b, b)
    rs = list(range(g, b - g + 1))
    rweight = {
        r: math.exp(2 * logchoose(b, r) - math.log(b) - logw) for r in rs
    }

    # Profiles indexed by q,s; entries are T/W.
    totals = np.zeros((h + 1, 2 * b + 1), dtype=np.float64)
    profiles: dict[int, np.ndarray] = {}
    bits_by_r: dict[int, np.ndarray] = {}
    phases = np.arange(b, dtype=np.int64)
    for r in rs:
        bits = (((mult * phases) % b) < r).astype(np.int8)
        bits_by_r[r] = bits
        prof = np.empty((b, h), dtype=np.int16)
        z = np.zeros(b, dtype=np.int16)
        for q in range(1, h + 1):
            z += bits[(phases + q) % b]
            prof[:, q - 1] = r + z
            totals[q] += np.bincount(prof[:, q - 1], minlength=2 * b + 1) * rweight[r]
        profiles[r] = prof

    rho = np.zeros_like(totals)
    for q in range(1, h + 1):
        for s in np.flatnonzero(totals[q] > 0):
            pnorm = math.exp(logchoose(b, int(s)) + logchoose(b, int(s) - q) - logw)
            rho[q, s] = min(1.0, pnorm / totals[q, s])

    a1 = 0.0
    a1_eventmass = 0.0
    a2 = 0.0
    a2_same = 0.0
    a2_alt = 0.0
    a2_same_events = 0.0
    a2_alt_events = 0.0
    max1 = (-1.0, None)
    max2_same = (-1.0, None)
    max2_alt = (-1.0, None)
    byq1 = np.zeros(h + 1)
    byq2_same = np.zeros(h + 1)
    byq2_alt = np.zeros(h + 1)
    support_same = np.zeros(h + 1)
    support_alt = np.zeros(h + 1)
    a2_by_source: dict[int, float] = {}
    a2_event_by_source: dict[int, float] = {}
    for r in rs:
        prof = profiles[r]
        bits = bits_by_r[r]
        w = rweight[r]
        for p in range(b):
            vals = np.array([rho[q, prof[p, q - 1]] for q in range(1, h + 1)])
            d1 = np.maximum(vals[1:] - vals[:-1], 0.0)
            a1 += w * d1.sum()
            a1_eventmass += w * np.count_nonzero(d1 > 0)
            byq1[2:] += w * d1
            j = int(np.argmax(d1)) if len(d1) else 0
            if len(d1) and d1[j] > max1[0]:
                max1 = (float(d1[j]), (r, p, j + 1, j + 2, int(prof[p, j]), int(prof[p, j + 1]), vals[j], vals[j + 1]))
            for q in range(3, h + 1):
                d = max(vals[q - 1] - vals[q - 3], 0.0)
                same = bits[(p + q - 1) % b] == bits[(p + q) % b]
                a2 += w * d
                if same:
                    support_same[q] += w
                    if d > 0:
                        a2_same_events += w
                        kk = abs(2 * r - b) // 2
                        a2_by_source[kk] = a2_by_source.get(kk, 0.0) + w * d
                        a2_event_by_source[kk] = a2_event_by_source.get(kk, 0.0) + w
                    a2_same += w * d
                    byq2_same[q] += w * d
                    if d > max2_same[0]:
                        max2_same = (d, (r, p, q - 2, q, int(prof[p, q - 3]), int(prof[p, q - 1]), vals[q - 3], vals[q - 1]))
                else:
                    support_alt[q] += w
                    if d > 0:
                        a2_alt_events += w
                    a2_alt += w * d
                    byq2_alt[q] += w * d
                    if d > max2_alt[0]:
                        max2_alt = (d, (r, p, q - 2, q, int(prof[p, q - 3]), int(prof[p, q - 1]), vals[q - 3], vals[q - 1]))

    source_mass = sum(b * rweight[r] for r in rs)
    defect_mass_exact = sum(rweight[r] * abs(2 * r - b) for r in rs)
    print("ROW", b, h)
    print("mass", source_mass, "defect", defect_mass_exact, "sqrtb*defect", math.sqrt(b) * defect_mass_exact)
    print("A1", a1, "eventmass", a1_eventmass, "avg", a1 / max(a1_eventmass, 1e-300), "b/H*A1", b / h * a1, "max", max1)
    print("A2", a2, "same", a2_same, "alt", a2_alt, "b2/H2*A2", b * b / (h * h) * a2)
    print("A2eventmass", a2_same_events, a2_alt_events, "support", support_same.sum(), support_alt.sum())
    print("max2same", max2_same)
    print("max2alt", max2_alt)
    q1 = sorted(((byq1[q], q) for q in range(2, h + 1)), reverse=True)[:8]
    q2s = sorted(((byq2_same[q], q) for q in range(3, h + 1)), reverse=True)[:8]
    q2a = sorted(((byq2_alt[q], q) for q in range(3, h + 1)), reverse=True)[:8]
    print("topq1", q1)
    print("topq2same", q2s)
    print("topq2alt", q2a)
    print("topsourceA2", sorted(((v, k, a2_event_by_source[k]) for k, v in a2_by_source.items()), reverse=True)[:15])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("h", type=int, nargs="?")
    args = ap.parse_args()
    h = args.h or int(math.sqrt(args.b * math.log(args.b)))
    run(args.b, h)


if __name__ == "__main__":
    main()
