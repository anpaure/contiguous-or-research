#!/usr/bin/env python3
"""Regression checks for the Gate-A conflict-variance reduction.

The exhaustive objects are simple 4-uniform, two-shore hypergraphs with
two vertices from each shore.  For the high/low split we declare same-shore
pairs high, so every edge has h=2 high and ell=4 low pairs.  The proof only
uses the constant per-edge counts, not the punctured meaning of the split.
"""

from fractions import Fraction
from itertools import combinations
from math import exp


def falling2(a):
    return a * (a - 1)


def phi(z, d, a):
    f = lambda x: (Fraction(x) - z) ** 6
    return a * (f(d) - f(d - 1)) - (f(d) - f(d - a))


def variance(values):
    mean = sum(values, Fraction(0)) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def check_hypergraph(edges, shores):
    vertices = tuple(sorted(shores))
    zcount = len(edges)
    q = len(edges[0])
    shore_names = sorted(set(shores.values()))
    k = {s: sum(shores[v] == s for v in edges[0]) for s in shore_names}
    assert all(sum(shores[v] == s for v in e) == k[s]
               for e in edges for s in shore_names)

    deg = {v: sum(v in e for e in edges) for v in vertices}
    n = {s: sum(shores[v] == s for v in vertices) for s in shore_names}
    z = {s: Fraction(k[s] * zcount, n[s]) for s in shore_names}
    zstar = z[shore_names[0]]

    edge_sets = [set(e) for e in edges]
    C, A, dup, Rext, S = [], [], [], [], []
    row_a = {}
    for i, F in enumerate(edge_sets):
        overlaps = [len(F & G) for G in edge_sets]
        C_i = sum(t > 0 for t in overlaps)
        A_i = sum(deg[v] for v in F)
        dup_i = sum(t - 1 for t in overlaps if t > 0)
        R_i = 0
        for v in vertices:
            if v not in F:
                a = sum(v in G and bool(F & G) for G in edge_sets)
                row_a[(i, v)] = a
                R_i += a
        S_i = sum(
            sum(P <= G for G in edge_sets) - 1
            for P in map(set, combinations(F, 2))
        )
        assert C_i == A_i - dup_i
        assert q * C_i == A_i + R_i
        assert S_i == sum(t * (t - 1) // 2 for j, t in enumerate(overlaps)
                          if j != i)
        assert dup_i - (q - 1) == sum(max(0, t - 1)
                                      for j, t in enumerate(overlaps)
                                      if j != i)
        assert 0 <= dup_i - (q - 1) <= S_i
        C.append(Fraction(C_i))
        A.append(Fraction(A_i))
        dup.append(Fraction(dup_i))
        Rext.append(Fraction(R_i))
        S.append(Fraction(S_i))

    pair_degree = {}
    for P in combinations(vertices, 2):
        pair_degree[P] = sum(set(P) <= F for F in edge_sets)

    # The test split: same-shore pairs are high.  With k_M=k_L=2,
    # every edge has h=2 and ell=4.
    high = {P for P in pair_degree if shores[P[0]] == shores[P[1]]}
    h = 2
    m = q * (q - 1) // 2
    ell = m - h
    assert all(sum(tuple(sorted(P)) in high for P in combinations(F, 2)) == h
               for F in edges)

    TH = sum(lam * (lam - 1) ** 2 for P, lam in pair_degree.items()
             if P in high)
    TL = sum(lam * (lam - 1) ** 2 for P, lam in pair_degree.items()
             if P not in high)
    theta_h = Fraction(TH, 1) / (zcount * zstar ** 2)
    theta_l = Fraction(TL, 1) / (zcount * zstar ** 2)
    assert variance(dup) / zstar ** 2 <= 2 * (h * theta_h + ell * theta_l)

    # Exact companion expansion and cap bound.
    b = {v: Fraction(deg[v]) - z[shores[v]] for v in vertices}
    a0 = sum(k[s] * z[s] for s in shore_names)
    omega = sum((A_i - a0) ** 2 for A_i in A) / (zcount * zstar ** 2)
    expansion = sum(deg[v] * b[v] ** 2 for v in vertices)
    expansion += 2 * sum(pair_degree[P] * b[P[0]] * b[P[1]]
                         for P in pair_degree)
    assert expansion == zcount * zstar ** 2 * omega

    K = max(Fraction(deg[v], 1) / z[shores[v]] for v in vertices)
    U2 = {}
    U6 = {}
    for s in shore_names:
        vs = [v for v in vertices if shores[v] == s]
        U2[s] = sum((Fraction(deg[v]) - z[s]) ** 2 for v in vs) / (n[s] * z[s] ** 2)
        U6[s] = sum((Fraction(deg[v]) - z[s]) ** 6 for v in vs) / (n[s] * z[s] ** 6)
        assert U2[s] ** 3 <= U6[s]
    cap_rhs = K * q * sum(k[s] * (z[s] / zstar) ** 2 * U2[s]
                          for s in shore_names)
    assert omega <= cap_rhs

    # Squared form of Theorem 5.1, entirely rational.
    vc = variance(C) / zstar ** 2
    bound = 2 * cap_rhs + 4 * (h * theta_h + ell * theta_l)
    assert vc <= bound

    # Centered row defect lower bounds and pair bridge.
    Dtot = Fraction(0)
    Q2tot = 0
    for s in shore_names:
        Ds = Fraction(0)
        Qs = 0
        for i, F in enumerate(edge_sets):
            for v in vertices:
                if shores[v] == s and v not in F:
                    a = row_a[(i, v)]
                    ph = phi(z[s], deg[v], a)
                    assert ph >= falling2(a)
                    stronger = Fraction(falling2(a)) * (
                        1 + Fraction(5, 108) * (a - 2) ** 2 * (a + 1) ** 2
                    )
                    assert ph >= stronger
                    Ds += ph
                    Qs += falling2(a)
        assert Ds >= Qs
        Dtot += Ds
        Q2tot += Qs

    bridge = Fraction(0)
    for u in vertices:
        for v in vertices:
            if u == v:
                continue
            lam = pair_degree[tuple(sorted((u, v)))]
            g = Fraction(falling2(lam)) * (
                1 + Fraction(5, 108) * (lam - 2) ** 2 * (lam + 1) ** 2
            )
            bridge += (deg[u] - lam) * g
    assert bridge <= q * Dtot


def exponent_audit():
    terms = [(3, 9), (4, 21), (4, 18), (5, 45)]
    direct = [Fraction(a - 1, b) for a, b in terms]
    fine_sqrt = [Fraction(a - 2, b + 4) for a, b in terms]
    coarse_o1 = [Fraction(2 * a - 3, 2 * b) for a, b in terms]
    coarse_o1r = [Fraction(a - 3, b) for a, b in terms]
    assert min(direct) == Fraction(4, 45)
    assert min(fine_sqrt) == Fraction(3, 49)
    assert min(coarse_o1) == Fraction(7, 90)
    assert min(coarse_o1r) == 0
    assert Fraction(1, 32) < min(direct + fine_sqrt)
    return min(direct), min(fine_sqrt), min(coarse_o1), min(coarse_o1r)


def microstep_weight_audit():
    # The number of steps grows like epsilon^{-1}, but every protection
    # increment carries epsilon.  Numerically check the density-integral
    # comparison for several very different microstep sizes.
    r = 200
    alpha = 0.04
    target = r ** (-alpha)
    ratios = []
    for epsilon in (1.0, 0.2, 0.04, 0.008):
        x = 1.0
        weighted = 0.0
        steps = 0
        b = 13
        while x > target:
            weighted += (epsilon / r) * x ** (-b)
            x *= exp(-epsilon / r)
            steps += 1
            assert steps < 1_000_000
        integral = (x ** (-b) - 1.0) / b
        ratio = weighted / integral
        assert 0.95 <= ratio <= 1.05
        ratios.append(ratio)
        # Removing epsilon would enlarge the same sum by exactly 1/epsilon.
        unweighted = weighted / epsilon
        assert abs(unweighted / weighted - 1.0 / epsilon) < 1e-10
    assert max(ratios) - min(ratios) < 0.04
    return len(ratios)


def two_edge_defect_separation():
    # Two distinct 4-edges with a 3-target intersection.  Every external
    # row has occupancy at most one, but every pair in the intersection
    # has current codegree two.
    edges = [set((0, 1, 2, 3)), set((0, 1, 2, 4))]
    vertices = set().union(*edges)
    D = Fraction(0)
    for G in edges:
        for v in vertices - G:
            a = sum(v in F and bool(F & G) for F in edges)
            assert a <= 1
            D += phi(Fraction(7, 5), sum(v in F for F in edges), a)
    pair_degree = {
        P: sum(set(P) <= F for F in edges)
        for P in combinations(sorted(vertices), 2)
    }
    pair_square = sum(lam * (lam - 1) ** 2 for lam in pair_degree.values())
    assert D == 0
    assert pair_square == 2 * 3


def main():
    # Three vertices per shore, every possible 2+2 edge: 9 candidates,
    # hence 511 nonempty simple residuals.
    M = (0, 1, 2)
    L = (3, 4, 5)
    shores = {v: ("M" if v in M else "L") for v in M + L}
    candidates = [tuple(sorted(a + b))
                  for a in combinations(M, 2) for b in combinations(L, 2)]
    checked = 0
    for mask in range(1, 1 << len(candidates)):
        edges = [candidates[i] for i in range(len(candidates)) if mask >> i & 1]
        check_hypergraph(edges, shores)
        checked += 1
    two_edge_defect_separation()
    thresholds = exponent_audit()
    microsteps = microstep_weight_audit()
    print(
        "GATE_A_CONFLICT_VARIANCE_REDUCTION_PASS",
        f"hypergraphs={checked}",
        f"fine={thresholds[1]}",
        f"coarse_o1={thresholds[2]}",
        f"coarse_o1r={thresholds[3]}",
        f"microsteps={microsteps}",
    )


if __name__ == "__main__":
    main()
