#!/usr/bin/env python3
"""Audit the canonical second-free-one selector and inverse fibers (H100 only)."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n,r):
    for c in itertools.combinations(range(n),r):yield sum(1<<i for i in c)


def matching(x,n):
    st=[];ma={}
    for i in range(n):
        if x>>i&1:st.append(i)
        elif st:
            j=st.pop();ma[i]=j;ma[j]=i
    return ma,[i for i in range(n) if i not in ma]


def canonical(m):
    n=2*m+1
    for u in masks(n,m+2):
        mu,fu=matching(u,n);fo=[i for i in fu if u>>i&1];p,q=fo[:2]
        a=u^(1<<p);l=a^(1<<q);b=u^(1<<q)
        yield u,p,q,a,l,b


def central_primitives(b,n):
    ma,fr=matching(b,n);fz=[i for i in fr if not(b>>i&1)];fo=[i for i in fr if b>>i&1]
    lo=fz[-1] if fz else -1;hi=fo[0] if fo else n
    # Matched pairs not strictly nested in another matched pair contained in
    # the central gap (lo,hi).
    pairs=[]
    for p,q in ma.items():
        if p<q and lo<p<q<hi:pairs.append((p,q))
    exposed=[]
    for p,q in pairs:
        if not any(r<p<q<s for r,s in pairs):exposed.append((p,q))
    return lo,hi,sorted(exposed),ma,fr


def audit(m):
    n=2*m+1;rows=list(canonical(m));byb=collections.defaultdict(list)
    for r in rows:byb[r[-1]].append(r)
    ls=[r[4] for r in rows];assert len(ls)==len(set(ls))
    bad=[]
    for b,rs in byb.items():
        lo,hi,pr,ma,fr=central_primitives(b,n)
        got=sorted((r[1],r[2]) for r in rs)
        if got!=pr:bad.append((b,got,pr,lo,hi,fr))
    print('M',m,'U',len(rows),'Linject',len(set(ls)),'Bimage',len(byb),
          'Bdef',len(rows)-len(byb),'fiber_hist',sorted(collections.Counter(map(len,byb.values())).items()),
          'bad_normal_form',len(bad))
    if bad:print('BAD',bad[:3])


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('ms',nargs='+',type=int);a=ap.parse_args()
    for m in a.ms:audit(m)
