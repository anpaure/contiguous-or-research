#!/usr/bin/env python3
"""Verify the inverse Dyck normal form for fixed-GK leaf options.

Run on H100 only.
"""

from __future__ import annotations

import argparse
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


def direct(m):
    n=2*m+1;ans=set()
    for u in masks(n,m+2):
        mu,fu=matching(u,n);p=next(i for i in fu if u>>i&1);a=u^(1<<p);ma,fa=matching(a,n)
        for q in range(n):
            if a>>q&1 and (q not in ma or ma[q]==q+1):
                ans.add((a^(1<<q),p,q))
    return ans


def inverse(m):
    n=2*m+1;ans=set()
    for l in masks(n,m):
        ml,fl=matching(l,n);fz=[i for i in fl if not(l>>i&1)]
        h=[];s=0
        for i in range(n):
            s += 1 if l>>i&1 else -1;h.append(s)
        suff=[0]*n;smin=10*n
        for i in range(n-1,-1,-1):smin=min(smin,h[i]);suff[i]=smin
        for t in range(min(3,len(fz))):
            p=fz[-1-t]
            for q in range(n):
                if q==p:continue
                if l>>q&1:continue
                a=l^(1<<q)
                ma,fa=matching(a,n)
                u=a^(1<<p)
                mu,fu=matching(u,n)
                if p != next((z for z in fu if u>>z&1),-1):continue
                free_after_flip=q not in ma
                adjacent_peak_after_flip=(q+1<n and not(l>>(q+1)&1))
                if free_after_flip or adjacent_peak_after_flip:ans.add((l,p,q))
    return ans


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('ms',nargs='+',type=int);a=ap.parse_args()
    for m in a.ms:
        d=direct(m);i=inverse(m);assert d==i,(m,len(d-i),len(i-d))
        dr={x for x in d if x[2]>x[1]}
        print('PASS','m',m,'leaf',len(d),'leaf_right',len(dr))
