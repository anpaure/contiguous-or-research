#!/usr/bin/env python3
"""Finite exact checks for the post-purge centered-defect theorem."""

from fractions import Fraction as F
from itertools import combinations
import random


def falling2(a):
    return a * (a - 1)


def p_direct(t):
    return t**6 - 2 * (t - 1) ** 6 + (t - 2) ** 6


def p_expanded(t):
    return 30 * t**4 - 120 * t**3 + 210 * t**2 - 180 * t + 62


def phi(z, d, a):
    return sum((a - 1 - h) * p_direct(F(d - h) - z)
               for h in range(max(0, a - 1)))


def degrees(vertices, edges):
    return {v: sum(v in e for e in edges) for v in vertices}


def row_a(v, g, edges):
    return sum(v in f and bool(set(f) & set(g)) for f in edges)


def rooted_q2(v, edges):
    return sum(falling2(row_a(v, g, edges))
               for g in edges if v not in g)


def defect(vertices, edges, z):
    deg = degrees(vertices, edges)
    return sum(phi(z, deg[v], row_a(v, g, edges))
               for v in vertices for g in edges if v not in g)


def induced(edges, keep):
    return tuple(e for e in edges if set(e) <= keep)


def verify_polynomial_and_row_inequality():
    for twice_t in range(-20, 21):
        t = F(twice_t, 2)
        assert p_direct(t) == p_expanded(t)
        assert p_direct(t) >= 0

    # eta=1 specialization:
    # phi_{z'}(d-ell,a') <= 8 phi_z(d,a)+120(a')_2|ell-(z-z')|^4.
    checks = 0
    for d in range(0, 11):
        for ell in range(d + 1):
            dp = d - ell
            for a in range(d + 1):
                for ap in range(min(a, dp) + 1):
                    for twice_z in range(-4, 13, 2):
                        for twice_zp in range(-5, 14, 3):
                            z, zp = F(twice_z, 2), F(twice_zp, 2)
                            lhs = phi(zp, dp, ap)
                            mismatch = F(ell) - (z - zp)
                            rhs = (8 * phi(z, d, a)
                                   + 120 * falling2(ap) * mismatch**4)
                            assert lhs <= rhs, (
                                d, ell, a, ap, z, zp, lhs, rhs
                            )
                            checks += 1
    return checks


def verify_aggregate_deletion_inequality():
    rng = random.Random(20260822)
    checks = 0
    for n, q in ((5, 2), (6, 2), (6, 3), (7, 3)):
        possible = list(combinations(range(n), q))
        for _ in range(250):
            edges = tuple(e for e in possible if rng.random() < 0.42)
            if not edges:
                continue
            keep = {v for v in range(n) if rng.random() < 0.78}
            if len(keep) < q:
                continue
            edges_p = induced(edges, keep)
            vertices = set(range(n))
            deg = degrees(vertices, edges)
            deg_p = degrees(keep, edges_p)
            z = F(q * len(edges), n)
            zp = F(q * len(edges_p), len(keep))

            lhs = defect(keep, edges_p, zp)
            old = defect(vertices, edges, z)
            charge = F(0)
            for v in keep:
                ell = deg[v] - deg_p[v]
                charge += rooted_q2(v, edges_p) * (ell - (z - zp)) ** 4
            assert lhs <= 8 * old + 120 * charge
            checks += 1
    return checks


def verify_local_q2_and_purge_ledgers():
    rng = random.Random(820226)
    checks = 0
    for n, q in ((7, 2), (8, 3), (9, 4)):
        possible = list(combinations(range(n), q))
        for _ in range(300):
            edges = tuple(e for e in possible if rng.random() < 0.31)
            if not edges:
                continue
            vertices = set(range(n))
            deg = degrees(vertices, edges)
            z = F(q * len(edges), n)

            # Choose a threshold from a small exact list and perform the
            # literal all-above-threshold purge.
            k0 = rng.choice((F(11, 10), F(5, 4), F(3, 2), F(2)))
            bad = {v for v in vertices if deg[v] > k0 * z}
            keep = vertices - bad
            if len(keep) < q:
                continue
            edges_p = induced(edges, keep)
            deg_p = degrees(keep, edges_p)

            # The exact local companion-degree majorant (3.3).
            for v in keep:
                companion = sum(
                    sum(deg_p[u] for u in f if u != v)
                    for f in edges_p if v in f
                )
                assert rooted_q2(v, edges_p) <= deg_p[v] * companion

            loss_incidence = sum(deg[v] for v in bad)
            removed_edges = len(edges) - len(edges_p)
            assert removed_edges <= loss_incidence
            assert loss_incidence <= q * removed_edges

            beta = F(loss_incidence, len(edges))
            lost_retained = sum(deg[v] - deg_p[v] for v in keep)
            assert lost_retained <= q * removed_edges
            assert lost_retained <= q * beta * len(edges)

            rho = F(removed_edges, len(edges))
            tau = F(len(bad), n)
            assert tau <= rho / k0

            if bad:
                assert F(len(bad), n) <= beta / (k0 * q)

            zp = F(q * len(edges_p), len(keep)) if keep else F(0)
            assert zp / z == (1 - rho) / (1 - tau)
            assert zp <= z
            assert zp >= (1 - rho) * z
            assert F(len(keep), n) >= 1 - rho / k0
            checks += 1
    return checks


def verify_two_shore_purge_ledgers():
    """Check the sharp shorewise L_sigma <= k_sigma M ledger."""
    rng = random.Random(120260822)
    shores = (tuple(range(5)), tuple(range(5, 10)))
    ks = (2, 2)
    possible = [a + b for a in combinations(shores[0], ks[0])
                for b in combinations(shores[1], ks[1])]
    checks = 0
    for _ in range(350):
        edges = tuple(e for e in possible if rng.random() < 0.19)
        if not edges:
            continue
        vertices = set(shores[0]) | set(shores[1])
        deg = degrees(vertices, edges)
        k0 = rng.choice((F(11, 10), F(5, 4), F(3, 2), F(2)))
        means = [F(k * len(edges), len(shore))
                 for k, shore in zip(ks, shores)]
        bad_by_shore = [
            {v for v in shore if deg[v] > k0 * mean}
            for shore, mean in zip(shores, means)
        ]
        bad = set().union(*bad_by_shore)
        keep = vertices - bad
        edges_p = induced(edges, keep)
        removed_edges = len(edges) - len(edges_p)
        rho = F(removed_edges, len(edges))

        for shore, k, mean, bad_sigma in zip(
                shores, ks, means, bad_by_shore):
            loss_incidence = sum(deg[v] for v in bad_sigma)
            assert loss_incidence <= k * removed_edges
            tau = F(len(bad_sigma), len(shore))
            assert tau <= rho / k0
            shore_keep = set(shore) - bad_sigma
            mean_p = F(k * len(edges_p), len(shore_keep))
            assert mean_p / mean == (1 - rho) / (1 - tau)
            assert mean_p <= mean
            assert mean_p >= (1 - rho) * mean
        checks += 1
    return checks


def verify_counterexamples():
    # Triangle plus an isolated vertex.
    vertices = {0, 1, 2, 3}
    edges = ((0, 1), (0, 2), (1, 2))
    old = defect(vertices, edges, F(3, 2))
    new = defect({0, 1, 2}, edges, F(2))
    assert old == F(273, 8)
    assert new == 186
    assert new > old

    # Fixed-center row failure.
    assert phi(F(3), 3, 2) == 62
    assert phi(F(3), 2, 2) == 602


def main():
    row_checks = verify_polynomial_and_row_inequality()
    aggregate_checks = verify_aggregate_deletion_inequality()
    ledger_checks = verify_local_q2_and_purge_ledgers()
    two_shore_checks = verify_two_shore_purge_ledgers()
    verify_counterexamples()
    print(
        "PASS post-purge centered-defect audit:",
        f"row={row_checks}, aggregate={aggregate_checks}, "
        f"purge-ledger={ledger_checks}, two-shore={two_shore_checks}",
    )


if __name__ == "__main__":
    main()
