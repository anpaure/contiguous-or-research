#!/usr/bin/env python3
"""H100 audit for the layer-saturated retired-chain rounding obstruction.

The proof is probabilistic; this script audits its exact deterministic
algebra and the asymptotic scale separation used in the specialization.  It
checks:

* the exact Boolean-layer retirement-cohort identities;
* the binomial ratio formula for every nonterminal cohort;
* the equipartition gadget's load, pair-load, and matching constants;
* the short/long cohort split on large asymptotic instances; and
* the claimed Omega(sqrt(b) W_b) mass scale using log-stable ratios.

Finite computation is an audit of the proof kernel, not a replacement for
the probabilistic-method proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, comb, exp, lgamma, log, sqrt


def exact_cohort_checks() -> int:
    checks = 0
    for b, H in [(31, 8), (101, 20), (251, 35), (503, 50)]:
        W = comb(2 * b, b)
        M = [comb(2 * b, b + q) for q in range(H + 1)] + [0]
        d = [0] + [M[ell] - M[ell + 1] for ell in range(1, H + 1)]

        assert sum(d[1:]) == M[1]
        for q in range(1, H + 1):
            assert sum(d[q:]) == M[q]
            checks += 1
        assert sum(ell * d[ell] for ell in range(1, H + 1)) == sum(M[1 : H + 1])
        checks += 1

        for ell in range(1, H):
            assert d[ell] * (b + ell + 1) == M[ell] * (2 * ell + 1)
            checks += 1
        assert d[H] == M[H]
        assert W > M[1]
        checks += 2
    return checks


def gadget_constant_checks() -> int:
    checks = 0
    # Algebraic counts for an r-partite D-regular equipartition gadget.
    # V=rL, E=LD, and uniform edge weight 1/D.
    for D, r, L in [(101, 1001, 10**9), (1009, 2001, 10**12), (10007, 5001, 10**15)]:
        vertices = r * L
        edges = L * D
        weight = Fraction(1, D)
        mass = edges * weight
        assert mass == L
        assert D * weight == 1
        assert 2 * weight == Fraction(2, D)
        assert vertices // r == L
        checks += 4
    return checks


def log_binom(n: int, k: int) -> float:
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


def asymptotic_checks() -> tuple[int, list[str]]:
    checks = 0
    rows: list[str] = []
    # The proof is asymptotic and the deliberately conservative constant 128
    # in R delays the visible separation until sqrt(b) dominates log(b).
    for b in [10**8, 10**9, 10**10]:
        H = int(sqrt(b * log(b)))
        Qb = log(2.0 * exp(1.0) * b * (H + 2))
        R = ceil(128.0 * Qb)
        assert R < H
        assert H < b
        checks += 2

        logW = log_binom(2 * b, b)
        ratios = [0.0] * (H + 1)
        # A recurrence is more stable than subtracting two lgamma values at
        # every q and exactly mirrors M_(q+1)/M_q.
        ratio = 1.0
        for q in range(1, H + 1):
            ratio *= (b - q + 1) / (b + q)
            ratios[q] = ratio

        d_ratios = [0.0] * (H + 1)
        for ell in range(1, H):
            d_ratios[ell] = ratios[ell] * (2 * ell + 1) / (b + ell + 1)
        d_ratios[H] = ratios[H]

        assert abs(sum(d_ratios[1:]) - ratios[1]) <= 5e-12
        total = sum(ratios[1:])
        cohort_total = sum(ell * d_ratios[ell] for ell in range(1, H + 1))
        assert abs(total - cohort_total) <= 2e-9 * total
        checks += 2

        short = sum(ell * d_ratios[ell] for ell in range(1, R))
        long = cohort_total - short
        assert total >= 0.2 * sqrt(b)
        assert short <= R
        assert long >= 0.1 * sqrt(b)
        checks += 3

        worst_fraction = 0.0
        for ell in range(R, H + 1):
            fraction = 32.0 * log(2.0 * exp(1.0) * b * (ell + 2)) / (ell + 2)
            worst_fraction = max(worst_fraction, fraction)
            assert fraction <= 0.25 + 1e-12
            checks += 1

        # Every cohort is exponentially larger than b.  We check this on a
        # log scale, avoiding construction of million-digit binomials.
        min_log_d = float("inf")
        for ell in [1, min(R - 1, H - 1), R, H - 1, H]:
            if ell == H:
                value = logW + log(ratios[ell])
            else:
                value = (
                    logW
                    + log(ratios[ell])
                    + log(2 * ell + 1)
                    - log(b + ell + 1)
                )
            min_log_d = min(min_log_d, value)
            assert value > 10 * log(b)
            checks += 1

        rows.append(
            "b={} H={} R={} total/W={:.3f}sqrt(b) short/total={:.3e} "
            "long/W={:.3f}sqrt(b) bad-match-frac<={:.4f} log(d_min)/log(b)={:.1f}".format(
                b,
                H,
                R,
                total / sqrt(b),
                short / total,
                long / sqrt(b),
                worst_fraction,
                min_log_d / log(b),
            )
        )
    return checks, rows


def central_product_lower_bound_checks() -> int:
    checks = 0
    for b in [10_000, 100_000, 1_000_000]:
        ratio = 1.0
        cutoff = int(sqrt(b) / 4)
        minimum = 1.0
        for q in range(1, cutoff + 1):
            ratio *= (b - q + 1) / (b + q)
            minimum = min(minimum, ratio)
            checks += 1
        assert minimum >= 0.80
    return checks


def main() -> None:
    exact = exact_cohort_checks()
    gadget = gadget_constant_checks()
    asymptotic, rows = asymptotic_checks()
    central = central_product_lower_bound_checks()
    for row in rows:
        print(row)
    print(
        "PASS: exact_cohort_checks={} gadget_constant_checks={} "
        "asymptotic_checks={} central_ratio_checks={}".format(
            exact, gadget, asymptotic, central
        )
    )


if __name__ == "__main__":
    main()
