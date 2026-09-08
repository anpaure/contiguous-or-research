#!/usr/bin/env python3
"""Fast exact structured j=2 evaluations for the Gate-B cyclic bypass.

The root-set sum is aggregated by the four Venn cells of a fixed blocker
pair.  This avoids enumerating all central root subsets and makes larger-r
exact data possible.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

from research_w2_hahn_venn_exact_20260822 import (
    cells_for_pair,
    degree_lookup,
    interval_mask,
)


def compositions_four(total: int, caps: tuple[int, int, int, int]):
    for x0 in range(max(0, total - sum(caps[1:])), min(caps[0], total) + 1):
        left1 = total - x0
        for x1 in range(
            max(0, left1 - caps[2] - caps[3]), min(caps[1], left1) + 1
        ):
            left2 = left1 - x1
            for x2 in range(max(0, left2 - caps[3]), min(caps[2], left2) + 1):
                x3 = left2 - x2
                if 0 <= x3 <= caps[3]:
                    yield (x0, x1, x2, x3)


@lru_cache(maxsize=None)
def harmonic_pair_degree_sum_key(
    b: int,
    root_size: int,
    left_size: int,
    right_size: int,
    cell_sizes: tuple[int, int, int, int],
    point_cells: tuple[int, int, int, int],
) -> int:
    """Sum_S deg(S,left,right) H_2(S) by Venn-cell aggregation."""
    lookup = degree_lookup(b, root_size, left_size, right_size)

    answer = 0
    # H=(1_a-1_b)(1_c-1_d).
    choices = ((0, 2, 1), (0, 3, -1), (1, 2, -1), (1, 3, 1))
    for first, second, sign in choices:
        selected = [0, 0, 0, 0]
        selected[point_cells[first]] += 1
        selected[point_cells[second]] += 1
        caps = tuple(cell_sizes[i] - selected[i] for i in range(4))
        subtotal = 0
        for extra in compositions_four(root_size - 2, caps):
            inside = tuple(selected[i] + extra[i] for i in range(4))
            signature = tuple(
                value
                for i in range(4)
                for value in (cell_sizes[i] - inside[i], inside[i])
            )
            multiplicity = 1
            for cap, take in zip(caps, extra):
                multiplicity *= comb(cap, take)
            subtotal += multiplicity * lookup.get(signature, 0)
        answer += sign * subtotal
    return answer


def harmonic_pair_degree_sum(
    b: int,
    root_size: int,
    left_size: int,
    right_size: int,
    pair_cells: tuple[int, int, int, int],
    points: tuple[int, int, int, int],
) -> int:
    cell_sizes = tuple(cell.bit_count() for cell in pair_cells)
    point_cells = tuple(
        next(i for i, cell in enumerate(pair_cells) if cell >> point & 1)
        for point in points
    )
    return harmonic_pair_degree_sum_key(
        b,
        root_size,
        left_size,
        right_size,
        cell_sizes,
        point_cells,
    )


def w_value(r: int, root_size: int, points: tuple[int, int, int, int]) -> int:
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    targets = [
        (size, interval_mask(b, start, size))
        for size in (r, r - 1)
        for start in range(1, b)
    ]
    answer = 0
    for (left_size, left), (right_size, right) in combinations(targets, 2):
        answer += harmonic_pair_degree_sum(
            b,
            root_size,
            left_size,
            right_size,
            cells_for_pair(all_mask, left, right),
            points,
        )
    return answer


def rotate_points(points: tuple[int, int, int, int], b: int, amount: int):
    return tuple((point + amount) % b for point in points)


def difference_w_value(
    r: int, root_size: int, points: tuple[int, int, int, int]
) -> int:
    b = 2 * r + 1
    # Matches x(B)-x(tau^{-1}B) in the exact coefficient checker.
    return w_value(r, root_size, points) - w_value(
        r, root_size, rotate_points(points, b, -1)
    )


def run(r: int, boundary: bool) -> None:
    z1 = (0, r - 1, r + 2, 2 * r)
    z2 = (0, r // 2, 2 * r, r + 1)
    zopp = (0, 1, r + 3, 2 * r)
    values = []
    for points in (z1, z2, zopp):
        values.append(
            tuple(difference_w_value(r, size, points) for size in (r, r - 1))
        )
    wedge = values[1][0] * values[0][1] - values[1][1] * values[0][0]
    opposite_wedge = (
        values[2][0] * values[0][1] - values[2][1] * values[0][0]
    )
    degree_scale = 2 * r * factorial(r) * factorial(r + 1)
    print(f"r={r} z1={z1} values={values[0]}")
    print(f"r={r} z2={z2} values={values[1]}")
    print(
        f"r={r} wedge={wedge} wedge_over_DM2={Fraction(wedge, degree_scale**2)}"
    )
    print(f"r={r} zopp={zopp} values={values[2]}")
    print(
        f"r={r} opposite_wedge={opposite_wedge} "
        f"opposite_wedge_over_DM2={Fraction(opposite_wedge, degree_scale**2)}"
    )
    if boundary:
        b = 2 * r + 1
        k = r - 2
        profiles = []
        for t in range(4):
            points = (
                t,
                (t - 1) % b,
                (t + k - 1) % b,
                (t + k) % b,
            )
            profiles.append(tuple(w_value(r, size, points) for size in (r, r - 1)))
        deviations = [
            tuple(profiles[t][i] - profiles[3][i] for i in range(2))
            for t in range(3)
        ]
        wedge = (
            deviations[0][0] * deviations[1][1]
            - deviations[0][1] * deviations[1][0]
        )
        print("boundary_profiles", *profiles)
        print("boundary_deviations", *deviations)
        print(
            "boundary_wedge",
            wedge,
            "boundary_wedge_over_DM2",
            Fraction(wedge, degree_scale**2),
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--boundary", action="store_true")
    args = parser.parse_args()
    if args.r < 4:
        raise SystemExit("r must be at least four")
    run(args.r, args.boundary)


if __name__ == "__main__":
    main()
