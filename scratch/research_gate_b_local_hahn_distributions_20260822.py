#!/usr/bin/env python3
"""Expose local Gate-B profiles as exact linear combinations of Hahn values."""

from __future__ import annotations

import argparse
from collections import defaultdict
from math import factorial

from research_gate_b_local_atoms_fast_venn_20260822 import (
    boundary_cell_data,
    cell_choice_polynomial,
)
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    blocker_cells,
    degree_lookup_many,
    local_blocker_sets,
)


def signed_root_choice_distribution(
    b: int,
    positional_inside_counts: tuple[int, ...],
    label_cell_sizes: tuple[int, ...],
    label_inside_sizes: tuple[int, ...],
    label_marks: tuple[int, ...],
) -> dict[tuple[int, int], int]:
    """Coefficients of E_m(a,c), before evaluating the Hahn polynomial."""
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
                updated[(old_marks | new_marks, old_inside + new_inside)] += old_count * count
        states = updated

    answer: dict[tuple[int, int], int] = defaultdict(int)
    for (marks, inside_hits), count in states.items():
        left = ((marks >> 0) & 1) - ((marks >> 1) & 1)
        right = ((marks >> 2) & 1) - ((marks >> 3) & 1)
        if not left or not right:
            continue
        outside_hits = sum(positional_inside_counts) - marks.bit_count() - inside_hits
        answer[(inside_hits, outside_hits)] += count * left * right
    return dict(answer)


def blocker_term_distribution(
    r: int,
    root_size: int,
    event_start: int,
    blocker_data: tuple[tuple[int, int, int], ...],
) -> dict[tuple[int, int], int]:
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    blocker_sizes = tuple(value[0] for value in blocker_data)
    label_blockers = tuple(value[2] for value in blocker_data)
    label_cells = blocker_cells(all_mask, label_blockers)
    label_cell_sizes, label_inside_sizes, label_marks = boundary_cell_data(
        b, event_start, label_blockers
    )
    assert label_cell_sizes == tuple(cell.bit_count() for cell in label_cells)

    answer: dict[tuple[int, int], int] = defaultdict(int)
    lookup = degree_lookup_many(b, root_size, blocker_sizes)
    for signature, degree_value in lookup.items():
        outside_counts = signature[0::2]
        inside_counts = signature[1::2]
        if tuple(a + c for a, c in zip(outside_counts, inside_counts)) != label_cell_sizes:
            continue
        for hits, coefficient in signed_root_choice_distribution(
            b,
            inside_counts,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        ).items():
            answer[hits] += degree_value * coefficient
    return {key: value for key, value in answer.items() if value}


def local_distribution(r: int, root_size: int, event_start: int):
    answer: dict[tuple[int, int], int] = defaultdict(int)
    for blocker_data in local_blocker_sets(r, event_start):
        sign = 1 if len(blocker_data) == 2 else -1
        for hits, coefficient in blocker_term_distribution(
            r, root_size, event_start, blocker_data
        ).items():
            answer[hits] += sign * coefficient
    return {key: value for key, value in answer.items() if value}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--shore", choices=("middle", "lower"), default="middle")
    args = parser.parse_args()
    shore = args.r if args.shore == "middle" else args.r - 1
    dm = 2 * args.r * factorial(args.r) * factorial(args.r + 1)
    first = local_distribution(args.r, shore, args.r + 1)
    second = local_distribution(args.r, shore, args.r + 2)
    central = local_distribution(args.r, shore, args.r + 3)
    keys = sorted(set(first) | set(second) | set(central))
    for key in keys:
        print(key, second.get(key, 0) - first.get(key, 0), central.get(key, 0), dm)


if __name__ == "__main__":
    main()
