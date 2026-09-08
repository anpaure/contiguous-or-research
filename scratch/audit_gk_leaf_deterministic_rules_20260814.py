#!/usr/bin/env python3
"""Audit simple deterministic leaf choices in the fixed-GK selector."""

from __future__ import annotations

import argparse, collections, itertools


def masks(n,r):
    for c in itertools.combinations(range(n),r):
        x=0
        for i in c:x|=1<<i
        yield x


def matching(x,n):
    st=[]; mate={}
    for i in range(n):
        if (x>>i)&1: st.append(i)
        elif st:
            j=st.pop();mate[i]=j;mate[j]=i
    free=[i for i in range(n) if i not in mate]
    return mate,free


def audit(m):
    n=2*m+1; us=list(masks(n,m+2))
    for origin in ('zero','p'):
      for direction in (1,-1):
       for rank in range(m+1):
        ls=collections.Counter();bs=collections.Counter();joint=collections.Counter();bad=0
        for u in us:
            mu,fu=matching(u,n); p=next(i for i in fu if (u>>i)&1); a=u^(1<<p)
            ma,fa=matching(a,n)
            leaves=[q for q in range(n) if (a>>q)&1 and (q not in ma or ma[q]==q+1)]
            start=0 if origin=='zero' else p
            leaves.sort(key=lambda q: direction*((q-start)%n))
            if rank>=len(leaves):bad+=1;continue
            q=leaves[rank];l=a^(1<<q);b=u^(1<<q)
            ls[l]+=1;bs[b]+=1;joint[a]+=1;joint[b]+=1
        print('m',m,'origin',origin,'dir',direction,'rank',rank,'bad',bad,
              'Lmax',max(ls.values(),default=0),'Ldup',sum(v-1 for v in ls.values()),
              'Bmax',max(bs.values(),default=0),'Bdup',sum(v-1 for v in bs.values()),
              'Omax',max(joint.values(),default=0))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('m',nargs='+',type=int);a=ap.parse_args()
    for m in a.m:audit(m)
