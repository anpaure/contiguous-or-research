#!/usr/bin/env python3
"""Exact finite audit for fixed-GK leaf selector structure.

This script is designed to run on H100 only.  It checks the structural
lemmas used in the accompanying reduction, finite SAT certificates, and
the smallest cycle counterexamples.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
from pathlib import Path


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


def options(m: int, right: bool = False):
    n = 2 * m + 1
    for u in masks(n, m + 2):
        mu, fu = matching(u, n)
        p = next(i for i in fu if (u >> i) & 1)
        a = u ^ (1 << p)
        ma, fa = matching(a, n)
        fz = [i for i in fa if not ((a >> i) & 1)]
        assert p == fz[-1]
        for q in range(n):
            if not ((a >> q) & 1):
                continue
            if not (q not in ma or ma[q] == q + 1):
                continue
            if right and not q > p:
                continue
            l = a ^ (1 << q)
            b = l ^ (1 << p)
            yield dict(upper=u, p=p, q=q, a=a, b=b, lower=l)


def verify_cert(path: Path, require_right: bool):
    d = json.loads(path.read_text())
    m, n, rows = d['m'], d['n'], d['chosen']
    assert n == 2*m+1
    expected = set(masks(n, m+2))
    us = set(); aa = set(); bb = set(); ll = set()
    edges = set(); adj = collections.defaultdict(set)
    for r in rows:
        u,p,q,a,b,l = (r[k] for k in ('upper','p','q','a','b','lower'))
        mu,fu=matching(u,n); assert p == next(i for i in fu if (u>>i)&1)
        ma,fa=matching(a,n)
        assert q not in ma or ma[q] == q+1
        if require_right: assert q > p
        assert a == u^(1<<p) and l == a^(1<<q) and b == l^(1<<p)
        assert u not in us and a not in aa and b not in bb and l not in ll
        e=tuple(sorted((a,b))); assert e not in edges
        us.add(u);aa.add(a);bb.add(b);ll.add(l);edges.add(e)
        adj[a].add(b);adj[b].add(a)
    assert us == expected
    assert max(map(len,adj.values()),default=0) <= 2
    if require_right:
        # The directed selected edges a->b strictly decrease coordinate sum,
        # hence no directed cycle; degree <=2 then excludes undirected cycles.
        assert all(sum(i for i in range(n) if (r['b']>>i)&1) <
                   sum(i for i in range(n) if (r['a']>>i)&1) for r in rows)
    seen=set(); comps=0
    for v in masks(n,m+1):
        if v in seen: continue
        comps += 1; stack=[(v,-1)];seen.add(v);ec=0;vc=0
        while stack:
            x,parent=stack.pop();vc+=1;ec+=len(adj[x])
            for y in adj[x]:
                if y==parent:continue
                assert y not in seen
                seen.add(y);stack.append((y,x))
        assert ec//2 == vc-1
    assert comps == len(list(masks(n,m+1))) - len(rows)
    print('CERT_PASS',path,'m',m,'right',int(require_right),'edges',len(rows),'components',comps)


def verify_structure(m: int):
    n=2*m+1
    rows=list(options(m,False)); rr=[r for r in rows if r['q']>r['p']]
    expected=set(masks(n,m+2)); images={r['a'] for r in rows}
    assert {r['upper'] for r in rows} == expected
    assert len(images)==len(expected)
    by_l=collections.defaultdict(list); by_lr=collections.defaultdict(list)
    for r in rows: by_l[r['lower']].append(r)
    for r in rr: by_lr[r['lower']].append(r)
    raw=max(map(len,by_l.values())); rawr=max(map(len,by_lr.values()))
    heads=max(len({r['b'] for r in rs}) for rs in by_l.values())
    headsr=max(len({r['b'] for r in rs}) for rs in by_lr.values())
    types=set()
    for l,rs in by_l.items():
        ml,fl=matching(l,n);fz=[i for i in fl if not ((l>>i)&1)]
        for r in rs:
            t=len(fz)-1-fz.index(r['p'])
            assert t in (0,1,2)
            assert r['b'] == l^(1<<fz[-1-t])
            types.add(t)
    assert raw == m+1 and rawr == m
    assert heads <= 3 and headsr <= 3
    assert all(r['q']>r['p'] and
               sum(i for i in range(n) if (r['b']>>i)&1) <
               sum(i for i in range(n) if (r['a']>>i)&1) for r in rr)
    print('STRUCTURE_PASS','m',m,'options',len(rows),'right_options',len(rr),
          'raw_lower_max',raw,'right_raw_lower_max',rawr,
          'distinct_head_max',heads,'right_distinct_head_max',headsr,
          'inverse_types',sorted(types))


def verify_cycle_examples():
    examples = {
        2: ['01011','10011','00111'],
        3: ['1100011','1000111','0001111','0011011','0110011'],
    }
    for m, words in examples.items():
        n=2*m+1; host={(r['a'],r['b']):r for r in options(m,False)}
        cyc=[sum((ch=='1')<<i for i,ch in enumerate(w)) for w in words]
        rows=[]
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            assert (a,b) in host;rows.append(host[(a,b)])
        if m==3: assert len({r['lower'] for r in rows})==len(rows)
        print('CYCLE_PASS','m',m,'length',len(rows),'lower_rainbow',len({r['lower'] for r in rows})==len(rows))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-m',type=int,default=9)
    ap.add_argument('--leaf-certs',nargs='*',type=Path,default=[])
    ap.add_argument('--right-certs',nargs='*',type=Path,default=[])
    a=ap.parse_args()
    for m in range(2,a.max_m+1):verify_structure(m)
    verify_cycle_examples()
    for p in a.leaf_certs:verify_cert(p,False)
    for p in a.right_certs:verify_cert(p,True)


if __name__=='__main__':main()
