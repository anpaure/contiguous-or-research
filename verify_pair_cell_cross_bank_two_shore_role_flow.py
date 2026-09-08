#!/usr/bin/env python3
"""Finite checks for the two-shore overlapping-core cross-bank theorem.

The script verifies concrete orbit-block allocations, pure-rail cross-edge
counts and signatures, the exact two-shore point ledger, the local
owner--facet incidence count, and the protected-lift residual role formulas.
It is not an integral named-order solver.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations


def pair_data(p: int) -> tuple[list[frozenset[int]], set[int], int]:
    pairs = [frozenset((2 * i, 2 * i + 1)) for i in range(p)]
    a_coordinates = {2 * i for i in range(p)}
    sentinel = 2 * p
    return pairs, a_coordinates, sentinel


def translated(items: frozenset[int], shift: int, k: int) -> frozenset[int]:
    return frozenset((item + shift) % k for item in items)


def translated_order(items: tuple[int, ...], shift: int, k: int) -> tuple[int, ...]:
    return tuple((item + shift) % k for item in items)


def xor_all(signatures: list[frozenset[int]]) -> frozenset[int]:
    answer: set[int] = set()
    for signature in signatures:
        answer.symmetric_difference_update(signature)
    return frozenset(answer)


def inspect_rail(
    p: int,
    q: int,
    core: frozenset[int],
    order: tuple[int, ...],
) -> dict[str, int]:
    pairs, a_coordinates, _ = pair_data(p)
    pair_set = set(pairs)
    n = len(order)
    assert n >= 2 * q + 2
    assert not (core & set(order))

    owners = [
        core | frozenset(order[(i + offset) % n] for offset in range(q))
        for i in range(n)
    ]
    lowers = [owners[i] & owners[(i + 1) % n] for i in range(n)]
    assert len(set(owners)) == n
    assert len(set(lowers)) == n
    assert all(len(owner) == len(core) + q for owner in owners)
    assert all(len(lower) == len(core) + q - 1 for lower in lowers)

    core_owner_load = Counter()
    core_lower_load = Counter()
    for owner in owners:
        core_owner_load.update(owner)
    for lower in lowers:
        core_lower_load.update(lower)
    for coordinate in core:
        assert core_owner_load[coordinate] == n
        assert core_lower_load[coordinate] == n
    for coordinate in order:
        assert core_owner_load[coordinate] == q
        assert core_lower_load[coordinate] == q - 1

    internal = 0
    signatures: list[frozenset[int]] = []
    eta_sum = 0
    for i in range(n):
        exchange = owners[i] ^ owners[(i + 1) % n]
        assert exchange == frozenset((order[i], order[(i + q) % n]))
        if exchange in pair_set:
            internal += 1
        signature = exchange & a_coordinates
        signatures.append(signature)
        edge_eta = (1 + len(signature)) & 1
        if exchange in pair_set:
            assert edge_eta == 0
        eta_sum ^= edge_eta
    assert internal <= n // 2
    assert xor_all(signatures) == frozenset()
    assert eta_sum == (n & 1)

    for owner in owners:
        contained = sum(lower < owner for lower in lowers)
        assert contained == 2

    return {
        "period": n,
        "internal_edges": internal,
        "cross_edges": n - internal,
        "cross_lower_bound": (n + 1) // 2,
        "eta_sum_mod_2": eta_sum,
        "lower_facets_per_owner_inside_rail": 2,
    }


def gray_lift(p: int) -> tuple[set[frozenset[int]], set[frozenset[int]]]:
    gray = [t ^ (t >> 1) for t in range(1 << p)]
    lowers = [frozenset(2 * i + ((word >> i) & 1) for i in range(p)) for word in gray]
    owners = [lowers[i] | lowers[(i + 1) % len(lowers)] for i in range(len(lowers))]
    assert len(set(lowers)) == 1 << p
    assert len(set(owners)) == 1 << p
    return set(lowers), set(owners)


def verify_case(p: int, q: int) -> dict[str, object]:
    k = 2 * p + 1
    r = p + 1
    c = r - q
    width = math.comb(k, r)
    catalan = width // k
    assert catalan * k == width
    assert catalan == math.comb(2 * p, p) // (p + 1)

    n = 2 * q + 2
    assert n + 1 <= k - c
    b_blocks = catalan % n
    a_blocks = (catalan - (n + 1) * b_blocks) // n
    assert a_blocks >= 0
    assert n * a_blocks + (n + 1) * b_blocks == catalan

    weighted_core = Counter()
    support_degree = Counter()
    cross_edges = 0
    eta_total = 0
    orbit_summaries: dict[int, dict[str, int]] = {}
    for period, multiplicity in ((n, a_blocks), (n + 1, b_blocks)):
        if multiplicity == 0:
            continue
        base_core = frozenset(range(c))
        base_order = tuple(range(c, c + period))
        assert c + period <= k
        one_orbit_cross = 0
        one_orbit_eta = 0
        for shift in range(k):
            core = translated(base_core, shift, k)
            order = translated_order(base_order, shift, k)
            summary = inspect_rail(p, q, core, order)
            one_orbit_cross += summary["cross_edges"]
            one_orbit_eta ^= summary["eta_sum_mod_2"]
            for coordinate in core:
                weighted_core[coordinate] += multiplicity * period
            for coordinate in order:
                support_degree[coordinate] += multiplicity
        cross_edges += multiplicity * one_orbit_cross
        if multiplicity & 1:
            eta_total ^= one_orbit_eta
        orbit_summaries[period] = {
            "blocks": multiplicity,
            "cross_edges_per_orbit_block": one_orbit_cross,
            "eta_per_orbit_block": one_orbit_eta,
        }

    assert set(weighted_core.values()) == {c * catalan}
    assert set(support_degree.values()) == {catalan}
    total_period = k * (n * a_blocks + (n + 1) * b_blocks)
    assert total_period == width
    assert cross_edges * 2 >= width
    assert eta_total == (width & 1)

    owner_point_degree = math.comb(k - 1, r - 1)
    lower_point_degree = math.comb(k - 1, r - 2)
    for coordinate in range(k):
        assert weighted_core[coordinate] + q * support_degree[coordinate] == owner_point_degree
        assert weighted_core[coordinate] + (q - 1) * support_degree[coordinate] == lower_point_degree

    expected_owner_load = Fraction(
        k * (n * a_blocks + (n + 1) * b_blocks), width
    )
    expected_lower_load = expected_owner_load
    assert expected_owner_load == expected_lower_load == 1

    protected_lowers, protected_owners = gray_lift(p)
    y = Counter()
    z = Counter()
    for owner in protected_owners:
        y.update(owner)
    for lower in protected_lowers:
        z.update(lower)
    residual_support = {
        coordinate: catalan - y[coordinate] + z[coordinate]
        for coordinate in range(k)
    }
    residual_core = {
        coordinate: c * catalan + (q - 1) * y[coordinate] - q * z[coordinate]
        for coordinate in range(k)
    }
    assert min(residual_support.values()) >= 0
    assert min(residual_core.values()) >= 0
    for coordinate in range(k):
        assert (
            residual_core[coordinate] + q * residual_support[coordinate]
            == owner_point_degree - y[coordinate]
        )
        assert (
            residual_core[coordinate] + (q - 1) * residual_support[coordinate]
            == lower_point_degree - z[coordinate]
        )
    lift_size = 1 << p
    assert sum(residual_support.values()) == width - lift_size
    assert sum(residual_core.values()) == c * (width - lift_size)

    return {
        "p": p,
        "k": k,
        "R": r,
        "q": q,
        "c": c,
        "W": width,
        "W_over_k": catalan,
        "period_blocks": {str(n): a_blocks, str(n + 1): b_blocks},
        "total_shells": k * (a_blocks + b_blocks),
        "total_period": total_period,
        "cross_edges_in_displayed_orbit_allocation": cross_edges,
        "universal_cross_lower_bound_ceiling": (width + 1) // 2,
        "eta_total_mod_2": eta_total,
        "owner_point_degree": owner_point_degree,
        "lower_point_degree": lower_point_degree,
        "weighted_core_degree": c * catalan,
        "support_degree": catalan,
        "fractional_named_owner_expectation": str(expected_owner_load),
        "fractional_named_lower_expectation": str(expected_lower_load),
        "orbit_summaries": orbit_summaries,
        "protected_lift_size": lift_size,
        "protected_residual_support_range": [
            min(residual_support.values()),
            max(residual_support.values()),
        ],
        "protected_residual_core_range": [
            min(residual_core.values()),
            max(residual_core.values()),
        ],
        "joint_complete_orbit_incident_codegree_ratio": f"2/{r}",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case",
        action="append",
        default=[],
        help="case p,q (repeatable); defaults to 5,2 and 7,3",
    )
    args = parser.parse_args()
    cases = [(5, 2), (7, 3)]
    if args.case:
        cases = [tuple(map(int, value.split(","))) for value in args.case]
    result = {
        "status": "PASS",
        "scope": (
            "finite identity checks for pure rails, orbit-block point roles, "
            "and protected residual targets; not an integral two-shore "
            "named-order, upper-support, residence-seam, or fusion solver"
        ),
        "cases": [verify_case(p, q) for p, q in cases],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

