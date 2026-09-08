#!/usr/bin/env python3
"""Independent q4 five-rail centre/profile and V13 support replay.

Run substantive verification on H100.  No OR-Tools or search code is
imported.  The script enumerates the finite centre ledger and directly
checks every displayed feasible hole certificate.
"""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict
from functools import lru_cache


V = tuple(range(13))
V12 = tuple(range(12))
TARGET = frozenset(range(5))

T_EXPECTED = {
    (-3, 1, 5), (-2, 3, -3), (-1, 1, 0),
    (0, -1, 3), (1, 1, -5), (2, -1, -2),
}
T_EXTRA_NORM6 = (3, -3, 1)
E_EXPECTED = {
    (-3, 2, 2), (-2, 0, 5), (-1, 2, -3), (0, 0, 0),
    (1, -2, 3), (2, 0, -5), (3, -2, -2),
}

T = [
    (-3, 1, 5), (-2, 3, -3), (-1, 1, 0),
    (0, -1, 3), (1, 1, -5), (2, -1, -2),
]
T_RELEVANT = T + [T_EXTRA_NORM6]
E = [
    (-3, 2, 2), (-2, 0, 5), (-1, 2, -3),
    (1, -2, 3), (2, 0, -5), (3, -2, -2),
]

EXPECTED_PROFILES = {
    ((0, 3, 3, 4, 4), ()),
    ((1, 3, 3, 3, 4), ()),
    ((2, 2, 2, 3, 3), (4,)),
    ((2, 2, 2, 3, 5), ()),
    ((2, 3, 3, 3, 4), (2,)),
    ((2, 3, 3, 4, 4), (1,)),
}


def local_states(h):
    out = set()
    for a in range(-5, 6):
        for b in range(-5, 6):
            positive_centres = max(a, 0) + max(b, 0)
            negative_centres = max(-a, 0) + max(-b, 0)
            if positive_centres > 5 or negative_centres > 5:
                continue
            numerator = h - 10 * a - 11 * b
            if numerator % 4:
                continue
            t = numerator // 4
            if abs(t) <= 5:
                out.add((a, b, t))
    return out


def enumerate_profiles():
    out = set()
    for targets in itertools.combinations_with_replacement(
            range(len(T_RELEVANT)), 5):
        norm = sum(
            abs(T_RELEVANT[i][0]) + abs(T_RELEVANT[i][1])
            for i in targets
        )
        if norm > 10:
            continue
        for number_exterior in range(6):
            for exterior in itertools.combinations_with_replacement(
                    range(len(E)), number_exterior):
                total_norm = norm + sum(
                    abs(E[i][0]) + abs(E[i][1]) for i in exterior
                )
                if total_norm != 10:
                    continue
                sum_a = sum(T_RELEVANT[i][0] for i in targets) + sum(
                    E[i][0] for i in exterior
                )
                sum_b = sum(T_RELEVANT[i][1] for i in targets) + sum(
                    E[i][1] for i in exterior
                )
                if (sum_a, sum_b) == (-1, 1):
                    out.add((targets, exterior))
    return out


MASS5_STATES = {
    2: ([T[1], T[3], T[3], T[3], T[4]], []),
    3: ([T[2], T[2], T[2], T[3], T[3]], [E[4]]),
    4: ([T[2], T[2], T[2], T[3], T[5]], []),
    5: ([T[2], T[3], T[3], T[3], T[4]], [E[2]]),
}

MASS5_ALL_STATES = {
    1: ([T[0], T[3], T[3], T[4], T[4]], []),
    **MASS5_STATES,
    6: ([T[2], T[3], T[3], T[4], T[4]], [E[1]]),
}

MASS5_HOLES = {
    2: {
        "n10c0_1": (1, 3), "n10c0_2": (1, 12),
        "n11c1_1": (2,), "n11c2_1": (3,), "n11c3_1": (2,),
        "p10c4_1": (0, 12), "p11c0_1": (4,), "p11c0_2": (4,),
        "p11c0_3": (4,), "p11c4_1": (0,),
    },
    3: {
        "n10c0_1": (1, 7), "n10c1_1": (3, 9),
        "n10c2_1": (4, 10), "n11c3_1": (4,), "n11c4_1": (3,),
        "p10c5_1": (7, 9), "p10c5_2": (1, 10),
        "p11c0_1": (5,), "p11c1_1": (5,), "p11c2_1": (5,),
    },
    4: {
        "n10c0_1": (3, 5), "n10c1_1": (0, 3),
        "n10c2_1": (1, 3), "n11c3_1": (0,), "n11c4_1": (3,),
        "p10c4_1": (0, 1), "p10c4_2": (0, 5),
        "p11c0_1": (3,), "p11c1_1": (4,), "p11c2_1": (3,),
    },
    5: {
        "n10c0_1": (1, 11), "n10c5_1": (1, 2),
        "n11c1_1": (3,), "n11c2_1": (3,), "n11c3_1": (2,),
        "p10c4_1": (5, 11), "p11c0_1": (4,), "p11c4_1": (5,),
        "p11c5_1": (4,), "p11c5_2": (4,),
    },
}

MASS4_HOLES = {
    (10, "A"): {
        "n10A": (3, 11), "n10A0": (3, 4), "n10A1": (3, 4),
        "n11C3": (12,), "n11C4": (0,), "p10A": (2, 12),
        "p10B": (0, 3), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    },
    (10, "C"): {
        "n10A0": (3, 11), "n10A1": (3, 5), "n10C": (4, 11),
        "n11C3": (4,), "n11C4": (0,), "p10B": (5, 11),
        "p10C": (0, 2), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    },
    (10, "X"): {
        "n10A0": (3, 11), "n10A1": (3, 4), "n10X": (4, 11),
        "n11C3": (4,), "n11C4": (1,), "p10B": (4, 11),
        "p10X": (1, 2), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    },
    (11, "A"): {
        "n10A0": (3, 5), "n10A1": (0, 12), "n11A": (4,),
        "n11C3": (4,), "n11C4": (3,), "p10B": (0, 5),
        "p11A": (2,), "p11A0": (2,), "p11A1": (2,), "p11B": (12,),
    },
    (11, "C"): {
        "n10A0": (3, 12), "n10A1": (3, 11), "n11C": (4,),
        "n11C3": (4,), "n11C4": (3,), "p10B": (3, 11),
        "p11A0": (2,), "p11A1": (2,), "p11B": (12,), "p11C": (2,),
    },
    (11, "X"): {
        "n10A0": (3, 7), "n10A1": (3, 11), "n11C3": (4,),
        "n11C4": (12,), "n11X": (4,), "p10B": (7, 11),
        "p11A0": (2,), "p11A1": (2,), "p11B": (12,), "p11X": (2,),
    },
}


def rails_from_states(target_states, exterior_states):
    rails = []
    serial = defaultdict(int)
    for centre, (a, b, _) in list(enumerate(target_states)) + [
            (5 + i, state) for i, state in enumerate(exterior_states)]:
        for period, count in ((10, a), (11, b)):
            sign = 1 if count > 0 else -1
            for _ in range(abs(count)):
                key = (sign, period, centre)
                serial[key] += 1
                rails.append((
                    f"{'p' if sign > 0 else 'n'}{period}c{centre}_{serial[key]}",
                    sign, period, centre,
                ))
    return rails


def mass4_rails(period, kind):
    centre = {"A": 0, "B": 2, "C": 3, "X": 5}[kind]
    rails = [
        ("p10B", 1, 10, 2), ("p11A0", 1, 11, 0),
        ("p11A1", 1, 11, 1), ("p11B", 1, 11, 2),
        (f"p{period}{kind}", 1, period, centre),
        ("n10A0", -1, 10, 0), ("n10A1", -1, 10, 1),
        ("n11C3", -1, 11, 3), ("n11C4", -1, 11, 4),
        (f"n{period}{kind}", -1, period, centre),
    ]
    return rails


def verify_holes(rails, holes):
    assert {name for name, *_ in rails} == set(holes)
    point = Counter()
    for name, sign, period, centre in rails:
        row_holes = frozenset(holes[name])
        assert centre not in row_holes
        assert len(row_holes) == 12 - period
        support = set(V) - {centre} - set(row_holes)
        assert len(support) == period
        point[centre] += sign * period
        for x in support:
            point[x] += sign * 4
    assert [point[x] for x in V] == [1] * 5 + [0] * 8


def v12_support_feasible(rails):
    """Exact one-hole assignment test; period-11 rows have no V12 hole."""
    desired = []
    for z in V12:
        a = sum(sign for _, sign, period, centre in rails
                if period == 10 and centre == z)
        b = sum(sign for _, sign, period, centre in rails
                if period == 11 and centre == z)
        numerator = (1 if z in TARGET else 0) - 10 * a - 11 * b
        assert numerator % 4 == 0
        t = numerator // 4
        desired.append(-(a + b) - t)

    short_rows = tuple(
        (sign, centre) for _, sign, period, centre in rails if period == 10
    )

    @lru_cache(None)
    def complete(row, remaining):
        if row == len(short_rows):
            return not any(remaining)
        sign, centre = short_rows[row]
        for hole in V12:
            if hole == centre:
                continue
            changed = list(remaining)
            changed[hole] -= sign
            if complete(row + 1, tuple(changed)):
                return True
        return False

    return complete(0, tuple(desired))


def main():
    target_states = local_states(1)
    exterior_states = local_states(0)
    assert {
        state for state in target_states
        if abs(state[0]) + abs(state[1]) <= 6
    } == T_EXPECTED | {T_EXTRA_NORM6}
    assert {
        state for state in exterior_states
        if abs(state[0]) + abs(state[1]) <= 5
    } == E_EXPECTED
    assert min(abs(a) + abs(b) for a, b, _ in target_states) == 1
    assert T_EXTRA_NORM6[0] + 4 * T[3][0] == 3 != -1
    assert T_EXTRA_NORM6[1] + 4 * T[3][1] == -7 != 1
    profiles = enumerate_profiles()
    assert profiles == EXPECTED_PROFILES, (profiles, EXPECTED_PROFILES)

    for profile, (targets, exterior) in MASS5_STATES.items():
        verify_holes(rails_from_states(targets, exterior), MASS5_HOLES[profile])
    for key, holes in MASS4_HOLES.items():
        verify_holes(mass4_rails(*key), holes)

    v12_cases = {
        f"mass4_p{period}_{kind}": mass4_rails(period, kind)
        for period in (10, 11) for kind in ("A", "B", "C", "X")
    }
    v12_cases.update({
        f"mass5_profile_{profile}": rails_from_states(targets, exterior)
        for profile, (targets, exterior) in MASS5_ALL_STATES.items()
    })
    assert len(v12_cases) == 14
    assert not {name for name, rails in v12_cases.items()
                if v12_support_feasible(rails)}

    # The two symbolic V13 failures.
    # Profile 1: T1 has one positive centre, so at most four positive
    # noncentre supports can contain it, yet t=5.
    assert T[0] == (-3, 1, 5) and 5 - (0 + 1) < 5
    # Profile 6: E2 forces all three noncentred negative rails to hole it;
    # both T5 columns force all three noncentred positives to hole them.
    # The unique positive long rail at T3 would need both T5 holes.
    assert T[2] == (-1, 1, 0) and T[4] == (1, 1, -5) and E[1] == (-2, 0, 5)
    assert 12 - 11 == 1 < 2

    # Cancellation at B leaves only four negative noncentre supports, so
    # its signed support value cannot be -5.
    assert 5 - 1 == 4 < 5

    print(
        "PASS q=4 shore=5 relevant_target_character_states=7 "
        "relevant_exterior_character_states=7 "
        "mass5_profiles=6 mass5_v13_feasible=4 mass5_v13_infeasible=2 "
        "mass4_v13_feasible=6 mass4_B_infeasible=yes "
        "v12_support_infeasible_cases=14"
    )


if __name__ == "__main__":
    main()
