#!/usr/bin/env python3
"""Exact small-b audit of FIFO cycles induced by the first GK addition.

All labels are positions 0,...,2b-1 in the alternating A,B order.  A queue
q=(y_{t-b+1},...,y_t) represents its rank-b source set.  Its forced next
letter is the rightmost unmatched zero in standard Greene--Kleitman
bracketing.  The FIFO transition drops q[0] and appends that letter.

For every directed cycle, also measure the largest h for which each edge
S -> S' satisfies a_j(S')=a_{j+1}(S), 0<=j<h.  Thus h>=H-1 is the exact
length-H prefix-shift compatibility requested by the direct-successor route.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter


def gk_additions(source: frozenset[int], n: int) -> tuple[int, ...]:
    stack: list[int] = []
    unmatched_zeros: list[int] = []
    for i in range(n):
        if i in source:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            unmatched_zeros.append(i)
    return tuple(reversed(unmatched_zeros))


def first_global_minimum(source: frozenset[int], n: int) -> int | None:
    height = 0
    minimum = 0
    first: int | None = None
    for i in range(n):
        height += 1 if i in source else -1
        if height < minimum:
            minimum = height
            first = i
    return first


def next_queue(q: tuple[int, ...], n: int) -> tuple[int, ...] | None:
    additions = gk_additions(frozenset(q), n)
    if not additions:
        return None
    a1 = additions[0]
    assert a1 not in q
    return q[1:] + (a1,)


def edge_compatibility(q: tuple[int, ...], q2: tuple[int, ...], n: int) -> int:
    a = gk_additions(frozenset(q), n)
    ap = gk_additions(frozenset(q2), n)
    h = 0
    while h + 1 < len(a) and h < len(ap) and ap[h] == a[h + 1]:
        h += 1
    return h


def audit_b(b: int) -> dict[str, object]:
    n = 2 * b
    for source_tuple in itertools.combinations(range(n), b):
        source = frozenset(source_tuple)
        additions = gk_additions(source, n)
        first = first_global_minimum(source, n)
        assert (additions[0] if additions else None) == first
        if first is not None:
            assert first < max(source)

    states = list(itertools.permutations(range(n), b))
    state_set = set(states)
    nxt: dict[tuple[int, ...], tuple[int, ...] | None] = {}
    for q in states:
        q2 = next_queue(q, n)
        assert q2 is None or q2 in state_set
        if q2 is not None:
            assert max(q2) <= max(q)
        nxt[q] = q2

    # Check the strict b-step maximum descent and the b^2 stopping bound
    # from the analytic proof, independently from the cycle census below.
    for start in states:
        q: tuple[int, ...] | None = start
        for block in range(b):
            if q is None:
                break
            old_max = max(q)
            for _ in range(b):
                q = nxt[q]
                if q is None:
                    break
            if q is None:
                break
            assert max(q) < old_max, (b, start, block, old_max, max(q))
        if q is not None:
            assert nxt[q] is None, (b, start, q)

    colour: dict[tuple[int, ...], int] = {}
    cycles: list[list[tuple[int, ...]]] = []
    for start in states:
        if start in colour:
            continue
        path: list[tuple[int, ...]] = []
        where: dict[tuple[int, ...], int] = {}
        q: tuple[int, ...] | None = start
        while q is not None and q not in colour and q not in where:
            where[q] = len(path)
            path.append(q)
            q = nxt[q]
        if q is not None and q in where:
            cycles.append(path[where[q] :])
        for v in path:
            colour[v] = 2

    cycle_lengths = Counter(len(c) for c in cycles)
    min_edge_depths = Counter()
    projected_unique = Counter()
    top_excess_ranges = Counter()
    examples: list[dict[str, object]] = []
    for cyc in cycles:
        depths = [
            edge_compatibility(cyc[i], cyc[(i + 1) % len(cyc)], n)
            for i in range(len(cyc))
        ]
        sources = [frozenset(q) for q in cyc]
        ks = [len(gk_additions(s, n)) for s in sources]
        min_edge_depths[min(depths)] += 1
        projected_unique[len(set(sources))] += 1
        top_excess_ranges[(min(ks), max(ks))] += 1
        if len(examples) < 8:
            examples.append(
                {
                    "length": len(cyc),
                    "distinct_sources": len(set(sources)),
                    "min_edge_depth": min(depths),
                    "top_excess": ks,
                    "queues": cyc,
                }
            )

    return {
        "b": b,
        "states": len(states),
        "defined": sum(v is not None for v in nxt.values()),
        "cycles": len(cycles),
        "cycle_lengths": dict(sorted(cycle_lengths.items())),
        "min_edge_depths": dict(sorted(min_edge_depths.items())),
        "projected_unique": dict(sorted(projected_unique.items())),
        "top_excess_ranges": {str(k): v for k, v in sorted(top_excess_ranges.items())},
        "examples": examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=6)
    args = parser.parse_args()
    for b in range(1, args.max_b + 1):
        row = audit_b(b)
        assert row["cycles"] == 0
        print(
            "b={b} states={states} defined={defined} cycles={cycles} PASS".format(
                **row
            )
        )
    print("AUDIT GK FIFO SUCCESSOR: PASS")


if __name__ == "__main__":
    main()
