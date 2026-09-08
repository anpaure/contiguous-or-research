#!/usr/bin/env python3
"""Exploratory H100 diagnostic for overlap graphs of the b=5 product bank."""

from __future__ import annotations

import random
from collections import deque

import numpy as np

from audit_polylog_factor_menu_residual_hitting_selector_20260821 import (
    conjugate_orders,
    factors_b5,
)


def physical_atoms_b5(rank_perm, q, rng):
    b = 5
    factors = factors_b5()
    atoms = []
    profiles = []
    all_sources = set()
    for r in range(q, b - q + 1):
        pa = list(range(b))
        pb = list(range(b))
        rng.shuffle(pa)
        rng.shuffle(pb)
        fa = conjugate_orders(factors[r], pa)
        fb = conjugate_orders(factors[r], pb)
        pset = {x for x in range(b) if rank_perm[x] < r}
        types = [x in pset for x in range(b)]
        for alpha in fa:
            for beta in fb:
                ca = cb = 0
                word = []
                for time in range(b * b + b):
                    if types[time % b]:
                        word.append(alpha[ca % b])
                        ca += 1
                    else:
                        word.append(b + beta[cb % b])
                        cb += 1
                atom = frozenset(
                    frozenset(word[start : start + b])
                    for start in range(b * b)
                )
                assert len(atom) == b * b
                assert not (atom & all_sources)
                all_sources |= atom
                atoms.append(atom)
                profiles.append(r)
    return atoms, profiles


def components(matrix):
    left, right = matrix.shape
    seen_l = set()
    seen_r = set()
    out = []
    for start in range(left):
        if start in seen_l:
            continue
        queue = deque([("l", start)])
        seen_l.add(start)
        ls, rs = set(), set()
        while queue:
            side, vertex = queue.popleft()
            if side == "l":
                ls.add(vertex)
                for j in np.flatnonzero(matrix[vertex]):
                    j = int(j)
                    if j not in seen_r:
                        seen_r.add(j)
                        queue.append(("r", j))
            else:
                rs.add(vertex)
                for i in np.flatnonzero(matrix[:, vertex]):
                    i = int(i)
                    if i not in seen_l:
                        seen_l.add(i)
                        queue.append(("l", i))
        out.append((tuple(sorted(ls)), tuple(sorted(rs))))
    assert len(seen_l) == left and len(seen_r) == right
    return out


def main():
    rng = random.Random(20260821)
    rank_perm = list(range(5))
    rng.shuffle(rank_perm)
    for q in (1, 2):
        for trial in range(5):
            aa, pa = physical_atoms_b5(rank_perm, q, rng)
            bb, pb = physical_atoms_b5(rank_perm, q, rng)
            matrix = np.array(
                [[len(x & y) for y in bb] for x in aa], dtype=float
            )
            assert np.all(matrix.sum(axis=0) == 25)
            assert np.all(matrix.sum(axis=1) == 25)
            comps = components(matrix)
            singular = np.linalg.svd(matrix / 25.0, compute_uv=False)
            print(
                {
                    "q": q,
                    "trial": trial,
                    "atoms": len(aa),
                    "components": len(comps),
                    "component_sizes": [(len(x), len(y)) for x, y in comps],
                    "component_profiles": [
                        (sorted({pa[i] for i in x}), sorted({pb[j] for j in y}))
                        for x, y in comps
                    ],
                    "singular_values": [round(float(x), 6) for x in singular],
                }
            )


if __name__ == "__main__":
    main()

