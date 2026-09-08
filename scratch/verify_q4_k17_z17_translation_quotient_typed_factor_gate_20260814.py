#!/usr/bin/env python3
"""Independent finite replay for the Z17 q4 typed-factor quotient reduction.

Run only on H100.  This checks orbit freeness/counts, every cyclic ticket
formula on one literal period-10 rail (including wrap), point regularity of
every subset orbit, and all forced occurrence histograms in the theorem.
It does not search for an exact cover.
"""

from __future__ import annotations

import itertools
from collections import Counter


K = 17
Q = 4
CORE = frozenset(range(5))
ORDER = tuple(range(5, 15))


def rotate(values: frozenset[int], shift: int) -> frozenset[int]:
    return frozenset((x + shift) % K for x in values)


def orbit(values: frozenset[int]) -> tuple[frozenset[int], ...]:
    return tuple(rotate(values, shift) for shift in range(K))


def canonical(values: frozenset[int]) -> tuple[int, ...]:
    return min(tuple(sorted(item)) for item in orbit(values))


def windows(width: int) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(ORDER[(i + t) % len(ORDER)] for t in range(width))
        for i in range(len(ORDER))
    )


def owners() -> tuple[frozenset[int], ...]:
    return tuple(CORE | window for window in windows(Q))


def intersection_ticket(deck, start, span):
    value = set(deck[start])
    for offset in range(1, span):
        value.intersection_update(deck[(start + offset) % len(deck)])
    return frozenset(value)


def union_ticket(deck, start, span):
    value = set()
    for offset in range(span):
        value.update(deck[(start + offset) % len(deck)])
    return frozenset(value)


def expected_lower(start, span):
    return CORE | frozenset(
        ORDER[(start + t) % len(ORDER)] for t in range(span - 1, Q)
    )


def expected_upper(start, span):
    return CORE | frozenset(
        ORDER[(start + t) % len(ORDER)] for t in range(Q + span - 1)
    )


def orbit_count(rank: int) -> int:
    reps = {
        canonical(frozenset(values))
        for values in itertools.combinations(range(K), rank)
    }
    expected = len(tuple(itertools.combinations(range(K), rank))) // K
    assert len(reps) == expected
    for rep in reps:
        values = frozenset(rep)
        developed = orbit(values)
        assert len(set(developed)) == K
        point_load = Counter(x for item in developed for x in item)
        assert set(point_load) == set(range(K))
        assert set(point_load.values()) == {rank}
    return len(reps)


def check_hist(total, bins, low, high, low_count, high_count):
    assert low_count + high_count == bins
    assert low * low_count + high * high_count == total


def main() -> None:
    expected_orbits = {
        5: 364,
        6: 728,
        7: 1144,
        8: 1430,
        9: 1430,
        10: 1144,
        11: 728,
        12: 364,
        13: 140,
        14: 40,
        15: 8,
    }
    actual_orbits = {rank: orbit_count(rank) for rank in expected_orbits}
    assert actual_orbits == expected_orbits

    deck = owners()
    assert len(deck) == 10
    assert len(set(deck)) == 10
    assert all(len(owner) == 9 for owner in deck)
    for i in range(10):
        assert len(deck[i] ^ deck[(i + 1) % 10]) == 2
        for span in range(1, 5):
            lower = intersection_ticket(deck, i, span)
            upper = union_ticket(deck, i, span)
            assert lower == expected_lower(i, span)
            assert upper == expected_upper(i, span)
            assert len(lower) == 10 - span
            assert len(upper) == 8 + span

        for span, rank in ((5, 13), (6, 14), (7, 15)):
            upper = union_ticket(deck, i, span)
            assert len(upper) == rank

    lower_core = [intersection_ticket(deck, i, 5) for i in range(10)]
    assert set(lower_core) == {CORE}
    upper_full = [union_ticket(deck, i, 7) for i in range(10)]
    assert len(set(upper_full)) == 1
    assert upper_full[0] == CORE | frozenset(ORDER)
    omitted = frozenset(range(K)) - upper_full[0]
    assert len(omitted) == 2

    # The same literal formulas through q3 hold on a period-11 rail.
    order11 = tuple(range(5, 16))
    deck11 = tuple(
        CORE
        | frozenset(order11[(i + t) % len(order11)] for t in range(Q))
        for i in range(len(order11))
    )
    assert len(deck11) == 11 and len(set(deck11)) == 11
    for i in range(11):
        assert len(deck11[i] ^ deck11[(i + 1) % 11]) == 2
        for span in range(1, 5):
            lower = intersection_ticket(deck11, i, span)
            upper = union_ticket(deck11, i, span)
            expected_l = CORE | frozenset(
                order11[(i + t) % 11] for t in range(span - 1, Q)
            )
            expected_u = CORE | frozenset(
                order11[(i + t) % 11] for t in range(Q + span - 1)
            )
            assert lower == expected_l and len(lower) == 10 - span
            assert upper == expected_u and len(upper) == 8 + span

    scalar_solutions = [
        (143 - 11 * t, 10 * t)
        for t in range(14)
    ]
    assert all(10 * a + 11 * b == 1430 for a, b in scalar_solutions)
    assert scalar_solutions[0] == (143, 0)
    assert scalar_solutions[-1] == (0, 130)

    check_hist(1430, 1144, 1, 2, 858, 286)
    check_hist(1430, 728, 1, 2, 26, 702)
    check_hist(1430, 364, 3, 4, 26, 338)
    check_hist(1430, 140, 10, 11, 110, 30)
    check_hist(1430, 40, 35, 36, 10, 30)
    check_hist(1430, 8, 170, 180, 1, 7)
    assert 170 % 10 == 0 and 180 % 10 == 0

    # Translation development of one rank-r orbit is point-regular with
    # point degree r; 1,430 quotient occurrences therefore have degree
    # r*1,430 on every coordinate.
    assert 9 * 1430 == 12870
    assert 8 * 1430 == 11440
    assert 10 * 1430 == 14300

    print(
        "PASS k=17 q=4 period=10 owner_orbits=1430 "
        "ticket_formulas=period10+11_all_wraps orbit_counts=r5..15 "
        "rank15_hist=170x1+180x7 mixed_scalar_faces=14"
    )


if __name__ == "__main__":
    main()
