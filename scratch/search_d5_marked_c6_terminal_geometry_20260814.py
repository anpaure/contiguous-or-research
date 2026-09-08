#!/usr/bin/env python3
"""Search terminal geometry embeddings for the marked C6 box (H100 only)."""

from itertools import combinations, permutations
import sys

from verify_d5_marked_c6_minimal_resident_reset_20260814 import (
    build,
    palettes,
    resident_port,
    trace_minima,
)


def dj(a, b):
    return len(a - b)


def common_neighbors(b, c, ground):
    d = dj(b, c)
    if d == 1:
        H = b & c
        # Star neighbors have triple intersection |b|-1, as required by
        # the D5 (1,1,1) terminal type.
        for s in sorted(ground - (b | c)):
            yield frozenset(H | {s})
    elif d == 2:
        K = b & c
        left = sorted(b - c)
        right = sorted(c - b)
        for p in left:
            for q in right:
                yield frozenset(K | {p, q})


def find_spectator(tail, ground, router_typed):
    rank = len(tail)
    tried = 0
    for z, s0 in permutations(sorted(tail), 2):
        Kp = frozenset(tail - {z, s0})
        if len(Kp) < 3:
            continue
        outside = sorted(ground - Kp - {z, s0})
        for x1, x2 in combinations(sorted(Kp), 2):
            for s1, y1, y2 in permutations(outside, 3):
                tried += 1
                spec = resident_port(Kp, x1, x2, y1, y2, z, s0, s1)
                if spec[0] != tail:
                    raise AssertionError("tail socket mismatch")
                typed = palettes([spec])
                if any(len(set(typed[k])) != 6 for k in range(3)):
                    continue
                if any(set(typed[k]) & router_typed[k] for k in range(3)):
                    continue
                if trace_minima([spec], ground) != (3, 3, 4, 2):
                    continue
                return spec, (x1, x2, y1, y2, z, s0, s1), tried
    return None, None, tried


def main():
    rank = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    ground, old_router, new_router, _, _, _ = build(rank)
    router_typed_raw = palettes(old_router)
    router_typed = [set(router_typed_raw[k]) for k in range(3)]
    router_owners = router_typed[0]

    solutions = {}
    pair_counts = {1: 0, 2: 0}
    tail_counts = {1: 0, 2: 0}
    for i, j in combinations(range(3), 2):
        for pi, b in enumerate(old_router[i]):
            for pj, c in enumerate(old_router[j]):
                delta = dj(b, c)
                if delta not in (1, 2):
                    continue
                pair_counts[delta] += 1
                for tail in common_neighbors(b, c, ground):
                    tail_counts[delta] += 1
                    if tail in router_owners:
                        continue
                    spec, params, tried = find_spectator(tail, ground, router_typed)
                    if spec is None:
                        continue
                    solutions.setdefault(
                        delta,
                        {
                            "components": (i, j),
                            "phases": (pi, pj),
                            "b": sorted(b),
                            "c": sorted(c),
                            "tail": sorted(tail),
                            "triple_intersection": len(tail & b & c),
                            "union": len(tail | b | c),
                            "spectator_params": params,
                            "spectator_trials": tried,
                        },
                    )
                    break
                if len(solutions) == 2:
                    break
            if len(solutions) == 2:
                break
        if len(solutions) == 2:
            break

    print("MARKED_C6_D5_TERMINAL_GEOMETRY")
    print("rank", rank, "ground", len(ground))
    print("pair counts", pair_counts)
    print("tail candidates visited", tail_counts)
    for delta in (1, 2):
        print("delta", delta, "solution", solutions.get(delta))
    assert set(solutions) == {1, 2}
    assert solutions[1]["triple_intersection"] == rank - 1
    assert solutions[1]["union"] == rank + 2
    assert solutions[2]["triple_intersection"] == rank - 2
    assert solutions[2]["union"] == rank + 2
    print("D5 terminal types (1,1,1) and (1,1,2): PASS")


if __name__ == "__main__":
    main()
