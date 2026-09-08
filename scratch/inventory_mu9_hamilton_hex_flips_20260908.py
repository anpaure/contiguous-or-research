#!/usr/bin/env python3
"""H100-only exact hexagon flip inventory, no partition/order solver."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import json
import resource
import socket
import sys
import time

N, FULL = 126, 511


def rot(x, step):
    step %= 9
    return ((x << step) & FULL) | (x >> (9-step) if step else 0)


def edge(a,b):
    return min(a,b), max(a,b)


def extract(adj):
    start = min(v for v in adj if v.bit_count()==4)
    seq, previous, current = [start], None, start
    while True:
        options = sorted(adj[current] - ({previous} if previous is not None else set()))
        following = options[0]
        if following == start:
            break
        if following in seq:
            raise AssertionError("cycle extraction repeated nonstart")
        seq.append(following)
        previous, current = current, following
    if len(seq) != 252:
        return None
    lower, upper = seq[::2], seq[1::2]
    assert len(set(lower))==len(set(upper))==126
    assert all(x.bit_count()==4 for x in lower)
    assert all(x.bit_count()==5 for x in upper)
    assert all(upper[i] == (lower[i] | lower[(i+1)%N]) for i in range(N))
    return lower, upper


def local_block(s,p,S,U,V):
    ss=[S[(s+j)%N] for j in range(p)]
    adds=[ss[j+1] & ~ss[j] for j in range(p-1)]
    removes=[ss[j] & ~ss[j+1] for j in range(p-1)]
    b5=U[(s-1)%N] & ~ss[0]
    common=FULL
    for x in ss:
        common &= x
    if any(x.bit_count()!=1 for x in adds+removes+[b5]) or common.bit_count()!=5-p:
        return None
    masks=adds+removes+[b5]
    if len(set(masks))!=len(masks) or any(x & common for x in masks):
        return None
    if any(x & U[(s-1)%N] for x in adds):
        return None
    return {"s":s,"p":p,"drops":(s+p-2)%N,
            "retained_V":[(s+j-2)%N for j in range(1,p)]}


def main():
    assert socket.gethostname().lower()=="arboghast", "Run only via ssh h100"
    resource.setrlimit(resource.RLIMIT_CPU,(18,18))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30))
    started=time.monotonic()
    seed=[3,18,130,258,264,72,96,36,33,48,24,272,144,192]
    A=[rot(seed[i],5*t) for t in range(9) for i in range(14)]
    S=[A[i]|A[(i+1)%N]|A[(i+2)%N] for i in range(N)]
    U=[S[i]|A[(i+3)%N] for i in range(N)]
    assert len(set(S))==len(set(U))==N
    adj={v:set() for v in S+U}
    for i in range(N):
        adj[S[i]].add(U[i]); adj[U[i]].add(S[i])
        adj[S[(i+1)%N]].add(U[i]); adj[U[i]].add(S[(i+1)%N])
    assert all(len(x)==2 for x in adj.values())
    base_edges={edge(v,w) for v,ws in adj.items() for w in ws}
    base_intrinsic={s:list(adj[s])[0] | list(adj[s])[1] for s in S}
    assert len(set(base_intrinsic.values()))==84
    eligible=0; nonham=0; retained=[]; coverhist=Counter(); seen=set(); total=0
    for core in combinations(range(9),3):
        K=sum(1<<i for i in core)
        outside=[i for i in range(9) if i not in core]
        for abc in combinations(outside,3):
            total+=1
            a,b,c=[1<<i for i in abc]
            ll=[K|a,K|b,K|c]
            uu=[K|a|b,K|b|c,K|c|a]
            m0={edge(ll[0],uu[0]),edge(ll[1],uu[1]),edge(ll[2],uu[2])}
            m1={edge(ll[1],uu[0]),edge(ll[2],uu[1]),edge(ll[0],uu[2])}
            if m0 <= base_edges and not (m1 & base_edges):
                remove,add=m0,m1
            elif m1 <= base_edges and not (m0 & base_edges):
                remove,add=m1,m0
            else:
                continue
            eligible+=1
            newadj={v:set(ws) for v,ws in adj.items()}
            for v,w in remove:
                newadj[v].remove(w);newadj[w].remove(v)
            for v,w in add:
                newadj[v].add(w);newadj[w].add(v)
            assert all(len(ws)==2 for ws in newadj.values())
            cycle=extract(newadj)
            if cycle is None:
                nonham+=1;continue
            ss,us=cycle
            key=tuple(ss+us)
            if key in seen:
                continue
            seen.add(key)
            vv=[us[i]|us[(i+1)%N] for i in range(N)]
            assert all(v.bit_count()==6 for v in vv)
            for s in S:
                newvalue=list(newadj[s])[0]|list(newadj[s])[1]
                if s not in ll:
                    assert newvalue==base_intrinsic[s]
            coverage=len(set(vv));coverhist[coverage]+=1
            if coverage>=83:
                blocks=[block for s in range(N) for p in range(1,6)
                        if (block:=local_block(s,p,ss,us,vv)) is not None]
                retained.append({"id":len(retained),"core":list(core),"abc":list(abc),
                                 "removed_edges":sorted(remove),"added_edges":sorted(add),
                                 "rank6_distinct":coverage,
                                 "rank6_missing":sorted(v for v in range(512) if v.bit_count()==6 and v not in set(vv)),
                                 "S":ss,"U":us,"V":vv,"blocks":blocks,
                                 "valid_block_counts":dict(Counter(b["p"] for b in blocks))})
    assert total==1680
    report={"host":socket.gethostname(),"elapsed_seconds":time.monotonic()-started,
            "hexagons":total,"eligible_matching_flips":eligible,
            "nonhamilton_flips":nonham,"distinct_hamilton_flips":len(seen),
            "rank6_coverage_histogram":dict(sorted(coverhist.items())),
            "retained_at_least83":len(retained),"retained_cycles":retained,
            "scope":"complete single-hexagon inventory and local block checks, no partition or full row solver"}
    Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+"\n")
    summary={k:v for k,v in report.items() if k!="retained_cycles"}
    summary["small_certificates"]=[{k:v for k,v in row.items() if k not in ("S","U","V","blocks")}
                                  for row in retained[:3]]
    print(json.dumps(summary,indent=2))


if __name__=="__main__":
    main()
