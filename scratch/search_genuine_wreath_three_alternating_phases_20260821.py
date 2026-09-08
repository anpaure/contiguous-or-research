#!/usr/bin/env python3
"""Soft search for three consecutive alternating monochromatic phases."""
from __future__ import annotations
import argparse,math,random
from search_genuine_wreath_gk_antidiagonal_20260821 import windows,top_parity,mutate

def evaluate(a,z):
 b=len(a);r=(b-1)//2;A=windows(a,r);B=windows(z,r+1);M=[[top_parity(A[i],B[j],b) for j in range(b)] for i in range(b)];best=(-1,None)
 for p in range(b):
  for e in (0,1):
   q=sum(M[i][(p+t-i)%b]==(e^(t&1)) for t in range(3) for i in range(b))
   if q>best[0]:best=(q,(p,e))
 return best[0],best[1],M

def run(b,restarts,steps,seed):
 rng=random.Random(seed);best=None
 starts=[]
 starts.append((tuple(range(b)),(0,)+tuple(range(b-1,0,-1))))
 for _ in range(restarts-1):
  a=list(range(b));z=list(range(b));rng.shuffle(a);rng.shuffle(z);qa=a.index(0);qz=z.index(0);starts.append((tuple(a[qa:]+a[:qa]),tuple(z[qz:]+z[:qz])))
 for rr,(a,z) in enumerate(starts):
  cur=evaluate(a,z)
  if best is None or cur[0]>best[0]:best=(*cur,a,z);print("best",b,rr,0,best[0],"of",3*b,best[1],a,z,flush=True)
  for it in range(1,steps+1):
   na,nz=(mutate(a,rng),z) if rng.randrange(2) else (a,mutate(z,rng));nxt=evaluate(na,nz);temp=max(.05,4*(1-it/steps))
   if nxt[0]>=cur[0] or rng.random()<math.exp((nxt[0]-cur[0])/temp):a,z,cur=na,nz,nxt
   if cur[0]>best[0]:best=(*cur,a,z);print("best",b,rr,it,best[0],"of",3*b,best[1],a,z,flush=True)
 print("FINAL",b,best[0],"of",3*b,best[1],best[-2],best[-1],flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument("--b",nargs="+",type=int,required=True);p.add_argument("--restarts",type=int,default=20);p.add_argument("--steps",type=int,default=10000);p.add_argument("--seed",type=int,default=1);a=p.parse_args()
 for b in a.b:run(b,a.restarts,a.steps,a.seed+b)
if __name__=="__main__":main()
