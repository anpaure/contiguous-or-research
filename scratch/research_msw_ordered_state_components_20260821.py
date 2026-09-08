#!/usr/bin/env python3
"""Ordered de-Bruijn state components of the canonical MSW factor.

Reads dump_msw_orders output.  The stored convention takes rank-b intervals
with step two, so the actual row is q[2i].  We join rows sharing an oriented
ordered (b-1)-tuple.  Research-only; run on H100.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import argparse
import sys


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.p[y] = x


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    b = args.b
    n = 2 * b + 1
    rows: list[tuple[int, ...]] = []
    for line in sys.stdin:
        if not line.strip():
            continue
        stored = [int(x) - 1 for x in line.split()]
        rows.append(tuple(stored[(2 * i) % n] for i in range(n)))
    dsu = DSU(len(rows))
    owners: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for rid, row in enumerate(rows):
        for start in range(n):
            state = tuple(row[(start + j) % n] for j in range(b - 1))
            owners[state].append(rid)
    mult = Counter(len(v) for v in owners.values())
    excess = 0
    for vv in owners.values():
        excess += len(vv) - 1
        for rid in vv[1:]:
            dsu.union(vv[0], rid)
    comp = Counter(dsu.find(i) for i in range(len(rows)))
    print(
        "MSW_ORDERED_COMPONENTS",
        "B",
        b,
        "ROWS",
        len(rows),
        "STATES",
        len(owners),
        "MULT_HIST",
        sorted(mult.items()),
        "EXCESS",
        excess,
        "COMPONENTS",
        len(comp),
        "COMP_SIZES",
        sorted(comp.values(), reverse=True)[:50],
        "COMP_FRACTION",
        len(comp) / max(1, len(rows)),
    )


if __name__ == "__main__":
    main()
