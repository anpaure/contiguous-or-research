#!/usr/bin/env python3
"""Independent verifier for an OR-universal word at the B(k) lower bound."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


def derivative(row: list[int]) -> list[int]:
    return [a | b for a, b in zip(row, row[1:])]


def rank_layer(k: int, rank: int) -> set[int]:
    return {
        sum(1 << bit for bit in choice)
        for choice in combinations(range(k), rank)
    }


def verify(
    path: Path,
    k: int,
    require_middle_row: bool,
    allow_longer: bool = False,
) -> dict:
    raw = path.read_bytes()
    word = [int(token) for token in raw.split()]
    full = (1 << k) - 1
    rank = (k + 1) // 2
    width = comb(k, rank)
    lower_ideal = sum(comb(k, j) for j in range(1, rank))
    depth = 0
    while depth * width + comb(depth + 1, 2) < lower_ideal:
        depth += 1
    lower_bound = width + depth

    if allow_longer:
        if len(word) < lower_bound:
            raise ValueError("word is shorter than the proved lower bound")
    else:
        if len(word) != lower_bound:
            raise ValueError("word length is not the exact lower bound")
    if not all(0 < value <= full for value in word):
        raise ValueError("word contains an empty or out-of-range mask")

    covered = set()
    enumerated = 0
    for start in range(len(word)):
        value = 0
        for entry in word[start:]:
            value |= entry
            covered.add(value)
            enumerated += 1
            if value == full:
                break
    if len(covered) != full:
        raise ValueError("word does not cover every nonempty mask")

    middle = word
    rows = [word]
    for _ in range(depth):
        middle = derivative(middle)
        rows.append(middle)
    middle_exact = (
        len(middle) == width
        and len(set(middle)) == width
        and set(middle) == rank_layer(k, rank)
    )
    if require_middle_row:
        if not middle_exact:
            raise ValueError("declared middle derivative row is not exact")

    return {
        "status": (
            "VERIFIED_OPTIMAL" if len(word) == lower_bound
            else "VERIFIED_UNIVERSAL_UPPER_BOUND"
        ),
        "k": k,
        "length": len(word),
        "lower_bound_B": lower_bound,
        "lower_bound_depth": depth,
        "middle_rank": rank,
        "middle_width": width,
        "middle_row_exact": middle_exact,
        "covered_nonempty_masks": len(covered),
        "missing_masks": full - len(covered),
        "enumerated_intervals_until_full": enumerated,
        "word_sha256": sha256(raw).hexdigest(),
        "row_rank_histograms": [
            dict(sorted(Counter(map(int.bit_count, row)).items()))
            for row in rows
        ],
        "word": str(path),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("word", type=Path)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--require-middle-row", action="store_true")
    parser.add_argument("--allow-longer", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(
        args.word,
        args.k,
        args.require_middle_row,
        args.allow_longer,
    )
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
