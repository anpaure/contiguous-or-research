#!/usr/bin/env python3
"""Enumerate small wreath t-codegrees; execute only on H100."""

from collections import defaultdict
from itertools import combinations, permutations
from math import factorial


def enumerate_profile(b: int, r: int, t: int) -> None:
    counts: dict[tuple[int, ...], int] = defaultdict(int)
    examples: dict[tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        windows = []
        for i in range(b):
            mask = 0
            for j in range(r):
                mask |= 1 << order[(i + j) % b]
            windows.append(mask)
        for indices in combinations(range(b), t):
            key = tuple(sorted(windows[i] for i in indices))
            counts[key] += 1
            examples.setdefault(key, (order, indices))
    maximum = max(counts.values())
    keys = [key for key, value in counts.items() if value == maximum]
    d = t - 1
    predicted = (
        2 * factorial(r - d) * factorial(b - r - d)
        if d <= min(r, b - r)
        else None
    )
    key = keys[0]
    order, indices = examples[key]
    distances = [
        (key[i] ^ key[j]).bit_count() // 2
        for i in range(t)
        for j in range(i + 1, t)
    ]
    print(
        "ENUM",
        b,
        r,
        t,
        "families",
        len(counts),
        "max",
        maximum,
        "pred",
        predicted,
        "nummax",
        len(keys),
        "dist",
        distances,
        "order",
        order,
        "indices",
        indices,
    )


def main() -> None:
    for b in range(6, 10):
        for r in range(2, b // 2 + 1):
            if b - 2 * r in (0, 1):
                continue
            for t in range(2, min(5, r + 2)):
                enumerate_profile(b, r, t)


if __name__ == "__main__":
    main()
