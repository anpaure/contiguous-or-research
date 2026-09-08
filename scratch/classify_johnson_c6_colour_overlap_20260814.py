#!/usr/bin/env python3
"""Classify alternating lower/upper colour overlaps of Johnson C6s.

Substantive enumeration belongs on H100.
"""

from __future__ import annotations

import argparse
import collections
import itertools


def bits(s):
    x=0
    for i in s:x|=1<<i
    return x


def lower(a,b):return a&b
def upper(a,b):return a|b


def canonical_cycle(c):
    rots=[]
    for z in (c,tuple(reversed(c))):
        rots += [z[i:]+z[:i] for i in range(6)]
    return min(rots)


def partitions(values):
    label={};out=[]
    for x in values:
        if x not in label:label[x]=len(label)
        out.append(label[x])
    return tuple(out)


def main(n,m):
    vs=[bits(c) for c in itertools.combinations(range(n),m)]
    adj={x:[y for y in vs if x<y and (x^y).bit_count()==2] for x in vs}
    und={x:set() for x in vs}
    for x,ys in adj.items():
        for y in ys:und[x].add(y);und[y].add(x)
    cycles=set()
    for start in vs:
        def dfs(path):
            x=path[-1]
            if len(path)==6:
                if start in und[x]:cycles.add(canonical_cycle(tuple(path)))
                return
            for y in und[x]:
                if y<=start or y in path:continue
                dfs(path+[y])
        dfs([start])
    census=collections.Counter(); examples={}
    implication_bad=[]; exact_lower=[]; exact_upper=[]; type_stats=collections.Counter()
    for c in cycles:
        e=[(c[i],c[(i+1)%6]) for i in range(6)]
        lo=[lower(*q) for q in e];up=[upper(*q) for q in e]
        lm=[lo[i] for i in (0,2,4)];lp=[lo[i] for i in (1,3,5)]
        um=[up[i] for i in (0,2,4)];upv=[up[i] for i in (1,3,5)]
        lcommon=sum((collections.Counter(lm)&collections.Counter(lp)).values())
        ucommon=sum((collections.Counter(um)&collections.Counter(upv)).values())
        key=(lcommon,ucommon,partitions(lo),partitions(up))
        census[key]+=1;examples.setdefault(key,c)
        if lcommon==2:implication_bad.append(c)
        if lcommon==3:exact_lower.append((c,ucommon,partitions(lo),partitions(up)))
        if ucommon==3:exact_upper.append((c,lcommon,partitions(lo),partitions(up)))
        common_lower=collections.Counter(lm)&collections.Counter(lp)
        if lcommon==3:
            distinct_lower=len(set(lm))==3 and len(set(lp))==3
            distinct_upper=len(set(um))==3 and len(set(upv))==3
            type_stats[('exactlower',distinct_lower,distinct_upper,ucommon)]+=1
    print('INSTANCE',n,m,'vertices',len(vs),'cycles',len(cycles),'types',len(census))
    print('OVERLAP_HIST',sorted(collections.Counter((k[0],k[1]) for k,v in census.items() for _ in range(v)).items()))
    print('TYPE_HIST')
    for key,count in sorted(census.items()):print(count,key,'example',examples[key])
    print('LOWER_COMMON_2',len(implication_bad),implication_bad[:10])
    print('EXACT_LOWER',len(exact_lower),'UPPER_HIST',collections.Counter(z[1] for z in exact_lower))
    for z in exact_lower[:80]:print('EL',z)
    print('EXACT_UPPER',len(exact_upper),'LOWER_HIST',collections.Counter(z[1] for z in exact_upper))
    print('TYPE_STATS',sorted(type_stats.items()))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('n',type=int);p.add_argument('m',type=int);a=p.parse_args();main(a.n,a.m)
