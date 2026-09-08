#!/usr/bin/env python3
"""One fixed canonical k19 height-adaptive construction. Mathematical execution: h100 only."""
import hashlib
import json
import math
import resource
import signal
import time
from collections import Counter
from itertools import combinations
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(300,300))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.alarm(360)
started=time.monotonic();cpu_started=time.process_time()
OUT=Path('/home/amodo/exact-b-k19-height-adaptive-20260908')
OUT.mkdir(parents=True,exist_ok=True)
R=9;N=2*R+1;FULL=(1<<N)-1

def root_height(mask):
    for u in range(N):
        if mask>>u&1:continue
        balance=0;height=0
        for j in range(1,N):
            balance+=1 if mask>>((u+j)%N)&1 else -1
            if balance<0:break
            height=max(height,balance)
        else:
            assert balance==0
            return u,height
    raise AssertionError('no canonical root')

states=[sum(1<<i for i in c) for c in combinations(range(N),R)]
rh={a:root_height(a) for a in states}
fm={a:FULL^a^(1<<rh[a][0]) for a in states}
assert len(set(fm.values()))==len(states)==math.comb(N,R)
unseen=set(states);cycles=[]
while unseen:
    a=min(unseen);p=a;cycle=[]
    while p in unseen:
        cycle.append(p);unseen.remove(p);p=fm[fm[p]]
    assert p==a
    cycles.append(cycle)

records=[];theorem=[];trimmed=[]
for cid,cycle in enumerate(cycles):
    h=rh[cycle[0]][1]
    assert all(rh[a][1]==h for a in cycle)
    owners=[FULL^a for a in cycle];length=len(owners)
    assert 1<=h<=R and length>=2*h-1
    letters=[]
    for i in range(length):
        mask=FULL
        for j in range(h+1):mask&=owners[(i+j)%length]
        assert mask
        letters.append(mask)
    for i in range(length):
        value=0
        for j in range(h+1):value|=letters[(i+j)%length]
        assert value==owners[(i+h)%length]
    runs=[]
    for bit in range(N):
        for i in range(length):
            if owners[i]>>bit&1 and not(owners[i-1]>>bit&1):
                run=1
                while owners[(i+run)%length]>>bit&1:
                    run+=1
                    assert run<length
                runs.append(run)
    assert runs and min(runs)>h
    records.append(dict(cycle=cid,first_lower_owner=cycle[0],length=length,height=h,
        min_positive_run=min(runs),lower_owners=cycle,source_period=letters,
        theorem_block_start=len(theorem),trimmed_block_start=len(trimmed)))
    theorem.extend(letters+letters[:2*h-1])
    trimmed.extend(letters+letters[:h])
height_sum=sum(rec['height'] for rec in records)
assert len(theorem)==len(states)+2*height_sum-len(cycles)
assert len(trimmed)==len(states)+height_sum
print(json.dumps(dict(stage='constructed_fixed_periods',dimension=N,owner_count=len(states),
    component_count=len(cycles),height_sum=height_sum,theorem_length=len(theorem),trimmed_length=len(trimmed))),flush=True)

def target_witnesses(word):
    suffix={};witnesses={}
    for end,letter in enumerate(word):
        current={letter:end}
        for target,start in suffix.items():current.setdefault(target|letter,start)
        assert len(current)<=N
        for target,start in current.items():witnesses.setdefault(target,(start,end))
        suffix=current
    return witnesses

def certify(word,label,witnesses=None):
    assert all(1<=a<=FULL for a in word)
    witnesses=target_witnesses(word) if witnesses is None else witnesses
    size=1
    while size<len(word):size*=2
    tree=[0]*(2*size);tree[size:size+len(word)]=word
    for i in range(size-1,0,-1):tree[i]=tree[2*i]|tree[2*i+1]
    for target,(left,right) in witnesses.items():
        assert 0<=left<=right<len(word)
        a=left+size;b=right+size+1;value=0
        while a<b:
            if a&1:value|=tree[a];a+=1
            if b&1:b-=1;value|=tree[b]
            a//=2;b//=2
        assert value==target
    missing=[t for t in range(1,FULL+1) if t not in witnesses]
    raw=('\n'.join(map(str,word))+'\n').encode()
    (OUT/(label+'.word')).write_bytes(raw)
    (OUT/(label+'_target_witnesses.json')).write_text(json.dumps({str(t):witnesses[t] for t in sorted(witnesses)})+'\n')
    rec=dict(word_file=label+'.word',length=len(word),sha256=hashlib.sha256(raw).hexdigest(),
        all_letters_nonzero=True,distinct_targets=len(witnesses),missing_count=len(missing),
        missing_targets=missing,missing_rank_counts=dict(sorted(Counter(t.bit_count() for t in missing).items())),
        target_rank_counts=dict(sorted(Counter(t.bit_count() for t in witnesses).items())),
        segment_tree_witnesses_rechecked=len(witnesses),witness_indexing='zero-based inclusive nonwrapping endpoints')
    print(label,json.dumps({k:v for k,v in rec.items() if k!='missing_targets'},sort_keys=True),flush=True)
    return rec

theorem_report=certify(theorem,'k19_height_theorem'+str(len(theorem)))
trim_witnesses=target_witnesses(trimmed)
trim_report=certify(trimmed,'k19_height_trimmed'+str(len(trimmed)),trim_witnesses)
repaired=trimmed+trim_report['missing_targets']
repair_report=certify(repaired,'k19_height_repaired'+str(len(repaired)))
assert theorem_report['missing_count']==repair_report['missing_count']==0
report=dict(status='PASS',dimension=N,owner_count=len(states),component_count=len(cycles),height_sum=height_sum,
    canonical_convention='f(A)=complement(A) minus unique unmatched zero; g=f^2; each lower cycle starts at its least integer mask; cycles ordered by that mask; future-(h+1)-intersection source; no cut, ordering or repair optimization',
    height_histogram=dict(sorted(Counter(rec['height'] for rec in records).items())),
    all_component_heights_invariant=True,all_positive_runs_strictly_exceed_height=True,
    all_periodic_owner_reconstructions_exact=True,theorem=theorem_report,trimmed=trim_report,repaired=repair_report,
    resource_caps=dict(cpu_seconds=300,wall_seconds=360,address_space_bytes=4*1024**3),
    elapsed_wall_seconds=time.monotonic()-started,elapsed_cpu_seconds=time.process_time()-cpu_started)
(OUT/'height_adaptive_fixed_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'height_adaptive_canonical_cycles.json').write_text(json.dumps(records)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('theorem','trimmed','repaired')},indent=2),flush=True)
print('PASS: one fixed k19 construction; both universal words fully checked and every saved witness independently range-OR verified.',flush=True)
