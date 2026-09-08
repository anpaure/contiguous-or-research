#!/usr/bin/env python3
"""Audit the canonical middle-inclusion odd-graph matching."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb


def masks(b: int, r: int) -> list[int]:
    return [sum(1 << q for q in c) for c in combinations(range(b), r)]


def successor(x: int, b: int) -> int:
    stack = []
    paired = set()
    for q in range(b):
        if (x >> q) & 1:
            stack.append(q)
        elif stack:
            p = stack.pop()
            paired.update((p, q))
    free_zero = [q for q in range(b) if not (x >> q) & 1 and q not in paired]
    assert free_zero
    return x | (1 << free_zero[-1])


def cycle_lengths(mapping: dict[int, int]) -> list[int]:
    unseen = set(mapping)
    lengths = []
    while unseen:
        start = next(iter(unseen))
        x = start
        length = 0
        while True:
            assert x in unseen
            unseen.remove(x)
            length += 1
            x = mapping[x]
            if x == start:
                break
        lengths.append(length)
    return lengths


def audit(b: int) -> None:
    r = (b - 1) // 2
    vv = masks(b, r)
    full = (1 << b) - 1
    upper = [successor(x, b) for x in vv]
    assert len(set(upper)) == len(vv)
    assert all(u.bit_count() == r + 1 and (x & u) == x for x, u in zip(vv, upper))
    mapping = {x: full ^ u for x, u in zip(vv, upper)}
    assert set(mapping) == set(mapping.values())
    assert all(not (x & y) for x, y in mapping.items())
    lengths = cycle_lengths(mapping)
    assert sum(lengths) == comb(b, r)
    assert all(length % 2 == 0 or length >= b for length in lengths)
    exposed = sum(length & 1 for length in lengths)
    assert exposed <= len(vv) // b
    print(
        "PASS",
        {
            "b": b,
            "targets": len(vv),
            "cycle_hist": dict(sorted(Counter(lengths).items())),
            "exposed": exposed,
            "bound_floor": len(vv) // b,
        },
        flush=True,
    )


if __name__ == "__main__":
    for bb in range(5, 24, 2):
        audit(bb)
