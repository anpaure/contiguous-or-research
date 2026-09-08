#!/usr/bin/env python3
"""Exact finite checks for current-scale external-row identities."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, prod
from random import Random


def falling(n, k):
    if k == 0:
        return 1
    if n < k:
        return 0
    return prod(range(n - k + 1, n + 1))


def punctured_hypergraph(r):
    b = 2 * r + 1
    middle = list(combinations(range(b), r))
    lower = list(combinations(range(b), r - 1))
    ids = {("M", x): i for i, x in enumerate(middle)}
    offset = len(middle)
    ids.update({("L", x): offset + i for i, x in enumerate(lower)})
    kinds = ["M"] * len(middle) + ["L"] * len(lower)
    edges = []
    for word in permutations(range(b)):
        edge = []
        for start in range(1, b):
            m = tuple(sorted(word[(start + i) % b] for i in range(r)))
            l = tuple(sorted(word[(start + i) % b] for i in range(r - 1)))
            edge.extend((ids[("M", m)], ids[("L", l)]))
        edges.append(frozenset(edge))
    assert len(edges) == len(set(edges))
    return edges, kinds


def setup(edges, vertices):
    stars = [{i for i, edge in enumerate(edges) if v in edge} for v in vertices]
    gamma = [
        {j for j, other in enumerate(edges) if edge & other}
        for edge in edges
    ]
    return stars, gamma


def monomial_probability(required, kinds, probabilities):
    answer = Fraction(1)
    for v in required:
        answer *= probabilities[kinds[v]]
    return answer


def check_conditional_mean_and_powered_expansion():
    r = 2
    edges, kinds = punctured_hypergraph(r)
    vertices = range(len(kinds))
    stars, gamma = setup(edges, vertices)
    g_index = 0
    g = edges[g_index]
    v = next(v for v in vertices if kinds[v] == "M" and v not in g)
    probabilities = {"M": Fraction(3, 4), "L": Fraction(2, 3)}
    x = min(probabilities.values())
    q0 = probabilities["M"] ** (2 * r) * probabilities["L"] ** (2 * r)
    degree = len(stars[v])
    mu = degree * q0 / probabilities[kinds[v]]

    kernel = Fraction(0)
    kernel2 = Fraction(0)
    direct_mean = Fraction(0)
    roots = set(g) | {v}
    family = [f for f in stars[v] if edges[f] & g]
    for f_index in stars[v]:
        f = edges[f_index]
        overlap = f & g
        if not overlap:
            continue
        weight = prod(
            (Fraction(1, probabilities[kinds[u]]) for u in overlap),
            start=Fraction(1),
        )
        kernel += weight / degree
        kernel2 += weight * weight / degree
        direct_mean += monomial_probability(f - roots, kinds, probabilities)
    assert direct_mean == mu * kernel
    candidate_count = len(family)
    assert kernel * kernel <= Fraction(candidate_count, degree) * kernel2

    # Exact three-carrier factorization, both unconditioned and rooted at v.
    f1, f2 = family[0], family[1]
    event_g = monomial_probability(g, kinds, probabilities)
    event_gf1 = monomial_probability(g | edges[f1], kinds, probabilities)
    event_gf2 = monomial_probability(g | edges[f2], kinds, probabilities)
    event_all = monomial_probability(g | edges[f1] | edges[f2], kinds, probabilities)
    correction = prod(
        (
            probabilities[kinds[u]] ** (-1)
            for u in (edges[f1] & edges[f2]) - g
        ),
        start=Fraction(1),
    )
    assert event_all == event_gf1 * event_gf2 / event_g * correction

    root_probability = monomial_probability(roots, kinds, probabilities)
    p1_given_roots = monomial_probability(edges[f1] - roots, kinds, probabilities)
    p2_given_roots = monomial_probability(edges[f2] - roots, kinds, probabilities)
    pair_given_roots = event_all / root_probability
    rooted_correction = prod(
        (
            probabilities[kinds[u]] ** (-1)
            for u in (edges[f1] & edges[f2]) - roots
        ),
        start=Fraction(1),
    )
    assert pair_given_roots == p1_given_roots * p2_given_roots * rooted_correction

    # Exact second factorial moment and the weighted rooted-kernel bound
    # used in Theorem 2.2.
    second_factorial = Fraction(0)
    for left, right in permutations(family, 2):
        second_factorial += monomial_probability(
            (edges[left] | edges[right]) - roots, kinds, probabilities
        )
    rooted_row_max = Fraction(0)
    for left in family:
        row = Fraction(0)
        for right in stars[v] - {left}:
            overlap = (edges[left] & edges[right]) - {v}
            row += x ** (-len(overlap)) - 1
        rooted_row_max = max(rooted_row_max, row / degree)
    theorem_rhs = mu * mu * (kernel * kernel + rooted_row_max * kernel2)
    assert second_factorial <= theorem_rhs

    # Check the exact binomial expansion underlying W_c for c=2.
    c = 2
    activity = x ** (-c) - 1
    lhs = sum(x ** (-c * len(f & g)) for f in edges if f & g)
    rhs = len(gamma[g_index])
    for size in range(1, len(g) + 1):
        for subset in combinations(g, size):
            codegree = sum(set(subset) <= f for f in edges)
            rhs += activity**size * codegree
    assert lhs == rhs

    # Check the v/F interchange in the aggregate powered kernel.
    for kind in ("M", "L"):
        degree_kind = len(stars[next(u for u in vertices if kinds[u] == kind)])
        left = Fraction(0)
        for u in vertices:
            if kinds[u] != kind or u in g:
                continue
            left += sum(
                prod(
                    (probabilities[kinds[z]] ** (-c) for z in edges[f] & g),
                    start=Fraction(1),
                )
                for f in stars[u]
                if edges[f] & g
            ) / degree_kind
        right = Fraction(0)
        for f in range(len(edges)):
            if not edges[f] & g:
                continue
            external = sum(kinds[u] == kind and u not in g for u in edges[f])
            weight = prod(
                (probabilities[kinds[z]] ** (-c) for z in edges[f] & g),
                start=Fraction(1),
            )
            right += external * weight / degree_kind
        assert left == right

    # Finite checks of the six-carrier conditional envelope (8.15).
    rng = Random(20260822)
    candidates = [f for f in stars[v] if edges[f] & g]
    other_star = list(stars[v])
    w = q0 / probabilities[kinds[v]]
    for _ in range(100):
        f1, f2 = rng.sample(candidates, 2)
        attachments = rng.sample(list(set(other_star) - {f1, f2}), 4)
        carriers = [f1, f2] + attachments

        centred_expectation = Fraction(0)
        for subset_size in range(5):
            for subset in combinations(attachments, subset_size):
                required_edges = [f1, f2] + list(subset)
                required_targets = set().union(*(edges[f] for f in required_edges))
                probability = monomial_probability(
                    required_targets - roots, kinds, probabilities
                )
                centred_expectation += (-w) ** (4 - subset_size) * probability

        s_values = []
        for f in carriers:
            overlap = edges[f] & g
            if overlap:
                s_values.append(
                    prod(
                        (
                            probabilities[kinds[u]] ** (-1)
                            for u in overlap
                        ),
                        start=Fraction(1),
                    )
                )
            else:
                s_values.append(Fraction(1))
        powered_overlap = 0
        for left, right in combinations(carriers, 2):
            powered_overlap += len((edges[left] & edges[right]) - roots)
        envelope = w**6 * prod(s_values) * x ** (-powered_overlap)
        assert abs(centred_expectation) <= 16 * envelope

        active_s = [
            value
            for value, f in zip(s_values, carriers)
            if edges[f] & g
        ]
        h = len(active_s)
        assert prod(active_s) <= sum(value**h for value in active_s) / h


def residual_quantities(edges, kinds, retained, ell):
    surviving = [i for i, edge in enumerate(edges) if edge <= retained]
    surviving_set = set(surviving)
    stars = {
        v: {i for i in surviving if v in edges[i]}
        for v in retained
    }
    q_value = 0
    tuple_value = 0
    for v in retained:
        d = len(stars[v])
        if d < ell:
            continue
        for g in surviving:
            if v in edges[g]:
                continue
            a = sum(bool(edges[f] & edges[g]) for f in stars[v])
            q_value += falling(a, 2) * falling(d - 2, ell - 2)
            for f1, f2 in permutations(stars[v], 2):
                if not (edges[f1] & edges[g]) or not (edges[f2] & edges[g]):
                    continue
                remaining = stars[v] - {f1, f2}
                tuple_value += falling(len(remaining), ell - 2)
    assert q_value == tuple_value
    max_degree = max((len(stars[v]) for v in retained), default=0)
    return q_value, max_degree


def check_positive_collision_expansion():
    edges, kinds = punctured_hypergraph(2)
    all_vertices = set(range(len(kinds)))
    test_states = [
        all_vertices,
        all_vertices - {0},
        all_vertices - {0, 3},
        all_vertices - {1, 7, 11},
    ]
    for retained in test_states:
        q2, maximum = residual_quantities(edges, kinds, retained, 2)
        for ell in range(2, 5):
            qell, check_maximum = residual_quantities(edges, kinds, retained, ell)
            assert check_maximum == maximum
            assert qell <= maximum ** (ell - 2) * q2


def conditional_slice_probability(n, m, roots, query):
    return Fraction(falling(m - roots, query), falling(n - roots, query))


def check_slice_formula():
    # Direct finite verification of the conditional hypergeometric formula.
    for n in range(12, 25):
        for m in range(7, n):
            for roots in range(1, min(5, m) + 1):
                for query in range(0, min(6, m - roots) + 1):
                    total = comb(n - roots, m - roots)
                    favourable = comb(n - roots - query, m - roots - query)
                    assert Fraction(favourable, total) == conditional_slice_probability(
                        n, m, roots, query
                    )


def second_difference_sixth(t):
    return t**6 - 2 * (t - 1) ** 6 + (t - 2) ** 6


def stirling_second(n, k):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def centred_falling_coefficient(z, ell):
    return sum(
        comb(6, j) * (-z) ** (6 - j) * stirling_second(j, ell)
        for j in range(ell, 7)
    )


def uniform_sum_moment(k):
    # E(U+V)^k for independent U,V uniform on [0,1].
    return sum(
        Fraction(comb(k, i), (i + 1) * (k - i + 1))
        for i in range(k + 1)
    )


def integrated_second_difference(t):
    expectation = sum(
        comb(4, k) * t ** (4 - k) * (-1) ** k * uniform_sum_moment(k)
        for k in range(5)
    )
    return 30 * expectation


def check_centered_row_defect():
    # Proposition 8.1: the full row defect is a shifted sum of second
    # differences, not merely the quadratic-multiplicity h=0 term.
    centres = [Fraction(-3, 2), Fraction(0), Fraction(7, 3), Fraction(10)]
    for z in centres:
        for d in range(0, 18):
            f = lambda u: (u - z) ** 6
            for a in range(d + 1):
                direct = a * (f(d) - f(d - 1)) - (f(d) - f(d - a))
                falling_basis = sum(
                    centred_falling_coefficient(z, ell)
                    * (
                        ell * a * falling(d - 1, ell - 1)
                        - (falling(d, ell) - falling(d - a, ell))
                    )
                    for ell in range(1, 7)
                )
                shifted = sum(
                    (a - 1 - h)
                    * (f(d - h) - 2 * f(d - h - 1) + f(d - h - 2))
                    for h in range(max(0, a - 1))
                )
                assert direct == falling_basis
                assert direct == shifted
                assert direct >= 0

                t = d - z
                polynomial = (
                    30 * t**4
                    - 120 * t**3
                    + 210 * t**2
                    - 180 * t
                    + 62
                )
                assert second_difference_sixth(t) == polynomial
                assert integrated_second_difference(t) == polynomial
                assert polynomial >= Fraction(5, 6)
                assert polynomial >= 30 * (t - 1) ** 4
                assert polynomial <= 30 * (abs(t) + 2) ** 4
                if a <= 2:
                    assert direct == Fraction(falling(a, 2), 2) * polynomial

    z = 10
    d = 10
    a = 3
    f = lambda u: (u - z) ** 6
    direct = a * (f(d) - f(d - 1)) - (f(d) - f(d - a))
    quadratic_only = Fraction(falling(a, 2), 2) * second_difference_sixth(d - z)
    assert direct == 726
    assert quadratic_only == 186
    assert direct != quadratic_only

    # Deterministic center shift, with a deliberately loose universal
    # constant obtained from the two-sided quartic comparison.
    shift_constant = 400_000
    for d in range(18):
        for a in range(d + 1):
            for z in centres:
                f = lambda u: (u - z) ** 6
                defect_z = a * (f(d) - f(d - 1)) - (f(d) - f(d - a))
                for shifted_z in centres:
                    shifted_f = lambda u: (u - shifted_z) ** 6
                    defect_shifted = a * (
                        shifted_f(d) - shifted_f(d - 1)
                    ) - (shifted_f(d) - shifted_f(d - a))
                    assert defect_shifted <= shift_constant * (
                        defect_z
                        + abs(shifted_z - z) ** 4 * falling(a, 2)
                    )

    # Exact positive falling-factorial expansion used for the A^4 tail.
    for a in range(30):
        assert falling(a, 2) * a**4 == (
            16 * falling(a, 2)
            + 65 * falling(a, 3)
            + 55 * falling(a, 4)
            + 14 * falling(a, 5)
            + falling(a, 6)
        )


def connected_components(n, edge_set):
    unseen = set(range(n))
    answer = []
    while unseen:
        root = unseen.pop()
        component = {root}
        stack = [root]
        while stack:
            u = stack.pop()
            neighbours = {
                v
                for v in range(n)
                if v != u and tuple(sorted((u, v))) in edge_set
            }
            new = neighbours & unseen
            unseen -= new
            component |= new
            stack.extend(new)
        answer.append(component)
    return answer


def check_centered_forest_constraint_count():
    # In Lemma 8.2, vertices 0,1 are the noncentred flower carriers and
    # vertices 2,...,5 are centred attachments.  R always contains 0,1.
    # Any dependency component disjoint from R must have size at least two;
    # hence there are at most two free such roots and at least three
    # candidate/tree costs among the other five vertices.
    n = 6
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edge_set = {
            pair for bit, pair in enumerate(pairs) if mask & (1 << bit)
        }
        components = connected_components(n, edge_set)
        for extra_r_mask in range(1 << 4):
            roots = {0, 1} | {
                2 + i for i in range(4) if extra_r_mask & (1 << i)
            }
            outside = [component for component in components if component.isdisjoint(roots)]
            if any(len(component) == 1 for component in outside):
                continue
            assert len(outside) <= 2
            small_costs = n - 1 - len(outside)
            assert small_costs >= 3


def main():
    check_conditional_mean_and_powered_expansion()
    check_positive_collision_expansion()
    check_slice_formula()
    check_centered_row_defect()
    check_centered_forest_constraint_count()
    print("PASS: current-scale external-row product/slice identities")


if __name__ == "__main__":
    main()
