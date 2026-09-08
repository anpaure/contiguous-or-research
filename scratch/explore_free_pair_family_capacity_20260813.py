#!/usr/bin/env python3
"""Capacity census for cyclic cancellation diamond subfamilies with h unmatched ones."""

from collections import Counter
from itertools import combinations


def masks(n,w):
    for cc in combinations(range(n),w):yield sum(1<<i for i in cc)


def cyclic_free_ones(word,n):
    h=0;vals=[0]
    for i in range(n):h+=1 if (word>>i)&1 else -1;vals.append(h)
    start=max(i for i,v in enumerate(vals[:-1]) if v==max(vals[:-1]))%n
    st=[];free=[]
    for j in range(n):
        i=(start+j)%n
        if not (word>>i)&1:st.append(i)
        elif st:st.pop()
        else:free.append(i)
    assert not st
    return free


def main():
    # upper excess is fixed at 3 here, so all pairs among free ones = 3 choices.
    # Enlarge by allowing a pair of ones whose cyclic reduced positions are within
    # t primitive boundaries after cancellation; currently just collect full diamonds
    # by cyclic separation of deleted ones in original word.
    for r in range(3,18):
        n=2*r-1; ups=list(masks(n,r+1)); lows=list(masks(n,r-1))
        for dist in (1,2,3,4,None):
            deg=Counter(); opts=0
            for u in ups:
                ones=[i for i in range(n) if (u>>i)&1]
                for a,b in combinations(ones,2):
                    sep=min((b-a)%n,(a-b)%n)
                    if dist is not None and sep>dist:continue
                    lo=u^(1<<a)^(1<<b);deg[lo]+=1;opts+=1
            # Each upper selects one; total omissions in its option hyperedge differs,
            # so simple triangle capacity no longer directly applies. Print degrees.
            print(r,dist,"opts/U",round(opts/len(ups),3),"covered",len(deg),
                  "mindeg",min((deg[x] for x in lows),default=0),
                  "maxdeg",max(deg.values(),default=0),"avg",round(opts/len(lows),3))
        print()


if __name__=="__main__":main()
