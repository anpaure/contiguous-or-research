#!/usr/bin/env python3
"""Exact all-four-target test of the boundary-codegree gate."""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter
from fractions import Fraction

from research_punctured_configuration_third_moment_20260821 import base_vertices
from research_punctured_boundary_graph_four_cycles_20260821 import (
    boundary_data,
    signature_n,
    target_start,
)


def positional_counters(r: int) -> dict[tuple[int, ...], Counter[tuple[int, ...]]]:
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    windows = {}
    for length in (r, r - 1):
        rows = []
        for start in range(1, b):
            mask = 0
            for offset in range(length):
                mask |= 1 << ((start + offset) % b)
            rows.append(mask & all_mask)
        windows[length] = rows

    answer = {}
    for lower_count in range(5):
        lengths = (r,) * (4 - lower_count) + (r - 1,) * lower_count
        counter = Counter()
        for starts in itertools.product(range(b - 1), repeat=4):
            arcs = tuple(windows[lengths[j]][starts[j]] for j in range(4))
            counter[signature_n(arcs, b)] += 1
        answer[lengths] = counter
    return answer


def analyze(r: int) -> None:
    b = 2 * r + 1
    vertices = base_vertices(r)
    positional = positional_counters(r)
    degree_middle = 2 * r * math.factorial(r) * math.factorial(r + 1)
    maxima = {}
    moment = 0

    for indices in itertools.combinations(range(4 * r), 4):
        targets = tuple(vertices[index] for index in indices)
        lengths = tuple(target[0] for target in targets)
        venn = signature_n(tuple(target[1] for target in targets), b)
        placements = positional[lengths][venn]
        labelings = math.prod(math.factorial(size) for size in venn)
        degree = placements * labelings
        moment += degree
        q, components, beta = boundary_data(indices, r)
        key = (q, components, beta)
        scaled = Fraction(degree * r ** (q - 2), degree_middle)
        if key not in maxima or scaled > maxima[key][0]:
            starts = tuple(target_start(index, r) for index in indices)
            maxima[key] = (scaled, lengths, starts, venn, degree)

    print({
        "r": r,
        "M4_over_D_M": str(Fraction(moment, degree_middle)),
        "r_M4_over_D_M": str(Fraction(r * moment, degree_middle)),
        "max_boundary_scaled": {
            str(key): {
                "r_pow_q_minus_2_degree_over_D_M": str(row[0]),
                "lengths": row[1],
                "starts": row[2],
                "venn": row[3],
                "degree_over_D_M": str(Fraction(row[4], degree_middle)),
            }
            for key, row in sorted(maxima.items())
        },
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    arguments = parser.parse_args()
    analyze(arguments.r)
