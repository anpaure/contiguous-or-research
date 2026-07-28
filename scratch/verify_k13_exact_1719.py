#!/usr/bin/env python3
"""Independent verifier for the exact length-1719 k=13 OR word."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from math import comb
from pathlib import Path
import sys


EXPECTED_SHA256 = "8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0"


def derivative(row: list[int]) -> list[int]:
    return [row[i] | row[i + 1] for i in range(len(row) - 1)]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "scratch/k13_two_cycle_one_seam_path_000.word.txt"
    )
    raw = path.read_bytes()
    word = list(map(int, raw.split()))
    k = 13
    full = (1 << k) - 1

    assert len(word) == 1719
    assert all(0 < value <= full for value in word)

    covered = set()
    for left in range(len(word)):
        value = 0
        for right in range(left, len(word)):
            value |= word[right]
            covered.add(value)
            if value == full:
                break
    missing = set(range(1, 1 << k)) - covered
    assert not missing

    rows = [word]
    for _ in range(3):
        rows.append(derivative(rows[-1]))
    middle = rows[-1]
    assert len(middle) == comb(13, 7)
    assert len(set(middle)) == comb(13, 7)
    assert all(value.bit_count() == 7 for value in middle)

    digest = sha256(raw).hexdigest()
    if path.name == "k13_two_cycle_one_seam_path_000.word.txt":
        assert digest == EXPECTED_SHA256

    print(f"PASS {path}")
    print(f"sha256={digest}")
    print(f"length={len(word)} covered={len(covered)} missing={len(missing)}")
    print(f"row_lengths={[len(row) for row in rows]}")
    print(f"row_distinct={[len(set(row)) for row in rows]}")
    print(f"entry_rank_histogram={dict(sorted(Counter(x.bit_count() for x in word).items()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
