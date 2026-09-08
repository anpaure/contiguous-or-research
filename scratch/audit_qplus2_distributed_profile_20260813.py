#!/usr/bin/env python3
"""Exact/log audit of the symmetric q+2 distributed-core rank profile.

Substantive runs are intended for ssh h100, not the local workstation.
"""

from __future__ import annotations

import argparse
import math


def logadd(a: float, b: float) -> float:
    if a == -math.inf:
        return b
    if b == -math.inf:
        return a
    if a < b:
        a, b = b, a
    return a + math.log1p(math.exp(b - a))


def logbinom(n: int, j: int) -> float:
    if j < 0 or j > n:
        return -math.inf
    return math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)


def log_bin_pmf(n: int, j: int, p: float) -> float:
    if j < 0 or j > n:
        return -math.inf
    if p == 0.0:
        return 0.0 if j == 0 else -math.inf
    if p == 1.0:
        return 0.0 if j == n else -math.inf
    return logbinom(n, j) + j * math.log(p) + (n - j) * math.log1p(-p)


def deadline(k: int) -> int:
    r = (k + 1) // 2
    w = math.comb(k, r)
    lower = sum(math.comb(k, s) for s in range(1, r))
    d = max(0, (lower + w - 1) // w - 1)
    while d * w + d * (d + 1) // 2 < lower:
        d += 1
    while d > 0 and (d - 1) * w + (d - 1) * d // 2 >= lower:
        d -= 1
    return d


def p_hit(ell: int, q: int) -> float:
    n = q + 2
    if ell <= 3:
        return 2.0 * ell / n
    if ell <= q - 2:
        return (ell + 3.0) / n
    if ell == q - 1:
        return 1.0
    raise ValueError((ell, q))


def profile(k: int):
    if k % 2 != 1:
        raise ValueError("odd k only")
    r = (k + 1) // 2
    d = deadline(k)
    q = d + 1
    c = r - q
    logw = logbinom(k, r)
    vals = []
    for s in range(1, r):
        total = -math.inf
        for ell in range(1, q):
            h = s - ell
            if h < 0 or h > c:
                continue
            total = logadd(total, log_bin_pmf(c, h, p_hit(ell, q)))
        vals.append((s, logw - logbinom(k, s) + total))
    return r, d, q, c, vals


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, nargs="*")
    ap.add_argument("--scan-max", type=int)
    args = ap.parse_args()
    ks = args.k or []
    if args.scan_max:
        ks.extend(range(3, args.scan_max + 1, 2))
    for k in ks:
        r, d, q, c, vals = profile(k)
        if q < 4 or c < 0:
            continue
        deficient = [(s, lv) for s, lv in vals if lv < -1e-12]
        min_s, min_lv = min(vals, key=lambda z: z[1])
        top = dict(vals)[r - 2] if r >= 3 else float("nan")
        first = deficient[0][0] if deficient else None
        last = deficient[-1][0] if deficient else None
        print(
            f"k={k} R={r} d={d} q={q} c={c} "
            f"def={len(deficient)} range={first}:{last} "
            f"min_s={min_s} loglam_min={min_lv:.9g} "
            f"loglam_Rm2={top:.9g}"
        )


if __name__ == "__main__":
    main()
