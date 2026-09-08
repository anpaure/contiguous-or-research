"""Independent finite checks of the overlap inequalities; no proof by sampling."""

from fractions import Fraction as Q
from itertools import product
from math import comb
from math import exp


def pos(x):
    return max(Q(0), x)


def profile(t, c, u, v):
    return pos(u - abs(t - c)) - pos(v - abs(t - c))


def smoothed_binomial(k, x):
    return sum(Q(comb(k, j)) * pos(1 - abs(x - j)) for j in range(k + 1))


def main():
    inequalities = 0
    for a, b in product(range(1, 10), repeat=2):
        u, v = Q(a + b, 2), Q(abs(a - b), 2)
        for c in (Q(j, 2) for j in range(-24, 25)):
            deficit = u - profile(Q(0), c, u, v)
            assert deficit == min(u, max(v, abs(c)))
            for t in (Q(j, 2) for j in range(1, 25)):
                assert profile(t, c, u, v) + profile(-t, c, u, v) <= (
                    2 * pos(u - t) + 2 * deficit
                )
                inequalities += 1

    moment_checks = 0
    # Check the scalar certificate used to sharpen Cauchy--Schwarz.
    for S in range(1, 10):
        for B in (Q(j, 4) for j in range(1, 2 * S + 1)):
            for t in (Q(1, 2), Q(1), Q(3)):
                lam, kap = 2 * t * S / B, t * S * S / (B * B)
                assert kap >= lam
                for x in (Q(j, 4) for j in range(81)):
                    assert x*x - lam*x + kap*min(t, x) >= 0
                    moment_checks += 1

    # A literal family of saturated rectangles: every target is a singleton
    # chain on each shore, and it is paired with its complement. This heavily
    # overlapping family tests normalization, odd k, and interpolation.
    covers = 0
    for k in range(2, 10):
        W, M, V = comb(k, k // 2), 2 ** (k + 1), 2 ** (k + 1)
        for t in (Q(j, 4) for j in range(1, 4*k + 1)):
            B = (2*M - W - smoothed_binomial(k, Q(k, 2) + t)) / 2
            assert B > 0
            assert V >= 2*t*pos(Q(W, 2)-B)**2/B
            if B <= Q(W, 4):
                assert V >= t*W*W/(2*B)
            covers += 1

    # Analytic tangent construction: locate its second crossing and check
    # the resulting profile and its slope. Floating point is diagnostic only.
    for a in (0.02, 0.05, 0.1, 0.2, 0.4):
        C, lam = (1 + 4*a*a)*exp(-2*a*a), 4*a*exp(-2*a*a)
        lo, hi = 0.5, C/lam
        for _ in range(100):
            mid = (lo + hi)/2
            if exp(-2*mid*mid) < C-lam*mid:
                lo = mid
            else:
                hi = mid
        z = (lo+hi)/2
        assert z > 0.5
        assert -4*z*exp(-2*z*z)+lam > 0
        assert abs(exp(-2*z*z)-(C-lam*z)) < 1e-12

    print(f"PASS: {inequalities} trapezoid inequalities; "
          f"{moment_checks} scalar certificates; {covers} finite cover checks; "
          "5 Gaussian tangent profiles")


if __name__ == "__main__":
    main()
