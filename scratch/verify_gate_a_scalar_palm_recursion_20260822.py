#!/usr/bin/env python3
"""Regression checks for the exact scalar-Palm recursion note.

The mathematical proof is in
MATH_AUDIT_GATE_A_SCALAR_PALM_ONE_STEP_RECURSION_20260822.md.
This script checks the discrete monotonicity algebra and independently
enumerates the component counts used in Proposition 5.1.
"""

from fractions import Fraction
from itertools import combinations
from math import prod


def falling(d: int, k: int = 12) -> int:
    return prod(range(d - k + 1, d + 1)) if d >= k else 0


def phi(d: int, c: Fraction) -> Fraction:
    if d < 12 or d <= c:
        return Fraction(0)
    return Fraction((d - c) ** 12, falling(d))


test_cs = {Fraction(c) for c in range(11, 80)}
test_cs.update(Fraction(11) + Fraction(a, 17) for a in range(1, 17))
test_cs.update(Fraction(12) + Fraction(a, 19) for a in range(1, 19))
for c in sorted(test_cs):
    vals = [phi(d, c) for d in range(0, 500)]
    assert all(x <= y for x, y in zip(vals, vals[1:]))


def scalar_recursion(weights, current_phi, outcomes):
    """Check (2.5)--(2.6) on a finite carrier-labelled subkernel.

    outcomes[s] consists of pairs (submass, terminal_phi_vector), where a
    terminal entry is None exactly when that current carrier was killed.
    """
    nu_t = sum(weights[s] * len(current_phi[s]) for s in range(len(weights)))
    current_f = sum(
        weights[s] * sum(current_phi[s]) for s in range(len(weights))
    )
    current_a = current_f / nu_t

    palm_ea = Fraction(0)
    palm_eaphi = Fraction(0)
    palm_ee = Fraction(0)
    terminal_t = Fraction(0)
    terminal_f = Fraction(0)
    total_output_mass = Fraction(0)
    for s, weight in enumerate(weights):
        total_output_mass += weight * sum(mass for mass, _ in outcomes[s])
        for i, old_phi in enumerate(current_phi[s]):
            survival = Fraction(0)
            erosion = Fraction(0)
            for mass, terminal in outcomes[s]:
                if terminal[i] is not None:
                    survival += mass
                    erosion += mass * (old_phi - terminal[i])
                    terminal_t += weight * mass
                    terminal_f += weight * mass * terminal[i]
            palm_weight = weight / nu_t
            palm_ea += palm_weight * survival
            palm_eaphi += palm_weight * survival * old_phi
            palm_ee += palm_weight * erosion

    terminal_a = terminal_f / terminal_t
    rhs_25 = (palm_eaphi - palm_ee) / palm_ea
    covariance = palm_eaphi - palm_ea * current_a
    rhs_26 = (covariance - palm_ee) / palm_ea
    assert terminal_a == rhs_25
    assert terminal_a - current_a == rhs_26

    # A single global normalization of the exact-size submeasure cancels.
    assert terminal_a == (
        (terminal_f / total_output_mass) / (terminal_t / total_output_mass)
    )
    return current_a, terminal_a, rhs_26


weights_actual = [Fraction(2), Fraction(3)]
phi_actual = [
    [Fraction(1, 10), Fraction(1, 5)],
    [Fraction(1, 4), Fraction(1, 3), Fraction(2, 5)],
]
outcomes_actual = [
    [
        (Fraction(1, 7), [Fraction(1, 20), None]),
        (Fraction(2, 9), [Fraction(1, 12), Fraction(1, 6)]),
    ],
    [
        (Fraction(1, 8), [None, Fraction(1, 4), Fraction(3, 10)]),
        (Fraction(1, 11), [Fraction(1, 5), None, Fraction(1, 5)]),
    ],
]
a_before, a_after, delta = scalar_recursion(
    weights_actual, phi_actual, outcomes_actual
)

weights_reference = [Fraction(1), Fraction(1)]
phi_reference = [
    [Fraction(1, 12), Fraction(1, 6)],
    [Fraction(1, 5), Fraction(3, 10)],
]
outcomes_reference = [
    [
        (Fraction(1, 4), [Fraction(1, 24), None]),
        (Fraction(1, 4), [Fraction(1, 16), Fraction(1, 8)]),
    ],
    [
        (Fraction(1, 5), [None, Fraction(1, 4)]),
        (Fraction(3, 10), [Fraction(1, 6), Fraction(1, 5)]),
    ],
]
b_before, b_after, delta0 = scalar_recursion(
    weights_reference, phi_reference, outcomes_reference
)
assert (a_after / b_after) / (a_before / b_before) == (
    (1 + delta / a_before) / (1 + delta0 / b_before)
)


def all_masks(n):
    for mask in range(1 << n):
        yield {i for i in range(n) if mask & (1 << i)}


# Independently check the literal W formula, including all normalization
# factors, on a nontrivial five-edge conflict graph.
toy_edges = [
    frozenset((0, 1)),
    frozenset((1, 2)),
    frozenset((3, 4)),
    frozenset((4, 5)),
    frozenset((3, 5)),
]
toy_m = len(toy_edges)
toy_adj = {
    i: {j for j in range(toy_m) if j != i and toy_edges[i] & toy_edges[j]}
    for i in range(toy_m)
}
toy_p = Fraction(2, 9)


def mark_probability(marked, universe_size):
    return toy_p ** len(marked) * (1 - toy_p) ** (universe_size - len(marked))


direct_by_deleted = {}
for marked in all_masks(toy_m):
    accepted = {
        i for i in marked if not any(j in marked for j in toy_adj[i])
    }
    deleted = frozenset().union(*(toy_edges[i] for i in accepted))
    direct_by_deleted[deleted] = direct_by_deleted.get(deleted, Fraction(0)) + (
        mark_probability(marked, toy_m)
    )
assert sum(direct_by_deleted.values()) == 1


def zeta(indices):
    indices = set(indices)
    ans = Fraction(0)
    ordered = sorted(indices)
    for local_mask in all_masks(len(ordered)):
        marked = {ordered[i] for i in local_mask}
        has_isolated = any(
            not any(j in marked for j in toy_adj[i]) for i in marked
        )
        if not has_isolated:
            ans += mark_probability(marked, len(ordered))
    return ans


w_by_deleted = {}
for accepted in all_masks(toy_m):
    if any(j in accepted for i in accepted for j in toy_adj[i]):
        continue
    open_neighborhood = set().union(
        *(toy_adj[i] for i in accepted)
    ) - accepted if accepted else set()
    closed_neighborhood = accepted | open_neighborhood
    remainder = set(range(toy_m)) - closed_neighborhood
    deleted = frozenset().union(*(toy_edges[i] for i in accepted))
    term = (
        toy_p ** len(accepted)
        * (1 - toy_p) ** len(open_neighborhood)
        * zeta(remainder)
    )
    w_by_deleted[deleted] = w_by_deleted.get(deleted, Fraction(0)) + term
assert w_by_deleted == direct_by_deleted
assert sum(
    mass for deleted, mass in w_by_deleted.items() if len(deleted) == 2
) == sum(
    mass for deleted, mass in direct_by_deleted.items() if len(deleted) == 2
)


def complete_graph(n: int):
    return set(combinations(range(n), 2))


def complete_bipartite(a: int, b: int):
    return {(i, a + j) for i in range(a) for j in range(b)}


k14 = complete_graph(14)
k1212 = complete_bipartite(12, 12)
assert len(k14) == 91
assert len(k1212) == 144
assert {sum(v in e for e in k14) for v in range(14)} == {13}
assert {sum(v in e for e in k1212) for v in range(24)} == {12}

for e in k14:
    rem = {f for f in k14 if not set(e) & set(f)}
    surviving_vertices = set(range(14)) - set(e)
    assert {sum(v in f for f in rem) for v in surviving_vertices} == {11}

for e in k1212:
    rem = {f for f in k1212 if not set(e) & set(f)}
    surviving_vertices = set(range(24)) - set(e)
    assert {sum(v in f for f in rem) for v in surviving_vertices} == {11}

# Every rooted twelve-carrier in K14 uses thirteen vertices, and the unique
# carrier edge-set at a K12,12 root uses the root and the whole opposite
# part.  Therefore no deletion edge in its own component can preserve it,
# while a deletion in every other component preserves it unchanged.
for v in range(14):
    star = [e for e in k14 if v in e]
    assert len(star) == 13
    for carrier in combinations(star, 12):
        carrier_vertices = set().union(*(set(e) for e in carrier))
        assert len(carrier_vertices) == 13
        assert all(carrier_vertices & set(e) for e in k14)

for v in range(24):
    carrier = [e for e in k1212 if v in e]
    assert len(carrier) == 12
    carrier_vertices = set().union(*(set(e) for e in carrier))
    assert len(carrier_vertices) == 13
    assert all(carrier_vertices & set(e) for e in k1212)

# Leading small-p singleton masses Q_H:Q_L = 91:144. Check the exact
# cross-multiplied Palm inequality for several component counts.
t_h = 14 * falling(13)
t_l = 24 * falling(12)
q_h = Fraction(91)
q_l = Fraction(144)
for m in range(1, 20):
    before = Fraction(14, t_h + m * t_l)
    after = Fraction(
        14 * m * q_l,
        m * q_l * (t_h + (m - 1) * t_l) + q_h * m * t_l,
    )
    assert after > before
    assert (after > before) == (q_l > q_h)
    a_h = m * q_l
    a_l = q_h + (m - 1) * q_l
    assert a_h - a_l == q_l - q_h > 0

for m in range(1, 8):
    before = Fraction(14, t_h + m * t_l)
    for q_h_test, q_l_test in [
        (Fraction(3, 10), Fraction(7, 20)),
        (Fraction(7, 20), Fraction(3, 10)),
        (Fraction(2, 9), Fraction(2, 9)),
    ]:
        after = Fraction(
            14 * m * q_l_test,
            m * q_l_test * (t_h + (m - 1) * t_l)
            + q_h_test * m * t_l,
        )
        assert (after > before) == (q_l_test > q_h_test)
        assert (after == before) == (q_l_test == q_h_test)

print(
    "GATE_A_SCALAR_PALM_RECURSION_PASS",
    f"phi_grid={len(test_cs)}x500",
    "literal_W_states=32",
    "finite_recursions=2",
    "relative_recursion=1",
    "K14_edges=91",
    "K12,12_edges=144",
    "component_counts=1..19",
)
