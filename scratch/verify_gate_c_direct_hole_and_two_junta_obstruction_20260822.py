#!/usr/bin/env python3
"""Exact finite checks for the direct-hole/two-junta Gate-C note."""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def phase_word(b: int):
    h = (b - 1) // 2
    types = ["B" if i % 2 == 0 else "A" for i in range(b)]
    counters = {"A": 0, "B": 0}
    word = []
    for _ in range(b):
        for shore in types:
            word.append((shore, counters[shore]))
            counters[shore] = (counters[shore] + 1) % b
    assert len(word) == b * b
    assert types.count("A") == h
    assert types.count("B") == h + 1
    return word


def cyclic_max_run(bits):
    n = len(bits)
    if all(bits):
        return n
    best = current = 0
    for bit in bits + bits:
        if bit:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return min(best, n)


def check_b(b: int):
    word = phase_word(b)
    n = b * b
    universe = sorted(set(word))
    assert len(universe) == 2 * b

    # The exact injectivity range used by Theorem 2.1.
    for t in range(n):
        for length in range(1, 2 * b - 1):
            block = [word[(t + i) % n] for i in range(length)]
            assert len(set(block)) == length
    assert any(
        len({word[(t + i) % n] for i in range(2 * b - 1)}) < 2 * b - 1
        for t in range(n)
    )

    # Every 2b-block contains exactly 2b-1 distinct coordinates.
    for t in range(n):
        block = {word[(t + i) % n] for i in range(2 * b)}
        assert len(block) == 2 * b - 1

    membership = {}
    middle_windows = [
        frozenset(word[(t + i) % n] for i in range(b)) for t in range(n)
    ]
    assert len(set(middle_windows)) == n
    for z in universe:
        membership[z] = [
            int(z in middle_windows[t]) for t in range(n)
        ]

    max_equality_run = 0
    for z, y in combinations(universe, 2):
        equality = [int(a == c) for a, c in zip(membership[z], membership[y])]
        max_equality_run = max(max_equality_run, cyclic_max_run(equality))
        assert cyclic_max_run(equality) <= b

    # Exact density identity in Theorem 3.1.
    size = 2 * comb(2 * b - 2, b - 2)
    assert Fraction(size, comb(2 * b, b)) == Fraction(b - 1, 2 * b - 1)

    return max_equality_run


def check_exact_juntas(b: int):
    """Brute-force (3.2), (3.3), and (4.6), not just their RHS algebra."""
    points = tuple(range(2 * b))
    full = frozenset(points)
    layer = [frozenset(c) for c in combinations(points, b)]

    for z, y in combinations(points, 2):
        family = [c for c in layer if ((z in c) == (y in c))]
        assert len(family) == 2 * comb(2 * b - 2, b - 2)
        family_set = set(family)
        assert all(full - c in family_set for c in family)
        for u in points:
            assert sum(u in c for c in family) * 2 == len(family)

    for m in range(1, min(4, b) + 1):
        pairs = [(2 * i, 2 * i + 1) for i in range(m)]
        family = [
            c
            for c in layer
            if all(((z in c) == (y in c)) for z, y in pairs)
        ]
        coefficient = sum(
            comb(m, j) * comb(2 * b - 2 * m, b - 2 * j)
            for j in range(m + 1)
            if 0 <= b - 2 * j <= 2 * b - 2 * m
        )
        assert len(family) == coefficient
        family_set = set(family)
        assert all(full - c in family_set for c in family)
        for u in points:
            assert sum(u in c for c in family) * 2 == len(family)


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def formula_minimum_overflow(loads):
    n = len(loads)
    a, r = divmod(sum(loads), n)
    ordered = sorted(loads, reverse=True)
    return sum(max(x - a - 1, 0) for x in ordered[:r]) + sum(
        max(x - a, 0) for x in ordered[r:]
    )


def check_quota_formula():
    # Exhaustively compare (2.10) with every placement of the high quotas.
    for n in range(1, 6):
        for total in range(0, 9):
            a, r = divmod(total, n)
            for loads in weak_compositions(total, n):
                brute = min(
                    sum(
                        max(loads[i] - a - int(i in high), 0)
                        for i in range(n)
                    )
                    for high in map(frozenset, combinations(range(n), r))
                )
                value = formula_minimum_overflow(loads)
                assert value == brute
                holes = sum(x == 0 for x in loads)
                if total <= n:
                    assert value == total - sum(x > 0 for x in loads)
                    assert holes == (n - total) + value

    # The strict example following (2.12): M=2N, loads 3/1.
    for n in (4, 6, 10, 20):
        loads = [3] * (n // 2) + [1] * (n // 2)
        _, r = divmod(sum(loads), n)
        overflow = formula_minimum_overflow(loads)
        assert r == 0
        assert overflow == n // 2
        assert all(x > 0 for x in loads)


def check_direct_compiler():
    """Construct the word in (2.7) and check its exact length/coverage."""
    b = 5
    word = phase_word(b)
    period = len(word)
    points = tuple(sorted(set(word)))
    targets_by_rank = {
        s: {frozenset(c) for c in combinations(points, s)}
        for s in range(1, 2 * b + 1)
    }
    starts = (0, 10)
    length = 3
    cores = [
        {
            frozenset(word[(a + u + i) % period] for i in range(b))
            for u in range(length)
        }
        for a in starts
    ]
    assert all(len(core) == length for core in cores)
    assert cores[0].isdisjoint(cores[1])

    for h_band in range(0, b - 1):
        g = b + h_band
        blocks = []
        supplied = {s: set() for s in range(b - h_band, b + h_band + 1)}
        for a in starts:
            block = [
                frozenset((word[(a + i) % period],))
                for i in range(length + g - 1)
            ]
            assert len(block) == length + g - 1
            blocks.extend(block)
            for s in supplied:
                for u in range(length):
                    token = frozenset(
                        word[(a + u + i) % period] for i in range(s)
                    )
                    assert len(token) == s
                    assert token == frozenset().union(*block[u : u + s])
                    supplied[s].add(token)

        missing = []
        for s in supplied:
            missing.extend(sorted(targets_by_rank[s] - supplied[s], key=repr))
        tail = []
        for s in range(1, 2 * b + 1):
            if abs(s - b) > h_band:
                tail.extend(sorted(targets_by_rank[s], key=repr))
        constructed = blocks + missing + tail
        predicted = (
            2 * length
            + (g - 1) * len(starts)
            + sum(len(targets_by_rank[s] - supplied[s]) for s in supplied)
            + sum(
                len(targets_by_rank[s])
                for s in range(1, 2 * b + 1)
                if abs(s - b) > h_band
            )
        )
        assert len(constructed) == predicted
        covered = set().union(*supplied.values(), missing, tail)
        assert covered == set().union(*targets_by_rank.values())


def check_binary_run_bound():
    # Exhaustive finite check of (5.1), the only numerical input to (5.2).
    for run_cap in range(1, 6):
        for length in range(1, 2 * run_cap + 5):
            for bits in product((0, 1), repeat=length):
                runs = "".join(map(str, bits)).split("0")
                if max(map(len, runs)) <= run_cap:
                    assert bits.count(0) >= length // (run_cap + 1)


def main():
    maxima = {}
    for b in (5, 7, 9, 11, 15, 21, 31):
        maxima[b] = check_b(b)
    for b in (5, 7):
        check_exact_juntas(b)
    check_quota_formula()
    check_direct_compiler()
    check_binary_run_bound()
    print(
        "GATE_C_DIRECT_HOLE_TWO_JUNTA_PASS",
        "max_runs=" + ",".join(f"{b}:{r}" for b, r in maxima.items()),
        "quota_example=PASS",
        "quota_formula=PASS",
        "direct_compiler=PASS",
        "exact_juntas=PASS",
        "run_bound=PASS",
    )


if __name__ == "__main__":
    main()
