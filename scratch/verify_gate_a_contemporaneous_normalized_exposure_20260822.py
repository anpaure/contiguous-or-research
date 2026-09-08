#!/usr/bin/env python3
"""Finite exact checks for the contemporaneous Gate-A reduction."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import random


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def mean(xs):
    return sum(xs, Fraction(0, 1)) / len(xs)


def covariance(xs, ys):
    return mean([x * y for x, y in zip(xs, ys)]) - mean(xs) * mean(ys)


def state_data(n, raw_edges, m):
    edges = tuple(frozenset(e) for e in raw_edges)
    zrows = len(edges)
    q = len(edges[0])
    gamma = [
        {j for j, f in enumerate(edges) if e & f}
        for e in edges
    ]
    c = [len(x) for x in gamma]
    degrees = [sum(v in e for e in edges) for v in range(n)]
    z = Fraction(q * zrows, n)
    a0 = q * z

    pair_degree = {}
    for u, v in combinations(range(n), 2):
        pair_degree[u, v] = sum(u in e and v in e for e in edges)

    excess = []
    for i, e in enumerate(edges):
        excess.append(sum(len(e & edges[j]) - 1 for j in gamma[i]))
        assert c[i] == sum(degrees[v] for v in e) - excess[-1]

    roots = []
    carrier_rows = []
    for v, d in enumerate(degrees):
        if d < m:
            continue
        star = {i for i, e in enumerate(edges) if v in e}
        av = Fraction(sum(c[i] for i in star), d)
        ev = av - d
        rv = Fraction(
            sum(
                sum(degrees[u] - z for u in edges[i] if u != v)
                for i in star
            ),
            d,
        )
        jv = Fraction(sum(excess[i] for i in star), d)
        assert av == a0 + (d - z) + rv - jv
        assert ev == a0 - z + rv - jv

        hs = []
        dups = []
        for rows in permutations(sorted(star), m):
            b = set().union(*(gamma[i] for i in rows))
            ext = [gamma[i] - star for i in rows]
            dup = sum(len(x) for x in ext) - len(set().union(*ext))
            hs.append(len(b))
            dups.append(dup)
            carrier_rows.append((v, rows))
        hbar = mean([Fraction(x, 1) for x in hs])
        dbar = mean([Fraction(x, 1) for x in dups])
        assert hbar == d + m * ev - dbar

        x = Fraction(d, 1) / z
        u = (rv - jv) / z
        qdup = dbar / z
        constant = m * (Fraction(a0, z) - 1)
        assert hbar / z == constant + x + m * u - qdup
        assert hbar / z == m * (av / z) - (m - 1) * x - qdup

        # The rootwise first duplicate inequality (4.6).
        asum2 = 0
        for g, eg in enumerate(edges):
            if v in eg:
                continue
            ag = sum(v in edges[f] and bool(edges[f] & eg) for f in range(zrows))
            asum2 += ag * (ag - 1)
        assert dbar <= Fraction(comb(m, 2) * asum2, d * (d - 1))

        # An arbitrary intrinsic two-type partition for Theorem 4.1.
        rho = [0, 0]
        for f in edges:
            if v not in f:
                continue
            counts = [0, 0]
            for u0 in f:
                if u0 == v:
                    continue
                typ = (u0 + v) % 2
                counts[typ] += 1
            rho = [max(rho[t], counts[t]) for t in range(2)]
        lam = [0, 0]
        for u0 in range(n):
            if u0 == v:
                continue
            typ = (u0 + v) % 2
            key = tuple(sorted((u0, v)))
            lam[typ] = max(lam[typ], pair_degree[key])
        kcap = Fraction(max(degrees), 1) / z
        rhs_dup = Fraction(comb(m, 2) * q, 1) * kcap
        rhs_dup *= Fraction(sum(rho[t] * lam[t] for t in range(2)), d - 1)
        assert qdup <= rhs_dup

        roots.append(
            {
                "v": v,
                "d": d,
                "multiplicity": falling(d, m),
                "x": x,
                "u": u,
                "qdup": qdup,
                "hbar": hbar,
                "z": z,
                "Z": zrows,
            }
        )
    return roots


def expand_roots(roots):
    expanded = []
    for root in roots:
        expanded.extend([root] * root["multiplicity"])
    return expanded


def check_mixture(all_roots, q, n, m):
    expanded = expand_roots(all_roots)
    if not expanded:
        return 0
    # A common increasing normalized-degree test.
    a = Fraction(11, 10)
    psi = []
    for r in expanded:
        x = r["x"]
        psi.append(Fraction(0, 1) if x <= a else ((x - a) / x) ** m)
    if not any(psi):
        return 0

    rates = [r["hbar"] / r["Z"] for r in expanded]
    xs = [r["x"] for r in expanded]
    us = [r["u"] for r in expanded]
    qs = [r["qdup"] for r in expanded]
    aps = mean(psi)
    tail_x = mean([x * p for x, p in zip(xs, psi)]) / aps
    tail_u = mean([u * p for u, p in zip(us, psi)]) / aps
    tail_q = mean([qq * p for qq, p in zip(qs, psi)]) / aps
    lhs = -covariance(rates, psi) / aps
    rhs_exact = Fraction(q, n) * (
        -(tail_x - mean(xs))
        + m * (mean(us) - tail_u)
        + (tail_q - mean(qs))
    )
    assert lhs == rhs_exact
    assert tail_x >= mean(xs)
    rhs_bound = Fraction(q, n) * (
        m * max(Fraction(0, 1), mean(us) - tail_u) + tail_q
    )
    assert max(Fraction(0, 1), lhs) <= rhs_bound
    return 4


def obstruction_statistics(D, M, m):
    """Exact formulas for Section 6's K_{D,D}-bulk plus star family."""
    n = 2 * D * M + 2 * D + 1
    zrows = M * D * D + 2 * D
    z = Fraction(2 * zrows, n)

    # Root statistics.  Leaves do not support an m-carrier.
    u_star = Fraction(-1, 1)
    u_bulk = (D - z - 1) / z
    x_bulk = Fraction(D, 1) / z
    x_star = Fraction(2 * D, 1) / z
    w_bulk = 2 * D * M * falling(D, m)
    w_star = falling(2 * D, m)
    palm_u = Fraction(w_bulk * u_bulk + w_star * u_star, w_bulk + w_star)

    # Uniform-row conflict variance and global companion energy.
    bulk_rows = M * D * D
    star_rows = 2 * D
    mean_c = Fraction(bulk_rows * (2 * D - 1) + star_rows * 2 * D, zrows)
    var_c = Fraction(
        bulk_rows * (Fraction(2 * D - 1, 1) - mean_c) ** 2
        + star_rows * (Fraction(2 * D, 1) - mean_c) ** 2,
        zrows,
    )
    companion_energy = Fraction(
        bulk_rows * (Fraction(2 * D, 1) - 2 * z) ** 2
        + star_rows * (Fraction(2 * D + 1, 1) - 2 * z) ** 2,
        zrows,
    ) / z**2

    # Vertexwise centered second moment, included as a representative
    # centered degree moment from the claim following (6.4).
    degree_energy = Fraction(
        2 * D * M * (Fraction(D, 1) - z) ** 2
        + (Fraction(2 * D, 1) - z) ** 2
        + 2 * D * (Fraction(1, 1) - z) ** 2,
        n,
    ) / z**2

    return {
        "z": z,
        "u_star": u_star,
        "u_bulk": u_bulk,
        "x_bulk": x_bulk,
        "x_star": x_star,
        "palm_u": palm_u,
        "tail_deficit": palm_u - u_star,
        "conflict_variance": var_c / z**2,
        "companion_energy": companion_energy,
        "degree_energy": degree_energy,
        "hazard_star": 2 * D,
        "hazard_bulk": D + m * (D - 1),
    }


def build_obstruction(D, M):
    edges = []
    cursor = 0
    for _ in range(M):
        left = range(cursor, cursor + D)
        right = range(cursor + D, cursor + 2 * D)
        edges.extend((u, v) for u in left for v in right)
        cursor += 2 * D
    center = cursor
    leaves = range(center + 1, center + 2 * D + 1)
    edges.extend((center, u) for u in leaves)
    return center + 2 * D + 1, edges, center


def check_obstruction_by_enumeration():
    checks = 0
    for D in range(3, 6):
        for M in range(1, 4):
            n, edges, center = build_obstruction(D, M)
            roots = state_data(n, edges, m=2)
            stats = obstruction_statistics(D, M, m=2)
            assert len(roots) == 2 * D * M + 1
            assert sum(r["v"] == center for r in roots) == 1
            checks += 2
            for root in roots:
                assert root["qdup"] == 0
                if root["v"] == center:
                    assert root["d"] == 2 * D
                    assert root["u"] == -1
                    assert root["hbar"] == 2 * D
                else:
                    assert root["d"] == D
                    assert root["u"] == stats["u_bulk"]
                    assert root["hbar"] == D + 2 * (D - 1)
                checks += 4

            edge_sets = [frozenset(e) for e in edges]
            degrees = [sum(v in e for e in edge_sets) for v in range(n)]
            conflicts = [sum(bool(e & f) for f in edge_sets) for e in edge_sets]
            z = stats["z"]
            assert max(
                sum(u in e and v in e for e in edge_sets)
                for u, v in combinations(range(n), 2)
            ) == 1
            assert covariance(
                [Fraction(c, 1) for c in conflicts],
                [Fraction(c, 1) for c in conflicts],
            ) / z**2 == stats["conflict_variance"]
            assert mean(
                [
                    (Fraction(sum(degrees[v] for v in e), 1) - 2 * z) ** 2
                    for e in edge_sets
                ]
            ) / z**2 == stats["companion_energy"]
            assert mean([(Fraction(d, 1) - z) ** 2 for d in degrees]) / z**2 \
                == stats["degree_energy"]
            checks += 4
    return checks


def check_tail_local_obstruction():
    checks = 0
    a = Fraction(3, 2)
    for D in range(3, 9):
        for m in range(2, min(4, D) + 1):
            samples = [obstruction_statistics(D, M, m) for M in (10, 100, 1000)]
            for s in samples:
                assert s["z"] < D
                assert s["x_bulk"] < a < s["x_star"]
                assert s["u_star"] == -1
                assert s["hazard_bulk"] > s["hazard_star"]
                assert s["tail_deficit"] > 0
                assert s["conflict_variance"] >= 0
                assert s["companion_energy"] >= 0
                assert s["degree_energy"] >= 0
                checks += 8

            target = Fraction(D - 1, D)
            assert abs(samples[-1]["u_bulk"] + Fraction(1, D)) < Fraction(1, 100)
            assert abs(samples[-1]["palm_u"] + Fraction(1, D)) < Fraction(1, 100)
            assert abs(samples[-1]["tail_deficit"] - target) < Fraction(1, 100)
            for key in ("conflict_variance", "companion_energy", "degree_energy"):
                assert samples[-1][key] < samples[0][key] / 50
            checks += 6
    return checks + check_obstruction_by_enumeration()


def main():
    rng = random.Random(20260822)
    checks = 0
    mixtures = 0
    for _ in range(350):
        n = rng.randint(6, 9)
        q = rng.choice([2, 3])
        universe = list(combinations(range(n), q))
        roots_by_state = []
        for _state in range(2):
            rng.shuffle(universe)
            take = rng.randint(max(3, n // 2), min(len(universe), 15))
            roots = state_data(n, universe[:take], m=2)
            roots_by_state.extend(roots)
            checks += 10 * len(roots)
        got = check_mixture(roots_by_state, q, n, m=2)
        if got:
            mixtures += 1
            checks += got
    obstruction_checks = check_tail_local_obstruction()
    checks += obstruction_checks
    assert mixtures >= 200
    print(
        "PASS: contemporaneous normalized-exposure identities; "
        f"{mixtures} state mixtures, {obstruction_checks} obstruction checks, "
        f"at least {checks} exact checks"
    )


if __name__ == "__main__":
    main()
