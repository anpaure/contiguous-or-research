#!/usr/bin/env python3
"""Anneal the maximum checkerboard count on one elementary antidiagonal."""
from __future__ import annotations
import argparse,math,random
from search_genuine_wreath_gk_checkerboard_squares_20260821 import evaluate as square_eval
from search_genuine_wreath_gk_antidiagonal_20260821 import mutate

def evaluate(a,z):
 Q,HV,squares,M=square_eval(a,z);b=len(a);cnt=[0]*b
 for i,j,c in squares:cnt[(i+j)%b]+=1
 return max(cnt),cnt.index(max(cnt)),cnt,squares,M

def run(b,restarts,steps,seed):
 rng=random.Random(seed);best=None
 starts=[(tuple(range(b)),(0,)+tuple(range(b-1,0,-1)))]
 for _ in range(restarts-1):
  a=list(range(b));z=list(range(b));rng.shuffle(a);rng.shuffle(z);qa=a.index(0);qz=z.index(0);starts.append((tuple(a[qa:]+a[:qa]),tuple(z[qz:]+z[:qz])))
 for rr,(a,z) in enumerate(starts):
  cur=evaluate(a,z)
  if best is None or cur[0]>best[0]:best=(*cur,a,z);print("best",b,rr,0,best[0],best[1],best[2],a,z,flush=True)
  for it in range(1,steps+1):
   na,nz=(mutate(a,rng),z) if rng.randrange(2) else (a,mutate(z,rng));nxt=evaluate(na,nz);temp=max(.03,3*(1-it/steps))
   if nxt[0]>=cur[0] or rng.random()<math.exp((nxt[0]-cur[0])/temp):a,z,cur=na,nz,nxt
   if cur[0]>best[0]:best=(*cur,a,z);print("best",b,rr,it,best[0],best[1],best[2],a,z,flush=True)
 print("FINAL",b,best[0],best[1],best[2],best[-2],best[-1],flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument("--b",nargs="+",type=int,required=True);p.add_argument("--restarts",type=int,default=30);p.add_argument("--steps",type=int,default=15000);p.add_argument("--seed",type=int,default=1);a=p.parse_args()
 for b in a.b:run(b,a.restarts,a.steps,a.seed+b)
if __name__=="__main__":main()
