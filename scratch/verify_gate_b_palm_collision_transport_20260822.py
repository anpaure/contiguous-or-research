#!/usr/bin/env python3
"""Exact rational checks for the Gate-B Palm collision identities."""

from fractions import Fraction as Q
from itertools import combinations
from math import exp, log


def counts(catalogue, n):
    out = [0] * n
    for row in catalogue:
        for t in row:
            out[t] += 1
    return out


def dot(p, f):
    return sum((p[i] * f[i] for i in range(len(p))), Q(0))


def check_transition(current, nxt, n, unhit, unhit_next):
    assert set(nxt).issubset(set(current))
    b = len(current[0])
    assert all(len(row) == b and len(set(row)) == b for row in current)
    assert all(len(row) == b and len(set(row)) == b for row in nxt)

    z, zp = len(current), len(nxt)
    x, xp = counts(current, n), counts(nxt, n)
    assert sum(x) == b * z and sum(xp) == b * zp
    assert all(v > 0 for v in x)

    pi = [Q(v, b * z) for v in x]
    pip = [Q(v, b * zp) for v in xp]
    d = Q(z - zp, z)
    dt = [Q(x[i] - xp[i], x[i]) for i in range(n)]
    zeta = [(d - dt[i]) / (1 - d) for i in range(n)]

    # Replicator and linear conservation.
    assert all(pip[i] == pi[i] * (1 + zeta[i]) for i in range(n))
    assert dot(pi, zeta) == 0

    # Collision, empirical-variance, and pair-count forms.
    k = n * sum((v * v for v in pi), Q(0))
    kp = n * sum((v * v for v in pip), Q(0))
    xbar = Q(b * z, n)
    empirical = 1 + Q(1, n) * sum(
        (((Q(v) - xbar) / xbar) ** 2 for v in x), Q(0)
    )
    assert k == empirical

    pair_sum = 0
    for f in current:
        for g in current:
            pair_sum += len(set(f).intersection(g))
    assert k == Q(n * pair_sum, b * b * z * z)

    # Escort recursion and covariance form.
    sq = sum((v * v for v in pi), Q(0))
    rho = [v * v / sq for v in pi]
    ratio = dot(rho, [(1 + v) ** 2 for v in zeta])
    assert kp / k == ratio
    escort_mean = dot(rho, zeta)
    escort_energy = 2 * max(Q(0), escort_mean) + dot(
        rho, [v * v for v in zeta]
    )
    assert log(float(kp / k)) <= float(escort_energy) + 1e-14

    likelihood = [n * v for v in pi]
    cov = dot(pi, [likelihood[i] * zeta[i] for i in range(n)])
    quad = dot(pi, [likelihood[i] * zeta[i] ** 2 for i in range(n)])
    assert kp - k == 2 * cov + quad

    # Hole-Palm transport in both exact forms.
    assert all(unhit_next[i] <= unhit[i] for i in range(n))
    hit = [unhit[i] - unhit_next[i] for i in range(n)]
    r = dot(pi, unhit)
    rp = dot(pip, unhit_next)
    rhs1 = dot(pi, [unhit_next[i] * zeta[i] for i in range(n)]) - dot(pi, hit)
    rhs2 = dot(pi, [unhit[i] * zeta[i] for i in range(n)]) - dot(
        pi, [hit[i] * (1 + zeta[i]) for i in range(n)]
    )
    assert rp - r == rhs1 == rhs2


def check_floor_bound(catalogue, n, good, k_const, x_density, a_middle):
    b = len(catalogue[0])
    z = len(catalogue)
    xcount = counts(catalogue, n)
    pi = [Q(v, b * z) for v in xcount]
    collision = n * sum((v * v for v in pi), Q(0))
    floor = Q(1, k_const) / (x_density * a_middle)
    assert all(pi[t] >= floor for t in good)
    bound = Q(n * len(good), 1) / (k_const * k_const * x_density**2 * a_middle**2)
    assert collision >= bound


def check_hole_palm_decomposition(catalogue, n, holes):
    b = len(catalogue[0])
    z = len(catalogue)
    xcount = counts(catalogue, n)
    pi = [Q(v, b * z) for v in xcount]
    hole_set = set(holes)
    a = Q(len(hole_set), n)
    r_mass = sum((pi[t] for t in hole_set), Q(0))
    collision = n * sum((v * v for v in pi), Q(0))
    kh = len(hole_set) * sum(
        ((pi[t] / r_mass) ** 2 for t in hole_set), Q(0)
    )
    outside = [t for t in range(n) if t not in hole_set]
    kc = len(outside) * sum(
        ((pi[t] / (1 - r_mass)) ** 2 for t in outside), Q(0)
    )
    decomposition = r_mass**2 / a * kh + (1 - r_mass) ** 2 / (1 - a) * kc
    lower = 1 + (r_mass - a) ** 2 / (a * (1 - a))
    assert collision == decomposition
    assert collision >= lower


def check_deterministic_countermodel():
    # Two holes have zero marks; every other target has three.  The formulas
    # are exact for this positive-probability outcome of the empty graph.
    n, d, holes, marks = 10, 100, 2, 3
    total_marks = (n - holes) * marks
    z0, z1 = n * d, n * d - total_marks
    protection_hole = Q(z0, z1)
    assert protection_hole < Q(11, 10)

    likelihoods = []
    for t in range(n):
        x1 = d if t < holes else d - marks
        likelihoods.append(Q(x1 * z0, d * z1))
    assert sum(likelihoods, Q(0)) == n
    collision = Q(1, n) * sum((v * v for v in likelihoods), Q(0))
    assert collision < Q(101, 100)


def check_entropy_and_hit_tail():
    # A nonuniform law with a pointwise floor on a two-point good set.
    pi = [Q(3, 10), Q(1, 4), Q(1, 5), Q(3, 20), Q(1, 10)]
    n = len(pi)
    good = (0, 1)
    a = Q(len(good), n)
    mass = sum((pi[t] for t in good), Q(0))
    m0 = Q(1, 2)
    assert mass >= m0 >= a
    kl = sum(float(v) * log(float(v * n)) for v in pi)
    binary = (float(m0) * log(float(m0 / a))
              + float(1 - m0) * log(float((1 - m0) / (1 - a))))
    tangent = float(m0) * log(float(m0 / a)) - float(m0 - a)
    assert kl + 1e-14 >= binary >= tangent - 1e-14

    # Empty-conflict one-round accepted-hit tail with kappa=1.
    for xstar in range(1, 15):
        for den in range(3, 15):
            p = Q(1, den)
            u = p * xstar
            occupation = u / (1 + u)
            no_hit = float((1 - p) ** xstar)
            assert no_hit <= exp(-float(occupation)) + 1e-14


def check_late_threshold_algebra():
    for r in range(2, 40):
        b = 2 * r + 1
        for k_const in (1, 2, 5):
            for gamma in (Q(1, 7), Q(2, 3)):
                for r_factor in (1, 3, 10):
                    x = Q(1, 20)
                    xj = r_factor * x
                    m_ratio = Q(r * xj + 2, r + 2)
                    # N cancels from lambda*threshold exactly.
                    product = gamma * b * m_ratio / (2 * k_const * r * r * x)
                    a_r = gamma * r_factor / (2 * k_const * r)
                    assert product >= a_r


def main():
    # A nonuniform deletion from a small two-window catalogue.
    catalogue = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0),
        (0, 2),
        (1, 3),
        (2, 4),
        (3, 0),
        (4, 1),
    ]
    nxt = [catalogue[i] for i in (1, 2, 4, 5, 7, 9)]
    check_transition(catalogue, nxt, 5, [1, 1, 1, 1, 1], [1, 0, 1, 1, 0])

    # A target star may become empty while the catalogue remains nonempty.
    extinct = [catalogue[i] for i in (0, 1, 2)]
    check_transition(catalogue, extinct, 5, [1] * 5, [1, 1, 1, 0, 0])

    # Exhaust several additional nested subcatalogues and hit patterns.
    for keep in combinations(range(len(catalogue)), 7):
        sub = [catalogue[i] for i in keep]
        if all(counts(sub, 5)):
            check_transition(catalogue, sub, 5, [1] * 5, [1, 1, 0, 1, 0])

    # A direct finite check of the floor-to-collision inequality.
    check_floor_bound(
        [(0,), (0,), (0,), (1,), (1,), (2,), (3,)],
        n=4,
        good=[0],
        k_const=2,
        x_density=Q(1, 2),
        a_middle=Q(7, 2),
    )
    check_hole_palm_decomposition(
        [(0,), (0,), (0,), (1,), (1,), (2,), (3,)], 4, [0, 2]
    )
    check_deterministic_countermodel()
    check_entropy_and_hit_tail()
    check_late_threshold_algebra()
    print("PASS: exact Palm collision, escort, transport, and countermodel checks")


if __name__ == "__main__":
    main()
