#!/usr/bin/env python3
"""Exact Venn--Hahn evaluation of the 16 leading zero-avoidance atoms."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import factorial
from typing import Iterable

from research_gate_b_allj_boundary_averages_20260822 import (
    exact_rho,
    extra_pair_numerator,
    falling,
    rank,
)
from research_w2_hahn_venn_exact_20260822 import interval_mask, masks_of_size


def blocker_cells(all_mask: int, blockers: tuple[int, ...]) -> tuple[int, ...]:
    cells = []
    for pattern in range(1 << len(blockers)):
        cell = all_mask
        for index, blocker in enumerate(blockers):
            if pattern & (1 << index):
                cell &= blocker
            else:
                cell &= ~blocker
        cells.append(cell & all_mask)
    return tuple(cells)


def rooted_signature(root: int, cells: tuple[int, ...]) -> tuple[int, ...]:
    answer = []
    for cell in cells:
        inside = (root & cell).bit_count()
        answer.extend((cell.bit_count() - inside, inside))
    return tuple(answer)


@lru_cache(maxsize=None)
def degree_lookup_many(
    b: int, root_size: int, blocker_sizes: tuple[int, ...]
) -> dict[tuple[int, ...], int]:
    all_mask = (1 << b) - 1
    arcs = {
        size: tuple(interval_mask(b, start, size) for start in range(1, b))
        for size in {root_size, *blocker_sizes}
    }
    counts: Counter[tuple[int, ...]] = Counter()
    for blockers in product(*(arcs[size] for size in blocker_sizes)):
        cells = blocker_cells(all_mask, blockers)
        for root in arcs[root_size]:
            counts[rooted_signature(root, cells)] += 1
    answer = {}
    for signature, multiplicity in counts.items():
        value = multiplicity
        for cell_size in signature:
            value *= factorial(cell_size)
        answer[signature] = value
    return answer


def edge_target(r: int, left: int, right: int) -> tuple[int, int, int]:
    """Return (rank,start,mask) for a Cayley boundary edge."""
    b = 2 * r + 1
    first = (r * left) % b
    second = (r * right) % b
    distance = (second - first) % b
    if distance in (r, r - 1):
        size, start = distance, first
    else:
        distance = (first - second) % b
        assert distance in (r, r - 1)
        size, start = distance, second
    return size, start, interval_mask(b, start, size)


def retained_boundary_edges(r: int) -> dict[tuple[int, int], tuple[int, int, int]]:
    b = 2 * r + 1
    answer = {}
    for size in (r, r - 1):
        for start in range(1, b):
            left = (-2 * start) % b
            right = (-2 * (start + size)) % b
            edge = tuple(sorted((left, right)))
            value = (size, start, interval_mask(b, start, size))
            assert edge_target(r, *edge) == value
            assert edge not in answer
            answer[edge] = value
    return answer


def local_blocker_sets(
    r: int, event_start: int
) -> list[tuple[tuple[int, int, int], ...]]:
    b = 2 * r + 1
    edges = retained_boundary_edges(r)
    first_root = (-2 * event_start) % b
    second_root = (first_root + 5) % b
    roots = {first_root, second_root}
    answer = []
    edge_items = list(edges.items())
    for size in (2, 3):
        for chosen in combinations(edge_items, size):
            vertices = {x for edge, _ in chosen for x in edge}
            if len(vertices) == 4 and roots <= vertices:
                answer.append(tuple(value for _, value in chosen))
    return answer


def local_coefficient_vector(
    r: int, root_size: int, event_start: int, root_masks: list[int]
) -> list[int]:
    all_mask = (1 << (2 * r + 1)) - 1
    answer = [0] * len(root_masks)
    for blockers in local_blocker_sets(r, event_start):
        blocker_sizes = tuple(value[0] for value in blockers)
        blocker_masks = tuple(value[2] for value in blockers)
        cells = blocker_cells(all_mask, blocker_masks)
        lookup = degree_lookup_many(2 * r + 1, root_size, blocker_sizes)
        sign = 1 if len(blockers) == 2 else -1
        for index, root in enumerate(root_masks):
            answer[index] += sign * lookup.get(rooted_signature(root, cells), 0)
    return answer


def signed_profile_value(
    r: int,
    root_size: int,
    root_masks: list[int],
    coefficients: list[int],
    level: int,
    event_start: int,
) -> int:
    b = 2 * r + 1
    k = r - 2
    inside_left = event_start
    outside_left = (event_start - 1) % b
    inside_right = (event_start + k - 1) % b
    outside_right = (event_start + k) % b
    shallow = interval_mask(b, event_start, k)
    boundary_mask = sum(
        1 << position
        for position in (inside_left, outside_left, inside_right, outside_right)
    )
    inside_pool = shallow & ~boundary_mask
    outside_pool = ((1 << b) - 1) ^ shallow
    outside_pool &= ~boundary_mask
    answer = 0
    for root, coefficient in zip(root_masks, coefficients):
        left = ((root >> inside_left) & 1) - ((root >> outside_left) & 1)
        right = ((root >> inside_right) & 1) - ((root >> outside_right) & 1)
        if not left or not right:
            continue
        extra = extra_pair_numerator(
            (root & inside_pool).bit_count(),
            (root & outside_pool).bit_count(),
            k - 2,
            b - k - 2,
            level - 2,
        )
        answer += coefficient * left * right * extra
    return answer


def run(r: int, show: bool) -> None:
    b = 2 * r + 1
    masks = {size: masks_of_size(b, size) for size in (r, r - 1)}
    local_coefficients = {
        (size, start): local_coefficient_vector(r, size, start, masks[size])
        for size in (r, r - 1)
        for start in range(b)
    }
    dm = 2 * r * factorial(r) * factorial(r + 1)
    k = r - 2
    for level in range(2, k + 1):
        denominator = falling(k - 2, level - 2) * falling(
            b - k - 2, level - 2
        )
        profile = []
        for start in range(b):
            profile.append(
                tuple(
                    signed_profile_value(
                        r,
                        size,
                        masks[size],
                        local_coefficients[(size, start)],
                        level,
                        start,
                    )
                    for size in (r, r - 1)
                )
            )
        residual = exact_rho(profile)
        if r >= 6:
            ell = r + 3
            assert tuple(
                profile[0][coordinate]
                + profile[ell][coordinate]
                - profile[3][coordinate]
                for coordinate in range(2)
            ) == (0, 0)
            assert residual >= Fraction(1, 3 * b)
        profile_rank = rank([list(row) for row in profile])
        augmented_rank = rank([[*row, 1] for row in profile])
        scale = denominator * dm
        print(
            f"r={r} j={level} rank={profile_rank} aug={augmented_rank} "
            f"rho={float(residual):.12g} exact={residual} "
            f"maxbar={max(abs(value) for row in profile for value in row) / scale:.12g}"
        )
        if show:
            for start, row in enumerate(profile):
                print(start, *row)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    if args.r < 5:
        raise SystemExit("r must be at least five")
    run(args.r, args.show)


if __name__ == "__main__":
    main()
