#!/usr/bin/env python3
"""Exact audit of the q=2 distance-one near-C owner absorber.

The published certificate is an exact simple owner trade.  This verifier
reconstructs both owner and immediate-lower decks and checks the coupled
alternating current.  It intentionally has no third-party dependencies.
"""

from collections import Counter


PLUS = [
    (0, "124685"),
    (0, "263748"),
    (1, "2486375"),
    (2, "1356487"),
    (3, "142678"),
    (5, "038247"),
    (6, "143827"),
    (8, "015647"),
]

MINUS = [
    (0, "1537468"),
    (1, "258437"),
    (2, "046358"),
    (3, "124678"),
    (4, "125786"),
    (6, "025813"),
    (7, "051628"),
    (8, "042635"),
]

EXPECTED_LOWER_CURRENT = {
    (0, 2): 1,
    (0, 4): 1,
    (0, 5): 1,
    (0, 7): -1,
    (0, 8): 1,
    (1, 2): 1,
    (1, 4): -1,
    (1, 6): 1,
    (1, 7): -1,
    (1, 8): 1,
    (2, 4): -1,
    (2, 5): 1,
    (2, 8): -1,
    (3, 5): 1,
    (3, 8): -1,
    (4, 7): -1,
    (4, 8): -1,
    (5, 6): -1,
    (5, 8): 1,
}


def decks(table):
    owners = Counter()
    lowers = Counter()
    support_degree = Counter()
    weighted_core_degree = Counter()
    for core, word_text in table:
        word = tuple(map(int, word_text))
        assert core not in word
        assert len(set(word)) == len(word)
        period = len(word)
        for j, x in enumerate(word):
            y = word[(j + 1) % period]
            owners[tuple(sorted((core, x, y)))] += 1
            lowers[tuple(sorted((core, x)))] += 1
        for x in word:
            support_degree[x] += 1
        weighted_core_degree[core] += period
    return owners, lowers, support_degree, weighted_core_degree


def signed(a, b):
    return {
        key: a[key] - b[key]
        for key in set(a) | set(b)
        if a[key] != b[key]
    }


def point_current(current):
    out = Counter()
    for subset, coefficient in current.items():
        for x in subset:
            out[x] += coefficient
    return Counter({x: v for x, v in out.items() if v})


def main():
    op, lp, up, kp = decks(PLUS)
    om, lm, um, km = decks(MINUS)

    assert sum(op.values()) == 50
    assert sum(om.values()) == 49
    assert max(op.values()) == max(om.values()) == 1
    assert signed(op, om) == {(0, 1, 2): 1}

    # The lower shores are not matchings, even though both owner shores are.
    assert sum(lp.values()) == 50 and len(lp) == 34 and max(lp.values()) == 3
    assert sum(lm.values()) == 49 and len(lm) == 35 and max(lm.values()) == 2
    assert sum(v > 1 for v in lp.values()) == 15
    assert sum(v > 1 for v in lm.values()) == 14

    lower_current = signed(lp, lm)
    assert lower_current == EXPECTED_LOWER_CURRENT
    assert sum(lower_current.values()) == 1
    assert sum(abs(v) for v in lower_current.values()) == 19

    owner_current = signed(op, om)
    owner_points = point_current(owner_current)
    lower_points = point_current(lower_current)
    support_current = signed(up, um)
    core_current = signed(kp, km)

    # For q=2: U=O-L and K=2L-O, on the reduced labels.  The omitted
    # common core C_0 contributes +1 to both O and L and hence +1 to K.
    assert Counter(owner_points) - Counter(lower_points) == Counter(
        {x: v for x, v in support_current.items() if v > 0}
    )
    # Counter subtraction discards negatives, so check the signed identities.
    assert signed(owner_points, lower_points) == support_current
    twice_lower = Counter({x: 2 * v for x, v in lower_points.items()})
    assert signed(twice_lower, owner_points) == core_current

    print("q2_near_c_owner_current", signed(op, om))
    print("plus_lower_mass_support_max", sum(lp.values()), len(lp), max(lp.values()))
    print("minus_lower_mass_support_max", sum(lm.values()), len(lm), max(lm.values()))
    print("lower_current_mass_l1_support", sum(lower_current.values()),
          sum(abs(v) for v in lower_current.values()), len(lower_current))
    print("lower_current", sorted(lower_current.items()))
    print("support_current", sorted(support_current.items()))
    print("weighted_core_current", sorted(core_current.items()))
    print("PASS")


if __name__ == "__main__":
    main()
