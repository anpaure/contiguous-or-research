#!/usr/bin/env python3
"""Pack maximal strong-GK FIFO paths that retire cleanly at k=0.

Candidates have length at least b and terminate at a source whose GK top
excess is zero.  Hence every earlier prescribed GK prefix has completely
retired before a reset seam.  We maximize covered middle sources exactly
for small b.  Exploratory; H100 only.
"""

from __future__ import annotations

from itertools import combinations, permutations
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def additions(n: int, ones: frozenset[int]) -> tuple[int, ...]:
    bits = [int(i in ones) for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return tuple(reversed([i for i in range(n) if not matched[i] and not bits[i]]))


def build(b: int) -> tuple[list[tuple[frozenset[int], int]], int, dict[int, int]]:
    n = 2 * b
    sources = [frozenset(c) for c in combinations(range(n), b)]
    sid = {s: i for i, s in enumerate(sources)}
    add = {s: additions(n, s) for s in sources}

    def step(q: tuple[int, ...]) -> tuple[int, ...] | None:
        s = frozenset(q)
        aa = add[s]
        if not aa:
            return None
        qp = q[1:] + (aa[0],)
        ap = add[frozenset(qp)]
        if len(aa) == 1:
            return qp
        common = min(len(ap), len(aa) - 1)
        if common == 0 or ap[:common] != aa[1 : 1 + common]:
            return None
        return qp

    unique: dict[frozenset[int], int] = {}
    length_hist: dict[int, int] = {}
    dirty_hist: dict[tuple[int, int], int] = {}
    for q0 in permutations(range(n), b):
        q = q0
        path: list[int] = []
        seen: set[int] = set()
        while True:
            z = sid[frozenset(q)]
            if z in seen:
                break
            seen.add(z)
            path.append(z)
            qp = step(q)
            if qp is None:
                if len(path) >= b:
                    end_k = len(add[frozenset(q)])
                    dirty_hist[(len(path), end_k)] = dirty_hist.get((len(path), end_k), 0) + 1
                # Keep only genuinely clean retirement endpoints.
                if not add[frozenset(q)] and len(path) >= b:
                    e = frozenset(path)
                    unique[e] = max(unique.get(e, 0), len(path))
                    length_hist[len(path)] = length_hist.get(len(path), 0) + 1
                break
            q = qp
    print("DIRTY_HIST", b, sorted(dirty_hist.items()), flush=True)
    return [(e, w) for e, w in unique.items()], len(sources), length_hist


def solve(b: int) -> None:
    edges, N, raw_hist = build(b)
    rr: list[int] = []
    cc: list[int] = []
    weights = []
    for j, (e, w) in enumerate(edges):
        weights.append(w)
        for v in e:
            rr.append(v)
            cc.append(j)
    A = coo_matrix((np.ones(len(rr)), (rr, cc)), shape=(N, len(edges))).tocsr()
    con = LinearConstraint(A, np.zeros(N), np.ones(N))
    res = milp(
        -np.asarray(weights, dtype=float),
        integrality=np.ones(len(edges)),
        bounds=Bounds(np.zeros(len(edges)), np.ones(len(edges))),
        constraints=con,
        options={"time_limit": 300.0, "mip_rel_gap": 0.0, "disp": False},
    )
    if res.x is None:
        raise RuntimeError(res.message)
    val = int(round(-res.fun))
    print(
        "CASE",
        b,
        "N",
        N,
        "UNIQUE",
        len(edges),
        "RAW_LENGTHS",
        sorted(raw_hist.items()),
        "COVER",
        val,
        "LEAVE",
        N - val,
        "FRACTION",
        val / N,
        "STATUS",
        res.message,
        flush=True,
    )


def main() -> None:
    build(6)


if __name__ == "__main__":
    main()
