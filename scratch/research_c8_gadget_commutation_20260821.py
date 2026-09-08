#!/usr/bin/env python3
"""Search for commuting C8 layers on several disjoint 1100/1010 gadgets."""

from __future__ import annotations

import argparse
from itertools import combinations, product

from search_b9_c8_switch_path_20260821 import canonical, msw_row, switches


def apply_pair(state, i, j, answer):
    return tuple(
        sorted(answer + tuple(state[k] for k in range(len(state)) if k not in (i, j)))
    )


def neighbours(state):
    for i, j in combinations(range(len(state)), 2):
        for answer in switches(state[i], state[j], (len(state[i]) - 1) // 2):
            yield apply_pair(state, i, j, answer), (state[i], state[j], answer)


def main(gadgets, outer, max_depth):
    words = ["".join(bits) + outer for bits in product(("1100", "1010"), repeat=gadgets)]
    r = 2 * gadgets + len(outer) // 2
    state = tuple(sorted(msw_row(w) for w in words))
    assert len(set(state)) == 2**gadgets
    frontier = {state}
    visited = {state: 0}
    layer = {0: 1}
    available_hist = {}
    for depth in range(1, max_depth + 1):
        new = set()
        counts = []
        for s in frontier:
            ns = list(neighbours(s))
            counts.append(len(ns))
            for t, _ in ns:
                if t not in visited:
                    visited[t] = depth
                    new.add(t)
        available_hist[depth - 1] = (min(counts, default=0), max(counts, default=0))
        if not new:
            break
        frontier = new
        layer[depth] = len(frontier)
    print(
        {
            "gadgets": gadgets,
            "outer": outer,
            "r": r,
            "rows": len(state),
            "states": len(visited),
            "layers": layer,
            "available_hist": available_hist,
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gadgets", type=int, default=2)
    parser.add_argument("--outer", default="")
    parser.add_argument("--max-depth", type=int, default=8)
    args = parser.parse_args()
    main(args.gadgets, args.outer, args.max_depth)
