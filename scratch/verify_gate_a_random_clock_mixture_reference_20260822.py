#!/usr/bin/env python3
"""Exact finite audit of the random-size mixture reference theorem."""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def subsets_of_size(items, k):
    return [frozenset(x) for x in combinations(items, k)]


def omega(shores, size):
    parts = [subsets_of_size(shore, k) for shore, k in zip(shores, size)]
    return [frozenset().union(*choice) for choice in product(*parts)]


def choose_vec(n, np):
    out = 1
    for a, b in zip(n, np):
        out *= comb(a, b)
    return out


def main():
    shores = [("a0", "a1", "a2", "a3"), ("b0", "b1", "b2")]
    sizes = [(4, 3), (3, 3), (3, 2), (2, 2)]
    spaces = {n: omega(shores, n) for n in sizes}

    w = {
        (4, 3): Fraction(1, 3),
        (3, 3): Fraction(1, 3),
        (3, 2): Fraction(1, 3),
        (2, 2): Fraction(0),
    }
    # Conditional size transition K(n,n').
    K = {
        ((4, 3), (3, 3)): Fraction(1, 2),
        ((4, 3), (3, 2)): Fraction(1, 2),
        ((3, 3), (3, 2)): Fraction(1, 3),
        ((3, 3), (2, 2)): Fraction(2, 3),
        ((3, 2), (3, 2)): Fraction(1, 4),
        ((3, 2), (2, 2)): Fraction(3, 4),
    }

    # Build Lambda and apply the literal nested kernel.
    lam = {}
    for n in sizes:
        for S in spaces[n]:
            lam[S] = lam.get(S, Fraction(0)) + w[n] / len(spaces[n])
    out = {}
    wp = {n: Fraction(0) for n in sizes}
    for (n, np), prob in K.items():
        wp[np] += w[n] * prob
    for n in sizes:
        if not w[n]:
            continue
        for S in spaces[n]:
            for (src, np), prob in K.items():
                if src != n:
                    continue
                denom = choose_vec(n, np)
                for Sp in spaces[np]:
                    if Sp <= S:
                        out[Sp] = out.get(Sp, Fraction(0)) + lam[S] * prob / denom

    assert sum(out.values(), Fraction(0)) == 1
    for np in sizes:
        for Sp in spaces[np]:
            assert out.get(Sp, Fraction(0)) == wp[np] / len(spaces[np])

    # Ratio convexity for deliberately nonconstant fibre means.
    f = {(4, 3): 7, (3, 3): 5, (3, 2): 11, (2, 2): 2}
    t = {(4, 3): 3, (3, 3): 4, (3, 2): 6, (2, 2): 5}
    ratio = sum(w[n] * f[n] for n in sizes) / sum(w[n] * t[n] for n in sizes)
    active_ratios = [Fraction(f[n], t[n]) for n in sizes if w[n] * t[n]]
    assert min(active_ratios) <= ratio <= max(active_ratios)

    # Carrier survival formula (4.1), checked both by falling factorials and
    # literal subset enumeration for one current size and footprint.
    n = (4, 3)
    footprint = frozenset(("a0", "a1", "b0"))
    b = (2, 1)
    exact = Fraction(0)
    literal = Fraction(0)
    for (src, np), prob in K.items():
        if src != n:
            continue
        factor = Fraction(1)
        for ns, nps, bs in zip(n, np, b):
            factor *= Fraction(
                comb(nps, bs), comb(ns, bs)
            )
        exact += prob * factor
        good = sum(footprint <= Sp for Sp in spaces[np])
        literal += prob * Fraction(good, len(spaces[np]))
    assert exact == literal

    print(
        "GATE_A_RANDOM_CLOCK_MIXTURE_REFERENCE_PASS",
        {"states": len(lam), "next_states": len(out), "size_marginal": wp},
    )


if __name__ == "__main__":
    main()
