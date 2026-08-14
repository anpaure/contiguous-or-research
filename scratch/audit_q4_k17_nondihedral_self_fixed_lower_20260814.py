#!/usr/bin/env python3
"""Replay and multiplier-expand the fixed-lower nondihedral q4 census.

Substantive execution belongs on H100.  This wrapper checks every retained
witness against the literal column constructor, takes the complete Z_17^*
closure, and computes the fixed-owner and fixed-lower edge graphs.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

import search_q4_k17_twisted_reflection_self_columns_20260814 as base
import search_q4_k17_z17_reflection_invariant_owner_cover_20260814 as strong
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
    rotate_mask,
    subset_mask,
)


def multiply_mask(mask, multiplier):
    result = 0
    for value in range(K):
        if mask >> value & 1:
            result |= 1 << ((multiplier * value) % K)
    return result


def multiply_necklace(mask, multiplier):
    return canonical_orbit_mask(multiply_mask(mask, multiplier))


def multiply_deck(deck, multiplier):
    return tuple(sorted(multiply_necklace(mask, multiplier) for mask in deck))


def reflected_deck(deck):
    return tuple(sorted(base.reflected_orbit(mask) for mask in deck))


def fixed_edge(deck):
    fixed = tuple(sorted(mask for mask in deck if base.fixed_necklace(mask)))
    assert len(fixed) == 2
    return fixed


def fixed_owner_pair_set(mask):
    """Normalize a fixed rank-nine necklace and return its four pair IDs."""
    literal = [
        rotate_mask(mask, shift)
        for shift in range(K)
        if base.negate_mask(rotate_mask(mask, shift)) == rotate_mask(mask, shift)
    ]
    assert len(literal) == 1
    representative = literal[0]
    assert representative >> 0 & 1
    pairs = frozenset(
        pair for pair in range(1, 9)
        if representative >> pair & 1
        and representative >> ((-pair) % K) & 1
    )
    assert len(pairs) == 4
    return pairs


def replay_row(core, order):
    core = tuple(core)
    order = tuple(order)
    core_mask = subset_mask(core)
    owners_physical = deck_masks(core, order)
    owners = tuple(map(canonical_orbit_mask, owners_physical))
    assert len(set(owners)) == 10
    owner_permutation = base.induced_permutation(owners)
    assert owner_permutation is not None
    lowers_physical = tuple(
        core_mask | subset_mask(
            order[(start + offset) % 10] for offset in (1, 2, 3)
        )
        for start in range(10)
    )
    lowers = tuple(map(canonical_orbit_mask, lowers_physical))
    assert len(set(lowers)) == 10
    lower_permutation = base.induced_permutation(lowers)
    shifts = []
    for start, owner in enumerate(owners_physical):
        shift = base.shift_to(
            base.negate_mask(owner), owners_physical[owner_permutation[start]]
        )
        assert shift is not None
        shifts.append(shift)
    return {
        "owner_orbits": list(owners),
        "lower_orbits": list(lowers),
        "owner_permutation": list(owner_permutation),
        "lower_permutation": (
            None if lower_permutation is None else list(lower_permutation)
        ),
        "owner_action": base.dihedral_name(owner_permutation),
        "lower_action": (
            None if lower_permutation is None else base.dihedral_name(lower_permutation)
        ),
        "fixed_owner_rows": sum(base.fixed_necklace(row) for row in owners),
        "fixed_lower_rows": sum(base.fixed_necklace(row) for row in lowers),
        "owner_translation_twist": shifts,
        "constant_owner_translation": len(set(shifts)) == 1,
    }


def graph_report(universe, edges):
    graph = nx.Graph()
    graph.add_nodes_from(universe)
    graph.add_edges_from(edges)
    matching = nx.algorithms.matching.max_weight_matching(
        graph, maxcardinality=True
    )
    components = Counter(len(component) for component in nx.connected_components(graph))
    degrees = Counter(dict(graph.degree()).values())
    return {
        "vertices": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "nonisolated_vertices": sum(degree > 0 for _, degree in graph.degree()),
        "maximum_matching": len(matching),
        "unmatched_vertices_at_maximum": graph.number_of_nodes() - 2 * len(matching),
        "degree_histogram": {str(key): value for key, value in sorted(degrees.items())},
        "component_size_histogram": {
            str(key): value for key, value in sorted(components.items())
        },
        "one_maximum_matching": sorted(sorted(edge) for edge in matching),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "primary_output",
        nargs="?",
        default="scratch/search_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out",
    )
    parser.add_argument(
        "--matching-output",
        default="scratch/search_q4_k17_z17_reflection_matching_faces_20260814.h100.out",
    )
    args = parser.parse_args()
    data = json.loads(Path(args.primary_output).read_text())

    assert data["status"] == "PASS"
    assert data["multiplier_normalization"]["all_fixed_lower_masks"] == 70
    assert data["multiplier_normalization"]["multiplier_orbits"] == 10
    assert sorted(data["multiplier_normalization"]["orbit_sizes"]) == [2, 4] + [8] * 8
    assert data["multiplier_normalization"]["representative_tasks"] == 560
    assert data["counts"]["owner_self"] == 8
    assert data["unique_quotient_self_columns"] == 4
    assert len(data["examples"]) == 4

    # Rebuild the multiplier orbit reduction without using the primary
    # search implementation.
    fixed_masks = frozenset(base.fixed_literal_lower_masks())
    unseen = set(fixed_masks)
    multiplier_orbits = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset(multiply_mask(seed, a) for a in range(1, K))
        assert orbit <= fixed_masks
        multiplier_orbits.append(orbit)
        unseen -= orbit
    assert len(multiplier_orbits) == 10
    assert sorted(map(len, multiplier_orbits)) == [2, 4] + [8] * 8

    normalized = {}
    for row in data["examples"]:
        replay = replay_row(row["core"], row["order"])
        for key in (
            "owner_orbits",
            "lower_orbits",
            "owner_permutation",
            "lower_permutation",
            "owner_action",
            "lower_action",
            "fixed_owner_rows",
            "fixed_lower_rows",
            "owner_translation_twist",
            "constant_owner_translation",
        ):
            assert replay[key] == row[key]
        assert row["fixed_owner_rows"] == row["fixed_lower_rows"] == 2
        assert row["owner_action"] == "nondihedral"
        assert row["lower_action"] is None
        assert not row["constant_owner_translation"]
        key = (
            tuple(sorted(row["owner_orbits"])),
            tuple(sorted(row["lower_orbits"])),
        )
        normalized[key] = row
    assert len(normalized) == 4

    typed = {}
    for owners, lowers in normalized:
        for multiplier in range(1, K):
            key = (
                multiply_deck(owners, multiplier),
                multiply_deck(lowers, multiplier),
            )
            typed[key] = True

    by_owner = defaultdict(set)
    joint_edges = set()
    owner_edges = set()
    lower_edges = set()
    for owners, lowers in typed:
        owner_edge = fixed_edge(owners)
        lower_edge = fixed_edge(lowers)
        owner_edges.add(owner_edge)
        lower_edges.add(lower_edge)
        joint_edges.add((owner_edge, lower_edge))
        by_owner[owners].add(lowers)
        assert reflected_deck(owners) == owners
        assert reflected_deck(lowers) != lowers

    # Each lower-asymmetric realization has its reflected mate with the
    # identical owner deck.  Taking that mate would duplicate all owners.
    owner_fibre_histogram = Counter(len(fibre) for fibre in by_owner.values())
    assert set(owner_fibre_histogram) == {2}
    for owners, lower_fibre in by_owner.items():
        assert len(lower_fibre) == 2
        first, second = tuple(lower_fibre)
        assert reflected_deck(first) == second
        assert reflected_deck(second) == first

    fixed_lower_universe = {
        canonical_orbit_mask(mask) for mask in base.fixed_literal_lower_masks()
    }
    full_mask = (1 << K) - 1
    fixed_owner_universe = {
        canonical_orbit_mask(full_mask ^ mask)
        for mask in base.fixed_literal_lower_masks()
    }
    assert len(fixed_owner_universe) == len(fixed_lower_universe) == 70
    assert all(base.fixed_necklace(mask) for mask in fixed_owner_universe)
    assert all(base.fixed_necklace(mask) for mask in fixed_lower_universe)

    owner_graph = graph_report(fixed_owner_universe, owner_edges)
    lower_graph = graph_report(fixed_lower_universe, lower_edges)

    # Compare the eight new owner decks against the frozen strong-self
    # catalogue and the sample-zero fixed matching used by the live master.
    representatives, orbit_index = owner_orbits()
    reflection = strong.reflection_action(representatives, orbit_index)
    strong_columns, strong_raw, strong_simple = strong.enumerate_strong_self_columns(
        orbit_index, reflection
    )
    strong_decks = {tuple(candidate["edge"]) for candidate in strong_columns}
    strong_fixed_edges = {
        tuple(sorted(vertex for vertex in candidate["edge"]
                     if reflection[vertex] == vertex))
        for candidate in strong_columns
    }
    assert len(strong_fixed_edges) == 1260
    candidate_owner_decks_indexed = {
        tuple(sorted(orbit_index[mask] for mask in owners))
        for owners in by_owner
    }
    candidate_owner_edges_indexed = {
        tuple(sorted(orbit_index[mask] for mask in edge))
        for edge in owner_edges
    }
    matching_data = json.loads(Path(args.matching_output).read_text())
    sample_zero_matching = {
        tuple(sorted(edge)) for edge in matching_data["samples"][0]["matching"]
    }
    assert len(sample_zero_matching) == 35
    strong_overlap = candidate_owner_decks_indexed & strong_decks
    matching_overlap = candidate_owner_edges_indexed & sample_zero_matching

    candidate_endpoints = {
        vertex for edge in candidate_owner_edges_indexed for vertex in edge
    }
    assert len(candidate_endpoints) == 16
    residual_strong_graph = nx.Graph()
    fixed_owner_indices = {
        orbit_index[mask] for mask in fixed_owner_universe
    }
    residual_strong_graph.add_nodes_from(fixed_owner_indices - candidate_endpoints)
    residual_strong_graph.add_edges_from(
        edge for edge in strong_fixed_edges
        if not (set(edge) & candidate_endpoints)
    )
    strong_completion = nx.algorithms.matching.max_weight_matching(
        residual_strong_graph, maxcardinality=True
    )
    combined_matching = set(candidate_owner_edges_indexed) | {
        tuple(sorted(edge)) for edge in strong_completion
    }
    intersection_histogram = Counter(
        len(fixed_owner_pair_set(left) & fixed_owner_pair_set(right))
        for left, right in owner_edges
    )

    print(json.dumps({
        "status": "PASS",
        "normalized_distinct_owner_lower_typed_columns": len(normalized),
        "multiplier_expanded_owner_lower_typed_columns": len(typed),
        "distinct_owner_decks": len(by_owner),
        "owner_deck_lower_fibre_histogram": {
            str(key): value for key, value in sorted(owner_fibre_histogram.items())
        },
        "distinct_fixed_owner_edges": len(owner_edges),
        "distinct_fixed_lower_edges": len(lower_edges),
        "distinct_joint_edge_pairs": len(joint_edges),
        "owner_fixed_edge_graph": owner_graph,
        "lower_fixed_edge_graph": lower_graph,
        "strong_self_comparison": {
            "raw_strong_orders": strong_raw,
            "quotient_simple_strong_orders": strong_simple,
            "distinct_strong_owner_decks": len(strong_decks),
            "strong_fixed_edges": len(strong_fixed_edges),
            "candidate_edges_in_strong_fixed_edge_graph": len(
                candidate_owner_edges_indexed & strong_fixed_edges
            ),
            "candidate_owner_decks_already_strong": len(strong_overlap),
            "genuinely_new_candidate_owner_decks": (
                len(candidate_owner_decks_indexed) - len(strong_overlap)
            ),
            "sample_zero_matching_edges": len(sample_zero_matching),
            "candidate_edges_in_sample_zero_matching": len(matching_overlap),
            "matching_overlap_edges": sorted(matching_overlap),
        },
        "new_fixed_face_completion": {
            "new_edge_pair_intersection_histogram": {
                str(key): value for key, value in sorted(intersection_histogram.items())
            },
            "new_nondihedral_edges": sorted(candidate_owner_edges_indexed),
            "removed_fixed_vertices": len(candidate_endpoints),
            "residual_strong_vertices": residual_strong_graph.number_of_nodes(),
            "residual_strong_edges": residual_strong_graph.number_of_edges(),
            "residual_strong_maximum_matching": len(strong_completion),
            "strong_completion_matching": sorted(
                sorted(edge) for edge in strong_completion
            ),
            "combined_matching_size": len(combined_matching),
            "combined_matching_is_perfect": (
                len(combined_matching) == 35
                and len({vertex for edge in combined_matching for vertex in edge}) == 70
            ),
        },
        "scope": (
            "complete multiplier closure of the normalized owner/lower typed "
            "columns; counts do not distinguish physical rails having the "
            "same owner and lower decks"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
