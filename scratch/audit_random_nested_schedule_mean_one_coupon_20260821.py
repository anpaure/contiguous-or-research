#!/usr/bin/env python3
"""Fail-closed audit for the random nested mean-one coupon obstruction."""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter
from fractions import Fraction


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def nested_sets(rank: tuple[int, ...]) -> list[set[int]]:
    b = len(rank)
    return [{x for x in range(b) if rank[x] < r} for r in range(b + 1)]


def histograms(rank: tuple[int, ...], q: int):
    b = len(rank)
    ps = nested_sets(rank)
    hist = [[0] * (q + 1) for _ in range(b + 1)]
    per_profile = [[0] * (b + 1) for _ in range(b + q + 1)]
    for p in range(b):
        window = {(p + j) % b for j in range(1, q + 1)}
        vals = []
        for r in range(b + 1):
            z = len(ps[r] & window)
            hist[r][z] += 1
            vals.append(r + z)
            per_profile[r + z][r] += 1
        assert all(vals[r + 1] - vals[r] in (1, 2) for r in range(b))
        assert len(set(vals)) == b + 1
    return hist, per_profile


def audit_exhaustive() -> None:
    # Exhaustive through b=8 would have 46233 permutations in total if one
    # representative q is used at b=8; use all q through b=7 and q<=3 at 8.
    for b in range(2, 9):
        sums = [[[0] * (q + 1) for _ in range(b + 1)]
                for q in range(1, b + 1)]
        count = 0
        for rank in itertools.permutations(range(b)):
            count += 1
            q_values = range(1, b + 1) if b <= 7 else range(1, 4)
            for q in q_values:
                hist, per_profile = histograms(rank, q)
                for r in range(b + 1):
                    for z in range(q + 1):
                        sums[q - 1][r][z] += hist[r][z]
                for s in range(b + q + 1):
                    assert sum(per_profile[s]) <= b
        q_values = range(1, b + 1) if b <= 7 else range(1, 4)
        for q in q_values:
            for r in range(b + 1):
                for z in range(q + 1):
                    expected = Fraction(
                        b * choose(r, z) * choose(b - r, q - z),
                        choose(b, q),
                    )
                    assert Fraction(sums[q - 1][r][z], count) == expected


def audit_ratio_identity() -> None:
    for b in range(11, 80, 2):
        for q in range(1, min(12, b) + 1):
            for s in range(max(q, b // 3), min(b, 2 * b // 3) + 1):
                t = s - q
                x2 = 2 * s - b - q
                for z in range(q + 1):
                    r = s - z
                    if not (0 <= t <= b and 0 <= r <= b):
                        continue
                    ratio = Fraction(choose(b, r) ** 2, choose(b, s) * choose(b, t))
                    # (2.3) is asymptotic; check its leading exponent against
                    # the exact log ratio at the expected O((q+|x|)^3/b^2) scale.
                    delta2 = 2 * z - q
                    lead = (q * q + 2 * x2 * delta2 - delta2 * delta2) / b
                    exact = math.log(ratio.numerator) - math.log(ratio.denominator)
                    err_scale = 1 + (q + abs(x2)) ** 3 / (b * b)
                    assert abs(exact - lead) <= 20 * err_scale


def audit_random_histograms() -> None:
    rng = random.Random(20260821)
    rows = []
    for b in (101, 251, 509, 1009, 2003, 4001):
        q = max(2, int(math.log(b) ** 2))
        q = min(q, b // 5)
        rank = list(range(b))
        rng.shuffle(rank)
        # Direct O(bq) rolling counts for central r values on a sparse grid.
        max_fraction = 0.0
        for r in range(b // 4, 3 * b // 4 + 1, max(1, b // 80)):
            word = [int(rank[x] < r) for x in range(b)]
            z = sum(word[j % b] for j in range(1, q + 1))
            counts = Counter([z])
            for p in range(1, b):
                z -= word[p % b]
                z += word[(p + q) % b]
                counts[z] += 1
            assert sum(counts.values()) == b
            max_fraction = max(max_fraction, max(counts.values()) / b)
        scaled_atom = max_fraction * math.sqrt(q)
        scale = 1 / math.sqrt(q) + q * math.sqrt(math.log(b) / b)
        rows.append((b, q, max_fraction, scaled_atom, scale))
        assert scaled_atom < 3
        assert max_fraction <= 4 * scale
    print("RANDOM_HISTOGRAMS", rows)


def audit_coupon_products() -> None:
    rng = random.Random(81726)
    for _ in range(5000):
        n = rng.randrange(2, 200)
        raw = [rng.random() for _ in range(n)]
        total = rng.random() * 1.01
        lambdas = [total * x / sum(raw) for x in raw]
        if max(lambdas) >= 1:
            continue
        product = math.prod(1 - x for x in lambdas)
        square = sum(x * x for x in lambdas)
        # Elementary finite form behind log product = -sum lambda-O(sum lambda^2).
        lower = math.exp(-sum(lambdas) - square / (1 - max(lambdas)))
        assert product + 1e-15 >= lower


def main() -> None:
    audit_exhaustive()
    audit_ratio_identity()
    audit_random_histograms()
    audit_coupon_products()
    print("PASS random nested mean-one coupon audit")


if __name__ == "__main__":
    main()
