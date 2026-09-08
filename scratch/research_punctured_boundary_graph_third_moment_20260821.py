#!/usr/bin/env python3
"""Boundary-cut graph refinement of the exact punctured M3 counter.

For each triple T of targets in the identity punctured configuration, H_T
has the cyclic cut positions as vertices and one edge {s,s+k} for the
length-k target beginning at s.  This script records (q,c,beta) for H_T,
the two-path skeleton class, and the exact Venn-factorial codegree.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter
from fractions import Fraction

from research_punctured_configuration_third_moment_20260821 import (
    base_vertices,
    positional_signatures,
    signature,
)


def boundary_data(indices: tuple[int, int, int], r: int) -> tuple[int, int, int]:
    b = 2 * r + 1
    shore_size = b - 1
    edges = []
    for index in indices:
        length = r if index < shore_size else r - 1
        start = index % shore_size + 1
        edges.append((start, (start + length) % b))

    vertices = sorted(set(itertools.chain.from_iterable(edges)))
    parent = {vertex: vertex for vertex in vertices}

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for left, right in edges:
        union(left, right)
    q = len(vertices)
    components = len({find(vertex) for vertex in vertices})
    beta = len(edges) - q + components
    return q, components, beta


def skeleton_edges(triple: tuple[tuple[int, int], ...], r: int) -> int:
    count = 0
    for left, right in itertools.combinations(triple, 2):
        left_length, left_mask = left
        right_length, right_mask = right
        if left_length == right_length == r and left_mask & right_mask == 0:
            count += 1
        elif left_length != right_length:
            lower_mask = left_mask if left_length == r - 1 else right_mask
            middle_mask = right_mask if left_length == r - 1 else left_mask
            count += lower_mask & middle_mask == lower_mask
    return count


def analyze(r: int, compact: bool = False) -> None:
    b = 2 * r + 1
    vertices = base_vertices(r)
    patterns = ((r, r, r), (r, r, r - 1), (r, r - 1, r - 1), (r - 1,) * 3)
    positional = {pattern: positional_signatures(pattern, b) for pattern in patterns}
    degree_middle = 2 * r * math.factorial(r) * math.factorial(r + 1)

    counts: Counter[tuple[int, int, int, int, int]] = Counter()
    mass: Counter[tuple[int, int, int, int, int]] = Counter()
    max_degree: dict[tuple[int, int, int], int] = {}
    counterexample = (1, r, 1, 0, 1, 0, r - 2, 0)
    counterexample_rows = []

    for indices in itertools.combinations(range(4 * r), 3):
        triple = tuple(vertices[index] for index in indices)
        lengths = tuple(row[0] for row in triple)
        venn = signature(tuple(row[1] for row in triple), b)
        placements = positional[lengths][venn]
        labelings = math.prod(math.factorial(size) for size in venn)
        degree = placements * labelings
        lower_count = sum(length == r - 1 for length, _ in triple)
        gamma_edges = skeleton_edges(triple, r)
        q, components, beta = boundary_data(indices, r)
        key = (lower_count, gamma_edges, q, components, beta)
        counts[key] += 1
        mass[key] += degree
        hkey = (q, components, beta)
        max_degree[hkey] = max(max_degree.get(hkey, 0), degree)

        if lengths == (r, r - 1, r - 1) and venn == counterexample:
            shore_size = b - 1
            starts = tuple(index % shore_size + 1 for index in indices)
            counterexample_rows.append((starts, q, components, beta, degree))

    report = {
        "r": r,
        "counterexample": [
            {
                "starts": starts,
                "q": q,
                "c_H": components,
                "beta": beta,
                "degree_over_D_M": str(Fraction(degree, degree_middle)),
            }
            for starts, q, components, beta, degree in counterexample_rows
        ],
        "max_scaled_by_H_type": {
            str(key): str(Fraction(value * r ** (3 + key[1] - 2), degree_middle))
            for key, value in sorted(max_degree.items())
        },
        "class_table": [
            {
                "class": key,
                "target_count": counts[key],
                "mass_over_D_M": str(Fraction(mass[key], degree_middle)),
            }
            for key in sorted(counts)
        ],
    }
    if compact:
        print({
            "r": r,
            "counterexample_count": len(counterexample_rows),
            "counterexample_H_types": sorted({row[1:4] for row in counterexample_rows}),
            "H_types": sorted(max_degree),
            "max_scaled_by_H_type": report["max_scaled_by_H_type"],
        })
    else:
        print(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--compact", action="store_true")
    arguments = parser.parse_args()
    analyze(arguments.r, arguments.compact)
