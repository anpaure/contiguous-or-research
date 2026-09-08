#!/usr/bin/env python3
"""Small-r diagnostics for the Gate-A carrier-avoidance regression.

This is a finite research diagnostic, not evidence for an asymptotic theorem.
It constructs the directed punctured configuration hypergraph, follows random
sequential greedy matching trajectories, and evaluates

    R_m(v) = sum_{G not containing v} (d_v-a_G(v))_m/(d_v)_m

and zeta_m(v)=|E|-R_m(v) exactly (up to floating arithmetic in the final
division).  Roots are grouped by their current degree within each shore.
"""

from __future__ import annotations

import argparse
import itertools
import random
from collections import defaultdict

import numpy as np


def falling(a: int, m: int) -> int:
    out = 1
    for j in range(m):
        out *= a - j
    return out


def build(r: int):
    b = 2 * r + 1
    middle = list(itertools.combinations(range(b), r))
    lower = list(itertools.combinations(range(b), r - 1))
    mid_id = {x: i for i, x in enumerate(middle)}
    low_id = {x: len(middle) + i for i, x in enumerate(lower)}
    edges = []
    seen = set()
    for w in itertools.permutations(range(b)):
        row = []
        for s in range(1, b):
            row.append(mid_id[tuple(sorted(w[(s + j) % b] for j in range(r)))])
        for s in range(1, b):
            row.append(low_id[tuple(sorted(w[(s + j) % b] for j in range(r - 1)))])
        row = tuple(sorted(row))
        if row not in seen:
            seen.add(row)
            edges.append(row)
    return len(middle), len(middle) + len(lower), edges


def residual_edges(edges, alive):
    return [e for e in edges if all(alive[v] for v in e)]


def regression_stats(n_mid: int, n_vert: int, edges, alive, m: int):
    z = len(edges)
    if not edges:
        return []
    incidence = np.zeros((n_vert, z), dtype=np.bool_)
    for j, e in enumerate(edges):
        incidence[list(e), j] = True
    overlap = (incidence.T.astype(np.uint8) @ incidence.astype(np.uint8)) > 0
    rows = []
    for lo, hi, shore in ((0, n_mid, "M"), (n_mid, n_vert, "L")):
        vals = defaultdict(list)
        alive_count = int(alive[lo:hi].sum())
        avg = (len(edges) * (len(edges[0]) // 2) / alive_count) if alive_count else 0.0
        for v in range(lo, hi):
            if not alive[v]:
                continue
            star = incidence[v]
            d = int(star.sum())
            if d < m:
                continue
            denom = falling(d, m)
            # a_G(v) is the number of star rows conflicting with G.
            a = overlap[:, star].sum(axis=1)
            external = ~star
            numer = np.array([falling(d - int(x), m) if d - int(x) >= m else 0
                              for x in a[external]], dtype=object).sum()
            R = float(numer / denom)
            vals[d].append((R, z - R))
        means = {d: (sum(x for x, _ in xs) / len(xs),
                     sum(y for _, y in xs) / len(xs), len(xs))
                 for d, xs in vals.items()}
        bad = 0.0
        witness = None
        ds = sorted(means)
        for i, d in enumerate(ds):
            for e in ds[i + 1:]:
                # zeta(d)-zeta(e) = R(e)-R(d)
                inv = means[e][0] - means[d][0]
                if inv > bad:
                    bad = inv
                    witness = (d, e, means[d], means[e])
        rows.append((shore, avg, bad, witness, means))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--r", type=int, default=3)
    ap.add_argument("--m", type=int, default=2)
    ap.add_argument("--trials", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    n_mid, n_vert, catalogue = build(args.r)
    print(f"r={args.r} supports={len(catalogue)} vertices={n_vert} middle={n_mid}")
    worst = []
    for trial in range(args.trials):
        alive = np.ones(n_vert, dtype=np.bool_)
        step = 0
        while True:
            current = residual_edges(catalogue, alive)
            if not current:
                break
            stats = regression_stats(n_mid, n_vert, current, alive, args.m)
            for shore, avg, bad, witness, means in stats:
                ratio = bad / avg if avg else 0.0
                worst.append((ratio, trial, step, shore, avg, bad, witness, means))
            chosen = rng.choice(current)
            alive[list(chosen)] = False
            step += 1
    worst.sort(key=lambda x: x[0], reverse=True)
    for row in worst[:20]:
        ratio, trial, step, shore, avg, bad, witness, means = row
        print(f"ratio={ratio:.8g} trial={trial} step={step} shore={shore} "
              f"z={avg:.8g} bad={bad:.8g} witness={witness}")
        print("  groups", means)


if __name__ == "__main__":
    main()
