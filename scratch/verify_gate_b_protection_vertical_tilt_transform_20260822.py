#!/usr/bin/env python3
"""Exact finite checks for the Gate-B protection/vertical-tilt reduction."""

from fractions import Fraction as F
from itertools import combinations
import random


def mean(xs):
    return sum(xs, F(0)) / len(xs)


def check_factorization_and_palm():
    # Start from complete b-subset catalogues, then take an irregular labelled
    # survivor subcatalogue with duplicates.  Integer weights test (2.3),
    # including nonconstant/empty protection, while summing the combined
    # potential tests (2.11).
    for N in range(3, 9):
        for b in range(1, N):
            complete = list(combinations(range(N), b))
            irregular = [
                row for i, row in enumerate(complete)
                if (5 * i * i + 7 * i + N + b) % 11 < 6
            ]
            if not irregular:
                irregular = [complete[0]]
            irregular.extend(irregular[: min(3, len(irregular))])
            for rows in (complete, irregular):
                Z = len(rows)
                weights = [
                    F(1 + ((7 * i * i + 3 * i) % 13)) for i in range(Z)
                ]
                Ew = mean(weights)
                exp_q = []
                for t in range(N):
                    star = [i for i, row in enumerate(rows) if t in row]
                    X = len(star)
                    lhs = sum(
                        (weights[i] for i in star), F(0)
                    ) / (Z * Ew)
                    if X == 0:
                        assert lhs == 0
                        exp_q.append(F(0))
                        continue
                    rooted = mean([weights[i] for i in star])
                    protection_factor = F(X, Z) / F(b, N)
                    rhs = F(b, N) * protection_factor * rooted / Ew
                    assert lhs == rhs
                    exp_q.append(F(N, b) * lhs)
                assert sum(exp_q, F(0)) == N


def check_vertical_size_bias_and_one_sided_cap():
    rng = random.Random(20260822)
    checked = 0
    for _ in range(4000):
        Z = rng.randint(5, 30)
        n = rng.randint(3, 14)
        two_b = 2 * rng.randint(1, 5)
        matrix = [[rng.randrange(2) for _ in range(n)] for _ in range(Z)]
        degrees = [sum(matrix[f][t] for f in range(Z)) for t in range(n)]
        if max(degrees) == 0:
            continue
        scores = [F(sum(row), two_b) for row in matrix]
        mu = mean(scores)
        if mu == 0:
            continue
        var = mean([(x - mu) ** 2 for x in scores])
        p = [F(d, Z) for d in degrees]

        # (4.18): incidence-weighted rooted mean gap equals 2b Var(Phi).
        deltas = []
        for t in range(n):
            star = [f for f in range(Z) if matrix[f][t]]
            deltas.append(
                mean([scores[f] for f in star]) - mu if star else F(0)
            )
        assert sum((p[t] * deltas[t] for t in range(n)), F(0)) == two_b * var

        event = [f for f in range(Z) if (11 * f + 5) % 17 < 6]
        if not event:
            continue
        u = F(len(event), Z)
        event_mean = mean([scores[f] for f in event])
        if event_mean == 0:
            continue
        beta = u * event_mean / mu
        assert F(0) < beta <= 1
        amplification = []
        for t in range(n):
            x_event = sum(matrix[f][t] for f in event)
            amplification.append(
                F(x_event, degrees[t]) / u if degrees[t] else F(0)
            )

        omega = [pt / (two_b * mu) for pt in p]
        assert sum(omega, F(0)) == 1
        R_event = event_mean / mu
        assert sum((omega[t] * amplification[t] for t in range(n)), F(0)) == R_event

        # Theorem 5.3 with beta_0 chosen as the exact beta.
        g0 = beta / (2 - beta)
        preliminary = [
            t for t in range(n)
            if degrees[t] and amplification[t] >= R_event / 2
        ]
        assert sum((omega[t] for t in preliminary), F(0)) >= g0

        avg_p = mean(p)
        cap_R = max(p) / avg_p
        moderate = {t for t in range(n) if p[t] >= g0 * avg_p / 2}
        good = [t for t in preliminary if t in moderate]
        good_mass = sum((omega[t] for t in good), F(0))
        assert good_mass >= g0 / 2
        assert F(len(good), n) >= g0 / (2 * cap_R)

        b_value = F(two_b, 2)
        target_floor = g0 * b_value * event_mean / (2 * n)
        for t in good:
            assert p[t] * amplification[t] >= target_floor
        checked += 1
    assert checked >= 1000


def check_moment_to_tail():
    # Corollary 5.4 after eliminating the arbitrary scale xi:
    # threshold = E Phi^2/(2 E Phi), and its tail has mass at least
    # E Phi^2/(2Q^2).  The incidence share has the stated square lower bound.
    rng = random.Random(541954)
    for _ in range(3000):
        Q = rng.randint(1, 20)
        values = [F(rng.randint(0, Q)) for _ in range(rng.randint(2, 30))]
        mu = mean(values)
        if mu == 0:
            continue
        second = mean([x * x for x in values])
        threshold = second / (2 * mu)
        event = [x for x in values if x >= threshold]
        probability = F(len(event), len(values))
        assert probability >= second / (2 * Q * Q)
        event_mean = mean(event)
        beta = probability * event_mean / mu
        assert beta >= second * second / (4 * Q * Q * mu * mu)


def check_geometric_peeling_mass():
    # Exact rational replay of (5.5)--(5.6), including finite truncations.
    for c in (F(1, 7), F(1, 3), F(2, 5), F(3, 4), F(1)):
        for xi0 in (F(1, 100), F(2, 7), F(9, 10)):
            xis = [xi0 * (1 - c) ** i for i in range(40)]
            assert sum(xis, F(0)) <= xi0 / c
            if c < 1:
                assert sum(xis, F(0)) < xi0 / c
            else:
                assert sum(xis, F(0)) == xi0


def main():
    check_factorization_and_palm()
    check_vertical_size_bias_and_one_sided_cap()
    check_moment_to_tail()
    check_geometric_peeling_mass()
    print("gate-B protection/vertical-tilt exact checks: PASS")


if __name__ == "__main__":
    main()
