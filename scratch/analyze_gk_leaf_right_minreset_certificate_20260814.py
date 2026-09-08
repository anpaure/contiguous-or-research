#!/usr/bin/env python3
"""Audit the finite m=7 minimum-left leaf repair certificate (H100 only)."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def gk(x,n):
    st=[];ma={}
    for i in range(n):
        if x>>i&1:st.append(i)
        elif st:
            j=st.pop();ma[j]=i;ma[i]=j
    fr=[i for i in range(n) if i not in ma]
    return ma,[i for i in fr if not(x>>i&1)],[i for i in fr if x>>i&1]


def word(x,n):return ''.join(str(x>>i&1) for i in range(n))


def profile(r,n):
    _ma,fz,fo=gk(r['lower'],n)
    t=len(fz)-1-fz.index(r['p'])
    return (t,r['p'],r['q'],r['p']-r['q'],len(fz),fo[0] if fo else -1)


def audit(path:Path):
    d=json.loads(path.read_text());m=d['m'];n=d.get('n',2*m+1)
    records=d.get('records') or d.get('chosen')
    if records is None:
        raise ValueError(d.keys())
    left=[r for r in records if r['q']<r['p']]
    right=[r for r in records if r['q']>r['p']]
    print('INSTANCE',m,n,'all',len(records),'left',len(left),'right',len(right))
    print('PROFILE',sorted(collections.Counter(profile(r,n) for r in left).items()))
    for r in sorted(left,key=lambda z:(z['p'],z['q'],z['upper'])):
        print('RESET',word(r['upper'],n),'p',r['p'],'q',r['q'],
              'A',word(r['a'],n) if 'a' in r else '-',
              'L',word(r['lower'],n),'B',word(r['b'],n),'profile',profile(r,n))

    # Exact owner graph components, and which reset edges/components join.
    adj=collections.defaultdict(list)
    for i,r in enumerate(records):
        a=r.get('a',r['upper']^(1<<r['p']))
        b=r['b'];adj[a].append((b,i));adj[b].append((a,i))
    seen=set();components=[]
    for seed in adj:
        if seed in seen:continue
        q=collections.deque([seed]);seen.add(seed);verts=set();edges=set()
        while q:
            x=q.popleft();verts.add(x)
            for y,i in adj[x]:
                edges.add(i)
                if y not in seen:seen.add(y);q.append(y)
        components.append((verts,edges))
    print('OWNER_COMPONENTS',len(components),collections.Counter(len(e) for v,e in components),
          'cycle_rank',sum(len(e)-len(v)+1 for v,e in components))
    reset_indices={i for i,r in enumerate(records) if r['q']<r['p']}
    print('RESET_COMPONENTS',sorted(collections.Counter(
        (len(v),len(e),len(e&reset_indices)) for v,e in components if e&reset_indices).items()))
    for v,e in components:
        if e&reset_indices:
            print('RESETCOMP',len(v),len(e),len(e&reset_indices),
                  sorted(word(x,n) for x in v),
                  sorted(word(records[i]['upper'],n) for i in e&reset_indices))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('certificate',type=Path);a=p.parse_args();audit(a.certificate)
