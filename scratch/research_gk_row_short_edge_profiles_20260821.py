#!/usr/bin/env python3
"""DP short-top profiles for fixed A rows in the GK orientation graphs."""

from __future__ import annotations
import argparse, math
from collections import defaultdict
from math import comb


def top_distribution(a):
    b=len(a); r=sum(a); need=b-r
    # (height, minimum, B-one count) -> number
    dp={(0,0,0):1}
    for abit in a:
        nd=defaultdict(int)
        da=1 if abit else -1
        for (h,m,c),v in dp.items():
            h1=h+da; m1=min(m,h1)
            # B zero
            h2=h1-1
            nd[(h2,min(m1,h2),c)]+=v
            # B one
            if c<need:
                h2=h1+1
                nd[(h2,min(m1,h2),c+1)]+=v
        dp=nd
    out=defaultdict(int)
    for (h,m,c),v in dp.items():
        if c==need:
            assert h==0
            out[-m]+=v
    assert sum(out.values())==comb(b,need)
    return out


def patterns(b,r):
    z=b-r
    ans={
      'zeros_then_ones':[0]*z+[1]*r,
      'ones_then_zeros':[1]*r+[0]*z,
    }
    alt=[]
    rr=r; zz=z
    while rr+zz:
        if zz: alt.append(0); zz-=1
        if rr: alt.append(1); rr-=1
    ans['alternating']=alt
    # Mechanical spread of r ones.
    ans['mechanical']=[((i+1)*r//b - i*r//b) for i in range(b)]
    return ans


def run(b,r,H):
    N=comb(b,r); delta=abs(2*r-b)
    nr=max(0,(b-delta-H+2)//2)
    d=nr*N//b
    DA=comb(b-1,r); DB=comb(b-1,r-1)
    for name,a in patterns(b,r).items():
        dist=top_distribution(a)
        print('pattern',name,'b,r,H',b,r,H,'N,d,DA,DB',N,d,DA,DB)
        for o,D,par in [('A',DA,1),('B',DB,0)]:
            assert sum(v for k,v in dist.items() if k%2==par)==D
            m=D-d
            cum=0; threshold=None; mincost=0; left=m
            for k in sorted(dist):
                if k%2!=par: continue
                take=min(left,dist[k]); mincost+=take*min(k,H); left-=take
                cum+=dist[k]
                if threshold is None and cum>=m: threshold=k
            print(o,'remove_degree',m,'row_min_cost',mincost,'threshold',threshold,
                  'dist',sorted((k,v) for k,v in dist.items() if k%2==par))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--b',type=int,required=True);p.add_argument('--r',type=int,required=True);p.add_argument('--H',type=int,required=True)
    a=p.parse_args();run(a.b,a.r,a.H)
