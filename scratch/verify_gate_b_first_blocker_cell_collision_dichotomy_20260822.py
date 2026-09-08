#!/usr/bin/env python3
"""Finite audit for the exact Gate-B first-blocker-cell factorization."""

from __future__ import annotations

import math
import random


def statistics(rows: list[frozenset[int]], n_targets: int):
    z = len(rows)
    assert z > 0
    b = len(rows[0])
    assert all(len(row) == b for row in rows)
    x = [0] * n_targets
    for row in rows:
        for target in row:
            x[target] += 1
    s = sum(value * value for value in x)
    k = n_targets * s / (b * b * z * z)
    return z, b, x, s, k


def one_cell(rows: list[frozenset[int]], deleted: set[int], n_targets: int):
    z, b, x, s, k = statistics(rows, n_targets)
    kept = [row for i, row in enumerate(rows) if i not in deleted]
    zp, bp, xp, sp, kp = statistics(kept, n_targets)
    assert b == bp
    y = [x[t] - xp[t] for t in range(n_targets)]
    m = len(deleted)
    rb = sum(x[t] * y[t] for t in range(n_targets))
    qb = sum(value * value for value in y)
    u, omega, chi = m / z, rb / s, qb / s
    rhs = 1 + (chi + 2 * (u - omega) - u * u) / ((1 - u) ** 2)
    assert math.isclose(kp / k, rhs, rel_tol=1e-12, abs_tol=1e-12)
    sign_lhs = kp / k - 1
    sign_rhs = chi + 2 * (u - omega) - u * u
    assert math.isclose(sign_lhs, sign_rhs / ((1 - u) ** 2),
                        rel_tol=1e-12, abs_tol=1e-12)
    if abs(sign_rhs) > 1e-11:
        assert (sign_lhs > 0) == (sign_rhs > 0)

    endpoint = [sum(x[t] for t in row) for row in rows]
    rb2 = sum(endpoint[i] for i in deleted)
    qb2 = sum(
        len(rows[i] & rows[j])
        for i in deleted
        for j in deleted
    )
    assert rb == rb2
    assert qb == qb2
    avg_cell = rb / m
    avg_all = s / z
    assert math.isclose(
        u - omega,
        u * (1 - avg_cell / avg_all),
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
    pi = [value / (b * z) for value in x]
    rho = [value * value / s for value in x]
    loss = [y[t] / x[t] if x[t] else 0.0 for t in range(n_targets)]
    assert math.isclose(sum(pi[t] * loss[t] for t in range(n_targets)), u,
                        rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(sum(rho[t] * loss[t] for t in range(n_targets)), omega,
                        rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(sum(rho[t] * loss[t] ** 2 for t in range(n_targets)), chi,
                        rel_tol=1e-12, abs_tol=1e-12)
    escort_factor = sum(
        rho[t] * ((1 - loss[t]) / (1 - u)) ** 2
        for t in range(n_targets)
    )
    assert math.isclose(escort_factor, kp / k, rel_tol=1e-12, abs_tol=1e-12)
    lval = [n_targets * value for value in pi]
    mean_l = sum(pi[t] * lval[t] for t in range(n_targets))
    mean_y = u
    cov = sum(
        pi[t] * (lval[t] - mean_l) * (loss[t] - mean_y)
        for t in range(n_targets)
    )
    assert math.isclose(omega - u, cov / k, rel_tol=1e-12, abs_tol=1e-12)


def sequence_audit(rows: list[frozenset[int]], n_targets: int, rng: random.Random):
    current = list(rows)
    k0 = statistics(current, n_targets)[4]
    cells: list[tuple[float, float, float]] = []
    product = 1.0
    while len(current) >= 3:
        max_m = max(1, min(len(current) - 1, len(current) // 4))
        m = rng.randint(1, max_m)
        deleted = set(rng.sample(range(len(current)), m))
        z, _, x, s, k = statistics(current, n_targets)
        kept = [row for i, row in enumerate(current) if i not in deleted]
        _, _, xp, _, kp = statistics(kept, n_targets)
        y = [x[t] - xp[t] for t in range(n_targets)]
        u = m / z
        omega = sum(x[t] * y[t] for t in range(n_targets)) / s
        chi = sum(value * value for value in y) / s
        factor = 1 + (chi + 2 * (u - omega) - u * u) / ((1 - u) ** 2)
        assert math.isclose(factor, kp / k, rel_tol=1e-12, abs_tol=1e-12)
        product *= factor
        cells.append((u, omega, chi))
        current = kept
        if len(cells) >= 8:
            break

    kt = statistics(current, n_targets)[4]
    assert math.isclose(product, kt / k0, rel_tol=1e-11, abs_tol=1e-11)
    eps = max(u for u, _, _ in cells)
    budget = sum(chi + 2 * max(0.0, u - omega) for u, omega, chi in cells)
    assert math.log(kt / k0) <= budget / ((1 - eps) ** 2) + 1e-12


def whole_bite_denominator_audit(
    rows: list[frozenset[int]], n_targets: int, rng: random.Random
):
    """Partition one <=1/8 deletion and verify the exact 1/8 cell cap."""
    z0 = len(rows)
    total = max(1, z0 // 8)
    chosen = rng.sample(range(z0), total)
    cut = rng.randint(0, total)
    parts = [chosen[:cut], chosen[cut:]]
    parts = [part for part in parts if part]
    current = list(enumerate(rows))
    k0 = statistics(rows, n_targets)[4]
    budget = 0.0
    for part in parts:
        labels = set(part)
        local = [i for i, (label, _) in enumerate(current) if label in labels]
        local_set = set(local)
        z, _, x, s, _ = statistics([row for _, row in current], n_targets)
        kept = [row for i, (_, row) in enumerate(current) if i not in local_set]
        _, _, xp, _, _ = statistics(kept, n_targets)
        y = [x[t] - xp[t] for t in range(n_targets)]
        u = len(local) / z
        assert u <= 1 / 8 + 1e-15
        omega = sum(x[t] * y[t] for t in range(n_targets)) / s
        chi = sum(value * value for value in y) / s
        budget += chi + 2 * max(0.0, u - omega)
        current = [entry for i, entry in enumerate(current) if i not in local_set]
    kt = statistics([row for _, row in current], n_targets)[4]
    assert math.log(kt / k0) <= (64 / 49) * budget + 1e-12


def first_blocker_graph_audit(rng: random.Random):
    """Check that ordered independent centers give literal current cells."""
    z = rng.randint(8, 30)
    adjacency = [set() for _ in range(z)]
    for i in range(z):
        for j in range(i + 1, z):
            if rng.random() < 0.18:
                adjacency[i].add(j)
                adjacency[j].add(i)
    order = list(range(z))
    rng.shuffle(order)
    accepted: list[int] = []
    for h in order:
        if all(h not in adjacency[g] for g in accepted):
            accepted.append(h)
        if len(accepted) >= 6:
            break
    assert accepted
    closed = [{h} | adjacency[h] for h in range(z)]
    deleted_union = set().union(*(closed[h] for h in accepted))
    prior: set[int] = set()
    cells: list[set[int]] = []
    for h in accepted:
        cell = closed[h] - prior
        assert h in cell
        current = set(range(z)) - prior
        current_closed = {h} | (adjacency[h] & current)
        assert cell == current_closed
        cells.append(cell)
        prior |= cell
    assert prior == deleted_union
    assert sum(map(len, cells)) == len(deleted_union)


def main():
    rng = random.Random(20260822)
    one_cell_count = 0
    sequence_count = 0
    bite_count = 0
    graph_count = 0
    for n_targets in range(4, 13):
        for b in range(1, min(5, n_targets) + 1):
            universe = [
                frozenset(rng.sample(range(n_targets), b))
                for _ in range(24)
            ]
            for _ in range(120):
                z = rng.randint(3, len(universe))
                rows = rng.sample(universe, z)
                m = rng.randint(1, z - 1)
                deleted = set(rng.sample(range(z), m))
                one_cell(rows, deleted, n_targets)
                one_cell_count += 1
            for _ in range(30):
                rows = list(universe)
                sequence_audit(rows, n_targets, rng)
                sequence_count += 1
                whole_bite_denominator_audit(rows, n_targets, rng)
                bite_count += 1
                first_blocker_graph_audit(rng)
                graph_count += 1
    print(
        "PASS Gate-B first-blocker-cell collision audit:",
        f"one-cell={one_cell_count}, sequences={sequence_count}, "
        f"bites={bite_count}, blocker-graphs={graph_count}",
    )


if __name__ == "__main__":
    main()
