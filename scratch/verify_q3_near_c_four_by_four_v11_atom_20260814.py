#!/usr/bin/env python3
"""Independent verifier for the q=3 four-by-four atom on 11 labels.

The verifier imports no solver code.  Run substantively on H100 only.
"""

from collections import Counter


GROUND = frozenset(range(11))
TARGET = frozenset((0, 1, 2, 3))

RAILS = [
    ("p8a", +1, 0, (1, 2, 3, 10, 7, 5, 6, 8)),
    ("p8b", +1, 0, (1, 4, 2, 7, 5, 3, 9, 8)),
    ("p9a", +1, 1, (2, 6, 3, 7, 5, 10, 9, 4, 8)),
    ("p9b", +1, 2, (0, 1, 7, 5, 10, 6, 8, 3, 9)),
    ("n9", -1, 0, (1, 9, 2, 3, 10, 7, 5, 6, 8)),
    ("n8a", -1, 1, (0, 8, 4, 9, 10, 5, 7, 2)),
    ("n8b", -1, 2, (0, 7, 5, 10, 6, 8, 1, 4)),
    ("n8c", -1, 3, (0, 5, 7, 1, 6, 2, 8, 9)),
]


def owners(center, cycle):
    n = len(cycle)
    return [
        frozenset((center, cycle[i], cycle[(i + 1) % n],
                   cycle[(i + 2) % n]))
        for i in range(n)
    ]


def encode(value):
    return "".join(map(str, sorted(value)))


def main():
    positive = Counter()
    negative = Counter()
    point_difference = Counter()
    support_holes = {}
    rail_owner_counts = {}

    for name, sign, center, cycle in RAILS:
        assert len(cycle) in (8, 9)
        assert len(cycle) == len(set(cycle))
        assert center not in cycle
        assert set(cycle) < GROUND
        deck = owners(center, cycle)
        assert len(deck) == len(set(deck)) == len(cycle)
        assert all(len(owner) == 4 for owner in deck)
        for left, right in zip(deck, deck[1:] + deck[:1]):
            assert len(left - right) == len(right - left) == 1
        (positive if sign > 0 else negative).update(deck)
        point_difference[center] += sign * len(cycle)
        for value in cycle:
            point_difference[value] += sign * 3
        support_holes[name] = sorted(GROUND - {center} - set(cycle))
        rail_owner_counts[name] = len(deck)

    assert sum(positive.values()) == 34
    assert sum(negative.values()) == 33
    assert len(positive) == 34 and all(value == 1 for value in positive.values())
    assert len(negative) == 33 and all(value == 1 for value in negative.values())
    assert set(negative) < set(positive)
    assert set(positive) - set(negative) == {TARGET}

    difference = positive.copy()
    difference.subtract(negative)
    assert {owner: count for owner, count in difference.items() if count} == {
        TARGET: 1
    }
    assert [point_difference[x] for x in range(11)] == [1, 1, 1, 1] + [0] * 7
    auxiliary_count_histogram = Counter(len(owner - TARGET) for owner in positive)

    # Exact centre profile: +2 short at z0, +1 long at z1,z2;
    # -1 long at z0 and -1 short at z1,z2,z3.
    assert [(sign, len(cycle), center) for _, sign, center, cycle in RAILS] == [
        (+1, 8, 0), (+1, 8, 0), (+1, 9, 1), (+1, 9, 2),
        (-1, 9, 0), (-1, 8, 1), (-1, 8, 2), (-1, 8, 3),
    ]
    assert support_holes == {
        "p8a": [4, 9], "p8b": [6, 10],
        "p9a": [0], "p9b": [4], "n9": [4],
        "n8a": [3, 6], "n8b": [3, 9], "n8c": [4, 10],
    }

    print(
        "PASS q=3 ground=11 positive_rails=4 negative_rails=4 "
        "positive_owners=34 negative_owners=33 common_owners=33 "
        "extra_owner=0123 shore_simple=yes rail_cycles_johnson=yes "
        "point_difference=1,1,1,1,0,0,0,0,0,0,0 "
        "rail_owner_counts="
        + ",".join(f"{name}:{rail_owner_counts[name]}" for name, *_ in RAILS)
        + " auxiliary_count_histogram="
        + ",".join(
            f"{count}:{auxiliary_count_histogram[count]}"
            for count in sorted(auxiliary_count_histogram)
        )
    )


if __name__ == "__main__":
    main()
