#!/usr/bin/env python3
"""Exact r=2 scan of tail leakage and disjoint-pair K shifts.

Evidence only.  It scans every integer cutoff for the product law with
p_M=3/4 and p_L=1/2.
"""

from fractions import Fraction
from itertools import combinations

from verify_gate_a_two_star_overlap_cell_decomposition_20260822 import (
    falling,
    make_catalogue,
    product_on_mask,
)


def subset_zeta(values, bit_count):
    output = list(values)
    for bit in range(bit_count):
        flag = 1 << bit
        for mask in range(1 << bit_count):
            if mask & flag:
                output[mask] += output[mask ^ flag]
    return output


def main():
    targets, rows, row_masks, _ = make_catalogue(r=2)
    probabilities = [
        Fraction(3, 4) if shore == "M" else Fraction(1, 2)
        for shore, _ in targets
    ]
    inverse = [1 / probability for probability in probabilities]
    target_count = len(targets)
    state_count = 1 << target_count
    all_target_mask = state_count - 1
    inverse_weight = [
        product_on_mask(inverse, mask) for mask in range(state_count)
    ]
    state_probability = [
        product_on_mask(probabilities, mask)
        * product_on_mask(
            [1 - probability for probability in probabilities],
            all_target_mask ^ mask,
        )
        for mask in range(state_count)
    ]

    root = next(u for u, target in enumerate(targets) if target[0] == "M")
    root_bit = 1 << root
    star = [row_id for row_id, row in enumerate(rows) if root in row]
    degree = [
        sum(row_masks[row_id] & ~state == 0 for row_id in star)
        for state in range(state_count)
    ]

    def kernel(first, second):
        total = Fraction(0)
        for further_mask in row_masks:
            left = (further_mask & row_masks[first]) & ~root_bit
            right = (further_mask & row_masks[second]) & ~root_bit
            if not left or not right:
                continue
            if further_mask & root_bit:
                total += inverse[root] * (
                    inverse_weight[left | right]
                    - inverse_weight[left]
                    - inverse_weight[right]
                    + 1
                )
            else:
                total += (
                    inverse_weight[left | right]
                    - inverse_weight[left]
                    - inverse_weight[right]
                )
        return total

    raw_count_overlap = [0 for _ in range(state_count)]
    raw_count_disjoint = [0 for _ in range(state_count)]
    raw_kernel_overlap = [Fraction(0) for _ in range(state_count)]
    raw_kernel_disjoint = [Fraction(0) for _ in range(state_count)]
    for first, second in combinations(star, 2):
        union = row_masks[first] | row_masks[second]
        value = 2 * kernel(first, second)
        offroot_common = (row_masks[first] & row_masks[second]) & ~root_bit
        if offroot_common:
            raw_count_overlap[union] += 2
            raw_kernel_overlap[union] += value
        else:
            raw_count_disjoint[union] += 2
            raw_kernel_disjoint[union] += value

    count_overlap = subset_zeta(raw_count_overlap, target_count)
    count_disjoint = subset_zeta(raw_count_disjoint, target_count)
    kernel_overlap = subset_zeta(raw_kernel_overlap, target_count)
    kernel_disjoint = subset_zeta(raw_kernel_disjoint, target_count)
    for state in range(state_count):
        assert count_overlap[state] + count_disjoint[state] == falling(
            degree[state], 2
        )

    def tilted_statistics(state_weight):
        normalizer = sum(
            state_probability[state] * state_weight[state]
            for state in range(state_count)
        )
        assert normalizer > 0

        def average(profile):
            return sum(
                state_probability[state]
                * state_weight[state]
                * (
                    Fraction(profile[state], falling(degree[state], 2))
                    if degree[state] >= 2
                    else 0
                )
                for state in range(state_count)
            ) / normalizer

        return (
            average(count_overlap),
            average(kernel_overlap),
            average(kernel_disjoint),
        )

    factorial_weight = [Fraction(falling(d, 12)) for d in degree]
    factorial = tilted_statistics(factorial_weight)
    print(
        "factorial",
        "overlap_probability",
        float(factorial[0]),
        "K_overlap",
        float(factorial[1]),
        "K_disjoint",
        float(factorial[2]),
    )
    print("cutoff overlap_probability deltaK_overlap deltaK_disjoint deltaK_total")
    for cutoff in range(11, max(degree)):
        tail_weight = [Fraction(max(d - cutoff, 0) ** 12) for d in degree]
        if not any(tail_weight):
            continue
        tail = tilted_statistics(tail_weight)
        deltas = (factorial[1] - tail[1], factorial[2] - tail[2])
        print(
            cutoff,
            f"{float(tail[0]):.12g}",
            f"{float(deltas[0]):+.12g}",
            f"{float(deltas[1]):+.12g}",
            f"{float(sum(deltas)):+.12g}",
        )


if __name__ == "__main__":
    main()
