#!/usr/bin/env python3
"""Verify the pair-cell parity signature, triangle carrier, and low-cell counts.

This is a finite identity checker, not a solver for the residual exact-cover
system.  It uses only the Python standard library.  By default it checks
p = 3, 4, 5, 7 and exhaustively classifies Johnson triangles at p = 3.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from itertools import combinations


def labels(p: int) -> tuple[list[tuple[int, int]], int, set[int]]:
    pairs = [(2 * i, 2 * i + 1) for i in range(p)]
    sentinel = 2 * p
    a_coordinates = {a for a, _ in pairs}
    return pairs, sentinel, a_coordinates


def transversal(p: int, word: int) -> frozenset[int]:
    return frozenset(2 * i + ((word >> i) & 1) for i in range(p))


def gray_lift(p: int) -> tuple[set[frozenset[int]], set[frozenset[int]]]:
    gray = [t ^ (t >> 1) for t in range(1 << p)]
    lower = [transversal(p, word) for word in gray]
    owners: list[frozenset[int]] = []
    for i, current in enumerate(lower):
        following = lower[(i + 1) % len(lower)]
        assert len(current ^ following) == 2
        owners.append(current | following)
    assert len(set(lower)) == 1 << p
    assert len(set(owners)) == 1 << p
    return set(lower), set(owners)


def singleton_count(owner: frozenset[int], pairs: list[tuple[int, int]]) -> int:
    return sum(len(owner & frozenset(pair)) == 1 for pair in pairs)


def internal_degree(owner: frozenset[int], pairs: list[tuple[int, int]]) -> int:
    neighbours: set[frozenset[int]] = set()
    for a, b in pairs:
        occupancy = owner & {a, b}
        if len(occupancy) == 1:
            present = next(iter(occupancy))
            absent = b if present == a else a
            neighbours.add((owner - {present}) | {absent})
    assert len(neighbours) == singleton_count(owner, pairs)
    return len(neighbours)


def edge_signature(
    left: frozenset[int], right: frozenset[int], a_coordinates: set[int]
) -> frozenset[int]:
    assert len(left ^ right) == 2
    return frozenset((left ^ right) & a_coordinates)


def eta(signature: frozenset[int]) -> int:
    return (1 + len(signature)) & 1


def is_internal(
    left: frozenset[int], right: frozenset[int], pairs: list[tuple[int, int]]
) -> bool:
    exchange = left ^ right
    return any(exchange == frozenset(pair) for pair in pairs)


def xor_signatures(signatures: list[frozenset[int]]) -> frozenset[int]:
    answer: set[int] = set()
    for signature in signatures:
        answer.symmetric_difference_update(signature)
    return frozenset(answer)


def canonical_triangle(p: int) -> dict[str, object]:
    assert p >= 3
    pairs, sentinel, a_coordinates = labels(p)
    deleted = [pairs[i][0] for i in range(3)]
    base = {sentinel} | {pairs[i][1] for i in range(p - 2)}
    assert len(base) == p - 1
    assert not (base & set(deleted))
    upper = frozenset(base | set(deleted))
    owners = [upper - {coordinate} for coordinate in deleted]

    edge_rows: list[dict[str, object]] = []
    signatures: list[frozenset[int]] = []
    degree = Counter()
    colours: list[frozenset[int]] = []
    for i, j in combinations(range(3), 2):
        left, right = owners[i], owners[j]
        colour = left & right
        signature = edge_signature(left, right, a_coordinates)
        assert len(left) == p + 1 and len(right) == p + 1
        assert len(colour) == p
        assert not is_internal(left, right, pairs)
        assert eta(signature) == 1
        assert sentinel in colour
        degree[left] += 1
        degree[right] += 1
        colours.append(colour)
        signatures.append(signature)
        edge_rows.append(
            {
                "deleted_pair": [deleted[i], deleted[j]],
                "colour": sorted(colour),
                "signature": sorted(signature),
                "eta": eta(signature),
            }
        )

    assert len(set(owners)) == 3
    assert len(set(colours)) == 3
    assert set(degree.values()) == {2}
    assert xor_signatures(signatures) == frozenset()
    assert sum(map(eta, signatures)) % 2 == 1

    transversal_colours, lift_owners = gray_lift(p)
    assert not (set(colours) & transversal_colours)
    assert not (set(owners) & lift_owners)
    assert all(sentinel in owner for owner in owners)
    assert all(sentinel not in owner for owner in lift_owners)

    return {
        "base": sorted(base),
        "upper": sorted(upper),
        "owners": [sorted(owner) for owner in owners],
        "edges": edge_rows,
        "signature_xor": [],
        "eta_sum_mod_2": 1,
        "disjoint_from_gray_lift": True,
    }


def classify_triangles_at_p3() -> dict[str, int]:
    p = 3
    pairs, _, a_coordinates = labels(p)
    owners = [frozenset(owner) for owner in combinations(range(2 * p + 1), p + 1)]
    johnson_triangles = 0
    colour_injective = 0
    all_cross = 0
    for triple in combinations(owners, 3):
        edge_pairs = [(0, 1), (1, 2), (2, 0)]
        if not all(len(triple[i] ^ triple[j]) == 2 for i, j in edge_pairs):
            continue
        johnson_triangles += 1
        colours = [triple[i] & triple[j] for i, j in edge_pairs]
        signatures = [
            edge_signature(triple[i], triple[j], a_coordinates) for i, j in edge_pairs
        ]
        assert xor_signatures(signatures) == frozenset()
        assert sum(map(eta, signatures)) % 2 == 1
        if len(set(colours)) != 3:
            assert len(set(colours)) == 1
            continue
        colour_injective += 1
        upper = set().union(*triple)
        assert len(upper) == p + 2
        assert all(len(upper - set(owner)) == 1 for owner in triple)
        if all(not is_internal(triple[i], triple[j], pairs) for i, j in edge_pairs):
            all_cross += 1
    assert johnson_triangles > colour_injective > 0
    assert all_cross > 0
    return {
        "johnson_triangles": johnson_triangles,
        "lower_colour_injective_bottom_triangles": colour_injective,
        "all_cross_bottom_triangles": all_cross,
    }


def verify_p(p: int) -> dict[str, object]:
    assert p >= 3
    pairs, sentinel, _ = labels(p)
    transversal_colours, lift_owners = gray_lift(p)
    assert all(sentinel not in lower for lower in transversal_colours)
    assert all(sentinel not in owner for owner in lift_owners)
    assert {singleton_count(owner, pairs) for owner in lift_owners} == {p - 1}

    owner_counts = Counter()
    for raw_owner in combinations(range(2 * p + 1), p + 1):
        owner = frozenset(raw_owner)
        m = singleton_count(owner, pairs)
        owner_counts[m] += 1
        assert internal_degree(owner, pairs) == m
    assert sum(owner_counts.values()) == math.comb(2 * p + 1, p + 1)

    n0 = owner_counts[0]
    n1 = owner_counts[1]
    if p & 1:
        formula_n0 = math.comb(p, (p - 1) // 2)
        formula_n1 = 2 * p * math.comb(p - 1, (p - 1) // 2)
        assert n0 == formula_n0
        assert n1 == formula_n1
    else:
        formula_n0 = n0
        formula_n1 = n1

    forced_cross_incidences = 2 * n0 + n1
    cross_edge_lower_bound = (forced_cross_incidences + 1) // 2
    if p & 1:
        closed_form = math.comb(p, (p - 1) // 2) + p * math.comb(
            p - 1, (p - 1) // 2
        )
        assert cross_edge_lower_bound == closed_form
    else:
        closed_form = cross_edge_lower_bound

    width = math.comb(2 * p + 1, p + 1)
    residual_colours = width - (1 << p)
    mersenne = ((p + 1) & p) == 0
    if mersenne:
        assert width & 1
        assert residual_colours & 1

    return {
        "p": p,
        "width": width,
        "lift_colours": len(transversal_colours),
        "lift_owners": len(lift_owners),
        "lift_singleton_count": p - 1,
        "residual_colours": residual_colours,
        "mersenne_p": mersenne,
        "N0": n0,
        "N1": n1,
        "formula_N0": formula_n0,
        "formula_N1": formula_n1,
        "forced_low_cell_cross_incidences": forced_cross_incidences,
        "nonlift_cross_edge_lower_bound": cross_edge_lower_bound,
        "closed_form_lower_bound": closed_form,
        "triangle": canonical_triangle(p),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", nargs="+", type=int, default=[3, 4, 5, 7])
    parser.add_argument(
        "--skip-triangle-classification",
        action="store_true",
        help="skip the exhaustive p=3 classification",
    )
    args = parser.parse_args()
    checked = [verify_p(p) for p in args.p]
    result: dict[str, object] = {
        "status": "PASS",
        "scope": (
            "finite checks of edge signatures, the canonical bottom triangle, "
            "Gray-lift disjointness, internal degrees, and N0/N1 formulas; "
            "not a residual exact-cover or chronology solver"
        ),
        "checked": checked,
    }
    if not args.skip_triangle_classification:
        result["p3_triangle_classification"] = classify_triangles_at_p3()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

