#!/usr/bin/env python3
"""Exact checks for the symmetrized convex-profile fractional cover.

The symmetric-group orbit is not enumerated: transitivity says that its
ordinary incidence at a rank is the distinct rank count of one actual pair,
divided by the rank size.  All arithmetic is Fraction/integer arithmetic.
"""

from collections import Counter
from fractions import Fraction as F
from math import comb


def finite_majorant(m: int, epsilon: F):
    assert m >= 3 and F(0) < epsilon < 1
    b = [F(comb(2 * m, m + j)) for j in range(m + 1)] + [F(0), F(0)]
    central = b[0]
    height = (1 + epsilon) * central
    inflection = min(j for j in range(m) if 2 * (j + 1) ** 2 >= m + 1)
    slope = min((height - b[j]) / j for j in range(1, inflection + 2))
    line = lambda j: height - slope * j
    assert line(m) < 0  # finite hypothesis, eventually true at fixed epsilon
    crossing = min(
        j for j in range(inflection + 1, m + 1) if b[j] >= line(j)
    )
    g = [line(j) if j < crossing else b[j] for j in range(m + 1)]
    g += [F(0), F(0)]
    assert all(g[j] >= b[j] for j in range(m + 1))
    assert all(g[j] >= g[j + 1] for j in range(m + 1))
    assert all(g[j] - 2 * g[j + 1] + g[j + 2] >= 0 for j in range(m + 1))
    weights = [F(0)] + [
        g[a - 1] - 2 * g[a] + g[a + 1] for a in range(1, m + 2)
    ]
    assert all(x >= 0 for x in weights)
    for j in range(m + 1):
        assert sum(weights[a] * (a - j) for a in range(j + 1, m + 2)) == g[j]
    assert sum(F(a) * weights[a] for a in range(1, m + 2)) == g[0]
    return b, g, weights, inflection, crossing


def symmetric_chain(offset: int, support_size: int, length: int):
    assert 1 <= length <= support_size + 1
    assert (support_size - length + 1) % 2 == 0
    bottom = (support_size - length + 1) // 2
    value = sum(1 << (offset + i) for i in range(bottom))
    out = [value]
    for i in range(bottom, bottom + length - 1):
        value |= 1 << (offset + i)
        out.append(value)
    assert len(out) == length
    assert [x.bit_count() for x in out] == list(
        range(bottom, support_size - bottom + 1)
    )
    return out


def actual_square_pair(m: int, length: int):
    # These two splits realize both possible chain-length parities.
    p = m if (length - (m + 1)) % 2 == 0 else m - 1
    q = 2 * m - p
    left = symmetric_chain(0, p, length)
    right = symmetric_chain(p, q, length)
    rectangle = {x | y for x in left for y in right}
    assert len(rectangle) == length * length
    full = (1 << (2 * m)) - 1
    complement = {full ^ x for x in rectangle}
    intersection = rectangle & complement
    P = (1 << p) - 1
    Q = full ^ P
    if length <= m:
        assert not intersection
    else:
        assert length == m + 1
        assert intersection == {0, P, Q, full}
    indexed = Counter(x.bit_count() for x in rectangle)
    indexed.update(x.bit_count() for x in complement)
    ordinary = Counter(x.bit_count() for x in rectangle | complement)
    for rank in range(2 * m + 1):
        expected = 2 * max(0, length - abs(rank - m))
        assert indexed[rank] == expected
    return ordinary


def check_case(m: int, epsilon: F):
    b, g, weights, inflection, crossing = finite_majorant(m, epsilon)
    ordinary_rank_mass = [F(0) for _ in range(2 * m + 1)]
    for length in range(1, m + 2):
        profile = actual_square_pair(m, length)
        orbit_weight = weights[length] / 2
        for rank, count in profile.items():
            ordinary_rank_mass[rank] += orbit_weight * count

    terminal = weights[m + 1]
    assert terminal == g[m] == b[m] == 1
    # Correct the four duplicate targets in the unique maximal-chain pair.
    # A middle complementary-singleton orbit adds total incidence terminal;
    # the {empty,full} pair adds terminal/2 at each extreme.
    ordinary_rank_mass[m] += terminal
    ordinary_rank_mass[0] += terminal / 2
    ordinary_rank_mass[2 * m] += terminal / 2
    for rank in range(2 * m + 1):
        assert ordinary_rank_mass[rank] == g[abs(rank - m)]
        assert ordinary_rank_mass[rank] >= b[abs(rank - m)]

    base_charge = sum(F(a) * weights[a] for a in range(1, m + 2))
    patched_charge = base_charge + 2 * terminal
    assert base_charge == (1 + epsilon) * b[0]
    assert patched_charge == (1 + epsilon) * b[0] + 2

    # Exact tail-charge telescope used for the mesoscopic-side statement.
    for cutoff in range(m + 1):
        tail = sum(F(a) * weights[a] for a in range(cutoff + 1, m + 2))
        rhs = (cutoff + 1) * (g[cutoff] - g[cutoff + 1]) + g[cutoff + 1]
        assert tail == rhs
    return inflection, crossing, patched_charge


def check_macroscopic_calibration(m: int):
    # One disjoint centered square pair of side m, averaged over coordinates.
    b = [F(comb(2 * m, m + j)) for j in range(m + 1)]
    W = b[0]
    orbit_weight = F(W * m, 2 * (m * m - 1))
    profile = actual_square_pair(m, m)
    for rank in range(1, 2 * m):
        mass = orbit_weight * profile[rank]
        assert mass >= b[abs(rank - m)]
    required = [
        F(b[q], 2 * (m - q)) for q in range(m)
    ]
    assert max(required) == required[1]
    charge = 2 * m * orbit_weight
    assert charge == F(W * m * m, m * m - 1)


def main():
    cases = [(6, F(1, 5)), (8, F(1, 10)), (12, F(1, 10)),
             (20, F(1, 20)), (30, F(1, 50))]
    for m, epsilon in cases:
        inflection, crossing, charge = check_case(m, epsilon)
        check_macroscopic_calibration(m)
        print(
            f"m={m} epsilon={epsilon} inflection={inflection} "
            f"crossing={crossing} patched_charge={charge}"
        )
    print("VERIFIED: exact convex majorants and ordinary fractional incidences")


if __name__ == "__main__":
    main()
