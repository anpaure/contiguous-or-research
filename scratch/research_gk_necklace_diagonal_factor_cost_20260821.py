#!/usr/bin/env python3
"""Exact costs for necklace-block diagonal GK factors (ssh h100)."""

from __future__ import annotations
import argparse
from itertools import combinations
from math import comb


def masks(b,r):
    return [sum(1<<i for i in cc) for cc in combinations(range(b),r)]


def rot(m,s,b):
    s%=b; z=(1<<b)-1
    return ((m<<s)&z)|(m>>(b-s) if s else 0)


def reps(b,r):
    seen=set(); out=[]
    for m in masks(b,r):
        if m in seen: continue
        oo={rot(m,s,b) for s in range(b)}
        assert len(oo)==b
        seen|=oo; out.append(min(oo))
    return out


def ktop(xm,ym,b):
    h=0;mn=0
    for i in range(b):
        h += 1 if xm>>i&1 else -1; mn=min(mn,h)
        h += 1 if ym>>i&1 else -1; mn=min(mn,h)
    assert h==0
    return -mn


def run(b,r,H):
    RX=reps(b,r); RY=reps(b,b-r); N=comb(b,r)
    defect=abs(2*r-b); n=max(0,(b-defect-H+2)//2)
    total={'A':0,'B':0}; full={'A':0,'B':0}; diagstats=[]
    maxratio={'A':(0,None),'B':(0,None)}
    for x in RX:
        for y in RY:
            vals={'A':[],'B':[]}
            for t in range(b):
                ks=[ktop(rot(x,s,b),rot(y,s+t,b),b) for s in range(b)]
                par={k%2 for k in ks}; assert len(par)==1
                o='A' if next(iter(par)) else 'B'
                vals[o].append(sum(min(k,H) for k in ks))
            assert len(vals['A'])==b-r and len(vals['B'])==r
            for o in 'AB':
                full[o]+=sum(vals[o]); total[o]+=sum(sorted(vals[o],reverse=True)[:n])
                remove_count=len(vals[o])-n
                removed=sum(sorted(vals[o])[:remove_count])
                ratio=removed/(b*(remove_count+1)**1.5)
                if ratio>maxratio[o][0]: maxratio[o]=(ratio,(x,y,sorted(vals[o]),remove_count))
                diagstats.extend((o,v) for v in vals[o])
    print({'b':b,'r':r,'H':H,'N':N,'necklaces':len(RX),'n':n,
           'full':full,'diagonal_factor':total,
           'loss':{o:full[o]-total[o] for o in 'AB'},
           'loss_over_L':{o:(full[o]-total[o])/(N*N) for o in 'AB'},
           'max_block_ratio_removed_over_b_a32':maxratio})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--b',type=int,required=True);p.add_argument('--r',type=int,required=True);p.add_argument('--H',type=int,required=True)
    a=p.parse_args();run(a.b,a.r,a.H)
