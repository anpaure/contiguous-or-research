#!/usr/bin/env python3
"""Classify the at-most-three inverse leaf options incident with a lower mask."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def matching(x: int, n: int):
    st: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (x >> i) & 1:
            st.append(i)
        elif st:
            j = st.pop()
            mate[i] = j
            mate[j] = i
    fz = [i for i in range(n) if not ((x >> i) & 1) and i not in mate]
    fo = [i for i in range(n) if ((x >> i) & 1) and i not in mate]
    return mate, fz, fo


def audit(m: int) -> None:
    n = 2 * m + 1
    by_l: dict[int, list[tuple]] = collections.defaultdict(list)
    for a in masks(n, m + 1):
        ma, fza, foa = matching(a, n)
        if not fza:
            continue
        p = fza[-1]
        for q in range(n):
            if not ((a >> q) & 1):
                continue
            if q in ma and ma[q] != q + 1:
                continue
            l = a ^ (1 << q)
            ml, fzl, fol = matching(l, n)
            def pos(seq, x):
                return seq.index(x) if x in seq else -1
            by_l[l].append((p, q, "F" if q not in ma else "P",
                            tuple(fzl), tuple(fol), pos(fzl, p), pos(fzl, q),
                            ma.get(q, -1)))

    pattern_hist = collections.Counter()
    degree_hist = collections.Counter(map(len, by_l.values()))
    samples: dict[tuple, tuple] = {}
    for l, opts in by_l.items():
        key = tuple(sorted((typ, pp, qp,
                            (p > q),
                            len(fz), len(fo),
                            (p == fz[-1] if fz else False),
                            (q == fz[-1] if fz else False),
                            mateq - q)
                           for p, q, typ, fz, fo, pp, qp, mateq in opts))
        pattern_hist[key] += 1
        samples.setdefault(key, (format(l, f"0{n}b")[::-1], opts))
    print("m", m, "lowers", len(by_l), "degree_hist", sorted(degree_hist.items()),
          "patterns", len(pattern_hist))
    for key, cnt in pattern_hist.most_common(30):
        print("pattern", cnt, key, "sample", samples[key])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int, nargs="+")
    args = ap.parse_args()
    for m in args.m:
        audit(m)
