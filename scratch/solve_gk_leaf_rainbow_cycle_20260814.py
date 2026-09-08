#!/usr/bin/env python3
"""CNF test for a directed leaf-move cycle with pairwise distinct lowers."""

from __future__ import annotations

import argparse
import collections
import itertools
from pathlib import Path


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def matching(x: int, n: int):
    stack: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    fz = [i for i in range(n) if not ((x >> i) & 1) and i not in mate]
    return mate, fz


class Cnf:
    def __init__(self):
        self.nvars = 0
        self.clauses: list[list[int]] = []

    def var(self) -> int:
        self.nvars += 1
        return self.nvars

    def at_most_one(self, xs: list[int]) -> None:
        if len(xs) < 2:
            return
        s = [self.var() for _ in range(len(xs) - 1)]
        self.clauses.append([-xs[0], s[0]])
        for i in range(1, len(xs) - 1):
            self.clauses.extend(([-xs[i], s[i]], [-s[i - 1], s[i]],
                                 [-xs[i], -s[i - 1]]))
        self.clauses.append([-xs[-1], -s[-1]])

    def write(self, path: Path) -> None:
        with path.open("w") as f:
            f.write(f"p cnf {self.nvars} {len(self.clauses)}\n")
            for c in self.clauses:
                f.write(" ".join(map(str, c)) + " 0\n")


def build(m: int, path: Path) -> None:
    n = 2 * m + 1
    cnf = Cnf()
    incoming: dict[int, list[int]] = collections.defaultdict(list)
    outgoing: dict[int, list[int]] = collections.defaultdict(list)
    by_lower: dict[int, list[int]] = collections.defaultdict(list)
    edge_vars: list[int] = []
    edges: list[tuple[int, int, int, int, int]] = []
    for a in masks(n, m + 1):
        mate, fz = matching(a, n)
        if not fz:
            continue
        p = fz[-1]
        for q in range(n):
            if not ((a >> q) & 1):
                continue
            if q in mate and mate[q] != q + 1:
                continue
            b = a ^ (1 << p) ^ (1 << q)
            lower = a ^ (1 << q)
            x = cnf.var()
            edges.append((x, a, b, lower, q))
            edge_vars.append(x)
            outgoing[a].append(x)
            incoming[b].append(x)
            by_lower[lower].append(x)
    vertices = set(incoming) | set(outgoing)
    for v in vertices:
        ins = incoming[v]
        outs = outgoing[v]
        cnf.at_most_one(ins)
        cnf.at_most_one(outs)
        if outs:
            for x in ins:
                cnf.clauses.append([-x] + outs)
        else:
            for x in ins:
                cnf.clauses.append([-x])
        if ins:
            for x in outs:
                cnf.clauses.append([-x] + ins)
        else:
            for x in outs:
                cnf.clauses.append([-x])
    for xs in by_lower.values():
        cnf.at_most_one(xs)
    cnf.clauses.append(edge_vars)
    cnf.write(path)
    map_path = path.with_suffix(path.suffix + ".map")
    with map_path.open("w") as f:
        for row in edges:
            f.write(" ".join(map(str, row)) + "\n")
    print({"m": m, "vertices": len(vertices), "edges": len(edges),
           "lowers": len(by_lower), "vars": cnf.nvars,
           "clauses": len(cnf.clauses), "cnf": str(path)})


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("cnf", type=Path)
    args = ap.parse_args()
    build(args.m, args.cnf)
