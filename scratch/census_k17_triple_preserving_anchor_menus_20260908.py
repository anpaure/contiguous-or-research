#!/usr/bin/env python3
"""Fixed H3 short hosts and one canonical width-three anchor catalogue; h100 only."""
import hashlib
import itertools
import json
import resource
import signal
import time
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
signal.alarm(150)
started=time.monotonic()
INPUT=Path('/home/amodo/exact-b-k17-height-adaptive-20260908/height_adaptive_canonical_cycles.json')
OUT=Path('/home/amodo/exact-b-k17-triple-anchor-menus-20260908')
OUT.mkdir(parents=True,exist_ok=True)
raw=INPUT.read_bytes(); records=json.loads(raw)
FULL=(1<<17)-1
all_lower=[s for s in range(1,FULL+1) if s.bit_count()<=7]
rank6=[s for s in all_lower if s.bit_count()==6]
rank7=[s for s in all_lower if s.bit_count()==7]
assert len(all_lower)==41225

def vor(values):
    ans=0
    for value in values: ans|=value
    return ans

def caps(F,V):
    free=V&~F; sub=free; result=[]
    while True:
        result.append(F|sub)
        if sub==0: break
        sub=(sub-1)&free
    return sorted(result)

def rank_counts(values): return dict(sorted(Counter(t.bit_count() for t in values).items()))

banks={}; fixed_low=set(); fixed_components=[]
single_counts=[0]*(FULL+1); pair_counts=[0]*(FULL+1)
first=[None]*(FULL+1)
short_intervals=0; short_incidences=0; short_owner_checks=0; pin_checks=0
for rec in records:
    cid=rec['cycle']; h=rec['height']; H=min(h,3)
    X=[FULL^a for a in rec['lower_owners']]; v=len(X)
    D=[]
    for i in range(v):
        m=FULL
        for j in range(H+1): m &= X[(i+j)%v]
        D.append(m)
    assert all(d.bit_count()==9-H for d in D)
    if H<3:
        fixed_components.append(cid)
        for i in range(v):
            m=0
            for ell in range(1,v+1):
                m|=D[(i+ell-1)%v]
                if m.bit_count()>7: break
                fixed_low.add(m)
        continue
    assert all((D[i]|D[(i+1)%v]).bit_count()==7 for i in range(v))
    R=[D[i]|D[(i+1)%v]|D[(i+2)%v] for i in range(v)]
    assert all(t.bit_count()==8 for t in R)
    assert all(vor(D[(i+j)%v] for j in range(4))==X[(i+3)%v] for i in range(v))
    pin=[]
    for i in range(v):
        demand=0
        for j in range(i-2,i+1):
            demand |= R[j%v]&~vor(D[z%v] for z in range(j,j+3) if z%v!=i)
            pin_checks+=1
        formula=(X[i]&~X[(i-1)%v])|(X[(i+3)%v]&~X[(i+4)%v])
        assert demand==formula and demand and demand&D[i]==demand
        pin.append(demand)
    banks[cid]=(D,pin,R,h)
    for i in range(v):
        F=V=0
        for ell in (1,2):
            z=(i+ell-1)%v; F|=pin[z]; V|=D[z]
            positions={(i+j)%v for j in range(ell)}
            demand=0
            for j in range(i-2,i+ell):
                demand |= R[j%v]&~vor(D[z%v] for z in range(j,j+3) if z%v not in positions)
            assert demand==F
            E={z:D[z]&F for z in positions}
            assert all(E.values())
            for j in range(i-2,i+ell):
                assert vor(E.get(z%v,D[z%v]) for z in range(j,j+3))==R[j%v]
                short_owner_checks+=1
            short_intervals+=1
            menu=caps(F,V)
            for target in menu:
                assert 1<=target.bit_count()<=7
                (single_counts if ell==1 else pair_counts)[target]+=1
                if first[target] is None: first[target]=[cid,i,ell]
            short_incidences+=len(menu)

individual_seen=fixed_low|{t for t in all_lower if first[t] is not None}
individual_missing=sorted(set(all_lower)-individual_seen)
individual_no_pair6=[t for t in rank6 if pair_counts[t]==0]
individual=dict(frozen_component_count=len(fixed_components),h3_component_count=len(banks),
    h3_positions=sum(len(b[0]) for b in banks.values()),fixed_lower_count=len(fixed_low),fixed_rank_counts=rank_counts(fixed_low),
    exact_pin_exclusion_windows=pin_checks,short_intervals=short_intervals,short_host_incidences=short_incidences,
    short_minimum_cap_triple_replays=short_owner_checks,all_pins_and_interval_deficits_exact=True,
    covered_count=len(individual_seen),covered_rank_counts=rank_counts(individual_seen),
    missing_count=len(individual_missing),missing_rank_counts=rank_counts(individual_missing),missing_masks=individual_missing,
    rank6_with_pair_host=len(rank6)-len(individual_no_pair6),rank6_without_pair_host=len(individual_no_pair6),
    mandatory_literal_rank6_masks=individual_no_pair6)
print('INDIVIDUAL',json.dumps({k:v for k,v in individual.items() if not k.endswith('masks')}),flush=True)

fixed_frame=set(fixed_low); frame_seen=set(fixed_low); frame_pair=set()
anchor_count=0; editable_count=0; boundary_pair_count=0; triple_checks=0
option_count=0; block_records=[]; cycle_records=[]
frame_first={}; block_length_hist=Counter(); cap_size_hist=Counter(); option_count_hist=Counter()
internal_rank7_providers={}
for cid,(D,pin,R,h) in banks.items():
    v=len(D); anchors=list(range(0,v,3)); anchor_set=set(anchors)
    minimum=[D[i] if i in anchor_set else pin[i] for i in range(v)]
    assert all(minimum)
    for i in range(v):
        assert vor(minimum[(i+j)%v] for j in range(3))==R[i]
        triple_checks+=1
        if i in anchor_set: fixed_frame.add(D[i])
        if i in anchor_set or (i+1)%v in anchor_set:
            value=D[i]|D[(i+1)%v]
            assert minimum[i]|minimum[(i+1)%v]==value
            fixed_frame.add(value); boundary_pair_count+=1
    anchor_count+=len(anchors); editable_count+=v-len(anchors)
    cycle_records.append(dict(cycle=cid,height=h,period=v,anchors=anchors,source=D,pins=pin))
    for j,a in enumerate(anchors):
        b=anchors[j+1] if j+1<len(anchors) else v
        positions=list(range(a+1,b))
        if not positions: continue
        assert len(positions) in (1,2)
        menus=[caps(pin[i],D[i]) for i in positions]
        assert all(len(m)<=32 for m in menus)
        for m in menus: cap_size_hist[len(m)]+=1
        count=1
        for m in menus: count*=len(m)
        assert count<=1024
        bid=len(block_records); local_seen=set(); local_pair=set()
        original_pair=vor(D[i] for i in positions) if len(positions)==2 else None
        retaining=0
        for choice in itertools.product(*menus):
            assert all(choice)
            targets=set(choice)
            if len(choice)==2:
                pair=choice[0]|choice[1]
                targets.add(pair);local_pair.add(pair)
                retaining+=pair==original_pair
            for target in targets:
                assert 1<=target.bit_count()<=7
                local_seen.add(target)
                if target not in frame_first: frame_first[target]=[bid,list(choice)]
        frame_seen.update(local_seen);frame_pair.update(local_pair)
        option_count+=count;block_length_hist[len(positions)]+=1;option_count_hist[count]+=1
        if original_pair is not None:
            assert original_pair.bit_count()==7
            assert retaining>0
            internal_rank7_providers.setdefault(original_pair,[]).append(bid)
        block_records.append(dict(block=bid,cycle=cid,positions=positions,letter_menus=menus,
            option_count=count,original_internal_rank7=original_pair,
            options_retaining_internal_rank7=retaining,
            possible_local_target_count=len(local_seen),possible_local_rank_counts=rank_counts(local_seen),
            possible_internal_pair_rank_counts=rank_counts(local_pair)))

frame_seen.update(fixed_frame)
frame_missing=sorted(set(all_lower)-frame_seen)
frame_no_pair6=[t for t in rank6 if t not in frame_pair]
mandatory6_unfixed=[t for t in frame_no_pair6 if t not in fixed_frame]
required7=[t for t in rank7 if t not in fixed_frame]
required7_missing=[t for t in required7 if t not in internal_rank7_providers]
required7_provider_hist=Counter(len(internal_rank7_providers.get(t,[])) for t in required7)
frame=dict(anchor_rule='Within each canonical H3 cycle anchors are positions 0,3,6,...; H1/H2 fully frozen.',
    anchor_count=anchor_count,editable_position_count=editable_count,
    editable_block_count=len(block_records),block_length_histogram=dict(sorted(block_length_hist.items())),
    per_position_cap_count_histogram=dict(sorted(cap_size_hist.items())),
    total_cartesian_options_enumerated=option_count,per_block_option_count_histogram=dict(sorted(option_count_hist.items())),
    all_global_minimum_caps_preserve_triples=True,global_minimum_triples_replayed=triple_checks,
    all_anchor_boundary_pairs_unchanged=True,anchor_boundary_pair_occurrences_replayed=boundary_pair_count,
    fixed_target_count=len(fixed_frame),fixed_rank_counts=rank_counts(fixed_frame),
    possible_target_count=len(frame_seen),possible_rank_counts=rank_counts(frame_seen),
    missing_count=len(frame_missing),missing_rank_counts=rank_counts(frame_missing),missing_masks=frame_missing,
    rank6_with_internal_pair_host=len(rank6)-len(frame_no_pair6),rank6_without_internal_pair_host=len(frame_no_pair6),
    mandatory_literal_rank6_masks=frame_no_pair6,
    mandatory_literal_rank6_already_fixed=len(frame_no_pair6)-len(mandatory6_unfixed),
    mandatory_literal_rank6_requiring_editable_literal=len(mandatory6_unfixed),
    mandatory_editable_literal_rank6_masks=mandatory6_unfixed,
    unique_rank7_labels_requiring_internal_preservation=len(required7),required_rank7_masks=required7,
    required_rank7_provider_count_histogram=dict(sorted(required7_provider_hist.items())),
    required_rank7_with_no_provider=required7_missing)

menu=dict(format_version=1,scope='Exact Cartesian-product menus for ONE fixed width-three anchor frame; no options selected.',
    option_encoding='For each block choose one mask independently from each letter_menus entry. Cartesian order agrees with itertools.product. Local lower targets are chosen letters and their OR for length-two blocks.',
    input_sha256=hashlib.sha256(raw).hexdigest(),cycles=cycle_records,blocks=block_records,
    fixed_target_masks=sorted(fixed_frame),required_rank7_providers={str(t):internal_rank7_providers.get(t,[]) for t in required7},
    mandatory_editable_literal_rank6_masks=mandatory6_unfixed)
menu_raw=(json.dumps(menu,separators=(',',':'))+'\n').encode()
assert len(menu_raw)<100*1024**2
(OUT/'canonical_w3_anchor_factorized_menus.json').write_bytes(menu_raw)
(OUT/'canonical_w3_anchor_target_first_options.json').write_text(json.dumps({str(t):v for t,v in sorted(frame_first.items())})+'\n')
(OUT/'individual_triple_preserving_first_hosts.json').write_text(json.dumps({str(t):first[t] for t in all_lower if first[t] is not None})+'\n')
(OUT/'individual_triple_preserving_host_counts.json').write_text(json.dumps({str(t):[single_counts[t],pair_counts[t]] for t in all_lower if single_counts[t] or pair_counts[t]})+'\n')
report=dict(status='PASS',scope='Individual feasibility and the union of all options in one fixed canonical anchor frame, not a simultaneous covering selection or a linear word.',
    dimension=17,input_file=str(INPUT),input_sha256=hashlib.sha256(raw).hexdigest(),
    individual=individual,anchor_frame=frame,menu_file='canonical_w3_anchor_factorized_menus.json',
    menu_bytes=len(menu_raw),menu_sha256=hashlib.sha256(menu_raw).hexdigest(),
    resource_caps=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3),elapsed_seconds=time.monotonic()-started)
(OUT/'triple_preserving_host_and_anchor_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print('ANCHOR',json.dumps({k:v for k,v in frame.items() if not k.endswith('masks')}),flush=True)
print('FINAL',json.dumps({k:v for k,v in report.items() if k not in ('individual','anchor_frame')}),flush=True)
