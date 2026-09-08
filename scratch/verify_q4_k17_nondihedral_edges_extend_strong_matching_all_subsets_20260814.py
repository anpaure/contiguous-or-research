#!/usr/bin/env python3
"""Verify all 256 mixed fixed-edge matching faces (run only on H100)."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

from audit_q4_k17_nondihedral_self_fixed_lower_20260814 import (
    fixed_owner_pair_set,
)
from search_q4_k17_z17_quotient_exact_cover_20260814 import owner_orbits


def nested_histogram(values):
    return {str(key): value for key, value in sorted(Counter(values).items())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "audit_output", nargs="?",
        default="scratch/audit_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out",
    )
    args = parser.parse_args()
    frozen = json.loads(Path(args.audit_output).read_text())
    new_edges = tuple(
        tuple(edge)
        for edge in frozen["new_fixed_face_completion"]["new_nondihedral_edges"]
    )
    assert len(new_edges) == 8
    assert len({vertex for edge in new_edges for vertex in edge}) == 16

    representatives, _ = owner_orbits()
    # fixed_owner_pair_set is defined only on fixed necklaces.  The 70
    # vertices are exactly those occurring in the frozen audit's universe;
    # reconstruct them by testing which representatives admit the unique
    # centered form.
    pair_sets = {}
    for index, mask in enumerate(representatives):
        try:
            pairs = fixed_owner_pair_set(mask)
        except AssertionError:
            continue
        pair_sets[index] = pairs
    assert len(pair_sets) == 70
    fixed_vertices = tuple(sorted(pair_sets))

    strong_edges = tuple(
        (left, right)
        for left, right in itertools.combinations(fixed_vertices, 2)
        if len(pair_sets[left] & pair_sets[right]) == 2
    )
    assert len(strong_edges) == 1260
    assert all(len(pair_sets[left] & pair_sets[right]) == 3
               for left, right in new_edges)
    assert not (set(new_edges) & set(strong_edges))

    by_size = defaultdict(lambda: {
        "subsets": 0,
        "residual_vertices": [],
        "residual_edges": [],
        "residual_min_degrees": [],
        "strong_matching_sizes": [],
    })
    certificates = {}
    all_subset_certificates = {}
    for mask in range(1 << len(new_edges)):
        chosen = tuple(new_edges[i] for i in range(8) if mask >> i & 1)
        size = len(chosen)
        removed = {vertex for edge in chosen for vertex in edge}
        assert len(removed) == 2 * size
        remaining = set(fixed_vertices) - removed
        residual_edges = tuple(
            edge for edge in strong_edges
            if edge[0] in remaining and edge[1] in remaining
        )
        graph = nx.Graph()
        graph.add_nodes_from(remaining)
        graph.add_edges_from(residual_edges)
        minimum_degree = min(dict(graph.degree()).values())
        matching = nx.algorithms.matching.max_weight_matching(
            graph, maxcardinality=True
        )
        matching = tuple(sorted(tuple(sorted(edge)) for edge in matching))
        assert len(matching) == 35 - size
        combined = chosen + matching
        assert len(combined) == 35
        assert len({vertex for edge in combined for vertex in edge}) == 70

        row = by_size[size]
        row["subsets"] += 1
        row["residual_vertices"].append(len(remaining))
        row["residual_edges"].append(len(residual_edges))
        row["residual_min_degrees"].append(minimum_degree)
        row["strong_matching_sizes"].append(len(matching))
        all_subset_certificates[str(mask)] = {
            "nondihedral_edge_indices": [
                index for index in range(8) if mask >> index & 1
            ],
            "strong_completion": [list(edge) for edge in matching],
        }
        if size not in certificates:
            certificates[size] = {
                "subset_mask": mask,
                "nondihedral_edges": [list(edge) for edge in chosen],
                "strong_completion": [list(edge) for edge in matching],
                "combined_size": len(combined),
                "covers_all_fixed_vertices": True,
            }

    summary = {}
    for size in range(9):
        row = by_size[size]
        assert row["subsets"] == len(tuple(itertools.combinations(range(8), size)))
        summary[str(size)] = {
            "subsets": row["subsets"],
            "residual_vertex_histogram": nested_histogram(row["residual_vertices"]),
            "residual_edge_histogram": nested_histogram(row["residual_edges"]),
            "residual_min_degree_histogram": nested_histogram(
                row["residual_min_degrees"]
            ),
            "strong_matching_size_histogram": nested_histogram(
                row["strong_matching_sizes"]
            ),
            "one_certificate": certificates[size],
        }

    print(json.dumps({
        "status": "PASS",
        "fixed_vertices": len(fixed_vertices),
        "strong_distance_two_edges": len(strong_edges),
        "nondihedral_distance_one_edges": len(new_edges),
        "subsets_checked": 1 << len(new_edges),
        "every_subset_extends_to_perfect_mixed_matching": True,
        "by_subset_size": summary,
        "all_subset_certificates": all_subset_certificates,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
