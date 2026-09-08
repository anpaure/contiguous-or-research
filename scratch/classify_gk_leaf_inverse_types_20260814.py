#!/usr/bin/env python3
"""Classify inverse incidences of fixed-GK leaf options (H100 only)."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n, r):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def matching(x, n):
    st = []
    mate = {}
    for i in range(n):
        if (x >> i) & 1:
            st.append(i)
        elif st:
            j = st.pop()
            mate[i] = j
            mate[j] = i
    free = [i for i in range(n) if i not in mate]
    return mate, free


def options(m, right=False):
    n = 2*m+1
    for a in masks(n, m+1):
        ma, fa = matching(a, n)
        fz = [i for i in fa if not ((a >> i) & 1)]
        if not fz:
            continue
        p = fz[-1]
        for q in range(n):
            if ((a >> q) & 1) and (q not in ma or ma[q] == q+1) and (not right or q > p):
                yield a, a ^ (1 << q), a ^ (1 << q) ^ (1 << p), p, q


def classify_lower(l, p, q, n):
    ml, fl = matching(l, n)
    fz = [i for i in fl if not ((l >> i) & 1)]
    fo = [i for i in fl if (l >> i) & 1]
    if q in fz:
        qt = ('free0', fz.index(q), len(fz))
    elif q in ml:
        qt = ('matched0', ml[q] - q)
    else:
        qt = ('other0',)
    if p in fz:
        pt = ('free0', fz.index(p), len(fz))
    elif p in ml:
        pt = ('matched0' if not ((l >> p) & 1) else 'matched1', ml[p]-p)
    elif p in fo:
        pt = ('free1', fo.index(p), len(fo))
    else:
        pt = ('other',)
    return qt, pt, (q > p) - (q < p), q-p


def classify_b(b, a, l, p, q, n):
    mb, fb = matching(b, n)
    fz = [i for i in fb if not ((b >> i) & 1)]
    fo = [i for i in fb if (b >> i) & 1]
    if q in fz:
        qt = ('free0', fz.index(q), len(fz))
    elif q in mb:
        qt = ('matched0', mb[q]-q)
    else:
        qt = ('other0',)
    if p in fo:
        pt = ('free1', fo.index(p), len(fo))
    elif p in mb:
        pt = ('matched1', mb[p]-p)
    else:
        pt = ('other1',)
    return qt, pt, (q > p) - (q < p), q-p


def bits(x, n):
    return ''.join('1' if (x >> i) & 1 else '0' for i in range(n))


def audit(m, right):
    n = 2*m+1
    by_l = collections.defaultdict(list)
    by_b = collections.defaultdict(list)
    for a, l, b, p, q in options(m, right):
        by_l[l].append((a,b,p,q))
        by_b[b].append((a,l,p,q))
    hist = collections.Counter(map(len, by_l.values()))
    types = collections.Counter()
    settypes = collections.Counter()
    examples = {}
    for l, rows in by_l.items():
        ts=[]
        for a,b,p,q in rows:
            t=classify_lower(l,p,q,n); ts.append(t); types[t]+=1; examples.setdefault(t,(l,a,b,p,q))
        settypes[tuple(sorted(ts))]+=1
    print('M',m,'right',right,'options',sum(hist[k]*k for k in hist),'Lhist',sorted(hist.items()),'Bhist',sorted(collections.Counter(map(len,by_b.values())).items()))
    print('LTYPES')
    for t,c in sorted(types.items(), key=lambda z:(str(z[0]),z[1])): print(c,t,'ex',tuple(bits(x,n) if i<3 else x for i,x in enumerate(examples[t])))
    print('LSETTYPES')
    for t,c in sorted(settypes.items(), key=lambda z:(len(z[0]),str(z[0]))): print(c,t)


if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('ms',nargs='+',type=int); ap.add_argument('--right',action='store_true'); args=ap.parse_args()
    for m in args.ms: audit(m,args.right)
