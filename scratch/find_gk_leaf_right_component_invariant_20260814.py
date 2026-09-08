#!/usr/bin/env python3
"""Mine exact edge invariants of the leaf-right U--B projection (H100 only)."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def gk(x, n):
    stack=[]; mate={}
    for i in range(n):
        if x>>i&1: stack.append(i)
        elif stack:
            j=stack.pop();mate[j]=i;mate[i]=j
    free=[i for i in range(n) if i not in mate]
    fz=[i for i in free if not(x>>i&1)]
    fo=[i for i in free if x>>i&1]
    return mate,fz,fo


def word(x,n): return ''.join(str(x>>i&1) for i in range(n))


def keys(x,n):
    ma,fz,fo=gk(x,n)
    p=fo[0]
    w=word(x,n)
    heights=[];h=0
    for c in w:
        h += 1 if c=='1' else -1;heights.append(h)
    minimum=min([0]+heights)
    last_min=max([-1]+[i for i,h in enumerate(heights) if h==minimum])
    last_zero=fz[-1] if fz else -1
    # Canonical first-free-one prefix and its matched/free-zero decorations.
    first_free=free[0] if (free:=sorted(fz+fo)) else n
    first_free_zero=fz[0] if fz else -1
    last_free_zero=fz[-1] if fz else -1
    first_free_one=fo[0]
    d0=w[:first_free]
    central=w[last_free_zero+1:first_free_one]
    return {
      'D0':d0,
      'central':central,
      'D0_central_pair':(d0,central),
      'prefix_before_first_free':w[:first_free],
      'free_zero_gap_words':tuple(w[(fz[i-1]+1 if i else 0):z] for i,z in enumerate(fz)),
      'prefix_to_fo':w[:p+1],
      'prefix_before_fo':w[:p],
      'fo':p,
      'lastmin_prefix':w[:last_min+1],
      'suffix_after_lastmin':w[last_min+1:],
      'prefix_to_last_fz':w[:last_zero+1],
      'prefix_through_gap':w[:p+1],
      'unmatched_zero_prefix':tuple(fz),
      'matched_prefix_pairs':tuple((i,ma[i]) for i in range(p) if i in ma and i<ma[i]),
      'cyclic_lastmin_rotation':w[last_min+1:]+w[:last_min+1],
    }


def audit(path):
    d=json.loads(path.read_text());n=d['n'];m=d['m']
    recs=[r for r in d['records'] if r['q']>r['p']]
    names=list(keys(recs[0]['upper'],n))
    print('INSTANCE',m,n,'edges',len(recs))
    for name in names:
        bad=[]
        for r in recs:
            ku=keys(r['upper'],n)[name];kb=keys(r['b'],n)[name]
            if ku!=kb:
                bad.append((r['upper'],r['b'],r['p'],r['q'],ku,kb))
        print('KEY',name,'bad',len(bad),'of',len(recs),'examples',bad[:3])

    # Cross-upper equality at each common head is what determines whether a
    # key really labels projection components.
    byb=collections.defaultdict(set)
    for r in recs:byb[r['b']].add(r['upper'])
    for name in names:
        badheads=[]
        for b,us in byb.items():
            vals={keys(u,n)[name] for u in us}
            if len(vals)>1:badheads.append((b,len(us),len(vals),list(vals)[:3]))
        print('COMMON_HEAD_KEY',name,'badheads',len(badheads),'examples',badheads[:3])


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('catalogue',type=Path);a=p.parse_args();audit(a.catalogue)
