#!/usr/bin/env python3
"""Row/column degree diagnostics for split-refined GK orientation/top relations."""

from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations


def bracket(mask,n):
    st=[]; pairs=[]
    for i in range(n):
        if mask>>i&1: st.append(i)
        elif st: pairs.append((st.pop(),i))
    paired={i for p in pairs for i in p}
    uu=[i for i in range(n) if i not in paired]
    return uu


def run(b):
    n=2*b
    for r in range(b+1):
        rows=defaultdict(list); cols=defaultdict(list)
        for cc in combinations(range(n),b):
            m=sum(1<<i for i in cc)
            X=tuple(j for j in range(b) if m>>(2*j)&1)
            Y=tuple(j for j in range(b) if m>>(2*j+1)&1)
            if len(X)!=r: continue
            uu=bracket(m,n)
            k=len(uu)//2
            orient='A' if k%2 else 'B'
            rows[X].append((Y,k,orient)); cols[Y].append((X,k,orient))
        print('b,r',b,r)
        for orient in 'AB':
            for q in range(0,b+1):
                rd=Counter(sum(k>=q and o==orient for _,k,o in vv) for vv in rows.values())
                cd=Counter(sum(k>=q and o==orient for _,k,o in vv) for vv in cols.values())
                if q==0 or len(rd)>1 or len(cd)>1:
                    print(orient,'q',q,'rowdeg',dict(rd),'coldeg',dict(cd))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--b',type=int,required=True); run(ap.parse_args().b)
