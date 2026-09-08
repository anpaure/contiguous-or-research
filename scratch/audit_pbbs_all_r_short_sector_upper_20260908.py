#!/usr/bin/env python3
"""Fixed all-r short-sector path: complete bounded upper support audit on h100."""
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
signal.alarm(110)
results=[]
for r in range(3,9):
    n=2*r+1
    full=(1<<n)-1
    def root(a):
        for u in range(n):
            if a>>u&1:
                continue
            height=0
            for j in range(1,n):
                height+=1 if a>>((u+j)%n)&1 else -1
                if height<0:
                    break
            else:
                assert height==0
                return u
        raise AssertionError(a)
    def tf(t):
        x,y,z,u=t
        return y,z,x,(u+2*(x+1))%n
    def lower(t):
        x,y,z,u=t
        d="10"*x+"1"+"10"*(y+1)+"0"+"10"*z
        return sum(1<<((u+i+1)%n) for i,c in enumerate(d) if c=="1")
    blocks=[]
    badstates=set()
    for b in list(range(1,r-2))+[0]:
        t=(b,r-2-b,0,n-1)
        for _ in range(2*n-b if b else 0):
            t=tf(tf(t))
        block=[]
        for _ in range(3*n):
            a=lower(t)
            badstates.add(a)
            block.append(full^a)
            t=tf(tf(t))
        blocks.append(block)
    path=[a for b in blocks for a in b]
    assert len(path)==len(badstates)==3*n*(r-2)
    states=[sum(1<<j for j in x) for x in combinations(range(n),r)]
    f={a:full^a^(1<<root(a)) for a in states}
    unseen=set(states)
    cycles=[]
    while unseen:
        a=min(unseen)
        p=a
        c=[]
        while p in unseen:
            unseen.remove(p)
            c.append(p)
            p=f[f[p]]
        assert p==a
        cycles.append(c)
    bad_upper=set()
    outside_upper=set()
    old_supplier_masks={}
    def cyclic_upper(w):
        out=set()
        for i in range(len(w)):
            acc=w[i]
            for q in range(1,len(w)):
                acc|=w[(i+q)%len(w)]
                if acc==full:
                    break
                if acc.bit_count()>=r+2:
                    out.add(acc)
        return out
    bad_id=0
    for c in cycles:
        isbad=c[0] in badstates
        assert all((a in badstates)==isbad for a in c)
        supp=cyclic_upper([full^a for a in c])
        if isbad:
            bad_upper|=supp
            for y in supp:
                old_supplier_masks[y]=old_supplier_masks.get(y,0)|(1<<bad_id)
            bad_id+=1
        else:
            outside_upper|=supp
    assert bad_id==r-2
    only_bad=bad_upper-outside_upper
    old_global=bad_upper|outside_upper
    assert len(old_global)==sum(comb(n,j) for j in range(r+2,n))
    path_upper=set()
    path_witness={}
    for i in range(len(path)):
        acc=path[i]
        for j in range(i+1,len(path)):
            acc|=path[j]
            if acc==full:
                break
            if acc.bit_count()>=r+2:
                path_upper.add(acc)
                path_witness.setdefault(acc,[i,j])
    missing=old_global-(path_upper|outside_upper)
    gap_patterns=Counter()
    for y in only_bad:
        a=full^y
        ones=[i for i in range(n) if a>>i&1]
        gaps=[(ones[(i+1)%len(ones)]-ones[i]-1)%n for i in range(len(ones))]
        gap_patterns[tuple(sorted(gaps))]+=1
    rec=dict(r=r,n=n,bad_owner_count=len(path),old_component_count=len(cycles),
        only_bad_upper_count=len(only_bad),
        only_bad_upper_rank_counts=dict(sorted(Counter(y.bit_count() for y in only_bad).items())),
        only_bad_lower_zero_gap_patterns={str(k):v for k,v in gap_patterns.items()},
        only_bad_supplier_component_counts=dict(sorted(Counter(old_supplier_masks[y].bit_count() for y in only_bad).items())),
        old_global_upper_count=len(old_global),new_global_upper_count=len(old_global)-len(missing),
        missing_upper=sorted(missing),
        only_bad_targets=sorted(only_bad),
        special_target_path_witnesses={str(y):path_witness[y] for y in only_bad if y in path_witness})
    results.append(rec)
    print(json.dumps({k:v for k,v in rec.items() if k not in ("only_bad_targets","special_target_path_witnesses")},sort_keys=True),flush=True)
    if missing:
        break
Path("short_sector_upper.json").write_text(json.dumps(results,indent=2)+"\n")
print("DONE: fixed-formula bounded support audit; no alternate paths searched")
