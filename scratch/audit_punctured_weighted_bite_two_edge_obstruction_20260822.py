#!/usr/bin/env python3
"""Regression checks for the two-edge punctured weighted-bite obstruction."""

from itertools import combinations, permutations
from fractions import Fraction


def edge(word, r):
    b = 2 * r + 1
    return frozenset(
        (shore, frozenset(word[(s + i) % b] for i in range(length)))
        for shore, length in (("M", r), ("L", r - 1))
        for s in range(1, b)
    )


def containment_path(targets):
    middle = [x for x in targets if x[0] == "M"]
    lower = [x for x in targets if x[0] == "L"]
    adjacency = {x: [] for x in targets}
    for low in lower:
        for mid in middle:
            if low[1] < mid[1]:
                adjacency[low].append(mid)
                adjacency[mid].append(low)
    endpoints = [x for x in targets if len(adjacency[x]) == 1]
    if len(endpoints) != 2 or any(len(adjacency[x]) not in (1, 2) for x in targets):
        return False
    seen = set()
    stack = [endpoints[0]]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adjacency[x])
    return len(seen) == len(targets)


def check_symbolic(r):
    b = 2 * r + 1
    word = tuple(range(b))
    swapped = tuple(range(b - 2)) + (b - 1, b - 2)
    first = edge(word, r)
    second = edge(swapped, r)
    union = first | second

    assert len(first) == len(second) == 4 * r
    assert len(first & second) == 4 * r - 4
    assert len(union) == 4 * r + 4
    for shore in ("M", "L"):
        assert sum(x[0] == shore for x in first & second) == 2 * r - 2
        assert sum(x[0] == shore for x in first - second) == 2
        assert sum(x[0] == shore for x in second - first) == 2

    middle = [x for x in union if x[0] == "M"]
    lower = [x for x in union if x[0] == "L"]
    path_subsets = []
    for omitted_middle in combinations(middle, 2):
        kept_middle = set(middle) - set(omitted_middle)
        for omitted_lower in combinations(lower, 2):
            candidate = kept_middle | (set(lower) - set(omitted_lower))
            if containment_path(candidate):
                path_subsets.append(frozenset(candidate))
    assert len(set(path_subsets)) == 4
    assert first in path_subsets and second in path_subsets

    common = first & second
    private = union - common
    y_sum = len(common) - (r - 1) * len(private)
    assert y_sum == -4 * (r - 1)
    for configuration in (first, second):
        edge_sum = len(configuration & common) - (r - 1) * len(configuration & private)
        assert edge_sum == 0


def check_exhaustive_small(r):
    b = 2 * r + 1
    word = tuple(range(b))
    swapped = tuple(range(b - 2)) + (b - 1, b - 2)
    union = edge(word, r) | edge(swapped, r)
    contained = {u for u in permutations(range(b)) if edge(u, r) <= union}
    assert contained == {word, swapped}


def check_boundary_expansion_and_erosion():
    """Check (3.2), the Farkas sign, and the literal two-edge drifts."""
    r = 3
    b = 2 * r + 1
    word = tuple(range(b))
    swapped = tuple(range(b - 2)) + (b - 1, b - 2)
    configs = (edge(word, r), edge(swapped, r))
    union = configs[0] | configs[1]

    def degree(target_set):
        return sum(target_set <= configuration for configuration in configs)

    for v in union:
        dv = degree(frozenset((v,)))
        for g in configs:
            direct = sum(max(len(f & g) - 1, 0)
                         for f in configs if v in f)
            expanded = 0
            glist = tuple(g)
            for size in range(2, len(glist) + 1):
                sign = -1 if size % 2 else 1
                for subset in combinations(glist, size):
                    expanded += sign * degree(frozenset(subset) | {v})
            assert direct == expanded
            assert Fraction(direct, dv) >= 0

    common = configs[0] & configs[1]
    private = union - common
    y = {v: (1 if v in common else -(r - 1)) for v in union}
    assert all(sum(y[v] for v in g) == 0 for g in configs)
    assert sum(y.values()) == -4 * (r - 1) < 0

    rates = (2, 3)
    loads = {v: sum(rate for rate, g in zip(rates, configs) if v in g)
             for v in union}
    hazards = {
        f: sum(rate for rate, g in zip(rates, configs) if f & g)
        for f in configs
    }
    erosion = {}
    for v in union:
        incident = [f for f in configs if v in f]
        erosion[v] = Fraction(sum(hazards[f] for f in incident), len(incident)) - loads[v]
    assert all(erosion[v] == 0 for v in common)
    assert all(erosion[v] == rates[1] for v in configs[0] - configs[1])
    assert all(erosion[v] == rates[0] for v in configs[1] - configs[0])


def main():
    # The union graph has the same branch-and-tail form for every r.  Checking
    # several values catches all local and path-segment cases without making
    # the O(r^4) path-subset regression needlessly slow.
    for r in range(3, 11):
        check_symbolic(r)
    # r=4 checks all 9! directed words, not just abstract containment paths.
    for r in (3, 4):
        check_exhaustive_small(r)
    check_boundary_expansion_and_erosion()
    print("PASS: punctured weighted-bite LP two-edge obstruction")


if __name__ == "__main__":
    main()
