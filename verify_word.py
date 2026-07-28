#!/usr/bin/env python3
"""Minimal independent verifier for an optimal contiguous-OR word."""

from __future__ import annotations

from collections import Counter
from math import comb
from pathlib import Path
import argparse


def derivative(row: list[int]) -> list[int]:
    return [a | b for a, b in zip(row, row[1:])]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("word", type=Path)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument(
        "--allow-nonoptimal",
        action="store_true",
        help="verify universal coverage without requiring length B(k)",
    )
    args = parser.parse_args()

    k = args.k
    full = (1 << k) - 1
    word = list(map(int, args.word.read_text().split()))
    assert all(0 < value <= full for value in word)

    covered = bytearray(1 << k)
    for left in range(len(word)):
        value = 0
        for right in range(left, len(word)):
            value |= word[right]
            covered[value] = 1
            if value == full:
                break
    missing = [value for value in range(1, 1 << k) if not covered[value]]
    assert not missing

    rank = (k + 1) // 2
    width = comb(k, rank)
    delay = len(word) - width
    assert delay >= 0
    rows = [word]
    for _ in range(delay):
        rows.append(derivative(rows[-1]))
    middle = set(value for value in range(1 << k) if value.bit_count() == rank)
    rank_exact = len(rows[delay]) == width and set(rows[delay]) == middle

    lower_mass = sum(comb(k, layer) for layer in range(1, rank))
    minimum_delay = 0
    while minimum_delay * width + comb(minimum_delay + 1, 2) < lower_mass:
        minimum_delay += 1
    if not args.allow_nonoptimal:
        assert delay == minimum_delay

    print(f"PASS k={k} length={len(word)} covered={full}/{full}")
    for depth, row in enumerate(rows):
        print(
            f"D^{depth}: length={len(row)} unique={len(set(row))} "
            f"ranks={dict(sorted(Counter(x.bit_count() for x in row).items()))}"
        )
    print(
        f"central rank={rank} exact={rank_exact}; counting lower bound: "
        f"d={minimum_delay}, B({k})={width}+{minimum_delay}={width+minimum_delay}"
    )


if __name__ == "__main__":
    main()
