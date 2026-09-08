#!/usr/bin/env python3
"""Exact r=3 check of the punctured Palm hazard-degree inversions."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


M = 12


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def catalogue():
    r = 3
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
    assert len(rows) == factorial(b) == 5040
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
    return targets, target_index, rows, row_masks, incidence, conflicts


def residual_roots(data, missing_middle, missing_lower):
    targets, target_index, rows, row_masks, incidence, conflicts = data
    state = (1 << len(targets)) - 1
    state &= ~(1 << target_index[("M", tuple(sorted(missing_middle)))])
    state &= ~(1 << target_index[("L", tuple(sorted(missing_lower)))])

    alive = 0
    for i, row_mask in enumerate(row_masks):
        if row_mask & ~state == 0:
            alive |= 1 << i
    alive_rows = [i for i in range(len(rows)) if alive & (1 << i)]
    z_rows = len(alive_rows)
    degrees = [(incidence[v] & alive).bit_count() for v in range(len(targets))]
    conflict_degree = {i: (conflicts[i] & alive).bit_count() for i in alive_rows}
    excess = {
        i: sum(degrees[v] for v in rows[i]) - conflict_degree[i]
        for i in alive_rows
    }

    output = []
    for v, target in enumerate(targets):
        degree = degrees[v]
        if degree < M:
            continue
        star = incidence[v] & alive
        star_rows = [i for i in alive_rows if star & (1 << i)]
        companion_raw = Fraction(
            sum(
                sum(degrees[u] for u in rows[i] if u != v)
                for i in star_rows
            ),
            degree,
        )
        repeated_intersection = Fraction(
            sum(excess[i] for i in star_rows), degree
        )
        external_exposure = companion_raw - repeated_intersection

        duplicate = Fraction(0)
        for g in alive_rows:
            if v in rows[g]:
                continue
            a_g = (star & conflicts[g]).bit_count()
            if not a_g:
                continue
            duplicate += (
                Fraction(M * a_g, degree)
                - 1
                + Fraction(falling(degree - a_g, M), falling(degree, M))
            )
        mean_hazard = degree + M * external_exposure - duplicate
        output.append(
            (target[0], degree, falling(degree, M), mean_hazard / z_rows)
        )
    return output


def main():
    data = catalogue()
    orbit_representatives = [
        ((0, 1, 2), (3, 4), 210),
        ((0, 1, 2), (0, 3), 420),
        ((0, 1, 2), (0, 1), 105),
    ]
    aggregate = defaultdict(lambda: [0, Fraction(0)])
    for middle, lower, orbit_size in orbit_representatives:
        for shore, degree, carrier_mass, normalized_hazard in residual_roots(
            data, middle, lower
        ):
            weight = orbit_size * carrier_mass
            aggregate[(shore, degree)][0] += weight
            aggregate[(shore, degree)][1] += weight * normalized_hazard

    expected = {
        ("M", 336): (
            712890041266595683494959155200000,
            Fraction(13024872042392062116997, 13024872409786236344800),
        ),
        ("M", 360): (
            1653472789066048199284914278400000,
            Fraction(
                2235525687519522070871431, 2235525879076321557398400
            ),
        ),
        ("L", 904): (
            348777979926295319417557795425730560000,
            Fraction(
                37273593396730211644099971989,
                37273593401732694120225886320,
            ),
        ),
        ("L", 912): (
            64653971485888926919287794438009856000,
            Fraction(
                10926671071114905752116222985,
                10926671079616552405470566332,
            ),
        ),
    }
    zeta = {}
    for key, (expected_mass, expected_zeta) in expected.items():
        mass, weighted_hazard = aggregate[key]
        value = weighted_hazard / mass
        assert mass == expected_mass
        assert value == expected_zeta
        zeta[key] = value

    middle_difference = zeta[("M", 360)] - zeta[("M", 336)]
    lower_difference = zeta[("L", 912)] - zeta[("L", 904)]
    assert middle_difference == Fraction(
        -38638925298524583531313366083931,
        672209791849300553006766641478067259520,
    )
    assert lower_difference == Fraction(
        -30176433336994070403791779508755991,
        46868446855715370703686778399001856387448080,
    )

    middle_support = sorted(d for shore, d in aggregate if shore == "M")
    lower_support = sorted(d for shore, d in aggregate if shore == "L")
    assert middle_support[middle_support.index(336) + 1] == 360
    assert lower_support[lower_support.index(904) + 1] == 912

    # Direct cross-product certificates before reducing the mean fractions.
    cross_expected = {
        ("M", 336, 360): Fraction(
            -1151830901063780635855141761027459967840634481696768000000000,
            17,
        ),
        ("L", 904, 912): Fraction(
            -14518829694116247471009902730923170977194708769871887961423872000000,
            1,
        ),
    }
    for shore, low, high in cross_expected:
        low_mass, low_sum = aggregate[(shore, low)]
        high_mass, high_sum = aggregate[(shore, high)]
        cross = high_sum * low_mass - low_sum * high_mass
        assert cross == cross_expected[(shore, low, high)]
        assert cross < 0

    print("PASS: exact r=3 punctured Palm hazard-degree monotonicity obstruction")
    print("middle adjacent difference", middle_difference)
    print("lower adjacent difference", lower_difference)
    print("catalogue rows", len(data[2]), "slice states", sum(x[2] for x in orbit_representatives))


if __name__ == "__main__":
    main()
