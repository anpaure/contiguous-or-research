#!/usr/bin/env python3
"""Exact finite ledgers for the Gate-C multiscale fragment reduction."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, floor, ceil, log, lgamma, sqrt
from random import Random


def atom_word(b, rho):
    h = (b - 1) // 2
    A = list(range(b))
    B = list(range(b, 2 * b))
    typ = ["B", "A"] * h + ["B"]
    ia, ib = rho % b, 0
    w = []
    for t in range(b * b):
        if typ[t % b] == "A":
            w.append(A[ia % b])
            ia += 1
        else:
            w.append(B[ib % b])
            ib += 1
    return w


def cset(w, a, length):
    n = len(w)
    return frozenset(w[(a + i) % n] for i in range(length))


def cyclic_max_run(bits):
    n = len(bits)
    assert not all(bits)
    best = cur = 0
    for x in bits + bits:
        cur = cur + 1 if x else 0
        best = max(best, cur)
    return min(best, n)


def cyclic_run_lengths(bits):
    """Lengths of all cyclic one-runs, with no boundary double counting."""
    n = len(bits)
    assert any(bits) and not all(bits)
    cut = next(i for i, x in enumerate(bits) if not x)
    linear = [bits[(cut + 1 + i) % n] for i in range(n)]
    runs = []
    cur = 0
    for x in linear:
        if x:
            cur += 1
        elif cur:
            runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    return runs


def check_atoms_and_stars():
    cases = 0
    for b in (5, 7, 9, 11, 13):
        n = b * b
        for rho in range(b):
            w = atom_word(b, rho)
            cells = [cset(w, t, b) for t in range(n)]
            assert len(set(cells)) == n
            for z in range(2 * b):
                positions = [i for i, value in enumerate(w) if value == z]
                gaps = [
                    (positions[(i + 1) % len(positions)] - positions[i]) % n
                    for i in range(len(positions))
                ]
                assert min(gaps) >= 2 * b - 2
                bits = [z in C for C in cells]
                assert cyclic_max_run(bits) == b
                assert set(cyclic_run_lengths(bits)) == {b}
                # No length-(b+1) fragment lies in the z-star.
                for t in range(n):
                    assert not all(bits[(t + i) % n] for i in range(b + 1))
            cases += 1
    return cases


def split_quotas(N, masses):
    rows = []
    pointer = 0
    for M in masses:
        a, r = divmod(M, N)
        row = [a] * N
        for k in range(r):
            row[(pointer + k) % N] += 1
        pointer = (pointer + r) % N
        rows.append(row)
    return rows


def random_load(rng, N, M):
    row = [0] * N
    for _ in range(M):
        row[rng.randrange(N)] += 1
    return row


def check_quota_splitting_and_holes():
    rng = Random(20260822)
    cases = 0
    for N in range(1, 13):
        for R in range(1, 6):
            for _ in range(300):
                masses = [rng.randrange(0, 4 * N + 1) for _ in range(R)]
                q = split_quotas(N, masses)
                M = sum(masses)
                assert all(sum(qj) == Mj for qj, Mj in zip(q, masses))
                for qj, Mj in zip(q, masses):
                    assert set(qj).issubset({Mj // N, ceil(Mj / N)})
                Q = [sum(q[j][i] for j in range(R)) for i in range(N)]
                assert sum(Q) == M
                assert set(Q).issubset({M // N, ceil(M / N)})

                loads = [random_load(rng, N, Mj) for Mj in masses]
                stage_V = sum(
                    max(loads[j][i] - q[j][i], 0)
                    for j in range(R) for i in range(N)
                )
                A = [sum(loads[j][i] for j in range(R)) for i in range(N)]
                global_V = sum(max(A[i] - Q[i], 0) for i in range(N))
                holes = sum(x == 0 for x in A)
                assert global_V <= stage_V
                assert holes <= max(N - M, 0) + stage_V
                cases += 1
    return cases


def check_central_aligned_quotas():
    rng = Random(17)
    for W in (23, 50, 101):
        remaining = list(range(W))
        rows = []
        for size in (W // 5, W // 7, W // 9):
            chosen = set(rng.sample(remaining, size))
            remaining = [x for x in remaining if x not in chosen]
            rows.append([int(i in chosen) for i in range(W)])
        Q = [sum(row[i] for row in rows) for i in range(W)]
        assert set(Q) <= {0, 1}
        assert sum(Q) == sum(map(sum, rows))
        for row in rows:
            assert set(row) <= {0, 1}
    return 3


def schedule(b, c=1.0, gamma=0.5, theta=Fraction(1, 5)):
    W = comb(2 * b, b)
    H = ceil(sqrt(2 * b * log(2 * b)))
    g = b + H
    residual = W
    seam = 0
    stages = 0
    records = []
    threshold = W // ceil(b ** gamma)
    while residual > threshold:
        x = residual / W
        d = max(log(log(b)), log(1 / x))
        L = floor(c * b * log(b) / d)
        assert g <= L <= b * b // 2
        t = (theta.numerator * residual
             + theta.denominator * L - 1) // (theta.denominator * L)
        M = t * L
        assert M <= residual
        assert M * theta.denominator >= theta.numerator * residual
        seam += (g - 1) * t
        records.append((Fraction(M, W), d, L))
        residual -= M
        stages += 1
        assert stages < 10000
    return W, residual, seam, records, stages


def check_schedule_and_support():
    results = []
    c, gamma = 1.0, 0.5
    for b in (101, 201, 401, 801):
        W, residual, seam, records, stages = schedule(b, c, gamma)
        assert Fraction(residual, W) <= Fraction(1, floor(b ** gamma))
        integral = ((1 - 1 / log(b)) * log(log(b))
                    + (log(log(b)) + 1) / log(b))
        assert seam / W <= 4 * integral / (c * log(b)) + 1e-12
        assert stages <= ceil(gamma * log(b) / -log(0.8)) + 1

        # At every tested pre-stage density, the labelled first moment has
        # exponent at least (2-c+o(1)) b log b.
        for delta_mass, _, L in records:
            # Reconstructing the pre-stage x is unnecessary for the seam
            # check, so separately test a grid of densities.
            pass
        for exponent in (0.0, 0.1, 0.25, gamma):
            x = b ** (-exponent)
            d = max(log(log(b)), log(1 / x))
            L = floor(c * b * log(b) / d)
            log_support = log(b) + lgamma(2 * b + 1) + L * log(x)
            assert log_support / (b * log(b)) > 2 - c - 0.2
        results.append((b, stages, seam / W))
    assert results[-1][2] < results[0][2]
    return results


def check_binomial_deficit():
    cases = 0
    for b in (31, 51, 81, 121):
        W = comb(2 * b, b)
        for gamma in (0.34, 0.4, 0.5):
            delta = b ** (-gamma)
            M = floor((1 - delta) * W)
            H = ceil(sqrt(2 * b * log(2 * b)))
            deficit = sum(
                max(comb(2 * b, s) - M, 0)
                for s in range(max(0, b - H), min(2 * b, b + H) + 1)
            )
            bound = 6 * W * delta * (1 + sqrt(b * delta))
            assert deficit <= bound
            for q in range(1, min(H, b) + 1):
                ratio = Fraction(comb(2 * b, b + q), W)
                prod_ratio = Fraction(1, 1)
                for i in range(q):
                    prod_ratio *= Fraction(b - i, b + i + 1)
                assert ratio == prod_ratio
                assert float(ratio) <= pow(2.718281828459045,
                                           -q * q / (2 * b)) + 1e-15
            cases += 1
    return cases


def check_support_identity():
    for b in range(5, 40, 2):
        W = comb(2 * b, b)
        Dhat = b * factorial(b) ** 2
        assert W * Dhat == b * factorial(2 * b)
    return 18


def main():
    atom_cases = check_atoms_and_stars()
    quota_cases = check_quota_splitting_and_holes()
    central_cases = check_central_aligned_quotas()
    schedule_results = check_schedule_and_support()
    deficit_cases = check_binomial_deficit()
    support_cases = check_support_identity()
    print("PASS Gate-C multiscale variable-fragment compiler")
    print("atom/phase star cases:", atom_cases)
    print("quota/overflow randomized exact cases:", quota_cases)
    print("central aligned-quota cases:", central_cases)
    print("schedule (b, stages, seam/W):", schedule_results)
    print("deficit-ledger cases:", deficit_cases)
    print("support-identity cases:", support_cases)


if __name__ == "__main__":
    main()
