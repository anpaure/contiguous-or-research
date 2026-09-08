#!/usr/bin/env python3
"""Exact finite certificate: two disjoint 7-point wreaths need not extend.

This verifier uses only the Python standard library.  Cyclic orders are
identified up to rotation and reversal.  It checks the separating weight
certificate against every possible remaining wreath row.
"""

import itertools


N = 7
M = 3
PI = (0, 1, 2, 3, 4, 5, 6)
TAU = (0, 2, 5, 1, 3, 6, 4)

WEIGHT = {
    (0, 1, 3): -1,
    (0, 2, 6): -1,
    (1, 2, 4): -1,
    (2, 3, 5): -1,
    (0, 3, 5): +1,
    (0, 3, 6): +1,
    (2, 5, 6): +1,
}


def rows():
    """The (7-1)!/2=360 unoriented cyclic orders, canonically rooted at 0."""
    for tail in itertools.permutations(range(1, N)):
        if tail[0] < tail[-1]:
            yield (0,) + tail


def windows(cycle):
    return frozenset(
        tuple(sorted(cycle[(j + a) % N] for a in range(M)))
        for j in range(N)
    )


def main():
    all_rows = list(rows())
    assert len(all_rows) == 360
    pwin, twin = windows(PI), windows(TAU)
    assert len(pwin) == len(twin) == 7
    assert pwin.isdisjoint(twin)
    forced = pwin | twin
    uncovered = set(itertools.combinations(range(N), M)) - forced
    assert len(uncovered) == 21
    assert set(WEIGHT) <= uncovered
    assert sum(WEIGHT.get(v, 0) for v in uncovered) == -1

    eligible = []
    for cycle in all_rows:
        win = windows(cycle)
        if win.isdisjoint(forced):
            score = sum(WEIGHT.get(v, 0) for v in win)
            assert score >= 0, (cycle, score)
            eligible.append((cycle, score))

    assert len(eligible) == 20
    print("PASS")
    print("forced rows:", PI, TAU)
    print("forced windows are disjoint; uncovered triples: 21")
    print("eligible remaining wreaths:", len(eligible))
    print("total separating weight on uncovered triples: -1")
    print("eligible row scores:")
    for cycle, score in eligible:
        print(" ", "".join(map(str, cycle)), score)


if __name__ == "__main__":
    main()
