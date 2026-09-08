#!/usr/bin/env python3
"""Exact r=2 audit of overlap-cell decompositions for Gate A's two-star.

This checker is deliberately diagnostic as well as algebraic.  It verifies
the laws of total covariance for total overlap and for the two-shore overlap
vector, and it tests which data are actually constant on those cells.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def falling(n, k):
    if n < k:
        return 0
    out = 1
    for j in range(k):
        out *= n - j
    return out


def make_catalogue(r):
    b = 2 * r + 1
    targets = (
        [("M", subset) for subset in combinations(range(b), r)]
        + [("L", subset) for subset in combinations(range(b), r - 1)]
    )
    target_index = {target: index for index, target in enumerate(targets)}
    row_word = {}
    for word in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(sorted(word[(start + j) % b] for j in range(r)))
            lower = tuple(sorted(word[(start + j) % b] for j in range(r - 1)))
            row.append(target_index[("M", middle)])
            row.append(target_index[("L", lower)])
        row_word[tuple(sorted(row))] = word
    rows = sorted(row_word)
    assert len(rows) == factorial(b)
    row_masks = [sum(1 << target for target in row) for row in rows]
    words = [row_word[row] for row in rows]
    return targets, rows, row_masks, words


def product_on_mask(values, mask):
    out = Fraction(1)
    for index, value in enumerate(values):
        if mask & (1 << index):
            out *= value
    return out


def superset_zeta(values, bit_count):
    output = list(values)
    for bit in range(bit_count):
        flag = 1 << bit
        for mask in range(1 << bit_count):
            if not mask & flag:
                output[mask] += output[mask | flag]
    return output


def weighted_mean(items, weight, value):
    total = sum(weight(item) for item in items)
    assert total > 0
    return sum(weight(item) * value(item) for item in items) / total


def weighted_covariance(items, weight, left, right):
    mean_left = weighted_mean(items, weight, left)
    mean_right = weighted_mean(items, weight, right)
    return weighted_mean(
        items,
        weight,
        lambda item: (left(item) - mean_left) * (right(item) - mean_right),
    )


def sign(value):
    return (value > 0) - (value < 0)


def main():
    targets, rows, row_masks, words = make_catalogue(r=2)
    probabilities = [
        Fraction(3, 4) if shore == "M" else Fraction(1, 2)
        for shore, _ in targets
    ]
    inverse = [1 / probability for probability in probabilities]
    middle_mask = sum(1 << u for u, target in enumerate(targets) if target[0] == "M")
    lower_mask = sum(1 << u for u, target in enumerate(targets) if target[0] == "L")

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
    assert len(star) == 48

    root_subset = targets[root][1]
    position = {}
    for row_id in star:
        word = words[row_id]
        matches = [
            start
            for start in range(1, 5)
            if tuple(sorted(word[(start + j) % 5] for j in range(2)))
            == root_subset
        ]
        assert len(matches) == 1
        position[row_id] = matches[0]
    representatives = {
        pos: next(row_id for row_id in star if position[row_id] == pos)
        for pos in range(1, 5)
    }

    def two_star(first, second):
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

    pair_kernel = {
        pair: two_star(*pair) for pair in combinations(star, 2)
    }

    def kernel(first, second):
        return pair_kernel[tuple(sorted((first, second)))]

    pair_probability = {
        pair: product_on_mask(
            probabilities, row_masks[pair[0]] | row_masks[pair[1]]
        )
        for pair in combinations(star, 2)
    }

    def q_pair(first, second):
        return pair_probability[tuple(sorted((first, second)))]

    degree = [
        sum(row_masks[row_id] & ~state == 0 for row_id in star)
        for state in range(state_count)
    ]
    m = 12
    cutoff = 12
    weights = {
        "factorial": [Fraction(falling(d - 2, m - 2)) for d in degree],
        "tail": [
            Fraction(max(d - cutoff, 0) ** m, falling(d, 2))
            if d >= 2
            else Fraction(0)
            for d in degree
        ],
    }
    conditioned = {}
    for label, values in weights.items():
        conditioned[label] = superset_zeta(
            [state_probability[state] * values[state] for state in range(state_count)],
            target_count,
        )

    def pair_profile(label, first, second):
        union = row_masks[first] | row_masks[second]
        return conditioned[label][union] / q_pair(first, second)

    def overlap_vector(first, second):
        common = (row_masks[first] & row_masks[second]) & ~root_bit
        return ((common & middle_mask).bit_count(), (common & lower_mask).bit_count())

    ordered_pairs = [
        (first, second)
        for first in star
        for second in star
        if second != first
    ]

    def l12_pair(pair):
        return pair_profile("factorial", *pair)

    def lc_pair(pair):
        return pair_profile("tail", *pair)

    def pair_ratio(pair):
        return lc_pair(pair) / l12_pair(pair)

    def factorial_pair_weight(pair):
        return q_pair(*pair) * l12_pair(pair)

    global_factorial_mean = weighted_mean(
        ordered_pairs, factorial_pair_weight, lambda pair: kernel(*pair)
    )
    global_tail_mean = weighted_mean(
        ordered_pairs,
        lambda pair: q_pair(*pair) * lc_pair(pair),
        lambda pair: kernel(*pair),
    )
    global_mean_ratio = weighted_mean(
        ordered_pairs, factorial_pair_weight, pair_ratio
    )
    global_covariance = weighted_covariance(
        ordered_pairs,
        factorial_pair_weight,
        lambda pair: kernel(*pair),
        pair_ratio,
    )
    assert (
        global_factorial_mean - global_tail_mean
        == -global_covariance / global_mean_ratio
    )

    global_cells = defaultdict(list)
    for pair in ordered_pairs:
        global_cells[overlap_vector(*pair)].append(pair)
    global_cell_mass = {
        vector: sum(factorial_pair_weight(pair) for pair in cell)
        for vector, cell in global_cells.items()
    }
    global_cell_k = {
        vector: weighted_mean(
            cell, factorial_pair_weight, lambda pair: kernel(*pair)
        )
        for vector, cell in global_cells.items()
    }
    global_cell_s = {
        vector: weighted_mean(cell, factorial_pair_weight, pair_ratio)
        for vector, cell in global_cells.items()
    }
    vectors = sorted(global_cells)
    global_between = weighted_covariance(
        vectors,
        lambda vector: global_cell_mass[vector],
        lambda vector: global_cell_k[vector],
        lambda vector: global_cell_s[vector],
    )
    global_within_by_cell = {
        vector: weighted_covariance(
            cell,
            factorial_pair_weight,
            lambda pair: kernel(*pair),
            pair_ratio,
        )
        for vector, cell in global_cells.items()
    }
    global_bare_determinant = {}
    for vector, cell in global_cells.items():
        a12 = sum(l12_pair(pair) for pair in cell)
        ac = sum(lc_pair(pair) for pair in cell)
        b12 = sum(kernel(*pair) * l12_pair(pair) for pair in cell)
        bc = sum(kernel(*pair) * lc_pair(pair) for pair in cell)
        global_bare_determinant[vector] = a12 * bc - b12 * ac
        assert (
            global_within_by_cell[vector]
            == global_bare_determinant[vector] / a12**2
        )
    global_total_mass = sum(global_cell_mass.values())
    global_within = sum(
        global_cell_mass[vector] * global_within_by_cell[vector]
        for vector in vectors
    ) / global_total_mass
    assert global_covariance == global_between + global_within

    # The vector fixes q_{FH}; total overlap does not when shore probabilities differ.
    q_by_vector = defaultdict(set)
    q_by_total = defaultdict(set)
    for first, second in combinations(star, 2):
        vector = overlap_vector(first, second)
        q_by_vector[vector].add(q_pair(first, second))
        q_by_total[sum(vector)].add(q_pair(first, second))
    assert all(len(values) == 1 for values in q_by_vector.values())
    total_q_witness = next(
        (total, values) for total, values in q_by_total.items() if len(values) > 1
    )

    # Even the two-shore vector is not a sufficient orbit statistic for the
    # conditional degree transforms: give exact witnesses at fixed first row.
    vector_nonsufficiency_witness = None
    signed_within_cell_witness = None

    for pos, first in representatives.items():
        seconds = [second for second in star if second != first]

        def l12(second):
            return pair_profile("factorial", first, second)

        def lc(second):
            return pair_profile("tail", first, second)

        def ratio(second):
            return lc(second) / l12(second)

        def palm_weight(second):
            return q_pair(first, second) * l12(second)

        cells_vector = defaultdict(list)
        cells_total = defaultdict(list)
        for second in seconds:
            vector = overlap_vector(first, second)
            cells_vector[vector].append(second)
            cells_total[sum(vector)].append(second)

        for vector, cell in cells_vector.items():
            profiles = {(l12(second), ratio(second)) for second in cell}
            if len(profiles) > 1 and vector_nonsufficiency_witness is None:
                left, right = next(combinations(cell, 2))
                while (l12(left), ratio(left)) == (l12(right), ratio(right)):
                    left, right = next(
                        pair
                        for pair in combinations(cell, 2)
                        if (l12(pair[0]), ratio(pair[0]))
                        != (l12(pair[1]), ratio(pair[1]))
                    )
                vector_nonsufficiency_witness = (
                    pos,
                    vector,
                    left,
                    right,
                    l12(left),
                    l12(right),
                    ratio(left),
                    ratio(right),
                )

        total_covariance = weighted_covariance(
            seconds, palm_weight, lambda second: kernel(first, second), ratio
        )

        def audit_partition(cells):
            cell_keys = sorted(cells)
            cell_mass = {
                key: sum(palm_weight(second) for second in cells[key])
                for key in cell_keys
            }
            mean_k = {
                key: weighted_mean(
                    cells[key], palm_weight, lambda second: kernel(first, second)
                )
                for key in cell_keys
            }
            mean_s = {
                key: weighted_mean(cells[key], palm_weight, ratio)
                for key in cell_keys
            }
            between = weighted_covariance(
                cell_keys,
                lambda key: cell_mass[key],
                lambda key: mean_k[key],
                lambda key: mean_s[key],
            )
            total_mass = sum(cell_mass.values())
            within_by_cell = {
                key: weighted_covariance(
                    cells[key],
                    palm_weight,
                    lambda second: kernel(first, second),
                    ratio,
                )
                for key in cell_keys
            }
            within = sum(
                cell_mass[key] * within_by_cell[key] for key in cell_keys
            ) / total_mass
            assert total_covariance == between + within
            return between, within, within_by_cell, cell_mass

        total_split = audit_partition(cells_total)
        vector_split = audit_partition(cells_vector)

        for vector, covariance in vector_split[2].items():
            if covariance < 0 and signed_within_cell_witness is None:
                cell = cells_vector[vector]
                mass = sum(palm_weight(second) for second in cell)
                sum_klc = sum(
                    q_pair(first, second)
                    * kernel(first, second)
                    * lc(second)
                    for second in cell
                )
                sum_kl12 = sum(
                    q_pair(first, second)
                    * kernel(first, second)
                    * l12(second)
                    for second in cell
                )
                sum_lc = sum(
                    q_pair(first, second) * lc(second) for second in cell
                )
                # q is constant in a vector cell.  This numerator has the
                # sign of Cov_{Palm(.|cell)}(K,S).
                determinant = mass * sum_klc - sum_kl12 * sum_lc
                assert sign(determinant) == sign(covariance)
                bare_l12 = sum(l12(second) for second in cell)
                bare_klc = sum(kernel(first, second) * lc(second) for second in cell)
                bare_kl12 = sum(
                    kernel(first, second) * l12(second) for second in cell
                )
                bare_lc = sum(lc(second) for second in cell)
                bare_determinant = (
                    bare_l12 * bare_klc - bare_kl12 * bare_lc
                )
                assert sign(bare_determinant) == sign(covariance)
                signed_within_cell_witness = (
                    pos,
                    vector,
                    len(cell),
                    covariance,
                    determinant,
                    bare_determinant,
                )

        print(
            "position",
            pos,
            "total cov sign",
            sign(total_covariance),
            "total-overlap (between,within) signs",
            (sign(total_split[0]), sign(total_split[1])),
            "shore-vector (between,within) signs",
            (sign(vector_split[0]), sign(vector_split[1])),
        )

    assert vector_nonsufficiency_witness is not None
    assert signed_within_cell_witness is not None

    assert total_q_witness[0] == 6
    assert total_q_witness[1] == {
        Fraction(81, 8192),
        Fraction(243, 16384),
    }
    assert sign(global_covariance) == sign(global_between) == sign(global_within) == 1
    expected_global_negative = {
        (1, 4): Fraction(
            -69353265067384988728156624982046766080, 267007
        ),
        (2, 3): Fraction(
            -26194450716406951846138782153558720000, 267007
        ),
    }
    assert {
        vector: value
        for vector, value in global_bare_determinant.items()
        if value < 0
    } == expected_global_negative

    pos, witness_vector, left, right, l12_left, l12_right, s_left, s_right = (
        vector_nonsufficiency_witness
    )
    assert pos == 1 and witness_vector == (1, 4)
    assert words[representatives[pos]] == (4, 1, 0, 2, 3)
    assert words[left] == (4, 3, 1, 0, 2)
    assert words[right] == (4, 2, 1, 0, 3)
    assert l12_left - l12_right == Fraction(51374238358275, 2)
    assert s_left - s_right == Fraction(
        -2437815679298638170531944948888,
        2916882906010537645991730793611375,
    )
    print("PASS: exact overlap-cell covariance decompositions")
    print(
        "global shore-vector (total,between,within) signs",
        (sign(global_covariance), sign(global_between), sign(global_within)),
    )
    print(
        "global negative within-vector cells",
        [vector for vector in vectors if global_within_by_cell[vector] < 0],
    )
    for vector in vectors:
        if global_within_by_cell[vector] < 0:
            value = global_bare_determinant[vector]
            print(
                "global negative cell certificate",
                vector,
                "size",
                len(global_cells[vector]),
                "numerator",
                value.numerator,
                "denominator",
                value.denominator,
            )
    print("total overlap fails to fix q_FH; two-shore overlap fixes q_FH")
    print(
        "total-overlap q witness:",
        total_q_witness[0],
        sorted(total_q_witness[1]),
    )
    print(
        "two-shore vector does not fix conditional transforms:",
        "position",
        pos,
        "vector",
        witness_vector,
        "second rows",
        left,
        right,
    )
    print("first word", words[representatives[pos]])
    print("left second word", words[left])
    print("right second word", words[right])
    print("L12 equal", l12_left == l12_right, "S equal", s_left == s_right)
    print("L12 difference", l12_left - l12_right)
    print("S difference", s_left - s_right)
    pos, vector, size, covariance, determinant, bare_determinant = (
        signed_within_cell_witness
    )
    print(
        "first negative within-vector cell:",
        "position",
        pos,
        "vector",
        vector,
        "size",
        size,
    )
    print("within covariance sign", sign(covariance))
    print("determinant sign", sign(determinant))
    print("determinant numerator", determinant.numerator)
    print("determinant denominator", determinant.denominator)
    print("bare determinant numerator", bare_determinant.numerator)
    print("bare determinant denominator", bare_determinant.denominator)


if __name__ == "__main__":
    main()
