#!/usr/bin/env python3
"""Symmetric fractional lower marginals for distributed-core first-hit rails.

All substantial runs belong on h100.
"""

import argparse
import math


def parameters(k):
    R = (k + 1) // 2
    W = math.comb(k, R)
    lower = sum(math.comb(k, s) for s in range(1, R))
    d = 0
    while d * W + d * (d + 1) // 2 < lower:
        d += 1
    return R, W, d


def first_hit_count(k, R, q):
    n = 2 * q + 1
    blocks, remainder = divmod(k, n)
    local = [math.comb(n, j) for j in range(n + 1)]
    local[q] = 0
    coeff = [1]
    for _ in range(blocks):
        nxt = [0] * min(R + 1, len(coeff) + n)
        for i, x in enumerate(coeff):
            for j, y in enumerate(local):
                if i + j <= R:
                    nxt[i + j] += x * y
        coeff = nxt
    if remainder:
        tail = [math.comb(remainder, j) for j in range(remainder + 1)]
        nxt = [0] * min(R + 1, len(coeff) + remainder)
        for i, x in enumerate(coeff):
            for j, y in enumerate(tail):
                if i + j <= R:
                    nxt[i + j] += x * y
        coeff = nxt
    leave = coeff[R] if R < len(coeff) else 0
    return math.comb(k, R) - leave, leave


def log_binom_pmf(n, h, p):
    if h < 0 or h > n:
        return float("-inf")
    if p == 0.0:
        return 0.0 if h == 0 else float("-inf")
    if p == 1.0:
        return 0.0 if h == n else float("-inf")
    return (
        math.lgamma(n + 1)
        - math.lgamma(h + 1)
        - math.lgamma(n - h + 1)
        + h * math.log(p)
        + (n - h) * math.log1p(-p)
    )


def logsumexp(values):
    values = [x for x in values if x != float("-inf")]
    if not values:
        return float("-inf")
    m = max(values)
    return m + math.log(sum(math.exp(x - m) for x in values))


def analyze(k):
    R, W, d = parameters(k)
    q = d + 1
    n = 2 * q + 1
    c = R - q
    hit, leave = first_hit_count(k, R, q)
    log_hit = math.log(hit)
    records = []
    shapes = sorted(
        {
            tuple(sorted((a, b, n - a - b)))
            for a in range(1, q + 1)
            for b in range(1, q + 1)
            if 1 <= n - a - b <= q
        }
    )
    minimum_schedule_count = n * math.comb(q + 1, 2) // 3
    best_records = []
    for s in range(1, R):
        terms = []
        for ell in range(1, q):
            h = s - ell
            t = q - ell
            avoid = (
                ell * t * (t + 1) // 2
                + t * (t + 1) * (2 * t + 1) // 6
            )
            p = 1.0 - avoid / minimum_schedule_count
            terms.append(log_binom_pmf(c, h, p))
        log_mu = (
            log_hit
            - (
                math.lgamma(k + 1)
                - math.lgamma(s + 1)
                - math.lgamma(k - s + 1)
            )
            + logsumexp(terms)
        )
        records.append((log_mu, s))

        best = (float("-inf"), None)
        for shape in shapes:
            shape_terms = []
            for ell in range(1, q):
                h = s - ell
                p = 1.0 - sum(max(g - ell, 0) for g in shape) / n
                shape_terms.append(log_binom_pmf(c, h, p))
            shape_log_mu = (
                log_hit
                - (
                    math.lgamma(k + 1)
                    - math.lgamma(s + 1)
                    - math.lgamma(k - s + 1)
                )
                + logsumexp(shape_terms)
            )
            if shape_log_mu > best[0]:
                best = (shape_log_mu, shape)
        best_records.append((best[0], s, best[1]))

    deep = [x for x in records if d + 1 <= x[1] <= R - d - 1]
    for label, values in (("all", records), ("deep", deep)):
        log_mu, s = min(values)
        normalized_log_mu = log_mu - math.log(hit / W)
        print(
            f"k={k} R={R} d={d} q={q} hit/W={hit/W:.12g} "
            f"{label}-min-rank={s} log(mu)={log_mu:.12g} "
            f"raw={math.exp(log_mu) if log_mu < 700 else float('inf'):.12g} "
            f"owner-normalized={math.exp(normalized_log_mu):.12g}"
        )
    print(
        "  minimum-schedules",
        minimum_schedule_count,
        "p1",
        1
        - (
            (q - 1) * q // 2
            + (q - 1) * q * (2 * q - 1) // 6
        )
        / minimum_schedule_count,
    )
    print("  ten-smallest", sorted(records)[:10])
    best_deep = [x for x in best_records if d + 1 <= x[1] <= R - d - 1]
    print("  per-rank-best-deep-smallest", sorted(best_deep)[:10])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    args = ap.parse_args()
    for k in args.k:
        analyze(k)
