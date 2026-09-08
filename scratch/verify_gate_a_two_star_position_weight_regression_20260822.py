#!/usr/bin/env python3
"""Exact r=2 check of the signed position-weight/two-star regression."""

from fractions import Fraction
from itertools import combinations

from verify_gate_a_two_star_directional_tail_response_20260822 import (
    falling,
    make_catalogue,
    product_on_mask,
    superset_zeta,
)


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
    root_subset = targets[root][1]
    star = [row_id for row_id, row in enumerate(rows) if root in row]
    assert len(star) == 48

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
    representatives = {}
    for pos in range(1, 5):
        orbit = [row_id for row_id in star if position[row_id] == pos]
        assert len(orbit) == 12
        representatives[pos] = orbit[0]

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

    extension_mass = {
        first: sum(q_pair(first, second) for second in star if second != first)
        for first in star
    }
    a_profile = {
        first: sum(
            q_pair(first, second) * kernel(first, second)
            for second in star
            if second != first
        )
        / extension_mass[first]
        for first in star
    }
    for profile in (extension_mass, a_profile):
        for pos in range(1, 5):
            assert len({profile[row_id] for row_id in star if position[row_id] == pos}) == 1

    degree = [
        sum(row_masks[row_id] & ~state == 0 for row_id in star)
        for state in range(state_count)
    ]
    m = 12
    c = 12
    weights = {
        "factorial": [Fraction(falling(d - 2, m - 2)) for d in degree],
        "tail": [
            Fraction(max(d - c, 0) ** m, falling(d, 2))
            if d >= 2
            else Fraction(0)
            for d in degree
        ],
    }

    outputs = {}
    for name, g_values in weights.items():
        raw = superset_zeta(
            [state_probability[state] * g_values[state] for state in range(state_count)],
            target_count,
        )

        def l_pair(first, second):
            union = row_masks[first] | row_masks[second]
            return raw[union] / q_pair(first, second)

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

        position_weight = {
            pos: extension_mass[representatives[pos]] * ell[representatives[pos]]
            for pos in range(1, 5)
        }
        position_normalizer = sum(position_weight.values())
        pi = {pos: position_weight[pos] / position_normalizer for pos in range(1, 5)}

        connected = {}
        for pos in range(1, 5):
            first = representatives[pos]
            covariance = sum(
                q_pair(first, second)
                * (kernel(first, second) - a_profile[first])
                * (l_pair(first, second) - ell[first])
                for second in star
                if second != first
            ) / extension_mass[first]
            connected[pos] = covariance / ell[first]

        direct = sum(
            q_pair(first, second)
            * kernel(first, second)
            * l_pair(first, second)
            for first in star
            for second in star
            if second != first
        ) / sum(
            q_pair(first, second) * l_pair(first, second)
            for first in star
            for second in star
            if second != first
        )
        by_position = sum(
            pi[pos] * (a_profile[representatives[pos]] + connected[pos])
            for pos in range(1, 5)
        )
        assert direct == by_position

        # Equation (2.3), including the literal statewise extension count.
        for pos in range(1, 5):
            first = representatives[pos]
            left = extension_mass[first] * ell[first]
            right = sum(
                state_probability[state]
                * int(row_masks[first] & ~state == 0)
                * (degree[state] - 1)
                * g_values[state]
                for state in range(state_count)
            )
            assert left == right

        l_values = {
            (first, second): l_pair(first, second)
            for first in star
            for second in star
            if second != first
        }
        outputs[name] = (pi, connected, direct, ell, l_values)

    pi_12, connected_12, direct_12, ell_12, l_12 = outputs["factorial"]
    pi_c, connected_c, direct_c, ell_c, l_c = outputs["tail"]
    ratio = {pos: pi_c[pos] / pi_12[pos] for pos in range(1, 5)}
    mean_ratio = sum(pi_12[pos] * ratio[pos] for pos in range(1, 5))
    assert mean_ratio == 1

    a_pos = {pos: a_profile[representatives[pos]] for pos in range(1, 5)}
    one_body_difference = sum(
        (pi_12[pos] - pi_c[pos]) * a_pos[pos] for pos in range(1, 5)
    )
    covariance_a = sum(
        pi_12[pos]
        * (a_pos[pos] - sum(pi_12[j] * a_pos[j] for j in range(1, 5)))
        * (ratio[pos] - 1)
        for pos in range(1, 5)
    )
    assert one_body_difference == -covariance_a

    b_pos = {pos: a_pos[pos] + connected_12[pos] for pos in range(1, 5)}
    mean_b = sum(pi_12[pos] * b_pos[pos] for pos in range(1, 5))
    covariance_b = sum(
        pi_12[pos] * (b_pos[pos] - mean_b) * (ratio[pos] - 1)
        for pos in range(1, 5)
    )
    combined = -covariance_b + sum(
        pi_c[pos] * (connected_12[pos] - connected_c[pos])
        for pos in range(1, 5)
    )
    assert direct_12 - direct_c == combined

    nested_within = Fraction(0)
    for pos in range(1, 5):
        first = representatives[pos]
        ratio_mean = ell_c[first] / ell_12[first]
        mean_kernel = b_pos[pos]
        covariance = sum(
            q_pair(first, second)
            * l_12[(first, second)]
            * (kernel(first, second) - mean_kernel)
            * (l_c[(first, second)] / l_12[(first, second)] - ratio_mean)
            for second in star
            if second != first
        ) / (extension_mass[first] * ell_12[first])
        within_difference = (
            a_pos[pos] + connected_12[pos]
            - a_pos[pos] - connected_c[pos]
        )
        assert within_difference == -covariance / ratio_mean
        nested_within += pi_c[pos] * within_difference

    assert direct_12 - direct_c == -covariance_b + nested_within

    print("PASS: signed two-star position-weight regression")
    print("position types", len(representatives), "rows per type", 12)
    print("position-profile range", max(a_pos.values()) - min(a_pos.values()))
    print("one-body difference", one_body_difference)
    print("connected-response difference", sum(
        pi_12[pos] * connected_12[pos] - pi_c[pos] * connected_c[pos]
        for pos in range(1, 5)
    ))
    print("full two-star difference", direct_12 - direct_c)


if __name__ == "__main__":
    main()
