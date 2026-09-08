#!/usr/bin/env python3
"""Anneal elementary checkerboard squares in a genuine-wreath GK matrix."""

from __future__ import annotations

import argparse
import math
import random

from search_genuine_wreath_gk_antidiagonal_20260821 import windows, top_parity, mutate


def evaluate(alpha, beta):
    b=len(alpha);r=(b-1)//2;aa=windows(alpha,r);bb=windows(beta,r+1)
    M=[[top_parity(aa[i],bb[j],b) for j in range(b)] for i in range(b)]
    squares=[]
    for i in range(b):
        for j in range(b):
            a=M[i][j];c=M[(i+1)%b][(j+1)%b]
            if a==c and M[(i+1)%b][j]==1-a and M[i][(j+1)%b]==1-a:squares.append((i,j,a))
    H=sum(M[i][j]!=M[i][(j+1)%b] for i in range(b) for j in range(b))
    V=sum(M[i][j]!=M[(i+1)%b][j] for i in range(b) for j in range(b))
    return len(squares),H+V,squares,M


def run(b,restarts,steps,seed):
    rng=random.Random(seed);best=None
    for z in range(restarts):
        a=list(range(b));c=list(range(b));rng.shuffle(a);rng.shuffle(c);qa=a.index(0);qc=c.index(0);a=tuple(a[qa:]+a[:qa]);c=tuple(c[qc:]+c[:qc]);cur=evaluate(a,c)
        if best is None or cur[:2]>best[:2]:best=(*cur,a,c);print("best",b,z,0,best[0],best[1],a,c,flush=True)
        for it in range(1,steps+1):
            na,nc=(mutate(a,rng),c) if rng.randrange(2) else (a,mutate(c,rng));nxt=evaluate(na,nc);old=cur[0]*(b*b+1)+cur[1];new=nxt[0]*(b*b+1)+nxt[1];temp=max(.05,4*(1-it/steps))
            if new>=old or rng.random()<math.exp((new-old)/temp):a,c,cur=na,nc,nxt
            if cur[:2]>best[:2]:best=(*cur,a,c);print("best",b,z,it,best[0],best[1],a,c,flush=True)
    print("FINAL",b,"Q",best[0],"HV",best[1],"squares",best[2],"alpha",best[-2],"beta",best[-1],flush=True)


def main():
    p=argparse.ArgumentParser();p.add_argument("--b",nargs="+",type=int,required=True);p.add_argument("--restarts",type=int,default=20);p.add_argument("--steps",type=int,default=10000);p.add_argument("--seed",type=int,default=1);a=p.parse_args()
    for b in a.b:run(b,a.restarts,a.steps,a.seed+b)


if __name__=="__main__":main()
