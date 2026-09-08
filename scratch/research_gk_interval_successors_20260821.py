#!/usr/bin/env python3
"""Test whether GK chains on interval source rectangles follow stream successors."""

from __future__ import annotations


def additions(bits: list[int]) -> list[int]:
    stack: list[int] = []
    matched = [False] * len(bits)
    for p, bit in enumerate(bits):
        if bit:
            stack.append(p)
        elif stack:
            q = stack.pop()
            matched[p] = matched[q] = True
    return list(reversed([p for p, bit in enumerate(bits) if not bit and not matched[p]]))


def interval(b: int, end: int, size: int) -> set[int]:
    return {(end - t) % b for t in range(size)}


def main() -> None:
    for b in range(3, 16, 2):
        for r in range(1, b):
            bad_first = 0
            bad_full = 0
            examples = []
            for i in range(b):
                X = interval(b, i, r)
                for j in range(b):
                    Y = interval(b, j, b - r)
                    bits = []
                    for t in range(b):
                        bits.extend((int(t in X), int(t in Y)))
                    aa = additions(bits)
                    expected_A = [(i + t) % b for t in range(1, b - r + 1)]
                    expected_B = [(j + t) % b for t in range(1, r + 1)]
                    # Physical alternating stream with the GK first orientation.
                    ea = iter(expected_A)
                    eb = iter(expected_B)
                    expected = []
                    if aa:
                        side = aa[0] % 2
                        for z in range(len(aa)):
                            if (side + z) % 2 == 0:
                                expected.append(2 * next(ea))
                            else:
                                expected.append(2 * next(eb) + 1)
                    if aa and aa[0] != expected[0]:
                        bad_first += 1
                    if aa != expected:
                        bad_full += 1
                        if len(examples) < 2:
                            examples.append((i, j, aa, expected))
            print("CASE", b, r, "BAD_FIRST", bad_first, "BAD_FULL", bad_full, "EX", examples)


if __name__ == "__main__":
    main()
