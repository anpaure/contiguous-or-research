#!/usr/bin/env python3
"""Exact audit for the radius-two Johnson shell packing reduction."""

from itertools import combinations
from math import comb


def c(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def lambda_formula(b: int, d: int) -> int:
    return sum(
        c(b - d, 2 + t - d) * c(d, t) ** 2 * c(b - d, 2 - t)
        for t in range(3)
    )


def lambda_closed(b: int, d: int) -> int:
    if d == 1:
        return (b - 1) ** 2 * (b - 2)
    if d == 2:
        return (b - 2) * (5 * b - 11)
    if d == 3:
        return 18 * (b - 3)
    if d == 4:
        return 36
    if d >= 5:
        return 0
    return comb(b, 2) ** 2


def mask(xs) -> int:
    ans = 0
    for x in xs:
        ans |= 1 << x
    return ans


def johnson_distance(x: int, y: int, b: int) -> int:
    return b - (x & y).bit_count()


def brute_audit(b: int) -> None:
    vertices = [mask(s) for s in combinations(range(2 * b), b)]
    base = vertices[0]
    shell_base = {z for z in vertices if johnson_distance(base, z, b) == 2}
    assert len(shell_base) == comb(b, 2) ** 2

    representatives = {}
    for y in vertices:
        d = johnson_distance(base, y, b)
        representatives.setdefault(d, y)

    for d, y in representatives.items():
        shell_y = {z for z in vertices if johnson_distance(y, z, b) == 2}
        actual = len(shell_base & shell_y)
        expected = lambda_formula(b, d)
        assert actual == expected, (b, d, actual, expected)
        if d <= 4:
            assert actual > 0
        else:
            assert actual == 0


def symbolic_audit() -> None:
    for b in range(5, 200):
        s = comb(b, 2) ** 2
        assert 1 + b * b + s == s + b * b + 1
        for d in range(1, b + 1):
            assert lambda_formula(b, d) == lambda_closed(b, d), (b, d)
        max_codegree = max(lambda_formula(b, d) for d in range(1, b + 1))
        assert max_codegree == (b - 1) ** 2 * (b - 2)
        assert max_codegree / s == 4 * (b - 2) / (b * b)


if __name__ == "__main__":
    for b in range(5, 8):
        brute_audit(b)
    symbolic_audit()
    print("PASS")
