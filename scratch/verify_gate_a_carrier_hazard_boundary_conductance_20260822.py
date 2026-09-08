#!/usr/bin/env python3
"""Exact finite-hypergraph checks for carrier hazard boundary conductance."""

from fractions import Fraction as F
from itertools import combinations, permutations
import hashlib
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "MATH_THEOREM_GATE_A_CARRIER_HAZARD_BOUNDARY_CONDUCTANCE_20260822.md"
RNG = random.Random(2026082202)


def falling(n, m):
    out = 1
    for i in range(m):
        out *= n - i
    return out


def conflict_data(edges):
    gamma = []
    for e in edges:
        gamma.append({j for j, f in enumerate(edges) if e & f})
    delta = max(map(len, gamma), default=0)
    return gamma, delta


def hazard_and_boundary(conf, carrier):
    B = set().union(*(conf[i] for i in carrier))
    D = set(range(len(conf))) - B
    h = len(B)
    T = sum(len(conf[k] & B) for k in D)
    assert T == sum(len(conf[r] & D) for r in B)
    return B, h, T


def bite_distribution(edges, p):
    z = len(edges)
    out = []
    for mask in range(1 << z):
        marked = {i for i in range(z) if (mask >> i) & 1}
        accepted = {
            i
            for i in marked
            if all(i == j or not (edges[i] & edges[j]) for j in marked)
        }
        deleted = set().union(*(edges[i] for i in accepted)) if accepted else set()
        residual = tuple(i for i, e in enumerate(edges) if not (e & deleted))
        prob = p ** len(marked) * (1 - p) ** (z - len(marked))
        out.append((prob, residual))
    return out


def conditional_stats(edges, conf, carrier, p, dist):
    B, h, T = hazard_and_boundary(conf, carrier)
    den = F(0)
    num = F(0)
    carrier_set = set(carrier)
    for prob, residual in dist:
        residual_set = set(residual)
        if not carrier_set <= residual_set:
            continue
        den += prob
        child_h = 0
        for r in residual:
            if any(edges[r] & edges[i] for i in carrier):
                child_h += 1
        num += prob * child_h
    assert den > 0
    return h, T, den, num, num / den


def check_instance(edges, m, p):
    conf, delta = conflict_data(edges)
    theta = p * delta
    assert m * theta <= F(1, 4)

    carriers = []
    for root in sorted(set().union(*edges)):
        star = [i for i, e in enumerate(edges) if root in e]
        carriers.extend(combinations(star, m))
    if not carriers:
        return 0

    dist = bite_distribution(edges, p)
    rows = []
    C = lambda s: F(s * s, 2) + s
    Cstar = 2 * (C(m + 1) + C(m) + m)
    for carrier in carriers:
        h, T, den, num, observed = conditional_stats(edges, conf, carrier, p, dist)
        predicted = h - p * T
        assert abs(observed - predicted) <= Cstar * h * theta * theta

        # Empty/singleton derivative coefficients.
        assert -h == -len(hazard_and_boundary(conf, carrier)[0])
        nprime = -h * h - T
        assert nprime - h * (-h) == -T
        rows.append((carrier, h, T, den, num))

    # Test Theorem 3.1 separately in each root bucket.
    checks = len(rows)
    by_root = {}
    for row in rows:
        root_candidates = set(edges[row[0][0]]).intersection(
            *(edges[i] for i in row[0][1:])
        )
        for root in root_candidates:
            by_root.setdefault(root, []).append(row)
    Cfam = 2 * (C(m + 1) + 2 * C(m) + m * (m + 1))
    for root, bucket in by_root.items():
        # Deduplicate carriers when a carrier has several common roots.
        unique = {row[0]: row for row in bucket}
        bucket = list(unique.values())
        n = F(len(bucket))
        mu = sum((F(row[1]) for row in bucket), F(0)) / n
        tau = sum((F(row[2]) for row in bucket), F(0)) / n
        eh2 = sum((F(row[1] * row[1]) for row in bucket), F(0)) / n
        var = eh2 - mu * mu

        # Exact two-blocker formulas (3.10)--(3.12).
        star = [i for i, e in enumerate(edges) if root in e]
        d = len(star)
        denom = falling(d, m)
        assert denom > 0
        p0 = {}
        p00 = {}
        for r in range(len(edges)):
            ar = sum(bool(edges[f] & edges[r]) for f in star)
            p0[r] = F(falling(d - ar, m), denom) if d - ar >= m else F(0)
            for k in range(len(edges)):
                ark = sum(bool(edges[f] & (edges[r] | edges[k])) for f in star)
                p00[r, k] = (
                    F(falling(d - ark, m), denom) if d - ark >= m else F(0)
                )
        tau_formula = sum(
            (
                p0[k] - p00[r, k]
                for r in range(len(edges))
                for k in range(len(edges))
                if edges[r] & edges[k]
            ),
            F(0),
        )
        eh2_formula = sum(
            (
                1 - p0[r] - p0[k] + p00[r, k]
                for r in range(len(edges))
                for k in range(len(edges))
            ),
            F(0),
        )
        mu_formula = sum((1 - p0[r] for r in range(len(edges))), F(0))
        assert tau == tau_formula
        assert eh2 == eh2_formula
        assert mu == mu_formula

        # Conflict-matrix compression (4.4), (4.8), and (4.9).
        z = len(edges)
        amat = [[int(bool(edges[r] & edges[k])) for k in range(z)] for r in range(z)]
        a2 = [
            [sum(amat[r][u] * amat[u][k] for u in range(z)) for k in range(z)]
            for r in range(z)
        ]
        a3 = [
            [sum(a2[r][u] * amat[u][k] for u in range(z)) for k in range(z)]
            for r in range(z)
        ]
        degrees = [sum(row) for row in amat]
        cbar = F(sum(degrees), z)
        js = []
        ws = []
        for carrier, h, tval, *_ in bucket:
            B, _, _ = hazard_and_boundary(conf, carrier)
            jval = sum((F(degrees[r]) - cbar for r in B), F(0))
            wval = sum(a3[f][g] for f in carrier for g in carrier)
            assert cbar * h + jval - wval <= tval
            assert tval <= cbar * h + jval
            js.append(jval)
            ws.append(F(wval))
        mean_j = sum(js, F(0)) / n
        mean_w = sum(ws, F(0)) / n
        j_formula = sum(
            ((1 - p0[r]) * (F(degrees[r]) - cbar) for r in range(z)), F(0)
        )
        w_formula = F(m, d) * sum((a3[f][f] for f in star), 0)
        if m >= 2:
            w_formula += F(m * (m - 1), d * (d - 1)) * sum(
                a3[f][g] for f in star for g in star if f != g
            )
        assert mean_j == j_formula
        assert mean_w == w_formula

        den = sum((row[3] for row in bucket), F(0)) / n
        num = sum((row[4] for row in bucket), F(0)) / n
        observed = num / den
        predicted = mu - p * (tau + var)
        assert abs(observed - predicted) <= Cfam * mu * theta * theta
        checks += 1
    return checks


def main():
    text = NOTE.read_text()
    for token in (
        "=-T_\\gamma",
        "finite-bite **ancestor-row hazard evolution**",
        "does not perform that stopped comparison",
    ):
        assert token in text, token

    # Exact witness (3.7b)--(3.7d): tau is constant but V increases.
    witness_edges = [
        frozenset(map(int, s))
        for s in ("04", "01", "134", "13", "234", "02", "013", "024", "034")
    ]
    witness_conf, _ = conflict_data(witness_edges)
    witness_values = []
    for root in (1, 0):
        star = [i for i, edge in enumerate(witness_edges) if root in edge]
        vals = [
            hazard_and_boundary(witness_conf, carrier)[1:]
            for carrier in permutations(star, 2)
        ]
        nvals = F(len(vals))
        mu = sum((F(h) for h, _ in vals), F(0)) / nvals
        tau = sum((F(t) for _, t in vals), F(0)) / nvals
        var = sum((F(h * h) for h, _ in vals), F(0)) / nvals - mu * mu
        witness_values.append((mu, tau, var))
    assert witness_values == [
        (F(53, 6), F(1), F(5, 36)),
        (F(44, 5), F(1), F(4, 25)),
    ]
    assert witness_values[1][1] == witness_values[0][1]
    assert sum(witness_values[1][1:]) > sum(witness_values[0][1:])

    checks = 0
    instances = 0
    for n_vertices in (4, 5):
        universe = list(range(n_vertices))
        possible = [frozenset(s) for k in (2, 3) for s in combinations(universe, k)]
        for _ in range(90):
            z = RNG.randrange(4, min(9, len(possible)) + 1)
            edges = RNG.sample(possible, z)
            conf, delta = conflict_data(edges)
            if not delta:
                continue
            for m in (1, 2, 3):
                p = F(1, 40 * m * delta)
                checks += check_instance(edges, m, p)
                instances += 1

    digest = hashlib.sha256(NOTE.read_bytes()).hexdigest()
    print(
        "GATE_A_CARRIER_HAZARD_BOUNDARY_CONDUCTANCE_PASS",
        f"instances={instances}",
        f"checks={checks}",
        f"note_sha256={digest}",
    )


if __name__ == "__main__":
    main()
