#!/usr/bin/env python3
"""Fast exact Venn evaluator for the sixteen Gate-B local atoms.

Unlike research_gate_b_zero_avoidance_local_atom_profiles_20260822.py this
does not enumerate all root subsets.  It swaps the root-subset sum with the
positional interval-start sum and evaluates the boundary Hahn functional by
cellwise coefficient extraction.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial

from research_gate_b_allj_boundary_averages_20260822 import (
    exact_rho,
    extra_pair_numerator,
    falling,
    rank,
)
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    blocker_cells,
    degree_lookup_many,
    local_blocker_sets,
    retained_boundary_edges,
)
from research_w2_hahn_venn_exact_20260822 import interval_mask


def blocker_pattern(mask: int, blockers: tuple[int, ...]) -> int:
    answer = 0
    for index, blocker in enumerate(blockers):
        if mask & blocker:
            answer |= 1 << index
    return answer


def boundary_cell_data(
    b: int, event_start: int, blockers: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Return blocker-cell sizes, inside-pool sizes, and 4-bit marks."""
    k = (b - 1) // 2 - 2
    boundary = (
        event_start,
        (event_start - 1) % b,
        (event_start + k - 1) % b,
        (event_start + k) % b,
    )
    shallow = interval_mask(b, event_start, k)
    cells = [0] * (1 << len(blockers))
    inside = [0] * len(cells)
    marks = [0] * len(cells)
    for position in range(b):
        pattern = 0
        for index, blocker in enumerate(blockers):
            if blocker & (1 << position):
                pattern |= 1 << index
        cells[pattern] += 1
        if position in boundary:
            marks[pattern] |= 1 << boundary.index(position)
        elif shallow & (1 << position):
            inside[pattern] += 1
    return tuple(cells), tuple(inside), tuple(marks)


def cell_choice_polynomial(
    cell_size: int, inside_size: int, marks: int, chosen: int
) -> dict[tuple[int, int], int]:
    """Map (boundary-pattern, inside hits) to numbers of root choices."""
    marked_positions = [bit for bit in range(4) if marks & (1 << bit)]
    outside_size = cell_size - inside_size - len(marked_positions)
    answer: dict[tuple[int, int], int] = {}
    for boundary_pattern in range(1 << len(marked_positions)):
        used = boundary_pattern.bit_count()
        actual_pattern = sum(
            1 << marked_positions[index]
            for index in range(len(marked_positions))
            if boundary_pattern & (1 << index)
        )
        for inside_hits in range(inside_size + 1):
            outside_hits = chosen - used - inside_hits
            if 0 <= outside_hits <= outside_size:
                answer[(actual_pattern, inside_hits)] = (
                    comb(inside_size, inside_hits)
                    * comb(outside_size, outside_hits)
                )
    return answer


def signed_root_choice_sum(
    b: int,
    level: int,
    positional_inside_counts: tuple[int, ...],
    label_cell_sizes: tuple[int, ...],
    label_inside_sizes: tuple[int, ...],
    label_marks: tuple[int, ...],
) -> int:
    """Sum the unnormalised signed boundary Hahn numerator over roots."""
    states: dict[tuple[int, int], int] = {(0, 0): 1}
    for cell_size, inside_size, marks, chosen in zip(
        label_cell_sizes,
        label_inside_sizes,
        label_marks,
        positional_inside_counts,
    ):
        choices = cell_choice_polynomial(cell_size, inside_size, marks, chosen)
        updated: dict[tuple[int, int], int] = defaultdict(int)
        for (old_marks, old_inside), old_count in states.items():
            for (new_marks, new_inside), count in choices.items():
                updated[(old_marks | new_marks, old_inside + new_inside)] += (
                    old_count * count
                )
        states = updated

    k = (b - 1) // 2 - 2
    inside_pool_size = k - 2
    outside_pool_size = b - k - 2
    pairs = level - 2
    answer = 0
    for (marks, inside_hits), count in states.items():
        left = ((marks >> 0) & 1) - ((marks >> 1) & 1)
        right = ((marks >> 2) & 1) - ((marks >> 3) & 1)
        if not left or not right:
            continue
        outside_hits = sum(positional_inside_counts) - marks.bit_count() - inside_hits
        answer += count * left * right * extra_pair_numerator(
            inside_hits,
            outside_hits,
            inside_pool_size,
            outside_pool_size,
            pairs,
        )
    return answer


def blocker_term_value(
    r: int,
    root_size: int,
    level: int,
    event_start: int,
    blocker_data: tuple[tuple[int, int, int], ...],
) -> int:
    """Exact raw signed numerator for one fixed labelled blocker tuple."""
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    blocker_sizes = tuple(value[0] for value in blocker_data)
    label_blockers = tuple(value[2] for value in blocker_data)
    label_cells = blocker_cells(all_mask, label_blockers)
    label_cell_sizes, label_inside_sizes, label_marks = boundary_cell_data(
        b, event_start, label_blockers
    )
    assert label_cell_sizes == tuple(cell.bit_count() for cell in label_cells)

    answer = 0
    lookup = degree_lookup_many(b, root_size, blocker_sizes)
    for signature, degree_value in lookup.items():
        outside_counts = signature[0::2]
        inside_counts = signature[1::2]
        if tuple(a + c for a, c in zip(outside_counts, inside_counts)) != label_cell_sizes:
            continue
        answer += degree_value * signed_root_choice_sum(
            b,
            level,
            inside_counts,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        )
    return answer


def local_profile(r: int, level: int) -> list[tuple[int, int]]:
    b = 2 * r + 1
    return [local_row(r, level, event_start) for event_start in range(b)]


def local_row(r: int, level: int, event_start: int) -> tuple[int, int]:
    row = []
    blockers = local_blocker_sets(r, event_start)
    for root_size in (r, r - 1):
        value = 0
        for blocker_data in blockers:
            sign = 1 if len(blocker_data) == 2 else -1
            value += sign * blocker_term_value(
                r, root_size, level, event_start, blocker_data
            )
        row.append(value)
    return tuple(row)


def bounded_vertex_blocker_sets(
    r: int, event_start: int, maximum_vertices: int
) -> list[tuple[tuple[int, int, int], ...]]:
    """Enumerate all retained blocker sets with <=q vertices covering roots."""
    b = 2 * r + 1
    edge_values = retained_boundary_edges(r)
    first_root = (-2 * event_start) % b
    second_root = (first_root + 5) % b
    roots = {first_root, second_root}

    reached = set(roots)
    for _ in range(maximum_vertices - 1):
        reached |= {
            vertex
            for edge in edge_values
            if set(edge) & reached
            for vertex in edge
        }

    answer: set[tuple[tuple[int, int, int], ...]] = set()
    remaining = sorted(reached - roots)
    for vertex_count in range(4, maximum_vertices + 1):
        for extras in combinations(remaining, vertex_count - 2):
            vertices = roots | set(extras)
            induced = [
                (edge, value)
                for edge, value in edge_values.items()
                if set(edge) <= vertices
            ]
            for mask in range(1 << len(induced)):
                chosen = [induced[index] for index in range(len(induced)) if mask >> index & 1]
                if len(chosen) < 2:
                    continue
                incident = {vertex for edge, _ in chosen for vertex in edge}
                if incident == vertices:
                    answer.add(tuple(sorted((value for _, value in chosen))))
    return sorted(answer)


def bounded_vertex_row(
    r: int, level: int, event_start: int, maximum_vertices: int
) -> tuple[int, int]:
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    blockers = bounded_vertex_blocker_sets(r, event_start, maximum_vertices)
    grouped: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]],
        int,
    ] = defaultdict(int)
    for blocker_data in blockers:
        blocker_sizes = tuple(value[0] for value in blocker_data)
        blocker_masks = tuple(value[2] for value in blocker_data)
        cell_sizes, inside_sizes, marks = boundary_cell_data(
            b, event_start, blocker_masks
        )
        assert cell_sizes == tuple(
            cell.bit_count() for cell in blocker_cells(all_mask, blocker_masks)
        )
        grouped[(blocker_sizes, cell_sizes, inside_sizes, marks)] += (
            (-1) ** len(blocker_data)
        )

    row = []
    for root_size in (r, r - 1):
        value = 0
        for (
            blocker_sizes,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        ), multiplicity in grouped.items():
            if not multiplicity:
                continue
            lookup = degree_lookup_many(b, root_size, blocker_sizes)
            term = 0
            for signature, degree_value in lookup.items():
                outside_counts = signature[0::2]
                inside_counts = signature[1::2]
                if tuple(
                    a + c for a, c in zip(outside_counts, inside_counts)
                ) != label_cell_sizes:
                    continue
                term += degree_value * signed_root_choice_sum(
                    b,
                    level,
                    inside_counts,
                    label_cell_sizes,
                    label_inside_sizes,
                    label_marks,
                )
            value += multiplicity * term
        row.append(value)
    return tuple(row)


def run(r: int, level: int, show: bool) -> None:
    profile = local_profile(r, level)
    b = 2 * r + 1
    denominator = falling(r - 4, level - 2) * falling(r + 1, level - 2)
    degree_scale = 2 * r * factorial(r) * factorial(r + 1)
    scale = denominator * degree_scale
    residual = exact_rho(profile)
    print(
        f"r={r} j={level} rank={rank([list(row) for row in profile])} "
        f"aug={rank([[*row, 1] for row in profile])} rho={residual} "
        f"maxbar={float(Fraction(max(abs(x) for row in profile for x in row), scale)):.12g}"
    )
    if show:
        for start, row in enumerate(profile):
            print(start, *row)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("level", type=int)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    if not 2 <= args.level <= args.r - 2:
        raise SystemExit("require 2 <= level <= r-2")
    run(args.r, args.level, args.show)


if __name__ == "__main__":
    main()
