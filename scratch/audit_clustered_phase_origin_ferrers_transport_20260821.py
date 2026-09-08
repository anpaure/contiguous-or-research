#!/usr/bin/env python3
"""Finite audit for the clustered Ferrers phase-origin transport theorem."""

from math import comb


def phase_set(b: int, r: int, q: int, s: int):
    answer = []
    phases = set(range(r))
    for p in range(b):
        interval = {(p + j) % b for j in range(1, q + 1)}
        if r + len(phases & interval) == s:
            answer.append(p)
    return answer


def shift_count(number: int, b: int, theta: int):
    if theta >= number:
        return 0
    return 1 + (number - 1 - theta) // b


def check(b: int, H: int):
    payloads = range(H + 2, b - H - 1)
    counts = {r: (comb(b, r) // b) ** 2 for r in payloads}

    for r, number in counts.items():
        values = [shift_count(number, b, theta) for theta in range(b)]
        assert sum(values) == number
        assert max(values) - min(values) <= 1
        assert all(abs(b * value - number) < b for value in values)

    for q in range(1, H + 1):
        low = max((b + 3) // 4, H + q + 2)
        high = min(3 * b // 4, b - H - 2)
        for s in range(low, high + 1):
            sets = {}
            for r in payloads:
                phases = phase_set(b, r, q, s)
                if phases:
                    sets[r] = phases
            assert sum(map(len, sets.values())) == b - q

            c = [comb(b, j) for j in range(b + 1)]
            total = (
                (b - s - q + 1) * c[s] ** 2
                + (s - 2 * q + 1) * c[s - q] ** 2
                + 2 * sum(c[s - z] ** 2 for z in range(1, q))
            ) // b
            capacities = []
            for d in range(b):
                diagonal_count = 0
                for r, phases in sets.items():
                    for p in phases:
                        theta = (d - q - p) % b
                        diagonal_count += shift_count(counts[r], b, theta)
                capacities.append(b * diagonal_count)
            assert sum(capacities) == total
            assert all(abs(b * value - total) < b**3 for value in capacities)

    print(f"PASS b={b} H={H}")


def main():
    for b, H in ((11, 1), (13, 2), (17, 3), (23, 4), (31, 5), (43, 7)):
        check(b, H)
    print("ALL CLUSTERED FERRERS PHASE-ORIGIN CHECKS PASS")


if __name__ == "__main__":
    main()
