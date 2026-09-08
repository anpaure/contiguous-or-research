#!/usr/bin/env python3
"""Test context operations on canonical defect-one tail seams.

Research only; substantive execution is on H100.
"""

from __future__ import annotations

import argparse
from collections import Counter

from research_dyck_paired_phase_structure_20260821 import build_paths
from research_msw_c8_shadow_anneal_20260821 import dyck_words


def target(raw):
    return frozenset(i + 1 for i, bit in enumerate(raw) if bit == "1")


def raw(x, r):
    return "".join("1" if i in x else "0" for i in range(1, 2 * r + 1))


def defects(path, ground):
    count = Counter()
    for left, right in zip(path, path[1:]):
        if len(left ^ right) != 2:
            return None
        count.update(left ^ right)
    return sum(max(0, count[x] - 1) for x in ground)


def safe_seams(left, right, r, paths):
    ground = frozenset(range(1, 2 * r + 1))
    answer = []
    for t in range(1, r + 1):
        if (len(paths[left][t - 1] ^ paths[right][t]) != 2
                or len(paths[right][t - 1] ^ paths[left][t]) != 2):
            continue
        first = paths[left][:t] + paths[right][t:]
        second = paths[right][:t] + paths[left][t:]
        if defects(first, ground) == defects(second, ground) == 1:
            answer.append(t)
    return tuple(answer)


def mu(word):
    return word[::-1].translate(str.maketrans("01", "10"))


def audit(max_r):
    paths = {r: build_paths(r) for r in range(1, max_r + 2)}
    operation = Counter()
    failure = []
    primitive_leaf_merge = Counter()
    for r in range(1, max_r + 1):
        roots = tuple(paths[r])
        root_set = set(roots)
        for left in roots:
            for i in range(1, 2 * r):
                if i not in left or i + 1 in left:
                    continue
                right = frozenset((left - {i}) | {i + 1})
                if right not in root_set or tuple(left) >= tuple(right):
                    continue
                seams = safe_seams(left, right, r, paths[r])
                if not seams:
                    continue
                x, y = raw(left, r), raw(right, r)
                transforms = {
                    "prefix10": ("10" + x, "10" + y),
                    "suffix10": (x + "10", y + "10"),
                    "wrap": ("1" + x + "0", "1" + y + "0"),
                    "mu": (mu(x), mu(y)),
                }
                for name, (xx, yy) in transforms.items():
                    rr = r if name == "mu" else r + 1
                    a, b = target(xx), target(yy)
                    lifted = safe_seams(a, b, rr, paths[rr])
                    operation[(name, seams, lifted)] += 1
                    if not lifted:
                        failure.append((r, name, x, y, seams, xx, yy))
    for r in range(2, max_r + 2):
        for a in range(r - 1):
            b = r - 2 - a
            for U in dyck_words(a):
                for V in dyck_words(b):
                    nonprimitive = "1" + U + "01" + V + "0"
                    primitive = "1" + U + "10" + V + "0"
                    seams = safe_seams(
                        target(nonprimitive), target(primitive), r, paths[r]
                    )
                    primitive_leaf_merge[(r, a, b, seams)] += 1
    return {
        "max_r": max_r,
        "operation_hist": dict(operation),
        "failures": tuple(failure[:20]),
        "failure_count": len(failure),
        "primitive_leaf_merge": dict(primitive_leaf_merge),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=8)
    args = parser.parse_args()
    print("DYCK_SAFE_SEAM_CONTEXT_LIFTS", audit(args.max_r), flush=True)


if __name__ == "__main__":
    main()
