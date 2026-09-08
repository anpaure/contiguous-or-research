#!/usr/bin/env python3
"""Exact H100 audit for persistent-alternating half-step retirement."""

from __future__ import annotations

import math
from fractions import Fraction


def C(b: int, r: int) -> int:
    return math.comb(b, r) if 0 <= r <= b else 0


def masses(b: int, r: int, u: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    E = C(b, r + u) * C(b, r - u)
    ae = Fraction(E * (b - r - u), b - 2 * u)
    be = Fraction(E * (r - u), b - 2 * u)
    ao = Fraction(E * (b - r - u), b + 2 * u + 1)
    bo = Fraction(E * (r - u), b + 2 * u + 1)
    return ae, be, ao, bo


def audit_boolean_identities() -> int:
    checks = 0
    for b in range(9, 122, 2):
        for u in range(0, min(12, (b - 3) // 2)):
            for r in range(u + 1, b - u):
                ae, be, ao, bo = masses(b, r, u)
                E = C(b, r + u) * C(b, r - u)
                assert ae + be == E
                prev_ao = masses(b, r - 1, u)[2]
                assert bo + prev_ao == C(b, r + u) * C(b, r - u - 1)
                if u + 1 < min(r, b - r):
                    nae, nbe, _, _ = masses(b, r, u + 1)
                    assert ae >= ao >= nae
                    assert be >= bo >= nbe
                checks += 1

            even_total = sum(C(b, r + u) * C(b, r - u) for r in range(u, b - u + 1))
            assert even_total == C(2 * b, b + 2 * u)
            odd_total = sum(
                masses(b, r, u)[2] + masses(b, r, u)[3]
                for r in range(u, b - u + 1)
            )
            assert odd_total == C(2 * b, b + 2 * u + 1)
            checks += 2
    return checks


def word(b: int, r: int) -> list[int]:
    m = (b - 1) // 2
    return [int((m * x) % b < r) for x in range(b)]


def persistent_phases(b: int, r: int, H: int) -> dict[int, list[int]]:
    bits = word(b, r)
    out = {0: [], 1: []}
    for p in range(b):
        seq = [bits[(p + q) % b] for q in range(1, H + 1)]
        if all(seq[j] != seq[j - 1] for j in range(1, H)):
            out[seq[0]].append(p)
    return out


def audit_persistent_counts() -> int:
    checks = 0
    for b in range(17, 130, 2):
        for H in range(1, min(12, b // 4) + 1):
            for r in range(1, b):
                d = abs(2 * r - b)
                n = (b - d - H + 2) // 2
                if n < 0:
                    continue
                pp = persistent_phases(b, r, H)
                assert len(pp[0]) >= n
                assert len(pp[1]) >= n
                if H >= 2:
                    expected = max(0, b - d - H + 2)
                    assert len(pp[0]) + len(pp[1]) == expected
                    assert abs(len(pp[0]) - len(pp[1])) <= 1
                checks += 1
    return checks


def audit_hypergeometric_moment_and_tail() -> int:
    checks = 0
    for b in range(9, 194, 2):
        W = C(2 * b, b)
        second = sum(C(b, r) ** 2 * (2 * r - b) ** 2 for r in range(b + 1))
        assert Fraction(second, W) == Fraction(b * b, 2 * b - 1)
        tail = sum(
            C(b, r) ** 2
            for r in range(b + 1)
            if abs(2 * r - b) > Fraction(b, 16)
        )
        assert Fraction(tail, W) <= Fraction(256, 2 * b - 1)
        checks += 2
    return checks


def audit_clamped_lp_and_bounds() -> tuple[int, list[tuple[int, int, float]]]:
    checks = 0
    rows_out: list[tuple[int, int, float]] = []
    for b, H in [(65, 4), (97, 6), (129, 8), (193, 12), (257, 16)]:
        assert H <= b // 16
        loads: list[dict[int, Fraction]] = [dict() for _ in range(H + 1)]
        objective = Fraction(0)
        unclamped = Fraction(0)
        source_bound = Fraction(0)
        omitted_L = sum(
            C(b, r) ** 2
            for r in range(b + 1)
            if abs(2 * r - b) > Fraction(b, 16)
        )

        for r in range(b + 1):
            d = abs(2 * r - b)
            if d > Fraction(b, 16):
                continue
            L = C(b, r) ** 2
            n = (b - d - H + 2) // 2
            assert n > 0
            cap = Fraction(n * L, b)
            pp = persistent_phases(b, r, H)
            chosen = {epsilon: pp[epsilon][:n] for epsilon in (0, 1)}
            assert all(len(chosen[e]) == n for e in (0, 1))

            branch_excess = Fraction(0)
            previous = {0: None, 1: None}
            for q in range(1, H + 1):
                if q % 2:
                    u = (q - 1) // 2
                    ae, be, ao, bo = masses(b, r, u)
                    natural = {1: ao, 0: bo}
                    profiles = {1: r + u + 1, 0: r + u}
                else:
                    u = q // 2
                    ae, be, ao, bo = masses(b, r, u)
                    natural = {1: ae, 0: be}
                    profiles = {1: r + u, 0: r + u}

                for epsilon in (0, 1):
                    clamped = min(natural[epsilon], cap)
                    if previous[epsilon] is not None:
                        assert clamped <= previous[epsilon]
                    previous[epsilon] = clamped
                    per_phase = clamped / n
                    assert per_phase <= Fraction(L, b)
                    # Literal selected paths have the claimed ideal profile.
                    bits = word(b, r)
                    for p in chosen[epsilon]:
                        s = r + sum(bits[(p + j) % b] for j in range(1, q + 1))
                        assert s == profiles[epsilon]
                    s = profiles[epsilon]
                    loads[q][s] = loads[q].get(s, Fraction(0)) + clamped
                    objective += clamped
                    unclamped += natural[epsilon]
                    branch_excess += natural[epsilon] - clamped
                    checks += 1

            Delta = d + H
            assert cap >= Fraction((b - d - H + 1) * L, 2 * b)
            max0 = Fraction((b + d) * L, 2 * b)
            assert max0 - cap <= Fraction(Delta * L, b)

            # Exact versions of the duration and aggregate clamp estimates.
            positive_us = {0: set(), 1: set()}
            exact_source_excess = Fraction(0)
            for u in range(0, (H + 1) // 2 + 1):
                ae, be, ao, bo = masses(b, r, u)
                for epsilon, ev, ov in ((1, ae, ao), (0, be, bo)):
                    displayed_even = 1 <= 2 * u <= H
                    displayed_odd = 2 * u + 1 <= H
                    if (displayed_even and ev > cap) or (displayed_odd and ov > cap):
                        positive_us[epsilon].add(u)
                    if displayed_even:
                        exact_source_excess += max(Fraction(0), ev - cap)
                    if displayed_odd:
                        exact_source_excess += max(Fraction(0), ov - cap)
            assert all(len(v) <= 6 * math.sqrt(Delta + 1) for v in positive_us.values())
            assert branch_excess == exact_source_excess
            bound = Fraction(24 * L, b) * math.ceil((Delta + 1) ** 1.5)
            assert branch_excess <= bound
            source_bound += bound
            checks += 5

        for q in range(1, H + 1):
            for s, value in loads[q].items():
                quota = C(b, s) * C(b, s - q)
                assert value <= quota
                checks += 1

        assert unclamped - objective <= source_bound
        full_quota = sum(C(2 * b, b + q) for q in range(1, H + 1))
        deficit = Fraction(full_quota) - objective
        assert deficit >= 0
        assert deficit <= source_bound + H * omitted_L
        assert Fraction(H * omitted_L, C(2 * b, b)) <= Fraction(256 * H, 2 * b - 1)
        rows_out.append((b, H, float(deficit / C(2 * b, b))))
    return checks, rows_out


def audit_decay_kernel() -> int:
    checks = 0
    for b in range(65, 514, 2):
        H = b // 16
        for r in range(b + 1):
            d = abs(2 * r - b)
            if d > Fraction(b, 16):
                continue
            L = C(b, r) ** 2
            for u in range(2, min(H // 2, math.isqrt(b)) + 1):
                E = C(b, r + u) * C(b, r - u)
                for f0_num, fu_num in ((b - r, b - r - u), (r, r - u)):
                    initial = Fraction(f0_num * L, b)
                    later = Fraction(fu_num * E, b - 2 * u)
                    assert initial - later >= Fraction(u * u * L, 16 * b)
                    checks += 1
    return checks


def main() -> None:
    identity_checks = audit_boolean_identities()
    phase_checks = audit_persistent_counts()
    moment_checks = audit_hypergeometric_moment_and_tail()
    decay_checks = audit_decay_kernel()
    lp_checks, rows = audit_clamped_lp_and_bounds()
    print("PERSISTENT_ALTERNATING_RETIREMENT_ROWS", rows)
    print(
        "PERSISTENT_ALTERNATING_RETIREMENT_AUDIT_PASS",
        {
            "identities": identity_checks,
            "phase_counts": phase_checks,
            "moment_and_tail": moment_checks,
            "decay": decay_checks,
            "lp_and_bounds": lp_checks,
        },
    )


if __name__ == "__main__":
    main()
