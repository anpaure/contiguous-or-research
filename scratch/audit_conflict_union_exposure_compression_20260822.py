#!/usr/bin/env python3
"""Exact finite checks for conflict-union compression and punctured bounds."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, prod
from random import Random


def falling(n, ell):
    if ell == 0:
        return 1
    if n < ell:
        return 0
    return prod(range(n - ell + 1, n + 1))


def check_local_bonferroni():
    for d in range(0, 24):
        for a in range(d + 1):
            for ell in range(1, 7):
                exact = falling(d, ell) - falling(d - a, ell)
                linear = ell * a * falling(d - 1, ell - 1)
                assert 0 <= linear - exact
                if ell >= 2:
                    upper = comb(ell, 2) * falling(a, 2) * falling(d - 2, ell - 2)
                    assert linear - exact <= upper


def check_hypergraph(edges, vertices):
    stars = {v: {i for i, edge in enumerate(edges) if v in edge} for v in vertices}
    gamma = [
        {j for j, other in enumerate(edges) if edge & other}
        for edge in edges
    ]
    degrees = {v: len(stars[v]) for v in vertices}

    for ell in range(1, 5):
        direct = 0
        for v in vertices:
            for tup in permutations(stars[v], ell):
                direct += len(set().union(*(gamma[i] for i in tup)))

        compressed = 0
        for g in range(len(edges)):
            for v in vertices:
                d = degrees[v]
                a = len(stars[v] & gamma[g])
                compressed += falling(d, ell) - falling(d - a, ell)
        assert direct == compressed

        linear = Fraction(0)
        defect_bound = 0
        for v in vertices:
            d = degrees[v]
            if not d:
                continue
            exposure_numerator = sum(len(gamma[f]) - d for f in stars[v])
            exposure = Fraction(exposure_numerator, d)
            linear += falling(d, ell) * (d + ell * exposure)
            if ell >= 2:
                for g, edge in enumerate(edges):
                    if v in edge:
                        continue
                    a = len(stars[v] & gamma[g])
                    defect_bound += (
                        comb(ell, 2)
                        * falling(a, 2)
                        * falling(d - 2, ell - 2)
                    )
        assert linear.denominator == 1
        assert 0 <= linear - direct
        if ell == 1:
            assert linear == direct
        else:
            assert linear - direct <= defect_bound


def random_hypergraph_checks():
    rng = Random(22082026)
    for n in range(5, 9):
        triples = [frozenset(x) for x in combinations(range(n), 3)]
        for _ in range(25):
            size = rng.randrange(3, min(10, len(triples)) + 1)
            check_hypergraph(rng.sample(triples, size), set(range(n)))


def punctured_degree(r, kind):
    d_middle = 2 * r * factorial(r) * factorial(r + 1)
    if kind == "M":
        return d_middle
    return Fraction(r + 2, r) * d_middle


def pair_codegree(r, kind_a, kind_b, overlap):
    b = 2 * r + 1
    k = r if kind_a == "M" else r - 1
    h = r if kind_b == "M" else r - 1
    minimum = min(k, h)
    if overlap == 0:
        multiplicity = b - k - h + 1
    elif overlap < minimum:
        multiplicity = 2
    else:
        assert overlap == minimum
        multiplicity = abs(k - h) + 1
    positional = (b - 2) * multiplicity + int(overlap == minimum)
    return (
        positional
        * factorial(overlap)
        * factorial(k - overlap)
        * factorial(h - overlap)
        * factorial(b - k - h + overlap)
    )


def check_pair_profile_bounds_and_mass():
    for r in range(3, 151):
        d_middle = punctured_degree(r, "M")
        high_mm = pair_codegree(r, "M", "M", 0)
        high_ml = pair_codegree(r, "M", "L", r - 1)
        assert high_mm <= Fraction(2, r) * d_middle
        assert high_ml <= Fraction(2, r) * d_middle

        for a in range(r):
            if a:
                assert pair_codegree(r, "M", "M", a) <= Fraction(6, r * r) * d_middle
        for a in range(r - 1):
            assert pair_codegree(r, "L", "L", a) <= Fraction(6, r * r) * d_middle
        for a in range(r):
            if a != r - 1:
                assert pair_codegree(r, "M", "L", a) <= Fraction(6, r * r) * d_middle

        s_mm = sum((2 * r - 1) * pair_codegree(r, "M", "M", a) for a in range(r))
        s_ll = (4 * r - 2) * pair_codegree(r, "L", "L", 0)
        s_ll += sum(
            (2 * r - 1) * pair_codegree(r, "L", "L", a)
            for a in range(1, r - 1)
        )
        s_ml = (6 * r - 3) * pair_codegree(r, "M", "L", 0)
        s_ml += sum(
            (4 * r - 2) * pair_codegree(r, "M", "L", a)
            for a in range(1, r - 1)
        )
        s_ml += (4 * r - 1) * pair_codegree(r, "M", "L", r - 1)
        normalized_mm = Fraction(s_mm, d_middle)
        normalized_ml = Fraction(s_ml, d_middle)
        normalized_ll = Fraction(s_ll, d_middle)
        normalized = normalized_mm + normalized_ml + normalized_ll
        assert r * abs(normalized - 12) < 64
        if r >= 5:
            approximations = (
                (normalized_mm, Fraction(4) - Fraction(4, r) + Fraction(9, r * r)),
                (normalized_ml, Fraction(8) + Fraction(32, r) - Fraction(111, 2 * r * r)),
                (normalized_ll, Fraction(4, r) + Fraction(96, r * r)),
                (normalized, Fraction(12) + Fraction(32, r) + Fraction(99, 2 * r * r)),
            )
            for exact, approximation in approximations:
                assert r**3 * abs(exact - approximation) < 200


def cyclic_interval(b, start, length):
    return frozenset((start + i) % b for i in range(length))


def check_external_row_cap():
    # Exhaustive target checks at the first several nontrivial radii.
    for r in range(3, 8):
        b = 2 * r + 1
        edge = []
        for start in range(1, b):
            edge.append(("M", cyclic_interval(b, start, r)))
            edge.append(("L", cyclic_interval(b, start, r - 1)))
        edge_set = set(edge)
        d_middle = punctured_degree(r, "M")

        for kind, size in (("M", r), ("L", r - 1)):
            for raw in combinations(range(b), size):
                target = (kind, frozenset(raw))
                if target in edge_set:
                    continue
                high_partners = 0
                row_sum = 0
                for other_kind, other in edge:
                    overlap = len(target[1] & other)
                    value = pair_codegree(r, kind, other_kind, overlap)
                    row_sum += value
                    if (
                        kind == other_kind == "M" and overlap == 0
                    ) or (
                        {kind, other_kind} == {"M", "L"} and overlap == r - 1
                    ):
                        high_partners += 1
                assert high_partners <= (4 if kind == "M" else 2)
                assert row_sum <= Fraction(32, r) * d_middle


def main():
    check_local_bonferroni()
    random_hypergraph_checks()
    check_pair_profile_bounds_and_mass()
    check_external_row_cap()
    print("PASS: exact conflict compression and initial punctured collision bounds")


if __name__ == "__main__":
    main()
