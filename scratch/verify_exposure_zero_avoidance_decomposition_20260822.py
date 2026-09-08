#!/usr/bin/env python3
"""Exact r=4 audit of exposure = pair sum - degree + zero avoidance."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


B = 9
R = 4
K = 2
J = 2
SIZES = (R, R - 1, K)
SUBSETS = {
    size: tuple(sum(1 << x for x in subset) for subset in combinations(range(B), size))
    for size in SIZES
}
IDS = {size: {mask: index for index, mask in enumerate(SUBSETS[size])} for size in SIZES}


def interval(word, start, size):
    return sum(1 << word[(start + offset) % B] for offset in range(size))


def retained(word):
    return (
        [IDS[R][interval(word, start, R)] for start in range(1, B)],
        [IDS[R - 1][interval(word, start, R - 1)] for start in range(1, B)],
    )


def harmonic(mask):
    value = 1
    for pair in range(J):
        value *= ((mask >> (2 * pair)) & 1) - ((mask >> (2 * pair + 1)) & 1)
    return value


def kernel(left_size, right_size, overlap):
    total = count = 0
    for left in SUBSETS[left_size]:
        for right in SUBSETS[right_size]:
            if (left & right).bit_count() == overlap:
                total += harmonic(left) * harmonic(right)
                count += 1
    return Fraction(total, count)


def gram_entry(left, right):
    left_size, left_vector = left
    right_size, right_vector = right
    kernels = {
        overlap: kernel(left_size, right_size, overlap)
        for overlap in range(min(left_size, right_size) + 1)
    }
    answer = Fraction()
    for left_index, left_mask in enumerate(SUBSETS[left_size]):
        if not left_vector[left_index]:
            continue
        for right_index, right_mask in enumerate(SUBSETS[right_size]):
            if right_vector[right_index]:
                answer += (
                    left_vector[left_index]
                    * right_vector[right_index]
                    * kernels[(left_mask & right_mask).bit_count()]
                )
    return answer


def angle(vectors):
    gram = [[gram_entry(left, right) for right in vectors] for left in vectors]
    matrix = [gram[row][:4] + [gram[row][4]] for row in range(4)]
    for column in range(4):
        pivot = next(row for row in range(column, 4) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        for row in range(4):
            if row != column:
                multiple = matrix[row][column]
                matrix[row] = [
                    matrix[row][entry] - multiple * matrix[column][entry]
                    for entry in range(5)
                ]
    projection = sum(gram[4][row] * matrix[row][4] for row in range(4))
    return 1 - projection / gram[4][4]


def main():
    identity = tuple(range(B))
    base_middle, base_lower = retained(identity)
    middle_count = len(SUBSETS[R])
    base_mask = sum(1 << index for index in base_middle)
    base_mask |= sum(1 << (middle_count + index) for index in base_lower)

    degree_m = [0] * middle_count
    degree_l = [0] * len(SUBSETS[R - 1])
    pair_m = [0] * middle_count
    pair_l = [0] * len(SUBSETS[R - 1])
    exposure_m = [0] * middle_count
    exposure_l = [0] * len(SUBSETS[R - 1])
    second_m = [0] * middle_count
    second_l = [0] * len(SUBSETS[R - 1])
    zero_m = [0] * middle_count
    zero_l = [0] * len(SUBSETS[R - 1])
    seen = set()
    first_component = IDS[R][interval(identity, 1, R)]
    second_component = IDS[R][interval(identity, 2, R)]
    root_zero = IDS[R][sum(1 << x for x in (0, 1, 2, 5))]
    root_large = IDS[R][sum(1 << x for x in (0, 1, 6, 7))]
    conditional_counts = {root_zero: [0, 0], root_large: [0, 0]}

    for word in permutations(range(B)):
        middle, lower = retained(word)
        configuration = sum(1 << index for index in middle)
        configuration |= sum(1 << (middle_count + index) for index in lower)
        assert configuration not in seen
        seen.add(configuration)
        overlap = (configuration & base_mask).bit_count()
        duplicate = max(0, overlap - 1)
        second_weight = overlap * (overlap - 1) // 2
        if first_component in middle:
            for root, counts in conditional_counts.items():
                if root in middle:
                    counts[0] += 1
                    counts[1] += second_component in middle
        for index in middle:
            degree_m[index] += 1
            pair_m[index] += overlap
            exposure_m[index] += duplicate
            second_m[index] += second_weight
            zero_m[index] += overlap == 0
        for index in lower:
            degree_l[index] += 1
            pair_l[index] += overlap
            exposure_l[index] += duplicate
            second_l[index] += second_weight
            zero_l[index] += overlap == 0

    assert len(seen) == factorial(B)
    assert len(set(degree_m)) == len(set(degree_l)) == 1
    assert all(
        exposure_m[index] == pair_m[index] - degree_m[index] + zero_m[index]
        for index in range(middle_count)
    )
    assert conditional_counts[root_zero] == [672, 0]
    assert conditional_counts[root_large] == [1008, 432]
    assert all(
        exposure_l[index] == pair_l[index] - degree_l[index] + zero_l[index]
        for index in range(len(SUBSETS[R - 1]))
    )

    incidence_m = [int(index in base_middle) for index in range(middle_count)]
    incidence_l = [int(index in base_lower) for index in range(len(SUBSETS[R - 1]))]
    shallow = [0] * len(SUBSETS[K])
    for start in range(B):
        shallow[IDS[K][interval(identity, start, K)]] = 1

    exposed_vectors = (
        (R, incidence_m), (R - 1, incidence_l),
        (R, exposure_m), (R - 1, exposure_l), (K, shallow),
    )
    avoidance_vectors = (
        (R, incidence_m), (R - 1, incidence_l),
        (R, zero_m), (R - 1, zero_l), (K, shallow),
    )
    second_vectors = (
        (R, incidence_m), (R - 1, incidence_l),
        (R, second_m), (R - 1, second_l), (K, shallow),
    )
    expected = Fraction(189833430275409744043, 952911127398052338603)
    assert angle(exposed_vectors) == expected
    assert angle(avoidance_vectors) == expected
    second_angle = Fraction(496145882096395115, 2871985372664539779)
    assert angle(second_vectors) == second_angle
    print(
        "PASS exact zero-avoidance/second-order decomposition: all targets, "
        f"alpha={expected}, second_alpha={second_angle}, "
        "disconnected conditional ratios=0,3/7"
    )


if __name__ == "__main__":
    main()
