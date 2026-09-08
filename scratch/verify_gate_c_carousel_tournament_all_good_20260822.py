#!/usr/bin/env python3
"""Finite audit for the carousel-tournament all-good reduction."""

from itertools import permutations
from math import gcd

from verify_gate_c_single_root_ballot_law_and_moment_gate_20260822 import (
    good_count,
    inverse,
    is_two_sided_ballot,
)


def x_sign(sigma, a, b):
    k = len(sigma)
    return 1 if (((b - a) % k + (sigma[b] - sigma[a]) % k) % 2 == 0) else -1


def y_sign(sigma, a, b):
    k = len(sigma)
    return x_sign(sigma, a, b) * (-1 if (b - a) % k % 2 else 1)


def audit_identities():
    for k in (3, 5, 7):
        e = (k - 1) // 2
        for order in permutations(range(k)):
            sigma = inverse(order)
            for a in range(k):
                out = []
                incoming = []
                for b in range(k):
                    if a == b:
                        continue
                    assert x_sign(sigma, a, b) == x_sign(sigma, b, a)
                    assert y_sign(sigma, a, b) == -y_sign(sigma, b, a)
                    expected = 1 if (sigma[b] - sigma[a]) % k % 2 == 0 else -1
                    assert y_sign(sigma, a, b) == expected
                    (out if expected == 1 else incoming).append(b)
                assert len(out) == len(incoming) == e
                for neighborhood in (out, incoming):
                    by_position = sorted(neighborhood, key=lambda b: (sigma[b] - sigma[a]) % k)
                    for i in range(len(by_position)):
                        for j in range(i + 1, len(by_position)):
                            assert y_sign(sigma, by_position[i], by_position[j]) == 1

            all_good = good_count(order) == k
            all_rows = all(
                is_two_sided_ballot(tuple(
                    ((-1 if offset % 2 else 1)
                     * y_sign(sigma, a, (a + offset) % k))
                    for offset in range(1, k)
                ))
                for a in range(k)
            )
            directed_cycle = all(y_sign(sigma, a, (a - 1) % k) == 1
                                 for a in range(k))
            assert all_good == all_rows
            assert not all_good or directed_cycle
        print(f"PASS: K={k} carousel, local transitivity, and equivalence")


def audit_affine_and_exhaustive():
    expected = {3: (1,), 5: (1,), 7: (1, 3, 5), 9: (1,)}
    for k, expected_gaps in expected.items():
        affine_gaps = []
        for d in range(1, k):
            if gcd(d, k) != 1:
                continue
            word = tuple(
                1 if (offset + (d * offset) % k) % 2 == 0 else -1
                for offset in range(1, k)
            )
            if is_two_sided_ballot(word):
                affine_gaps.append(d)
        assert tuple(affine_gaps) == expected_gaps

        all_good_orders = []
        for tail in permutations(range(1, k)):
            order = (0,) + tail
            if good_count(order) == k:
                sigma = inverse(order)
                gaps = tuple((sigma[(a + 1) % k] - sigma[a]) % k
                             for a in range(k))
                all_good_orders.append(gaps)
        assert len(all_good_orders) == len(expected_gaps)
        assert {gaps[0] for gaps in all_good_orders} == set(expected_gaps)
        assert all(len(set(gaps)) == 1 for gaps in all_good_orders)
        print(f"PASS: K={k} exhaustive all-good orders are affine {expected_gaps}")


if __name__ == "__main__":
    audit_identities()
    audit_affine_and_exhaustive()
