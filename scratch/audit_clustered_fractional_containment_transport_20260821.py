#!/usr/bin/env python3
"""Exact finite audit of the clustered fractional containment flow."""

from fractions import Fraction
from math import comb


def phase_count(b: int, r: int, q: int, z: int):
    if z == 0:
        return b - r - q + 1
    if z == q:
        return r - q + 1
    return 2


def check(b: int, H: int):
    payloads = range(H + 2, b - H - 1)
    for q in range(1, H + 1):
        for r in payloads:
            assert sum(phase_count(b, r, q, z) for z in range(q + 1)) == b

        low = max((b + 3) // 4, H + q + 2)
        high = min(3 * b // 4, b - H - 2)
        for s in range(low, high + 1):
            target_count = comb(b, s) * comb(b, s - q)
            total_capacity = 0
            contributions = []
            for r in payloads:
                z = s - r
                if not 0 <= z <= q:
                    continue
                n = phase_count(b, r, q, z)
                degree = comb(b - r, z) * comb(r, q - z)
                sources_in_target = comb(s, r) * comb(b + q - s, b - r)
                assert sources_in_target * target_count == degree * comb(b, r) ** 2
                capacity = Fraction(n * comb(b, r) ** 2, b)
                total_capacity += capacity
                contributions.append((r, z, n, degree, sources_in_target))

            rho = min(Fraction(1), Fraction(target_count, total_capacity))
            target_load = sum(
                rho * Fraction(n, b * degree) * sources_in_target
                for _, _, n, degree, sources_in_target in contributions
            )
            assert target_load == min(Fraction(1), total_capacity / target_count)
            assert target_count * target_load == min(Fraction(target_count), total_capacity)

            for r in payloads:
                source_load = Fraction(0)
                for z in range(q + 1):
                    profile = r + z
                    if not low <= profile <= high:
                        continue
                    profile_target = comb(b, profile) * comb(b, profile - q)
                    profile_capacity = sum(
                        Fraction(phase_count(b, rr, q, profile - rr) * comb(b, rr) ** 2, b)
                        for rr in payloads
                        if 0 <= profile - rr <= q
                    )
                    profile_rho = min(Fraction(1), Fraction(profile_target, profile_capacity))
                    source_load += profile_rho * Fraction(phase_count(b, r, q, z), b)
                assert source_load <= 1

    print(f"PASS b={b} H={H}")


def main():
    for b, H in ((11, 1), (13, 2), (17, 3), (23, 4), (31, 5), (43, 7)):
        check(b, H)
    print("ALL CLUSTERED FRACTIONAL-CONTAINMENT CHECKS PASS")


if __name__ == "__main__":
    main()
