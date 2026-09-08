#!/usr/bin/env python3
"""REVIEW BEFORE RUN: one named-target carrier comparison, h100 only.

No trial switch, solver, optimization, coordinate-permutation search, or
new construction is attempted. Four fixed oriented matching comparisons
and their orientation-free incidence comparison are all reported.
"""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from collections import Counter
from pathlib import Path

N=17
FULL=(1<<N)-1
SOURCE_SHA='7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
PBBS_SHA='fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3'


def rot(mask):
    return ((mask<<1)&FULL)|(mask>>(N-1))


def union_masks(masks):
    result=0
    for mask in masks:result|=mask
    return result


def intersect_masks(masks):
    result=FULL
    for mask in masks:result&=mask
    return result


def dump(path,body):
    path.write_text(json.dumps(body,separators=(',',':'))+'\n')


def native_data(cycles):
    records={}
    for cycle in cycles:
        lower=cycle['lower_owners'];v=cycle['length']
        assert len(lower)==v and all(x.bit_count()==8 for x in lower)
        upper=[FULL^x for x in lower]
        facets=[upper[i]&upper[(i+1)%v] for i in range(v)]
        for i,L in enumerate(facets):
            assert L.bit_count()==8 and L not in records
            successor=facets[(i+1)%v]
            U=upper[(i+1)%v]
            assert L!=successor and L|successor==U and U.bit_count()==9
            records[L]=dict(lower=L,successor=successor,outgoing=U,incoming=upper[i],
                            cycle=cycle['cycle'],position=i,height=cycle['height'],
                            insertion=successor&~L,deletion=L&~successor)
    return records


def actual_data(words):
    records={}
    for cid,word in enumerate(words):
        v=len(word)
        lower=[union_masks(word[(i+j)%v] for j in range(3)) for i in range(v)]
        upper=[union_masks(word[(i+j)%v] for j in range(4)) for i in range(v)]
        envelope=[intersect_masks(upper[(i-j)%v] for j in range(4)) for i in range(v)]
        for i,L in enumerate(lower):
            nxt=(i+1)%v;successor=lower[nxt];U=upper[i]
            assert L.bit_count()==8 and U.bit_count()==9 and L not in records
            assert successor!=L and L|successor==U
            assert envelope[i].bit_count()==6 and word[i]&~envelope[i]==0
            assert word[i]|word[nxt]==envelope[i]|envelope[nxt]
            assert (envelope[i]|envelope[nxt]).bit_count()==7
            pin=(envelope[i]&~envelope[(i-1)%v])|(envelope[i]&~envelope[nxt])
            assert pin&~word[i]==0
            records[L]=dict(lower=L,successor=successor,outgoing=U,incoming=upper[(i-1)%v],
                            cycle=cid,position=i,letter=word[i],envelope=envelope[i],pins=pin,
                            insertion=successor&~L,deletion=L&~successor)
    return records


def verify_factor(records):
    assert len(records)==24310
    labels=set(records)
    assert len({v['outgoing'] for v in records.values()})==len(labels)
    assert len({v['incoming'] for v in records.values()})==len(labels)
    assert {v['successor'] for v in records.values()}==labels
    assert {v['outgoing'] for v in records.values()}=={v['incoming'] for v in records.values()}
    for L,row in records.items():
        assert row['incoming']!=row['outgoing']
        assert row['outgoing']==records[row['successor']]['incoming']
        assert row['insertion'].bit_count()==row['deletion'].bit_count()==1
        assert row['outgoing']==L|row['insertion']


def temporal_violations(records):
    violations=[]
    for L,row in sorted(records.items()):
        next1=records[row['successor']]
        next2=records[next1['successor']]
        bad=[j for j,t in ((1,next1),(2,next2)) if row['insertion']==t['deletion']]
        if bad:violations.append(dict(lower=L,insertion=row['insertion'],delays=bad,
                                       cycle=row['cycle'],height=row.get('height')))
    return violations


def matching_difference(native,actual,native_side,actual_side):
    inverse={row[native_side]:L for L,row in native.items()}
    theta={L:inverse[row[actual_side]] for L,row in actual.items()}
    assert set(theta)==set(theta.values())
    seen=set();circuits=[];lengths=Counter();shapes=Counter();unchanged=0
    for start in sorted(theta):
        if start in seen:continue
        cycle=[];L=start
        while L not in seen:
            seen.add(L);cycle.append(L);L=theta[L]
        assert L==start
        if len(cycle)==1:
            unchanged+=1
            assert native[start][native_side]==actual[start][actual_side]
            continue
        old=[native[L][native_side] for L in cycle]
        new=[actual[L][actual_side] for L in cycle]
        assert new==old[1:]+old[:1]
        core=intersect_masks(cycle);universe=union_masks(old+new)
        assert core&~universe==0
        lengths[len(cycle)]+=1
        shape=(len(cycle),core.bit_count(),(universe&~core).bit_count())
        shapes[shape]+=1
        circuits.append(dict(lower_cycle=cycle,old_upper=old,new_upper=new,common_core=core,
                             active_coordinates=universe&~core,
                             native_components=sorted({native[L]['cycle'] for L in cycle}),
                             native_heights=sorted({native[L]['height'] for L in cycle})))
    assert unchanged+sum(len(c['lower_cycle']) for c in circuits)==24310
    return dict(native_side=native_side,actual_side=actual_side,unchanged=unchanged,
                changed=24310-unchanged,nontrivial_circuit_count=len(circuits),
                circuit_lengths=sorted(lengths.items()),
                circuit_shapes=[dict(length=k[0],common_core_rank=k[1],active_coordinate_count=k[2],count=v)
                                for k,v in sorted(shapes.items())],circuits=circuits)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--word',type=Path,required=True)
    ap.add_argument('--canonical',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    assert platform.node().split('.')[0]=='arboghast','h100 only'
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    signal.alarm(45);started=time.monotonic()
    word_raw=args.word.read_bytes();native_raw=args.canonical.read_bytes()
    assert hashlib.sha256(word_raw).hexdigest()==SOURCE_SHA
    assert hashlib.sha256(native_raw).hexdigest()==PBBS_SHA
    word=[int(x) for x in word_raw.decode('ascii').splitlines() if x.strip()]
    assert len(word)==24313 and all(0<x<=FULL for x in word)
    Q,R=word[:85],word[86:-2]
    assert len(Q)==85 and len(R)==24225 and word==Q+[Q[0]]+R+R[:2]
    canonical=json.loads(native_raw)
    assert len(canonical)==146
    native=native_data(canonical);actual=actual_data([Q,R])
    verify_factor(native);verify_factor(actual)
    assert set(native)==set(actual)
    args.out.mkdir(parents=True,exist_ok=False)
    dump(args.out/'actual_named_middle_carrier.json',[actual[L] for L in sorted(actual)])
    dump(args.out/'canonical_named_middle_carrier.json',[native[L] for L in sorted(native)])

    actual_bad=temporal_violations(actual)
    native_bad=temporal_violations(native)
    assert not actual_bad
    dump(args.out/'native_temporal_exclusion_violations.json',native_bad)

    # Named lower labels eliminate arbitrary phase and component numbering.
    # Unordered incident upper labels also eliminate orientation choices.
    shared=Counter();changed_by_height=Counter();successor_same=0;rows=[]
    for L in sorted(actual):
        a,n=actual[L],native[L]
        old={n['outgoing'],n['incoming']};new={a['outgoing'],a['incoming']}
        common=len(old&new);shared[common]+=1
        if common<2:changed_by_height[n['height']]+=1
        successor_same+=a['successor']==n['successor']
        rows.append(dict(lower=L,native_cycle=n['cycle'],native_height=n['height'],
                         shared_middle_incidences=common,
                         native_in=n['incoming'],native_out=n['outgoing'],
                         actual_in=a['incoming'],actual_out=a['outgoing'],
                         native_successor=n['successor'],actual_successor=a['successor']))
    dump(args.out/'all_named_incidence_differences.json',rows)

    differences=[]
    for nside in ('outgoing','incoming'):
        for aside in ('outgoing','incoming'):
            result=matching_difference(native,actual,nside,aside)
            filename=f'alternating_circuits_native_{nside}_actual_{aside}.json'
            dump(args.out/filename,result)
            differences.append({k:v for k,v in result.items() if k!='circuits'}|dict(artifact=filename))

    # Recover exact physical rotation orbits. Nothing is assumed about
    # equivariance of the supplied matching maps or refined letters.
    orbit={};representatives=[]
    for L in sorted(actual):
        if L in orbit:continue
        oi=len(representatives);representatives.append(L);mask=L
        for shift in range(N):
            assert mask in actual and mask not in orbit
            orbit[mask]=(oi,shift);mask=rot(mask)
        assert mask==L
    assert len(representatives)==1430
    equivariance={}
    for name,records,fields in (
        ('native',native,('successor','outgoing','incoming')),
        ('actual',actual,('successor','outgoing','incoming','letter','envelope','pins'))):
        equivariance[name]={}
        for field in fields:
            bad=[L for L in sorted(records) if records[rot(L)][field]!=rot(records[L][field])]
            equivariance[name][field]=dict(violations=len(bad),first_examples=bad[:20])
    assert all(v['violations']==0 for v in equivariance['native'].values())
    quotient=[]
    for oi,L in enumerate(representatives):
        a,n=actual[L],native[L]
        aj,ashift=orbit[a['successor']];nj,nshift=orbit[n['successor']]
        quotient.append(dict(row=oi,lower=L,actual_outgoing=a['outgoing'],actual_incoming=a['incoming'],
                             actual_insertion=a['insertion'],actual_deletion=a['deletion'],
                             actual_successor_row=aj,actual_successor_shift=ashift,
                             actual_letter=a['letter'],actual_envelope=a['envelope'],actual_pins=a['pins'],
                             native_outgoing=n['outgoing'],native_incoming=n['incoming'],
                             native_successor_row=nj,native_successor_shift=nshift))
    dump(args.out/'recovered_1430_canonical_rotation_rows.json',quotient)

    lower_compiler=dict(literal_rank_occurrences=sorted(Counter(r['letter'].bit_count() for r in actual.values()).items()),
                        literal_distinct_targets=len({r['letter'] for r in actual.values()}),
                        envelope_rank_occurrences=sorted(Counter(r['envelope'].bit_count() for r in actual.values()).items()),
                        distinct_rank6_envelopes=len({r['envelope'] for r in actual.values()}),
                        pin_rank_occurrences=sorted(Counter(r['pins'].bit_count() for r in actual.values()).items()),
                        pair_preservation_checks=len(actual))
    report=dict(status='PASS',word17_sha256=SOURCE_SHA,canonical_sha256=PBBS_SHA,
                scope='One specified literal two-cycle carrier versus one specified canonical PBBS carrier. No construction search or trial switches.',
                actual_component_lengths=[len(Q),len(R)],canonical_components=len(canonical),
                lower_labels=len(actual),upper_labels=len({r['outgoing'] for r in actual.values()}),
                shared_unoriented_incidences_per_lower=sorted(shared.items()),
                total_common_middle_incidences=sum(k*v for k,v in shared.items()),
                changed_incidence_lower_labels_by_native_height=sorted(changed_by_height.items()),
                unchanged_native_forward_successors=successor_same,
                actual_temporal_violations=len(actual_bad),native_temporal_violations=len(native_bad),
                native_temporal_violations_by_height=sorted(Counter(x['height'] for x in native_bad).items()),
                matching_differences=differences,rotation_equivariance=equivariance,
                quotient_row_count=len(quotient),quotient_scope='Rows determine the full object only for fields whose equivariance violation count is zero.',
                lower_compiler=lower_compiler,
                resource_caps=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=1024**3),
                host=platform.node(),elapsed_seconds=time.monotonic()-started)
    (args.out/'optimal_vs_pbbs_carrier_comparison_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':main()
