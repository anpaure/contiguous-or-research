#!/usr/bin/env python3
"""Targeted exact Venn evaluator for larger local Gate-B blocker banks.

Instead of enumerating every positional blocker tuple, this uses the fixed
label Venn signature to generate at most four relative starts per blocker.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import product
from itertools import combinations
from math import factorial

from research_gate_b_local_atoms_fast_venn_20260822 import (
    boundary_cell_data,
    bounded_vertex_blocker_sets,
    signed_root_choice_sum,
)
from research_gate_b_zero_avoidance_local_atom_profiles_20260822 import (
    blocker_cells,
    local_blocker_sets,
)
from research_gate_b_local_hahn_distributions_20260822 import (
    signed_root_choice_distribution,
)
from research_w2_hahn_venn_exact_20260822 import interval_mask


def pair_intersection(
    cell_sizes: tuple[int, ...], first: int, second: int
) -> int:
    return sum(
        size
        for pattern, size in enumerate(cell_sizes)
        if pattern >> first & 1 and pattern >> second & 1
    )


def falling_small(value: int, count: int) -> int:
    answer = 1
    for offset in range(count):
        answer *= value - offset
    return answer if value >= count else 0


def signed_j2_cell_polynomial(
    cell_sizes: tuple[int, ...],
    marks: tuple[int, ...],
    root_inside: tuple[int, ...],
) -> int:
    """Signed bijection weight after removing the common cell factorials."""
    answer = 0
    for left_mark, left_sign in ((0, 1), (1, -1)):
        for right_mark, right_sign in ((2, 1), (3, -1)):
            selected = (1 << left_mark) | (1 << right_mark)
            term = left_sign * right_sign
            for cell_size, cell_marks, inside in zip(
                cell_sizes, marks, root_inside
            ):
                marked = cell_marks.bit_count()
                selected_here = (cell_marks & selected).bit_count()
                term *= falling_small(inside, selected_here)
                term *= falling_small(
                    cell_size - inside, marked - selected_here
                )
            answer += term
    return answer


@lru_cache(maxsize=None)
def positional_j2_polynomial_sum(
    r: int,
    root_size: int,
    blocker_sizes: tuple[int, ...],
    label_cell_sizes: tuple[int, ...],
    label_marks: tuple[int, ...],
) -> int:
    """Return the raw j=2 term after factoring ``prod(c-m)!``."""
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    starts = range(b)
    arcs = {
        size: tuple(interval_mask(b, start, size) for start in starts)
        for size in {root_size, *blocker_sizes}
    }
    anchor = arcs[blocker_sizes[0]][0]
    candidate_lists: list[tuple[tuple[int, int], ...]] = []
    for index, size in enumerate(blocker_sizes[1:], start=1):
        required = pair_intersection(label_cell_sizes, 0, index)
        candidate_lists.append(
            tuple(
                (start, mask)
                for start, mask in enumerate(arcs[size])
                if (mask & anchor).bit_count() == required
            )
        )

    answer = 0
    for tail in product(*candidate_lists):
        relative_starts = (0, *(start for start, _ in tail))
        blockers = (anchor, *(mask for _, mask in tail))
        cells = blocker_cells(all_mask, blockers)
        if tuple(cell.bit_count() for cell in cells) != label_cell_sizes:
            continue
        for root_start, root in enumerate(arcs[root_size]):
            inside = tuple((root & cell).bit_count() for cell in cells)
            allowed_translates = b - len(
                {(-start) % b for start in (*relative_starts, root_start)}
            )
            answer += allowed_translates * signed_j2_cell_polynomial(
                label_cell_sizes, label_marks, inside
            )
    return answer


def j2_factor_signature(
    r: int, cell_sizes: tuple[int, ...], marks: tuple[int, ...]
) -> tuple[tuple[int, int], tuple[int, ...]]:
    """Encode the two macroscopic factorial cells by offsets from r."""
    reduced = [size - mark.bit_count() for size, mark in zip(cell_sizes, marks)]
    large = sorted(value for value in reduced if value > r // 2)
    small = tuple(sorted(value for value in reduced if value <= r // 2))
    if len(large) != 2:
        raise AssertionError((r, cell_sizes, marks, reduced))
    return (large[0] - r, large[1] - r), small


@lru_cache(maxsize=None)
def positional_root_weights(
    r: int,
    root_size: int,
    blocker_sizes: tuple[int, ...],
    label_cell_sizes: tuple[int, ...],
) -> dict[tuple[int, ...], int]:
    """Map root-inside cell counts to exact positional factorial weights."""
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    starts = range(1, b)
    arcs = {
        size: tuple(interval_mask(b, start, size) for start in starts)
        for size in {root_size, *blocker_sizes}
    }
    anchor_size = blocker_sizes[0]
    answer: dict[tuple[int, ...], int] = defaultdict(int)

    for anchor in arcs[anchor_size]:
        candidate_lists = []
        for index, size in enumerate(blocker_sizes[1:], start=1):
            required = pair_intersection(label_cell_sizes, 0, index)
            candidates = tuple(mask for mask in arcs[size] if (mask & anchor).bit_count() == required)
            candidate_lists.append(candidates)
        for tail in product(*candidate_lists):
            blockers = (anchor, *tail)
            cells = blocker_cells(all_mask, blockers)
            if tuple(cell.bit_count() for cell in cells) != label_cell_sizes:
                continue
            for root in arcs[root_size]:
                inside = tuple((root & cell).bit_count() for cell in cells)
                weight = 1
                for cell_size, inside_size in zip(label_cell_sizes, inside):
                    weight *= factorial(inside_size) * factorial(cell_size - inside_size)
                answer[inside] += weight
    return dict(answer)


@lru_cache(maxsize=None)
def positional_root_weights_cyclic(
    r: int,
    root_size: int,
    blocker_sizes: tuple[int, ...],
    label_cell_sizes: tuple[int, ...],
) -> dict[tuple[int, ...], int]:
    """Translation-quotiented version of ``positional_root_weights``.

    Fix the first blocker at start zero, enumerate only relative starts,
    and multiply each relative root/blocker pattern by the exact number of
    cyclic translates for which every retained start is nonzero.
    """
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    starts = range(b)
    arcs = {
        size: tuple(interval_mask(b, start, size) for start in starts)
        for size in {root_size, *blocker_sizes}
    }
    anchor = arcs[blocker_sizes[0]][0]
    candidate_lists: list[tuple[tuple[int, int], ...]] = []
    for index, size in enumerate(blocker_sizes[1:], start=1):
        required = pair_intersection(label_cell_sizes, 0, index)
        candidates = tuple(
            (start, mask)
            for start, mask in enumerate(arcs[size])
            if (mask & anchor).bit_count() == required
        )
        candidate_lists.append(candidates)

    answer: dict[tuple[int, ...], int] = defaultdict(int)
    for tail in product(*candidate_lists):
        relative_starts = (0, *(start for start, _ in tail))
        blockers = (anchor, *(mask for _, mask in tail))
        cells = blocker_cells(all_mask, blockers)
        if tuple(cell.bit_count() for cell in cells) != label_cell_sizes:
            continue
        for root_start, root in enumerate(arcs[root_size]):
            inside = tuple((root & cell).bit_count() for cell in cells)
            allowed_translates = b - len(
                {(-start) % b for start in (*relative_starts, root_start)}
            )
            weight = allowed_translates
            for cell_size, inside_size in zip(label_cell_sizes, inside):
                weight *= factorial(inside_size) * factorial(
                    cell_size - inside_size
                )
            answer[inside] += weight
    return dict(answer)


def targeted_blocker_term_value(
    r: int,
    root_size: int,
    level: int,
    event_start: int,
    blocker_data: tuple[tuple[int, int, int], ...],
) -> int:
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    blocker_sizes = tuple(value[0] for value in blocker_data)
    label_blockers = tuple(value[2] for value in blocker_data)
    label_cells = blocker_cells(all_mask, label_blockers)
    label_cell_sizes, label_inside_sizes, label_marks = boundary_cell_data(
        b, event_start, label_blockers
    )
    assert label_cell_sizes == tuple(cell.bit_count() for cell in label_cells)
    weights = positional_root_weights_cyclic(
        r, root_size, blocker_sizes, label_cell_sizes
    )
    return sum(
        weight
        * signed_root_choice_sum(
            b,
            level,
            inside,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        )
        for inside, weight in weights.items()
    )


def targeted_blocker_term_distribution(
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
    weights = positional_root_weights_cyclic(
        r, root_size, blocker_sizes, label_cell_sizes
    )
    answer: dict[tuple[int, int], int] = defaultdict(int)
    for inside, weight in weights.items():
        for hits, coefficient in signed_root_choice_distribution(
            b,
            inside,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        ).items():
            answer[hits] += weight * coefficient
    return {key: value for key, value in answer.items() if value}


def bank_row(
    r: int, level: int, event_start: int, maximum_vertices: int
) -> tuple[int, int]:
    blockers = (
        local_blocker_sets(r, event_start)
        if maximum_vertices == 4
        else bounded_vertex_blocker_sets(r, event_start, maximum_vertices)
    )
    return tuple(
        sum(
            (-1) ** len(blocker_data)
            * targeted_blocker_term_value(
                r, root_size, level, event_start, blocker_data
            )
            for blocker_data in blockers
        )
        for root_size in (r, r - 1)
    )


def bank_distribution(
    r: int, root_size: int, event_start: int, maximum_vertices: int
) -> dict[tuple[int, int], int]:
    blockers = (
        local_blocker_sets(r, event_start)
        if maximum_vertices == 4
        else bounded_vertex_blocker_sets(r, event_start, maximum_vertices)
    )
    answer: dict[tuple[int, int], int] = defaultdict(int)
    for blocker_data in blockers:
        sign = (-1) ** len(blocker_data)
        for hits, coefficient in targeted_blocker_term_distribution(
            r, root_size, event_start, blocker_data
        ).items():
            answer[hits] += sign * coefficient
    return {key: value for key, value in answer.items() if value}


def complete_boundary_edges(r: int) -> dict[tuple[int, int], tuple[int, int, int]]:
    b = 2 * r + 1
    answer = {}
    for size in (r, r - 1):
        for start in range(b):
            left = (-2 * start) % b
            right = (-2 * (start + size)) % b
            edge = tuple(sorted((left, right)))
            answer[edge] = (size, start, interval_mask(b, start, size))
    return answer


def complete_bounded_blocker_sets(
    r: int, event_start: int, maximum_vertices: int
) -> list[tuple[tuple[int, int, int], ...]]:
    b = 2 * r + 1
    edge_values = complete_boundary_edges(r)
    first_root = (-2 * event_start) % b
    roots = {first_root, (first_root + 5) % b}
    reached = set(roots)
    for _ in range(maximum_vertices - 1):
        reached |= {
            vertex
            for edge in edge_values
            if set(edge) & reached
            for vertex in edge
        }
    answer = set()
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
                chosen = [
                    induced[index]
                    for index in range(len(induced))
                    if mask >> index & 1
                ]
                if len(chosen) < 2:
                    continue
                incident = {vertex for edge, _ in chosen for vertex in edge}
                if incident == vertices:
                    answer.add(tuple(sorted(value for _, value in chosen)))
    return sorted(answer)


def blocker_boundary_edge(
    r: int, blocker: tuple[int, int, int]
) -> frozenset[int]:
    size, start, _ = blocker
    b = 2 * r + 1
    return frozenset(((-2 * start) % b, (-2 * (start + size)) % b))


def every_component_is_rooted(
    r: int,
    event_start: int,
    blocker_data: tuple[tuple[int, int, int], ...],
) -> bool:
    b = 2 * r + 1
    first_root = (-2 * event_start) % b
    roots = {first_root, (first_root + 5) % b}
    edges = [blocker_boundary_edge(r, blocker) for blocker in blocker_data]
    unseen = set(range(len(edges)))
    while unseen:
        seed = unseen.pop()
        vertices = set(edges[seed])
        changed = True
        while changed:
            changed = False
            for index in tuple(unseen):
                if vertices & edges[index]:
                    vertices.update(edges[index])
                    unseen.remove(index)
                    changed = True
        if not vertices & roots:
            return False
    return True


def complete_bounded_rooted_core_sets(
    r: int, event_start: int, maximum_vertices: int
) -> list[tuple[tuple[int, int, int], ...]]:
    """Bounded blocker sets for which every component contains an event root."""
    return [
        blocker_data
        for blocker_data in complete_bounded_blocker_sets(
            r, event_start, maximum_vertices
        )
        if every_component_is_rooted(r, event_start, blocker_data)
    ]


def puncture_correction_row(
    r: int, level: int, event_start: int, maximum_vertices: int
) -> tuple[int, int]:
    blockers = [
        blocker_data
        for blocker_data in complete_bounded_blocker_sets(
            r, event_start, maximum_vertices
        )
        if any(start == 0 for _, start, _ in blocker_data)
    ]
    return tuple(
        sum(
            (-1) ** len(blocker_data)
            * targeted_blocker_term_value(
                r, root_size, level, event_start, blocker_data
            )
            for blocker_data in blockers
        )
        for root_size in (r, r - 1)
    )


def grouped_puncture_correction_row(
    r: int, level: int, event_start: int, maximum_vertices: int
) -> tuple[int, int]:
    """The same puncture correction, grouped by exact labelled cell data."""
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    grouped: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]],
        int,
    ] = defaultdict(int)
    for blocker_data in complete_bounded_blocker_sets(
        r, event_start, maximum_vertices
    ):
        if not any(start == 0 for _, start, _ in blocker_data):
            continue
        blocker_sizes = tuple(value[0] for value in blocker_data)
        blocker_masks = tuple(value[2] for value in blocker_data)
        label_cells = blocker_cells(all_mask, blocker_masks)
        cell_sizes, inside_sizes, marks = boundary_cell_data(
            b, event_start, blocker_masks
        )
        assert cell_sizes == tuple(cell.bit_count() for cell in label_cells)
        grouped[(blocker_sizes, cell_sizes, inside_sizes, marks)] += (
            (-1) ** len(blocker_data)
        )

    rows = []
    for root_size in (r, r - 1):
        answer = 0
        for (
            blocker_sizes,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        ), multiplicity in grouped.items():
            if not multiplicity:
                continue
            weights = positional_root_weights_cyclic(
                r, root_size, blocker_sizes, label_cell_sizes
            )
            answer += multiplicity * sum(
                weight
                * signed_root_choice_sum(
                    b,
                    level,
                    inside,
                    label_cell_sizes,
                    label_inside_sizes,
                    label_marks,
                )
                for inside, weight in weights.items()
            )
        rows.append(answer)
    return tuple(rows)


def grouped_puncture_rooted_core_row(
    r: int, level: int, event_start: int, maximum_vertices: int
) -> tuple[int, int]:
    """Puncture correction restricted to components meeting an event root."""
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    grouped: dict[
        tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]],
        int,
    ] = defaultdict(int)
    for blocker_data in complete_bounded_rooted_core_sets(
        r, event_start, maximum_vertices
    ):
        if not any(start == 0 for _, start, _ in blocker_data):
            continue
        blocker_sizes = tuple(value[0] for value in blocker_data)
        blocker_masks = tuple(value[2] for value in blocker_data)
        label_cells = blocker_cells(all_mask, blocker_masks)
        cell_sizes, inside_sizes, marks = boundary_cell_data(
            b, event_start, blocker_masks
        )
        assert cell_sizes == tuple(cell.bit_count() for cell in label_cells)
        grouped[(blocker_sizes, cell_sizes, inside_sizes, marks)] += (
            (-1) ** len(blocker_data)
        )

    rows = []
    for root_size in (r, r - 1):
        answer = 0
        for (
            blocker_sizes,
            label_cell_sizes,
            label_inside_sizes,
            label_marks,
        ), multiplicity in grouped.items():
            if not multiplicity:
                continue
            weights = positional_root_weights_cyclic(
                r, root_size, blocker_sizes, label_cell_sizes
            )
            answer += multiplicity * sum(
                weight
                * signed_root_choice_sum(
                    b,
                    level,
                    inside,
                    label_cell_sizes,
                    label_inside_sizes,
                    label_marks,
                )
                for inside, weight in weights.items()
            )
        rows.append(answer)
    return tuple(rows)


def puncture_j2_factor_groups(
    r: int,
    root_size: int,
    event_start: int,
    maximum_vertices: int,
    rooted_only: bool = False,
) -> dict[tuple[tuple[int, int], tuple[int, ...]], int]:
    """Group a j=2 puncture correction by its two large factorial cells."""
    b = 2 * r + 1
    answer: dict[tuple[tuple[int, int], tuple[int, ...]], int] = defaultdict(int)
    blocker_sets = (
        complete_bounded_rooted_core_sets(r, event_start, maximum_vertices)
        if rooted_only
        else complete_bounded_blocker_sets(r, event_start, maximum_vertices)
    )
    for blocker_data in blocker_sets:
        if not any(start == 0 for _, start, _ in blocker_data):
            continue
        blocker_sizes = tuple(value[0] for value in blocker_data)
        blocker_masks = tuple(value[2] for value in blocker_data)
        cell_sizes, _, marks = boundary_cell_data(b, event_start, blocker_masks)
        signature = j2_factor_signature(r, cell_sizes, marks)
        polynomial = positional_j2_polynomial_sum(
            r,
            root_size,
            blocker_sizes,
            cell_sizes,
            marks,
        )
        answer[signature] += (-1) ** len(blocker_data) * polynomial
    return {signature: value for signature, value in answer.items() if value}


def expand_j2_factor_groups(
    r: int,
    groups: dict[tuple[tuple[int, int], tuple[int, ...]], int],
) -> int:
    answer = 0
    for (large_offsets, small_cells), polynomial in groups.items():
        factorial_core = 1
        for offset in large_offsets:
            factorial_core *= factorial(r + offset)
        for cell in small_cells:
            factorial_core *= factorial(cell)
        answer += polynomial * factorial_core
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("level", type=int)
    parser.add_argument("--vertices", type=int, default=5)
    args = parser.parse_args()
    for start in (3, args.r + 1, args.r + 2):
        print(start, *bank_row(args.r, args.level, start, args.vertices), flush=True)


if __name__ == "__main__":
    main()
