#!/usr/bin/env python3
"""Audit the exact q1-cycle/q2-colour reduction and b=9 separation."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from audit_b9_five_wreath_shadow_switch_20260821 import (
    canonical,
    dyck_words,
    msw_row,
)


BALANCED_VERTICAL = (
    (8, 5, 4, 6, 7, 1, 3, 2, 9),
    (7, 8, 3, 5, 6, 9, 2, 4, 1),
    (6, 5, 2, 7, 8, 3, 9, 1, 4),
    (1, 8, 5, 6, 7, 9, 2, 3, 4),
    (8, 7, 4, 3, 6, 5, 2, 1, 9),
    (7, 2, 6, 4, 8, 9, 1, 5, 3),
    (1, 8, 6, 4, 7, 9, 2, 5, 3),
    (3, 2, 8, 6, 7, 9, 1, 4, 5),
    (3, 7, 6, 8, 1, 2, 5, 4, 9),
    (7, 5, 4, 3, 8, 6, 9, 2, 1),
    (7, 4, 2, 5, 8, 6, 9, 1, 3),
    (1, 8, 7, 5, 4, 9, 6, 3, 2),
    (7, 5, 3, 9, 8, 4, 2, 1, 6),
    (2, 8, 7, 9, 5, 1, 6, 3, 4),
)


Q1_COMPLETE_Q2_HOLE = (
    (1, 2, 5, 7, 8, 4, 3, 6, 9),
    (1, 2, 5, 8, 9, 3, 6, 7, 4),
    (1, 2, 6, 5, 3, 7, 8, 9, 4),
    (1, 3, 2, 6, 7, 4, 9, 5, 8),
    (1, 3, 4, 6, 2, 9, 5, 7, 8),
    (1, 4, 3, 2, 8, 9, 6, 5, 7),
    (1, 4, 6, 5, 9, 3, 7, 2, 8),
    (1, 4, 8, 7, 6, 9, 2, 3, 5),
    (1, 5, 9, 3, 4, 7, 2, 8, 6),
    (1, 5, 9, 4, 2, 8, 6, 3, 7),
    (1, 6, 3, 5, 4, 7, 2, 9, 8),
    (1, 7, 2, 3, 5, 8, 6, 4, 9),
    (1, 7, 6, 2, 5, 8, 4, 3, 9),
    (1, 8, 7, 6, 5, 4, 2, 3, 9),
)


def windows(order, length):
    b = len(order)
    return tuple(
        frozenset(order[(start + j) % b] for j in range(length))
        for start in range(b)
    )


def profile(factor, r):
    answer = []
    for q in range(r):
        length = r - q
        multiplicity = Counter(
            target for row in factor for target in windows(row, length)
        )
        universe = set(map(frozenset, combinations(range(1, 2 * r + 2), length)))
        answer.append({
            "holes": len(universe - multiplicity.keys()),
            "duplicate_excess": sum(multiplicity.values()) - len(multiplicity),
            "pair_energy": sum(value * (value - 1) // 2 for value in multiplicity.values()),
            "max_load": max(multiplicity.values()),
        })
    return answer


def audit_cycle_identities(factor, r):
    middle_unions = []
    depth_support = [set() for _ in range(r)]
    q1_degree = Counter()
    for row in factor:
        q1 = windows(row, r - 1)
        assert len(set(q1)) == len(row)
        for start in range(len(row)):
            left = q1[start]
            right = q1[(start + 1) % len(row)]
            assert len(left ^ right) == 2
            middle_unions.append(left | right)
            q1_degree[left] += 2
        for q in range(1, r):
            for start in range(len(row)):
                common = set(q1[start])
                for offset in range(1, q):
                    common &= q1[(start + offset) % len(row)]
                assert len(common) == r - q
                depth_support[q].add(frozenset(common))
    all_middle = set(map(frozenset, combinations(range(1, 2 * r + 2), r)))
    assert Counter(middle_unions) == Counter({target: 1 for target in all_middle})
    q1_mult = Counter(target for row in factor for target in windows(row, r - 1))
    assert q1_degree == Counter({target: 2 * value for target, value in q1_mult.items()})
    for q in range(1, r):
        literal = set(target for row in factor for target in windows(row, r - q))
        assert depth_support[q] == literal


def main():
    r = 4
    canonical_factor = {msw_row(word) for word in dyck_words(r)}
    vertical_factor = {canonical(row) for row in BALANCED_VERTICAL}
    bad_factor = {canonical(row) for row in Q1_COMPLETE_Q2_HOLE}
    assert len(canonical_factor) == len(vertical_factor) == len(bad_factor) == 14

    for factor in (vertical_factor, bad_factor):
        audit_cycle_identities(factor, r)
    vertical = profile(vertical_factor, r)
    bad = profile(bad_factor, r)
    assert tuple(item["holes"] for item in vertical) == (0, 0, 0, 0)
    assert tuple(item["holes"] for item in bad) == (0, 0, 2, 0)
    assert vertical[1]["duplicate_excess"] == bad[1]["duplicate_excess"] == 42
    assert vertical[1]["pair_energy"] == bad[1]["pair_energy"] == 42
    assert vertical[1]["max_load"] == bad[1]["max_load"] == 2
    missing_q2 = (
        set(map(frozenset, combinations(range(1, 10), 2)))
        - set(target for row in bad_factor for target in windows(row, 2))
    )
    assert missing_q2 == {frozenset((3, 8)), frozenset((7, 9))}
    print("WREATH_Q1_CYCLE_Q2_COLOR_GATE_AUDIT_PASS", {
        "vertical_holes": tuple(item["holes"] for item in vertical[1:]),
        "separation_holes": tuple(item["holes"] for item in bad[1:]),
        "common_q1_duplicate_excess": 42,
        "common_q1_pair_energy": 42,
        "common_q1_max_load": 2,
        "missing_q2": ((3, 8), (7, 9)),
    })


if __name__ == "__main__":
    main()
