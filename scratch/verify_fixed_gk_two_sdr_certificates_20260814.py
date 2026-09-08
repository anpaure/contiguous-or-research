#!/usr/bin/env python3
"""Independent verifier for fixed-GK two-SDR certificates."""

from __future__ import annotations

import argparse, collections, itertools, json
from pathlib import Path


def masks(n,r):
    for c in itertools.combinations(range(n),r):
        x=0
        for i in c:x|=1<<i
        yield x


def matching(x,n):
    st=[];mate={}
    for i in range(n):
        if (x>>i)&1:st.append(i)
        elif st:
            j=st.pop();mate[i]=j;mate[j]=i
    free=[i for i in range(n) if i not in mate]
    return mate,free


def verify(path:Path):
    d=json.loads(path.read_text());m=d['m'];n=d['n'];chosen=d['chosen']
    upper_all=set(masks(n,m+2)); owners_all=set(masks(n,m+1))
    assert len(chosen)==len(upper_all)
    us=set();ls=set();aa=set();bb=set();adj=collections.defaultdict(set);edge_set=set()
    for r in chosen:
        u,p,q,a,b,l=(r[k] for k in ('upper','p','q','a','b','lower'))
        assert u in upper_all and p!=q and ((u>>p)&1) and ((u>>q)&1)
        mu,fu=matching(u,n); assert p==next(i for i in fu if (u>>i)&1)
        assert a==u^(1<<p) and b==u^(1<<q) and l==u^(1<<p)^(1<<q)
        ma,fa=matching(a,n); assert q not in ma or ma[q]==q+1
        us.add(u);ls.add(l);aa.add(a);bb.add(b)
        assert a!=b
        e=tuple(sorted((a,b))); assert e not in edge_set;edge_set.add(e)
        adj[a].add(b);adj[b].add(a)
    assert us==upper_all and len(ls)==len(chosen) and len(aa)==len(chosen) and len(bb)==len(chosen)
    assert max(map(len,adj.values()),default=0)<=2
    seen=set();cycles=0;comps=0
    for v in owners_all:
        if v in seen: continue
        comps+=1;stack=[(v,-1)];seen.add(v);ec=0;vc=0
        while stack:
            x,parent=stack.pop();vc+=1;ec+=len(adj[x])
            for y in adj[x]:
                if y==parent:continue
                if y in seen:cycles+=1
                else:seen.add(y);stack.append((y,x))
        # Each undirected cycle is detected twice in this DFS convention.
    cycles//=2
    expected=len(owners_all)-len(chosen)
    assert comps>=expected
    print('PASS',path,'m',m,'edges',len(chosen),'components',comps,
          'expected_if_forest',expected,'cycle_rank',len(chosen)-len(owners_all)+comps,
          'backedge_cycles',cycles,'q_lt_p',sum(r['q']<r['p'] for r in chosen))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('paths',nargs='+',type=Path);a=ap.parse_args()
    for p in a.paths:verify(p)
