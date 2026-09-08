#!/usr/bin/env python3
"""Search longest cyclic run of alternating monochromatic GK phases."""
from __future__ import annotations
import argparse,math,random
from search_genuine_wreath_gk_antidiagonal_20260821 import windows,top_parity,mutate

def evaluate(a,z):
 b=len(a);r=(b-1)//2;A=windows(a,r);B=windows(z,r+1);w=[]
 for p in range(b):
  v=top_parity(A[0],B[p],b);mono=all(top_parity(A[i],B[(p-i)%b],b)==v for i in range(1,b));w.append(v if mono else None)
 best=0
 for s in range(b):
  q=0
  while q<b and w[(s+q)%b] is not None and (q==0 or w[(s+q)%b]!=w[(s+q-1)%b]):q+=1
  best=max(best,q)
 return best,w

def run(b,restarts,steps,seed):
 rng=random.Random(seed);best=None
 for z in range(restarts):
  a=list(range(b));c=list(range(b));rng.shuffle(a);rng.shuffle(c);qa=a.index(0);qc=c.index(0);a=tuple(a[qa:]+a[:qa]);c=tuple(c[qc:]+c[:qc]);cur=evaluate(a,c)
  if best is None or cur[0]>best[0]:best=(*cur,a,c);print("best",b,z,0,best,flush=True)
  for it in range(1,steps+1):
   na,nc=(mutate(a,rng),c) if rng.randrange(2) else (a,mutate(c,rng));nxt=evaluate(na,nc);temp=max(.03,2*(1-it/steps))
   if nxt[0]>=cur[0] or rng.random()<math.exp((nxt[0]-cur[0])/temp):a,c,cur=na,nc,nxt
   if cur[0]>best[0]:best=(*cur,a,c);print("best",b,z,it,best,flush=True)
 print("FINAL",b,best,flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument("--b",nargs="+",type=int,required=True);p.add_argument("--restarts",type=int,default=20);p.add_argument("--steps",type=int,default=10000);p.add_argument("--seed",type=int,default=1);a=p.parse_args()
 for b in a.b:run(b,a.restarts,a.steps,a.seed+b)
if __name__=="__main__":main()
