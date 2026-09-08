#!/usr/bin/env python3
"""Regression checks for the fixed-slice/Palm Gate A note.

The proofs are analytic.  This script checks the exact finite-population
ratios, the tuple AM--GM inequality, the support-entropy scale, and the
exponent arithmetic used in the stopped union bound.
"""

from fractions import Fraction
from math import comb, factorial, log
import random
from itertools import combinations


def falling(n: int, a: int) -> int:
    z = 1
    for i in range(a):
        z *= n - i
    return z


def inclusion_ratio(N: int, m: int, a: int) -> Fraction:
    if a == 0:
        return Fraction(1, 1)
    h = Fraction(falling(m, a), falling(N, a))
    p_power = Fraction(m, N) ** a
    return h / p_power


def check_inclusion_lemma() -> None:
    for N in range(12, 121):
        for m in range(2, N + 1):
            q = min(8, m // 2)
            for a in range(q + 1):
                ratio = float(inclusion_ratio(N, m, a))
                assert ratio > 0
                lhs = abs(log(ratio))
                rhs = 2 * q * q / m
                assert lhs <= rhs + 1e-12, (N, m, q, a, lhs, rhs)


def check_amgm_step() -> None:
    rng = random.Random(20260822)
    for count in range(1, 12):
        for _ in range(2000):
            vals = [10 ** rng.uniform(-2, 4) for _ in range(count)]
            lhs = 1.0
            for z in vals:
                lhs *= z
            rhs = sum(z ** count for z in vals) / count
            assert lhs <= rhs * (1 + 1e-12)


def check_support_entropy() -> None:
    previous = None
    for r in range(3, 81):
        n_m = comb(2 * r + 1, r)
        n_l = comb(2 * r + 1, r - 1)
        states = comb(n_m, 2 * r) * comb(n_l, 2 * r)
        support = factorial(2 * r + 1)
        log_inverse_mass = log(states) - log(support)
        assert log_inverse_mass > 0
        scaled = log_inverse_mass / (r * r)
        if r >= 12:
            assert scaled > 1.0
        if previous is not None and r >= 8:
            # The normalized exponent approaches a positive constant; allow
            # tiny finite-size variation but reject a collapse.
            assert scaled > 0.75 * previous
        previous = scaled


def check_exponent_budget() -> None:
    # J=O(r log r), reference failure r^(-3/2+9 alpha), and comparison
    # factor r^kappa give total exponent -1/2+9 alpha+kappa.
    samples = [
        (Fraction(0), Fraction(1, 20)),
        (Fraction(1, 10), Fraction(1, 30)),
        (Fraction(1, 4), Fraction(1, 40)),
    ]
    for kappa, alpha in samples:
        condition = kappa + 9 * alpha < Fraction(1, 2)
        exponent = -Fraction(1, 2) + 9 * alpha + kappa
        assert condition == (exponent < 0)

    # Uncompressed sixth-moment component types, after incidence conversion,
    # Markov at r^-delta, and O(r log r) stopped rounds.
    # Each pair is (constant exponent, x exponent) in the sixth moment.
    terms = [(-3, -9), (-4, -21), (-4, -18), (-5, -45)]
    alpha = Fraction(1, 16)  # strictly below the sharp 1/15 endpoint
    bounds = []
    for r_power, x_power in terms:
        # Add 2+delta to r exponent; x^-a contributes alpha*a.
        bound = -(r_power + 2 + alpha * (-x_power))
        bounds.append(bound)
    expected = [
        1 - 9 * alpha,
        2 - 21 * alpha,
        2 - 18 * alpha,
        3 - 45 * alpha,
    ]
    assert bounds == expected
    assert all(z > 0 for z in bounds)

    endpoint = Fraction(1, 15)
    endpoint_bounds = [
        1 - 9 * endpoint,
        2 - 21 * endpoint,
        2 - 18 * endpoint,
        3 - 45 * endpoint,
    ]
    assert min(endpoint_bounds) == 0

    # The fixed-slice six-tuple error uses rooted rows through c=5.
    # At alpha<1/15 both terms in
    # R_c=O(r^-1 x^-3c + r^-2 x^-4c) are o(1).
    alpha = Fraction(1, 16)
    for c in range(1, 6):
        assert -1 + 3 * c * alpha < 0
        assert -2 + 4 * c * alpha < 0
    endpoint = Fraction(1, 15)
    assert -1 + 3 * 5 * endpoint == 0


def check_bad_incidence_arithmetic() -> None:
    # r (r x^3)^(-s), at s=3.
    s = 3
    r_exponent = 1 - s
    x_exponent = -3 * s
    assert (r_exponent, x_exponent) == (-2, -9)
    # Markov at epsilon=r^-1/2.
    assert r_exponent + Fraction(1, 2) == Fraction(-3, 2)


def isolated_set(mask: int, adj: list[int], n: int) -> int:
    ans = 0
    for v in range(n):
        if (mask >> v) & 1 and not (adj[v] & mask):
            ans |= 1 << v
    return ans


def check_transition_kernel() -> None:
    rng = random.Random(41020260822)
    p = Fraction(2, 7)
    for n in range(1, 8):
        for _ in range(60):
            adj = [0] * n
            for u, v in combinations(range(n), 2):
                if rng.randrange(3) == 0:
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u

            direct: dict[int, Fraction] = {}
            for marks in range(1 << n):
                a = isolated_set(marks, adj, n)
                weight = p ** marks.bit_count() * (1 - p) ** (n - marks.bit_count())
                direct[a] = direct.get(a, Fraction(0)) + weight

            for a0, observed in direct.items():
                assert all(not ((a0 >> v) & 1 and (adj[v] & a0)) for v in range(n))
                open_n = 0
                for v in range(n):
                    if (a0 >> v) & 1:
                        open_n |= adj[v]
                open_n &= ~a0
                closed = open_n | a0
                u_mask = ((1 << n) - 1) & ~closed

                zeta = Fraction(0)
                sub = u_mask
                while True:
                    if isolated_set(sub, adj, n) == 0:
                        zeta += p ** sub.bit_count() * (1 - p) ** (u_mask.bit_count() - sub.bit_count())
                    if sub == 0:
                        break
                    sub = (sub - 1) & u_mask

                formula = p ** a0.bit_count() * (1 - p) ** open_n.bit_count() * zeta
                assert formula == observed, (n, adj, a0, formula, observed)


def main() -> None:
    check_inclusion_lemma()
    check_amgm_step()
    check_support_entropy()
    check_exponent_budget()
    check_bad_incidence_arithmetic()
    check_transition_kernel()
    print("PASS: fixed-slice high moments / stopped-Palm regression audit")


if __name__ == "__main__":
    main()
