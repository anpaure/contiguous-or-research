#!/usr/bin/env python3
"""Independent H100 replay of the q4 pure-rail / k17 age-host bridge."""

from __future__ import annotations

import itertools
import math
from collections import Counter


Q = 4
GROUND = frozenset(range(17))
CORE = frozenset(range(5))
TYPE_COUNTS = {
    (1, 5, 2, 1): 139,
    (1, 6, 1, 1): 297,
    (2, 5, 1, 1): 8,
    (3, 3, 2, 1): 20,
    (3, 4, 1, 1): 20,
    (4, 3, 1, 1): 140,
    (5, 1, 2, 1): 127,
    (5, 2, 1, 1): 237,
    (6, 1, 1, 1): 442,
}


def partitions_with_sizes(sizes):
    values = tuple(CORE)
    for first in itertools.combinations(values, sizes[0]):
        first = frozenset(first)
        rest1 = tuple(x for x in values if x not in first)
        for second in itertools.combinations(rest1, sizes[1]):
            second = frozenset(second)
            third = CORE - first - second
            assert len(third) == sizes[2]
            yield first, second, third


def translate(value, shift):
    return frozenset((x + shift) % 17 for x in value)


def set_orbit_key(value):
    return min(tuple(sorted(translate(value, shift))) for shift in range(17))


def marked_orbit_key(owner, coordinate):
    return min(
        (tuple(sorted(translate(owner, shift))), (coordinate + shift) % 17)
        for shift in range(17)
    )


def check_period(period):
    order = tuple(range(5, 5 + period))
    owners = tuple(
        CORE
        | frozenset(order[(i + t) % period] for t in range(Q))
        for i in range(period)
    )
    assert len(set(owners)) == period
    for i in range(period):
        deleted = owners[i] - owners[(i + 1) % period]
        inserted = owners[(i + 1) % period] - owners[i]
        assert deleted == {order[i]}
        assert inserted == {order[(i + 4) % period]}

        j = (i + 1) % period
        inserted_before_j = next(iter(inserted))
        deleted_after_j3 = next(
            iter(owners[(j + 3) % period] - owners[(j + 4) % period])
        )
        assert inserted_before_j == deleted_after_j3
        run = [
            inserted_before_j in owners[(j + t) % period]
            for t in range(period)
        ]
        assert run[:4] == [True] * 4
        assert all(not bit for bit in run[4:])
        assert inserted_before_j not in owners[(j - 1) % period]
        assert inserted_before_j not in owners[(j + 4) % period]

        lower_q2 = owners[i] & owners[(i + 1) % period] & owners[(i + 2) % period]
        expected = CORE | {
            order[(i + 2) % period], order[(i + 3) % period]
        }
        assert lower_q2 == expected


def main():
    check_period(10)
    check_period(11)

    # Translation orbits are free, and forgetting a marked run coordinate
    # maps one marked orbit to exactly one owner orbit.  Hence marked run
    # starts over distinct owner orbits are necessarily distinct.
    owner_orbits = {}
    marked_to_owner = {}
    for owner_tuple in itertools.combinations(GROUND, 9):
        owner = frozenset(owner_tuple)
        owner_key = set_orbit_key(owner)
        owner_orbits.setdefault(owner_key, owner)
        for coordinate in owner:
            marked_key = marked_orbit_key(owner, coordinate)
            projected = set_orbit_key(frozenset(marked_key[0]))
            assert projected == owner_key
            if marked_key in marked_to_owner:
                assert marked_to_owner[marked_key] == owner_key
            else:
                marked_to_owner[marked_key] = owner_key
    assert len(owner_orbits) == math.comb(17, 9) // 17 == 1430
    assert len(marked_to_owner) == 9 * 1430 == 12870

    assert sum(TYPE_COUNTS.values()) == 1430
    singleton_age_zero = sum(
        count for kind, count in TYPE_COUNTS.items() if kind[0] == 1
    )
    rank7_slots = sum(
        count for kind, count in TYPE_COUNTS.items()
        if kind[0] + kind[1] == 7
    )
    assert singleton_age_zero == 436
    assert rank7_slots == 1144
    assert math.comb(17, 7) // 17 == 1144
    rank7_orbits = {
        set_orbit_key(frozenset(value))
        for value in itertools.combinations(GROUND, 7)
    }
    assert len(rank7_orbits) == 1144
    # A load in {1,2} at all 1,144 targets and total load 1,430 has the
    # unique multiplicity histogram below and admits one distinct selected
    # occurrence per target.
    doubled = 1430 - len(rank7_orbits)
    assert doubled == 286
    assert len(rank7_orbits) - doubled == 858

    expected_state_counts = {
        (1, 5, 2, 1): 5,
        (1, 6, 1, 1): 1,
        (2, 5, 1, 1): 5,
        (3, 3, 2, 1): 30,
        (3, 4, 1, 1): 10,
        (4, 3, 1, 1): 10,
        (5, 1, 2, 1): 5,
        (5, 2, 1, 1): 5,
        (6, 1, 1, 1): 1,
    }
    states = {}
    for kind in TYPE_COUNTS:
        sizes = tuple(value - 1 for value in kind[:3])
        assert sum(sizes) == 5
        states[kind] = tuple(partitions_with_sizes(sizes))
        assert len(states[kind]) == expected_state_counts[kind]

    transition_hist = Counter()
    for old_kind, old_states in states.items():
        for new_kind, new_states in states.items():
            legal_type = (
                new_kind[1] <= old_kind[0]
                and new_kind[2] <= old_kind[1]
                and new_kind[3] <= old_kind[2]
            )
            old_sizes = tuple(value - 1 for value in old_kind[:3])
            new_sizes = tuple(value - 1 for value in new_kind[:3])
            expected_successors = (
                math.comb(old_sizes[0], new_sizes[1])
                * math.comb(old_sizes[1], new_sizes[2])
                if legal_type else 0
            )
            for old_state in old_states:
                actual = [
                    new_state for new_state in new_states
                    if new_state[1] <= old_state[0]
                    and new_state[2] <= old_state[1]
                ]
                assert len(actual) == expected_successors
                transition_hist[(old_kind, new_kind)] += len(actual)
            assert (expected_successors > 0) == legal_type

    assert max(len(value) for value in states.values()) == 30
    mixed_faces = [
        (a, b) for a in range(144) for b in range(131)
        if 10 * a + 11 * b == 1430
    ]
    assert mixed_faces == sorted((143 - 11 * t, 10 * t) for t in range(14))
    print(
        "PASS q4_pure_age_bridge periods=10,11 run4=all_positions "
        "marked_orbit_projection=12870_to_1430 rank7=L3 "
        "certified_demands=436+1144 core_states_max=30 "
        f"legal_type_pairs={sum(v > 0 for v in transition_hist.values())}"
    )


if __name__ == "__main__":
    main()
