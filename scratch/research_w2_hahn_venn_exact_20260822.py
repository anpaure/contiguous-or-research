#!/usr/bin/env python3
"""Exact W2 Hahn/Venn Gram research without enumerating (2r+1)! words."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def interval_mask(b: int, start: int, size: int) -> int:
    return sum(1 << ((start + offset) % b) for offset in range(size))


def masks_of_size(b: int, size: int) -> list[int]:
    return [sum(1 << x for x in subset) for subset in combinations(range(b), size)]


def cells_for_pair(all_mask: int, left: int, right: int) -> tuple[int, ...]:
    return (
        all_mask & ~left & ~right,
        all_mask & ~left & right,
        all_mask & left & ~right,
        all_mask & left & right,
    )


def signature(root: int, pair_cells: tuple[int, ...]) -> tuple[int, ...]:
    answer: list[int] = []
    for cell in pair_cells:
        inside = (root & cell).bit_count()
        answer.extend((cell.bit_count() - inside, inside))
    return tuple(answer)


@lru_cache(maxsize=None)
def degree_lookup(b: int, root_size: int, left_size: int, right_size: int):
    """Map a labelled three-set Venn signature to its exact configuration degree."""
    all_mask = (1 << b) - 1
    arcs = {
        size: [interval_mask(b, start, size) for start in range(1, b)]
        for size in {root_size, left_size, right_size}
    }
    counts: Counter[tuple[int, ...]] = Counter()
    for left in arcs[left_size]:
        for right in arcs[right_size]:
            cells = cells_for_pair(all_mask, left, right)
            for root in arcs[root_size]:
                counts[signature(root, cells)] += 1
    return {
        key: multiplicity * product_factorials(key)
        for key, multiplicity in counts.items()
    }


def product_factorials(values: tuple[int, ...]) -> int:
    answer = 1
    for value in values:
        answer *= factorial(value)
    return answer


def coefficient_vectors(r: int):
    b = 2 * r + 1
    all_mask = (1 << b) - 1
    targets: list[tuple[int, int]] = []
    for size in (r, r - 1):
        targets.extend(
            (size, interval_mask(b, start, size)) for start in range(1, b)
        )
    target_pairs = []
    for first, second in combinations(targets, 2):
        left_size, left = first
        right_size, right = second
        target_pairs.append(
            (
                degree_lookup(b, r, left_size, right_size),
                degree_lookup(b, r - 1, left_size, right_size),
                cells_for_pair(all_mask, left, right),
            )
        )

    by_size: dict[int, list[int]] = {
        size: masks_of_size(b, size) for size in (r, r - 1, r - 2)
    }
    vector: dict[str, list[int]] = {}
    for size, name in ((r, "c_m"), (r - 1, "c_l")):
        base = {
            interval_mask(b, start, size) for start in range(1, b)
        }
        vector[name] = [int(mask in base) for mask in by_size[size]]

    for size, name, lookup_index in ((r, "w_m", 0), (r - 1, "w_l", 1)):
        values = []
        for root in by_size[size]:
            total = 0
            for pair_data in target_pairs:
                lookup = pair_data[lookup_index]
                total += lookup.get(signature(root, pair_data[2]), 0)
            values.append(total)
        vector[name] = values

    shallow_base = {
        interval_mask(b, start, r - 2) for start in range(b)
    }
    vector["q"] = [int(mask in shallow_base) for mask in by_size[r - 2]]
    return b, by_size, vector


def superset_sums(b: int, masks: list[int], coefficients: list[int]) -> list[int]:
    answer = [0] * (1 << b)
    for mask, coefficient in zip(masks, coefficients):
        answer[mask] = coefficient
    for bit in range(b):
        step = 1 << bit
        for mask in range(1 << b):
            if not mask & step:
                answer[mask] += answer[mask | step]
    return answer


def multinomial(total: int, cells: tuple[int, ...]) -> int:
    if any(value < 0 for value in cells) or sum(cells) != total:
        return 0
    answer = factorial(total)
    for value in cells:
        answer //= factorial(value)
    return answer


def zeta(b: int, left_size: int, right_size: int, level: int, overlap: int):
    if overlap < max(0, left_size + right_size - b):
        return Fraction(0)
    if overlap > min(left_size, right_size):
        return Fraction(0)
    denominator = (
        comb(b, left_size)
        * comb(left_size, overlap)
        * comb(b - left_size, right_size - overlap)
    )
    numerator = 0
    for same in range(level + 1):
        cells = (
            overlap - same,
            left_size - level - overlap + same,
            right_size - level - overlap + same,
            b - left_size - right_size + overlap - same,
        )
        numerator += (
            (-1) ** (level - same)
            * comb(level, same)
            * multinomial(b - 2 * level, cells)
        )
    return Fraction((1 << level) * numerator, denominator)


def binomial_coefficients(values: list[Fraction]) -> list[Fraction]:
    """Newton coefficients f(x)=sum_i answer[i] binom(x,i)."""
    work = values[:]
    answer = []
    while work:
        answer.append(work[0])
        work = [work[i + 1] - work[i] for i in range(len(work) - 1)]
    return answer


def gram_entry(
    b: int,
    left_size: int,
    right_size: int,
    level: int,
    left_sums: list[int],
    right_sums: list[int],
) -> Fraction:
    maximum = min(left_size, right_size)
    kernel = [zeta(b, left_size, right_size, level, h) for h in range(maximum + 1)]
    newton = binomial_coefficients(kernel)
    assert all(coefficient == 0 for coefficient in newton[level + 1 :])
    totals = [0] * (maximum + 1)
    for mask in range(1 << b):
        size = mask.bit_count()
        if size <= maximum:
            totals[size] += left_sums[mask] * right_sums[mask]
    return sum((newton[i] * totals[i] for i in range(maximum + 1)), Fraction())


def residual_fraction(gram: list[list[Fraction]]) -> Fraction:
    matrix = [gram[row][:4] + [gram[row][4]] for row in range(4)]
    for column in range(4):
        pivot = next(row for row in range(column, 4) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        for row in range(4):
            if row == column:
                continue
            multiple = matrix[row][column]
            matrix[row] = [
                matrix[row][entry] - multiple * matrix[column][entry]
                for entry in range(5)
            ]
    projection = sum(gram[4][row] * matrix[row][4] for row in range(4))
    return 1 - projection / gram[4][4]


def central_schur(gram: list[list[Fraction]]) -> list[list[Fraction]]:
    determinant = gram[0][0] * gram[1][1] - gram[0][1] ** 2
    inverse = (
        (gram[1][1] / determinant, -gram[0][1] / determinant),
        (-gram[0][1] / determinant, gram[0][0] / determinant),
    )
    answer = [[Fraction() for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for column in range(3):
            correction = sum(
                gram[row + 2][a] * inverse[a][c] * gram[c][column + 2]
                for a in range(2)
                for c in range(2)
            )
            answer[row][column] = gram[row + 2][column + 2] - correction
    return answer


def conditional_scalars(
    gram: list[list[Fraction]],
) -> tuple[Fraction, Fraction, Fraction]:
    conditional = central_schur(gram)
    determinant_two = (
        conditional[0][0] * conditional[1][1] - conditional[0][1] ** 2
    )
    determinant_three = (
        conditional[0][0]
        * (conditional[1][1] * conditional[2][2] - conditional[1][2] ** 2)
        - conditional[0][1]
        * (conditional[1][0] * conditional[2][2]
           - conditional[1][2] * conditional[2][0])
        + conditional[0][2]
        * (conditional[1][0] * conditional[2][1]
           - conditional[1][1] * conditional[2][0])
    )
    delta = determinant_two / (conditional[0][0] * conditional[1][1])
    xi = determinant_three / (
        conditional[0][0] * conditional[1][1] * conditional[2][2]
    )
    central_angle = conditional[2][2] / gram[4][4]
    return central_angle, delta, xi


def orbit_factor(r: int, level: int) -> Fraction:
    b = 2 * r + 1
    k = r - 2
    n = comb(b, k)
    weights = [6] + [2] * (k - 1) + [1]
    total = Fraction()
    for overlap in range(k + 1):
        eigen = 0
        for chosen in range(level + 1):
            first = choose(k - level, overlap - chosen)
            second = choose(b - k - level, k - level - overlap + chosen)
            eigen += (-1) ** (level - chosen) * comb(level, chosen) * first * second
        shell = comb(k, overlap) * comb(b - k, k - overlap)
        total += Fraction(weights[overlap] * eigen, shell)
    theta = Fraction(b, n) * total
    return theta / Fraction(b, n) ** 2


def run(r: int, show_matrix: bool = False) -> None:
    b, masks, coefficients = coefficient_vectors(r)
    metadata = (
        (r, "c_m"),
        (r - 1, "c_l"),
        (r, "w_m"),
        (r - 1, "w_l"),
        (r - 2, "q"),
    )
    transforms = {
        name: superset_sums(b, masks[size], coefficients[name])
        for size, name in metadata
    }
    for level in range(2, r - 1):
        gram = [[Fraction() for _ in range(5)] for _ in range(5)]
        for row, (left_size, left_name) in enumerate(metadata):
            for column, (right_size, right_name) in enumerate(metadata):
                gram[row][column] = gram_entry(
                    b,
                    left_size,
                    right_size,
                    level,
                    transforms[left_name],
                    transforms[right_name],
                )
        alpha = residual_fraction(gram)
        expected = {
            (4, 2): Fraction(496145882096395115, 2871985372664539779),
            (5, 2): Fraction(
                920020551945270166975711,
                12998197791101807219670856,
            ),
            (5, 3): Fraction(
                596657511940736589690394281,
                1103569337664148347762679657,
            ),
        }.get((r, level))
        if expected is not None:
            assert alpha == expected
        theta_relative = orbit_factor(r, level)
        expected_theta = {
            (4, 2): Fraction(4),
            (5, 2): Fraction(180, 7),
            (5, 3): Fraction(75, 7),
        }.get((r, level))
        if expected_theta is not None:
            assert theta_relative == expected_theta
        central_angle, delta, xi = conditional_scalars(gram)
        assert alpha == central_angle * xi / delta
        assert 0 <= central_angle <= 1
        assert 0 <= xi <= delta <= 1
        print(
            f"r={r} j={level} alpha={alpha} decimal={float(alpha):.12g} "
            f"central={float(central_angle):.12g} "
            f"delta={float(delta):.12g} xi={float(xi):.12g} "
            f"Theta={float(theta_relative):.12g} "
            f"product={float(alpha * theta_relative):.12g}"
        )
        if show_matrix:
            for row in range(5):
                print(
                    "corr",
                    *(f"{float(gram[row][column] / (gram[row][row] * gram[column][column]) ** Fraction(1, 2)):.9g}"
                      for column in range(5)),
                )
            conditional = central_schur(gram)
            for row in range(3):
                print(
                    "conditional",
                    *(f"{float(conditional[row][column] / (conditional[row][row] * conditional[column][column]) ** Fraction(1, 2)):.9g}"
                      for column in range(3)),
                )
    print(f"PASS exact W2 Hahn--Venn Gram reduction at r={r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--matrix", action="store_true")
    args = parser.parse_args()
    if args.r < 4:
        raise SystemExit("r must be at least 4")
    run(args.r, args.matrix)


if __name__ == "__main__":
    main()
