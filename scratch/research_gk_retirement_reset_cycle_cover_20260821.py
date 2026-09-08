#!/usr/bin/env python3
"""Exact finite search for GK-successor FIFO cycles with free retirement resets.

A state is an ordered b-tuple of distinct labels.  Its source is the
underlying rank-b set.  If the source has positive GK top excess, append its
first GK addition and require full surviving-prefix compatibility.  If the
source has top excess zero, append any absent label.  We ask for a directed
cycle cover selecting exactly one state above every source, and iteratively
add source-subtour cuts in an attempt to obtain one Hamilton cycle.

Research-only; run on H100.
"""

from __future__ import annotations

from itertools import combinations, permutations
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix, vstack


def additions(n: int, source: frozenset[int]) -> tuple[int, ...]:
    bits = [i in source for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return tuple(
        reversed([i for i in range(n) if not matched[i] and not bits[i]])
    )


def build(b: int):
    n = 2 * b
    sources = [frozenset(c) for c in combinations(range(n), b)]
    source_id = {s: i for i, s in enumerate(sources)}
    add = {s: additions(n, s) for s in sources}
    states = [q for s in sources for q in permutations(sorted(s))]
    state_id = {q: i for i, q in enumerate(states)}
    state_source = np.asarray([source_id[frozenset(q)] for q in states], dtype=int)

    edges: list[tuple[int, int]] = []
    dirty_good = 0
    dirty_bad = 0
    for qi, q in enumerate(states):
        s = frozenset(q)
        aa = add[s]
        if aa:
            qp = q[1:] + (aa[0],)
            ap = add[frozenset(qp)]
            common = min(len(ap), max(0, len(aa) - 1))
            good = len(aa) == 1 or (
                common > 0 and ap[:common] == aa[1 : 1 + common]
            )
            if good:
                edges.append((qi, state_id[qp]))
                dirty_good += 1
            else:
                dirty_bad += 1
        else:
            for y in range(n):
                if y not in s:
                    qp = q[1:] + (y,)
                    edges.append((qi, state_id[qp]))

    return sources, states, state_source, edges, add, dirty_good, dirty_bad


def selected_cycles(
    chosen: np.ndarray,
    edges: list[tuple[int, int]],
    state_source: np.ndarray,
) -> list[list[int]]:
    nxt = {edges[j][0]: edges[j][1] for j in np.flatnonzero(chosen > 0.5)}
    cycles: list[list[int]] = []
    seen: set[int] = set()
    for start in nxt:
        if start in seen:
            continue
        cur = start
        cyc: list[int] = []
        while cur not in seen:
            seen.add(cur)
            cyc.append(int(state_source[cur]))
            cur = nxt[cur]
        cycles.append(cyc)
    return cycles


def solve(b: int, max_rounds: int = 100) -> None:
    sources, states, state_source, edges, add, dirty_good, dirty_bad = build(b)
    ns = len(sources)
    nv = len(states)
    ne = len(edges)

    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    lower: list[float] = []
    upper: list[float] = []
    row = 0

    # One outgoing edge among all states above each source.
    for sid in range(ns):
        for j, (u, _v) in enumerate(edges):
            if state_source[u] == sid:
                rows.append(row)
                cols.append(j)
                data.append(1.0)
        lower.append(1.0)
        upper.append(1.0)
        row += 1

    # Statewise flow conservation selects one consistent state per source.
    outgoing: list[list[int]] = [[] for _ in range(nv)]
    incoming: list[list[int]] = [[] for _ in range(nv)]
    for j, (u, v) in enumerate(edges):
        outgoing[u].append(j)
        incoming[v].append(j)
    for u in range(nv):
        if not outgoing[u] and not incoming[u]:
            continue
        for j in outgoing[u]:
            rows.append(row)
            cols.append(j)
            data.append(1.0)
        for j in incoming[u]:
            rows.append(row)
            cols.append(j)
            data.append(-1.0)
        lower.append(0.0)
        upper.append(0.0)
        row += 1

    base = coo_matrix((data, (rows, cols)), shape=(row, ne)).tocsr()
    cut_rows = []
    cut_lb = []
    cut_ub = []
    rng = np.random.default_rng(20260821 + b)

    for rnd in range(max_rounds):
        if cut_rows:
            A = vstack([base] + cut_rows, format="csr")
            lb = np.asarray(lower + cut_lb)
            ub = np.asarray(upper + cut_ub)
        else:
            A = base
            lb = np.asarray(lower)
            ub = np.asarray(upper)
        # A tiny random objective changes the cycle cover between cut rounds.
        cost = rng.uniform(0.0, 1.0e-6, size=ne)
        res = milp(
            cost,
            integrality=np.ones(ne),
            bounds=Bounds(np.zeros(ne), np.ones(ne)),
            constraints=LinearConstraint(A, lb, ub),
            options={"time_limit": 600.0, "mip_rel_gap": 0.0, "disp": False},
        )
        if res.x is None:
            print("CASE", b, "INFEASIBLE_AFTER", rnd, res.message, flush=True)
            return
        cycles = selected_cycles(res.x, edges, state_source)
        lens = sorted((len(c) for c in cycles), reverse=True)
        print(
            "ROUND",
            rnd,
            "B",
            b,
            "SOURCES",
            ns,
            "STATES",
            nv,
            "EDGES",
            ne,
            "DIRTY_GOOD_BAD",
            dirty_good,
            dirty_bad,
            "CYCLES",
            len(cycles),
            "LENGTHS",
            lens[:20],
            flush=True,
        )
        if len(cycles) == 1:
            print("HAMILTON_PASS", b, flush=True)
            return

        # Every proper source cycle must send at least one selected edge out.
        for cyc in cycles:
            shore = set(cyc)
            rr: list[int] = []
            cc: list[int] = []
            for j, (u, v) in enumerate(edges):
                if state_source[u] in shore and state_source[v] not in shore:
                    rr.append(0)
                    cc.append(j)
            if not cc:
                print("CLOSED_SOURCE_COMPONENT", b, len(shore), flush=True)
                return
            cut_rows.append(
                coo_matrix((np.ones(len(cc)), (rr, cc)), shape=(1, ne)).tocsr()
            )
            cut_lb.append(1.0)
            cut_ub.append(np.inf)

    print("NO_HAMILTON_WITHIN_ROUNDS", b, max_rounds, flush=True)


def reachability_diagnostic(b: int) -> None:
    sources, states, state_source, edges, add, _dirty_good, _dirty_bad = build(b)
    outgoing: list[list[int]] = [[] for _ in states]
    incoming: list[list[int]] = [[] for _ in states]
    for u, v in edges:
        outgoing[u].append(v)
        incoming[v].append(u)
    clean = [
        i for i, q in enumerate(states) if not add[frozenset(q)]
    ]
    reached = set(clean)
    frontier = list(clean)
    while frontier:
        u = frontier.pop()
        for v in outgoing[u]:
            if v not in reached:
                reached.add(v)
                frontier.append(v)
    source_reached = {int(state_source[u]) for u in reached}
    k_hist: dict[int, list[int]] = {}
    for sid, source in enumerate(sources):
        k_hist.setdefault(len(add[source]), [0, 0])
        k_hist[len(add[source])][0] += 1
        if sid in source_reached:
            k_hist[len(add[source])][1] += 1

    # Iteratively peel states which cannot lie on any directed cycle.
    alive = set(range(len(states)))
    outdeg = [len(outgoing[u]) for u in range(len(states))]
    indeg = [len(incoming[u]) for u in range(len(states))]
    queue = [u for u in alive if outdeg[u] == 0 or indeg[u] == 0]
    while queue:
        u = queue.pop()
        if u not in alive:
            continue
        alive.remove(u)
        for v in outgoing[u]:
            if v in alive:
                indeg[v] -= 1
                if indeg[v] == 0 or outdeg[v] == 0:
                    queue.append(v)
        for v in incoming[u]:
            if v in alive:
                outdeg[v] -= 1
                if indeg[v] == 0 or outdeg[v] == 0:
                    queue.append(v)
    alive_sources = {int(state_source[u]) for u in alive}
    alive_hist: dict[int, list[int]] = {}
    for sid, source in enumerate(sources):
        alive_hist.setdefault(len(add[source]), [0, 0])
        alive_hist[len(add[source])][0] += 1
        if sid in alive_sources:
            alive_hist[len(add[source])][1] += 1
    print(
        "REACH",
        b,
        "STATES",
        len(states),
        "REACHED",
        len(reached),
        "SOURCES",
        len(source_reached),
        "K_TOTAL_REACHED",
        sorted(k_hist.items()),
        "CYCLE_CORE_STATES",
        len(alive),
        "SOURCES",
        len(alive_sources),
        "K_TOTAL_ALIVE",
        sorted(alive_hist.items()),
        flush=True,
    )


def max_cycle_packing(b: int) -> None:
    sources, states, state_source, edges, _add, _dg, _db = build(b)
    ns = len(sources)
    nv = len(states)
    ne = len(edges)
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    lower: list[float] = []
    upper: list[float] = []
    row = 0
    outgoing: list[list[int]] = [[] for _ in range(nv)]
    incoming: list[list[int]] = [[] for _ in range(nv)]
    for j, (u, v) in enumerate(edges):
        outgoing[u].append(j)
        incoming[v].append(j)
    for sid in range(ns):
        for j, (u, _v) in enumerate(edges):
            if state_source[u] == sid:
                rows.append(row)
                cols.append(j)
                data.append(1.0)
        lower.append(0.0)
        upper.append(1.0)
        row += 1
    for u in range(nv):
        for j in outgoing[u]:
            rows.append(row)
            cols.append(j)
            data.append(1.0)
        for j in incoming[u]:
            rows.append(row)
            cols.append(j)
            data.append(-1.0)
        lower.append(0.0)
        upper.append(0.0)
        row += 1
    A = coo_matrix((data, (rows, cols)), shape=(row, ne)).tocsr()
    res = milp(
        -np.ones(ne),
        integrality=np.ones(ne),
        bounds=Bounds(np.zeros(ne), np.ones(ne)),
        constraints=LinearConstraint(A, np.asarray(lower), np.asarray(upper)),
        options={"time_limit": 600.0, "mip_rel_gap": 0.0, "disp": False},
    )
    if res.x is None:
        print("MAX_CYCLE_FAIL", b, res.message, flush=True)
        return
    cycles = selected_cycles(res.x, edges, state_source)
    value = int(round(-res.fun))
    selected_sources = {sid for cyc in cycles for sid in cyc}
    k_selected: dict[int, list[int]] = {}
    for sid, source in enumerate(sources):
        k = len(additions(2 * b, source))
        k_selected.setdefault(k, [0, 0])
        k_selected[k][0] += 1
        if sid in selected_sources:
            k_selected[k][1] += 1
    print(
        "MAX_CYCLE",
        b,
        "VALUE",
        value,
        "LEAVE",
        ns - value,
        "CYCLES",
        len(cycles),
        "LENGTHS",
        sorted((len(c) for c in cycles), reverse=True)[:30],
        "K_TOTAL_SELECTED",
        sorted(k_selected.items()),
        "STATUS",
        res.message,
        flush=True,
    )


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "max":
        b = int(sys.argv[2])
        reachability_diagnostic(b)
        max_cycle_packing(b)
        return
    for b in (2, 3, 4):
        reachability_diagnostic(b)
        max_cycle_packing(b)
        solve(b)


if __name__ == "__main__":
    main()
