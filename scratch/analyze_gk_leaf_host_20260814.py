#!/usr/bin/env python3
"""Analyze the fixed-GK leaf-option owner digraph and saved certificates.

Run on H100 only.  This is exploratory; exact claims are separately verified.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import sys
from pathlib import Path

sys.setrecursionlimit(1_000_000)


def masks(n: int, r: int):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def matching(x: int, n: int):
    stack = []
    mate = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    free = [i for i in range(n) if i not in mate]
    return mate, free


def owner_data(a: int, n: int):
    mate, free = matching(a, n)
    free_zero = [i for i in free if not ((a >> i) & 1)]
    free_one = [i for i in free if (a >> i) & 1]
    if not free_zero:
        return None
    p = free_zero[-1]
    leaves = [q for q in range(n) if (a >> q) & 1 and (q not in mate or mate[q] == q + 1)]
    return p, leaves, free_zero, free_one, mate


def tarjan(vertices, out):
    index = 0
    stack = []
    onstack = set()
    indices = {}
    low = {}
    comps = []

    def visit(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in out.get(v, ()): 
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(comp)

    for v in vertices:
        if v not in indices:
            visit(v)
    return comps


def bits(x: int, n: int):
    return ''.join('1' if (x >> i) & 1 else '0' for i in range(n))


def inv(x: int, n: int):
    # Number of 0-before-1 pairs in the displayed left-to-right word.
    zeros = 0
    ans = 0
    for i in range(n):
        if (x >> i) & 1:
            ans += zeros
        else:
            zeros += 1
    return ans


def prefix_min(x: int, n: int):
    s = 0
    mn = 0
    for i in range(n):
        s += 1 if (x >> i) & 1 else -1
        mn = min(mn, s)
    return mn


def analyze_m(m: int):
    n = 2 * m + 1
    vertices = list(masks(n, m + 1))
    out = collections.defaultdict(list)
    edge_meta = {}
    roots = []
    leaf_hist = collections.Counter()
    deltas = collections.defaultdict(collections.Counter)
    for a in vertices:
        data = owner_data(a, n)
        if data is None:
            roots.append(a)
            continue
        p, leaves, fz, fo, mate = data
        leaf_hist[(len(leaves), len(fz), len(fo))] += 1
        for q in leaves:
            b = a ^ (1 << p) ^ (1 << q)
            out[a].append(b)
            typ = 'free' if q not in mate else 'peak'
            edge_meta[(a, b)] = (p, q, typ)
            deltas[typ]['sum_sign_' + str((p > q) - (p < q))] += 1
            deltas[typ]['inv_' + str(inv(b, n) - inv(a, n))] += 1
            deltas[typ]['pmin_' + str(prefix_min(b, n) - prefix_min(a, n))] += 1
    comps = tarjan(vertices, out)
    cyclic = [c for c in comps if len(c) > 1 or (c and c[0] in out.get(c[0], ()))]
    print('HOST', m, 'n', n, 'V', len(vertices), 'roots', len(roots),
          'active', len(vertices) - len(roots), 'edges', sum(map(len, out.values())),
          'scc', len(comps), 'cyclic_scc', len(cyclic),
          'max_scc', max(map(len, cyclic), default=0))
    print('LEAF_HIST', sorted(leaf_hist.items()))
    print('DELTAS', {k: dict(v) for k, v in deltas.items()})
    if cyclic:
        cset = set(cyclic[0])
        start = cyclic[0][0]
        # Find one directed cycle inside the SCC.
        path = []
        pos = {}
        v = start
        while v not in pos:
            pos[v] = len(path)
            path.append(v)
            v = next(w for w in out[v] if w in cset)
        cyc = path[pos[v]:]
        print('CYCLE')
        for a in cyc:
            b = next(w for w in out[a] if w in cset)
            print(bits(a, n), '->', bits(b, n), edge_meta[(a, b)])
    return out, edge_meta


def analyze_cert(path: Path):
    d = json.loads(path.read_text())
    m = d['m']
    n = d['n']
    rows = d['chosen']
    hist = collections.Counter()
    for r in rows:
        a, p, q = r['a'], r['p'], r['q']
        mate, free = matching(a, n)
        typ = 'free' if q not in mate else 'peak'
        leaves = [z for z in range(n) if (a >> z) & 1 and (z not in mate or mate[z] == z + 1)]
        hist[(typ, leaves.index(q), len(leaves), (q > p) - (q < p))] += 1
    print('CERT', path, 'm', m, 'rows', len(rows), 'CHOICE_HIST', sorted(hist.items()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-m', type=int, default=7)
    ap.add_argument('--certs', nargs='*', type=Path, default=[])
    args = ap.parse_args()
    for m in range(1, args.max_m + 1):
        analyze_m(m)
    for path in args.certs:
        analyze_cert(path)


if __name__ == '__main__':
    main()
