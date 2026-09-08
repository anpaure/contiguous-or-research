#!/usr/bin/env python3
"""Describe the leaf choices in fixed-GK selector certificates."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def matching(x: int, n: int):
    st: list[int] = []
    mate: dict[int, int] = {}
    depth_before: dict[int, int] = {}
    depth = 0
    for i in range(n):
        depth_before[i] = depth
        if (x >> i) & 1:
            st.append(i)
            depth += 1
        elif st:
            j = st.pop()
            mate[i] = j
            mate[j] = i
            depth -= 1
        else:
            depth -= 1
    return mate, depth_before


def audit(path: Path) -> None:
    data = json.loads(path.read_text())
    m, n = data["m"], data["n"]
    counters: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    examples = collections.defaultdict(list)
    for r in data["chosen"]:
        a, p, q = r["a"], r["p"], r["q"]
        mate, depth = matching(a, n)
        leaves = [i for i in range(n) if (a >> i) & 1 and
                  (i not in mate or mate[i] == i + 1)]
        inc = sorted(leaves)
        cyc = sorted(leaves, key=lambda x: (x - p) % n)
        right = [x for x in inc if x > p]
        left = [x for x in inc if x < p]
        kind = "free" if q not in mate else "peak"
        side = "right" if q > p else "left"
        counters["kind_side"][(kind, side)] += 1
        counters["inc_rank"][inc.index(q)] += 1
        counters["inc_reverse_rank"][len(inc) - 1 - inc.index(q)] += 1
        counters["cyc_rank"][cyc.index(q)] += 1
        if q > p:
            counters["side_rank"][right.index(q)] += 1
            counters["side_reverse_rank"][len(right) - 1 - right.index(q)] += 1
        else:
            counters["side_rank"][left.index(q)] += 1
            counters["side_reverse_rank"][len(left) - 1 - left.index(q)] += 1
        counters["leaf_count"][len(leaves)] += 1
        counters["q_depth"][depth[q]] += 1
        if kind == "peak":
            counters["peak_height"][depth[q]] += 1
        key = (kind, side, depth[q], len(leaves), cyc.index(q))
        if len(examples[key]) < 2:
            examples[key].append((format(a, f"0{n}b")[::-1], p, q))
    print("m", m)
    for name in sorted(counters):
        print(name, sorted(counters[name].items()))
    print("left_examples")
    shown = 0
    for key in sorted(examples):
        if key[1] == "left" and shown < 30:
            print(key, examples[key])
            shown += 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", type=Path, nargs="+")
    args = ap.parse_args()
    for p in args.paths:
        audit(p)
