#!/usr/bin/env python3
"""Exact j=2 first rootless-edge cumulant for the Gate-B defect rows."""

from __future__ import annotations

import multiprocessing as mp
import sys
import time
from collections import defaultdict
from fractions import Fraction
from math import factorial

sys.path.insert(0, "scratch")

from research_gate_b_local_atoms_fast_venn_20260822 import boundary_cell_data
from research_gate_b_targeted_local_bank_20260822 import (
    blocker_boundary_edge,
    complete_boundary_edges,
    complete_bounded_rooted_core_sets,
    grouped_puncture_rooted_core_row,
    positional_j2_polynomial_sum,
)


def one_remote_edge_sets(
    r: int, event_start: int
) -> list[tuple[tuple[int, int, int], ...]]:
    """A <=5-vertex rooted core plus one vertex-disjoint blocker edge."""
    all_edges = tuple(complete_boundary_edges(r).values())
    answer = set()
    for core in complete_bounded_rooted_core_sets(r, event_start, 5):
        core_vertices = set()
        for blocker in core:
            core_vertices.update(blocker_boundary_edge(r, blocker))
        for remote in all_edges:
            if blocker_boundary_edge(r, remote) & core_vertices:
                continue
            answer.add(tuple(sorted((*core, remote))))
    return sorted(answer)


def elementary_gap_defect(
    r: int, blocker_data: tuple[tuple[int, int, int], ...]
) -> int:
    b = 2 * r + 1
    cuts = sorted(
        {start % b for size, start, _ in blocker_data}
        | {(start + size) % b for size, start, _ in blocker_data}
    )
    gaps = sorted(
        (
            (cuts[(index + 1) % len(cuts)] - cuts[index]) % b
            for index in range(len(cuts))
        ),
        reverse=True,
    )
    return sum(gaps[2:])


def one_remote_correction_row(
    r: int, event_start: int, maximum_defect: int | None = None
) -> tuple[int, int]:
    b = 2 * r + 1
    grouped: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]], int
    ] = defaultdict(int)
    for blocker_data in one_remote_edge_sets(r, event_start):
        if (
            maximum_defect is not None
            and elementary_gap_defect(r, blocker_data) > maximum_defect
        ):
            continue
        if not any(start == 0 for _, start, _ in blocker_data):
            continue
        blocker_sizes = tuple(value[0] for value in blocker_data)
        blocker_masks = tuple(value[2] for value in blocker_data)
        cell_sizes, _, marks = boundary_cell_data(b, event_start, blocker_masks)
        grouped[(blocker_sizes, cell_sizes, marks)] += (-1) ** len(blocker_data)

    rows = []
    for root_size in (r, r - 1):
        answer = 0
        for (blocker_sizes, cell_sizes, marks), multiplicity in grouped.items():
            if not multiplicity:
                continue
            factorial_core = 1
            for cell_size, cell_marks in zip(cell_sizes, marks):
                factorial_core *= factorial(cell_size - cell_marks.bit_count())
            answer += (
                multiplicity
                * factorial_core
                * positional_j2_polynomial_sum(
                    r,
                    root_size,
                    blocker_sizes,
                    cell_sizes,
                    marks,
                )
            )
        rows.append(answer)
    return tuple(rows)


def calculate(r: int):
    started = time.time()
    degree = 2 * r * factorial(r) * factorial(r + 1)
    corrections = {}
    remote_corrections = {}
    for shift in (r, r + 1, r + 2, r + 3):
        rooted = grouped_puncture_rooted_core_row(r, 2, shift, 6)
        remote = one_remote_correction_row(r, shift)
        corrections[shift] = tuple(rooted[i] + remote[i] for i in range(2))
        remote_corrections[shift] = remote
    left = tuple(
        Fraction(corrections[r][shore] - corrections[r + 1][shore], degree)
        for shore in range(2)
    )
    right = tuple(
        Fraction(corrections[r + 2][shore] - corrections[r + 3][shore], degree)
        for shore in range(2)
    )
    determinant = left[0] * right[1] - left[1] * right[0]
    return r, time.time() - started, left, right, determinant


def main() -> None:
    values = [int(value) for value in sys.argv[1:]] or [15, 20, 30, 40]
    context = mp.get_context("fork")
    with context.Pool(min(6, len(values))) as pool:
        for r, seconds, left, right, determinant in pool.imap_unordered(
            calculate, values
        ):
            print(
                r,
                "seconds",
                round(seconds, 3),
                "left*r2",
                *(float(value * r**2) for value in left),
                "right*r2",
                *(float(value * r**2) for value in right),
                "det*r6",
                float(determinant * r**6),
                "det*r7",
                float(determinant * r**7),
                "exact",
                determinant,
                flush=True,
            )


if __name__ == "__main__":
    main()
