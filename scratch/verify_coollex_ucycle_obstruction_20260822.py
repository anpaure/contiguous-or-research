#!/usr/bin/env python3
"""Exact finite checks for the cool-lex / central-ucycle obstruction note.

The general statements in the note have proofs independent of this script.
This file checks the successor count for small m and the literal (7,3)
universal-cycle certificate, including coverage by intervals of arbitrary
cyclic length.
"""

from collections import Counter
from itertools import combinations
from math import comb


def coollex_successor(word: str) -> str:
    n = len(word)
    prefix_length = None
    for length in range(3, n + 1):
        if word[length - 3 : length] in ("010", "011"):
            prefix_length = length
            break
    if prefix_length is None:
        prefix_length = n
    prefix = word[:prefix_length]
    return prefix[-1] + prefix[:-1] + word[prefix_length:]


def coollex_cycle(n: int, weight: int) -> list[str]:
    start = "1" * weight + "0" * (n - weight)
    cycle = []
    seen = set()
    word = start
    while word not in seen:
        seen.add(word)
        cycle.append(word)
        word = coollex_successor(word)
    assert word == start
    return cycle


def verify_coollex_counts() -> None:
    for m in range(1, 10):
        n = 2 * m + 1
        cycle = coollex_cycle(n, m)
        assert len(cycle) == comb(n, m)
        histogram = Counter()
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            hamming = sum(a != b for a, b in zip(left, right))
            assert hamming in (2, 4)
            histogram[hamming // 2] += 1
        bad = 0 if m == 1 else comb(2 * m - 1, m - 1) - 1
        assert histogram[2] == bad
        assert histogram[1] + histogram[2] == comb(n, m)


def cyclic_window(sequence: list[int], start: int, length: int) -> frozenset[int]:
    size = len(sequence)
    return frozenset(sequence[(start + offset) % size] for offset in range(length))


def verify_seven_three_certificate() -> None:
    # Written with zero-based symbols; the note displays the symbols 1,...,7.
    sequence = [
        0, 1, 2, 3, 0, 1, 4, 2, 0, 5, 1, 2, 6, 0, 3, 4, 1, 5,
        6, 2, 4, 3, 5, 0, 4, 6, 3, 2, 5, 4, 6, 1, 3, 5, 6,
    ]
    assert len(sequence) == comb(7, 3) == 35

    triples = {cyclic_window(sequence, start, 3) for start in range(35)}
    assert len(triples) == comb(7, 3)
    assert triples == {frozenset(x) for x in combinations(range(7), 3)}

    pairs = {cyclic_window(sequence, start, 2) for start in range(35)}
    fours = {cyclic_window(sequence, start, 4) for start in range(35)}
    assert pairs == {frozenset(x) for x in combinations(range(7), 2)}
    assert len(fours) == 21

    # Check all cyclic intervals, not merely windows whose length is their rank.
    by_rank = {rank: set() for rank in range(1, 8)}
    for start in range(35):
        union = set()
        for length in range(1, 36):
            union.add(sequence[(start + length - 1) % 35])
            by_rank[len(union)].add(frozenset(union))
            if len(union) == 7:
                break
    assert len(by_rank[3]) == 35
    assert len(by_rank[4]) == 21
    assert by_rank[4] == fours

    missing_fours = {
        frozenset(x) for x in combinations(range(7), 4)
    } - fours
    expected_missing = {
        frozenset(int(c) - 1 for c in token)
        for token in (
            "1246 1247 1256 1257 1345 1346 1357 1367 "
            "2345 2346 2347 2356 2357 4567"
        ).split()
    }
    assert missing_fours == expected_missing


if __name__ == "__main__":
    verify_coollex_counts()
    verify_seven_three_certificate()
    print("COOLLEX_UCYCLE_OBSTRUCTION_VERIFY_PASS")

