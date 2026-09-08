#!/usr/bin/env python3
"""Signed unique-window boundary averages for every Gate-B module."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from math import comb, factorial

from research_w2_hahn_venn_exact_20260822 import coefficient_vectors


def falling(value: int, length: int) -> int:
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


def extra_pair_numerator(
    inside_hits: int,
    outside_hits: int,
    inside_size: int,
    outside_size: int,
    pairs: int,
) -> int:
    """Signed injection sum over the remaining distinguished pairs."""
    answer = 0
    for chosen_inside in range(pairs + 1):
        chosen_outside = pairs - chosen_inside
        answer += (
            (-1) ** chosen_outside
            * comb(pairs, chosen_inside)
            * falling(inside_hits, chosen_inside)
            * falling(inside_size - chosen_inside, chosen_outside)
            * falling(outside_hits, chosen_outside)
            * falling(outside_size - chosen_outside, chosen_inside)
        )
    return answer


def boundary_profile_value(
    b: int,
    k: int,
    size: int,
    masks: list[int],
    coefficients: list[int],
    level: int,
    start: int,
) -> int:
    inside_left = start
    outside_left = (start - 1) % b
    inside_right = (start + k - 1) % b
    outside_right = (start + k) % b
    interval = sum(1 << ((start + offset) % b) for offset in range(k))
    boundary_mask = (
        (1 << inside_left)
        | (1 << outside_left)
        | (1 << inside_right)
        | (1 << outside_right)
    )
    all_mask = (1 << b) - 1
    inside_pool = interval & ~boundary_mask
    outside_pool = (all_mask ^ interval) & ~boundary_mask
    inside_size = k - 2
    outside_size = b - k - 2
    extra_pairs = level - 2
    answer = 0
    for mask, coefficient in zip(masks, coefficients):
        left_factor = int(bool(mask & (1 << inside_left))) - int(
            bool(mask & (1 << outside_left))
        )
        if not left_factor:
            continue
        right_factor = int(bool(mask & (1 << inside_right))) - int(
            bool(mask & (1 << outside_right))
        )
        if not right_factor:
            continue
        numerator = extra_pair_numerator(
            (mask & inside_pool).bit_count(),
            (mask & outside_pool).bit_count(),
            inside_size,
            outside_size,
            extra_pairs,
        )
        answer += coefficient * left_factor * right_factor * numerator
    return answer


def rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(answer, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        value = work[answer][column]
        work[answer] = [entry / value for entry in work[answer]]
        for row in range(len(work)):
            if row == answer:
                continue
            multiple = work[row][column]
            if multiple:
                work[row] = [
                    work[row][i] - multiple * work[answer][i]
                    for i in range(len(work[row]))
                ]
        answer += 1
    return answer


def exact_rho(profile: list[tuple[int, int]]) -> Fraction:
    g00 = sum(a * a for a, _ in profile)
    g01 = sum(a * b for a, b in profile)
    g11 = sum(b * b for _, b in profile)
    h0 = sum(a for a, _ in profile)
    h1 = sum(b for _, b in profile)
    determinant = g00 * g11 - g01 * g01
    if not determinant:
        return Fraction()
    projection = Fraction(
        g11 * h0 * h0 - 2 * g01 * h0 * h1 + g00 * h1 * h1,
        determinant,
    )
    return (Fraction(len(profile)) - projection) / len(profile)


def run(r: int, show: bool) -> None:
    b, masks_by_size, coefficients = coefficient_vectors(r)
    k = r - 2
    for level in range(2, r - 1):
        profile = []
        for start in range(b):
            profile.append(
                tuple(
                    boundary_profile_value(
                        b,
                        k,
                        size,
                        masks_by_size[size],
                        coefficients[name],
                        level,
                        start,
                    )
                    for size, name in ((r, "w_m"), (r - 1, "w_l"))
                )
            )
        profile_rank = rank([list(row) for row in profile])
        augmented_rank = rank([[a, b_value, 1] for a, b_value in profile])
        common, multiplicity = Counter(profile).most_common(1)[0]
        rho = exact_rho(profile)
        u0, u1, u3 = profile[0], profile[1], profile[3]
        local_determinant = (
            (u0[0] - u3[0]) * (u1[1] - u3[1])
            - (u0[1] - u3[1]) * (u1[0] - u3[0])
        )
        average_denominator = (
            falling(k - 2, level - 2)
            * falling(b - k - 2, level - 2)
        )
        degree_scale = 2 * r * factorial(r) * factorial(r + 1)
        normalized_k = Fraction(
            local_determinant,
            average_denominator**2 * degree_scale**2,
        )
        print(
            f"r={r} j={level} rank={profile_rank} aug={augmented_rank} "
            f"common={multiplicity}/{b} rho={float(rho):.12g} "
            f"Ksign={(local_determinant > 0) - (local_determinant < 0)} "
            f"KbarDM={float(normalized_k):.12g} "
            f"r4KbarDM={float(normalized_k * r**4):.12g}"
        )
        if show:
            print("baseline", common)
            for start, value in enumerate(profile):
                if value != common:
                    print("exception", start, value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    run(args.r, args.show)


if __name__ == "__main__":
    main()
