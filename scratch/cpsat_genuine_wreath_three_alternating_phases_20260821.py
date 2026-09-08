#!/usr/bin/env python3
"""CP-SAT search for three consecutive alternating monochromatic GK phases."""
from __future__ import annotations
import argparse,itertools
from ortools.sat.python import cp_model

def top_parity(x,y,b):
 h=mn=0
 for q in range(b):
  h += 1 if x>>q&1 else -1; mn=min(mn,h)
  h += 1 if y>>q&1 else -1; mn=min(mn,h)
 return (-mn)&1

def masks(b,k):return [sum(1<<q for q in c) for c in itertools.combinations(range(b),k)]

def solve(b,e,seconds,workers):
 r=(b-1)//2;m=cp_model.CpModel();pa=[m.new_int_var(0,b-1,f"pa{q}") for q in range(b)];pb=[m.new_int_var(0,b-1,f"pb{q}") for q in range(b)];m.add_all_different(pa);m.add_all_different(pb);m.add(pa[0]==0)
 A=[[m.new_bool_var(f"A{i}_{q}") for q in range(b)] for i in range(b)];B=[[m.new_bool_var(f"B{j}_{q}") for q in range(b)] for j in range(b)]
 AM=[m.new_int_var(0,(1<<b)-1,f"AM{i}") for i in range(b)];BM=[m.new_int_var(0,(1<<b)-1,f"BM{j}") for j in range(b)]
 for i in range(b):
  for q in range(b):m.add_allowed_assignments([pa[q],A[i][q]],[(z,int((i-z)%b<r)) for z in range(b)])
  m.add(AM[i]==sum((1<<q)*A[i][q] for q in range(b)))
 for j in range(b):
  for q in range(b):m.add_allowed_assignments([pb[q],B[j][q]],[(z,int((j-z)%b<r+1)) for z in range(b)])
  m.add(BM[j]==sum((1<<q)*B[j][q] for q in range(b)))
 xs=masks(b,r);ys=masks(b,r+1);allowed={c:[] for c in (0,1)}
 for x in xs:
  for y in ys:allowed[top_parity(x,y,b)].append((x,y))
 print({"b":b,"pairs":{c:len(allowed[c]) for c in (0,1)}},flush=True)
 for t in range(3):
  c=e^(t&1)
  for i in range(b):m.add_allowed_assignments([AM[i],BM[(t-i)%b]],allowed[c])
 s=cp_model.CpSolver();s.parameters.max_time_in_seconds=seconds;s.parameters.num_search_workers=workers;s.parameters.log_search_progress=False
 status=s.solve(m);print("STATUS",s.status_name(status),"b",b,"e",e,"wall",s.wall_time,flush=True)
 if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
  ia=[s.value(z) for z in pa];ib=[s.value(z) for z in pb];alpha=[None]*b;beta=[None]*b
  for q,z in enumerate(ia):alpha[z]=q
  for q,z in enumerate(ib):beta[z]=q
  print("WITNESS alpha",tuple(alpha),"beta",tuple(beta),flush=True)

if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--b",type=int,required=True);p.add_argument("--e",type=int,nargs="+",default=[0,1]);p.add_argument("--seconds",type=float,default=600);p.add_argument("--workers",type=int,default=64);a=p.parse_args()
 for e in a.e:solve(a.b,e,a.seconds,a.workers)
