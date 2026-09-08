#!/usr/bin/env python3
"""Finite regression checks for the Gate-A avoidance extension hierarchy.

The mathematical proof is in
MATH_THEOREM_GATE_A_AVOIDANCE_EXTENSION_HIERARCHY_AND_EROSION_REBINNING_20260822.md.
This script only exhausts small finite examples using exact rational
arithmetic.
"""

from __future__ import annotations

import itertools
import random
from collections import defaultdict
from fractions import Fraction


def falling(a: int, m: int) -> int:
    if a < m:
        return 0
    out = 1
    for j in range(m):
        out *= a - j
    return out


def disjoint(e, f) -> bool:
    return e.isdisjoint(f)


def conflict_degrees(edges):
    return [sum(not disjoint(e, f) for f in edges) for e in edges]


def degrees(n, edges):
    return [sum(v in e for e in edges) for v in range(n)]


def carriers(n, edges, roots, m):
    stars = {v: [i for i, e in enumerate(edges) if v in e] for v in roots}
    out = []
    for v in roots:
        for fs in itertools.permutations(stars[v], m):
            out.append((v, fs, ()))
    return out


def extend_objects(edges, objects):
    out = []
    for v, fs, gs in objects:
        used = fs + gs
        for k, edge in enumerate(edges):
            if all(disjoint(edge, edges[j]) for j in used):
                out.append((v, fs, gs + (k,)))
    return out


def objects(n, edges, roots, m, t):
    out = carriers(n, edges, roots, m)
    for _ in range(t):
        out = extend_objects(edges, out)
    return out


def extension_set(edges, obj):
    _, fs, gs = obj
    used = fs + gs
    return tuple(k for k, edge in enumerate(edges)
                 if all(disjoint(edge, edges[j]) for j in used))


def x_values(n, edges, roots, m, tmax):
    omega = carriers(n, edges, roots, m)
    vals = [len(omega)]
    all_objects = [omega]
    for _ in range(tmax):
        omega = extend_objects(edges, omega)
        vals.append(len(omega))
        all_objects.append(omega)
    return vals, all_objects


def induced_after_edge(n, edges, k):
    killed = edges[k]
    return [e for e in edges if disjoint(e, killed)]


def residual_after_marked(n, edges, marked):
    accepted = []
    for k in marked:
        if all(j == k or disjoint(edges[k], edges[j]) for j in marked):
            accepted.append(k)
    killed = set()
    for k in accepted:
        killed.update(edges[k])
    return [e for e in edges if e.isdisjoint(killed)]


def carrier_avoidance_r(n, edges, v, m):
    d = sum(v in e for e in edges)
    if d < m:
        return Fraction(0)
    den = falling(d, m)
    total = 0
    for g in edges:
        if v in g:
            continue
        a = sum(v in f and not disjoint(f, g) for f in edges)
        total += falling(d - a, m)
    return Fraction(total, den)


def check_case(n, edges, m, p):
    z = len(edges)
    if z == 0:
        return 0
    cdeg = conflict_degrees(edges)
    delta = max(cdeg)
    deg = degrees(n, edges)
    checks = 0

    root_sets = []
    positive = {v for v, d in enumerate(deg) if d >= m}
    if positive:
        root_sets.append(positive)
    for d in sorted(set(deg)):
        bucket = {v for v, x in enumerate(deg) if x == d and x >= m}
        if bucket:
            root_sets.append(bucket)

    for roots in root_sets:
        vals, omegas = x_values(n, edges, roots, m, 3)
        for t in range(3):
            # Prefix identity X_(t+1)=sum r(omega).
            assert vals[t + 1] == sum(len(extension_set(edges, w))
                                      for w in omegas[t])
            checks += 1

            # Exact singleton-deletion recursion.
            deleted_sum = 0
            for k in range(z):
                child = induced_after_edge(n, edges, k)
                deleted_sum += len(objects(n, child, roots, m, t))
            assert deleted_sum == vals[t + 1]
            checks += 1

        # Curvature identity and approximate log concavity.
        for t in range(2):
            if vals[t] == 0 or vals[t + 1] == 0:
                continue
            rs = [len(extension_set(edges, w)) for w in omegas[t]]
            qt = Fraction(vals[t + 1], vals[t])
            qt1 = Fraction(vals[t + 2], vals[t + 1])
            mean2 = sum(r * r for r in rs) / Fraction(len(rs))
            var = mean2 - qt * qt
            kappas = []
            for w in omegas[t + 1]:
                prefix = (w[0], w[1], w[2][:-1])
                k = w[2][-1]
                dset = extension_set(edges, prefix)
                kap = sum(not disjoint(edges[j], edges[k]) for j in dset)
                kappas.append(kap)
            ekappa = Fraction(sum(kappas), len(kappas))
            assert qt1 - qt == var / qt - ekappa
            checks += 1
            s = m + t
            if z > s * delta:
                upper = Fraction(s * s * delta * delta,
                                 4 * (z - s * delta))
                assert max(Fraction(0), qt1 - qt) <= upper
                assert Fraction(vals[t] * vals[t + 2],
                                vals[t + 1] * vals[t + 1]) <= (
                    1 + Fraction(s * s * delta * delta,
                                 4 * (z - s * delta) ** 2))
                cbar = Fraction(sum(cdeg), z)
                affine_error = Fraction((s * s + 12 * s) * delta * delta,
                                        4 * (z - s * delta))
                assert abs(qt1 - (qt - cbar)) <= affine_error
                # Check the sharper conditional-kappa estimate (2.14)
                # carrier by carrier.
                for obj in omegas[t]:
                    dset = extension_set(edges, obj)
                    if not dset:
                        continue
                    mean_kappa = Fraction(sum(
                        sum(j in dset and not disjoint(edges[j], edges[k])
                            for j in range(z))
                        for k in dset), len(dset))
                    sharp = Fraction(3 * s * delta * delta,
                                     z - s * delta)
                    assert abs(mean_kappa - cbar) <= sharp
                checks += 4

        # q_0 is the carrier-Palm mean of the exact R_m formula.
        if vals[0] > 0:
            weighted = sum(falling(deg[v], m) * carrier_avoidance_r(n, edges, v, m)
                           for v in roots)
            assert Fraction(vals[1], vals[0]) == weighted / vals[0]
            checks += 1
            if len({deg[v] for v in roots}) == 1:
                direct = sum(carrier_avoidance_r(n, edges, v, m) for v in roots)
                direct /= len(roots)
                assert Fraction(vals[1], vals[0]) == direct
                checks += 1

        # Exact finite isolated-bite expectation and (4.7).
        if z <= 9:
            ex = [Fraction(0) for _ in range(2)]
            for mask in range(1 << z):
                marked = [k for k in range(z) if (mask >> k) & 1]
                prob = p ** len(marked) * (1 - p) ** (z - len(marked))
                child = residual_after_marked(n, edges, marked)
                for t in range(2):
                    ex[t] += prob * len(objects(n, child, roots, m, t))
            for t in range(2):
                if vals[t] == 0:
                    continue
                qt = Fraction(vals[t + 1], vals[t])
                ratio = ex[t] / vals[t]
                lower = 1 - p * (z - qt)
                c_s = Fraction((m + t) ** 2, 2) + (m + t)
                upper = lower + c_s * (p * delta) ** 2
                assert lower <= ratio <= upper
                checks += 1

        # Erosion-rebinning row sums and direct child-column enumeration.
        y = defaultdict(int)
        wsum = defaultdict(int)
        triples_by_degree = defaultdict(list)
        for obj in omegas[0]:
            v, fs, _ = obj
            d = deg[v]
            for k in extension_set(edges, obj):
                a = sum(v in f and not disjoint(f, edges[k]) for f in edges)
                e = d - a
                child_ext = sum(
                    all(disjoint(edges[g], edges[j]) for j in fs + (k,))
                    for g in range(z)
                )
                y[d, e] += 1
                wsum[d, e] += child_ext
                triples_by_degree[d].append((child_ext, e))
        for d in {a for a, _ in y}:
            # Compare each old-degree row against the corresponding bucket
            # extension counts, including when the chosen root set is mixed.
            bucket = {v for v in roots if deg[v] == d}
            bvals, _ = x_values(n, edges, bucket, m, 2)
            assert sum(vv for (a, _), vv in y.items() if a == d) == bvals[1]
            assert sum(vv for (a, _), vv in wsum.items() if a == d) == bvals[2]
            checks += 2
            if d > 0 and z > m * delta:
                triples = triples_by_degree[d]
                count = len(triples)
                mean_q = Fraction(sum(q for q, _ in triples), count)
                mean_psi = Fraction(sum(e for _, e in triples), count * d)
                mean_product = Fraction(sum(q * e for q, e in triples), count * d)
                covariance = mean_product - mean_q * mean_psi
                erosion_bound = Fraction((m + 1) * delta * delta,
                                          z - m * delta)
                assert abs(covariance) <= erosion_bound
                checks += 1

        direct_y = defaultdict(int)
        direct_w = defaultdict(int)
        for k in range(z):
            child = induced_after_edge(n, edges, k)
            child_deg = degrees(n, child)
            for v, fs, _ in carriers(n, child, roots, m):
                e = child_deg[v]
                direct_y[e] += 1
                obj = (v, fs, ())
                direct_w[e] += len(extension_set(child, obj))
        assert {e: sum(vv for (d, ee), vv in y.items() if ee == e)
                for e in direct_y} == dict(direct_y)
        assert {e: sum(vv for (d, ee), vv in wsum.items() if ee == e)
                for e in direct_w} == dict(direct_w)
        checks += 2
    return checks


def random_hypergraph(rng, n, uniformity, edge_count):
    universe = list(itertools.combinations(range(n), uniformity))
    chosen = rng.sample(universe, min(edge_count, len(universe)))
    return [frozenset(e) for e in chosen]


def main():
    rng = random.Random(20260822)
    total = 0
    cases = 0
    # Include hand-built disconnected and overlapping examples.
    fixtures = [
        (6, [frozenset(e) for e in [(0, 1), (0, 2), (1, 2),
                                    (3, 4), (3, 5), (4, 5)]]),
        (7, [frozenset(e) for e in [(0, 1, 2), (0, 3, 4),
                                    (1, 3, 5), (2, 4, 6),
                                    (0, 5, 6), (1, 4, 6)]]),
    ]
    for n, edges in fixtures:
        for m in (1, 2):
            total += check_case(n, edges, m, Fraction(1, 101))
            cases += 1
    for n in range(5, 8):
        for uniformity in (2, 3):
            if uniformity > n:
                continue
            for _ in range(35):
                edge_count = rng.randint(3, min(8, len(list(itertools.combinations(range(n), uniformity)))))
                edges = random_hypergraph(rng, n, uniformity, edge_count)
                for m in (1, 2):
                    total += check_case(n, edges, m, Fraction(1, 127))
                    cases += 1
    print(f"GATE_A_AVOIDANCE_EXTENSION_HIERARCHY_PASS cases={cases} checks={total}")


if __name__ == "__main__":
    main()
