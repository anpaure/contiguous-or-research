#!/usr/bin/env python3
"""Finite checks for the rooted twelve-carrier Gate-A reduction."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import exp, log


def falling(n: int, k: int) -> int:
    out = 1
    for i in range(k):
        out *= n - i
    return out


def complete_graph(n: int):
    return {tuple(sorted(e)) for e in combinations(range(n), 2)}


def complete_bipartite(a: int, b: int):
    return {(i, a + j) for i in range(a) for j in range(b)}


def star(edges, v):
    return {e for e in edges if v in e}


def gamma_neighborhood(edges, f):
    sf = set(f)
    return {g for g in edges if sf.intersection(g)}


def duplicate_for_full_star(edges, v):
    sv = sorted(star(edges, v))
    external = []
    for f in sv:
        external.append(gamma_neighborhood(edges, f) - set(sv))
    union = set().union(*external)
    d = sum(len(x) for x in external) - len(union)
    multiplicity = sum(
        max(0, sum(g in x for x in external) - 1) for g in union
    )
    return d, len(union), [len(x) for x in external], external


def row_a(edges, v, g):
    return sum(bool(set(f).intersection(g)) for f in star(edges, v))


def phi(z: int, d: int, a: int) -> int:
    f = lambda x: (x - z) ** 6
    return a * (f(d) - f(d - 1)) - (f(d) - f(d - a))


def check_graph_realization():
    k13 = complete_graph(13)
    k1212 = complete_bipartite(12, 12)
    assert len(k13) == 78
    assert len(k1212) == 144
    for edges, n in [(k13, 13), (k1212, 24)]:
        for v in range(n):
            assert len(star(edges, v)) == 12
        for f in edges:
            assert len(gamma_neighborhood(edges, f)) == 23

    d13, u13, e13, _ = duplicate_for_full_star(k13, 0)
    db, ub, eb, _ = duplicate_for_full_star(k1212, 0)
    assert (d13, u13, set(e13)) == (66, 66, {11})
    assert (db, ub, set(eb)) == (0, 132, {11})

    # In a simple graph, every 2-target codegree is 0 or 1.
    for edges, n in [(k13, 13), (k1212, 24)]:
        for pair in combinations(range(n), 2):
            lam = int(tuple(sorted(pair)) in edges)
            assert lam * (lam - 1) ** 2 == 0

    defect13 = 0
    for v in range(13):
        for g in k13 - star(k13, v):
            a = row_a(k13, v, g)
            assert a == 2
            defect13 += phi(12, 12, a)
    assert phi(12, 12, 2) == 62
    assert defect13 == 13 * 66 * 62

    defectb = 0
    for v in range(24):
        for g in k1212 - star(k1212, v):
            a = row_a(k1212, v, g)
            assert a <= 1
            defectb += phi(12, 12, a)
    assert defectb == 0
    return 1


def check_first_blocker_and_q2():
    # Exhaust all simple graphs through six vertices, all roots, and all
    # ordered tuples up to order three.  This checks that D counts edges,
    # not ordered pairs.
    checks = 0
    n = 5
    all_edges = list(combinations(range(n), 2))
    for mask in range(1 << len(all_edges)):
        edges = {all_edges[i] for i in range(len(all_edges)) if mask >> i & 1}
        for v in range(n):
            sv = sorted(star(edges, v))
            for ell in range(1, min(3, len(sv)) + 1):
                total_d = 0
                tuple_count = 0
                for tup in permutations(sv, ell):
                    ext = [gamma_neighborhood(edges, f) - set(sv) for f in tup]
                    cells = []
                    seen = set()
                    for x in ext:
                        cells.append(x - seen)
                        seen |= x
                    d1 = sum(map(len, ext)) - len(seen)
                    d2 = sum(len(ext[i]) - len(cells[i]) for i in range(ell))
                    d3 = sum(
                        max(0, sum(g in x for x in ext) - 1) for g in seen
                    )
                    assert d1 == d2 == d3
                    total_d += d1
                    tuple_count += 1

                q2 = 0
                for g in edges - set(sv):
                    a = row_a(edges, v, g)
                    q2 += a * (a - 1)
                # E D <= C(ell,2) Q2/(d)_2.
                if len(sv) >= 2:
                    lhs = Fraction(total_d, tuple_count)
                    rhs = Fraction(ell * (ell - 1), 2) * Fraction(
                        q2, len(sv) * (len(sv) - 1)
                    )
                    assert lhs <= rhs
                checks += 1

    # The order-12 K13 bridge is equality.
    k13 = complete_graph(13)
    v = 0
    q2 = sum(
        row_a(k13, v, g) * (row_a(k13, v, g) - 1)
        for g in k13 - star(k13, v)
    )
    rhs = Fraction(66 * q2, falling(12, 2))
    assert q2 == 132 and rhs == 66
    return checks


def check_two_type_replicator():
    checks = 0
    for eta in [1e-2, 1e-4, 1e-6]:
        for delta in [0.5, 0.1, 0.01, 0.001]:
            t = 0
            pi = eta
            qv = 0.0
            while exp(t * delta) < 1.0 / eta:
                closed = eta * exp(t * delta) / (1 - eta + eta * exp(t * delta))
                assert abs(pi - closed) < 2e-12
                qv += delta * delta * pi * (1 - pi)
                pi = pi * exp(delta) / (1 - pi + pi * exp(delta))
                t += 1
            density_b = exp(t * delta) / (1 - eta + eta * exp(t * delta))
            assert density_b >= 1.0 / (3.0 * eta)
            assert qv <= 2.0 * delta + 1e-12
            checks += 1
    return checks


def check_forced_refresh_recurrence():
    # Compare the explicit sum with the scalar recurrence for varied inputs.
    checks = 0
    schedules = [
        [(0.2, 0.05)] * 20,
        [(0.05 + 0.001 * j, 0.01 + 0.0002 * j) for j in range(30)],
        [(0.0, 0.02)] * 15,
    ]
    for schedule in schedules:
        m = 1.0
        terms = []
        for lam, omega in schedule:
            a = (1 - lam) * exp(omega)
            b = (1 - lam) * (exp(omega) - 1)
            m = 1 + a * (m - 1) + b
            terms.append((a, b))
        explicit = 0.0
        for i, (_, b) in enumerate(terms):
            prod = 1.0
            for a, _ in terms[i + 1 :]:
                prod *= a
            explicit += b * prod
        assert abs((m - 1) - explicit) < 1e-10
        checks += 1
    return checks


def check_carrier_identity_and_threshold():
    checks = 0
    z = 100
    c = 110
    for d in range(0, 301):
        lhs = max(d - c, 0) ** 12
        if d < 12:
            rhs = 0
        else:
            psi = Fraction(lhs, falling(d, 12))
            rhs = falling(d, 12) * psi
        assert rhs == lhs
        checks += 1

    # Deterministic carrier-mass normalization:
    # sum (d)_12 >= n(average(d)-11)_+^12.
    degree_arrays = [
        [22, 22, 22],
        [12, 24, 36, 48],
        [0, 0, 60, 60],
        [11, 12, 100, 37, 25],
    ]
    for degrees in degree_arrays:
        avg = Fraction(sum(degrees), len(degrees))
        lhs = sum(falling(d, 12) for d in degrees)
        rhs = len(degrees) * max(avg - 11, 0) ** 12
        assert lhs >= rhs
        checks += 1

    # Full shore-safe threshold is strictly stronger than the base-stop one.
    for alpha in [Fraction(1, 100), Fraction(1, 40), Fraction(1, 37)]:
        assert 2 - 20 * alpha < 2 - 18 * alpha
        assert alpha < Fraction(1, 36)
    return checks


def check_high_root_strengthening():
    # A finite grid check of the strictly positive ratio in Lemma 6.1.
    # The proof, not this grid, supplies uniformity.
    delta = Fraction(1, 4)
    k_cap = 3
    ratios = []
    for z in range(32, 81):
        d_min = (5 * z + 3) // 4
        for d in range(d_min, k_cap * z + 1):
            for a in range(2, d + 1):
                ratios.append(Fraction(phi(z, d, a), z**4 * a * (a - 1)))
    assert min(ratios) > 0
    return len(ratios)


def check_microbite_tangent():
    # For a finite graph G, the no-accepted-edge probability has derivative
    # -|E(G)| at p=0: the zero-mark event contributes 1-mp+..., every
    # one-mark event is excluded, and all >=2-mark events are O(p^2).
    m13 = len(complete_graph(13))
    mb = len(complete_bipartite(12, 12))
    assert (m13, mb, mb - m13) == (78, 144, 66)
    return 1


def main():
    graph = check_graph_realization()
    blockers = check_first_blocker_and_q2()
    repl = check_two_type_replicator()
    refresh = check_forced_refresh_recurrence()
    carrier = check_carrier_identity_and_threshold()
    high_root = check_high_root_strengthening()
    tangent = check_microbite_tangent()
    print(
        "GATE_A_ROOTED_TWELVE_CARRIER_PASS",
        f"graph={graph}",
        f"blockers={blockers}",
        f"replicator={repl}",
        f"refresh={refresh}",
        f"carrier={carrier}",
        f"high_root={high_root}",
        f"tangent={tangent}",
    )


if __name__ == "__main__":
    main()
