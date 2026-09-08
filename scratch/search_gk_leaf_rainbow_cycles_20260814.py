#!/usr/bin/env python3
"""SAT search for a directed fixed-GK leaf cycle with distinct lower labels.

Run only on H100.  A satisfying assignment is a disjoint union of directed
cycles, uses every vertex at most once as head/tail, and uses each lower label
at most once.  Thus SAT iff the leaf host contains a lower-rainbow cycle.
"""

from __future__ import annotations

import argparse
import collections
import itertools

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


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


def edges(m: int):
    n = 2 * m + 1
    ans = []
    for a in masks(n, m + 1):
        mate, free = matching(a, n)
        fz = [i for i in free if not ((a >> i) & 1)]
        if not fz:
            continue
        p = fz[-1]
        for q in range(n):
            if (a >> q) & 1 and (q not in mate or mate[q] == q + 1):
                b = a ^ (1 << p) ^ (1 << q)
                lower = a ^ (1 << q)
                ans.append((a, b, lower, p, q))
    return ans


def bits(x: int, n: int):
    return ''.join('1' if (x >> i) & 1 else '0' for i in range(n))


def solve(m: int):
    es = edges(m)
    n = 2 * m + 1
    pool = IDPool()
    ev = [pool.id(('e', i)) for i in range(len(es))]
    out = collections.defaultdict(list)
    inc = collections.defaultdict(list)
    by_lower = collections.defaultdict(list)
    for i, (a, b, lower, p, q) in enumerate(es):
        out[a].append(ev[i])
        inc[b].append(ev[i])
        by_lower[lower].append(ev[i])
    cnf = CNF()

    def atmost1(vs):
        if len(vs) > 1:
            cnf.extend(CardEnc.atmost(vs, 1, vpool=pool, encoding=EncType.seqcounter).clauses)

    vertices = set(out) | set(inc)
    for v in vertices:
        atmost1(out[v])
        atmost1(inc[v])
        # Conservation after the at-most-one constraints.
        for e in out[v]:
            cnf.append([-e] + inc[v])
        for e in inc[v]:
            cnf.append([-e] + out[v])
    for vs in by_lower.values():
        atmost1(vs)
    cnf.append(ev[:])
    print('INSTANCE', m, 'vertices', len(vertices), 'edges', len(es),
          'lowers', len(by_lower), 'vars', pool.top, 'clauses', len(cnf.clauses), flush=True)
    with Solver(name='cadical195', bootstrap_with=cnf) as solver:
        sat = solver.solve()
        print('RESULT', m, 'SAT' if sat else 'UNSAT', flush=True)
        if not sat:
            return
        model = set(x for x in solver.get_model() if x > 0)
    chosen = [es[i] for i, x in enumerate(ev) if x in model]
    nxt = {a: (b, lower, p, q) for a, b, lower, p, q in chosen}
    start = next(iter(nxt))
    cyc = []
    seen = {}
    a = start
    while a not in seen:
        seen[a] = len(cyc)
        row = nxt[a]
        cyc.append((a,) + row)
        a = row[0]
    cyc = cyc[seen[a]:]
    print('CYCLE_LEN', len(cyc))
    for a, b, lower, p, q in cyc:
        print(bits(a, n), '->', bits(b, n), 'lower', bits(lower, n), 'p', p, 'q', q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ms', nargs='+', type=int)
    args = ap.parse_args()
    for m in args.ms:
        solve(m)


if __name__ == '__main__':
    main()
