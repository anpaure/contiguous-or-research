#!/usr/bin/env python3
"""Exhaustive r=2 product/slice scan for the G.168 U and Q terms."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def catalogue(r=2):
    b = 2 * r + 1
    middle = list(combinations(range(b), r))
    lower = list(combinations(range(b), r - 1))
    targets = [("M", x) for x in middle] + [("L", x) for x in lower]
    index = {t: i for i, t in enumerate(targets)}
    rows = set()
    for w in permutations(range(b)):
        row = []
        for s in range(1, b):
            row.append(index[("M", tuple(sorted(w[(s + j) % b] for j in range(r))))])
            row.append(index[("L", tuple(sorted(w[(s + j) % b] for j in range(r - 1))))])
        rows.add(tuple(sorted(row)))
    rows = sorted(rows)
    assert len(rows) == factorial(b)
    row_masks = [sum(1 << v for v in row) for row in rows]
    incidence = []
    for v in range(len(targets)):
        incidence.append(sum(1 << i for i, row in enumerate(rows) if v in row))
    conflicts = []
    for row in rows:
        mask = 0
        for v in row:
            mask |= incidence[v]
        conflicts.append(mask)
    return targets, rows, row_masks, incidence, conflicts


def state_roots(state, targets, rows, row_masks, incidence, conflicts, m=12):
    alive_mask = 0
    for i, row_mask in enumerate(row_masks):
        if row_mask & ~state == 0:
            alive_mask |= 1 << i
    Z = alive_mask.bit_count()
    if not Z:
        return []
    n_m = sum(bool(state & (1 << v)) for v, t in enumerate(targets) if t[0] == "M")
    n_l = sum(bool(state & (1 << v)) for v, t in enumerate(targets) if t[0] == "L")
    if not n_m or not n_l:
        return []
    z = {"M": Fraction(4 * Z, n_m), "L": Fraction(4 * Z, n_l)}
    degrees = [(incidence[v] & alive_mask).bit_count() for v in range(len(targets))]
    c = [(conflicts[i] & alive_mask).bit_count() for i in range(len(rows))]
    excess = [sum(degrees[v] for v in row) - c[i] for i, row in enumerate(rows)]
    roots = []
    for v, target in enumerate(targets):
        d = degrees[v]
        if d < m:
            continue
        star = incidence[v] & alive_mask
        row_ids = [i for i in range(len(rows)) if star & (1 << i)]
        rv = Fraction(
            sum(
                sum(degrees[u] - z[targets[u][0]] for u in rows[i] if u != v)
                for i in row_ids
            ),
            d,
        )
        jv = Fraction(sum(excess[i] for i in row_ids), d)
        uval = (rv - jv) / z[target[0]]
        companion_raw = Fraction(
            sum(
                sum(degrees[u] for u in rows[i] if u != v)
                for i in row_ids
            ),
            d,
        )

        dbar = Fraction(0, 1)
        for g, row in enumerate(rows):
            if not (alive_mask & (1 << g)) or v in row:
                continue
            ag = (star & conflicts[g]).bit_count()
            if not ag:
                continue
            dbar += Fraction(m * ag, d) - 1 + Fraction(falling(d - ag, m), falling(d, m))
        qval = dbar / z[target[0]]
        roots.append(
            (
                target[0], d, z[target[0]], uval, qval,
                falling(d, m), companion_raw - jv,
            )
        )
    return roots


def scan():
    targets, rows, row_masks, incidence, conflicts = catalogue()
    print("catalogue", len(targets), len(rows))
    accum = defaultdict(lambda: [0.0] * 5)
    # key=(x,a,shore): denom, U, tailden, tailU, tailQ
    xs = (0.5, 0.8, 0.95, 0.98, 0.99)
    aa = (1.001, 1.01, 1.05, 1.1, 1.25, 1.5)
    slice_accum = defaultdict(lambda: [0.0] * 5)
    n_targets = len(targets)
    for state in range(1 << n_targets):
        roots = state_roots(state, targets, rows, row_masks, incidence, conflicts)
        if not roots:
            continue
        nm = sum(bool(state & (1 << v)) for v, t in enumerate(targets) if t[0] == "M")
        nl = sum(bool(state & (1 << v)) for v, t in enumerate(targets) if t[0] == "L")
        for shore, d, z, u, q, carrier_mass, _raw in roots:
            for a in aa:
                X = d / float(z)
                psi = 0.0 if X <= a else ((X - a) / X) ** 12
                key = (nm, nl, a, shore)
                vals = slice_accum[key]
                vals[0] += carrier_mass
                vals[1] += carrier_mass * float(u)
                vals[2] += carrier_mass * psi
                vals[3] += carrier_mass * psi * float(u)
                vals[4] += carrier_mass * psi * float(q)
            for x in xs:
                y = (x + 1) / 2
                prob = x**nl * (1 - x) ** (5 - nl) * y**nm * (1 - y) ** (10 - nm)
                for a in aa:
                    X = d / float(z)
                    psi = 0.0 if X <= a else ((X - a) / X) ** 12
                    vals = accum[x, a, shore]
                    vals[0] += prob * carrier_mass
                    vals[1] += prob * carrier_mass * float(u)
                    vals[2] += prob * carrier_mass * psi
                    vals[3] += prob * carrier_mass * psi * float(u)
                    vals[4] += prob * carrier_mass * psi * float(q)
    for key, vals in sorted(accum.items()):
        x, a, shore = key
        if vals[2] == 0:
            continue
        eu = vals[1] / vals[0]
        etu = vals[3] / vals[2]
        etq = vals[4] / vals[2]
        print(f"product x={x:.3f} a={a:.3f} {shore}: deficit={eu-etu:+.9g} EtQ={etq:.9g}")
    print("exact slices nearest y=(x+1)/2")
    wanted = {(7, 2), (8, 3), (9, 4)}
    for key, vals in sorted(slice_accum.items()):
        nm, nl, a, shore = key
        if (nm, nl) not in wanted or vals[2] == 0:
            continue
        eu = vals[1] / vals[0]
        etu = vals[3] / vals[2]
        etq = vals[4] / vals[2]
        print(
            f"slice nm={nm}/10 nl={nl}/5 a={a:.3f} {shore}: "
            f"deficit={eu-etu:+.9g} EtQ={etq:.9g}"
        )


if __name__ == "__main__":
    scan()
