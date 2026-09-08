#!/usr/bin/env python3
"""Exact r=2 regression for the punctured connected-carrier identity."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


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
    assert len(rows) == factorial(b) == 120
    row_masks = [sum(1 << v for v in row) for row in rows]
    incidence = [
        sum(1 << i for i, row in enumerate(rows) if v in row)
        for v in range(len(targets))
    ]
    conflicts = []
    for row in rows:
        mask = 0
        for v in row:
            mask |= incidence[v]
        conflicts.append(mask)
    return targets, rows, row_masks, incidence, conflicts


def subsets(mask):
    current = mask
    while True:
        yield current
        if current == 0:
            return
        current = (current - 1) & mask


def main():
    targets, rows, row_masks, incidence, conflicts = make_catalogue()
    probabilities = [
        Fraction(3, 4) if shore == "M" else Fraction(1, 2)
        for shore, _ in targets
    ]
    activities = [(1 - p) / p for p in probabilities]

    def product_on_mask(values, mask):
        output = Fraction(1)
        for u, value in enumerate(values):
            if mask & (1 << u):
                output *= value
        return output

    inverse_probabilities = [1 / p for p in probabilities]
    mask_count = 1 << len(targets)
    inverse_weight = [
        product_on_mask(inverse_probabilities, mask) for mask in range(mask_count)
    ]
    activity_weight = [
        product_on_mask(activities, mask) for mask in range(mask_count)
    ]
    state_probability = [
        product_on_mask(probabilities, mask)
        * product_on_mask(
            [1 - p for p in probabilities], (mask_count - 1) ^ mask
        )
        for mask in range(mask_count)
    ]
    row_probability = product_on_mask(probabilities, row_masks[0])
    assert all(
        product_on_mask(probabilities, row_mask) == row_probability
        for row_mask in row_masks
    )

    def one_body(row_id):
        carrier_mask = row_masks[row_id]
        return row_probability * sum(
            inverse_weight[row_mask & carrier_mask]
            for row_mask in row_masks
            if row_mask & carrier_mask
        )

    one_body_values = [one_body(i) for i in range(len(rows))]
    assert len(set(one_body_values)) == 1
    one_body_constant = one_body_values[0]

    def connected_statistic(carrier, verify_expansion=False):
        carrier_masks = [row_masks[i] for i in carrier]
        carrier_union = 0
        for mask in carrier_masks:
            carrier_union |= mask
        total = Fraction(0)
        for row_mask in row_masks:
            intersections = [row_mask & mask for mask in carrier_masks]
            live_intersections = [mask for mask in intersections if mask]
            if not live_intersections:
                continue
            union = row_mask & carrier_union
            direct = inverse_weight[union]
            singles = sum(
                inverse_weight[mask] for mask in live_intersections
            )
            summand = direct - singles

            # Independently reconstruct the signed subset-activity expansion.
            if verify_expansion:
                expansion = Fraction(0)
                for target_subset in subsets(union):
                    containment_count = sum(
                        target_subset & ~mask == 0 for mask in live_intersections
                    )
                    expansion += (
                        1 - containment_count
                    ) * activity_weight[target_subset]
                assert summand == expansion
            if len(live_intersections) <= 1:
                assert summand == 0
            total += summand
        return total

    def direct_mean_hazard(carrier):
        carrier_union = 0
        for row_id in carrier:
            carrier_union |= row_masks[row_id]
        return row_probability * sum(
            inverse_weight[row_mask & carrier_union]
            for row_mask in row_masks
            if any(row_mask & row_masks[row_id] for row_id in carrier)
        )

    root = next(i for i, target in enumerate(targets) if target[0] == "M")
    star = [i for i, row in enumerate(rows) if root in row]
    carriers = list(combinations(star, 2))
    assert len(star) == 48 and len(carriers) == 1128

    connected = {}
    rooted_connected = {}
    for carrier_index, carrier in enumerate(carriers):
        xi = connected_statistic(carrier, verify_expansion=carrier_index < 16)
        connected[carrier] = xi
        assert direct_mean_hazard(carrier) == 2 * one_body_constant + row_probability * xi

        carrier_masks = [row_masks[i] for i in carrier]
        xi_circ = Fraction(0)
        for row_mask in row_masks:
            off_root_intersections = [
                (row_mask & carrier_mask) & ~(1 << root)
                for carrier_mask in carrier_masks
            ]
            active = [mask for mask in off_root_intersections if mask]
            union = 0
            for mask in active:
                union |= mask
            if row_mask & (1 << root):
                summand = inverse_probabilities[root] * (
                    inverse_weight[union]
                    - sum(inverse_weight[mask] for mask in off_root_intersections)
                    + len(carrier) - 1
                )
            else:
                summand = (
                    inverse_weight[union]
                    - sum(inverse_weight[mask] for mask in active)
                    if active
                    else Fraction(0)
                )
            if len(active) <= 1:
                assert summand == 0
            xi_circ += summand
        rooted_connected[carrier] = xi_circ
        constant_root_cluster = (
            (1 - len(carrier)) * inverse_probabilities[root] * len(star)
        )
        assert xi == constant_root_cluster + xi_circ

    # Verify the full Palm covariance decomposition for a nonconstant tail.
    tail_threshold = 4
    alive_by_state = []
    degree_by_state = []
    for state in range(mask_count):
        alive = 0
        for row_id, row_mask in enumerate(row_masks):
            if row_mask & ~state == 0:
                alive |= 1 << row_id
        alive_by_state.append(alive)
        degree_by_state.append((incidence[root] & alive).bit_count())

    profiles = []
    for carrier in carriers:
        carrier_union = row_masks[carrier[0]] | row_masks[carrier[1]]
        carrier_probability = product_on_mask(probabilities, carrier_union)
        free_targets = [
            u for u in range(len(targets)) if not (carrier_union & (1 << u))
        ]
        mean_hazard = Fraction(0)
        mean_tail = Fraction(0)
        mean_product = Fraction(0)
        carrier_conflicts = conflicts[carrier[0]] | conflicts[carrier[1]]
        for bits in range(1 << len(free_targets)):
            state = carrier_union
            for j, u in enumerate(free_targets):
                if bits & (1 << j):
                    state |= 1 << u
            probability = state_probability[state] / carrier_probability
            alive = alive_by_state[state]
            degree = degree_by_state[state]
            hazard = (carrier_conflicts & alive).bit_count()
            tail = int(degree >= tail_threshold)
            mean_hazard += probability * hazard
            mean_tail += probability * tail
            mean_product += probability * hazard * tail
        assert mean_hazard == direct_mean_hazard(carrier)
        profiles.append(
            (
                carrier_probability,
                mean_hazard,
                mean_tail,
                mean_product,
                rooted_connected[carrier],
            )
        )

    normalizer = sum(profile[0] for profile in profiles)
    palm_hazard = sum(q * h for q, h, p, hp, xi in profiles) / normalizer
    palm_tail = sum(q * p for q, h, p, hp, xi in profiles) / normalizer
    palm_product = sum(q * hp for q, h, p, hp, xi in profiles) / normalizer
    full_covariance = palm_product - palm_hazard * palm_tail
    within = sum(q * (hp - h * p) for q, h, p, hp, xi in profiles) / normalizer
    mean_xi = sum(q * xi for q, h, p, hp, xi in profiles) / normalizer
    mean_xi_tail = sum(q * xi * p for q, h, p, hp, xi in profiles) / normalizer
    between_connected = row_probability * (
        mean_xi_tail - mean_xi * palm_tail
    )
    assert full_covariance == within + between_connected
    assert within >= 0 and palm_tail > 0

    print("PASS: exact punctured product connected-carrier decomposition")
    print("catalogue rows", len(rows), "root-star rows", len(star))
    print("one-body conditional hazard", one_body_constant)
    print("Palm tail mass", palm_tail)
    print("within-carrier covariance", within)
    print("connected between-carrier covariance", between_connected)
    print("full covariance", full_covariance)


if __name__ == "__main__":
    main()
