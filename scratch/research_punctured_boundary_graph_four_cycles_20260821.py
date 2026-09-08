#!/usr/bin/env python3
"""Exact boundary-graph/Venn data for four-target skeleton cycles."""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter
from fractions import Fraction

from research_punctured_configuration_third_moment_20260821 import base_vertices


def signature_n(sets: tuple[int, ...], b: int) -> tuple[int, ...]:
    counts = [0] * (1 << len(sets))
    for point in range(b):
        cell = sum(((sets[j] >> point) & 1) << j for j in range(len(sets)))
        counts[cell] += 1
    return tuple(counts)


def target_start(index: int, r: int) -> int:
    return index % (2 * r) + 1


def boundary_data(indices: tuple[int, ...], r: int) -> tuple[int, int, int]:
    b = 2 * r + 1
    shore_size = b - 1
    edges = []
    for index in indices:
        length = r if index < shore_size else r - 1
        start = target_start(index, r)
        edges.append((start, (start + length) % b))
    vertices = sorted(set(itertools.chain.from_iterable(edges)))
    parent = {vertex: vertex for vertex in vertices}

    def find(vertex: int) -> int:
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    for left, right in edges:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root
    q = len(vertices)
    components = len({find(vertex) for vertex in vertices})
    return q, components, len(edges) - q + components


def skeleton_adjacent(left: tuple[int, int], right: tuple[int, int], r: int) -> bool:
    left_length, left_mask = left
    right_length, right_mask = right
    if left_length == right_length == r:
        return left_mask & right_mask == 0
    if left_length != right_length:
        lower = left_mask if left_length == r - 1 else right_mask
        middle = right_mask if left_length == r - 1 else left_mask
        return lower & middle == lower
    return False


def retained_placement_counts(
    r: int,
    needed: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], int]:
    b = 2 * r + 1
    windows = {}
    all_mask = (1 << b) - 1
    for length in (r, r - 1):
        rows = []
        for start in range(1, b):
            mask = 0
            for offset in range(length):
                mask |= 1 << ((start + offset) % b)
            rows.append(mask & all_mask)
        windows[length] = rows

    answer = {}
    for lengths, desired in needed.items():
        counts = Counter()
        for starts in itertools.product(range(b - 1), repeat=4):
            arcs = tuple(windows[lengths[j]][starts[j]] for j in range(4))
            venn = signature_n(arcs, b)
            if venn in desired:
                counts[venn] += 1
        for venn in desired:
            answer[(lengths, venn)] = counts[venn]
    return answer


def analyze(r: int) -> None:
    b = 2 * r + 1
    vertices = base_vertices(r)
    cycle_rows = []
    needed: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for indices in itertools.combinations(range(4 * r), 4):
        triple = tuple(vertices[index] for index in indices)
        adjacency = [[False] * 4 for _ in range(4)]
        for left, right in itertools.combinations(range(4), 2):
            adjacency[left][right] = adjacency[right][left] = skeleton_adjacent(
                triple[left], triple[right], r
            )
        degrees = tuple(sum(row) for row in adjacency)
        if degrees != (2, 2, 2, 2):
            continue
        lengths = tuple(row[0] for row in triple)
        venn = signature_n(tuple(row[1] for row in triple), b)
        q, components, beta = boundary_data(indices, r)
        starts = tuple(target_start(index, r) for index in indices)
        cycle_rows.append((indices, starts, lengths, venn, q, components, beta))
        needed.setdefault(lengths, set()).add(venn)

    placements = retained_placement_counts(r, needed)
    degree_middle = 2 * r * math.factorial(r) * math.factorial(r + 1)
    grouped = Counter()
    witnesses = {}
    for _, starts, lengths, venn, q, components, beta in cycle_rows:
        labelings = math.prod(math.factorial(size) for size in venn)
        degree = placements[(lengths, venn)] * labelings
        key = (lengths, q, components, beta, venn, degree)
        grouped[key] += 1
        witnesses.setdefault(key, starts)

    print({
        "r": r,
        "cycle_count": len(cycle_rows),
        "types": [
            {
                "lengths": key[0],
                "q": key[1],
                "c_H": key[2],
                "beta": key[3],
                "venn": key[4],
                "target_count": count,
                "witness_starts": witnesses[key],
                "degree_over_D_M": str(Fraction(key[5], degree_middle)),
                "scaled": str(Fraction(key[5] * r ** (4 + key[2] - 2), degree_middle)),
            }
            for key, count in sorted(grouped.items())
        ],
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    arguments = parser.parse_args()
    analyze(arguments.r)
