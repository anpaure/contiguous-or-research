#!/usr/bin/env python3
"""Finite audit for the completed coherent-tour selector reduction.

The proof is in
MATH_REDUCTION_GATE_C_COMPLETED_TOUR_SELECTOR_20260905.md.
"""

from collections import Counter
from fractions import Fraction
from math import comb


def completed_word(b: int) -> tuple[int, ...]:
    """Canonical FIFO word; labels 2*j+bit are the two members of pair j."""
    state = [0] * b
    word: list[int] = []
    for s in range(b):
        for k in range(1, b):
            j = (s + k) % b
            state[j] ^= 1
            word.append(2 * j + state[j])
        word.append(2 * s + state[s])
    assert state == [0] * b
    return tuple(word)


def support(word: tuple[int, ...], ell: int) -> set[frozenset[int]]:
    n = len(word)
    return {
        frozenset(word[(a + j) % n] for j in range(ell))
        for a in range(n)
    }


def audit_word(b: int) -> None:
    word = completed_word(b)
    assert len(word) == b * b

    gap_hist: Counter[int] = Counter()
    for label in range(2 * b):
        positions = [a for a, value in enumerate(word) if value == label]
        for i, a in enumerate(positions):
            gap = (positions[(i + 1) % len(positions)] - a) % (b * b)
            if gap == 0:
                gap = b * b
            gap_hist[gap] += 1
    assert gap_hist == Counter(
        {2 * b - 2: b * (b - 2), 2 * b - 1: b, 4 * b - 3: b}
    )

    for ell in range(1, 2 * b - 2):
        windows = support(word, ell)
        assert all(len(window) == ell for window in windows)
        expected = b * (ell + 1) if ell <= b - 1 else b * b
        assert len(windows) == expected, (b, ell, len(windows), expected)


def audit_scalar_inequalities(b: int) -> None:
    W = comb(2 * b, b)
    q = b * (b - 1)
    for j in range(1, b):
        Wj = comb(2 * b, b + j)
        product = Fraction(Wj, W)
        assert product <= Fraction(b - j + 1, b + 1)

        d_minus = b * (b - j + 1)
        lambda_minus = Fraction(W * d_minus, q * Wj)
        assert lambda_minus >= Fraction(b + 1, b - 1)

        d_plus = b * b
        lambda_plus = Fraction(W * d_plus, q * Wj)
        assert lambda_plus >= Fraction(b, b - 1)


def main() -> None:
    for b in range(5, 32, 2):
        audit_word(b)
    for b in range(5, 502, 2):
        audit_scalar_inequalities(b)
    print("PASS: exact gap and all-band support census for odd 5 <= b <= 31")
    print("PASS: fractional-load inequalities for odd 5 <= b <= 501")


if __name__ == "__main__":
    main()
