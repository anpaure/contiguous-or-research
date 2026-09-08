#!/usr/bin/env python3
"""Exact recurrent core of length-b strong-GK FIFO macros.

A macro consists of b source states, hence b-1 forced GK transitions.  If
its ordered start is q=(P,R), its ordered endpoint is (R,F), where F is the
block of b-1 forced additions.  One arbitrary FIFO reset then gives the
next macro start (F,R').  This script constructs that directed macro graph
and deletes every vertex not lying on a directed cycle.

The computation is exploratory and intended for H100.  It deliberately
reports both reset conventions: R'=R is either allowed as an ignored
duplicate window or forbidden as a non-Johnson reset.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations


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
        reversed([i for i in range(n) if not bits[i] and not matched[i]])
    )


def interval_runs(prefix: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Split an ordered prefix at every failure of x_(i+1)=x_i-1."""
    if not prefix:
        return ()
    runs: list[list[int]] = [[prefix[0]]]
    for x in prefix[1:]:
        if x == runs[-1][-1] - 1:
            runs[-1].append(x)
        else:
            runs.append([x])
    return tuple(tuple(run) for run in runs)


def build(b: int, allow_same_reset: bool) -> dict[str, object]:
    n = 2 * b
    add_cache: dict[frozenset[int], tuple[int, ...]] = {}

    def aa(q: tuple[int, ...]) -> tuple[int, ...]:
        source = frozenset(q)
        if source not in add_cache:
            add_cache[source] = additions(n, source)
        return add_cache[source]

    def strong_step(q: tuple[int, ...]) -> tuple[int, ...] | None:
        add = aa(q)
        if not add:
            return None
        nxt = q[1:] + (add[0],)
        nxt_add = aa(nxt)
        common = min(len(nxt_add), max(0, len(add) - 1))
        if len(add) == 1 or (
            common > 0 and nxt_add[:common] == add[1 : 1 + common]
        ):
            return nxt
        return None

    starts: dict[tuple[int, ...], int] = {}
    endpoints: list[tuple[int, ...]] = []
    paths: list[tuple[frozenset[int], ...]] = []
    forced_blocks: list[tuple[int, ...]] = []
    for q0 in permutations(range(n), b):
        q = q0
        path = [frozenset(q)]
        forced: list[int] = []
        for _ in range(b - 1):
            add = aa(q)
            if not add:
                q = ()
                break
            forced.append(add[0])
            q = strong_step(q)
            if q is None:
                q = ()
                break
            path.append(frozenset(q))
        if q:
            starts[q0] = len(endpoints)
            endpoints.append(q)
            paths.append(tuple(path))
            forced_blocks.append(tuple(forced))

    adjacency: list[list[int]] = [[] for _ in endpoints]
    reverse: list[list[int]] = [[] for _ in endpoints]
    for q0, i in starts.items():
        endpoint = endpoints[i]
        old_sentinel = endpoint[0]
        forced = endpoint[1:]
        assert forced == forced_blocks[i]
        for new_sentinel in range(n):
            if new_sentinel in forced:
                continue
            if not allow_same_reset and new_sentinel == old_sentinel:
                continue
            nxt = forced + (new_sentinel,)
            j = starts.get(nxt)
            if j is not None:
                adjacency[i].append(j)
                reverse[j].append(i)

    # Kosaraju SCCs.  A vertex lies on a directed cycle exactly when its SCC
    # has size at least two or it has a self-loop.
    seen = bytearray(len(endpoints))
    finish_order: list[int] = []
    for start in range(len(endpoints)):
        if seen[start]:
            continue
        seen[start] = 1
        stack: list[tuple[int, int]] = [(start, 0)]
        while stack:
            v, cursor = stack[-1]
            if cursor < len(adjacency[v]):
                w = adjacency[v][cursor]
                stack[-1] = (v, cursor + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                finish_order.append(v)
                stack.pop()

    component = [-1] * len(endpoints)
    component_sizes: list[int] = []
    for start in reversed(finish_order):
        if component[start] >= 0:
            continue
        cid = len(component_sizes)
        component[start] = cid
        size = 0
        stack = [start]
        while stack:
            v = stack.pop()
            size += 1
            for w in reverse[v]:
                if component[w] < 0:
                    component[w] = cid
                    stack.append(w)
        component_sizes.append(size)

    inverse = {i: q for q, i in starts.items()}
    core = [
        i
        for i in range(len(endpoints))
        if component_sizes[component[i]] > 1 or i in adjacency[i]
    ]
    core_sources = set().union(*(set(paths[i]) for i in core)) if core else set()

    # Exact necessary condition for a bi-infinite/cyclic macro chain: the
    # largest coordinate cannot occur in P.  Every P is the preceding forced
    # output block, while every forced GK output is below the current maximum.
    assert all((n - 1) not in inverse[i][:-1] for i in core)

    run_hist = Counter(len(interval_runs(inverse[i][:-1])) for i in core)
    return {
        "b": b,
        "ordered_macros": len(starts),
        "arcs": sum(map(len, adjacency)),
        "core": core,
        "core_states": [inverse[i] for i in core],
        "core_sources": core_sources,
        "run_hist": run_hist,
    }


def main() -> None:
    for allow_same in (True, False):
        print("ALLOW_SAME_RESET", allow_same)
        for b in range(2, 7):
            data = build(b, allow_same)
            states = data["core_states"]
            assert isinstance(states, list)
            print(
                "CASE",
                b,
                "ORDERED_MACROS",
                data["ordered_macros"],
                "ARCS",
                data["arcs"],
                "CORE",
                len(states),
                "SOURCE_UNION",
                len(data["core_sources"]),
                "W",
                __import__("math").comb(2 * b, b),
                "INTERVAL_RUNS",
                sorted(data["run_hist"].items()),
                flush=True,
            )
            if b in (5, 6):
                reps = sorted(
                    states,
                    key=lambda q: (-len(interval_runs(q[:-1])), q),
                )[:12]
                print(
                    "REPRESENTATIVES",
                    b,
                    [(q, interval_runs(q[:-1])) for q in reps],
                    flush=True,
                )


if __name__ == "__main__":
    main()
