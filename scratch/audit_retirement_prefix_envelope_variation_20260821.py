#!/usr/bin/env python3
"""Fail-closed audit for the retirement prefix-envelope variation lemma."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def affine_profiles(b: int, r: int, p: int, h: int) -> list[int]:
    a = (b - 1) // 2
    z = 0
    out = []
    for q in range(1, h + 1):
        z += ((a * ((p + q) % b)) % b) < r
        out.append(r + z)
    return out


def positive(x):
    return max(type(x)(0), x)


def sequence_bound(u) -> tuple:
    h = len(u)
    running = u[0]
    loss = type(u[0])(0)
    a1 = type(u[0])(0)
    a2 = type(u[0])(0)
    for q, value in enumerate(u):
        running = min(running, value)
        loss += value - running
        if q >= 1:
            a1 += positive(value - u[q - 1])
        if q >= 2:
            a2 += positive(value - u[q - 2])
    em = type(u[0])(0)
    am = type(u[0])(0)
    if h >= 2:
        mins = [min(u[q], u[q - 1]) for q in range(1, h)]
        running_min = mins[0]
        for q, value in enumerate(mins):
            running_min = min(running_min, value)
            em += value - running_min
            if q >= 1:
                am += positive(value - mins[q - 1])
    assert loss == a1 + em
    assert am <= a2
    return loss, a1, a2, em, am


def audit_abstract_bound() -> None:
    vals = [Fraction(j, 3) for j in range(4)]
    for h in range(1, 8):
        for u in itertools.product(vals, repeat=h):
            loss, a1, a2, em, am = sequence_bound(u)
            assert loss == a1 + em <= a1 + h * am <= a1 + h * a2
            isolated = all(
                not (u[q + 2] > u[q]) or u[q + 4] <= u[q]
                for q in range(h - 4)
            )
            if isolated:
                assert loss <= a1 + 2 * a2


def exact_affine_data(b: int, h: int):
    g = b // 4
    paths = []
    totals: list[dict[int, Fraction]] = [dict() for _ in range(h + 1)]
    for r in range(g, b - g + 1):
        cap = Fraction(choose(b, r) ** 2, b)
        for p in range(b):
            ss = affine_profiles(b, r, p, h)
            paths.append((cap, ss))
            for q, s in enumerate(ss, 1):
                totals[q][s] = totals[q].get(s, Fraction(0)) + cap
    rho: list[dict[int, Fraction]] = [dict() for _ in range(h + 1)]
    for q in range(1, h + 1):
        for s, total in totals[q].items():
            quota = Fraction(choose(b, s) * choose(b, s - q))
            rho[q][s] = min(Fraction(1), quota / total)
    return paths, totals, rho


def audit_small_affine() -> None:
    for b, h in [(7, 3), (11, 4), (17, 5)]:
        paths, totals, rho = exact_affine_data(b, h)
        sep_mass = Fraction(0)
        prefix_mass = Fraction(0)
        a1 = Fraction(0)
        a2 = Fraction(0)
        for cap, ss in paths:
            u = [rho[q][ss[q - 1]] for q in range(1, h + 1)]
            loss, path_a1, path_a2, _, _ = sequence_bound(u)
            sep_mass += cap * sum(u)
            prefix_mass += cap * (sum(u) - loss)
            a1 += cap * path_a1
            a2 += cap * path_a2

            running = Fraction(1)
            for q, value in enumerate(u, 1):
                running = min(running, value)
                assert 0 <= running <= 1
                s = ss[q - 1]
                # Profile feasibility is checked after path aggregation below.

        direct_prefix = Fraction(0)
        for q in range(1, h + 1):
            loads: dict[int, Fraction] = {}
            for cap, ss in paths:
                running = min(rho[j][ss[j - 1]] for j in range(1, q + 1))
                loads[ss[q - 1]] = loads.get(ss[q - 1], Fraction(0)) + cap * running
                direct_prefix += cap * running
            for s, load in loads.items():
                assert load <= choose(b, s) * choose(b, s - q)

        assert direct_prefix == prefix_mass
        assert sep_mass - prefix_mass <= a1 + h * a2
        ideal = sum(choose(2 * b, b + q) for q in range(1, h + 1))
        dsep = Fraction(ideal) - sep_mass
        dprefix = Fraction(ideal) - prefix_mass
        assert dsep <= dprefix <= dsep + a1 + h * a2


def audit_defect_mass() -> None:
    for b in range(5, 42, 2):
        a = (b - 1) // 2
        weighted = 0
        for r in range(b + 1):
            lr = choose(b, r) ** 2
            for p in range(b):
                # Any consecutive physical pair has affine ranks separated
                # by (b+1)/2.  Its 0/2 contribution count is |2r-b|.
                bits = [
                    ((a * ((p + j) % b)) % b) < r
                    for j in (1, 2)
                ]
                if sum(bits) != 1:
                    weighted += lr
            assert sum(
                sum(
                    ((a * ((p + j) % b)) % b) < r
                    for j in (1, 2)
                )
                != 1
                for p in range(b)
            ) == abs(2 * r - b)
        w = choose(2 * b, b)
        # Square the Cauchy--Schwarz claim to stay in exact integer arithmetic.
        assert weighted * weighted * (2 * b - 1) <= b * b * w * w


def exact_counterexample() -> None:
    b = 503
    h = 49
    g = b // 4
    wanted = {(47, 300): 0, (49, 302): 0}
    a = (b - 1) // 2
    for r in range(g, b - g + 1):
        lr = choose(b, r) ** 2
        bits = [((a * x) % b) < r for x in range(b)]
        for p in range(b):
            z = 0
            for q in range(1, h + 1):
                z += bits[(p + q) % b]
                key = (q, r + z)
                if key in wanted:
                    wanted[key] += lr

    rhos = {}
    for (q, s), numerator in wanted.items():
        total = Fraction(numerator, b)
        rhos[(q, s)] = min(
            Fraction(1), Fraction(choose(b, s) * choose(b, s - q), 1) / total
        )
    assert affine_profiles(b, 265, 452, 49)[46] == 300
    assert affine_profiles(b, 265, 452, 49)[48] == 302
    delta = rhos[(49, 302)] - rhos[(47, 300)]
    assert delta > 0
    assert Fraction(1714, 10_000_000) < delta < Fraction(1715, 10_000_000)
    print(
        "EXACT_TWO_STEP_COUNTEREXAMPLE",
        float(rhos[(47, 300)]),
        float(rhos[(49, 302)]),
        float(delta),
    )


def finite_diagnostics() -> None:
    # Exact arithmetic is deliberately limited to moderate instances.  These
    # rows are evidence only; no asserted asymptotic threshold depends on them.
    rows = []
    for b in [31, 61, 101]:
        h = min(b // 4, int(math.sqrt(b * math.log(b))))
        paths, _, rho = exact_affine_data(b, h)
        w = Fraction(choose(2 * b, b))
        a1 = Fraction(0)
        a2 = Fraction(0)
        envelope = Fraction(0)
        for cap, ss in paths:
            u = [rho[q][ss[q - 1]] for q in range(1, h + 1)]
            loss, path_a1, path_a2, _, _ = sequence_bound(u)
            a1 += cap * path_a1
            a2 += cap * path_a2
            envelope += cap * loss
        assert envelope <= a1 + h * a2
        rows.append((b, h, float(a1 / w), float(a2 / w), float(envelope / w)))
    print("FINITE_VARIATION_DIAGNOSTICS", rows)


def main() -> None:
    audit_abstract_bound()
    audit_small_affine()
    audit_defect_mass()
    exact_counterexample()
    finite_diagnostics()
    print("PASS retirement prefix-envelope positive-variation audit")


if __name__ == "__main__":
    main()
