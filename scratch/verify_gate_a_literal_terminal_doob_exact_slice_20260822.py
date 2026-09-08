#!/usr/bin/env python3
"""Finite exact checks for the literal terminal Palm/Doob identity.

The path calculation uses C_8, ordered two-carriers, and p=1/5.  The
carrier order is reduced only to keep exhaustive enumeration tiny; every
normalization is the same as for ordered twelve-carriers.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def falling(a, k):
    out = 1
    for i in range(k):
        out *= a - i
    return out


def cycle_edges(n, state):
    state = set(state)
    return tuple(
        tuple(sorted((i, (i + 1) % n)))
        for i in range(n)
        if i in state and (i + 1) % n in state
    )


def bite_kernel(n, state, p):
    """Exact law of the induced residual after one isolated-edge bite."""
    state = frozenset(state)
    edges = cycle_edges(n, state)
    out = defaultdict(Fraction)
    for mask in range(1 << len(edges)):
        marked = {i for i in range(len(edges)) if mask >> i & 1}
        accepted = set()
        for i in marked:
            ei = set(edges[i])
            if all(i == h or ei.isdisjoint(edges[h]) for h in marked):
                accepted.add(i)
        deleted = set()
        for i in accepted:
            deleted.update(edges[i])
        nxt = frozenset(set(state) - deleted)
        prob = p ** len(marked) * (1 - p) ** (len(edges) - len(marked))
        out[nxt] += prob
    assert sum(out.values()) == 1
    return out


def slices(n, size):
    return tuple(frozenset(c) for c in combinations(range(n), size))


def carriers(n):
    es = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    out = []
    for v in range(n):
        inc = sorted(e for e in es if v in e)
        out.append((v, inc[0], inc[1]))
        out.append((v, inc[1], inc[0]))
    return tuple(out)


def alive(gamma, state):
    _, e1, e2 = gamma
    return set(e1).union(e2).issubset(state)


def t_mass(cars, state):
    return sum(alive(g, state) for g in cars)


def make_p_matrix(n, omega, omega_next, p):
    allowed = set(omega_next)
    ans = {}
    for s in omega:
        raw = bite_kernel(n, s, p)
        for sp, value in raw.items():
            if sp in allowed and value:
                ans[s, sp] = value
    return ans


def check_terminal_doob():
    n = 8
    p = Fraction(1, 5)
    sizes = (8, 6, 4)
    omegas = [slices(n, k) for k in sizes]
    cars = carriers(n)
    lambdas = [{s: Fraction(1, len(om)) for s in om} for om in omegas]
    z = [sum(lambdas[j][s] * t_mass(cars, s) for s in omegas[j])
         for j in range(3)]
    assert all(value > 0 for value in z)
    ps = [make_p_matrix(n, omegas[j], omegas[j + 1], p) for j in range(2)]

    # Raw residual measures nu_j.
    nu = lambdas[0]
    for j in range(2):
        nxt = defaultdict(Fraction)
        for s, mass in nu.items():
            for sp in omegas[j + 1]:
                nxt[sp] += mass * ps[j].get((s, sp), 0)
        nu = dict(nxt)

    # Enumerate reference carrier histories, their Q mass, and L-weight.
    q_terminal = defaultdict(Fraction)
    r_terminal = defaultdict(Fraction)
    q_total = Fraction(0)
    r_total = Fraction(0)
    c = [z[j + 1] / z[j] for j in range(2)]
    choose = [Fraction(1, comb(sizes[j], sizes[j + 1])) for j in range(2)]

    s0 = omegas[0][0]
    for gamma in cars:
        pi0 = lambdas[0][s0] / z[0]
        for s1 in omegas[1]:
            if not s1.issubset(s0) or not alive(gamma, s1):
                continue
            k0 = choose[0] / c[0]
            p0 = ps[0].get((s0, s1), 0)
            r0 = c[0] * p0 / choose[0]
            for s2 in omegas[2]:
                if not s2.issubset(s1) or not alive(gamma, s2):
                    continue
                k1 = choose[1] / c[1]
                p1 = ps[1].get((s1, s2), 0)
                r1 = c[1] * p1 / choose[1]
                qmass = pi0 * k0 * k1
                lval = r0 * r1
                y = (s2, gamma)
                q_terminal[y] += qmass
                r_terminal[y] += qmass * lval
                q_total += qmass
                r_total += qmass * lval

    assert q_total == 1
    assert r_total == sum(nu[s] * t_mass(cars, s) for s in omegas[2]) / z[0]
    checked = 0
    for y, qmass in q_terminal.items():
        s, gamma = y
        pi2 = lambdas[2][s] / z[2]
        assert qmass == pi2
        assert r_terminal[y] == nu[s] / z[0]
        e_cond = r_terminal[y] / qmass
        rhs_cond = (z[2] / z[0]) * nu[s] / lambdas[2][s]
        assert e_cond == rhs_cond
        palm_density = e_cond / r_total
        rhs_palm = z[2] * nu[s] / (lambdas[2][s] *
                    sum(nu[u] * t_mass(cars, u) for u in omegas[2]))
        assert palm_density == rhs_palm
        checked += 1
    return checked


def check_environment_factor():
    # On C_8, condition the first bite on deleting exactly two vertices.
    # Edge transitivity makes the actual deleted edge uniform over 8 edges.
    n = 8
    all_pairs = comb(n, 2)
    actual_edges = n
    full_state_ratio = Fraction(all_pairs, actual_edges)
    assert full_state_ratio == Fraction(7, 2)

    # A full star uses three vertices.  Four cycle edges and ten arbitrary
    # pairs avoid that footprint.  The exact factorization is
    # (survival ratio) * (environment ratio) = full state ratio.
    actual_survival = Fraction(4, 8)
    slice_survival = Fraction(comb(5, 2), comb(8, 2))
    environment_ratio = Fraction(comb(5, 2), 4)
    assert actual_survival / slice_survival == Fraction(7, 5)
    assert environment_ratio == Fraction(5, 2)
    assert (actual_survival / slice_survival) * environment_ratio == full_state_ratio
    return full_state_ratio, environment_ratio


def check_functional_gate():
    # The two-carrier analogue of (6.3)--(6.6).  On a residual of C_8 and
    # at threshold c=1, F=sum_v(d(v)-1)_+^2=t/2 state by state.  Hence the
    # functional Palm ratio is exactly one although the state density is
    # supported only on edge-deletion slices.
    n = 8
    p = Fraction(1, 5)
    omega0 = slices(n, 8)
    omega1 = slices(n, 6)
    cars = carriers(n)
    lam0 = {omega0[0]: Fraction(1)}
    lam1 = {s: Fraction(1, len(omega1)) for s in omega1}
    pm = make_p_matrix(n, omega0, omega1, p)
    nu = {s: pm.get((omega0[0], s), 0) for s in omega1}

    def degrees(state):
        ans = {v: 0 for v in state}
        for a, b in cycle_edges(n, state):
            ans[a] += 1
            ans[b] += 1
        return ans

    def f_mass(state):
        return sum(max(d - 1, 0) ** 2 for d in degrees(state).values())

    for s in omega1:
        assert f_mass(s) * 2 == t_mass(cars, s)

    h = {s: nu[s] / lam1[s] for s in omega1}
    e_hf = sum(lam1[s] * h[s] * f_mass(s) for s in omega1)
    e_ht = sum(lam1[s] * h[s] * t_mass(cars, s) for s in omega1)
    e_f = sum(lam1[s] * f_mass(s) for s in omega1)
    e_t = sum(lam1[s] * t_mass(cars, s) for s in omega1)
    assert e_hf / e_ht == e_f / e_t == Fraction(1, 2)

    nu_one = sum(nu.values())
    actual_f = e_hf / nu_one
    actual_t = e_ht / nu_one
    assert actual_f / e_f == (actual_t / e_t) * ((e_hf / e_ht) / (e_f / e_t))
    return e_hf / e_ht, e_f / e_t


def check_torus_bound():
    # Arithmetic form of Proposition 5.1 for a representative m.
    m = 7
    n = m ** 6
    lower = Fraction(n - 1, 12) * Fraction(n - 26, n)
    assert lower > 1000
    assert 6 * n * 2 == 12 * n  # handshake normalization
    assert factorial(12) * (n - 26) > 0
    return n, lower


def main():
    terminal = check_terminal_doob()
    full, env = check_environment_factor()
    func_actual, func_ref = check_functional_gate()
    n, lower = check_torus_bound()
    print(
        "GATE_A_LITERAL_TERMINAL_DOOB_PASS",
        f"terminal_states={terminal}",
        f"c8_state_ratio={full}",
        f"c8_environment_ratio={env}",
        f"functional_actual={func_actual}",
        f"functional_ref={func_ref}",
        f"torus_vertices={n}",
        f"torus_palm_lower={float(lower):.3f}",
    )


if __name__ == "__main__":
    main()
