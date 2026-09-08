#!/usr/bin/env python3
"""Enumerate exact path-feasibility states around odd two-step affine defects."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict

from research_affine_histogram_recurrence_20260821 import rho_odd


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("H", type=int)
    ap.add_argument("kmax", type=int)
    z = ap.parse_args()
    b, H = z.b, z.H
    m = (b - 1) // 2
    states = Counter()
    violations = []
    feasible = defaultdict(set)
    for k in range(z.kmax + 1):
        r = m + 1 + k
        bits = [int((m * x) % b < r) for x in range(b)]
        for p in range(b):
            pref = [0]
            for q in range(1, H + 5):
                pref.append(pref[-1] + bits[(p + q) % b])
            for u in range(1, (H - 4) // 2 + 1):
                q = 2 * u + 1
                zz = pref[q]
                K = k + zz - u
                pair1 = pref[q + 2] - pref[q]
                pair2 = pref[q + 4] - pref[q + 2]
                if pair1 != 2:
                    continue
                old = rho_odd(b, u, K)
                bump = rho_odd(b, u + 1, K + 1) - old
                if bump <= 1e-14:
                    continue
                d = K - k
                states[(pair2, d)] += 1
                feasible[(u, K, pair2)].add((k, d))
                K2 = K + (2 if pair2 == 2 else 1 if pair2 == 1 else 0)
                end = rho_odd(b, u + 2, K2)
                if end > old + 1e-13:
                    violations.append((end - old, b, u, K, k, d, p, pair2, old, end))
    print("STATE_COUNTS", sorted(states.items()))
    print("MAX_VIOLATIONS", sorted(violations, reverse=True)[:20])
    summaries = []
    for key, vals in sorted(feasible.items()):
        u, K, pair2 = key
        ks = [a for a, _ in vals]
        ds = [a for _, a in vals]
        summaries.append((u, K, pair2, min(ks), max(ks), min(ds), max(ds), len(vals)))
    print("FEASIBLE_HEAD", summaries[:100])
    print("FEASIBLE_TAIL", summaries[-100:])


if __name__ == "__main__":
    main()
