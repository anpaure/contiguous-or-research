#!/usr/bin/env python3
"""Verify fixed-shell order degrees/codegrees and complete-orbit formulas.

Substantive execution is H100-only.  The script exhausts cyclic orders for
small shells and materializes the complete parameterized orbit at one small
middle-layer instance.  It is not a protected fixed-bank fractional or
integral named-order solver.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter


def cyclic_orders(labels: tuple[int, ...]):
    first = labels[0]
    for rest in itertools.permutations(labels[1:]):
        yield (first,) + rest


def windows(order: tuple[int, ...], width: int) -> tuple[frozenset[int], ...]:
    size = len(order)
    return tuple(
        frozenset(order[(start + offset) % size] for offset in range(width))
        for start in range(size)
    )


def kappa(order_size: int, q: int, overlap: int) -> int:
    multiplier = order_size - 2 * q + 2 if overlap == 0 else 2
    return (
        multiplier
        * math.factorial(overlap)
        * math.factorial(q - overlap)
        * math.factorial(q - 1 - overlap)
        * math.factorial(order_size - 2 * q + 1 + overlap)
    )


def verify_fixed_shell(order_size: int, q: int) -> dict[str, object]:
    labels = tuple(range(order_size))
    owner_degree = Counter()
    lower_degree = Counter()
    owner_pairs = Counter()
    lower_pairs = Counter()
    mixed_pairs = Counter()
    order_count = 0
    for order in cyclic_orders(labels):
        order_count += 1
        owners = windows(order, q)
        lowers = windows(order, q - 1)
        assert len(set(owners)) == order_size
        assert len(set(lowers)) == order_size
        owner_degree.update(owners)
        lower_degree.update(lowers)
        owner_pairs.update(frozenset(pair) for pair in itertools.combinations(owners, 2))
        lower_pairs.update(frozenset(pair) for pair in itertools.combinations(lowers, 2))
        mixed_pairs.update((owner, lower) for owner in owners for lower in lowers)
    assert order_count == math.factorial(order_size - 1)
    expected_owner_degree = math.factorial(q) * math.factorial(order_size - q)
    expected_lower_degree = math.factorial(q - 1) * math.factorial(order_size - q + 1)
    assert set(owner_degree.values()) == {expected_owner_degree}
    assert set(lower_degree.values()) == {expected_lower_degree}

    for pair, value in owner_pairs.items():
        left, right = tuple(pair)
        delta = q - len(left & right)
        if delta < q:
            expected = (
                2
                * math.factorial(q - delta)
                * math.factorial(delta) ** 2
                * math.factorial(order_size - q - delta)
            )
        else:
            expected = (
                (order_size - 2 * q + 1)
                * math.factorial(q) ** 2
                * math.factorial(order_size - 2 * q)
            )
        assert value == expected
    for pair, value in lower_pairs.items():
        left, right = tuple(pair)
        delta = q - 1 - len(left & right)
        if delta < q - 1:
            expected = (
                2
                * math.factorial(q - 1 - delta)
                * math.factorial(delta) ** 2
                * math.factorial(order_size - q + 1 - delta)
            )
        else:
            expected = (
                (order_size - 2 * q + 3)
                * math.factorial(q - 1) ** 2
                * math.factorial(order_size - 2 * q + 2)
            )
        assert value == expected
    for (owner, lower), value in mixed_pairs.items():
        overlap = len(owner & lower)
        assert value == kappa(order_size, q, overlap)

    incident_values = {
        value for (owner, lower), value in mixed_pairs.items() if lower < owner
    }
    assert incident_values == {
        2 * math.factorial(q - 1) * math.factorial(order_size - q)
    }
    return {
        "N": order_size,
        "q": q,
        "cyclic_orders": order_count,
        "owner_degree": expected_owner_degree,
        "lower_degree": expected_lower_degree,
        "incident_owner_lower_codegree": next(iter(incident_values)),
        "incident_ratio": f"2/{q}",
        "owner_pair_types": len(set(owner_pairs.values())),
        "lower_pair_types": len(set(lower_pairs.values())),
        "mixed_overlap_types": {
            str(overlap): kappa(order_size, q, overlap) for overlap in range(q)
        },
    }


def verify_complete_orbit() -> dict[str, object]:
    p, q, order_size = 5, 2, 6
    k, rank, core_size = 2 * p + 1, p + 1, p + 1 - q
    ground = tuple(range(k))
    owner_degree = Counter()
    lower_degree = Counter()
    mixed = Counter()
    rail_count = 0
    for core_tuple in itertools.combinations(ground, core_size):
        core = frozenset(core_tuple)
        complement = tuple(x for x in ground if x not in core)
        for support_tuple in itertools.combinations(complement, order_size):
            support = tuple(support_tuple)
            for order in cyclic_orders(support):
                rail_count += 1
                owners = tuple(core | petal for petal in windows(order, q))
                lowers = tuple(core | petal for petal in windows(order, q - 1))
                owner_degree.update(owners)
                lower_degree.update(lowers)
                mixed.update((owner, lower) for owner in owners for lower in lowers)
    expected_degree = (
        math.factorial(rank)
        * math.factorial(rank - 1)
        // (
            math.factorial(core_size)
            * math.factorial(rank - 1 - order_size + q)
        )
    )
    assert set(owner_degree.values()) == {expected_degree}
    assert set(lower_degree.values()) == {expected_degree}
    incident = {
        value for (owner, lower), value in mixed.items() if lower < owner
    }
    assert incident == {2 * expected_degree // rank}
    assert len(owner_degree) == math.comb(k, rank)
    assert len(lower_degree) == math.comb(k, rank - 1)
    return {
        "p": p,
        "q": q,
        "N": order_size,
        "parameterized_rails": rail_count,
        "common_vertex_degree": expected_degree,
        "incident_owner_lower_codegree": next(iter(incident)),
        "normalized_incident_codegree": f"2/{rank}",
        "owner_vertices": len(owner_degree),
        "lower_vertices": len(lower_degree),
    }


def main() -> None:
    result = {
        "status": "PASS",
        "scope": (
            "exhaustive small-shell and complete-orbit enumeration; not a "
            "protected fixed-bank fractional or integral named-order solver"
        ),
        "fixed_shells": [verify_fixed_shell(6, 2), verify_fixed_shell(7, 3)],
        "complete_orbit": verify_complete_orbit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
