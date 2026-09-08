#!/usr/bin/env python3
"""Independently audit the 256 fixed-edge extension certificates (H100 only)."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    owner_orbits,
    rotate_mask,
)


def negate_mask(mask):
    result = 0
    for value in range(K):
        if mask >> value & 1:
            result |= 1 << ((-value) % K)
    return result


def normalized_pair_set(mask):
    centered = tuple(
        rotate_mask(mask, shift)
        for shift in range(K)
        if negate_mask(rotate_mask(mask, shift)) == rotate_mask(mask, shift)
    )
    if len(centered) != 1:
        return None
    representative = centered[0]
    if not (representative & 1):
        return None
    pairs = frozenset(
        value for value in range(1, 9)
        if representative >> value & 1
        and representative >> ((-value) % K) & 1
    )
    return pairs if len(pairs) == 4 else None


def histogram(values):
    return {str(key): value for key, value in sorted(Counter(values).items())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate_output", nargs="?",
        default=(
            "scratch/verify_q4_k17_nondihedral_edges_extend_"
            "strong_matching_all_subsets_20260814.h100.out"
        ),
    )
    parser.add_argument(
        "frozen_catalogue_output", nargs="?",
        default=(
            "scratch/audit_q4_k17_nondihedral_self_fixed_lower_"
            "20260814.h100.out"
        ),
    )
    args = parser.parse_args()
    report = json.loads(Path(args.certificate_output).read_text())
    catalogue = json.loads(Path(args.frozen_catalogue_output).read_text())

    new_edges = tuple(
        tuple(sorted(edge))
        for edge in catalogue["new_fixed_face_completion"][
            "new_nondihedral_edges"
        ]
    )
    assert len(new_edges) == 8
    assert len({vertex for edge in new_edges for vertex in edge}) == 16

    representatives, _ = owner_orbits()
    pair_sets = {
        index: pairs
        for index, mask in enumerate(representatives)
        if (pairs := normalized_pair_set(mask)) is not None
    }
    assert len(pair_sets) == 70
    vertices = frozenset(pair_sets)
    strong_edges = frozenset(
        tuple(sorted((left, right)))
        for left, right in itertools.combinations(sorted(vertices), 2)
        if len(pair_sets[left] & pair_sets[right]) == 2
    )
    assert len(strong_edges) == 1260
    assert all(len(pair_sets[left] & pair_sets[right]) == 3
               for left, right in new_edges)

    expected_by_size = defaultdict(lambda: {
        "vertices": [],
        "edges": [],
        "minimum_degrees": [],
        "matching_sizes": [],
    })
    all_certificates = report["all_subset_certificates"]
    assert set(all_certificates) == {str(mask) for mask in range(256)}

    for mask in range(256):
        certificate = all_certificates[str(mask)]
        selected_indices = tuple(
            index for index in range(8) if mask >> index & 1
        )
        assert certificate["nondihedral_edge_indices"] == list(selected_indices)
        selected = tuple(new_edges[index] for index in selected_indices)
        removed = {vertex for edge in selected for vertex in edge}
        remaining = vertices - removed

        completion = tuple(
            tuple(sorted(edge)) for edge in certificate["strong_completion"]
        )
        assert len(completion) == 35 - len(selected_indices)
        assert len(set(completion)) == len(completion)
        assert all(edge in strong_edges for edge in completion)
        assert all(left in remaining and right in remaining
                   for left, right in completion)
        completion_vertices = [vertex for edge in completion for vertex in edge]
        assert len(completion_vertices) == len(set(completion_vertices))
        assert set(completion_vertices) == set(remaining)

        residual_edges = tuple(
            edge for edge in strong_edges
            if edge[0] in remaining and edge[1] in remaining
        )
        degree = Counter()
        for left, right in residual_edges:
            degree[left] += 1
            degree[right] += 1
        minimum_degree = min(degree.get(vertex, 0) for vertex in remaining)
        size = len(selected_indices)
        expected_by_size[size]["vertices"].append(len(remaining))
        expected_by_size[size]["edges"].append(len(residual_edges))
        expected_by_size[size]["minimum_degrees"].append(minimum_degree)
        expected_by_size[size]["matching_sizes"].append(len(completion))

    for size in range(9):
        row = report["by_subset_size"][str(size)]
        expected = expected_by_size[size]
        assert row["subsets"] == len(tuple(itertools.combinations(range(8), size)))
        assert row["residual_vertex_histogram"] == histogram(expected["vertices"])
        assert row["residual_edge_histogram"] == histogram(expected["edges"])
        assert row["residual_min_degree_histogram"] == histogram(
            expected["minimum_degrees"]
        )
        assert row["strong_matching_size_histogram"] == histogram(
            expected["matching_sizes"]
        )
        sample = row["one_certificate"]
        sample_mask = sample["subset_mask"]
        assert sample["strong_completion"] == all_certificates[str(sample_mask)][
            "strong_completion"
        ]
        assert sample["combined_size"] == 35
        assert sample["covers_all_fixed_vertices"] is True

    assert report["status"] == "PASS"
    assert report["fixed_vertices"] == 70
    assert report["strong_distance_two_edges"] == 1260
    assert report["nondihedral_distance_one_edges"] == 8
    assert report["subsets_checked"] == 256
    assert report["every_subset_extends_to_perfect_mixed_matching"] is True
    print(json.dumps({
        "status": "PASS",
        "method": (
            "independent literal validation of every perfect-matching "
            "certificate; no matching algorithm used"
        ),
        "fixed_vertices": len(vertices),
        "strong_edges": len(strong_edges),
        "nondihedral_edges": len(new_edges),
        "subsets_checked": len(all_certificates),
        "all_certificates_cover_every_vertex_exactly_once": True,
        "reported_histograms_recomputed_exactly": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
