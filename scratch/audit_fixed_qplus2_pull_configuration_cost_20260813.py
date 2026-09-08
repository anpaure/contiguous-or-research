#!/usr/bin/env python3
"""Audit fixed-period q+2 configuration cost for corrected pull coefficients.

Substantive runs are intended for ssh h100, not the local workstation.
"""

from __future__ import annotations

import argparse
import math


def deadline(k: int) -> tuple[int, int, int, int]:
    r = (k + 1) // 2
    w = math.comb(k, r)
    lower = sum(math.comb(k, s) for s in range(1, r))
    d = 0
    while d * w + d * (d + 1) // 2 < lower:
        d += 1
    return r, w, lower, d


def ferrers_columns(d: int, h: int) -> list[int]:
    b = [0] * (d + 1)
    left = h
    for s in range(1, d + 1):
        take = min(d - s + 1, left)
        b[s] = take
        left -= take
    assert left == 0
    return b


def costs(k: int):
    r, w, lower, d = deadline(k)
    c = r - d - 1
    if c <= 0:
        return r, d, c, 0.0, 0.0, []
    h_boundary = max(0, lower - d * w)
    b = ferrers_columns(d, h_boundary)

    def qs(s: int) -> float:
        return (math.comb(k, s) - (b[s] if s <= d else 0)) / w

    a = [0.0] + [qs(c - t + 1) for t in range(1, c + 1)] + [0.0]
    g = [0.0] + [1.0 - qs(c + j) for j in range(1, d + 1)]
    hh = sum(g)
    if hh == 0.0:
        return r, d, c, 0.0, 0.0, []
    ww = [0.0] + [g[j] / hh for j in range(1, d + 1)] + [0.0, 0.0]
    delta = [0.0] + [ww[j] - ww[j + 1] for j in range(1, d + 2)]
    n = d + 3
    by_j = []
    ordinary = 0.0
    fixed = 0.0
    min_x = 1.0
    for j in range(1, d + 1):
        xj = 0.0
        for dd in range(1, c + 1):
            x = a[dd] * delta[j] - a[dd + 1] * delta[j + 1]
            min_x = min(min_x, x)
            xj += x
        ordinary += (j + 1) * xj
        fixed += n / (n // (j + 1)) * xj
        by_j.append(xj)
    if n % 2 == 0:
        half = n // 2
        long_gate = n * (0.5 * by_j[half - 2] + sum(by_j[half - 1 :]))
    else:
        half = n // 2
        long_gate = n * sum(by_j[half:])
    return r, d, c, ordinary, fixed, by_j, min_x, h_boundary, long_gate


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, nargs="*")
    ap.add_argument("--scan-max", type=int)
    args = ap.parse_args()
    ks = args.k or []
    if args.scan_max:
        ks.extend(range(3, args.scan_max + 1, 2))
    for k in ks:
        z = costs(k)
        if len(z) == 6:
            continue
        r, d, c, ordinary, fixed, by_j, min_x, hb, long_gate = z
        positive = [(j + 1, v) for j, v in enumerate(by_j) if v > 1e-15]
        print(
            f"k={k} R={r} d={d} q={d+1} N={d+3} c={c} hb={hb} "
            f"C={ordinary:.12g} CN={fixed:.12g} slack={1-fixed:.12g} "
            f"longgate={long_gate:.12g} minx={min_x:.3g} posj={positive}"
        )


if __name__ == "__main__":
    main()
