#!/usr/bin/env python3
"""H100-only test of explicit primitive-fiber collision repairs."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = sum(1 << i for i in c)
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
    free = [i for i in range(n) if i not in mate]
    return mate, free


def central_primitive_closers(b: int, n: int):
    mate, free = matching(b, n)
    fz = [i for i in free if not ((b >> i) & 1)]
    fo = [i for i in free if (b >> i) & 1]
    lo = fz[-1] if fz else -1
    hi = fo[0] if fo else n
    depth = 0
    closers: list[int] = []
    for i in range(lo + 1, hi):
        if (b >> i) & 1:
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                closers.append(i)
        assert depth >= 0
    assert depth == 0
    return closers


def choose(rule: str, u: int, n: int):
    _, free = matching(u, n)
    ones = [i for i in free if (u >> i) & 1]
    assert len(ones) >= 3
    p, q2, q3 = ones[:3]
    b0 = u ^ (1 << q2)
    closers = central_primitive_closers(b0, n)
    idx = closers.index(q2)
    k = len(closers)
    if rule == "last_keeps":
        q = q2 if idx == k - 1 else q3
    elif rule == "first_keeps":
        q = q2 if idx == 0 else q3
    elif rule == "parity":
        q = q2 if idx % 2 == 0 else q3
    elif rule == "reverse_parity":
        q = q2 if idx % 2 else q3
    else:
        raise ValueError(rule)
    a = u ^ (1 << p)
    l = a ^ (1 << q)
    b = l ^ (1 << p)
    ma, _ = matching(a, n)
    assert q > p and (q not in ma or ma[q] == q + 1)
    return p, q, a, l, b, idx, k


def audit(m: int):
    n = 2 * m + 1
    for rule in ("last_keeps", "first_keeps", "parity", "reverse_parity"):
        by_l = collections.Counter()
        by_b = collections.Counter()
        rows = []
        for u in masks(n, m + 2):
            row = choose(rule, u, n)
            by_l[row[3]] += 1
            by_b[row[4]] += 1
            rows.append(row)
        print(
            "REPAIR", m, rule,
            "rows", len(rows),
            "L_image", len(by_l),
            "B_image", len(by_b),
            "L_def", len(rows) - len(by_l),
            "B_def", len(rows) - len(by_b),
            "L_max", max(by_l.values()),
            "B_max", max(by_b.values()),
        )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=10)
    args = ap.parse_args()
    for m in range(2, args.max_m + 1):
        audit(m)


if __name__ == "__main__":
    main()
