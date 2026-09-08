#!/usr/bin/env python3
"""Finite exact checks for rooted conflict-exposure identities."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, prod
from random import Random


def conflict_neighborhoods(edges):
    return [
        {j for j, g in enumerate(edges) if f & g}
        for f in edges
    ]


def degrees(edges, vertices):
    return {v: sum(v in e for e in edges) for v in vertices}


def residual_from_marks(edges, marked):
    gamma = conflict_neighborhoods(edges)
    accepted = {
        e for e in marked
        if not ((gamma[e] - {e}) & marked)
    }
    deleted = set().union(*(edges[e] for e in accepted)) if accepted else set()
    surviving_vertices = set().union(*edges) - deleted
    surviving_edges = [e for e in edges if not (e & deleted)]
    return surviving_vertices, surviving_edges, accepted


def falling(x, ell):
    return prod(range(x - ell + 1, x + 1)) if ell else 1


def stirling2(j, ell):
    table = [[0] * (j + 1) for _ in range(j + 1)]
    table[0][0] = 1
    for n in range(1, j + 1):
        for k in range(1, n + 1):
            table[n][k] = table[n - 1][k - 1] + k * table[n - 1][k]
    return table[j][ell]


def check_centered_factorial_reconstruction():
    rng = Random(61420260822)
    for _ in range(200):
        values = [rng.randrange(0, 20) for _ in range(rng.randrange(1, 15))]
        a = rng.randrange(-5, 20)
        coefficients = []
        for ell in range(7):
            coefficients.append(sum(
                Fraction(1) * comb(6, j) * ((-a) ** (6 - j)) * stirling2(j, ell)
                for j in range(ell, 7)
            ))
        lhs = sum((d - a) ** 6 for d in values)
        f = [sum(falling(d, ell) for d in values) for ell in range(7)]
        rhs = sum(coefficients[ell] * f[ell] for ell in range(7))
        assert lhs == rhs


def check_derivatives(edges):
    vertices = set().union(*edges)
    gamma = conflict_neighborhoods(edges)
    c = [len(x) for x in gamma]
    deg = degrees(edges, vertices)

    for v in vertices:
        star = [i for i, e in enumerate(edges) if v in e]
        d = deg[v]

        # Derivative at p=0 is the sum over one-mark states minus Z copies
        # of the zero-mark value.
        base_vertices, base_edges, _ = residual_from_marks(edges, set())
        assert v in base_vertices and len(base_edges) == len(edges)

        survival_derivative = 0
        degree_derivative = 0
        for e in range(len(edges)):
            vv, ee, _ = residual_from_marks(edges, {e})
            survival_derivative += int(v in vv) - 1
            degree_derivative += sum(v in f for f in ee) - d
        assert survival_derivative == -d
        assert degree_derivative == -sum(c[f] for f in star)

        for ell in range(1, min(4, d) + 1):
            base = falling(d, ell)
            derivative = 0
            for e in range(len(edges)):
                _, ee, _ = residual_from_marks(edges, {e})
                new_d = sum(v in f for f in ee)
                derivative += falling(new_d, ell) - base

            union_sum = 0
            for tup in permutations(star, ell):
                union_sum += len(set().union(*(gamma[f] for f in tup)))
            assert derivative == -union_sum


def fano_k4_example():
    fano = []
    for i in range(7):
        fano.append(frozenset({i, (i + 1) % 7, (i + 3) % 7}))
    assert len(set(fano)) == 7
    assert all(len(a & b) == 1 for a, b in combinations(fano, 2))

    k_vertices = range(7, 11)
    k4 = [frozenset(c) for c in combinations(k_vertices, 3)]
    edges = fano + k4
    vertices = set(range(11))
    deg = degrees(edges, vertices)
    assert set(deg.values()) == {3}

    gamma = conflict_neighborhoods(edges)
    c = [len(x) for x in gamma]
    assert c[:7] == [7] * 7
    assert c[7:] == [4] * 4
    cbar = Fraction(sum(c), len(c))
    assert cbar == Fraction(65, 11)

    xi = {}
    for v in vertices:
        star = [i for i, e in enumerate(edges) if v in e]
        av = Fraction(sum(c[i] for i in star), len(star))
        ev = av - deg[v]
        xi[v] = ev - (cbar - 3)
    assert {xi[v] for v in range(7)} == {Fraction(12, 11)}
    assert {xi[v] for v in range(7, 11)} == {Fraction(-21, 11)}

    # The explicit positive-probability mark pattern in Theorem 6.
    vv, ee, accepted = residual_from_marks(edges, {0})
    assert accepted == {0}
    assert len(vv) == 8
    assert len(ee) == 4
    residual_deg = degrees(ee, vv)
    assert max(residual_deg.values()) == 3
    avg = Fraction(3 * len(ee), len(vv))
    assert avg == Fraction(3, 2)
    assert Fraction(max(residual_deg.values()), 1) / avg == 2

    check_derivatives(edges)


def random_derivative_checks():
    rng = Random(20260822)
    for n in range(5, 9):
        triples = [frozenset(c) for c in combinations(range(n), 3)]
        for _ in range(30):
            edges = rng.sample(triples, rng.randrange(3, min(9, len(triples)) + 1))
            check_derivatives(edges)


def main():
    fano_k4_example()
    random_derivative_checks()
    check_centered_factorial_reconstruction()
    print("PASS: rooted conflict exposure, factorial derivatives, and cap-only no-go")


if __name__ == "__main__":
    main()
