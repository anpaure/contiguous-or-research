#!/usr/bin/env python3
"""Exact recurrent core for GK/FIFO macros with ``c`` arbitrary resets.

A start queue is ``(P,R_0,...,R_{c-1})`` with ``|P|=b-c``.  After
``b-c`` suffix-compatible Greene--Kleitman steps it is
``(R_0,...,R_{c-1},F)``.  We then permit ``c`` legal FIFO updates, so the
next macro starts at ``(F,R'_0,...,R'_{c-1})``.  Only the intermediate
reset sources are sacrificed.  Thus any fixed c, and more generally any
``c=o(b/H)``, would have asymptotically negligible incidence cost.

This is a finite diagnostic, not a theorem.  Run only on H100.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations
from math import comb
import argparse


def additions(n: int, source: frozenset[int]) -> tuple[int, ...]:
    """Future additions in the alternating-coordinate GK chain."""
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


def build(b: int, resets: int, forbid_reusing_dropped: bool):
    assert 1 <= resets < b
    n = 2 * b
    strong_count = b - resets
    add_cache: dict[frozenset[int], tuple[int, ...]] = {}

    def aa(q: tuple[int, ...]) -> tuple[int, ...]:
        source = frozenset(q)
        if source not in add_cache:
            add_cache[source] = additions(n, source)
        return add_cache[source]

    def strong_step(q: tuple[int, ...]):
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
    paths: list[tuple[frozenset[int], ...]] = []
    forced_blocks: list[tuple[int, ...]] = []
    old_suffixes: list[tuple[int, ...]] = []
    by_prefix: dict[tuple[int, ...], list[int]] = defaultdict(list)

    for q0 in permutations(range(n), b):
        q = q0
        path = [frozenset(q)]
        forced: list[int] = []
        for _ in range(strong_count):
            add = aa(q)
            if not add:
                q = None
                break
            forced.append(add[0])
            q = strong_step(q)
            if q is None:
                break
            path.append(frozenset(q))
        if q is None:
            continue
        forced_tuple = tuple(forced)
        old_suffix = q[:resets]
        assert q[resets:] == forced_tuple
        idx = len(paths)
        starts[q0] = idx
        paths.append(tuple(path))
        forced_blocks.append(forced_tuple)
        old_suffixes.append(old_suffix)
        by_prefix[q0[:strong_count]].append(idx)

    inverse: list[tuple[int, ...] | None] = [None] * len(starts)
    for q, i in starts.items():
        inverse[i] = q

    adjacency: list[list[int]] = [[] for _ in paths]
    reverse: list[list[int]] = [[] for _ in paths]
    for i, forced in enumerate(forced_blocks):
        old = old_suffixes[i]
        for j in by_prefix.get(forced, ()):
            qn = inverse[j]
            assert qn is not None
            new = qn[strong_count:]
            # At reset j, the queue still contains old[j+1:], all of F,
            # and new[:j].  The candidate start already guarantees that
            # F and the new labels are mutually disjoint.
            legal = all(new[t] not in old[t + 1 :] for t in range(resets))
            if forbid_reusing_dropped:
                legal = legal and all(new[t] != old[t] for t in range(resets))
            if not legal:
                continue
            adjacency[i].append(j)
            reverse[j].append(i)

    # Exact SCC support via iterative Kosaraju.
    seen = bytearray(len(paths))
    finish: list[int] = []
    for root in range(len(paths)):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, at = stack[-1]
            if at < len(adjacency[v]):
                w = adjacency[v][at]
                stack[-1] = (v, at + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                finish.append(v)
                stack.pop()

    component = [-1] * len(paths)
    sizes: list[int] = []
    for root in reversed(finish):
        if component[root] >= 0:
            continue
        cid = len(sizes)
        size = 0
        component[root] = cid
        stack = [root]
        while stack:
            v = stack.pop()
            size += 1
            for w in reverse[v]:
                if component[w] < 0:
                    component[w] = cid
                    stack.append(w)
        sizes.append(size)

    cyclic_components = {cid for cid, size in enumerate(sizes) if size > 1}
    for i, row in enumerate(adjacency):
        if i in row:
            cyclic_components.add(component[i])
    core = [i for i in range(len(paths)) if component[i] in cyclic_components]
    core_sources = set().union(*(set(paths[i]) for i in core)) if core else set()
    return {
        "b": b,
        "resets": resets,
        "starts": len(starts),
        "arcs": sum(map(len, adjacency)),
        "core": len(core),
        "components": Counter(component[i] for i in core),
        "core_sources": len(core_sources),
        "W": comb(2 * b, b),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=5)
    parser.add_argument("--max-resets", type=int, default=3)
    parser.add_argument("--b", type=int)
    parser.add_argument("--resets", type=int)
    parser.add_argument(
        "--forbid-mode",
        choices=("both", "allow", "forbid"),
        default="both",
    )
    args = parser.parse_args()
    forbid_values = {
        "both": (False, True),
        "allow": (False,),
        "forbid": (True,),
    }[args.forbid_mode]
    b_values = (args.b,) if args.b is not None else range(2, args.max_b + 1)
    for forbid in forbid_values:
        print("FORBID_REUSING_DROPPED", forbid)
        for b in b_values:
            reset_values = (
                (args.resets,)
                if args.resets is not None
                else range(1, min(args.max_resets, b - 1) + 1)
            )
            for resets in reset_values:
                data = build(b, resets, forbid)
                print(
                    "CASE",
                    b,
                    "RESETS",
                    resets,
                    "STARTS",
                    data["starts"],
                    "ARCS",
                    data["arcs"],
                    "CORE",
                    data["core"],
                    "CYCLIC_COMPONENTS",
                    len(data["components"]),
                    "MAX_COMPONENT",
                    max(data["components"].values(), default=0),
                    "SOURCE_UNION",
                    data["core_sources"],
                    "W",
                    data["W"],
                    flush=True,
                )


if __name__ == "__main__":
    main()
