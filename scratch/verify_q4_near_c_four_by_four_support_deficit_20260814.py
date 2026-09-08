#!/usr/bin/env python3
"""Verify the q=4 centre-equality profiles and support deficit.

Substantive execution belongs on H100.  The script enumerates every local
target equality state of the sharp supporting plane, every five-target
global equality profile with sums a=-1,b=1, and the forced toggle-support
imbalance t from the exact point equation.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import product


def main():
    local = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            if (2 * a + 3 * b - 1) % 4:
                continue
            slack = 2 * abs(a) + 2 * abs(b) - b
            if slack != 3:
                continue
            numerator = 1 - 10 * a - 11 * b
            assert numerator % 4 == 0
            local.append((a, b, numerator // 4))
    assert set(local) == {(-1, 1, 0), (1, 1, -5), (0, -1, 3), (0, 3, -8)}

    exterior = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            if (2 * a + 3 * b) % 4:
                continue
            if 2 * abs(a) + 2 * abs(b) - b:
                continue
            numerator = -10 * a - 11 * b
            assert numerator % 4 == 0
            exterior.append((a, b, numerator // 4))
    assert exterior == [(0, 0, 0)]

    profiles = set()
    for states in product(local, repeat=5):
        if sum(state[0] for state in states) != -1:
            continue
        if sum(state[1] for state in states) != 1:
            continue
        if sum(abs(state[0]) + abs(state[1]) for state in states) != 8:
            continue
        profiles.add(tuple(sorted(Counter(states).items())))

    expected = {
        tuple(sorted(Counter({(-1, 1, 0): 2, (1, 1, -5): 1,
                              (0, -1, 3): 2}).items())),
        tuple(sorted(Counter({(-1, 1, 0): 1, (0, -1, 3): 3,
                              (0, 3, -8): 1}).items())),
    }
    assert profiles == expected
    assert all(any(abs(state[2]) > 4 for state, count in profile if count)
               for profile in profiles)
    shore_five_survivors = {
        profile for profile in profiles
        if all(abs(state[2]) <= 5 for state, count in profile if count)
    }
    assert len(shore_five_survivors) == 1
    survivor = next(iter(shore_five_survivors))
    assert dict(survivor) == {
        (-1, 1, 0): 2,
        (0, -1, 3): 2,
        (1, 1, -5): 1,
    }

    report = {
        "status": "PASS",
        "q": 4,
        "short_period": 10,
        "long_period": 11,
        "target_equality_states": [
            {"a": a, "b": b, "forced_t": t}
            for a, b, t in sorted(local)
        ],
        "exterior_equality_states": [
            {"a": a, "b": b, "forced_t": t} for a, b, t in exterior
        ],
        "global_equality_profiles": [
            [
                {"a": state[0], "b": state[1], "forced_t": state[2],
                 "multiplicity": count}
                for state, count in profile
            ]
            for profile in sorted(profiles)
        ],
        "physical_shore_four_support_bound": 4,
        "all_profiles_violate_support_bound": True,
        "minimum_physical_shore_lower_bound": 5,
        "shore_five_net_mass_four_surviving_profiles": 1,
        "shore_five_survivor_is_profile_I": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
