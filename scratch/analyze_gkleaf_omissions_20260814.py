#!/usr/bin/env python3
"""Classify the Catalan-sized omitted shores of fixed-GK leaf solutions."""

from __future__ import annotations

import argparse, collections, itertools, json
from pathlib import Path


def masks(n,r):
    for c in itertools.combinations(range(n),r):
        x=0
        for i in c:x|=1<<i
        yield x


def matching(x,n):
    st=[];mate={}
    for i in range(n):
        if (x>>i)&1:st.append(i)
        elif st:
            j=st.pop();mate[i]=j;mate[j]=i
    free=[i for i in range(n) if i not in mate]
    return mate,free


def profile(x,n):
    mate,free=matching(x,n)
    f0=sum(not ((x>>i)&1) for i in free);f1=len(free)-f0
    minpref=0;s=0
    for i in range(n):
        s += 1 if (x>>i)&1 else -1
        minpref=min(minpref,s)
    return (f0,f1,minpref,s)


def main(path):
    d=json.loads(path.read_text());m=d['m'];n=d['n'];ch=d['chosen']
    used_l={r['lower'] for r in ch};used_b={r['b'] for r in ch};used_a={r['a'] for r in ch}
    all_l=set(masks(n,m));all_o=set(masks(n,m+1))
    for name,vals in [('Lomit',all_l-used_l),('Bomit',all_o-used_b),('Aomit',all_o-used_a)]:
        print('m',m,name,'count',len(vals),'profiles',sorted(collections.Counter(profile(x,n) for x in vals).items()))
        print('first', [format(x,f'0{n}b')[::-1] for x in sorted(vals)[:min(12,len(vals))]])


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('paths',nargs='+',type=Path);a=ap.parse_args()
    for p in a.paths:main(p)
