#!/usr/bin/env python3
"""Verify the q=3 cyclic near-C factor and its one-rail deletion obstruction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


M = 11
Q = 3
H = frozenset({0, 1, 2, 3})

BASE_CYCLES = (
    (1, 2, 3, 4, 6, 9, 5, 10, 7, 8),
    (1, 5, 9, 2, 4, 8, 7, 6, 3, 10),
    (1, 6, 9, 3, 8, 10, 2, 4, 5, 7),
)


def translate(cycle: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple((x + shift) % M for x in cycle)


def deck(centre: int, cycle: tuple[int, ...]) -> tuple[frozenset[int], ...]:
    n = len(cycle)
    assert centre not in cycle
    assert len(set(cycle)) == n
    return tuple(
        frozenset({centre, cycle[i], cycle[(i + 1) % n], cycle[(i + 2) % n]})
        for i in range(n)
    )


def candidate_rails_inside(target: set[frozenset[int]]):
    ans = []
    for centre in range(M):
        available = [x for x in range(M) if x != centre]
        allowed = {owner - {centre} for owner in target if centre in owner}
        for period in (8, 9, 10):
            for support in combinations(available, period):
                root = min(support)
                tail = [x for x in support if x != root]
                for perm in permutations(tail):
                    cycle = (root,) + perm
                    if cycle[1] > cycle[-1]:
                        continue
                    rail_deck = set(deck(centre, cycle))
                    if rail_deck <= target:
                        ans.append((centre, cycle, rail_deck))
    return ans


def main() -> None:
    rails = []
    for shift in range(M):
        for base in BASE_CYCLES:
            cycle = translate(base, shift)
            rails.append((shift, cycle, deck(shift, cycle)))

    owners = Counter(owner for _, _, values in rails for owner in values)
    all_owners = set(map(frozenset, combinations(range(M), Q + 1)))
    assert len(rails) == 33
    assert sum(owners.values()) == 330
    assert set(owners) == all_owners
    assert set(owners.values()) == {1}

    h_occurrences = [i for i, (_, _, values) in enumerate(rails) if H in values]
    assert h_occurrences == [0]
    punctured = set(rails[0][2]) - {H}
    assert len(punctured) == 9

    candidates = candidate_rails_inside(punctured)
    assert candidates == []

    print("PASS q=3 cyclic bridge factor")
    print("rails:", len(rails), "owners:", len(owners), "multiplicities:", set(owners.values()))
    print("H occurs in rail indices:", h_occurrences)
    print("punctured rail owner count:", len(punctured))
    print("legal period-8/9/10 rails inside punctured deck:", len(candidates))


if __name__ == "__main__":
    main()
