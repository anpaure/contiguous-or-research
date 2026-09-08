#!/usr/bin/env python3
"""Exact-rational certificate for the q+2 pull long-block obstruction at k=8191.

Substantive execution is intended for ssh h100.
"""

from fractions import Fraction
from math import comb


def main() -> None:
    k = 8191
    r = (k + 1) // 2
    w = comb(k, r)
    lower = 2 ** (k - 1) - 1
    d = 0
    while d * w + d * (d + 1) // 2 < lower:
        d += 1
    assert d == 57
    assert lower <= d * w  # zero Ferrers boundary in this instance
    q = d + 1
    n = q + 2
    c = r - d - 1

    def qs(s: int) -> Fraction:
        return Fraction(comb(k, s), w)

    a1 = qs(c)
    ptotal = sum((qs(s) for s in range(1, c + 1)), Fraction())
    g = [Fraction()] + [1 - qs(c + j) for j in range(1, d + 1)]
    htotal = sum(g, Fraction())
    g.extend([Fraction(), Fraction()])
    delta = [Fraction()] + [(g[j] - g[j + 1]) / htotal for j in range(1, d + 2)]
    x = [Fraction()] * (d + 1)
    for j in range(1, d + 1):
        x[j] = ptotal * delta[j] - (ptotal - a1) * delta[j + 1]
        assert x[j] >= 0

    assert n == 60
    # A block of type j consumes j+1 cyclic slots.  In 60 slots, a
    # configuration has at most two 30-slot blocks, or one block of length
    # at least 31.  Thus 1/2 n_30 + sum_(w>=31)n_w <= 1.
    lhs = n * (Fraction(1, 2) * x[29] + sum(x[30:], Fraction()))
    assert lhs > 1
    print(f"k={k} R={r} d={d} q={q} N={n} c={c}")
    print(f"numerator={lhs.numerator}")
    print(f"denominator={lhs.denominator}")
    print(f"excess_numerator={lhs.numerator-lhs.denominator}")
    print(f"decimal={float(lhs):.15f}")


if __name__ == "__main__":
    main()
