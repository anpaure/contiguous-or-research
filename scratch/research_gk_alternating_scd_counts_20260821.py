#!/usr/bin/env python3
"""Enumerate Greene--Kleitman middle chains in the interleaved A/B order."""

from collections import Counter
from itertools import combinations
from math import comb
from fractions import Fraction


def chain_data(n: int, ones: tuple[int, ...]) -> tuple[int, int]:
    """Return (top excess, parity of the next unpaired zero), positions 0-based."""
    bits = [0] * n
    for i in ones:
        bits[i] = 1
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit == 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[j] = matched[i] = True
    unpaired = [i for i in range(n) if not matched[i]]
    k = len(unpaired) // 2
    assert all(bits[i] == 0 for i in unpaired[:k])
    assert all(bits[i] == 1 for i in unpaired[k:])
    orient = unpaired[k - 1] % 2 if k else -1  # 0=A, 1=B
    return k, orient


def formula_count(b: int, r: int, k: int) -> Fraction:
    """Candidate formula for chains of source split r and top excess k."""
    if k == b:
        return Fraction(int(r == b // 2))
    aa = r - k // 2
    bb = b - r - (k + 1) // 2
    num = (k + 1) * comb(b, aa - 1) * comb(b, bb) if 0 <= aa - 1 <= b and 0 <= bb <= b else 0
    num += k * comb(b + 1, aa) * comb(b - 1, bb - 1) if 0 <= aa <= b + 1 and 0 <= bb - 1 <= b - 1 else 0
    return Fraction(num, b - k)


def main() -> None:
    checks = 0
    for b in range(1, 11):
        counts: Counter[tuple[int, int, int]] = Counter()
        for ones in combinations(range(2 * b), b):
            r = sum(i % 2 == 0 for i in ones)
            k, orient = chain_data(2 * b, ones)
            counts[r, k, orient] += 1
        print("B", b, "TOTAL", sum(counts.values()))
        if b <= 3:
            print("COUNTS", sorted(counts.items()))
            print("FORMULA", [(r, k, formula_count(b, r, k)) for r in range(b + 1) for k in range(1, b)])
        for r in range(b + 1):
            for k in range(1, b):
                expected_orient = 0 if k % 2 else 1
                got = counts[r, k, expected_orient]
                assert counts[r, k, 1 - expected_orient] == 0
                want = formula_count(b, r, k)
                if got != want:
                    print("MISMATCH", b, r, k, got, want, "B", counts[r, k, 1])
                    raise AssertionError
                checks += 1
    print("PASS", checks)

    smooth_checks = 0
    for b in (31, 61, 101, 201, 401, 801):
        for r in range((15 * b) // 32, (17 * b) // 32 + 1):
            seq = [formula_count(b, r, k) for k in range(b + 1)]
            assert all(x.denominator == 1 and x >= 0 for x in seq)
            # Unimodality is the key parity-tail cancellation hypothesis.
            peak = max(range(b + 1), key=lambda k: seq[k])
            if not all(seq[k] <= seq[k + 1] for k in range(peak)) or not all(
                seq[k] >= seq[k + 1] for k in range(peak, b)
            ):
                bad = [(k, int(seq[k]), int(seq[k + 1])) for k in range(b) if (k < peak and seq[k] > seq[k + 1]) or (k >= peak and seq[k] < seq[k + 1])]
                print("NONUNIMODAL", b, r, peak, bad[:20])
                raise AssertionError
            signed_suffix = [Fraction(0)] * (b + 2)
            max_suffix = [Fraction(0)] * (b + 2)
            for k in range(b, -1, -1):
                signed_suffix[k] = (seq[k] if k % 2 == 0 else -seq[k]) + signed_suffix[k + 1]
                max_suffix[k] = max(seq[k], max_suffix[k + 1])
            for q in range(min(b, int(3 * b**0.5)) + 1):
                assert abs(signed_suffix[q]) <= 2 * max_suffix[q]
                smooth_checks += 1
        print("SMOOTH", b, smooth_checks)
    print("PASS_SMOOTH", smooth_checks)


if __name__ == "__main__":
    main()
