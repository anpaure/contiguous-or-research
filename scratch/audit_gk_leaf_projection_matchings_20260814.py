#!/usr/bin/env python3
"""Maximum projection matchings for fixed-GK leaf catalogues (H100 only)."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def audit(path: Path, mode: str, types: set[int] | None):
    d=json.loads(path.read_text()); recs=d['records']; n=d['n'];m=d['m']
    def matching(x):
        st=[];ma={}
        for i in range(n):
            if x>>i&1:st.append(i)
            elif st:
                j=st.pop();ma[i]=j;ma[j]=i
        return ma,[i for i in range(n) if i not in ma]
    kept=[]
    for r in recs:
        if mode=='right' and not r['q']>r['p']:continue
        if types is not None:
            ml,fl=matching(r['lower']);fz=[i for i in fl if not(r['lower']>>i&1)]
            t=len(fz)-1-fz.index(r['p'])
            if t not in types:continue
        kept.append(r)
    us=sorted({r['upper'] for r in recs});uid={x:i for i,x in enumerate(us)}
    for shore in ('lower','b'):
        vs=sorted({r[shore] for r in kept});vid={x:i for i,x in enumerate(vs)}
        pairs={(uid[r['upper']],vid[r[shore]]) for r in kept}
        rr=np.fromiter((x for x,y in pairs),dtype=np.int32);cc=np.fromiter((y for x,y in pairs),dtype=np.int32)
        a=csr_matrix((np.ones(len(pairs),dtype=np.int8),(rr,cc)),shape=(len(us),len(vs)))
        mat=maximum_bipartite_matching(a,perm_type='column')
        size=int(np.sum(mat>=0));unmatched=[us[i] for i,x in enumerate(mat) if x<0]
        print('MATCH',m,mode,types,shore,'U',len(us),'V',len(vs),'pairs',len(pairs),'size',size,'def',len(us)-size,'unmatched',unmatched[:5])


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('paths',nargs='+',type=Path);ap.add_argument('--mode',choices=['leaf','right'],default='right');ap.add_argument('--types');a=ap.parse_args()
    types=None if a.types is None else {int(x) for x in a.types}
    for p in a.paths:audit(p,a.mode,types)
