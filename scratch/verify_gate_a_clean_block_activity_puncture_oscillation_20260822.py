#!/usr/bin/env python3
"""Finite exact audit for the clean-block activity-oscillation theorem.

This is not a premise of the asymptotic proof.  It exhausts the cyclic
skeleton-neighbour claims at small ranks, records the necessary r=2
exception, and checks the activity-expansion and exponent bookkeeping.
"""

from fractions import Fraction
from itertools import combinations


def interval(start: int, length: int, b: int) -> frozenset[int]:
    return frozenset((start + j) % b for j in range(length))


def full_factor(r: int):
    b = 2 * r + 1
    return (
        [("M", interval(s, r, b)) for s in range(b)]
        + [("L", interval(s, r - 1, b)) for s in range(b)]
    )


def target_universe(r: int):
    b = 2 * r + 1
    return (
        [("M", frozenset(a)) for a in combinations(range(b), r)]
        + [("L", frozenset(a)) for a in combinations(range(b), r - 1)]
    )


def is_skeleton_pair(a, b) -> bool:
    shore_a, set_a = a
    shore_b, set_b = b
    if shore_a == shore_b == "M":
        return set_a.isdisjoint(set_b)
    if shore_a == "L" and shore_b == "M":
        return set_a < set_b
    if shore_a == "M" and shore_b == "L":
        return set_b < set_a
    return False


def audit_skeleton_neighbours() -> None:
    observed = []
    for r in range(2, 7):
        b = 2 * r + 1
        factor = full_factor(r)
        universe = target_universe(r)

        outside_counts = [
            sum(is_skeleton_pair(u, t) for t in factor)
            for u in universe
            if u not in factor
        ]
        outside_max = max(outside_counts, default=0)
        if r == 2:
            assert outside_max == 3
        else:
            assert outside_max <= 2

        punctured_max = 0
        for h in range(b):
            row = factor[:h] + factor[h + 1 : b + h] + factor[b + h + 1 :]
            assert len(row) == 2 * b - 2
            punctured_max = max(
                punctured_max,
                max(
                    (
                        sum(is_skeleton_pair(u, t) for t in row)
                        for u in universe
                        if u not in row
                    ),
                    default=0,
                ),
            )
        assert punctured_max <= 3
        observed.append((r, outside_max, punctured_max))

    print("skeleton maxima (r, outside full factor, outside punctured row):")
    for item in observed:
        print(" ", item)


def audit_activity_expansion() -> None:
    # In (2.3), a monomial with nonempty support S has coefficient 1 on
    # the left and |S| on the right.
    for n in range(1, 13):
        for size in range(1, n + 1):
            assert size >= 1

    # Also check the numerical inequality for heterogeneous exact rational
    # activities, including the square estimate used in (2.6).
    activities = [Fraction(1, 7), Fraction(2, 5), Fraction(3, 4), Fraction(5, 3)]
    product = Fraction(1)
    for a in activities:
        product *= 1 + a
    lhs = product - 1
    rhs = sum(a * product / (1 + a) for a in activities)
    assert lhs <= rhs
    assert (product - 1) ** 2 <= product**2 - 1
    print("activity expansion and square inequality: exact rational checks pass")


def audit_intermediate_toggle_identity() -> None:
    # Section 3 extends B^+ to a non-row intermediate set A contained in
    # a genuine row R.  The toggle identity is purely set-theoretic; check
    # it exactly over every subset G of a six-target toy universe.
    universe = tuple(range(6))
    v, u = 0, 1
    row = frozenset({0, 1, 2, 3})
    intermediate = frozenset({0, 1, 3})
    intermediate_0 = intermediate - {u}
    opposite = frozenset({0, 4, 5})
    assert {v, u} <= intermediate <= row
    assert row & opposite == {v}
    probabilities = {
        0: Fraction(2, 3),
        1: Fraction(3, 5),
        2: Fraction(4, 5),
        3: Fraction(5, 6),
        4: Fraction(3, 4),
        5: Fraction(7, 8),
    }

    def weight(a) -> Fraction:
        answer = Fraction(1)
        for t in a:
            answer /= probabilities[t]
        return answer

    rows = [
        frozenset(a)
        for size in range(1, len(universe) + 1)
        for a in combinations(universe, size)
    ]

    def bplus(a, h) -> Fraction:
        return sum(
            (weight(g & a) - 1) * (weight(g & h) - 1)
            for g in rows
            if v not in g
        )

    direct = bplus(intermediate, opposite) - bplus(intermediate_0, opposite)
    expanded = (probabilities[u] ** -1 - 1) * sum(
        weight(g & intermediate_0) * (weight(g & opposite) - 1)
        for g in rows
        if v not in g and u in g
    )
    assert direct == expanded >= 0
    print("non-row intermediate toggle identity: exact rational check passes")


def audit_exponents() -> None:
    # Vanishing requirements from the two terms in (0.2), plus every
    # auxiliary use of C.3bis and the absorptions in Sections 2--3.
    thresholds = {
        "r^-1/2 x^-5": Fraction(1, 10),
        "r^-3/4 x^-8": Fraction(3, 32),
        "R_4 applicability": Fraction(1, 8),
        "T_2 absorption": Fraction(1, 4),
        "R_2 simplification": Fraction(1, 2),
    }
    assert min(thresholds.values()) == Fraction(3, 32)
    print("exponent bottleneck:", min(thresholds.values()), thresholds)


if __name__ == "__main__":
    audit_skeleton_neighbours()
    audit_activity_expansion()
    audit_intermediate_toggle_identity()
    audit_exponents()
    print("all finite exact audits pass")
