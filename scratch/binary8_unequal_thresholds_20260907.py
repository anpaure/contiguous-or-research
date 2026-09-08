"""Exact, constructive unequal-threshold test. Run only via ssh h100.

The matching partitions each actual staircase into ascending grid paths;
it is not a fractional cover or an inference from the rank polynomial.
"""

import argparse
from itertools import product
import json
from math import prod
from pathlib import Path
import time

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


ROWS = [
    ("0461", "5723"), ("0473", "2651"), ("0674", "3152"),
    ("0726", "1435"), ("1507", "4263"), ("1605", "7432"),
    ("2104", "6375"), ("2150", "7463"), ("3206", "7154"),
    ("3210", "4567"), ("3617", "5204"), ("4302", "6157"),
    ("5034", "6721"), ("5426", "7301"),
]
ROWS = [(tuple(map(int, left)), tuple(map(int, right))) for left, right in ROWS]


def allowed(point, cuts):
    bits = [x >= c for x, c in zip(point, cuts)]
    return all(a >= b for a, b in zip(bits, bits[1:]))


def staircase_paths(q, cuts, allow_jumps=False):
    points = [point for point in product(range(q), repeat=4) if allowed(point, cuts)]
    index = {point: i for i, point in enumerate(points)}
    left, right = [], []
    for i, point in enumerate(points):
        if allow_jumps:
            neighbors = (nxt for nxt in product(*(range(v, q) for v in point))
                         if nxt != point)
        else:
            neighbors = (tuple(v + (axis == k) for k, v in enumerate(point))
                         for axis in range(4) if point[axis] + 1 < q)
        for nxt in neighbors:
            j = index.get(nxt)
            if j is not None:
                left.append(i)
                right.append(j)
    graph = csr_matrix((np.ones(len(left), dtype=np.int8), (left, right)),
                       shape=(len(points), len(points)))
    successor = maximum_bipartite_matching(graph, perm_type="column")
    incoming = {int(j) for j in successor if j >= 0}
    assert len(incoming) == sum(j >= 0 for j in successor)
    # An equal-size vertex cover independently certifies maximum cardinality.
    adjacency = [[] for _ in points]
    for i, j in zip(left, right):
        adjacency[i].append(j)
    predecessor = {int(j): i for i, j in enumerate(successor) if j >= 0}
    reachable_left = {i for i, j in enumerate(successor) if j < 0}
    reachable_right = set()
    pending = list(reachable_left)
    while pending:
        i = pending.pop()
        for j in adjacency[i]:
            if int(successor[i]) == j or j in reachable_right:
                continue
            reachable_right.add(j)
            mate = predecessor.get(j)
            if mate is not None and mate not in reachable_left:
                reachable_left.add(mate)
                pending.append(mate)
    cover_left = set(range(len(points))) - reachable_left
    assert len(cover_left) + len(reachable_right) == len(incoming)
    assert all(i in cover_left or j in reachable_right for i, j in zip(left, right))
    paths, seen = [], set()
    for start in range(len(points)):
        if start in incoming:
            continue
        path, current = [], start
        while current >= 0:
            assert current not in seen
            seen.add(current)
            path.append(points[current])
            nxt = int(successor[current])
            if nxt >= 0:
                delta = [b - a for a, b in zip(points[current], points[nxt])]
                assert min(delta) >= 0 and sum(delta) >= 1
                if not allow_jumps:
                    assert sum(delta) == 1
            current = nxt
        paths.append(path)
    assert len(seen) == len(points)
    assert len(paths) == len(points) - len(incoming)
    return paths


def exact_cube_check(q, cuts, selected):
    seen = bytearray(q ** 8)
    for (left, right), (left_paths, right_paths) in zip(ROWS, selected):
        left_points = [x for chain in left_paths for x in chain]
        right_points = [x for chain in right_paths for x in chain]
        assert len(left_points) == len(set(left_points))
        assert len(right_points) == len(set(right_points))
        for x in left_points:
            for y in right_points:
                point = [0] * 8
                for axis, value in zip(left, x):
                    point[axis] = value
                for axis, value in zip(right, y):
                    point[axis] = value
                code = sum(value * q ** axis for axis, value in enumerate(point))
                seen[code] = 1
    assert all(seen)
    return len(seen)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--all-comparabilities", action="store_true")
    args = parser.parse_args()
    q = args.q
    assert 2 <= q <= 8
    started = time.monotonic()
    # Independently verify the finite binary template before any lifting.
    assert all(any(allowed(tuple(bits[i] for i in left), (1,) * 4)
                       and allowed(tuple(bits[i] for i in right), (1,) * 4)
                       for left, right in ROWS)
               for bits in product(range(2), repeat=8))
    cache = {}
    for cuts in product(range(1, q), repeat=4):
        paths = staircase_paths(q, cuts, args.all_comparabilities)
        volume = sum(map(len, paths))
        expected = sum(prod(q - cuts[i] if i < j else cuts[i] for i in range(4))
                       for j in range(5))
        assert volume == expected
        cache[cuts] = (volume, len(paths), paths)
    print("SHORES", len(cache), "q", q, flush=True)
    best = None
    best_cuts = None
    number = 0
    minimizers = 0
    for cuts in product(range(1, q), repeat=8):
        cost = 0
        for left, right in ROWS:
            lv, lw, _ = cache[tuple(cuts[i] for i in left)]
            rv, rw, _ = cache[tuple(cuts[i] for i in right)]
            cost += lv * rw + rv * lw
        number += 1
        if best is None or cost < best:
            best, best_cuts, minimizers = cost, cuts, 1
        elif cost == best:
            minimizers += 1
    selected = [(cache[tuple(best_cuts[i] for i in left)][2],
                 cache[tuple(best_cuts[i] for i in right)][2]) for left, right in ROWS]
    assert best == sum(sum(map(len, left)) * len(right)
                       + sum(map(len, right)) * len(left) for left, right in selected)
    improvement = 32 * best < 35 * q ** 7
    report = {"q": q, "cut_vectors": number, "best_cost": int(best),
              "shore_partition_model": ("all_strict_chains" if args.all_comparabilities
                                        else "unit_step_paths"),
              "best_cuts": best_cuts, "minimizers": minimizers,
              "normalized_cost": best / q ** 7,
              "strictly_beats_35_over_32": improvement,
              "elapsed_seconds": time.monotonic() - started}
    if args.verify or improvement:
        report["verified_grid_points"] = exact_cube_check(q, best_cuts, selected)
    if args.output:
        certificate = {"report": report, "rows": ROWS, "paths": selected}
        args.output.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    print(json.dumps(report, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
