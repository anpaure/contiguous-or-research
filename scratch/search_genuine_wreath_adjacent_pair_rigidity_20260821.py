#!/usr/bin/env python3
"""Anneal the best oppositely-colored adjacent pair of phase antidiagonals."""

from __future__ import annotations

import argparse
import math
import random

from search_genuine_wreath_gk_antidiagonal_20260821 import windows, top_parity, mutate


def evaluate(alpha, beta):
    b = len(alpha); r = (b - 1) // 2
    aa = windows(alpha, r); bb = windows(beta, r + 1)
    mat = [[top_parity(aa[i], bb[j], b) for j in range(b)] for i in range(b)]
    best = (-1, None)
    for p in range(b):
        for eps in (0, 1):
            good = sum(mat[i][(p-i) % b] == eps and mat[i][(p+1-i) % b] == 1-eps for i in range(b))
            if good > best[0]: best = (good, (p, eps))
    return best[0], best[1], mat


def run(b, restarts, steps, seed):
    rng = random.Random(seed); best = None
    for restart in range(restarts):
        a = list(range(b)); z = list(range(b)); rng.shuffle(a); rng.shuffle(z)
        qa = a.index(0); qz = z.index(0); a=tuple(a[qa:]+a[:qa]); z=tuple(z[qz:]+z[:qz])
        cur=evaluate(a,z)
        if best is None or cur[0]>best[0]: best=(*cur,a,z); print("best",b,restart,0,best[0],best[1],a,z,flush=True)
        for it in range(1,steps+1):
            na,nz=(mutate(a,rng),z) if rng.randrange(2) else (a,mutate(z,rng)); nxt=evaluate(na,nz)
            temp=max(.03,2*(1-it/steps))
            if nxt[0]>=cur[0] or rng.random()<math.exp((nxt[0]-cur[0])/temp):a,z,cur=na,nz,nxt
            if cur[0]>best[0]:best=(*cur,a,z);print("best",b,restart,it,best[0],best[1],a,z,flush=True)
    print("FINAL",b,best[0],best[1],best[-2],best[-1],flush=True)


def main():
    p=argparse.ArgumentParser();p.add_argument("--b",nargs="+",type=int,required=True);p.add_argument("--restarts",type=int,default=20);p.add_argument("--steps",type=int,default=10000);p.add_argument("--seed",type=int,default=1);a=p.parse_args()
    for b in a.b:run(b,a.restarts,a.steps,a.seed+b)


if __name__=="__main__":main()
