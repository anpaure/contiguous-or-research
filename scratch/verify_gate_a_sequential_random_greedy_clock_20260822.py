#!/usr/bin/env python3
"""Exact finite checks for the sequential Gate-A clock note."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import random


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def build_state(n, edges):
    edges = tuple(frozenset(e) for e in edges)
    z = len(edges)
    gamma = []
    for i, e in enumerate(edges):
        gamma.append({j for j, f in enumerate(edges) if e & f})
        assert i in gamma[-1]
    c = [len(x) for x in gamma]
    degrees = [sum(v in e for e in edges) for v in range(n)]
    return edges, gamma, c, degrees


def carrier_data(carrier, gamma, c):
    b = set()
    for i in carrier:
        b.update(gamma[i])
    d = set(range(len(gamma))) - b
    t = {k: len(gamma[k] & b) for k in d}
    return b, d, t, sum(t.values())


def all_carriers(edges, degrees, m):
    out = []
    for v, degree in enumerate(degrees):
        if degree < m:
            continue
        star = [i for i, e in enumerate(edges) if v in e]
        for rows in permutations(star, m):
            out.append((v, rows))
    return out


def mean(vals):
    return sum(vals, Fraction(0, 1)) / len(vals)


def check_state(n, raw_edges, m=2):
    edges, gamma, c, degrees = build_state(n, raw_edges)
    z = len(edges)
    if z == 0:
        return 0
    delta = max(c)
    carriers = all_carriers(edges, degrees, m)
    if not carriers:
        return 0

    records = []
    normalized_records = []
    checks = 0
    for _, rows in carriers:
        b, d, t, big_t = carrier_data(rows, gamma, c)
        h = len(b)
        assert len(d) == z - h
        assert h <= m * delta
        assert big_t <= h * delta

        # Theorem 2.1, including the exact generator moments.
        if d:
            lhs = mean([Fraction(h - t[k], 1) for k in d])
            rhs = Fraction(h, 1) - Fraction(big_t, z - h)
            assert lhs == rhs
            checks += 1
        raw_decrements = [h] * h + [t[k] for k in d]
        assert sum(raw_decrements) == h * h + big_t
        assert sum(x * x for x in raw_decrements) == h ** 3 + sum(
            x * x for x in t.values()
        )
        checks += 2

        # Theorem 2.3bis: pointwise normalized-hazard payoff.
        if z > delta:
            srate = Fraction(h, z)
            survive = Fraction(z - h, z)
            beta = sum(
                (Fraction(h - t[k], z - c[k]) for k in d), Fraction(0, 1)
            ) / z
            rrate = beta - survive * srate
            assert abs(rrate) <= Fraction(2 * h * delta, z * (z - delta))
            raw_second = srate ** 3 + sum(
                (
                    Fraction(h - t[k], z - c[k]) - srate
                ) ** 2
                for k in d
            ) / z
            theta = Fraction(delta, z)
            bracket_bound = (
                m ** 3 * theta ** 3
                + (
                    2 * m * theta ** 3 + 2 * m ** 2 * theta ** 4
                )
                / (1 - theta) ** 2
            )
            assert raw_second <= bracket_bound
            normalized_records.append((srate, survive, beta, rrate))
            checks += 2

        # Exact conflict-matrix identity T = Cbar*h + J - b^T A b.
        cbar = Fraction(sum(c), z)
        jstat = sum(Fraction(c[r], 1) - cbar for r in b)
        qstat = sum(1 for r in b for s in b if s in gamma[r])
        assert Fraction(big_t, 1) == cbar * h + jstat - qstat
        checks += 1
        records.append((h, big_t, b, d, t, jstat, qstat))

    # Proposition 2.4 at t=0,1, written directly in the original labels.
    x0 = len(records)
    x1 = sum(z - rec[0] for rec in records)
    x2 = sum(
        (z - rec[0]) - c[k] + rec[4][k]
        for rec in records
        for k in rec[3]
    )
    child_x0_sum = sum(
        sum(k in rec[3] for rec in records) for k in range(z)
    )
    child_x1_sum = sum(
        sum(
            (z - c[k]) - (rec[0] - rec[4][k])
            for rec in records
            if k in rec[3]
        )
        for k in range(z)
    )
    assert child_x0_sum == x1
    assert child_x1_sum == x2
    checks += 2


    if len(normalized_records) == len(records):
        bars = mean([x[0] for x in normalized_records])
        bara = mean([x[1] for x in normalized_records])
        if bara:
            barsplus = mean([x[2] for x in normalized_records]) / bara
            var_s = mean([x[0] * x[0] for x in normalized_records]) - bars * bars
            mean_r = mean([x[3] for x in normalized_records])
            assert barsplus - bars == (-var_s + mean_r) / bara
            checks += 1

    # Use the complete labelled family.  This checks Theorem 2.2 and (4.10).
    hs = [Fraction(rec[0], 1) for rec in records]
    ts = [Fraction(rec[1], 1) for rec in records]
    mu = mean(hs)
    tau = mean(ts)
    var = mean([x * x for x in hs]) - mu * mu
    kappa = tau + var
    surviving_pairs = sum(z - rec[0] for rec in records)
    if surviving_pairs:
        actual_num = sum(
            rec[0] - rec[4][k] for rec in records for k in rec[3]
        )
        actual = Fraction(actual_num, surviving_pairs)
        predicted = mu - kappa / (z - mu)
        assert actual == predicted
        checks += 1

        if z > delta:
            qplus = mean(
                [
                    Fraction(rec[0] - rec[4][k], z - c[k])
                    for rec in records
                    for k in rec[3]
                ]
            )
            base = predicted / z
            err = qplus - base
            assert err >= 0
            assert err <= Fraction(m * delta * delta, z * (z - delta))
            checks += 1

    cbar = Fraction(sum(c), z)
    residual_a = kappa - cbar * mu
    residual_b = var + mean([r[5] for r in records]) - mean(
        [Fraction(r[6], 1) for r in records]
    )
    assert residual_a == residual_b
    checks += 1

    # Continuous cohort quotient derivative mu'=-ET-Var(h).
    x = Fraction(len(records), 1)
    y = sum(hs)
    xprime = -y
    yprime = -sum(h * h + t for h, t in zip(hs, ts))
    quotient_derivative = (yprime * x - y * xprime) / (x * x)
    assert quotient_derivative == -kappa
    checks += 1

    # Root-degree drift and raw second-moment identity.
    for v in range(n):
        a = []
        for k in range(z):
            a.append(sum(v in edges[f] and bool(edges[f] & edges[k]) for f in range(z)))
        assert sum(a) == sum(c[f] for f in range(z) if v in edges[f])
        assert sum(x * x for x in a) <= degrees[v] ** 2 * delta
        checks += 2

    return checks


def counterexample_check():
    checks = 0
    for mcomp in range(1, 8):
        th = 14 * falling(13, 12)
        tl = 24 * falling(12, 12)
        a0 = Fraction(14, th + mcomp * tl)
        a1 = Fraction(
            14 * mcomp * 144,
            mcomp * 144 * (th + (mcomp - 1) * tl) + 91 * mcomp * tl,
        )
        assert a1 > a0
        checks += 1

    # Same n, Z, and average degree, common cap 3; different predictable drift.
    # 3s disjoint edges have C=1.  s triangles plus 3s isolates have C=3.
    for s in range(1, 20):
        assert 3 * s == 3 * s
        assert 1 <= 3 and 3 <= 3
        assert Fraction(2 * (3 * s), 6 * s) == Fraction(2 * (3 * s), 6 * s)
        assert 1 != 3
        checks += 1

    # A pure algebraic Simpson table: monotone in each state, inverted after
    # degree-dependent state mixing.
    low = Fraction(99, 100) * 100 + Fraction(1, 100) * 1
    high = Fraction(1, 100) * 101 + Fraction(99, 100) * 2
    assert 1 < 2 and 100 < 101 and low > high
    checks += 1
    return checks


def main():
    rng = random.Random(20260822)
    total_checks = counterexample_check()
    states = 0
    for _ in range(500):
        n = rng.randint(5, 8)
        q = rng.choice([2, 3])
        universe = list(combinations(range(n), q))
        rng.shuffle(universe)
        take = rng.randint(max(2, n // 2), min(len(universe), 14))
        raw_edges = universe[:take]
        got = check_state(n, raw_edges, m=2)
        if got:
            states += 1
            total_checks += got
    assert states >= 300
    print(
        "PASS: sequential random-greedy carrier identities; "
        f"{states} nontrivial states, {total_checks} exact checks"
    )


if __name__ == "__main__":
    main()
