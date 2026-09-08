#!/usr/bin/env python3
"""Independent direct-forward OR audit of the supplied literal optimum; h100 only."""
import hashlib,json,math,resource,signal,socket,time
from collections import Counter
from pathlib import Path
assert socket.gethostname().split('.')[0]=='arboghast'
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(45)
started=time.monotonic()
SOURCE=Path('/home/amodo/k17_optimal24313_forward_input.word')
OUT=Path('/home/amodo/exact-b-k17-optimal24313-forward-20260908');OUT.mkdir(exist_ok=True)
EXPECTED='7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
FULL=(1<<17)-1
raw=SOURCE.read_bytes();digest=hashlib.sha256(raw).hexdigest();assert digest==EXPECTED
word=[int(token) for token in raw.split()]
assert len(word)==24313 and all(1<=a<=FULL for a in word)

def ranks(targets):return dict(sorted(Counter(t.bit_count() for t in targets).items()))

def direct_forward_linear(values):
    witnesses={};scanned=0
    for left in range(len(values)):
        target=0
        for right in range(left,len(values)):
            target|=values[right];scanned+=1
            witnesses.setdefault(target,(left,right))
            if target==FULL:break
    return witnesses,scanned

def direct_forward_cyclic(period):
    double=period+period;v=len(period);witnesses={};scanned=0
    for left in range(v):
        target=0
        for right in range(left,left+v):
            target|=double[right];scanned+=1
            witnesses.setdefault(target,(left,right))
            if target==FULL:break
    return witnesses,scanned

whole,whole_scanned=direct_forward_linear(word)
assert whole_scanned==552396
assert len(whole)==FULL and all(t in whole for t in range(1,FULL+1))
assert ranks(whole)=={r:math.comb(17,r) for r in range(1,18)}
print('FULL_WORD_PASS',json.dumps(dict(length=len(word),sha256=digest,targets=len(whole),
    direct_forward_intervals=whole_scanned)),flush=True)

V=word[:86];Z=word[86:]
Vcov,Vscans=direct_forward_linear(V);Zcov,Zscans=direct_forward_linear(Z)
assert len(V)==86 and len(Z)==24227
assert len(Vcov)==639 and len(Zcov)==130747
internal=set(Vcov)|set(Zcov)
missing=sorted(set(range(1,FULL+1))-internal)
assert len(internal)==131066 and missing==[27299,27303,27315,27319,29363]
seam=word[83:89]
assert seam==[19076,19106,8834,25249,689,12849]
seam_checks=[]
for target,a,b in ((27299,2,4),(27303,1,4),(27315,2,5),(27319,1,5),(29363,3,6)):
    left=83+a-1;right=83+b-1;value=0
    for i in range(left,right+1):value|=word[i]
    assert left<86<=right and value==target
    seam_checks.append(dict(target=target,rank=target.bit_count(),local_one_based=[a,b],
        global_zero_based_inclusive=[left,right],global_one_based_inclusive=[left+1,right+1],
        direct_or=value))
assert [row['rank'] for row in seam_checks]==[8,9,9,10,9]

short=[]
for width,expected_rank_set,expected_count in ((1,set(range(1,7)),21777),(2,{7},19448),
        (3,{8},24310),(4,{9},24310),(5,{10},19448)):
    counts=Counter();targets=set()
    for left in range(len(word)-width+1):
        target=0
        for right in range(left,left+width):target|=word[right]
        counts[target.bit_count()]+=1;targets.add(target)
    assert set(counts)==expected_rank_set and len(targets)==expected_count
    short.append(dict(width=width,window_count=len(word)-width+1,
        rank_occurrence_counts=dict(sorted(counts.items())),distinct_targets=len(targets),
        distinct_target_rank_counts=ranks(targets)))
assert short[3]['window_count']==short[3]['distinct_targets']==24310

Q=word[:85];R=word[86:-2]
assert len(Q)==85 and len(R)==24225
assert word[85]==Q[0] and word[-2:]==R[:2]
assert word==Q+[Q[0]]+R+R[:2]
Qcov,Qscans=direct_forward_cyclic(Q);Rcov,Rscans=direct_forward_cyclic(R)
assert len(Qcov)==664 and len(Rcov)==130748
assert len(set(Qcov)|set(Rcov))==FULL
cyclic_middle=[]
for width,rank in ((3,8),(4,9)):
    seen=Counter()
    for period in (Q,R):
        v=len(period)
        for left in range(v):
            target=0
            for offset in range(width):target|=period[(left+offset)%v]
            assert target.bit_count()==rank
            seen[target]+=1
    assert len(seen)==math.comb(17,rank)==24310 and set(seen.values())=={1}
    cyclic_middle.append(dict(width=width,rank=rank,total_windows=sum(seen.values()),
        distinct_targets=len(seen),every_target_occurs_once=True))

W=math.comb(17,9);lower_mass=sum(math.comb(17,r) for r in range(1,9))
d=0
while d*W+d*(d+1)//2<lower_mass:d+=1
assert (W,lower_mass,d,W+d)==(24310,65535,3,24313)
report=dict(status='PASS',scope='Direct ordinary forward OR scans of the supplied literal word; no search, quotient-certificate assumption, suffix recurrence, or segment-tree algorithm used in this independent audit.',
    length=len(word),input_sha256=digest,all_letters_nonempty=True,all_letters_in_17_cube=True,
    all_nonempty_targets=len(whole),missing_targets=[],direct_forward_intervals=whole_scanned,
    global_target_rank_counts=ranks(whole),all_stored_witnesses_nonwrapping=True,
    lower_bound=dict(W=W,lower_rank_target_count=lower_mass,
        two_extra_positions_capacity=2*W+3,three_extra_positions_capacity=3*W+6,
        endpoint_delay=d,B17=W+d),exact_optimal_length=24313,
    linear_blocks=dict(V=dict(length=len(V),targets=len(Vcov),forward_intervals=Vscans,target_rank_counts=ranks(Vcov)),
        Z=dict(length=len(Z),targets=len(Zcov),forward_intervals=Zscans,target_rank_counts=ranks(Zcov)),
        internal_union_count=len(internal),missing_internal_targets=missing),
    seam_letters=seam,seam_witnesses=seam_checks,short_windows=short,
    two_cycle_decomposition=dict(Q_length=len(Q),R_length=len(R),
        copied_Q_letter_matches=True,copied_R_two_letters_match=True,
        Q_cyclic_targets=len(Qcov),R_cyclic_targets=len(Rcov),cyclic_union_targets=FULL,
        Q_cyclic_forward_intervals=Qscans,R_cyclic_forward_intervals=Rscans,
        Q_cyclic_rank_counts=ranks(Qcov),R_cyclic_rank_counts=ranks(Rcov),middle_windows=cyclic_middle),
    unverified_scope='Original quotient-row generator, temporal transition certificate, and reported search/regeneration history were not supplied and are not premises of the literal optimality proof.',
    resource_caps=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=1024**3),
    elapsed_seconds=time.monotonic()-started)
(OUT/'k17_optimal24313_direct_forward_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'k17_optimal24313_direct_forward_witnesses.json').write_text(json.dumps({str(t):whole[t] for t in sorted(whole)})+'\n')
(OUT/'k17_optimal24313.word').write_bytes(raw)
print('FINAL',json.dumps({k:report[k] for k in ('status','length','input_sha256','all_nonempty_targets','direct_forward_intervals','lower_bound','linear_blocks','seam_witnesses','short_windows','two_cycle_decomposition','elapsed_seconds')}),flush=True)
