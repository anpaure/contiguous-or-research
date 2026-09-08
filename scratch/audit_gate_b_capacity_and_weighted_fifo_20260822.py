#!/usr/bin/env python3
"""Finite regression audit for the Gate-B capacity and seam identities.

The theorem note is self-contained; this script is only a cross-check.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, floor, sqrt
from random import Random


def check_binomial_profile() -> None:
    for r in range(2, 401):
        b = 2 * r + 1
        layer1 = comb(b, r - 1)
        product = Fraction(1)
        for q in range(1, r):
            layerq = comb(b, r - q)
            assert Fraction(layerq, layer1) == product
            lower = Fraction(1) - Fraction((q - 1) * (q + 2), r)
            assert Fraction(layerq, layer1) >= lower
            product *= Fraction(r - q, r + q + 2)

    # Check the constants in Theorem 3.1 on a rational grid.
    for r in range(64, 401):
        b = 2 * r + 1
        layer1 = comb(b, r - 1)
        for numerator in range(1, 65):
            x = Fraction(numerator, 64)
            if r * x < 64:
                continue
            qmax = floor(sqrt(float(r * x)) / 4)
            for q in range(1, qmax + 1):
                layerq = comb(b, r - q)
                assert layerq - (1 - x) * layer1 >= Fraction(7, 8) * x * layer1


def random_simple_johnson_path(n: int, m: int, length: int, rng: Random):
    current = frozenset(range(m))
    path = [current]
    used = {current}
    for _ in range(length):
        candidates = []
        for out in current:
            for into in set(range(n)) - set(current):
                nxt = frozenset((set(current) - {out}) | {into})
                if nxt not in used:
                    candidates.append(nxt)
        if not candidates:
            break
        current = rng.choice(candidates)
        path.append(current)
        used.add(current)
    return path


def occurrence_data(path, hmax):
    m = len(path[0])
    by_depth = {}
    for q in range(1, hmax + 1):
        occurrences = []
        for i in range(len(path) - q):
            target = frozenset.intersection(*path[i : i + q + 1])
            if len(target) == m - q:
                occurrences.append((i, target))
        multiplicity = {}
        for _, target in occurrences:
            multiplicity[target] = multiplicity.get(target, 0) + 1
        by_depth[q] = (occurrences, multiplicity)
    return by_depth


def check_weighted_ledger() -> None:
    rng = Random(20260822)
    for n, m in [(7, 3), (9, 4)]:
        for _ in range(30):
            path = random_simple_johnson_path(n, m, min(10, comb(n, m) - 1), rng)
            transition_count = len(path) - 1
            data = occurrence_data(path, m - 1)
            omega = [Fraction(0) for _ in range(transition_count)]
            total_support_mass = 0
            for q, (occurrences, multiplicity) in data.items():
                total_support_mass += q * len(multiplicity)
                for i, target in occurrences:
                    for c in range(i, i + q):
                        omega[c] += Fraction(1, multiplicity[target])
            assert sum(omega) == total_support_mass

            # Exhaust every cut set up to size three and verify the killed-target bound.
            for size in range(min(3, transition_count) + 1):
                for cut_tuple in combinations(range(transition_count), size):
                    cuts = set(cut_tuple)
                    killed = 0
                    for q, (occurrences, multiplicity) in data.items():
                        destroyed = {target: 0 for target in multiplicity}
                        for i, target in occurrences:
                            if cuts.intersection(range(i, i + q)):
                                destroyed[target] += 1
                        killed += sum(
                            destroyed[target] == multiplicity[target]
                            for target in multiplicity
                        )
                    assert Fraction(killed) <= sum(omega[c] for c in cuts)


def admissible_gap(u, v, intervals):
    return not any(u < left <= right < v for left, right in intervals)


def dp_minimum(weights, intervals, cuts_needed):
    n = len(weights)
    infinity = None
    # State after `arcs` arcs, ending at a position.  Interior positions carry weight.
    previous = {-1: Fraction(0)}
    for arc in range(1, cuts_needed + 2):
        current = {}
        candidates = range(n) if arc <= cuts_needed else [n]
        for v in candidates:
            best = infinity
            for u, cost in previous.items():
                if u < v and admissible_gap(u, v, intervals):
                    candidate = cost + (weights[v] if v < n else 0)
                    if best is None or candidate < best:
                        best = candidate
            if best is not None:
                current[v] = best
        previous = current
    return previous.get(n)


def check_interval_dp() -> None:
    rng = Random(9173)
    for n in range(3, 10):
        for _ in range(100):
            weights = [Fraction(rng.randrange(1, 20), rng.randrange(1, 8)) for _ in range(n)]
            all_intervals = [(a, b) for a in range(n) for b in range(a, n)]
            intervals = rng.sample(all_intervals, rng.randrange(len(all_intervals) + 1))
            for cuts_needed in range(n + 1):
                brute = None
                for cut_tuple in combinations(range(n), cuts_needed):
                    cuts = set(cut_tuple)
                    if all(cuts.intersection(range(a, b + 1)) for a, b in intervals):
                        cost = sum(weights[c] for c in cuts)
                        if brute is None or cost < brute:
                            brute = cost
                assert dp_minimum(weights, intervals, cuts_needed) == brute


def main() -> None:
    check_binomial_profile()
    check_weighted_ledger()
    check_interval_dp()
    print("PASS: Gate-B capacity ratios, normalized seam ledger, and exact DP")


if __name__ == "__main__":
    main()
