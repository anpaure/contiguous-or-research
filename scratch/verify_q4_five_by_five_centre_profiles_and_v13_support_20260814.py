#!/usr/bin/env python3
"""Independent verifier for the q4 five-rail centre/support reduction.

No solver code is imported.  Substantive execution belongs on H100.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter


V = frozenset(range(13))
TARGET = frozenset(range(5))

T = (
    (-3, 1, 5), (-2, 3, -3), (-1, 1, 0),
    (0, -1, 3), (1, 1, -5), (2, -1, -2),
)
T_EXTRA_NORM6 = (3, -3, 1)
T_RELEVANT = T + (T_EXTRA_NORM6,)
E = (
    (-3, 2, 2), (-2, 0, 5), (-1, 2, -3),
    (1, -2, 3), (2, 0, -5), (3, -2, -2),
)


def enumerate_local(h):
    states = []
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
            if abs(t) <= 5 and (a or b or h):
                states.append((a, b, t))
    return tuple(states)


def centre_profiles():
    profiles = set()
    for targets in itertools.combinations_with_replacement(T_RELEVANT, 5):
        target_norm = sum(abs(a) + abs(b) for a, b, _ in targets)
        if target_norm > 10:
            continue
        for counts in itertools.product(range(6), repeat=len(E)):
            if sum(counts) > 5:
                continue
            norm = target_norm + sum(
                count * (abs(state[0]) + abs(state[1]))
                for state, count in zip(E, counts)
            )
            if norm != 10:
                continue
            all_states = list(targets) + [
                state for state, count in zip(E, counts) for _ in range(count)
            ]
            if sum(state[0] for state in all_states) != -1:
                continue
            if sum(state[1] for state in all_states) != 1:
                continue
            profiles.add((
                tuple(sorted(Counter(targets).items())),
                tuple((state, count) for state, count in zip(E, counts) if count),
            ))
    return profiles


def rail(name, sign, period, center, holes):
    return (name, sign, period, center, tuple(holes))


MASS5 = {
    2: [
        rail("n10c0_1", -1, 10, 0, (1, 3)),
        rail("n10c0_2", -1, 10, 0, (1, 12)),
        rail("n11c1", -1, 11, 1, (2,)),
        rail("n11c2", -1, 11, 2, (3,)),
        rail("n11c3", -1, 11, 3, (2,)),
        rail("p10c4", 1, 10, 4, (0, 12)),
        rail("p11c0_1", 1, 11, 0, (4,)),
        rail("p11c0_2", 1, 11, 0, (4,)),
        rail("p11c0_3", 1, 11, 0, (4,)),
        rail("p11c4", 1, 11, 4, (0,)),
    ],
    3: [
        rail("n10c0", -1, 10, 0, (1, 7)),
        rail("n10c1", -1, 10, 1, (3, 9)),
        rail("n10c2", -1, 10, 2, (4, 10)),
        rail("n11c3", -1, 11, 3, (4,)),
        rail("n11c4", -1, 11, 4, (3,)),
        rail("p10c5_1", 1, 10, 5, (7, 9)),
        rail("p10c5_2", 1, 10, 5, (1, 10)),
        rail("p11c0", 1, 11, 0, (5,)),
        rail("p11c1", 1, 11, 1, (5,)),
        rail("p11c2", 1, 11, 2, (5,)),
    ],
    4: [
        rail("n10c0", -1, 10, 0, (3, 5)),
        rail("n10c1", -1, 10, 1, (0, 3)),
        rail("n10c2", -1, 10, 2, (1, 3)),
        rail("n11c3", -1, 11, 3, (0,)),
        rail("n11c4", -1, 11, 4, (3,)),
        rail("p10c4_1", 1, 10, 4, (0, 1)),
        rail("p10c4_2", 1, 10, 4, (0, 5)),
        rail("p11c0", 1, 11, 0, (3,)),
        rail("p11c1", 1, 11, 1, (4,)),
        rail("p11c2", 1, 11, 2, (3,)),
    ],
    5: [
        rail("n10c0", -1, 10, 0, (1, 11)),
        rail("n10c5", -1, 10, 5, (1, 2)),
        rail("n11c1", -1, 11, 1, (3,)),
        rail("n11c2", -1, 11, 2, (3,)),
        rail("n11c3", -1, 11, 3, (2,)),
        rail("p10c4", 1, 10, 4, (5, 11)),
        rail("p11c0", 1, 11, 0, (4,)),
        rail("p11c4", 1, 11, 4, (5,)),
        rail("p11c5_1", 1, 11, 5, (4,)),
        rail("p11c5_2", 1, 11, 5, (4,)),
    ],
}


def mass4_case(period, kind, holes):
    centre = {"A": 0, "C": 3, "X": 5}[kind]
    rails = [
        ("p10B", 1, 10, 2), ("p11A0", 1, 11, 0),
        ("p11A1", 1, 11, 1), ("p11B", 1, 11, 2),
        (f"p{period}{kind}", 1, period, centre),
        ("n10A0", -1, 10, 0), ("n10A1", -1, 10, 1),
        ("n11C3", -1, 11, 3), ("n11C4", -1, 11, 4),
        (f"n{period}{kind}", -1, period, centre),
    ]
    return [rail(name, sign, size, center, holes[name])
            for name, sign, size, center in rails]


MASS4 = {
    "p10A": mass4_case(10, "A", {
        "n10A": (3, 11), "n10A0": (3, 4), "n10A1": (3, 4),
        "n11C3": (12,), "n11C4": (0,), "p10A": (2, 12),
        "p10B": (0, 3), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    }),
    "p10C": mass4_case(10, "C", {
        "n10A0": (3, 11), "n10A1": (3, 5), "n10C": (4, 11),
        "n11C3": (4,), "n11C4": (0,), "p10B": (5, 11),
        "p10C": (0, 2), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    }),
    "p10X": mass4_case(10, "X", {
        "n10A0": (3, 11), "n10A1": (3, 4), "n10X": (4, 11),
        "n11C3": (4,), "n11C4": (1,), "p10B": (4, 11),
        "p10X": (1, 2), "p11A0": (2,), "p11A1": (2,), "p11B": (11,),
    }),
    "p11A": mass4_case(11, "A", {
        "n10A0": (3, 5), "n10A1": (0, 12), "n11A": (4,),
        "n11C3": (4,), "n11C4": (3,), "p10B": (0, 5),
        "p11A": (2,), "p11A0": (2,), "p11A1": (2,), "p11B": (12,),
    }),
    "p11C": mass4_case(11, "C", {
        "n10A0": (3, 12), "n10A1": (3, 11), "n11C": (4,),
        "n11C3": (4,), "n11C4": (3,), "p10B": (3, 11),
        "p11A0": (2,), "p11A1": (2,), "p11B": (12,), "p11C": (2,),
    }),
    "p11X": mass4_case(11, "X", {
        "n10A0": (3, 7), "n10A1": (3, 11), "n11C3": (4,),
        "n11C4": (12,), "n11X": (4,), "p10B": (7, 11),
        "p11A0": (2,), "p11A1": (2,), "p11B": (12,), "p11X": (2,),
    }),
}


def verify_support_case(name, rails):
    assert len(rails) == 10
    assert sum(sign > 0 for _, sign, *_ in rails) == 5
    assert sum(sign < 0 for _, sign, *_ in rails) == 5
    point = Counter()
    positive_holes = Counter()
    negative_holes = Counter()
    centre_short = Counter()
    centre_long = Counter()
    support_signed = Counter()
    for rail_name, sign, period, center, holes in rails:
        assert len(holes) == 12 - period
        assert len(set(holes)) == len(holes)
        assert center not in holes
        assert set(holes) < V
        support = V - {center} - set(holes)
        assert len(support) == period
        point[center] += sign * period
        for value in support:
            point[value] += sign * 4
            support_signed[value] += sign
        (positive_holes if sign > 0 else negative_holes).update(holes)
        (centre_short if period == 10 else centre_long)[center] += sign
    assert [point[x] for x in range(13)] == [1] * 5 + [0] * 8
    for x in range(13):
        a, b, t = centre_short[x], centre_long[x], support_signed[x]
        assert 10 * a + 11 * b + 4 * t == (1 if x in TARGET else 0)
        assert positive_holes[x] - negative_holes[x] == -(a + b) - t
    return {
        "case": name,
        "positive_period_sum": sum(period for _, sign, period, *_ in rails if sign > 0),
        "negative_period_sum": sum(period for _, sign, period, *_ in rails if sign < 0),
    }


def main():
    target_states = enumerate_local(1)
    exterior_states = enumerate_local(0)
    assert tuple(
        state for state in target_states
        if abs(state[0]) + abs(state[1]) <= 6
    ) == T_RELEVANT
    assert tuple(
        state for state in exterior_states
        if 0 < abs(state[0]) + abs(state[1]) <= 5
    ) == E
    assert T_EXTRA_NORM6[0] + 4 * T[3][0] == 3 != -1
    assert T_EXTRA_NORM6[1] + 4 * T[3][1] == -7 != 1
    profiles = centre_profiles()
    assert len(profiles) == 6

    expected_targets = (
        (T[0], T[3], T[3], T[4], T[4]),
        (T[1], T[3], T[3], T[3], T[4]),
        (T[2], T[2], T[2], T[3], T[3]),
        (T[2], T[2], T[2], T[3], T[5]),
        (T[2], T[3], T[3], T[3], T[4]),
        (T[2], T[3], T[3], T[4], T[4]),
    )
    expected_exteriors = ((), (), (E[4],), (), (E[2],), (E[1],))
    expected = {
        (tuple(sorted(Counter(targets).items())),
         tuple(sorted(Counter(exteriors).items())))
        for targets, exteriors in zip(expected_targets, expected_exteriors)
    }
    assert profiles == expected

    # Profile 1: at T1 only four positive rails are noncentred, so t<=4<5.
    assert T[0] == (-3, 1, 5)
    # Profile 6: E2 forces three negative holes; each T5 forces three
    # positive holes.  The unique positive long T3 rail would need a hole at
    # both T5 labels although a period-11 row has only one.
    assert E[1] == (-2, 0, 5) and T[4] == (1, 1, -5)

    reports = []
    for profile, rails in MASS5.items():
        reports.append(verify_support_case(f"mass5_profile_{profile}", rails))
    for case, rails in MASS4.items():
        reports.append(verify_support_case(f"mass4_cancel_{case}", rails))

    print(json.dumps({
        "status": "PASS",
        "target_local_states": len(T),
        "exterior_local_states": len(E),
        "mass5_centre_profiles": len(profiles),
        "mass5_support_infeasible_profiles": [1, 6],
        "mass5_literal_support_certificates": sorted(MASS5),
        "mass4_literal_support_certificates": sorted(MASS4),
        "verified_support_cases": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
