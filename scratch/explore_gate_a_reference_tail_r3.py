#!/usr/bin/env python3
"""Monte Carlo exact-slice G.168 U scan for the genuine r=3 catalogue."""

import argparse
from collections import defaultdict
from itertools import combinations, permutations
from math import factorial
import random


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def catalogue(r):
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


def state_roots(state, data, r, m=12):
    targets, rows, row_masks, incidence, conflicts = data
    alive = 0
    for i, row_mask in enumerate(row_masks):
        if row_mask & ~state == 0:
            alive |= 1 << i
    Z = alive.bit_count()
    if not Z:
        return []
    counts = {
        shore: sum(bool(state & (1 << v)) for v, t in enumerate(targets) if t[0] == shore)
        for shore in ("M", "L")
    }
    z = {shore: 2 * r * Z / counts[shore] for shore in counts}
    degrees = [(incidence[v] & alive).bit_count() for v in range(len(targets))]
    alive_rows = [i for i in range(len(rows)) if alive & (1 << i)]
    c = {i: (conflicts[i] & alive).bit_count() for i in alive_rows}
    excess = {i: sum(degrees[v] for v in rows[i]) - c[i] for i in alive_rows}
    bvals = [degrees[v] - z[targets[v][0]] for v in range(len(targets))]
    rowsum = {i: sum(bvals[v] for v in rows[i]) for i in alive_rows}
    roots = []
    for v, target in enumerate(targets):
        d = degrees[v]
        if d < m:
            continue
        star = incidence[v] & alive
        ids = [i for i in alive_rows if star & (1 << i)]
        rv = sum(rowsum[i] - bvals[v] for i in ids) / d
        jv = sum(excess[i] for i in ids) / d
        companion_raw = sum(
            sum(degrees[u] for u in rows[i] if u != v) for i in ids
        ) / d
        roots.append(
            (
                target[0],
                d,
                z[target[0]],
                (rv - jv) / z[target[0]],
                falling(d, m),
                companion_raw - jv,
                Z,
            )
        )
    return roots


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260822)
    args = ap.parse_args()
    r = 3
    data = catalogue(r)
    targets = data[0]
    shores = {
        shore: [v for v, t in enumerate(targets) if t[0] == shore]
        for shore in ("M", "L")
    }
    print("catalogue", len(targets), len(data[1]), {k: len(v) for k, v in shores.items()})
    rng = random.Random(args.seed)
    aa = (1.001, 1.01, 1.05, 1.1, 1.25, 1.5)
    removed = (1, 3, 6, 9, 12)
    accum = defaultdict(lambda: [0.0] * 4)
    for t in removed:
        nm = len(shores["M"]) - t
        nl = len(shores["L"]) - t
        for _ in range(args.samples):
            kept = rng.sample(shores["M"], nm) + rng.sample(shores["L"], nl)
            state = sum(1 << v for v in kept)
            for shore, d, z, u, mass, _raw, _Z in state_roots(state, data, r):
                for a in aa:
                    X = d / z
                    psi = 0.0 if X <= a else ((X - a) / X) ** 12
                    vals = accum[t, a, shore]
                    vals[0] += mass
                    vals[1] += mass * u
                    vals[2] += mass * psi
                    vals[3] += mass * psi * u
    for key, vals in sorted(accum.items()):
        if vals[2] == 0:
            continue
        t, a, shore = key
        print(
            f"remove={t} a={a:.3f} {shore}: "
            f"deficit={vals[1]/vals[0]-vals[3]/vals[2]:+.9g} "
            f"tailmass={vals[2]/vals[0]:.3g}"
        )


if __name__ == "__main__":
    main()
