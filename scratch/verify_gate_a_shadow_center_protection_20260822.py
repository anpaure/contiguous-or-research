#!/usr/bin/env python3
"""Finite algebra checks for the Gate-A shadow-center/protection note."""

from fractions import Fraction
from itertools import combinations
from math import log


def p4(t):
    return 15 * t**4 - 20 * t**3 + 15 * t**2 - 6 * t + 1


def nabla6(t):
    return t**6 - (t - 1) ** 6


def positive(x):
    return x if x > 0 else Fraction(0)


def build_graph(d):
    # K_{d,d} on 0,...,2d-1 and a disjoint K_{1,d}.
    edges = []
    for i in range(d):
        for j in range(d):
            edges.append(frozenset((i, d + j)))
    center = 2 * d
    for j in range(d):
        edges.append(frozenset((center, center + 1 + j)))
    return edges, 3 * d + 1


def graph_data(d):
    edges, n = build_graph(d)
    z_count = len(edges)
    deg = [0] * n
    for e in edges:
        for v in e:
            deg[v] += 1
    conflicts = []
    for e in edges:
        conflicts.append(sum(bool(e & f) for f in edges))
    cbar = Fraction(sum(conflicts), z_count)
    z = Fraction(2 * z_count, n)
    b = cbar - z
    eprof = []
    for v in range(n):
        if deg[v] == 0:
            eprof.append(Fraction(0))
        else:
            eprof.append(
                Fraction(sum(conflicts[i] for i, e in enumerate(edges) if v in e), deg[v])
                - deg[v]
            )
    return edges, n, deg, conflicts, z, cbar, b, eprof


def check_rows_and_drift(d):
    edges, n, deg, conflicts, z, cbar, b, eprof = graph_data(d)
    # Triangle-free external rows have size at most one.
    max_a = 0
    for v in range(n):
        for g in edges:
            if v in g:
                continue
            a = sum(v in f and bool(f & g) for f in edges)
            max_a = max(max_a, a)
    assert max_a <= 1

    # Direct and decomposed tangent calculations for the one-sided sixth mass.
    s = Fraction(0)
    t5 = Fraction(0)
    fixed_loss = Fraction(0)
    d_term = Fraction(0)  # row defect, identically zero here
    rhs_decomp = Fraction(0)
    weights = []
    for v in range(n):
        t = Fraction(deg[v]) - z
        fp = positive(t) ** 6
        grad = fp - positive(t - 1) ** 6
        weights.append(grad)
        s += fp
        t5 += positive(t) ** 5
        fixed_loss += deg[v] * fp + deg[v] * eprof[v] * grad
        xi = eprof[v] - b
        p4plus = 6 * positive(t) ** 5 - grad
        rhs_decomp += -positive(t) ** 7 + b * deg[v] * p4plus - deg[v] * xi * grad
    s_prime = -fixed_loss + 6 * z * b * t5 + d_term
    direct_norm_num = s_prime + (z + 6 * b) * s
    assert direct_norm_num == rhs_decomp

    # Exact covariance compression (4.10).
    w_edge = [sum(weights[v] for v in e) for e in edges]
    mean_w = Fraction(sum(w_edge), len(edges))
    cov = Fraction(sum(conflicts[i] * w_edge[i] for i in range(len(edges))), len(edges)) - cbar * mean_w
    lhs = -sum(deg[v] * (eprof[v] - b) * weights[v] for v in range(n))
    rhs = sum(deg[v] * (Fraction(deg[v]) - z) * weights[v] for v in range(n)) - len(edges) * cov
    assert lhs == rhs
    psi = s / (n * z**6)
    psi_prime = direct_norm_num / (n * z**6)
    return z, cbar, psi, psi_prime


def analytic_drift(d):
    """Same drift from the three vertex orbits, without constructing Kdd."""
    n = 3 * d + 1
    z = Fraction(2 * d * (d + 1), n)
    cbar = Fraction(2 * d * d, d + 1)
    b = cbar - z
    # (multiplicity, degree, E_v): Kdd vertices, star centre, star leaves.
    groups = ((2 * d, d, d - 1), (1, d, 0), (d, 1, d - 1))
    s = Fraction(0)
    rhs = Fraction(0)
    for count, degree, exposure in groups:
        t = Fraction(degree) - z
        fp = positive(t) ** 6
        grad = fp - positive(t - 1) ** 6
        xi = Fraction(exposure) - b
        p4plus = 6 * positive(t) ** 5 - grad
        s += count * fp
        rhs += count * (
            -positive(t) ** 7 + b * degree * p4plus - degree * xi * grad
        )
    return z, cbar, s / (n * z**6), rhs / (n * z**6)


def row_phi(degree, a, center, one_sided):
    def f(x):
        t = Fraction(x) - center
        return positive(t) ** 6 if one_sided else t**6

    return a * (f(degree) - f(degree - 1)) - (f(degree) - f(degree - a))


def check_general_graph(edges, n, one_sided):
    z_count = len(edges)
    deg = [sum(v in e for e in edges) for v in range(n)]
    conflicts = [sum(bool(e & f) for f in edges) for e in edges]
    z = Fraction(2 * z_count, n)
    cbar = Fraction(sum(conflicts), z_count)
    b = cbar - z
    exposure = []
    for v in range(n):
        if not deg[v]:
            exposure.append(Fraction(0))
        else:
            exposure.append(
                Fraction(sum(conflicts[i] for i, e in enumerate(edges) if v in e), deg[v])
                - deg[v]
            )

    defect = Fraction(0)
    for v in range(n):
        for g in edges:
            if v in g:
                continue
            a = sum(v in f and bool(f & g) for f in edges)
            defect += row_phi(deg[v], a, z, one_sided)

    s = Fraction(0)
    t5 = Fraction(0)
    fixed_loss = Fraction(0)
    rhs = defect
    for v in range(n):
        t = Fraction(deg[v]) - z
        fp = positive(t) ** 6 if one_sided else t**6
        fm = positive(t - 1) ** 6 if one_sided else (t - 1) ** 6
        grad = fp - fm
        fifth = positive(t) ** 5 if one_sided else t**5
        seventh = positive(t) ** 7 if one_sided else t**7
        p4value = 6 * fifth - grad
        xi = exposure[v] - b
        s += fp
        t5 += fifth
        fixed_loss += deg[v] * fp + deg[v] * exposure[v] * grad
        rhs += -seventh + b * deg[v] * p4value - deg[v] * xi * grad
    direct = -fixed_loss + defect + 6 * z * b * t5 + (z + 6 * b) * s
    assert direct == rhs

    # Cross-center one-sided collision domination for several rational lifts.
    for delta in (Fraction(0), Fraction(1, 5), Fraction(3, 2)):
        lifted = z + delta
        dplus = Fraction(0)
        dsym = Fraction(0)
        for v in range(n):
            for g in edges:
                if v in g:
                    continue
                a = sum(v in f and bool(f & g) for f in edges)
                dplus += row_phi(deg[v], a, lifted, True)
                dsym += row_phi(deg[v], a, z, False)
        assert 0 <= dplus <= dsym


def check_polynomial():
    for q in range(-40, 81):
        t = Fraction(q, 7)
        assert 6 * t**5 - nabla6(t) == p4(t)
        assert p4(t) >= 0


def check_shadow_ledger():
    # The exact logarithmic lower bound in (5.3).
    for k0 in (Fraction(6, 5), Fraction(3, 2), Fraction(2), Fraction(4)):
        for irho in range(1, 90):
            rho = Fraction(irho, 100)
            if rho >= 1:
                continue
            for itau in range(0, irho + 1):
                tau = Fraction(itau, 100)
                if tau > rho / k0:
                    continue
                lhs = log(float((1 - tau) / (1 - rho)))
                rhs = float((1 - 1 / k0) * rho)
                assert lhs + 1e-14 >= rhs


def check_tail_charge():
    # Scalar inequality underlying (5.6), over a finite rational grid.
    a = Fraction(6, 5)
    rstar = Fraction(11, 10)
    k0 = Fraction(3, 2)
    assert a * rstar < k0
    c1 = (k0 - a * rstar) / rstar
    for iz in range(1, 30):
        z = Fraction(iz, 3)
        for iw in range(1, 80):
            w = Fraction(iw, 7)
            if w / z > rstar:
                continue
            for ideg in range(1, 100):
                degree = Fraction(ideg, 2)
                if degree <= k0 * z:
                    continue
                assert degree - a * w >= c1 * w


def main():
    check_polynomial()
    check_shadow_ledger()
    check_tail_charge()
    complete_edges = [frozenset(e) for e in combinations(range(4), 2)]
    for mask in range(1, 1 << len(complete_edges)):
        graph = [e for i, e in enumerate(complete_edges) if mask & (1 << i)]
        check_general_graph(graph, 4, False)
        check_general_graph(graph, 4, True)
    for d in range(2, 9):
        z, cbar, psi, psi_prime = check_rows_and_drift(d)
        assert psi_prime > 0
        assert z == Fraction(2 * d * (d + 1), 3 * d + 1)
        assert cbar == Fraction(2 * d * d, d + 1)
        assert (z, cbar, psi, psi_prime) == analytic_drift(d)
    z, cbar, psi, psi_prime = analytic_drift(10_000)
    assert abs(float(psi) - 1 / 96) < 2e-4
    assert abs(float(psi_prime / 10_000) - 17 / 288) < 2e-4
    print("PASS polynomial identity/nonnegativity")
    print("PASS exact shadow ledger grid")
    print("PASS fixed-shadow bad-tail grid")
    print("PASS exact tangent and cross-center domination on all 4-vertex graphs")
    print("PASS Kdd union star: row cap a<=1 and exact tangent identity")
    print("PASS asymptotics Psi->1/96 and Psi'/d->17/288")


if __name__ == "__main__":
    main()
