#!/usr/bin/env python3
"""Independent literal replay of the q=4 V13 seven-by-seven atom.

Run on H100.  The first five rails per shore form a four-owner rectangle;
the final two adjacent-swap pairs telescope through an intermediate core and
cancel that rectangle exactly.
"""

from collections import Counter


TARGET = frozenset(range(5))

BASE = [
    ("p10c4_1", +1, 4, [7, 10, 11, 3, 0, 5, 8, 9, 1, 2]),
    ("p10c4_2", +1, 4, [2, 12, 5, 11, 6, 10, 8, 1, 9, 0]),
    ("p11c0", +1, 0, [12, 11, 1, 10, 6, 5, 8, 9, 3, 4, 2]),
    ("p11c1", +1, 1, [8, 5, 11, 12, 6, 10, 2, 0, 4, 3, 9]),
    ("p11c2", +1, 2, [6, 0, 8, 9, 1, 12, 3, 7, 10, 11, 5]),
    ("n10c0", -1, 0, [5, 8, 9, 4, 2, 12, 11, 1, 10, 6]),
    ("n10c1", -1, 1, [12, 6, 10, 2, 0, 4, 9, 8, 5, 11]),
    ("n10c2", -1, 2, [4, 1, 9, 8, 0, 6, 5, 11, 10, 7]),
    ("n11c3", -1, 3, [1, 9, 8, 5, 0, 4, 11, 10, 7, 2, 12]),
    ("n11c4", -1, 4, [2, 0, 3, 9, 1, 8, 10, 6, 11, 5, 12]),
]

EXTRA = [
    ("pX1", +1, 8, [10, 11, 0, 4, 9, 2, 3, 5, 6, 7]),
    ("pX2", +1, 8, [10, 11, 5, 6, 7, 2, 3, 1, 9, 12]),
    ("nX1", -1, 8, [10, 11, 0, 4, 9, 3, 2, 5, 6, 7]),
    ("nX2", -1, 8, [10, 11, 5, 6, 7, 3, 2, 1, 9, 12]),
]


def deck(center, order):
    n = len(order)
    return [
        frozenset((center, *(order[(i+j) % n] for j in range(4))))
        for i in range(n)
    ]


def signed_nonzero(rails):
    out = Counter()
    for _, sign, center, order in rails:
        for owner in deck(center, order):
            out[owner] += sign
    return {owner: value for owner, value in out.items() if value}


def main():
    rails = BASE + EXTRA
    positive = Counter()
    negative = Counter()
    point = Counter()
    for name, sign, center, order in rails:
        assert len(order) in (10, 11)
        assert len(order) == len(set(order))
        assert center not in order
        assert set(order) <= set(range(13))
        owners = deck(center, order)
        assert len(owners) == len(set(owners)) == len(order)
        assert all(
            len(owners[i] ^ owners[(i + 1) % len(owners)]) == 2
            for i in range(len(owners))
        )
        (positive if sign > 0 else negative).update(owners)
        point[center] += sign * len(order)
        for x in order:
            point[x] += sign * 4

    assert sum(positive.values()) == 73
    assert sum(negative.values()) == 72
    assert max(positive.values()) == max(negative.values()) == 1
    difference = positive.copy()
    difference.subtract(negative)
    assert {owner: value for owner, value in difference.items() if value} == {
        TARGET: 1
    }
    assert [point[x] for x in range(13)] == [1] * 5 + [0] * 8
    assert set(negative) < set(positive)
    assert set(positive) - set(negative) == {TARGET}

    c1a = frozenset((0, 2, 4, 8, 9))
    c1b = frozenset((0, 3, 4, 8, 9))
    c2a = frozenset((1, 2, 8, 9, 12))
    c2b = frozenset((1, 3, 8, 9, 12))
    assert signed_nonzero(BASE) == {c1a: -1, c1b: 1, c2a: 1, c2b: -1, TARGET: 1}
    assert signed_nonzero(EXTRA) == {c1a: 1, c1b: -1, c2a: -1, c2b: 1}

    cstar_a = frozenset((2, 5, 6, 7, 8))
    cstar_b = frozenset((3, 5, 6, 7, 8))
    assert signed_nonzero((EXTRA[0], EXTRA[2])) == {
        c1a: 1, c1b: -1, cstar_a: -1, cstar_b: 1,
    }
    assert signed_nonzero((EXTRA[1], EXTRA[3])) == {
        cstar_a: 1, cstar_b: -1, c2a: -1, c2b: 1,
    }

    # Each extra negative order is obtained from its positive mate by the
    # single adjacent transposition 2,3.  The intermediate core is
    # {5,6,7,8}; its two contributions cancel in the sum.
    assert EXTRA[2][3] == EXTRA[0][3][:5] + [3, 2] + EXTRA[0][3][7:]
    assert EXTRA[3][3] == EXTRA[1][3][:5] + [3, 2] + EXTRA[1][3][7:]

    print(
        "PASS q=4 ground=13 rails=7x7 positive_owners=73 negative_owners=72 "
        "shore_simple=yes difference=01234 rectangle_telescoped=yes"
    )


if __name__ == "__main__":
    main()
