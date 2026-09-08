#!/usr/bin/env python3
"""Extract a canonical alternating-reachability Hall witness (H100 only)."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def matching(x,n):
    st=[];ma={}
    for i in range(n):
        if x>>i&1:st.append(i)
        elif st:
            j=st.pop();ma[i]=j;ma[j]=i
    return ma,[i for i in range(n) if i not in ma]


def profile(x,n):
    ma,fr=matching(x,n);fz=[i for i in fr if not(x>>i&1)];fo=[i for i in fr if x>>i&1]
    s=0;mn=0
    for i in range(n):s += 1 if x>>i&1 else -1;mn=min(mn,s)
    return (len(fz),len(fo),mn,fo[0] if fo else -1,fz[-1] if fz else -1)


def audit(path:Path, dump:Path|None):
    d=json.loads(path.read_text());m=d['m'];n=d['n'];recs=[r for r in d['records'] if r['q']>r['p']]
    us=sorted({r['upper'] for r in d['records']});bs=sorted({r['b'] for r in recs});uid={x:i for i,x in enumerate(us)};bid={x:i for i,x in enumerate(bs)}
    adj=[set() for _ in us]
    for r in recs:adj[uid[r['upper']]].add(bid[r['b']])
    pairs={(i,j) for i,js in enumerate(adj) for j in js}
    rr=np.fromiter((i for i,j in pairs),dtype=np.int32);cc=np.fromiter((j for i,j in pairs),dtype=np.int32)
    a=csr_matrix((np.ones(len(pairs),dtype=np.int8),(rr,cc)),shape=(len(us),len(bs)))
    row_to_col=maximum_bipartite_matching(a,perm_type='column')
    col_to_row={j:i for i,j in enumerate(row_to_col) if j>=0}
    start=[i for i,j in enumerate(row_to_col) if j<0]
    reach_u=set(start);reach_b=set();q=collections.deque(start)
    while q:
        i=q.popleft()
        matched=row_to_col[i]
        for j in adj[i]:
            if j==matched:continue
            if j in reach_b:continue
            reach_b.add(j)
            if j in col_to_row and col_to_row[j] not in reach_u:
                reach_u.add(col_to_row[j]);q.append(col_to_row[j])
    neigh={j for i in reach_u for j in adj[i]}
    assert neigh==reach_b
    U=[us[i] for i in sorted(reach_u)];B=[bs[j] for j in sorted(reach_b)]
    print('WITNESS',m,'allU',len(us),'allB',len(bs),'matching',sum(row_to_col>=0),'S',len(U),'N',len(B),'def',len(U)-len(B))
    print('UPROFILE',sorted(collections.Counter(profile(x,n) for x in U).items()))
    print('BPROFILE',sorted(collections.Counter(profile(x,n) for x in B).items()))
    # Simple coordinate marginals and endpoint blocks.
    print('UMARG', [sum(x>>i&1 for x in U) for i in range(n)])
    print('BMARG', [sum(x>>i&1 for x in B) for i in range(n)])
    for k in range(1,min(8,n)+1):
        cu=collections.Counter(x&((1<<k)-1) for x in U)
        cb=collections.Counter(x&((1<<k)-1) for x in B)
        print('PREFIX',k,'U',sorted(cu.items()),'B',sorted(cb.items()))
    if dump:
        dump.write_text(json.dumps({'m':m,'n':n,'S':U,'N':B,'deficiency':len(U)-len(B)},indent=2,sort_keys=True))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('path',type=Path);ap.add_argument('--dump',type=Path);a=ap.parse_args();audit(a.path,a.dump)
