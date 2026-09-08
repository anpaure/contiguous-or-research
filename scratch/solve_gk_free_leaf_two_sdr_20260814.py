#!/usr/bin/env python3
"""Build/solve fixed-GK two-SDR subcatalogues. Run on H100 only."""

from __future__ import annotations

import argparse
import collections
import itertools
import json
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


def masks(n, r):
    for c in itertools.combinations(range(n), r):
        x=0
        for i in c: x |= 1 << i
        yield x


def matching(x,n):
    st=[]; mate={}
    for i in range(n):
        if (x>>i)&1: st.append(i)
        elif st:
            j=st.pop(); mate[i]=j; mate[j]=i
    free=[i for i in range(n) if i not in mate]
    return mate,free


def options(m,mode):
    n=2*m+1
    for u in masks(n,m+2):
        mu,fu=matching(u,n)
        p=next(i for i in fu if (u>>i)&1)
        a=u^(1<<p)
        ma,fa=matching(a,n)
        for q in range(n):
            if not ((a>>q)&1): continue
            typ='free' if q not in ma else ('peak' if ma[q]==q+1 else 'other')
            if typ == 'other': continue
            if mode=='free' and typ!='free': continue
            if mode=='peak_right' and not (typ=='peak' and q>p): continue
            if mode=='free_first_or_peak_right':
                freeones=[z for z in fa if (a>>z)&1]
                if not (q==freeones[0] or (typ=='peak' and q>p)): continue
            if mode=='free_last_or_peak_right':
                freeones=[z for z in fa if (a>>z)&1]
                if not (q==freeones[-1] or (typ=='peak' and q>p)): continue
            if mode.startswith('lower_') and typ not in ('free','peak'): continue
            l=a^(1<<q); b=l^(1<<p)
            ml,fl=matching(l,n)
            lfz=[z for z in fl if not ((l>>z)&1)]
            sig=len(lfz)-1-lfz.index(p)
            if mode.startswith('sig'):
                payload=mode[3:].removesuffix('r')
                allowed={int(ch) for ch in payload}
                if sig not in allowed: continue
                if mode.endswith('r') and not q>p: continue
            if mode=='lower_last_free' and p != lfz[-1]: continue
            if mode=='lower_first_free' and p != lfz[0]: continue
            if mode=='lower_last_free_right' and not (p == lfz[-1] and q>p): continue
            if mode=='lower_first_free_right' and not (p == lfz[0] and q>p): continue
            yield dict(upper=u,a=a,p=p,q=q,lower=l,b=b,typ=typ,sig=sig)


def solve(m,mode,out):
    records=list(options(m,mode)); pool=IDPool(); cnf=CNF()
    byu=collections.defaultdict(list); byl=collections.defaultdict(list); byb=collections.defaultdict(list)
    for i,r in enumerate(records):
        x=pool.id(('x',i)); r['var']=x
        byu[r['upper']].append(x); byl[r['lower']].append(x); byb[r['b']].append(x)
    def amo(xs):
        if len(xs)>1: cnf.extend(CardEnc.atmost(xs,1,vpool=pool,encoding=EncType.seqcounter).clauses)
    for xs in byu.values():
        cnf.append(xs); amo(xs)
    for xs in byl.values(): amo(xs)
    for xs in byb.values(): amo(xs)
    expected=len(list(masks(2*m+1,m+2)))
    print('INSTANCE',m,mode,'uppers',len(byu),'expected',expected,'options',len(records),'lowers',len(byl),'heads',len(byb),'vars',pool.top,'clauses',len(cnf.clauses),flush=True)
    if len(byu)<expected or any(not xs for xs in byu.values()):
        print('RESULT',m,mode,'UNSAT_EMPTY',flush=True); return
    with Solver(name='cadical195',bootstrap_with=cnf) as s:
        sat=s.solve()
        print('RESULT',m,mode,'SAT' if sat else 'UNSAT',flush=True)
        if not sat:return
        pos={x for x in s.get_model() if x>0}
    chosen=[r for r in records if r['var'] in pos]
    Path(out.format(m=m,mode=mode)).write_text(json.dumps({'m':m,'n':2*m+1,'mode':mode,'chosen':chosen},indent=2,sort_keys=True))
    print('CHOSEN',len(chosen),'types',collections.Counter(r['typ'] for r in chosen),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['free','peak_right','free_first_or_peak_right','free_last_or_peak_right','lower_last_free','lower_first_free','lower_last_free_right','lower_first_free_right','sig0','sig1','sig2','sig01','sig02','sig12','sig012','sig0r','sig1r','sig2r','sig01r','sig02r','sig12r','sig012r']); ap.add_argument('ms',nargs='+',type=int); ap.add_argument('--out',default='/dev/shm/gksub_{mode}_m{m}.json'); a=ap.parse_args()
    for m in a.ms: solve(m,a.mode,a.out)
