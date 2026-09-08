#!/usr/bin/env python3
"""Exact small-hypergraph audit for the finite-bite carrier theorem.

The script enumerates every mark set, constructs the isolated accepted set,
forms the induced residual, and checks:
  * the carrier survival remainder in Lemma 2.1;
  * the exact scalar Palm recursion;
  * the finite-bite inequality with a deliberately generous universal
    constant, on several rational marking probabilities.

This is an audit of formulas, not an asymptotic proof.
"""

from fractions import Fraction
from itertools import combinations, permutations


def falling(x, m):
    ans = 1
    for j in range(m):
        ans *= x - j
    return ans


def phi(d, c, m):
    if d < m or d <= c:
        return Fraction(0)
    return Fraction((d - c) ** m, falling(d, m))


def accepted(edges, mask):
    marked = [i for i in range(len(edges)) if (mask >> i) & 1]
    out = []
    for i in marked:
        if all(not (edges[i] & edges[j]) for j in marked if j != i):
            out.append(i)
    return out


def residual_degrees(edges, roots, mask):
    acc = accepted(edges, mask)
    deleted = set().union(*(edges[i] for i in acc)) if acc else set()
    alive_edges = [e for e in edges if not (e & deleted)]
    return {v: (0 if v in deleted else sum(v in e for e in alive_edges))
            for v in roots}


def prob_mask(p, z, mask):
    q = 1 - p
    a = mask.bit_count()
    return p ** a * q ** (z - a)


def audit(edges_raw, roots, m, c, ps):
    edges = [frozenset(e) for e in edges_raw]
    zed = len(edges)
    stars = {v: [i for i, e in enumerate(edges) if v in e] for v in roots}
    carriers = []
    for v in roots:
        carriers.extend((v, tup) for tup in permutations(stars[v], m))
    assert carriers

    conflict = [{j for j, g in enumerate(edges) if e & g} for e in edges]
    Delta = max(map(len, conflict))
    h = {}
    for gam in carriers:
        _, tup = gam
        h[gam] = len(set().union(*(conflict[i] for i in tup)))

    weights = {gam: phi(len(stars[gam[0]]), c, m) for gam in carriers}
    A = sum(weights.values(), Fraction(0)) / len(carriers)
    assert A > 0

    # Degree-conditioned carrier-union regression, Lemma 3.4.
    degree_groups = {}
    for gam in carriers:
        degree_groups.setdefault(len(stars[gam[0]]), []).append(gam)
    zeta = {
        d: Fraction(sum(h[g] for g in gs), len(gs))
        for d, gs in degree_groups.items()
    }
    # Avoidance identity (3.21b), checked root by root.
    for v in roots:
        d = len(stars[v])
        if d < m:
            continue
        avoid = Fraction(0)
        star_set = set(stars[v])
        for gi, edge in enumerate(edges):
            if v in edge:
                continue
            aa = sum(gi in conflict[fi] for fi in stars[v])
            avoid += Fraction(falling(d - aa, m), falling(d, m))
        root_carriers = [g for g in carriers if g[0] == v]
        avg_h = Fraction(sum(h[g] for g in root_carriers), len(root_carriers))
        assert avg_h == len(edges) - avoid
    degree_prob = {
        d: Fraction(len(gs), len(carriers)) for d, gs in degree_groups.items()
    }
    inversion_sup = Fraction(0)
    inversion_weighted = Fraction(0)
    for d in degree_groups:
        for e in degree_groups:
            if d >= e or phi(d, c, m) >= phi(e, c, m):
                continue
            drop = max(zeta[d] - zeta[e], 0)
            inversion_sup = max(inversion_sup, drop)
            inversion_weighted += (
                degree_prob[d] * degree_prob[e] * drop
                * (phi(e, c, m) - phi(d, c, m)) / A
            )
    mean_h = sum(h.values(), Fraction(0)) / len(carriers)
    mean_hphi = sum(Fraction(h[g]) * weights[g] for g in carriers) / len(carriers)
    cov_h_phi = mean_hphi - mean_h * A
    assert -cov_h_phi / A <= inversion_weighted <= inversion_sup

    for p in ps:
        survive_prob = {gam: Fraction(0) for gam in carriers}
        payoff_prob = {gam: Fraction(0) for gam in carriers}
        num = Fraction(0)
        den = Fraction(0)
        for mask in range(1 << zed):
            pr = prob_mask(p, zed, mask)
            deg = residual_degrees(edges, roots, mask)
            num += pr * sum(max(deg[v] - c, 0) ** m for v in roots)
            den += pr * sum(falling(deg[v], m) if deg[v] >= m else 0
                            for v in roots)
            alive_indices = {i for i, e in enumerate(edges)
                             if all(u not in (set().union(*(
                                 [edges[j] for j in accepted(edges, mask)]
                             )) if accepted(edges, mask) else set()) for u in e)}
            for gam in carriers:
                if set(gam[1]) <= alive_indices:
                    survive_prob[gam] += pr
                    payoff_prob[gam] += pr * phi(deg[gam[0]], c, m)

        Anew = num / den
        K = Fraction(m * m, 2) + m
        for gam in carriers:
            rem = survive_prob[gam] - (1 - p * h[gam])
            assert rem >= 0
            assert rem <= K * (p * Delta) ** 2

        mean_a = sum(survive_prob.values(), Fraction(0)) / len(carriers)
        mean_aphi = sum(survive_prob[g] * weights[g] for g in carriers) / len(carriers)
        # Erosion is favourable, so this is the exact inequality used in (3.4).
        assert Anew <= mean_aphi / mean_a

        # Exact tail-tilted erosion quotient (3.13d).
        tail_payoff = Fraction(0)
        for gam in carriers:
            if not weights[gam]:
                continue
            tau_mass = weights[gam] / (len(carriers) * A)
            beta = payoff_prob[gam] / weights[gam]
            tail_payoff += tau_mass * beta
        assert Anew / A == tail_payoff / mean_a

        # Rational version of Anew/A - 1 <= tangent + C theta^2.
        # C=1000 is intentionally loose and is used only as a formula audit.
        assert Anew / A - 1 <= -p * cov_h_phi / A + 1000 * (p * Delta) ** 2
        assert Anew / A - 1 <= p * inversion_sup + 1000 * (p * Delta) ** 2

    return len(carriers), Delta


def audit_slice_remainder():
    """Check Lemma 2.2 exactly on a small two-shore footprint table."""
    shores = [(100, 99), (90, 89)]
    footprints = [(3, 4), (5, 2), (6, 5), (2, 7)]
    deltas = [Fraction(n - np, n) for n, np in shores]
    eta = max(sum(d * b for d, b in zip(deltas, bs)) for bs in footprints)
    rho = max(sum(d * b * b / n for d, b, (n, _) in zip(deltas, bs, shores))
              for bs in footprints)
    assert eta < Fraction(1, 2)
    for bs in footprints:
        exact = Fraction(1)
        for b, (n, np) in zip(bs, shores):
            exact *= Fraction(falling(np, b), falling(n, b))
        g = sum(d * b for d, b in zip(deltas, bs))
        # A loose absolute constant is sufficient for this formula audit.
        assert abs(exact - (1 - g)) <= 10 * (eta * eta + rho)
    return len(footprints)


def audit_incidence_jensen(edges_raw, roots, m, c):
    """Exact check of Lemma 5.1 with the sharp statewise K and a0."""
    edges = [frozenset(e) for e in edges_raw]
    # All supplied examples use one root shore and constant edge rank k.
    ks = {len(e & set(roots)) for e in edges}
    assert len(ks) == 1
    k = ks.pop()
    n = len(roots)
    z = Fraction(k * len(edges), n)
    deg = {v: sum(v in e for e in edges) for v in roots}
    conflict_size = {
        i: sum(bool(e & g) for g in edges) for i, e in enumerate(edges)
    }
    avec = {}
    exposure = {}
    for v in roots:
        star = [i for i, e in enumerate(edges) if v in e]
        if not star:
            avec[v] = Fraction(0)
            exposure[v] = Fraction(0)
        else:
            avec[v] = Fraction(sum(conflict_size[i] for i in star), len(star))
            exposure[v] = avec[v] - deg[v]
    cbar = Fraction(sum(conflict_size.values()), len(edges))
    var_c = sum((conflict_size[i] - cbar) ** 2 for i in range(len(edges))) / len(edges)
    u2 = sum((deg[v] - z) ** 2 for v in roots) / (n * z * z)
    total = sum(falling(deg[v], m) for v in roots)
    assert total > 0
    mean_e = sum(Fraction(falling(deg[v], m), total) * exposure[v] for v in roots)
    var_e = sum(Fraction(falling(deg[v], m), total) * (exposure[v] - mean_e) ** 2
                for v in roots)
    K = max(Fraction(deg[v], z) for v in roots)
    a0 = Fraction(total, 1) / (n * z ** m)
    rhs = Fraction(2) * K ** (m - 1) / a0 * z * z * (
        var_c / (z * z) + K * u2
    )
    assert var_e <= rhs

    # Tail-local self-normalization, Lemma 5.2.
    f = {v: max(deg[v] - c, 0) ** m for v in roots}
    ftotal = sum(f.values())
    assert ftotal > 0
    vtail_num = Fraction(0)
    for v in roots:
        if not f[v]:
            continue
        star = [i for i, e in enumerate(edges) if v in e]
        vtail_num += Fraction(f[v], deg[v]) * sum(
            (conflict_size[i] - cbar) ** 2 for i in star
        )
    vtail = vtail_num / (z * z * ftotal)
    utail = sum(f[v] * (deg[v] - z) ** 2 for v in roots) / (
        z * z * ftotal
    )
    xstat = sum(Fraction(f[v], ftotal) * max(mean_e - exposure[v], 0)
                for v in roots)
    brace = vtail + utail + K ** (m - 1) / a0 * (
        var_c / (z * z) + K * u2
    )
    assert xstat * xstat <= 4 * z * z * brace

    # Exact regression core of Lemma 5.3, before the deterministic tail cap.
    xi = {v: exposure[v] - (cbar - z) for v in roots}
    mean_xi_rho = sum(Fraction(deg[v], n * z) * xi[v] for v in roots)
    assert mean_xi_rho == -z * u2
    grad = {
        v: max(deg[v] - c, 0) ** m - max(deg[v] - c - 1, 0) ** m
        for v in roots
    }
    by_degree = {}
    for v in roots:
        by_degree.setdefault(deg[v], []).append(v)
    # Conditional rho and uniform-root means coincide within a degree class.
    chi = {d: sum(xi[v] for v in vs) / len(vs) for d, vs in by_degree.items()}
    inv = Fraction(0)
    for d in by_degree:
        for e in by_degree:
            wd = max(d - c, 0) ** m - max(d - c - 1, 0) ** m
            we = max(e - c, 0) ** m - max(e - c - 1, 0) ** m
            if d < e and wd < we:
                inv = max(inv, chi[d] - chi[e], Fraction(0))
    ew = sum(Fraction(deg[v], n * z) * grad[v] for v in roots)
    protection = -sum(deg[v] * xi[v] * grad[v] for v in roots)
    assert max(protection, 0) <= n * z * (inv + z * u2) * ew
    return (n, len(edges))


def main():
    cases = [
        # K5, m=2, with a nonintegral threshold.
        ([{i, j} for i, j in combinations(range(5), 2)], list(range(5)), 2, Fraction(3, 2)),
        # A deliberately inhomogeneous graph.
        ([{0, 1}, {0, 2}, {0, 3}, {1, 2}, {2, 3}, {2, 4}, {3, 4}], list(range(5)), 2, Fraction(1)),
        # Small 3-uniform example.
        ([{0, 1, 2}, {0, 1, 3}, {0, 2, 4}, {1, 3, 4}, {2, 3, 4}], list(range(5)), 2, Fraction(1)),
    ]
    ps = [Fraction(1, 200), Fraction(1, 100), Fraction(1, 50)]
    reports = [audit(*case, ps) for case in cases]
    slice_cases = audit_slice_remainder()
    jensen_cases = [audit_incidence_jensen(case[0], case[1], case[2], case[3])
                    for case in cases]
    print("GATE_A_FINITE_BITE_CARRIER_REMAINDER_PASS", reports,
          {"slice_cases": slice_cases, "jensen_cases": jensen_cases})


if __name__ == "__main__":
    main()
