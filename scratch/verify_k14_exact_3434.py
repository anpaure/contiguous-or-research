#!/usr/bin/env python3
"""Fail-closed independent verifier for the exact k=14 certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


def derivative(row: list[int]) -> list[int]:
    return [row[i] | row[i + 1] for i in range(len(row) - 1)]


def rank_layer(k: int, rank: int) -> set[int]:
    return {
        sum(1 << bit for bit in choice)
        for choice in combinations(range(k), rank)
    }


def verify(word_path: Path) -> dict:
    raw = word_path.read_bytes()
    word = [int(token) for token in raw.split()]
    k = 14
    full = (1 << k) - 1
    r = 7
    width = comb(k, r)
    lower_ideal = sum(comb(k, rank) for rank in range(1, r))
    depth = 0
    while depth * width + comb(depth + 1, 2) < lower_ideal:
        depth += 1
    lower_bound = width + depth

    assert depth == 2
    assert lower_bound == 3434
    assert len(word) == lower_bound
    assert all(0 < value <= full for value in word)

    covered = set()
    interval_count = 0
    for start in range(len(word)):
        value = 0
        for end in range(start, len(word)):
            value |= word[end]
            covered.add(value)
            interval_count += 1
            if value == full:
                break
    missing = [value for value in range(1, full + 1) if value not in covered]
    assert not missing

    middle = derivative(derivative(word))
    middle_target = rank_layer(k, r)
    assert len(middle) == width
    assert len(set(middle)) == width
    assert set(middle) == middle_target

    rows = [word]
    for _ in range(k - 1):
        rows.append(derivative(rows[-1]))
    report = {
        "status": "VERIFIED_OPTIMAL",
        "k": k,
        "length": len(word),
        "lower_bound_B": lower_bound,
        "lower_bound_depth": depth,
        "lower_ideal_size": lower_ideal,
        "middle_layer_size": width,
        "middle_unique": len(set(middle)),
        "covered_nonempty_masks": len(covered),
        "missing_masks": len(missing),
        "enumerated_intervals_until_full": interval_count,
        "word_sha256": sha256(raw).hexdigest(),
        "entry_rank_histogram": dict(sorted(Counter(map(int.bit_count, word)).items())),
        "derivative_rank_histograms": [
            dict(sorted(Counter(map(int.bit_count, row)).items())) for row in rows[:4]
        ],
        "word": str(word_path),
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        type=Path,
        nargs="?",
        default=Path("scratch/k14_intersection_sixpiece_hallpass_004a.word"),
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.word)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
