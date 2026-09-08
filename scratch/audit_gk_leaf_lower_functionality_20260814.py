#!/usr/bin/env python3
"""Check whether leaf options make B (or p) a function of lower L."""

from __future__ import annotations

import argparse, collections, itertools


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


def audit(m, right):
    n=2*m+1; by_l=collections.defaultdict(set); by_b=collections.defaultdict(set)
    for u in masks(n,m+2):
        mu,fu=matching(u,n);p=next(i for i in fu if (u>>i)&1);a=u^(1<<p)
        ma,fa=matching(a,n)
        for q in range(n):
            if (a>>q)&1 and (q not in ma or ma[q]==q+1) and (not right or q>p):
                l=a^(1<<q);b=u^(1<<q)
                by_l[l].add((b,p));by_b[b].add((l,p))
    print('m',m,'right',int(right),'Lhist',sorted(collections.Counter(map(len,by_l.values())).items()),
          'Bhist',sorted(collections.Counter(map(len,by_b.values())).items()),
          'L_functional',sum(len({b for b,p in s})==1 for s in by_l.values()),'of',len(by_l),
          'B_functional',sum(len({l for l,p in s})==1 for s in by_b.values()),'of',len(by_b))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('m',nargs='+',type=int);ap.add_argument('--right',action='store_true');a=ap.parse_args()
    for m in a.m:audit(m,a.right)
