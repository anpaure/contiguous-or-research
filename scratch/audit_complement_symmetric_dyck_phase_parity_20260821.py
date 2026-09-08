#!/usr/bin/env python3
"""Finite audit of the complement-symmetric Dyck-phase parity obstruction."""

from __future__ import annotations

from collections import Counter
from math import comb

from research_c8_orbit_phase_normal_form_20260821 import canonical_layers


def catalan(r):
    return comb(2 * r, r) // (r + 1)


def v2(value):
    answer = 0
    while value % 2 == 0:
        value //= 2
        answer += 1
    return answer


def audit_layers(r):
    layer, _, sizes = canonical_layers(r)
    ground = frozenset(range(1, 2 * r + 1))
    middle = r // 2
    assert all(layer[ground - target] == r - phase
               for target, phase in layer.items())
    m = catalan(r)
    assert set(sizes.values()) == {m}
    degree_zero = Counter(
        point for target, phase in layer.items() if phase == 0 for point in target
    )
    degree_middle = Counter(
        point
        for target, phase in layer.items()
        if phase == middle
        for point in target
    )
    assert degree_middle[2] == m // 2
    assert degree_zero[2] == m - catalan(r - 1)
    q = m // 2
    delta = degree_zero[2] - degree_middle[2]
    assert (q - delta) % 2 == catalan(r - 1) % 2 == 1
    return {
        "r": r,
        "Cat_r": m,
        "half": q,
        "degree_D0_at_2": degree_zero[2],
        "degree_Dhalf_at_2": degree_middle[2],
        "parity_mismatch": True,
    }


def main():
    layer_rows = [audit_layers(r) for r in (2, 4, 8)]
    arithmetic = []
    for exponent in range(1, 11):
        r = 1 << exponent
        central = comb(2 * r - 2, r - 1)
        assert v2(central) == exponent
        assert central // r == catalan(r - 1)
        assert catalan(r - 1) % 2 == 1
        arithmetic.append((r, exponent))
    print(
        "COMPLEMENT_SYMMETRIC_DYCK_PHASE_PARITY_AUDIT_PASS",
        {"literal_layers": layer_rows, "arithmetic_cases": arithmetic},
    )


if __name__ == "__main__":
    main()
