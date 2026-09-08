#!/usr/bin/env python3
"""Exact r=4 dimensionless compensated Gram-angle certificate."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


B = 9
R = 4
K = 2
J = 2


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def multinomial(total: int, cells: tuple[int, ...]) -> int:
    if any(cell < 0 for cell in cells) or sum(cells) != total:
        return 0
    answer = factorial(total)
    for cell in cells:
        answer //= factorial(cell)
    return answer


def harmonic_kernel(left_size: int, right_size: int, overlap: int) -> Fraction:
    numerator = 0
    for common_pairs in range(J + 1):
        cells = (
            overlap - common_pairs,
            left_size - J - overlap + common_pairs,
            right_size - J - overlap + common_pairs,
            B - left_size - right_size + overlap - common_pairs,
        )
        numerator += (
            2**J
            * (-1) ** (J - common_pairs)
            * choose(J, common_pairs)
            * multinomial(B - 2 * J, cells)
        )
    denominator = (
        choose(B, left_size)
        * choose(left_size, overlap)
        * choose(B - left_size, right_size - overlap)
    )
    return Fraction(numerator, denominator)


def harmonic_value(mask: int) -> int:
    value = 1
    for pair in range(J):
        value *= ((mask >> (2 * pair)) & 1) - ((mask >> (2 * pair + 1)) & 1)
    return value


def interval_mask(word: tuple[int, ...], start: int, size: int) -> int:
    return sum(1 << word[(start + offset) % B] for offset in range(size))


SUBSETS = {
    size: tuple(sum(1 << x for x in subset) for subset in combinations(range(B), size))
    for size in (R, R - 1, K)
}
SUBSET_ID = {
    size: {mask: index for index, mask in enumerate(SUBSETS[size])}
    for size in SUBSETS
}


def retained_ids(word: tuple[int, ...]) -> tuple[list[int], list[int]]:
    middle = [
        SUBSET_ID[R][interval_mask(word, start, R)] for start in range(1, B)
    ]
    lower = [
        SUBSET_ID[R - 1][interval_mask(word, start, R - 1)]
        for start in range(1, B)
    ]
    return middle, lower


def exact_exposure() -> tuple[list[int], list[int]]:
    identity = tuple(range(B))
    base_middle, base_lower = retained_ids(identity)
    middle_count = len(SUBSETS[R])
    base_configuration = sum(1 << index for index in base_middle)
    base_configuration |= sum(1 << (middle_count + index) for index in base_lower)
    middle_exposure = [0] * middle_count
    lower_exposure = [0] * len(SUBSETS[R - 1])
    configurations = set()
    for word in permutations(range(B)):
        middle, lower = retained_ids(word)
        configuration = sum(1 << index for index in middle)
        configuration |= sum(1 << (middle_count + index) for index in lower)
        assert configuration not in configurations
        configurations.add(configuration)
        duplicate = max(0, (configuration & base_configuration).bit_count() - 1)
        if duplicate:
            for index in middle:
                middle_exposure[index] += duplicate
            for index in lower:
                lower_exposure[index] += duplicate
    assert len(configurations) == factorial(B)
    return middle_exposure, lower_exposure


def gram_entry(left, right) -> Fraction:
    left_size, left_coefficients = left
    right_size, right_coefficients = right
    histogram = [0] * (min(left_size, right_size) + 1)
    for left_index, left_mask in enumerate(SUBSETS[left_size]):
        if not left_coefficients[left_index]:
            continue
        for right_index, right_mask in enumerate(SUBSETS[right_size]):
            if right_coefficients[right_index]:
                overlap = (left_mask & right_mask).bit_count()
                histogram[overlap] += (
                    left_coefficients[left_index] * right_coefficients[right_index]
                )
    return sum(
        (weight * harmonic_kernel(left_size, right_size, overlap)
         for overlap, weight in enumerate(histogram)),
        Fraction(),
    )


def solve(matrix: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    augmented = [row[:] + [target[index]] for index, row in enumerate(matrix)]
    dimension = len(matrix)
    for column in range(dimension):
        pivot = next(row for row in range(column, dimension) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(dimension):
            if row != column:
                multiple = augmented[row][column]
                augmented[row] = [
                    augmented[row][entry] - multiple * augmented[column][entry]
                    for entry in range(dimension + 1)
                ]
    return [augmented[row][-1] for row in range(dimension)]


def main() -> None:
    # Independently check the closed harmonic kernel against literal averaging.
    for left_size in (R, R - 1, K):
        for right_size in (R, R - 1, K):
            sums = {}
            counts = {}
            for left in SUBSETS[left_size]:
                for right in SUBSETS[right_size]:
                    overlap = (left & right).bit_count()
                    sums[overlap] = sums.get(overlap, 0) + harmonic_value(left) * harmonic_value(right)
                    counts[overlap] = counts.get(overlap, 0) + 1
            for overlap in counts:
                assert Fraction(sums[overlap], counts[overlap]) == harmonic_kernel(
                    left_size, right_size, overlap
                )

    middle_exposure, lower_exposure = exact_exposure()
    identity = tuple(range(B))
    middle_ids, lower_ids = retained_ids(identity)
    middle_incidence = [0] * len(SUBSETS[R])
    lower_incidence = [0] * len(SUBSETS[R - 1])
    shallow = [0] * len(SUBSETS[K])
    for index in middle_ids:
        middle_incidence[index] = 1
    for index in lower_ids:
        lower_incidence[index] = 1
    for start in range(B):
        shallow[SUBSET_ID[K][interval_mask(identity, start, K)]] = 1

    vectors = (
        (R, middle_incidence),
        (R - 1, lower_incidence),
        (R, middle_exposure),
        (R - 1, lower_exposure),
        (K, shallow),
    )
    gram = [[gram_entry(left, right) for right in vectors] for left in vectors]
    assert gram == [list(row) for row in zip(*gram)]
    solution = solve([row[:4] for row in gram[:4]], [row[4] for row in gram[:4]])
    projection = sum(gram[4][index] * solution[index] for index in range(4))
    alpha = 1 - projection / gram[4][4]
    expected = Fraction(189833430275409744043, 952911127398052338603)
    assert alpha == expected
    relative_eigenvalue = 4 * alpha
    assert relative_eigenvalue == Fraction(
        759333721101638976172, 952911127398052338603
    )
    print(
        "PASS exact r=4 dimensionless compensated Gram angle: "
        f"alpha={alpha}, alpha*Theta={relative_eigenvalue}"
    )


if __name__ == "__main__":
    main()
