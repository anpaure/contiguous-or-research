#!/usr/bin/env python3
"""Exploratory floating-point decomposition of affine retirement variation.

Diagnostics only; theorem artifacts use exact arithmetic elsewhere.
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict


def profiles(b: int, r: int, p: int, h: int) -> list[int]:
    a = (b - 1) // 2
    z = 0
    out = []
    for q in range(1, h + 1):
        z += ((a * ((p + q) % b)) % b) < r
        out.append(r + z)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("--h", type=int)
    ap.add_argument("--inspect-q", type=int)
    args = ap.parse_args()
    b = args.b
    h = args.h or int(math.sqrt(b * math.log(b)))
    g = b // 4
    logc = [math.lgamma(b + 1) - math.lgamma(k + 1) - math.lgamma(b - k + 1) for k in range(b + 1)]
    scale = max(2 * logc[r] for r in range(g, b - g + 1))
    lr = [math.exp(2 * logc[r] - scale) for r in range(b + 1)]
    paths: list[tuple[int, int, float, list[int]]] = []
    totals = [defaultdict(float) for _ in range(h + 1)]
    for r in range(g, b - g + 1):
        cap = lr[r] / b
        for p in range(b):
            ss = profiles(b, r, p, h)
            paths.append((r, p, cap, ss))
            for q, s in enumerate(ss, 1):
                totals[q][s] += cap
    rho = [dict() for _ in range(h + 1)]
    for q in range(1, h + 1):
        for s, total in totals[q].items():
            quota = math.exp(logc[s] + logc[s - q] - scale) if q <= s <= b else 0.0
            rho[q][s] = min(1.0, quota / total)
    byq1 = defaultdict(float)
    byq2 = defaultdict(float)
    byr1 = defaultdict(float)
    byr2 = defaultdict(float)
    byx1 = defaultdict(float)
    byx2 = defaultdict(float)
    max_inc1 = []
    max_inc2 = []
    envelope = 0.0
    min_pair_violations = []
    pos_transition_profiles = defaultdict(set)
    positive_regular_mass = 0.0
    positive_total_mass = 0.0
    max_positive_regular = []
    positive_regular_r = defaultdict(set)
    regular_gap_by_qr = defaultdict(float)
    positive_count_hist = defaultdict(float)
    for r, p, cap, ss in paths:
        us = [rho[q][ss[q - 1]] for q in range(1, h + 1)]
        running = 1.0
        for value in us:
            running = min(running, value)
            envelope += cap * (value - running)
        for q in range(3, h + 1):
            old_pair = min(us[q - 3], us[q - 2])
            new_pair = min(us[q - 2], us[q - 1])
            if new_pair > old_pair + 1e-13:
                min_pair_violations.append((new_pair - old_pair, q, r, p, old_pair, new_pair))
        for q in range(2, h + 1):
            raw = us[q - 1] - us[q - 2]
            d = max(0.0, raw) * cap
            byq1[q] += d
            byr1[r] += d
            x2 = 2 * ss[q - 1] - b - q
            byx1[x2] += d
            if raw > 0:
                max_inc1.append((raw, q, r, p, ss[q - 2], ss[q - 1], us[q - 2], us[q - 1]))
                pos_transition_profiles[q].add((ss[q - 2], ss[q - 1]))
                oldz = ss[q - 2] - r
                newz = ss[q - 1] - r
                old_regular = (oldz == (q - 1) // 2) if (q - 1) % 2 == 0 else (oldz in {(q - 2) // 2, q // 2})
                new_regular = (newz == q // 2) if q % 2 == 0 else (newz in {(q - 1) // 2, (q + 1) // 2})
                positive_total_mass += cap
                if old_regular and new_regular:
                    positive_regular_mass += cap
                    max_positive_regular.append((raw, q, r, p, oldz, newz))
                    positive_regular_r[q].add(r)
                    regular_gap_by_qr[(q, r)] = max(regular_gap_by_qr[(q, r)], raw)
        positive_count_hist[sum(1 for q in range(2, h + 1) if us[q - 1] > us[q - 2] + 1e-13)] += cap
        for q in range(3, h + 1):
            raw = us[q - 1] - us[q - 3]
            d = max(0.0, raw) * cap
            byq2[q] += d
            byr2[r] += d
            x2 = 2 * ss[q - 1] - b - q
            byx2[x2] += d
            if raw > 0:
                max_inc2.append((raw, q, r, p, ss[q - 3], ss[q - 1], us[q - 3], us[q - 1]))
    w = math.comb(2 * b, b) * math.exp(-scale)
    print("b,h,Wscaled", b, h, w)
    print("A1/W,A2/W,envelope/W", sum(byq1.values()) / w, sum(byq2.values()) / w, envelope / w)
    print("q1", [(q, v / w) for q, v in sorted(byq1.items()) if v / w > 1e-14])
    print("q2", [(q, v / w) for q, v in sorted(byq2.items()) if v / w > 1e-14])
    print("top_r1", sorted(((v / w, r) for r, v in byr1.items()), reverse=True)[:20])
    print("top_r2", sorted(((v / w, r) for r, v in byr2.items()), reverse=True)[:20])
    print("top_x1", sorted(((v / w, x) for x, v in byx1.items()), reverse=True)[:20])
    print("top_x2", sorted(((v / w, x) for x, v in byx2.items()), reverse=True)[:20])
    mono = []
    rho_mono = []
    for q in range(1, h - 1):
        for s, old_total in totals[q].items():
            if s + 1 not in totals[q + 2]:
                continue
            old_quota = math.exp(logc[s] + logc[s - q] - scale) if q <= s <= b else 0.0
            new_quota = math.exp(logc[s + 1] + logc[s - q - 1] - scale) if q + 2 <= s + 1 <= b else 0.0
            old_ratio = old_total / old_quota if old_quota else math.inf
            new_ratio = totals[q + 2][s + 1] / new_quota if new_quota else math.inf
            if new_ratio + 1e-13 < old_ratio:
                mono.append((old_ratio - new_ratio, q, s, old_ratio, new_ratio))
            old_rho = min(1.0, 1.0 / old_ratio)
            new_rho = min(1.0, 1.0 / new_ratio)
            if new_rho > old_rho + 1e-13:
                rho_mono.append((new_rho - old_rho, q, s, old_rho, new_rho))
    print("top_nondefect_R_violations", sorted(mono, reverse=True)[:20])
    print("top_nondefect_rho_violations", sorted(rho_mono, reverse=True)[:20])
    print("max_path_inc1", sorted(max_inc1, reverse=True)[:20])
    print("max_path_inc2", sorted(max_inc2, reverse=True)[:20])
    print("min_pair_violations", sorted(min_pair_violations, reverse=True)[:20])
    print("positive_transition_profile_counts", [(q, len(v), sorted(v)) for q, v in sorted(pos_transition_profiles.items())])
    print("positive_regular_capacity/W", positive_regular_mass / w, "positive_total_capacity/W", positive_total_mass / w)
    print("max_positive_regular", sorted(max_positive_regular, reverse=True)[:20])
    print("positive_regular_r_counts", [(q, len(v), min(v), max(v)) for q, v in sorted(positive_regular_r.items())])
    print("positive_count_hist/W", [(k, v / w) for k, v in sorted(positive_count_hist.items())])
    if args.inspect_q:
        print("regular_gaps_at_q", args.inspect_q,
              [(r, regular_gap_by_qr[(args.inspect_q, r)],
                regular_gap_by_qr[(args.inspect_q, r)] * b)
               for r in sorted(positive_regular_r.get(args.inspect_q, set()))])


if __name__ == "__main__":
    main()
