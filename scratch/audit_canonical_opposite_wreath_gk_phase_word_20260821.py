#!/usr/bin/env python3
"""Exact audit of the canonical opposite-wreath GK phase word."""

from __future__ import annotations


def windows(order: tuple[int, ...], size: int) -> tuple[frozenset[int], ...]:
    b = len(order)
    return tuple(
        frozenset(order[(end - q) % b] for q in range(size))
        for end in range(b)
    )


def top_excess(x: frozenset[int], y: frozenset[int], b: int) -> int:
    stack = 0
    unmatched = 0
    for i in range(b):
        for bit in (i in x, i in y):
            if bit:
                stack += 1
            elif stack:
                stack -= 1
            else:
                unmatched += 1
    assert stack == unmatched
    return unmatched


def longest_alternating_cyclic(word: list[int]) -> int:
    b = len(word)
    best = 1
    for start in range(b):
        length = 1
        while length < b and word[(start + length) % b] != word[(start + length - 1) % b]:
            length += 1
        best = max(best, length)
    return best


def audit(b: int) -> None:
    r = (b - 1) // 2
    alpha = tuple(range(b))
    beta = (0,) + tuple(range(b - 1, 0, -1))
    xs = windows(alpha, r)
    ys = windows(beta, r + 1)
    orientation = []
    for p in range(b):
        values = [top_excess(xs[i], ys[(p - i) % b], b) for i in range(b)]
        assert len({k & 1 for k in values}) == 1
        expected = 2 * p if p < r else (2 * r - 1 if p == r else 2 * (2 * r - p) + 1)
        assert values[0] == expected, (b, p, values[0], expected)
        orientation.append(values[0] & 1)
    assert orientation == [0] * r + [1] * (r + 1)
    assert longest_alternating_cyclic(orientation) == 2

    rank = lambda x: ((b - 1) // 2 * x) % b
    tau = [int(rank(x) < r) for x in range(b)]
    equal_edges = sum(tau[x] == tau[(x + 1) % b] for x in range(b))
    assert equal_edges == 1
    best = max(
        sum(orientation[p] == tau[(p + shift) % b] for p in range(b))
        for shift in range(b)
    )
    assert best <= (b + 3) // 2

    for h in range(1, b):
        n = max(0, (b - h + 1) // 2)
        shortfall = 2 * n - (b + 3) / 2
        if shortfall > 0:
            assert 2 * n > best


def main() -> None:
    for b in range(5, 102, 2):
        audit(b)
        print(f"b={b} PASS")
    print("AUDIT CANONICAL OPPOSITE WREATH GK PHASE WORD: PASS")


if __name__ == "__main__":
    main()
