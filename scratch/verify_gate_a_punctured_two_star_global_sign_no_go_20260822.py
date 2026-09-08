#!/usr/bin/env python3
"""Exact r=2 counterexample to a global favorable two-star sign.

The program constructs the complete directed-punctured catalogue, evaluates
the signed two-star kernel, and compares its factorial and cutoff-tail pair
means using rational arithmetic only.
"""

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


def catalogue(r):
    b = 2 * r + 1
    targets = (
        [("M", s) for s in combinations(range(b), r)]
        + [("L", s) for s in combinations(range(b), r - 1)]
    )
    target_id = {target: i for i, target in enumerate(targets)}
    rows = set()
    for word in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(sorted(word[(start + j) % b] for j in range(r)))
            lower = tuple(sorted(word[(start + j) % b] for j in range(r - 1)))
            row.append(target_id[("M", middle)])
            row.append(target_id[("L", lower)])
        rows.add(tuple(sorted(row)))
    rows = sorted(rows)
    assert len(rows) == factorial(b)
    masks = [sum(1 << u for u in row) for row in rows]
    return targets, rows, masks


def mask_product(values, mask):
    out = Fraction(1)
    for i, value in enumerate(values):
        if mask & (1 << i):
            out *= value
    return out


def superset_zeta(values, bit_count):
    out = list(values)
    for bit in range(bit_count):
        flag = 1 << bit
        for mask in range(1 << bit_count):
            if not mask & flag:
                out[mask] += out[mask | flag]
    return out


def main():
    r = 2
    targets, rows, row_masks = catalogue(r)
    target_count = len(targets)
    state_count = 1 << target_count
    full_mask = state_count - 1

    p_middle = Fraction(9, 10)
    p_lower = Fraction(1, 10)
    probabilities = [
        p_middle if shore == "M" else p_lower for shore, _ in targets
    ]
    inverse = [1 / p for p in probabilities]
    inverse_weight = [
        mask_product(inverse, state) for state in range(state_count)
    ]
    state_probability = [
        mask_product(probabilities, state)
        * mask_product(
            [1 - p for p in probabilities], full_mask ^ state
        )
        for state in range(state_count)
    ]

    root = next(i for i, target in enumerate(targets) if target[0] == "M")
    root_bit = 1 << root
    star = [i for i, row in enumerate(rows) if root in row]
    assert len(star) == 48
    pairs = list(combinations(star, 2))

    def two_star(first, second):
        total = Fraction(0)
        for further in row_masks:
            left = (further & row_masks[first]) & ~root_bit
            right = (further & row_masks[second]) & ~root_bit
            if not left or not right:
                continue
            if further & root_bit:
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

    kernels = [two_star(first, second) for first, second in pairs]
    unions = [row_masks[first] | row_masks[second] for first, second in pairs]
    degrees = [
        sum(row_masks[row] & ~state == 0 for row in star)
        for state in range(state_count)
    ]

    factorial_integrand = [
        state_probability[state] * falling(degrees[state] - 2, 10)
        for state in range(state_count)
    ]
    cutoff = 47
    tail_integrand = [
        state_probability[state]
        * (
            Fraction((degrees[state] - cutoff) ** 12, falling(degrees[state], 2))
            if degrees[state] > cutoff
            else 0
        )
        for state in range(state_count)
    ]
    factorial_conditioned = superset_zeta(factorial_integrand, target_count)
    tail_conditioned = superset_zeta(tail_integrand, target_count)
    factorial_weights = [factorial_conditioned[union] for union in unions]
    tail_weights = [tail_conditioned[union] for union in unions]

    def mean(weights):
        return sum(w * k for w, k in zip(weights, kernels)) / sum(weights)

    factorial_mean = mean(factorial_weights)
    tail_mean = mean(tail_weights)
    delta = factorial_mean - tail_mean

    expected_factorial_mean = Fraction(
        27541902730054743803792, 53417259809424225
    )
    expected_tail_mean = Fraction(158982160240, 308367)
    expected_delta = Fraction(94888059014964404224, 2510611211042938575)
    expected_normalized = Fraction(
        2965251844217637632, 4184352018404897625
    )

    assert factorial_mean == expected_factorial_mean
    assert tail_mean == expected_tail_mean
    assert delta == expected_delta > 0

    # Every row has four targets on each shore.  For a middle root,
    # z = 48 p_M^3 p_L^4 and q_0 = p_M^4 p_L^4, so q_0/z = p_M/48.
    normalized = p_middle * delta / 48
    assert normalized == expected_normalized > 0

    print("factorial mean:", factorial_mean)
    print("cutoff-tail mean:", tail_mean)
    print("Delta_2,47:", delta)
    print("q_0 Delta_2,47 / z:", normalized)
    print("decimal normalized value:", float(normalized))


if __name__ == "__main__":
    main()
