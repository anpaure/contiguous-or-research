#!/usr/bin/env python3
"""Symbolic coefficient probes for adjacent affine capacities."""

from __future__ import annotations

import sympy as sp


def h(u, ell, j):
    if ell <= 0 or j <= 0 or j > min(u, ell):
        return 0
    if j < min(u, ell):
        return 2
    return abs(u - ell) + 1


def even_coeff(m, u, K):
    b = 2 * m + 1
    meet = lambda ell: 0 if ell <= 0 else u + ell - 1
    out = {K: b - meet(K) - meet(K + 1)}
    for j in range(1, K + 1):
        c = h(u, K - j, j) + h(u, K - j + 1, j)
        if c:
            out[K - j] = out.get(K - j, 0) + c
    return out


def odd_coeff(m, u, K):
    if K == 0:
        return {0: 2 * (m - u)}
    out = {K: m - K - u}
    d = m + 1 + u if K == 1 else m - K + 4 - u
    out[K - 1] = out.get(K - 1, 0) + d
    for j in range(1, K):
        c = 2 * h(u, K - j - 1, j)
        if c:
            out[K - j - 1] = out.get(K - j - 1, 0) + c
    return out


def combine(a, x, b, y):
    keys = set(x) | set(y)
    return {k: sp.factor(a * x.get(k, 0) + b * y.get(k, 0)) for k in sorted(keys)
            if sp.factor(a * x.get(k, 0) + b * y.get(k, 0)) != 0}


def main():
    m = sp.symbols("m", integer=True, positive=True)
    for u in range(2, 7):
        for K in range(0, 10):
            E = even_coeff(m, u, K)
            O0 = odd_coeff(m, u, K)
            O1 = odd_coeff(m, u, K + 1)
            # Q_odd(K)/Q_even(K)
            a0 = sp.Rational(1, 1) * (m - u + 1 + K) / (m + u + 1 - K)
            # Q_odd(K+1)/Q_even(K)
            a1 = sp.Rational(1, 1) * (m - u - K) / (m + u + 2 + K)
            d0 = combine(a0, E, -1, O0)
            d1 = combine(a1, E, -1, O1)
            print("EO0", u, K, d0)
            print("EO1", u, K, d1)


if __name__ == "__main__":
    main()
