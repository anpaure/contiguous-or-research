#!/usr/bin/env python3
"""Search simple monotone statistics for all fixed-GK leaf rotations."""

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


def stats(x,n):
    ma,fr=matching(x,n)
    zeros=[i for i in fr if not ((x>>i)&1)]; ones=[i for i in fr if (x>>i)&1]
    s=0;pref=[]
    for i in range(n):
        s += 1 if (x>>i)&1 else -1;pref.append(s)
    return (len(zeros), tuple(zeros), tuple(ones), min(pref), sum(pref), sum(i for i in range(n) if (x>>i)&1))


def audit(m):
    n=2*m+1; changes=collections.Counter(); examples={}
    sign_counts=[collections.Counter() for _ in range(6)]
    for u in masks(n,m+2):
        mu,fu=matching(u,n);p=next(i for i in fu if (u>>i)&1);a=u^(1<<p)
        ma,fa=matching(a,n)
        sa=stats(a,n)
        for q in range(n):
            if (a>>q)&1 and (q not in ma or ma[q]==q+1):
                b=a^(1<<q)^(1<<p);sb=stats(b,n)
                kind=('free' if q not in ma else 'peak', 'left' if q<p else 'right')
                delta=(sb[0]-sa[0],sb[3]-sa[3],sb[4]-sa[4],sb[5]-sa[5])
                changes[(kind,delta)]+=1;examples.setdefault((kind,delta),(u,a,b,p,q,sa,sb))
                vals=[sb[0]-sa[0], (sb[1]>sa[1])-(sb[1]<sa[1]), (sb[2]>sa[2])-(sb[2]<sa[2]), sb[3]-sa[3], sb[4]-sa[4], sb[5]-sa[5]]
                for i,v in enumerate(vals):sign_counts[i][(v>0)-(v<0)]+=1
    print('m',m,'changes',sorted(changes.items()))
    print('sign_counts',sign_counts)
    for k,v in sorted(examples.items()): print('example',k,v)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('m',nargs='+',type=int);a=ap.parse_args()
    for m in a.m:audit(m)
