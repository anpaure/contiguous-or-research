#!/usr/bin/env python3
"""Print the high-overlap words relative to the identity configuration."""

from __future__ import annotations

import argparse
import itertools


def edge(word: tuple[int, ...], r: int) -> frozenset[tuple[int, frozenset[int]]]:
    b = 2 * r + 1
    return frozenset(
        (layer, frozenset(word[(start + offset) % b] for offset in range(length)))
        for layer, length in ((0, r), (1, r - 1))
        for start in range(1, b)
    )


def main(r: int, defect: int) -> None:
    b = 2 * r + 1
    identity = tuple(range(b))
    base = edge(identity, r)
    threshold = 4 * r - defect
    rows = []
    for word in itertools.permutations(range(b)):
        overlap = len(base & edge(word, r))
        if overlap >= threshold:
            rows.append((4 * r - overlap, word))
    rows.sort()
    for row in rows:
        print(row)
    print({"r": r, "threshold": threshold, "count": len(rows)})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=4)
    parser.add_argument("--defect", type=int, default=3)
    arguments = parser.parse_args()
    main(arguments.r, arguments.defect)
