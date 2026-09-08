#!/usr/bin/env python3
"""Analyze the t=0,1,2 fixed-GK lower-to-owner chart overlaps (H100 only)."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n,r):
    for c in itertools.combinations(range(n),r):
        yield sum(1<<i for i in c)


def matching(x,n):
    st=[];ma={}
    for i in range(n):
        if x>>i&1:st.append(i)
        elif st:
            j=st.pop();ma[i]=j;ma[j]=i
    return ma,[i for i in range(n) if i not in ma]


def charts(m):
    n=2*m+1;ans={0:{},1:{},2:{}}
    for l in masks(n,m):
        ml,fl=matching(l,n);fz=[i for i in fl if not(l>>i&1)]
        for t in range(min(3,len(fz))):
            p=fz[-1-t];ans[t][l]=l^(1<<p)
    return ans


def audit(m):
    n=2*m+1;cs=charts(m);owners=set(masks(n,m+1))
    for t,c in cs.items():
        vals=collections.Counter(c.values())
        print('CHART',m,t,'domain',len(c),'image',len(vals),'injective',max(vals.values(),default=0)==1,
              'owner_complement',len(owners-set(vals)))
    # Directed overlap: l --t--> owner == l' --s--> owner.
    for ts in ((0,1),(0,2),(1,2)):
        inv={t:{b:l for l,b in cs[t].items()} for t in ts}
        overlap=set(inv[ts[0]])&set(inv[ts[1]])
        arcs=[]
        for b in overlap:arcs.append((inv[ts[0]][b],inv[ts[1]][b]))
        adj=collections.defaultdict(set)
        for x,y in arcs:adj[x].add(y);adj[y].add(x)
        deg=collections.Counter(map(len,adj.values()))
        seen=set();cyc=0;comps=0;maxcomp=0
        for v in adj:
            if v in seen:continue
            comps+=1;stack=[v];seen.add(v);vc=0;ec=0
            while stack:
                x=stack.pop();vc+=1;ec+=len(adj[x])
                for y in adj[x]:
                    if y not in seen:seen.add(y);stack.append(y)
            ec//=2;cyc += ec-vc+1;maxcomp=max(maxcomp,vc)
        print('OVERLAP',m,ts,'arcs',len(arcs),'vertices',len(adj),'deg',sorted(deg.items()),
              'components',comps,'cycle_rank',cyc,'maxcomp',maxcomp)
    # Reindex every nonzero chart head through the bijective chart 0.
    inv0={b:l for l,b in cs[0].items()}
    for t in (1,2):
        arcs=[(l,inv0[b]) for l,b in cs[t].items()]
        assert all(x!=y for x,y in arcs)
        indeg=collections.Counter(y for x,y in arcs)
        outdeg=collections.Counter(x for x,y in arcs)
        adj=collections.defaultdict(set)
        for x,y in arcs:adj[x].add(y);adj[y].add(x)
        seen=set();cyc=0;comps=0;maxcomp=0
        for v in adj:
            if v in seen:continue
            comps+=1;stack=[v];seen.add(v);vc=0;ec=0
            while stack:
                x=stack.pop();vc+=1;ec+=len(adj[x])
                for y in adj[x]:
                    if y not in seen:seen.add(y);stack.append(y)
            ec//=2;cyc+=ec-vc+1;maxcomp=max(maxcomp,vc)
        print('FUNCTION',m,t,'arcs',len(arcs),'vertices',len(adj),
              'in_hist',sorted(collections.Counter(indeg.values()).items()),
              'max_in',max(indeg.values(),default=0),'max_out',max(outdeg.values(),default=0),
              'components',comps,'cycle_rank',cyc,'maxcomp',maxcomp)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('ms',nargs='+',type=int);a=ap.parse_args()
    for m in a.ms:audit(m)
