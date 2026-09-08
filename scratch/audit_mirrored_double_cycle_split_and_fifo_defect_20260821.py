#!/usr/bin/env python3
"""H100 audit for the mirrored double-cycle split/FIFO-defect theorem."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product

from research_mirrored_double_cycle_recut_20260821 import (
    induced_two_wreath_factors,
    lift_johnson_path,
    paired_cycles,
)


def swaps(path):
    answer = []
    for left, right in zip(path, path[1:]):
        deleted = tuple(left - right)
        added = tuple(right - left)
        assert len(deleted) == len(added) == 1
        answer.append((deleted[0], added[0]))
    return tuple(answer)


def doubled(path, r):
    ground = frozenset(range(1, 2 * r + 1))
    reverse_complement = tuple(ground - target for target in reversed(path))
    return lift_johnson_path(path, r) + lift_johnson_path(reverse_complement, r)


def edge_holes(cycle, r):
    full = frozenset(range(1, 2 * r + 2))
    holes = []
    for index, left in enumerate(cycle):
        right = cycle[(index + 1) % len(cycle)]
        gap = full - left - right
        assert len(gap) == 1
        holes.append(next(iter(gap)))
    return tuple(holes)


def check_clean_blocks(path, r):
    exchange = swaps(path)
    multiplicity = Counter(x for deleted, added in exchange for x in (added, deleted))
    repeated = {x for x, value in multiplicity.items() if value >= 2}
    delta = sum(max(0, value - 1) for value in multiplicity.values())
    bad = {
        index
        for index, (deleted, added) in enumerate(exchange, start=1)
        if deleted in repeated or added in repeated
    }
    assert len(bad) <= 2 * delta
    blocks = []
    start = 0
    for transition in range(1, r + 1):
        if transition in bad:
            blocks.append((start, transition - 1))
            start = transition
    blocks.append((start, r))
    assert len(blocks) <= 2 * delta + 1
    for lo, hi in blocks:
        block_swaps = exchange[lo:hi]
        labels = [x for pair in block_swaps for x in pair]
        assert len(labels) == len(set(labels))
        deleted = [pair[0] for pair in block_swaps]
        added = [pair[1] for pair in block_swaps]
        core = sorted(path[lo] - set(deleted))
        word = deleted + core + added
        assert len(word) == r + hi - lo
        assert len(word) == len(set(word))
        windows = [frozenset(word[j : j + r]) for j in range(hi - lo + 1)]
        assert windows == list(path[lo : hi + 1])
    return delta, len(blocks), len(bad)


def audit_path(path, r):
    ground = frozenset(range(1, 2 * r + 1))
    anchor = 2 * r + 1
    exchange = swaps(path)
    s = Counter(x for deleted, added in exchange for x in (added, deleted))
    delta = sum(max(0, value - 1) for value in s.values())
    assert delta == sum(x not in s for x in ground)
    cycle = doubled(path, r)

    expected = tuple(
        x for deleted, added in exchange for x in (added, deleted)
    )
    expected = expected + (anchor,) + tuple(
        x for deleted, added in reversed(exchange) for x in (added, deleted)
    ) + (anchor,)
    assert edge_holes(cycle, r) == expected

    if len(set(cycle)) == len(cycle):
        degree = Counter(x for target in cycle for x in target)
        assert degree[anchor] == 2 * r
        for x in ground:
            assert degree[x] == 2 * r + 1 - s[x]
        # Two wreath rows would have point degree 2r.  Simplicity therefore
        # forces failure of the necessary margin condition.
        assert any(degree[x] != 2 * r for x in ground)

    P = path[0]
    Q = ground - path[-1]
    distance = len(P - Q)
    even = {x for x in ground if s[x] % 2 == 0}
    assert P ^ Q == even
    assert distance <= delta
    clean_delta, block_count, bad_count = check_clean_blocks(path, r)
    assert clean_delta == delta
    return len(set(cycle)) == len(cycle), delta, distance, block_count, bad_count


def exhaustive_paths(r):
    ground = frozenset(range(1, 2 * r + 1))
    root = frozenset(range(1, r + 1))
    stack = [(root, (root,))]
    while stack:
        current, path = stack.pop()
        if len(path) == r + 1:
            yield path
            continue
        for deleted, added in product(sorted(current), sorted(ground - current)):
            nxt = frozenset((current - {deleted}) | {added})
            stack.append((nxt, path + (nxt,)))


def audit_adjacent_converse(r):
    ground = frozenset(range(1, 2 * r + 1))
    sets = [frozenset(x) for x in combinations(ground, r)]
    checked = 0
    for P_index, P in enumerate(sets):
        for Q in sets[P_index + 1 :]:
            if len(P ^ Q) != 2:
                continue
            checked += 1
            u = next(iter(P - Q))
            v = next(iter(Q - P))
            S = sorted(P & Q)
            R = sorted(ground - (P | Q))
            assert len(S) == len(R) == r - 1
            current = P
            path = [current]
            steps = [(S[0], v), (v, R[0])] + list(zip(S[1:], R[1:]))
            assert len(steps) == r
            for deleted, added in steps:
                assert deleted in current and added not in current
                current = frozenset((current - {deleted}) | {added})
                path.append(current)
            assert current == ground - Q
            _, delta, distance, _, _ = audit_path(tuple(path), r)
            assert delta == distance == 1
    return {"r": r, "adjacent_pairs": checked}


def audit_exhaustive(r):
    count = 0
    simple = 0
    defect_hist = Counter()
    distance_hist = Counter()
    for path in exhaustive_paths(r):
        count += 1
        is_simple, delta, distance, _, _ = audit_path(path, r)
        simple += is_simple
        defect_hist[delta] += 1
        distance_hist[distance] += 1
    assert count == (r * r) ** r
    return {
        "r": r,
        "paths": count,
        "simple_doubles": simple,
        "defect_hist": dict(defect_hist),
        "endpoint_distance_hist": dict(distance_hist),
    }


def audit_canonical(r):
    pairs = paired_cycles(r)
    simple = 0
    defect_hist = Counter()
    chord_hist = Counter()
    for _, _, cycle in pairs:
        first_lift = cycle[: 2 * r + 1]
        path = tuple(first_lift[2 * t] for t in range(r + 1))
        is_simple, delta, distance, _, _ = audit_path(path, r)
        assert is_simple == (len(set(cycle)) == len(cycle))
        if not is_simple:
            continue
        simple += 1
        defect_hist[delta] += 1
        factors, chords = induced_two_wreath_factors(cycle, r)
        assert not factors
        chord_hist[chords] += 1
    expected = {
        4: (7, 4, {1: 3, 2: 1}),
        6: (66, 47, {1: 16, 2: 26, 3: 5}),
        8: (715, 546, {1: 115, 2: 235, 3: 166, 4: 30}),
    }
    assert (len(pairs), simple, dict(defect_hist)) == expected[r]
    return {
        "r": r,
        "pairs": len(pairs),
        "simple": simple,
        "simple_defect_hist": dict(defect_hist),
        "induced_chord_hist": dict(chord_hist),
        "two_wreath_factors": 0,
    }


def main():
    exhaustive = [audit_exhaustive(r) for r in (2, 3, 4)]
    adjacent_converse = [audit_adjacent_converse(r) for r in (2, 3, 4, 5)]
    canonical = [audit_canonical(r) for r in (4, 6, 8)]
    print(
        "MIRRORED_DOUBLE_CYCLE_SPLIT_AND_FIFO_DEFECT_AUDIT_PASS",
        {
            "exhaustive": exhaustive,
            "adjacent_converse": adjacent_converse,
            "canonical": canonical,
        },
    )


if __name__ == "__main__":
    main()
