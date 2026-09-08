#!/usr/bin/env python3
"""Greedy tests for the 3-choice cyclic-unmatched Catalan pathization."""

from collections import Counter
from itertools import combinations, permutations
from explore_cyclic_unmatched_diamonds_20260813 import sets, cyclic_unmatched_ones, comps


def options(r):
    n=2*r-1;ret={}
    for u in sets(n,r+1):
        ff=cyclic_unmatched_ones(u,n); vv=[]
        for rule in range(3):
            d=[ff[rule],ff[(rule+1)%3]]
            lo=u^(1<<d[0])^(1<<d[1]);a=lo|(1<<d[0]);b=lo|(1<<d[1])
            vv.append((rule,lo,a,b))
        ret[u]=vv
    return ret


def run(r, order_key, pref):
    n=2*r-1;oo=options(r);used=set();deg=Counter();sel=[]
    for u in sorted(oo,key=order_key):
        av=[x for x in oo[u] if x[0] in pref and x[1] not in used and deg[x[2]]<2 and deg[x[3]]<2]
        av.sort(key=lambda x:(pref.index(x[0]),deg[x[2]]+deg[x[3]],x[1]))
        if not av:return False,len(sel),0,0
        x=av[0];sel.append((x[2],x[3]));used.add(x[1]);deg[x[2]]+=1;deg[x[3]]+=1
    cc=comps(list(sets(n,r)),sel)
    return True,len(sel),max(deg.values()),sum(v==e and e for v,e in cc)


def main():
    keys={
      "lex":lambda u:u,
      "rev":lambda u:-u,
      "popweighted":lambda u:sum(i for i in range(u.bit_length()) if (u>>i)&1),
      "revpop":lambda u:-sum(i for i in range(u.bit_length()) if (u>>i)&1),
    }
    for name,key in keys.items():
      for pref in permutations(range(3)):
        vals=[]
        for r in range(2,9):vals.append(run(r,key,pref))
        if all(x[0] for x in vals):print(name,pref,vals)
        elif vals[-1][1]>4000:print("near",name,pref,vals)


if __name__=="__main__":main()
