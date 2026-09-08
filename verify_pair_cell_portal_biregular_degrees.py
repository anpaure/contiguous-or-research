#!/usr/bin/env python3
"""Exact biregular degree identities for universal pair-cell portals.

Substantial instances belong on h100.
"""

import argparse
import math


def odd_double_factorial_from_pairs(p):
    return math.factorial(2 * p) // (2**p * math.factorial(p))


def middle_parameters(k, R, q, s):
    p = R - 1
    m = s + q - 1
    epsilon = (R - m) & 1
    a = (R - epsilon - m) // 2
    b = p - m - a
    return p, m, epsilon, a, b


def middle_degrees(k, R, q, s):
    p, m, epsilon, a, b = middle_parameters(k, R, q, s)
    target_degree = math.factorial(k - s) // (
        2 ** (p - s) * math.factorial(q - 1) * math.factorial(a) * math.factorial(b)
    )
    cell_degree = math.comb(m, q - 1) * 2**s
    cells = (
        k
        * odd_double_factorial_from_pairs(p)
        * math.comb(p, m)
        * math.comb(p - m, a)
    )
    assert math.comb(k, s) * target_degree == cells * cell_degree
    return target_degree, cell_degree, cells


def top_letter_degrees(k, R, q):
    p = R - 1
    s = R - q + 1
    target_degree = s * math.factorial(k - s) // (
        2 ** (q - 1) * math.factorial(q - 1)
    )
    cell_degree = math.comb(p, q - 1) * 2 ** (s - 1)
    cells = k * odd_double_factorial_from_pairs(p)
    assert math.comb(k, s) * target_degree == cells * cell_degree
    return s, target_degree, cell_degree, cells


def fan_degrees(k, R, r):
    p = R - 1
    s = R - r
    target_degree = s * math.factorial(k - s) // (
        2**r * math.factorial(r)
    )
    cell_degree = math.comb(p, r) * 2 ** (s - 1)
    cells = k * odd_double_factorial_from_pairs(p)
    assert math.comb(k, s) * target_degree == cells * cell_degree
    return s, target_degree, cell_degree, cells


def deadline_parameters(k):
    R = (k + 1) // 2
    W = math.comb(k, R)
    lower = sum(math.comb(k, s) for s in range(1, R))
    d = 0
    while d * W + d * (d + 1) // 2 < lower:
        d += 1
    return R, d + 1


def log_ratio(x, y):
    return math.log(x) - math.log(y)


def middle_local_codegree_count(s, q, j):
    return sum(
        math.comb(s, c)
        * (math.comb(q - 1, s - c) if 0 <= s - c <= q - 1 else 0)
        * (math.comb(c, j) if 0 <= j <= c else 0)
        * 2 ** (s - c)
        for c in range(s + 1)
    )


def top_local_codegree_count(p, s, t, j):
    u = s - 1
    return sum(
        math.comb(u, c)
        * (math.comb(t, u - c) if 0 <= u - c <= t else 0)
        * (math.comb(c, j - 1) if 0 <= j - 1 <= c else 0)
        * 2 ** (u - c)
        for c in range(u + 1)
    )


def assert_codegrees_integral(k, R, q, s, degree, local_counter):
    # The boundary cases plus a deterministic interior sample catch all
    # factorial/binomial index conventions without a quadratic large-k loop.
    js = {0, 1, s // 2, max(0, s - 1), s}
    for j in js:
        denominator = math.comb(s, j) * math.comb(k - s, s - j)
        n = local_counter(j)
        numerator = degree * n
        assert numerator % denominator == 0


def audit(k):
    R, q = deadline_parameters(k)
    p = R - 1
    h = math.ceil(3 * math.log2(p))
    M = q + h
    assert M <= p
    ratios = []

    for s in range(h + 1, R - q + 1):
        degree, cell_degree, _ = middle_degrees(k, R, q, s)
        assert_codegrees_integral(
            k,
            R,
            q,
            s,
            degree,
            lambda j, s=s: middle_local_codegree_count(s, q, j),
        )
        ratios.append((log_ratio(degree, cell_degree), "middle", s))

    s, degree, cell_degree, _ = top_letter_degrees(k, R, q)
    assert_codegrees_integral(
        k,
        R,
        q,
        s,
        degree,
        lambda j, s=s: top_local_codegree_count(p, s, q - 1, j),
    )
    ratios.append((log_ratio(degree, cell_degree), "top-letter", s))

    for r in range(1, q - 1):
        s, degree, cell_degree, _ = fan_degrees(k, R, r)
        assert_codegrees_integral(
            k,
            R,
            q,
            s,
            degree,
            lambda j, s=s, r=r: top_local_codegree_count(p, s, r, j),
        )
        ratios.append((log_ratio(degree, cell_degree), "fan", s))

    minimum = min(ratios)
    print(
        f"k={k} R={R} q={q} h={h} ranks={len(ratios)} "
        f"min-log(D/e)={minimum[0]:.12f} type={minimum[1]} s={minimum[2]} PASS",
        flush=True,
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    args = ap.parse_args()
    for k in args.k:
        audit(k)
