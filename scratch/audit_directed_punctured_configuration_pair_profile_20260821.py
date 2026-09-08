#!/usr/bin/env python3
"""Audit the exact directed punctured-configuration pair profile.

The theorem is analytic.  Exhaustive enumeration is run only through r=4;
all substantive runs are intended for H100.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter
from fractions import Fraction


def degrees(r):
    dm = 2 * r * math.factorial(r) * math.factorial(r + 1)
    dl = 2 * (r + 2) * math.factorial(r) * math.factorial(r + 1)
    return dm, dl


def pair_table(r):
    c = 2 * r - 1
    mm = {
        s: 2 * c * math.factorial(r - s) ** 2
        * math.factorial(s) * math.factorial(s + 1)
        for s in range(r)
    }
    ll = {0: 24 * c * math.factorial(r - 1) ** 2}
    ll.update({
        s: 2 * c * math.factorial(r - 1 - s) ** 2
        * math.factorial(s) * math.factorial(s + 3)
        for s in range(1, r - 1)
    })
    ml = {0: 6 * c * math.factorial(r) * math.factorial(r - 1)}
    ml.update({
        s: 2 * c * math.factorial(r - s) * math.factorial(r - 1 - s)
        * math.factorial(s) * math.factorial(s + 2)
        for s in range(1, r - 1)
    })
    ml[r - 1] = (4 * r - 1) * math.factorial(r - 1) * math.factorial(r + 1)
    return mm, ll, ml


def internal_sum(r):
    c = 2 * r - 1
    mm, ll, ml = pair_table(r)
    smm = c * sum(mm.values())
    sll = 2 * c * ll[0] + c * sum(ll[s] for s in range(1, r - 1))
    sml = (3 * c * ml[0]
           + 2 * c * sum(ml[s] for s in range(1, r - 1))
           + (4 * r - 1) * ml[r - 1])
    return smm, sll, sml


def edge(word, r):
    b = 2 * r + 1
    answer = set()
    for layer, length in ((0, r), (1, r - 1)):
        for start in range(1, b):
            mask = sum(1 << word[(start + offset) % b]
                       for offset in range(length))
            answer.add((layer, mask))
    assert len(answer) == 4 * r
    return frozenset(answer)


def exhaustive(r):
    b = 2 * r + 1
    base = edge(tuple(range(b)), r)
    pair_sum = 0
    pair_counts = Counter()
    full_overlap = 0
    for word in itertools.permutations(range(b)):
        other = edge(word, r)
        overlap = base & other
        full_overlap += len(overlap) == 4 * r
        pair_sum += len(overlap) * (len(overlap) - 1) // 2
        for left, right in itertools.combinations(overlap, 2):
            layers = tuple(sorted((left[0], right[0])))
            intersection = (left[1] & right[1]).bit_count()
            pair_counts[(layers, intersection)] += 1
    return pair_sum, pair_counts, full_overlap


def expected_category_sums(r):
    c = 2 * r - 1
    mm, ll, ml = pair_table(r)
    answer = {}
    for s, value in mm.items():
        answer[((0, 0), s)] = c * value
    for s, value in ll.items():
        answer[((1, 1), s)] = (2 * c if s == 0 else c) * value
    for s, value in ml.items():
        count = 3 * c if s == 0 else (4 * r - 1 if s == r - 1 else 2 * c)
        answer[((0, 1), s)] = count * value
    return answer


def audit_formula(r_max):
    known = {2: 1158, 3: 21208, 4: 521856, 5: 17754336}
    for r in range(2, r_max + 1):
        dm, dl = degrees(r)
        smm, sll, sml = internal_sum(r)
        total = smm + sll + sml
        assert total > 0
        if r in known:
            assert total == known[r], (r, total, known[r])
        mm, ll, ml = pair_table(r)
        maximum = max((*mm.values(), *ll.values(), *ml.values()))
        if r == 2:
            assert maximum == ll[0] == 72
        else:
            assert maximum == ml[r - 1]
            assert Fraction(4 * r * maximum, dm) == Fraction(8 * r - 2, r)
        assert 2 * r * (dm + dl) == 4 * (r + 1) * dm
        containment = (4 * r - 1) * ml[r - 1]
        disjoint_mm = (2 * r - 1) * mm[0]
        assert total >= containment + disjoint_mm

    r = max(200, r_max)
    dm, _ = degrees(r)
    total = sum(internal_sum(r))
    scaled = Fraction(r * (total - 12 * dm), dm)
    assert abs(float(scaled) - 32.0) < 1.0, float(scaled)


def main(exhaustive_max, formula_max):
    audit_formula(formula_max)
    cases = 0
    for r in range(2, exhaustive_max + 1):
        observed_sum, observed_categories, full_overlap = exhaustive(r)
        expected = expected_category_sums(r)
        # By coordinate transitivity, uniqueness of the base target deck
        # implies injectivity of the directed target-deck map.
        assert full_overlap == 1, (r, full_overlap)
        assert observed_sum == sum(internal_sum(r))
        assert observed_categories == Counter(expected), (
            r,
            observed_categories,
            expected,
        )
        cases += 1
    print("DIRECTED_PUNCTURED_CONFIGURATION_PAIR_PROFILE_AUDIT_PASS", {
        "exhaustive_cases": cases,
        "exhaustive_max_r": exhaustive_max,
        "formula_max_r": formula_max,
        "asymptotic_probe_r": max(200, formula_max),
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive-max", type=int, default=4)
    parser.add_argument("--formula-max", type=int, default=200)
    arguments = parser.parse_args()
    main(arguments.exhaustive_max, arguments.formula_max)
