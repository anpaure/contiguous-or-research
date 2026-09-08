#!/usr/bin/env python3
"""H100-only diagnostic for canonical fixed-GK leaf-right selectors.

This does not search for a selector.  It tests a short list of explicit
choices in order to expose the exact collision relation that an all-m proof
must repair.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import math


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
    free = [i for i in range(n) if i not in mate]
    return mate, free


def rows(m: int):
    n = 2 * m + 1
    for u in masks(n, m + 2):
        mu, fu = matching(u, n)
        free_ones_u = [i for i in fu if (u >> i) & 1]
        p = free_ones_u[0]
        a = u ^ (1 << p)
        ma, fa = matching(a, n)
        leaves = [
            q for q in range(n)
            if q > p and ((a >> q) & 1) and (q not in ma or ma[q] == q + 1)
        ]
        free_leaves = [q for q in leaves if q not in ma]
        assert free_leaves
        choices = {
            "first_free": free_leaves[0],
            "last_free": free_leaves[-1],
            "leftmost_leaf": leaves[0],
            "rightmost_leaf": leaves[-1],
        }
        for name, q in choices.items():
            l = a ^ (1 << q)
            b = l ^ (1 << p)
            yield name, u, p, q, a, l, b


def primitive_closers_before_first_free_one(b: int, n: int):
    """Closing zeros of ground-level primitives before the first free one."""
    mate, free = matching(b, n)
    free_ones = [i for i in free if (b >> i) & 1]
    stop = free_ones[0] if free_ones else n
    return [q for q in range(stop) if not ((b >> q) & 1) and q in mate]


def audit(m: int):
    n = 2 * m + 1
    by_rule = collections.defaultdict(list)
    for row in rows(m):
        by_rule[row[0]].append(row)
    for name, rs in sorted(by_rule.items()):
        by_l = collections.defaultdict(list)
        by_b = collections.defaultdict(list)
        for r in rs:
            by_l[r[5]].append(r)
            by_b[r[6]].append(r)
        l_hist = collections.Counter(map(len, by_l.values()))
        b_hist = collections.Counter(map(len, by_b.values()))
        print(
            "RULE", m, name,
            "rows", len(rs),
            "L_unique", int(max(l_hist) == 1),
            "B_unique", int(max(b_hist) == 1),
            "L_max", max(l_hist),
            "B_max", max(b_hist),
            "L_hist", sorted(l_hist.items()),
            "B_hist", sorted(b_hist.items()),
        )
        if name == "first_free":
            assert max(l_hist) == 1
            expected = {
                k: math.comb(2 * m - k, m - k)
                for k in range(1, m + 1)
            }
            assert dict(b_hist) == expected
            assert len(by_b) == math.comb(2 * m, m - 1)
            assert len(rs) - len(by_b) == math.comb(2 * m, m - 2)
            bad = [(b, rr) for b, rr in by_b.items() if len(rr) > 1]
            if bad:
                b, rr = min(bad, key=lambda z: (len(z[1]), z[0]))
                qs = sorted(r[3] for r in rr)
                print(
                    "FIRST_FREE_COLLISION", m,
                    format(b, f"0{n}b")[::-1],
                    "mult", len(rr),
                    "q", qs,
                    "primitive_closers", primitive_closers_before_first_free_one(b, n),
                )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=10)
    args = ap.parse_args()
    for m in range(2, args.max_m + 1):
        audit(m)


if __name__ == "__main__":
    main()
