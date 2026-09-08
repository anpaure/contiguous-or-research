#!/usr/bin/env python3
"""Search orbitwise bounds for parity of GK chain height under pair rotations."""

from __future__ import annotations

import argparse
from itertools import product


def height(seq):
    s=0
    mn=0
    for a,bb in seq:
        s += 1 if a else -1
        mn=min(mn,s)
        s += 1 if bb else -1
        mn=min(mn,s)
    assert s==0
    return -mn


def audit(b):
    pairs=((0,0),(0,1),(1,0),(1,1))
    worst=[]
    failures=[]
    seen=set()
    for ww in product(pairs, repeat=b):
        if sum(a+c for a,c in ww)!=b:
            continue
        rots=[ww[j:]+ww[:j] for j in range(b)]
        key=min(rots)
        if key in seen:
            continue
        seen.add(key)
        hs=[height(rr) for rr in rots]
        r=sum(a for a,c in ww)
        d=abs(2*r-b)
        for q in range(1,b+1):
            odd=sum(k>=q and k%2==1 for k in hs)
            even=sum(k>=q and k%2==0 for k in hs)
            diff=abs(odd-even)
            slack=diff-d
            worst.append((slack,q,d,diff,ww,hs))
            if diff>d+q:
                failures.append((q,d,diff,ww,hs))
    worst.sort(reverse=True,key=lambda z:z[0])
    print({"b":b,"orbits":len(seen),"fail_diff_le_d_plus_q":len(failures),"worst":worst[:12]})
    if failures:
        print("first failures",failures[:5])


if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--b",type=int,required=True)
    audit(ap.parse_args().b)
