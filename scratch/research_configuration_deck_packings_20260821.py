#!/usr/bin/env python3
"""Finite exploration of target-disjoint punctured-wreath decks.

The script only builds the simple target-set hypergraph (multiplicity of
directed words is irrelevant for a packing) and solves its maximum packing
MILP for small r.  It is research scaffolding, not a proof.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def mask(xs):
    z = 0
    for x in xs:
        z |= 1 << x
    return z


def deck(word, r):
    b = 2 * r + 1
    mids, lows = [], []
    for i in range(1, 2 * r + 1):
        mids.append(mask(word[(i + j) % b] for j in range(r)))
        lows.append(mask(word[(i + j) % b] for j in range(r - 1)))
    return tuple(sorted(mids)), tuple(sorted(lows))


def canonical_words(b):
    # The dirty start is linear, so a cyclic shift changes the puncture and
    # must not be quotiented out.  Reversal can still collapse after target
    # sets are formed; the dictionary below handles that safely.
    yield from itertools.permutations(range(b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("r", type=int)
    ap.add_argument("--time-limit", type=float, default=300.0)
    args = ap.parse_args()
    r = args.r
    b = 2 * r + 1

    unique = {}
    mult = Counter()
    for w in canonical_words(b):
        d = deck(w, r)
        mult[d] += 1
        unique.setdefault(d, w)
    edges = list(unique)
    print({"r": r, "b": b, "unique_target_edges": len(edges),
           "multiplicities": dict(Counter(mult.values()))})

    mid_vertices = sorted({x for e in edges for x in e[0]})
    low_vertices = sorted({x for e in edges for x in e[1]})
    vertices = [("M", x) for x in mid_vertices] + [("L", x) for x in low_vertices]
    vi = {v: i for i, v in enumerate(vertices)}
    rows, cols = [], []
    for j, (ms, ls) in enumerate(edges):
        for x in ms:
            rows.append(vi[("M", x)])
            cols.append(j)
        for x in ls:
            rows.append(vi[("L", x)])
            cols.append(j)
    A = coo_matrix((np.ones(len(rows)), (rows, cols)),
                   shape=(len(vertices), len(edges))).tocsr()
    res = milp(c=-np.ones(len(edges)), integrality=np.ones(len(edges)),
               bounds=Bounds(0, 1),
               constraints=LinearConstraint(A, 0, 1),
               options={"time_limit": args.time_limit, "mip_rel_gap": 0.0})
    chosen = np.flatnonzero(res.x > 0.5) if res.x is not None else []
    used_m = set()
    used_l = set()
    print({"status": res.message, "objective": -res.fun if res.fun is not None else None,
           "bound": getattr(res, "mip_node_count", None), "chosen": len(chosen),
           "middle_total": len(mid_vertices), "lower_total": len(low_vertices)})
    for j in chosen:
        ms, ls = edges[j]
        used_m.update(ms)
        used_l.update(ls)
        print("WORD", unique[edges[j]], "DIRTY_M", mask(unique[edges[j]][:r]))
    print({"unused_middle": len(mid_vertices) - len(used_m),
           "unused_lower": len(low_vertices) - len(used_l)})


if __name__ == "__main__":
    main()
