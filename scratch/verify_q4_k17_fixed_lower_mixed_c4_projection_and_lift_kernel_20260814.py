#!/usr/bin/env python3
"""Verify the fixed-rank8 unit-current graph and frozen 54-deficit cut.

Substantive execution and hashing belong on H100.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


K = 17
RANK = 8
FULL = (1 << K) - 1


def rotate(mask, shift):
    return ((mask << shift) | (mask >> (K - shift))) & FULL


def canonical(mask):
    return min(rotate(mask, shift) for shift in range(K))


def negate(mask):
    return sum(
        1 << ((-value) % K)
        for value in range(K)
        if mask >> value & 1
    )


def orbit_table():
    representatives = []
    orbit_index = {}
    for subset in itertools.combinations(range(K), RANK):
        mask = sum(1 << value for value in subset)
        if canonical(mask) == mask:
            orbit_index[mask] = len(representatives)
            representatives.append(mask)
    assert len(representatives) == 1430
    reflection = [
        orbit_index[canonical(negate(mask))] for mask in representatives
    ]
    return representatives, orbit_index, reflection


def centered_pair_set(mask):
    centered = [
        rotate(mask, shift)
        for shift in range(K)
        if negate(rotate(mask, shift)) == rotate(mask, shift)
    ]
    assert len(centered) == 1
    representative = centered[0]
    assert not (representative & 1)
    pairs = frozenset(
        value for value in range(1, 9)
        if representative >> value & 1
        and representative >> ((-value) % K) & 1
    )
    assert len(pairs) == 4
    return pairs


def quotient_neighbors(index, representatives, orbit_index):
    neighbors = set()
    for shift in range(K):
        mask = rotate(representatives[index], shift)
        inside = [value for value in range(K) if mask >> value & 1]
        outside = [value for value in range(K) if not (mask >> value & 1)]
        for deleted in inside:
            for inserted in outside:
                neighbor = (mask ^ (1 << deleted)) | (1 << inserted)
                neighbors.add(orbit_index[canonical(neighbor)])
    return neighbors


def components(vertices, edges):
    adjacency = {vertex: set() for vertex in vertices}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    result = []
    seen = set()
    for start in sorted(vertices):
        if start in seen:
            continue
        component = {start}
        stack = [start]
        seen.add(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        result.append(component)
    return adjacency, result


def cycle_order(component, adjacency):
    assert len(component) == 16
    start = min(component)
    order = [start]
    previous = None
    current = start
    while True:
        choices = sorted(adjacency[current] - ({previous} if previous is not None else set()))
        if len(order) < len(component):
            following = next(vertex for vertex in choices if vertex != start)
        else:
            assert start in choices
            break
        order.append(following)
        previous, current = current, following
    assert len(order) == 16 and set(order) == component
    return order


def minimum_projected_moves_on_cycle(target_bits):
    """Edges cost one; any residual target bit uses a singleton move."""
    size = len(target_bits)
    best = None
    for edge_mask in range(1 << size):
        boundary = [
            ((edge_mask >> ((index - 1) % size)) & 1)
            ^ ((edge_mask >> index) & 1)
            for index in range(size)
        ]
        singleton_mask = tuple(
            target_bits[index] ^ boundary[index] for index in range(size)
        )
        cost = edge_mask.bit_count() + sum(singleton_mask)
        candidate = (cost, edge_mask, singleton_mask)
        if best is None or candidate < best:
            best = candidate
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "catalogue_output", nargs="?",
        default=(
            "scratch/audit_q4_k17_nondihedral_self_fixed_lower_"
            "20260814.h100.out"
        ),
    )
    args = parser.parse_args()
    representatives, orbit_index, reflection = orbit_table()
    fixed = frozenset(
        index for index, mate in enumerate(reflection) if index == mate
    )
    assert len(fixed) == 70
    pair_sets = {
        index: centered_pair_set(representatives[index]) for index in fixed
    }

    neighbor_table = {
        index: quotient_neighbors(index, representatives, orbit_index)
        for index in fixed
    }
    fixed_edges = frozenset(
        tuple(sorted((left, right)))
        for left in fixed
        for right in neighbor_table[left] & fixed
        if left != right
    )
    fixed_loops = frozenset(
        index for index in fixed if index in neighbor_table[index]
    )
    assert len(fixed_edges) == 32
    assert len(fixed_loops) == 8
    adjacency, component_sets = components(fixed, fixed_edges)
    component_histogram = Counter(map(len, component_sets))
    assert component_histogram == Counter({1: 38, 16: 2})
    assert all(len(adjacency[index]) == (0 if len(component) == 1 else 2)
               for component in component_sets for index in component)
    intersection_histogram = Counter(
        len(pair_sets[left] & pair_sets[right]) for left, right in fixed_edges
    )
    assert intersection_histogram == Counter({0: 8, 1: 8, 2: 8, 3: 8})

    nonfixed_degree_histogram = Counter(
        len(neighbor_table[index] - fixed) for index in fixed
    )
    assert nonfixed_degree_histogram == Counter({52: 8, 66: 24, 72: 38})
    assert min(nonfixed_degree_histogram) > 0

    catalogue = json.loads(Path(args.catalogue_output).read_text())
    covered_masks = {
        mask
        for edge in catalogue["lower_fixed_edge_graph"]["one_maximum_matching"]
        for mask in edge
    }
    assert len(covered_masks) == 16
    covered = {orbit_index[mask] for mask in covered_masks}
    assert covered <= fixed
    deficit = fixed - covered
    assert len(deficit) == 54

    component_profiles = []
    cycle_certificates = []
    isolated_deficits = 0
    fixed_fixed_rank = 0
    projected_minimum = 0
    for component in component_sets:
        fixed_fixed_rank += len(component) - 1
        deficit_count = len(component & deficit)
        covered_count = len(component & covered)
        if len(component) == 1:
            if deficit_count:
                isolated_deficits += 1
                projected_minimum += 1
            component_profiles.append((1, deficit_count, covered_count))
            continue
        order = cycle_order(component, adjacency)
        target_bits = tuple(int(index in deficit) for index in order)
        cost, edge_mask, singleton_mask = minimum_projected_moves_on_cycle(
            target_bits
        )
        projected_minimum += cost
        component_profiles.append((16, deficit_count, covered_count))
        cycle_certificates.append({
            "orbit_indices": order,
            "deficit_word": "".join(map(str, target_bits)),
            "chosen_fixed_fixed_edge_word": format(edge_mask, "016b"),
            "residual_singleton_word": "".join(map(str, singleton_mask)),
            "minimum_unit_moves": cost,
        })

    assert fixed_fixed_rank == 30
    assert isolated_deficits == 30
    assert sorted(
        profile for profile in component_profiles if profile[0] == 16
    ) == [(16, 12, 4), (16, 12, 4)]
    assert projected_minimum == 46

    # Fixed-to-nonfixed unit transfers project to singleton columns e_A.
    # Since every fixed A has such a neighbor, these 70 columns give full
    # F_2 rank.  Fixed-to-fixed columns alone have the graphic rank 30.
    print(json.dumps({
        "status": "PASS",
        "rank8_translation_orbits": len(representatives),
        "fixed_bracelets": len(fixed),
        "abstract_unit_current_fixed_fixed_nonloop_edges": len(fixed_edges),
        "abstract_unit_current_fixed_self_loops": len(fixed_loops),
        "fixed_fixed_component_histogram": dict(sorted(component_histogram.items())),
        "fixed_fixed_pair_intersection_histogram": dict(
            sorted(intersection_histogram.items())
        ),
        "fixed_to_nonfixed_neighbor_degree_histogram": dict(
            sorted(nonfixed_degree_histogram.items())
        ),
        "fixed_fixed_action_rank_mod2": fixed_fixed_rank,
        "unrestricted_fixed_projection_rank_mod2": 70,
        "frozen_covered_fixed_bracelets": len(covered),
        "frozen_fixed_parity_deficits": len(deficit),
        "deficient_isolated_fixed_bracelets": isolated_deficits,
        "deficit_in_fixed_fixed_span": False,
        "minimum_abstract_unit_moves_for_fixed_projection": projected_minimum,
        "cycle_certificates": cycle_certificates,
        "scope": (
            "abstract lower-q1 unit-current projection only; occurrence, "
            "chronology, edge disjointness, and L3-kernel compatibility "
            "are not asserted"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
