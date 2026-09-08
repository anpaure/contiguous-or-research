#!/usr/bin/env python3
"""Sample rowwise short-top degrees at the global unconstrained cutoff."""

from __future__ import annotations
import argparse, math, random, statistics
from math import comb
from research_gk_row_short_edge_profiles_20260821 import top_distribution


def E(b,r,u):
    return comb(b,r+u)*comb(b,r-u) if u<=r<=b-u else 0


def ncount(b,r,k):
    if k%2==0:
        u=k//2
        return (r+u)*E(b,r,u)//b-(r+u+1)*E(b,r,u+1)//b
    u=k//2
    return (b-r-u)*E(b,r,u)//b-(b-r-u-1)*E(b,r,u+1)//b


def run(b,r,H,samples,seed):
    rng=random.Random(seed); N=comb(b,r); defect=abs(2*r-b)
    nr=max(0,(b-defect-H+2)//2)
    for o,par,D in [('A',1,comb(b-1,r)),('B',0,comb(b-1,r-1))]:
        m=D-nr*N//b
        left=m*N; cutoff=None; below=0; tie_need=0; tie_total=0
        for k in range(par,b+1,2):
            z=ncount(b,r,k)
            if left>z:
                below+=z;left-=z
            else:
                cutoff=k;tie_need=left;tie_total=z;break
        frac=tie_need/tie_total if tie_total else 0
        global_cost=sum(ncount(b,r,k)*min(k,H) for k in range(par,cutoff,2)) + tie_need*min(cutoff,H)
        global_cost_ratio=global_cost/(N*N)
        vals=[]; belowvals=[]; tievals=[]
        row_cost_ratios=[]
        for _ in range(samples):
            ones=set(rng.sample(range(b),r)); a=[int(i in ones) for i in range(b)]
            dist=top_distribution(a)
            low=sum(v for k,v in dist.items() if k%2==par and k<cutoff)
            tie=dist.get(cutoff,0)
            expected=low+frac*tie
            vals.append(float((expected-m)/N))
            belowvals.append(float(low/N)); tievals.append(float(tie/N))
            leftrow=m; rcost=0
            for k in range(par,b+1,2):
                take=min(leftrow,dist.get(k,0)); rcost+=take*min(k,H); leftrow-=take
                if not leftrow: break
            assert leftrow==0
            row_cost_ratios.append(rcost/N)
        print({'b':b,'r':r,'H':H,'o':o,'N':N,'D/N':D/N,'m/N':m/N,
               'cutoff':cutoff,'tie_frac':frac,
               'dev_mean':statistics.mean(vals),'dev_sd':statistics.pstdev(vals),
               'dev_min':min(vals),'dev_max':max(vals),
               'below_mean':statistics.mean(belowvals),'tie_mean':statistics.mean(tievals),
               'global_uncon_remove_cost/L':global_cost_ratio,
               'sample_row_min_cost/L_mean':statistics.mean(row_cost_ratios),
               'row_only_extra_LB_est':statistics.mean(row_cost_ratios)-global_cost_ratio,
               'row_cost_sd':statistics.pstdev(row_cost_ratios)})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--b',type=int,required=True);p.add_argument('--r',type=int,required=True);p.add_argument('--H',type=int,required=True);p.add_argument('--samples',type=int,default=20);p.add_argument('--seed',type=int,default=1)
    a=p.parse_args();run(a.b,a.r,a.H,a.samples,a.seed)
