#!/usr/bin/env python3
"""Exact finite audits for the Gate-B cross-depth association reduction."""

from fractions import Fraction as F
from itertools import permutations, product
from random import Random


def mean(values):
    return sum(values, F(0)) / len(values)


def moments(catalogue, holes_by_depth, two_b):
    """Audit (1.7) and (2.3) for a tagged finite incidence catalogue."""
    z = len(catalogue)
    all_holes = [t for layer in holes_by_depth for t in layer]
    assert len(all_holes) == len(set(all_holes))
    depth_scores = [
        [F(sum(t in row for t in layer), two_b) for row in catalogue]
        for layer in holes_by_depth
    ]
    scores = [
        sum((depth_scores[q][f] for q in range(len(depth_scores))), F(0))
        for f in range(z)
    ]
    mu = mean(scores)
    second = mean([x * x for x in scores])
    p = {t: F(sum(t in row for row in catalogue), z) for t in all_holes}
    p2 = {
        (t, u): F(sum(t in row and u in row for row in catalogue), z)
        for t in all_holes
        for u in all_holes
    }
    assert mu == sum(p.values(), F(0)) / two_b
    assert second == sum(p2.values(), F(0)) / (two_b * two_b)
    if mu:
        omega = {t: p[t] / (two_b * mu) for t in all_holes}
        assert sum(omega.values(), F(0)) == 1
        association = sum(
            (
                omega[t] * omega[u] * p2[t, u] / (p[t] * p[u])
                if p[t] and p[u]
                else F(0)
            )
            for t, u in product(all_holes, repeat=2)
        )
        assert association == second / (mu * mu)
    return {
        "mu": mu,
        "second": second,
        "p": p,
        "p2": p2,
        "depth_scores": depth_scores,
    }


def covariance_constants(depth_scores, xi, c1, c2):
    """Audit the exact covariance decomposition and constants (2.5)--(2.7)."""
    q_count = len(depth_scores)
    z = len(depth_scores[0])
    assert all(len(layer) == z for layer in depth_scores)
    depth_means = [mean(layer) for layer in depth_scores]
    phi = [sum((depth_scores[q][f] for q in range(q_count)), F(0))
           for f in range(z)]
    mu = mean(phi)
    second = mean([x * x for x in phi])
    cross_covariance = sum(
        mean([depth_scores[q][f] * depth_scores[d][f] for f in range(z)])
        - depth_means[q] * depth_means[d]
        for q in range(q_count)
        for d in range(q_count)
        if q != d
    )
    rhs_exact = (
        second
        - sum((mean([x * x for x in layer]) for layer in depth_scores), F(0))
        - (mu * mu - sum((x * x for x in depth_means), F(0)))
    )
    assert cross_covariance == rhs_exact
    assert mu <= c1 * xi * q_count
    assert second >= c2 * xi * q_count * q_count
    lower = (
        c2 * xi * q_count * q_count
        - c1 * xi * q_count
        - c1 * c1 * xi * xi * q_count * q_count
    )
    assert cross_covariance >= lower
    if q_count >= 4 * c1 / c2 and xi <= c2 / (4 * c1 * c1):
        assert cross_covariance >= c2 * xi * q_count * q_count / 2


def labelled_telescope(states, targets):
    """Audit (3.9)--(3.14), retaining labels on duplicate physical rows."""

    def probabilities(state):
        z = len(state)
        p = {
            t: F(sum(t in payload for _, payload in state), z)
            for t in targets
        }
        p2 = {
            (t, u): F(
                sum(t in payload and u in payload for _, payload in state), z
            )
            for t in targets
            for u in targets
        }
        return p, p2

    p0, p20 = probabilities(states[0])
    pt, p2t = probabilities(states[-1])

    # First-blocker equations only use that the labelled cells partition the
    # deleted records.  Use a deterministic synthetic partition in each round.
    for before, after in zip(states, states[1:]):
        after_labels = {label for label, _ in after}
        deleted = [record for record in before if record[0] not in after_labels]
        cells = [[record for record in deleted if record[0] % 3 == residue]
                 for residue in range(3)]
        assert sum(map(len, cells)) == len(deleted)
        for t, u in product(targets, repeat=2):
            lhs_t = sum(
                sum(t in payload for _, payload in cell) for cell in cells
            )
            lhs_tu = sum(
                sum(t in payload and u in payload for _, payload in cell)
                for cell in cells
            )
            assert lhs_t == sum(t in payload for _, payload in deleted)
            assert lhs_tu == sum(
                t in payload and u in payload for _, payload in deleted
            )

    for t, u in product(targets, repeat=2):
        if not p2t[t, u]:
            continue
        marginal_t = F(1)
        marginal_u = F(1)
        joint = F(1)
        association = F(1)
        for before, after in zip(states, states[1:]):
            after_labels = {label for label, _ in after}
            deleted = [record for record in before if record[0] not in after_labels]
            d = F(len(deleted), len(before))
            xt = sum(t in payload for _, payload in before)
            xu = sum(u in payload for _, payload in before)
            xtu = sum(t in payload and u in payload for _, payload in before)
            dt = F(sum(t in payload for _, payload in deleted), xt)
            du = F(sum(u in payload for _, payload in deleted), xu)
            dtu = F(
                sum(t in payload and u in payload for _, payload in deleted), xtu
            )
            marginal_t *= (1 - dt) / (1 - d)
            marginal_u *= (1 - du) / (1 - d)
            joint *= (1 - dtu) / (1 - d)
            association *= ((1 - dtu) * (1 - d)) / ((1 - dt) * (1 - du))
        assert pt[t] == p0[t] * marginal_t
        assert pt[u] == p0[u] * marginal_u
        assert p2t[t, u] == p20[t, u] * joint
        assert p2t[t, u] / (pt[t] * pt[u]) == (
            p20[t, u] / (p0[t] * p0[u]) * association
        )


def protection_bound():
    """Exact rational replay of the constants in (1.9) and (3.17)."""
    b = 5
    a_size = 100
    b_q = 60
    q_count = 4
    xi = F(1, 10)
    c1 = F(1)
    r_cap = F(2)
    hole_count = xi * a_size * q_count
    assert hole_count.denominator == 1
    probabilities = [F(1, 10)] * int(hole_count)
    mu = sum(probabilities, F(0)) / (2 * b)
    average = mean(probabilities)
    assert mu <= c1 * xi * q_count
    assert max(probabilities) <= r_cap * average
    assert average == 2 * b * mu / (xi * a_size * q_count)
    assert max(probabilities) <= 2 * r_cap * c1 * b / a_size
    initial = F(b, b_q)
    assert b_q <= a_size
    for p_t in probabilities:
        # This is exp(P_tau(T)); taking logs preserves the inequality.
        assert p_t / initial <= 2 * r_cap * c1


def scrambling_scope(depth_matrices, two_b):
    """Exhaustively audit (4.2) and every claimed fixed-depth invariant."""
    q_count = len(depth_matrices)
    z = len(depth_matrices[0])
    assert all(len(matrix) == z for matrix in depth_matrices)
    perms = list(permutations(range(z)))

    def invariants(matrix):
        target_count = len(matrix[0])
        degrees = tuple(sum(matrix[f][t] for f in range(z))
                        for t in range(target_count))
        codegrees = tuple(
            sum(matrix[f][t] and matrix[f][u] for f in range(z))
            for t in range(target_count)
            for u in range(target_count)
        )
        row_scores = tuple(sorted(F(sum(row), two_b) for row in matrix))
        return degrees, codegrees, row_scores

    base_invariants = [invariants(matrix) for matrix in depth_matrices]
    depth_scores = [
        [F(sum(row), two_b) for row in matrix] for matrix in depth_matrices
    ]
    total = F(0)
    count = 0
    realized_seconds = set()
    for choices in product(perms, repeat=q_count):
        permuted = [
            [depth_matrices[q][choices[q][f]] for f in range(z)]
            for q in range(q_count)
        ]
        assert [invariants(matrix) for matrix in permuted] == base_invariants
        value = mean([
            sum((F(sum(permuted[q][f]), two_b) for q in range(q_count)), F(0))
            ** 2
            for f in range(z)
        ])
        total += value
        count += 1
        realized_seconds.add(value)

    lhs = total / count
    means = [mean(layer) for layer in depth_scores]
    rhs = sum((mean([x * x for x in layer]) for layer in depth_scores), F(0))
    rhs += sum(
        means[q] * means[d]
        for q in range(q_count)
        for d in range(q_count)
        if q != d
    )
    mu = sum(means, F(0))
    assert lhs == rhs
    assert lhs <= mu + mu * mu
    assert min(realized_seconds) <= lhs
    assert len(realized_seconds) > 1


def four_root_gate_and_counterexample():
    """Audit Theorem 6.1 and the affine scrambling counterexample."""
    prime = 17
    q_count = 8
    records = [(a, c) for a in range(prime) for c in range(prime)]
    aligned = [
        [F(int(a == 0)) for a, _ in records] for _ in range(q_count)
    ]
    scrambled = [
        [F(int((a + q * c) % prime == 0)) for a, c in records]
        for q in range(q_count)
    ]

    def second_and_cross(layers):
        phi = [sum((layers[q][f] for q in range(q_count)), F(0))
               for f in range(len(records))]
        second = mean([x * x for x in phi])
        diagonal = sum((mean([x * x for x in layer]) for layer in layers), F(0))
        cross = sum(
            mean([layers[q][f] * layers[d][f] for f in range(len(records))])
            for q in range(q_count)
            for d in range(q_count)
            if q != d
        )
        assert second == diagonal + cross
        return second, cross

    xi = F(1, prime)
    aligned_second, aligned_cross = second_and_cross(aligned)
    scrambled_second, scrambled_cross = second_and_cross(scrambled)
    assert aligned_second == xi * q_count * q_count
    assert aligned_cross == xi * q_count * (q_count - 1)
    assert scrambled_second == (
        xi * q_count + xi * xi * q_count * (q_count - 1)
    )
    assert scrambled_cross == xi * xi * q_count * (q_count - 1)
    assert all(sorted(aligned[q]) == sorted(scrambled[q]) for q in range(q_count))

    # Cross-depth product-Palm association is 1/xi when aligned and 1 when
    # pairwise independent.
    product_mass = xi * xi * q_count * (q_count - 1)
    assert aligned_cross / product_mass == 1 / xi
    assert scrambled_cross / product_mass == 1

    # Scalar moment => cross moment with the factor-two constants of (6.3).
    c1 = F(1)
    c2 = F(1)
    mu = xi * q_count
    assert mu <= c1 * xi * q_count
    assert aligned_second >= c2 * xi * q_count * q_count
    assert q_count >= 2 * c1 / c2
    assert aligned_cross >= c2 * xi * q_count * q_count / 2
    # Cross moment => scalar moment is the nonnegative-diagonal implication.
    assert aligned_second >= aligned_cross


def main():
    rng = Random(20260822)
    targets = [(q, t) for q in range(3) for t in range(3)]
    payloads = [
        frozenset(t for t in targets if rng.randrange(2)) for _ in range(12)
    ]
    payloads[0] = frozenset(targets)
    payloads[1] = payloads[0]  # duplicate physical row, distinct label
    payloads[11] = payloads[0]  # one duplicate is deleted while one survives
    labelled_rows = list(enumerate(payloads))
    states = [labelled_rows, labelled_rows[:-2], labelled_rows[:-4], labelled_rows[:-6]]
    holes = [targets[:3], targets[3:6], targets[6:]]

    moments([payload for _, payload in states[-1]], holes, two_b=6)
    # Positive marginal Palm mass with an empty joint star audits the zero
    # extension in (3.15a)--(3.15).
    moments(
        [frozenset({("left", 0)}), frozenset({("right", 0)})],
        [[("left", 0)], [("right", 0)]],
        two_b=2,
    )
    labelled_telescope(states, targets)

    # Select a new family only after the terminal state is known, then replay
    # the pathwise identities.  This is the finite quantifier audit in section 5.
    terminal = states[-1]
    future_selected = sorted(
        targets,
        key=lambda t: sum(t in payload for _, payload in terminal),
        reverse=True,
    )[:6]
    future_holes = [future_selected[:2], future_selected[2:4], future_selected[4:]]
    moments([payload for _, payload in terminal], future_holes, two_b=6)
    labelled_telescope(states, future_selected)

    aligned_scores = [[F(int(f < 8)) for f in range(64)] for _ in range(16)]
    covariance_constants(aligned_scores, xi=F(1, 8), c1=F(1), c2=F(1))
    protection_bound()
    scrambling_scope(
        [
            [[0, 0], [1, 0], [1, 1]],
            [[1, 1], [0, 0], [1, 0]],
            [[1, 0], [1, 1], [0, 0]],
        ],
        two_b=2,
    )
    four_root_gate_and_counterexample()
    print("gate-B cross-depth association audits: PASS")


if __name__ == "__main__":
    main()
