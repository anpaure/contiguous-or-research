#!/usr/bin/env python3
"""Exact r=2 check of the directional two-star tail-response identity."""

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


def make_catalogue(r=2):
    b = 2 * r + 1
    targets = (
        [("M", s) for s in combinations(range(b), r)]
        + [("L", s) for s in combinations(range(b), r - 1)]
    )
    target_index = {target: i for i, target in enumerate(targets)}
    row_word = {}
    for word in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(sorted(word[(start + j) % b] for j in range(r)))
            lower = tuple(sorted(word[(start + j) % b] for j in range(r - 1)))
            row.append(target_index[("M", middle)])
            row.append(target_index[("L", lower)])
        row = tuple(sorted(row))
        row_word[row] = word
    rows = sorted(row_word)
    assert len(rows) == factorial(b)
    row_masks = [sum(1 << u for u in row) for row in rows]
    words = [row_word[row] for row in rows]
    return targets, rows, row_masks, words


def product_on_mask(values, mask):
    out = Fraction(1)
    for u, value in enumerate(values):
        if mask & (1 << u):
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


def subset_zeta(values, bit_count):
    output = list(values)
    for bit in range(bit_count):
        flag = 1 << bit
        for mask in range(1 << bit_count):
            if mask & flag:
                output[mask] += output[mask ^ flag]
    return output


def main():
    targets, rows, row_masks, words = make_catalogue()
    probabilities = [
        Fraction(3, 4) if shore == "M" else Fraction(1, 2)
        for shore, _ in targets
    ]
    inverse = [1 / p for p in probabilities]
    target_count = len(targets)
    state_count = 1 << target_count
    all_target_mask = state_count - 1
    inverse_weight = [
        product_on_mask(inverse, mask) for mask in range(state_count)
    ]
    state_probability = [
        product_on_mask(probabilities, mask)
        * product_on_mask(
            [1 - p for p in probabilities], all_target_mask ^ mask
        )
        for mask in range(state_count)
    ]

    root = next(i for i, target in enumerate(targets) if target[0] == "M")
    root_bit = 1 << root
    star = [i for i, row in enumerate(rows) if root in row]
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
    assert {pos: sum(position[row_id] == pos for row_id in star) for pos in range(1, 5)} == {
        1: 12,
        2: 12,
        3: 12,
        4: 12,
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
        (first, second): two_star(first, second)
        for first, second in combinations(star, 2)
    }

    def kernel(first, second):
        return pair_kernel[tuple(sorted((first, second)))]

    row_probability = {
        row_id: product_on_mask(probabilities, row_masks[row_id])
        for row_id in star
    }
    assert len(set(row_probability.values())) == 1

    pair_probability = {}
    for first, second in combinations(star, 2):
        pair_probability[(first, second)] = product_on_mask(
            probabilities, row_masks[first] | row_masks[second]
        )

    def q_pair(first, second):
        return pair_probability[tuple(sorted((first, second)))]

    extension_mass = {
        first: sum(q_pair(first, second) for second in star if second != first)
        for first in star
    }
    assert len(set(extension_mass.values())) > 1

    kernel_profile = {
        first: sum(
            q_pair(first, second) * kernel(first, second)
            for second in star
            if second != first
        )
        / extension_mass[first]
        for first in star
    }
    for profile in (extension_mass, kernel_profile):
        for pos in range(1, 5):
            assert len({profile[row_id] for row_id in star if position[row_id] == pos}) == 1
    for first in star:
        assert sum(
            q_pair(first, second)
            * (kernel(first, second) - kernel_profile[first])
            for second in star
            if second != first
        ) == 0

    degree = []
    for state in range(state_count):
        degree.append(
            sum(row_masks[row_id] & ~state == 0 for row_id in star)
        )

    m = 12
    c = 12
    g_bulk = [Fraction(falling(d - 2, m - 2)) for d in degree]
    g_tail = [
        Fraction(max(d - c, 0) ** m, falling(d, 2)) if d >= 2 else Fraction(0)
        for d in degree
    ]

    # Y_2(state) is obtained by a superset zeta transform of the union-mask
    # weights.  Ordered pairs contribute twice each unordered pair.
    kernel_union_weight = [Fraction(0) for _ in range(state_count)]
    for (first, second), value in pair_kernel.items():
        kernel_union_weight[row_masks[first] | row_masks[second]] += 2 * value
    ordered_pair_kernel_sum = subset_zeta(kernel_union_weight, target_count)

    def check_weight(g_values, label):
        weighted_state = [
            state_probability[state] * g_values[state]
            for state in range(state_count)
        ]
        conditioned_raw = superset_zeta(weighted_state, target_count)

        pair_profile = {}
        for first, second in combinations(star, 2):
            union = row_masks[first] | row_masks[second]
            pair_profile[(first, second)] = (
                conditioned_raw[union] / q_pair(first, second)
            )

        def l_pair(first, second):
            return pair_profile[tuple(sorted((first, second)))]

        ell = {
            first: sum(
                q_pair(first, second) * l_pair(first, second)
                for second in star
                if second != first
            )
            / extension_mass[first]
            for first in star
        }
        for pos in range(1, 5):
            assert len({ell[row_id] for row_id in star if position[row_id] == pos}) == 1

        denominator = sum(
            q_pair(first, second) * l_pair(first, second)
            for first in star
            for second in star
            if second != first
        )
        state_denominator = sum(
            state_probability[state]
            * falling(degree[state], 2)
            * g_values[state]
            for state in range(state_count)
        )
        assert denominator == state_denominator and denominator > 0

        direct = sum(
            q_pair(first, second)
            * kernel(first, second)
            * l_pair(first, second)
            for first in star
            for second in star
            if second != first
        ) / denominator

        state_direct = sum(
            state_probability[state]
            * g_values[state]
            * ordered_pair_kernel_sum[state]
            for state in range(state_count)
        ) / state_denominator
        assert direct == state_direct

        one_body = sum(
            extension_mass[first] * ell[first] * kernel_profile[first]
            for first in star
        ) / denominator
        connected = sum(
            q_pair(first, second)
            * (kernel(first, second) - kernel_profile[first])
            * (l_pair(first, second) - ell[first])
            for first in star
            for second in star
            if second != first
        ) / denominator
        assert direct == one_body + connected

        # Equation (2.7), checked directly by its state expansion.
        for first in star:
            left = extension_mass[first] * ell[first]
            right = sum(
                state_probability[state]
                * int(row_masks[first] & ~state == 0)
                * (degree[state] - 1)
                * g_values[state]
                for state in range(state_count)
            )
            assert left == right

        print(label, "direct", direct)
        print(label, "one-body", one_body)
        print(label, "pair-connected", connected)
        return direct, one_body, connected

    bulk = check_weight(g_bulk, "factorial")
    tail = check_weight(g_tail, "tail")
    assert bulk[0] - tail[0] == (bulk[1] - tail[1]) + (bulk[2] - tail[2])

    print("PASS: directional two-star tail-response identity")
    print("catalogue rows", len(rows), "root-star rows", len(star))
    print("rooted extension-mass levels", len(set(extension_mass.values())))
    print("two-star difference", bulk[0] - tail[0])


if __name__ == "__main__":
    main()
