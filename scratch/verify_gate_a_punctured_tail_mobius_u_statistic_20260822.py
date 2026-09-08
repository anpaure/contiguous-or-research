#!/usr/bin/env python3
"""Exact checks for the punctured carrier-index Möbius/U-statistic reduction."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def falling(n, k):
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
    row_set = set()
    for word in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(sorted(word[(start + j) % b] for j in range(r)))
            lower = tuple(sorted(word[(start + j) % b] for j in range(r - 1)))
            row.append(target_index[("M", middle)])
            row.append(target_index[("L", lower)])
        row_set.add(tuple(sorted(row)))
    rows = sorted(row_set)
    assert len(rows) == factorial(b)
    masks = [sum(1 << u for u in row) for row in rows]
    return targets, rows, masks


def product_on_mask(values, mask):
    out = Fraction(1)
    for u, value in enumerate(values):
        if mask & (1 << u):
            out *= value
    return out


def main():
    targets, rows, row_masks = make_catalogue()
    probabilities = [
        Fraction(3, 4) if shore == "M" else Fraction(1, 2)
        for shore, _ in targets
    ]
    inverse = [1 / p for p in probabilities]
    all_target_mask = (1 << len(targets)) - 1
    inverse_weight = [
        product_on_mask(inverse, mask) for mask in range(all_target_mask + 1)
    ]
    state_probability = [
        product_on_mask(probabilities, mask)
        * product_on_mask(
            [1 - p for p in probabilities], all_target_mask ^ mask
        )
        for mask in range(all_target_mask + 1)
    ]

    root = next(i for i, target in enumerate(targets) if target[0] == "M")
    root_bit = 1 << root
    full_star = [i for i, row in enumerate(rows) if root in row]
    assert len(full_star) == 48

    # A deterministic eight-row root subcatalogue keeps the exhaustive
    # carrier/state calculation small.  K_s still sums over every G in the
    # complete 120-row punctured catalogue.
    allowed = tuple(full_star[::6][:8])
    assert len(allowed) == 8
    m = 3
    c = 3

    def g_value(carrier, further_mask, index_subset):
        union = 0
        for local_index in index_subset:
            carrier_mask = row_masks[carrier[local_index]]
            union |= (further_mask & carrier_mask) & ~root_bit
        if further_mask & root_bit:
            return inverse[root] * (inverse_weight[union] - 1)
        if union:
            return inverse_weight[union]
        return Fraction(0)

    def mobius_kernel(carrier, check_support=False):
        s = len(carrier)
        total = Fraction(0)
        for further_mask in row_masks:
            coefficient = Fraction(0)
            for subset_mask in range(1 << s):
                index_subset = [
                    i for i in range(s) if subset_mask & (1 << i)
                ]
                coefficient += (
                    -1 if (s - len(index_subset)) % 2 else 1
                ) * g_value(carrier, further_mask, index_subset)
            if check_support:
                all_linked = all(
                    ((further_mask & row_masks[row_id]) & ~root_bit) != 0
                    for row_id in carrier
                )
                if not all_linked:
                    assert coefficient == 0
            total += coefficient
        return total

    kernels = {}
    for s in range(2, m + 1):
        for carrier in combinations(allowed, s):
            kernels[carrier] = mobius_kernel(carrier, check_support=True)

    def xi_direct(carrier):
        total = Fraction(0)
        for further_mask in row_masks:
            offroot = [
                (further_mask & row_masks[row_id]) & ~root_bit
                for row_id in carrier
            ]
            union = 0
            for intersection in offroot:
                union |= intersection
            if further_mask & root_bit:
                total += inverse[root] * (
                    inverse_weight[union]
                    - sum(inverse_weight[a] for a in offroot)
                    + len(carrier) - 1
                )
            else:
                active = [a for a in offroot if a]
                if active:
                    total += inverse_weight[union] - sum(
                        inverse_weight[a] for a in active
                    )
        return total

    carriers = list(combinations(allowed, m))
    xi = {}
    for carrier in carriers:
        direct = xi_direct(carrier)
        expanded = sum(
            kernels[subcarrier]
            for s in range(2, m + 1)
            for subcarrier in combinations(carrier, s)
        )
        assert direct == expanded
        xi[carrier] = direct

    def carrier_union_mask(carrier):
        union = 0
        for row_id in carrier:
            union |= row_masks[row_id]
        return union

    carrier_probability = {
        carrier: product_on_mask(probabilities, carrier_union_mask(carrier))
        for carrier in carriers
    }
    carrier_normalizer = sum(carrier_probability.values())

    # Statewise Y_s, U-statistics, and direct sums over live m-carriers.
    state_data = []
    for state, probability in enumerate(state_probability):
        alive = tuple(row_id for row_id in allowed if row_masks[row_id] & ~state == 0)
        d = len(alive)
        y = {}
        averages = {}
        for s in range(2, m + 1):
            y[s] = sum(kernels[sub] for sub in combinations(alive, s))
            averages[s] = y[s] / comb(d, s) if d >= s else Fraction(0)

        live_carriers = list(combinations(alive, m)) if d >= m else []
        direct_state_sum = sum(xi[carrier] for carrier in live_carriers)
        extension_sum = sum(
            comb(d - s, m - s) * y[s] if d >= m else 0
            for s in range(2, m + 1)
        )
        assert direct_state_sum == extension_sum

        f = max(d - c, 0) ** m
        phi = Fraction(f, falling(d, m)) if d >= m else Fraction(0)
        state_data.append((probability, d, averages, f, phi, direct_state_sum))

    # Direct carrier-label Palm and tail-tilted means.
    direct_pi_xi = sum(
        carrier_probability[carrier] * xi[carrier] for carrier in carriers
    ) / carrier_normalizer

    tail_profile = {}
    for carrier in carriers:
        union = carrier_union_mask(carrier)
        q = carrier_probability[carrier]
        tail_profile[carrier] = sum(
            probability * phi
            for state, (probability, d, averages, f, phi, direct_sum)
            in enumerate(state_data)
            if union & ~state == 0
        ) / q

    tail_mass_pi = sum(
        carrier_probability[carrier] * tail_profile[carrier]
        for carrier in carriers
    ) / carrier_normalizer
    assert tail_mass_pi > 0
    direct_tau_xi = sum(
        carrier_probability[carrier] * tail_profile[carrier] * xi[carrier]
        for carrier in carriers
    ) / (carrier_normalizer * tail_mass_pi)

    factorial_normalizer = sum(
        probability * falling(d, m)
        for probability, d, averages, f, phi, direct_sum in state_data
    )
    tail_normalizer = sum(
        probability * f
        for probability, d, averages, f, phi, direct_sum in state_data
    )
    assert factorial_normalizer == factorial(m) * carrier_normalizer

    collapsed_pi = sum(
        comb(m, s)
        * sum(
            probability * falling(d, m) * averages[s]
            for probability, d, averages, f, phi, direct_sum in state_data
        )
        / factorial_normalizer
        for s in range(2, m + 1)
    )
    collapsed_tau = sum(
        comb(m, s)
        * sum(
            probability * f * averages[s]
            for probability, d, averages, f, phi, direct_sum in state_data
        )
        / tail_normalizer
        for s in range(2, m + 1)
    )
    assert direct_pi_xi == collapsed_pi
    assert direct_tau_xi == collapsed_tau

    print("PASS: punctured carrier Möbius/U-statistic identities")
    print("catalogue rows", len(rows), "full root star", len(full_star))
    print("checked subcatalogue rows", len(allowed), "carrier order", m)
    print("Palm Xi", direct_pi_xi)
    print("tail-tilted Xi", direct_tau_xi)
    print("Palm minus tail", direct_pi_xi - direct_tau_xi)


if __name__ == "__main__":
    main()
