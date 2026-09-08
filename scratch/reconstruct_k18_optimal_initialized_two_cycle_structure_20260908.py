#!/usr/bin/env python3
"""REVIEW BEFORE RUN: exact structure of the supplied optimal k18 word.

One h100 run,30CPU/45wall/1GiB. No search except a linear-time exact
lookup of the unique phase of a known cyclic word.
"""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from array import array
from collections import Counter, defaultdict
from pathlib import Path

FULL17=(1<<17)-1
NEW=1<<17
PI=(2,1,7,12,11,15,5,4,3,6,17,8,9,10,14,13,16)


def update(state,letter):
    return (letter,)+tuple(b&~letter for b in state if b&~letter)


def relabel(mask,permutation):
    answer=0
    for i,j in enumerate(permutation):
        if mask&(1<<i):answer|=1<<(j-1)
    return answer


def parse(path):
    raw=path.read_bytes()
    return raw,[int(line) for line in raw.decode('ascii').splitlines() if line.strip()]


def write_word(path,word):
    raw=''.join(f'{letter}\n' for letter in word).encode('ascii')
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def find_pattern(pattern,text):
    """KMP: all exact occurrences in linear time."""
    prefix=[0]*len(pattern)
    for i in range(1,len(pattern)):
        j=prefix[i-1]
        while j and pattern[i]!=pattern[j]:j=prefix[j-1]
        if pattern[i]==pattern[j]:j+=1
        prefix[i]=j
    matches=[];j=0
    for i,value in enumerate(text):
        while j and value!=pattern[j]:j=prefix[j-1]
        if value==pattern[j]:j+=1
        if j==len(pattern):
            matches.append(i-len(pattern)+1)
            j=prefix[j-1]
    return matches


def forward_cov(word,cyclic):
    v=len(word);physical=word+word if cyclic else word
    covered=set();scanned=0
    for start in range(v):
        value=0
        stop=start+v if cyclic else v
        for end in range(start,stop):
            value|=physical[end];covered.add(value);scanned+=1
            if value==FULL17:break
    return covered,scanned


def segment_tree(word):
    size=1
    while size<len(word):size<<=1
    tree=[0]*(2*size);tree[size:size+len(word)]=word
    for i in range(size-1,0,-1):tree[i]=tree[2*i]|tree[2*i+1]
    return size,tree


def range_or(size,tree,start,end):
    left,right,value=start+size,end+size+1,0
    while left<right:
        if left&1:value|=tree[left];left+=1
        if right&1:right-=1;value|=tree[right]
        left>>=1;right>>=1
    return value


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--word17',type=Path,required=True)
    ap.add_argument('--word18',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    assert platform.node().split('.')[0]=='arboghast','h100 only'
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    signal.alarm(45);started=time.monotonic()
    raw17,A=parse(args.word17);raw18,W=parse(args.word18)
    assert hashlib.sha256(raw17).hexdigest()=='7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
    assert hashlib.sha256(raw18).hexdigest()=='6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5'
    assert len(A)==24313 and len(W)==48623
    assert all(0<a<=FULL17 for a in A) and all(0<a<=(1<<18)-1 for a in W)
    args.out.mkdir(parents=True,exist_ok=False)
    m=len(A);left=W[:m]
    assert left[:-1]==A[:-1] and A[-1]==689 and left[-1]==8881
    assert A[-2]==25249 and (A[-2]|A[-1])==(left[-2]|left[-1])==25265
    backups=[i for i in range(1,m-1) if left[i]==A[-1]]
    assert 87 in backups
    assert W[m]==NEW and all(letter&NEW for letter in W[m+1:])
    tail=[letter&FULL17 for letter in W[m+1:]]
    assert len(tail)==24309 and all(tail)
    left_sha=write_word(args.out/'k17_optimal24313_tail8881.word',left)
    write_word(args.out/'initialized_tail_actual24309.word',tail)

    # Recover the actual initializer and independently check each later state
    # by the physical last-occurrence times in left||tail (bridge projected out).
    state=();last=[-1]*17
    for time_index,letter in enumerate(left):
        state=update(state,letter)
        for x in range(17):
            if letter&(1<<x):last[x]=time_index
    assert min(last)>=0
    initial=state
    assert [b.bit_count() for b in initial]==[6]+[1]*11
    witness_start=array('i',[-1])*(FULL17+1)
    witness_end=array('i',[-1])*(FULL17+1)
    middle8=Counter();middle9=Counter();long_stage_cov=set()
    long_length=24224
    with (args.out/'initialized_recency_states.jsonl').open('w') as states_out:
        for t in range(len(tail)+1):
            if t:
                letter=tail[t-1]
                state=update(state,letter)
                for x in range(17):
                    if letter&(1<<x):last[x]=m+t-1
            groups=defaultdict(int)
            for x,stamp in enumerate(last):groups[stamp]|=1<<x
            grouped=[(stamp,groups[stamp]) for stamp in sorted(groups,reverse=True)]
            assert tuple(mask for stamp,mask in grouped)==state
            value=0;have8=have9=False
            for stamp,mask in grouped:
                value|=mask
                if witness_start[value]<0:
                    witness_start[value]=stamp if stamp<m else stamp+1
                    witness_end[value]=m+t
                if t<=long_length:long_stage_cov.add(value)
                if value.bit_count()==8:middle8[value]+=1;have8=True
                if value.bit_count()==9:middle9[value]+=1;have9=True
            assert value==FULL17 and have8 and have9
            states_out.write(json.dumps([t,list(state)],separators=(',',':'))+'\n')
    assert all(witness_start[t]>=0 for t in range(1,FULL17+1))
    assert len(middle8)==len(middle9)==24310
    assert set(middle8.values())==set(middle9.values())=={1}
    size,tree=segment_tree(W)
    with (args.out/'initialized_targets_actual18_witnesses.jsonl').open('w') as f:
        for target in range(1,FULL17+1):
            start,end=witness_start[target],witness_end[target]
            assert 0<=start<=end<len(W)
            assert range_or(size,tree,start,end)==target|NEW
            f.write(json.dumps([target|NEW,start,end],separators=(',',':'))+'\n')
    assert W[m]==NEW

    # Whole-word critical-rank census, independently of the projected tour.
    full_state=();full_middle9=Counter();no_middle9=[]
    for endpoint,letter in enumerate(W):
        full_state=update(full_state,letter)
        value=0;have9=False
        for block in full_state:
            value|=block
            if value.bit_count()==9:full_middle9[value]+=1;have9=True
        if not have9:no_middle9.append(endpoint)
    assert no_middle9==[0,1,2]
    assert len(full_middle9)==48620 and set(full_middle9.values())=={1}

    # Undo only the submitted physical coordinate permutation.
    assert sorted(PI)==list(range(1,18))
    inverse=[0]*17
    for i,j in enumerate(PI,1):inverse[j-1]=i
    unpermuted=[relabel(letter,inverse) for letter in tail]
    assert [relabel(letter,PI) for letter in unpermuted]==tail
    write_word(args.out/'initialized_tail_unpermuted24309.word',unpermuted)
    Q=A[:85];R=A[86:-2]
    assert len(Q)==85 and len(R)==24225
    assert A==Q+[Q[0]]+R+R[:2]
    reverse_Q=list(reversed(Q));reverse_R=list(reversed(R))
    assert unpermuted[-85:]==reverse_Q
    long_tail=unpermuted[:-85]
    assert len(long_tail)==24224
    matches=[p for p in find_pattern(long_tail,reverse_R+reverse_R) if p<len(reverse_R)]
    assert len(matches)==1
    start_phase=matches[0];omitted=(start_phase-1)%len(reverse_R)
    complete_rotation=[reverse_R[(start_phase+j)%len(reverse_R)] for j in range(len(reverse_R))]
    assert complete_rotation[:-1]==long_tail and complete_rotation[-1]==reverse_R[omitted]
    regenerated=A[:-1]+[8881,NEW]+[
        relabel(letter,PI)|NEW for letter in complete_rotation[:-1]+reverse_Q]
    regenerated_raw=''.join(f'{letter}\n' for letter in regenerated).encode('ascii')
    assert regenerated==W and regenerated_raw==raw18
    (args.out/'k18_optimal48623_regenerated_from17.word').write_bytes(regenerated_raw)
    periodic=()
    for letter in complete_rotation:periodic=update(periodic,letter)
    initial_unpermuted=tuple(relabel(block,inverse) for block in initial)
    assert periodic==initial_unpermuted
    assert sum(block.bit_count() for block in periodic)==17
    write_word(args.out/'recovered_Q85.word',Q)
    write_word(args.out/'recovered_R24225.word',R)

    # Independently compute the two constituent target families by direct
    # forward interval scans, then verify every seven-hole join witness.
    long_cov,long_scans=forward_cov(reverse_R,True)
    short_cov,short_scans=forward_cov(reverse_Q,False)
    assert len(long_cov)==130748 and len(short_cov)==633
    assert {relabel(t,inverse) for t in long_stage_cov}==long_cov
    separate=long_cov|short_cov
    holes=sorted(set(range(1,FULL17+1))-separate)
    assert len(separate)==131064 and len(holes)==7
    assert holes==[27298,27299,27302,27303,27315,27319,60070]
    expected_join_intervals=[[3,4],[2,4],[3,5],[2,5],[1,4],[1,5],[3,6]]
    six=long_tail[-3:]+reverse_Q[:3]
    assert six==[10771,8739,26656,19106,19076,33444]
    seam=[];six_global_start=m+1+long_length-3
    for target in holes:
        found=[]
        for a in range(3):
            value=0
            for b in range(a,6):
                value|=six[b]
                if b>=3 and value==target:found.append((a,b))
        assert found
        a,b=found[0]
        actual_target=relabel(target,PI)|NEW
        start,end=six_global_start+a,six_global_start+b
        assert range_or(size,tree,start,end)==actual_target
        seam.append(dict(old_mask=target,old_rank=target.bit_count(),local_one_based_interval=[a+1,b+1],
                         actual18_target=actual_target,actual18_zero_based_interval=[start,end]))
    assert [item['local_one_based_interval'] for item in seam]==expected_join_intervals
    seam_record=dict(unpermuted_six_letters=six,join_holes=holes,witnesses=seam,
                     long_cyclic_targets=len(long_cov),short_linear_targets=len(short_cov),
                     separate_union_targets=len(separate),long_forward_intervals=long_scans,
                     short_forward_intervals=short_scans)
    (args.out/'seven_target_initialized_join_certificate.json').write_text(json.dumps(seam_record,indent=2)+'\n')
    report=dict(status='PASS',source17_sha256=hashlib.sha256(raw17).hexdigest(),
                supplied18_sha256=hashlib.sha256(raw18).hexdigest(),supplied18_length=len(W),
                left_length=m,left_last_old=A[-1],left_last_new=left[-1],left_pair_union=25265,
                old_last_interior_backups_zero_based=backups,left_modified_sha256=left_sha,
                initializer_blocks=list(initial),initializer_profile=[b.bit_count() for b in initial],
                initialized_steps=len(tail),initialized_states=len(tail)+1,initialized_nonempty_targets=FULL17,
                initialized_rank8_once=len(middle8),initialized_rank9_once=len(middle9),
                full18_rank9_once=len(full_middle9),
                full18_endpoints_without_rank9_zero_based=no_middle9,
                independent_actual18_marked_witnesses_replayed=FULL17,
                lambda17_equals_width_minus_one=True,lambda17_value=24309,
                permutation_one_based=list(PI),inverse_permutation_one_based=inverse,
                recovered_Q_length=len(Q),recovered_R_length=len(R),
                reverse_R_start_phase_zero_based=start_phase,reverse_R_omitted_phase_zero_based=omitted,
                omitted_letter=reverse_R[omitted],unique_phase_lookup='linear-time KMP on known doubled reverse R',
                initializer_matches_periodic_state_after_omitted_letter=True,
                regenerated_from17_byte_equal_to_supplied18=True,
                regenerated18_sha256=hashlib.sha256(regenerated_raw).hexdigest(),
                initializer_unpermuted_blocks=list(initial_unpermuted),
                **seam_record,
                scope='Exact supplied words, one specified coordinate permutation, and one unique cyclic phase lookup. No search over constructions.',
                resource_caps=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=1024**3),
                host=platform.node(),elapsed_seconds=time.monotonic()-started)
    (args.out/'optimal18_initialized_structure_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':main()
