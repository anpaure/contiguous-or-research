#!/usr/bin/env python3
"""Finite audit for the phase-packet higher-overlap theorem.

The proof is in
MATH_THEOREM_GATE_C_PHASE_PACKET_HIGHER_OVERLAP_AND_REGENERATION_GATE_20260822.md.
This script exhausts every packet label for b=3,5 and checks the finite
identities and inequalities used there.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def packet_sequence(label: tuple[int, ...], b: int) -> tuple[int, ...]:
    """Return the b+1 middle targets as coordinate bit masks."""
    cyc = label[:-1]
    n = 2 * b - 1
    return tuple(
        sum(1 << cyc[(i + j) % n] for j in range(b))
        for i in range(b + 1)
    )


def predicted_position_count(K: tuple[int, ...], b: int) -> int:
    if len(K) == 1:
        return factorial(b) ** 2
    gaps = tuple(K[i + 1] - K[i] for i in range(len(K) - 1))
    span = K[-1] - K[0]
    if span < b:
        value = factorial(b - span)
        for gap in gaps:
            value *= factorial(gap)
        return value * value
    value = 1
    for gap in gaps:
        value *= factorial(gap) ** 2
    return value // (gaps[0] * gaps[-1])


def falling(b: int, r: int) -> int:
    ans = 1
    for j in range(r):
        ans *= b - j
    return ans


def A_value(b: int, r: int) -> Fraction:
    if r < 0 or r > b - 1:
        return Fraction(0)
    return Fraction(comb(b - 1, r), falling(b, r) ** 2)


def audit_symbolic_tail_bounds() -> None:
    """Audit every deterministic inequality used in the split at b/2."""
    for b in range(5, 202, 2):
        n = (b - 1) // 2
        An = A_value(b, n)
        exact_An = Fraction((n + 1) ** 2, b * b * factorial(b - 1))
        assert An == exact_An, (b, An, exact_An)

        # Low-order estimate (3.11).
        for r in range(n + 1):
            low_rhs = Fraction(4**r, b**r * factorial(r))
            assert A_value(b, r) <= low_rhs, (
                "low A bound", b, r, A_value(b, r), low_rhs
            )

        # Corrected high-order monotonicity (4.6)--(4.7).
        for r in range(n, b - 1):
            ratio = A_value(b, r + 1) / A_value(b, r)
            ratio_formula = Fraction(
                b - 1 - r, (r + 1) * (b - r) ** 2
            )
            assert ratio == ratio_formula < 1, (b, r, ratio, ratio_formula)
        factorial_tail = Fraction(1, factorial(b - 1))
        power_tail = Fraction(4 ** (b - 1), b ** (b - 1))
        final_tail = Fraction(b * 4**b, b**b)
        assert An <= factorial_tail <= power_tail <= final_tail, (
            b, An, factorial_tail, power_tail, final_tail
        )

        # The coefficient used before summing at most b high moments.
        moment_tail = Fraction(2 * b * b * 8**b, b**b)
        for s in range(n + 1, b + 1):
            moment_rhs = (2**s) * (s + 1) * (
                A_value(b, s) + Fraction(A_value(b, s - 1), b + 1)
            )
            assert moment_rhs <= moment_tail, (
                "high moment bound", b, s, moment_rhs, moment_tail
            )

        # Independently audit the exact pair-profile sum used in (3.3).
        q = b + 1
        for anchor in range(q):
            rooted_pair_sum = Fraction(0)
            for other in range(q):
                if other == anchor:
                    continue
                distance = abs(anchor - other)
                if {anchor, other} == {0, b}:
                    distance = b - 1
                if distance <= b - 2:
                    rooted_pair_sum += Fraction(
                        2 * (b + 1 - distance),
                        (b + 1) * comb(b, distance) ** 2,
                    )
                elif distance == b - 1:
                    rooted_pair_sum += Fraction(6, (b + 1) * b * b)
            assert rooted_pair_sum <= Fraction(12, b * b), (
                "M1 bound", b, anchor, rooted_pair_sum
            )

    print("PASS symbolic tail bounds for every odd 5 <= b <= 201")


def audit_b(b: int) -> None:
    canonical = tuple(range(2 * b))
    Fseq = packet_sequence(canonical, b)
    F = frozenset(Fseq)
    q = b + 1
    labelled_degree = q * factorial(b) ** 2

    # match_masks records which canonical target occurs at its prescribed
    # canonical position.  rooted_hist[i] records |E cap F| for labels E
    # containing the canonical target at position i.
    match_masks: Counter[int] = Counter()
    rooted_hist = [Counter() for _ in range(q)]
    canonical_support_labels = 0

    for label in permutations(range(2 * b)):
        Eseq = packet_sequence(label, b)
        E = frozenset(Eseq)
        if E == F:
            canonical_support_labels += 1
        overlap = len(E & F)
        mask = 0
        for i in range(q):
            if Eseq[i] == Fseq[i]:
                mask |= 1 << i
            if Fseq[i] in E:
                rooted_hist[i][overlap] += 1
        match_masks[mask] += 1

    assert canonical_support_labels == 2, (b, canonical_support_labels)

    # Theorem 2.1 for every prescribed position set.
    for t in range(1, q + 1):
        for K in combinations(range(q), t):
            required = sum(1 << i for i in K)
            actual = sum(
                count for mask, count in match_masks.items()
                if mask & required == required
            )
            expected = predicted_position_count(K, b)
            assert actual == expected, (b, K, actual, expected)

    # Rooted histograms have the exact labelled degree, are even (support
    # multiplicity two), and satisfy Theorem 3.2.
    for i, hist in enumerate(rooted_hist):
        assert sum(hist.values()) == labelled_degree, (b, i, hist)
        assert all(count % 2 == 0 for count in hist.values())

        moments: dict[int, Fraction] = {}
        for s in range(1, b + 1):
            moments[s] = Fraction(
                sum(count * comb(overlap - 1, s)
                    for overlap, count in hist.items()),
                labelled_degree,
            )

        assert moments[1] <= Fraction(12, b * b), (b, i, moments[1])
        for s in range(2, b + 1):
            rhs = (2**s) * (s + 1) * (
                A_value(b, s) + Fraction(A_value(b, s - 1), b + 1)
            )
            assert moments[s] <= rhs, (b, i, s, moments[s], rhs)

        # Check (4.2) at representative rational densities.  The bound is
        # valid algebraically even when its displayed asymptotic hypothesis
        # 8(1+z)<b is not active at these small audit ranks.
        for rho in (Fraction(1), Fraction(3, 4), Fraction(1, 2)):
            z = 1 / rho - 1
            actual_kernel = Fraction(0)
            for overlap, count in hist.items():
                actual_kernel += count * (rho ** (-(overlap - 1)) - 1)
            # Remove the two labels of the fixed simple support F.
            actual_kernel -= 2 * (rho ** (-b) - 1)
            actual_kernel /= labelled_degree

            rhs_kernel = (
                Fraction(12) * z / (b * b)
                + Fraction(1280) * z * z / (b * b)
                + 2 * b**3 * (Fraction(8) * (1 + z) / b) ** b
            )
            assert actual_kernel <= rhs_kernel, (
                b, i, rho, actual_kernel, rhs_kernel
            )

    print(
        f"PASS b={b}: labels={factorial(2*b)}, "
        f"simple_degree={labelled_degree//2}, "
        f"rooted_histograms={[dict(sorted(h.items())) for h in rooted_hist]}"
    )


def main() -> None:
    audit_symbolic_tail_bounds()
    for b in (3, 5):
        audit_b(b)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
