#!/usr/bin/env python3
"""Analyze H100 SAT certificates for the fixed-GK upper selector."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def matching(mask: int, n: int):
    stack = []
    mate = {}
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    free = [i for i in range(n) if i not in mate]
    return mate, free


def main(path: Path):
    data = json.loads(path.read_text())
    n = data["n"]
    stats = collections.Counter()
    distances = collections.Counter()
    pair_spans = collections.Counter()
    leaf_ranks = collections.Counter()
    leaf_ranks_after_p = collections.Counter()
    for r in data["chosen"]:
        a, p, q = r["a"], r["p"], r["q"]
        mate, free = matching(a, n)
        free_ones = [i for i in free if (a >> i) & 1]
        if q in free_ones:
            stats[("free1", free_ones.index(q), len(free_ones))] += 1
        elif q in mate:
            stats[("paired1", int(mate[q] < q))] += 1
            pair_spans[abs(q - mate[q])] += 1
            leaves = [i for i in range(n) if ((a >> i) & 1) and (i not in mate or mate[i] == i + 1)]
            leaf_ranks[(leaves.index(q), len(leaves))] += 1
            after = [i for i in leaves if i > p]
            if q in after:
                leaf_ranks_after_p[(after.index(q), len(after))] += 1
        else:
            stats[("other",)] += 1
        distances[(q - p) % n] += 1
    print("m", data["m"], "chosen", len(data["chosen"]))
    print("stats", sorted(stats.items(), key=lambda z: (-z[1], z[0])))
    print("cyclic_dist", sorted(distances.items()))
    print("pair_span", sorted(pair_spans.items()))
    print("leaf_ranks", sorted(leaf_ranks.items(), key=lambda z: (-z[1], z[0])))
    print("leaf_ranks_after_p", sorted(leaf_ranks_after_p.items(), key=lambda z: (-z[1], z[0])))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("paths", nargs="+", type=Path); a=ap.parse_args()
    for path in a.paths: main(path)
