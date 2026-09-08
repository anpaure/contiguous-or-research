#!/usr/bin/env python3
"""Exact individual-host census for one fixed periodic PBBS bank; h100 only."""
import hashlib
import json
import resource
import signal
import time
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
signal.alarm(150)
started=time.monotonic()
INPUT=Path('/home/amodo/exact-b-k17-height-adaptive-20260908/height_adaptive_canonical_cycles.json')
OUT=Path('/home/amodo/exact-b-k17-capped-short-hosts-20260908')
OUT.mkdir(parents=True,exist_ok=True)
raw=INPUT.read_bytes(); records=json.loads(raw)
N=17; FULL=(1<<N)-1
first=[None]*(FULL+1)
host_counts=[0]*(FULL+1)
banks={}
singleton_intervals=[[] for _ in range(N)]
singleton_positions=[set() for _ in range(N)]
interval_count=0; enumerated_count=0; minimum_owner_checks=0
pin_window_checks=0; initial_owner_checks=0
by_height=Counter(); by_cap=Counter()

def mask_or(values):
    result=0
    for value in values: result |= value
    return result

for rec in records:
    cid=rec['cycle']; h=rec['height']; H=min(h,3)
    X=[FULL^a for a in rec['lower_owners']]; v=len(X)
    assert H<v and v==rec['length']
    D=[]
    for i in range(v):
        value=FULL
        for z in range(H+1): value &= X[(i+z)%v]
        assert value
        D.append(value)
    for j in range(v):
        assert mask_or(D[(j+z)%v] for z in range(H+1))==X[(j+H)%v]
        initial_owner_checks+=1
    pin=[]
    for i in range(v):
        demand=0
        for j in range(i-H,i+1):
            outside=mask_or(D[z%v] for z in range(j,j+H+1) if z%v!=i)
            demand |= X[(j+H)%v] & ~outside
            pin_window_checks+=1
        formula=(X[i]&~X[(i-1)%v]) | (X[(i+H)%v]&~X[(i+H+1)%v])
        assert demand==formula and demand and demand&D[i]==demand
        pin.append(demand)
    banks[cid]=(X,D,pin,H,h)
    for i in range(v):
        F=V=0
        for ell in range(1,H+1):
            z=(i+ell-1)%v; F |= pin[z]; V |= D[z]
            interval=set((i+u)%v for u in range(ell))
            affected=list(range(i-H,i+ell))
            exact=0
            for j in affected:
                outside=mask_or(D[z%v] for z in range(j,j+H+1) if z%v not in interval)
                exact |= X[(j+H)%v] & ~outside
            assert exact==F
            assert all(D[z]&F for z in interval)
            for j in affected:
                value=mask_or((D[z%v]&F) if z%v in interval else D[z%v]
                              for z in range(j,j+H+1))
                assert value==X[(j+H)%v]
                minimum_owner_checks+=1
            interval_count+=1
            free=V&~F; sub=free
            while True:
                target=F|sub
                enumerated_count+=1
                rank=target.bit_count()
                if rank<=8:
                    host_counts[target]+=1
                    by_height[h]+=1; by_cap[H]+=1
                    if first[target] is None: first[target]=[cid,i,ell]
                    if rank==1:
                        bit=target.bit_length()-1
                        singleton_intervals[bit].append([cid,i,ell])
                        singleton_positions[bit].update((cid,z) for z in interval)
                if not sub: break
                sub=(sub-1)&free

assert len(records)==146 and initial_owner_checks==24310
covered=[t for t in range(1,FULL+1) if t.bit_count()<=8 and first[t] is not None]
missing=[t for t in range(1,FULL+1) if t.bit_count()<=8 and first[t] is None]
assert len(covered)+len(missing)==65535
replay_windows=0
for target in covered:
    cid,i,ell=first[target]
    X,D,pin,H,h=banks[cid]; v=len(X)
    interval=set((i+u)%v for u in range(ell))
    capped={z:D[z]&target for z in interval}
    assert all(capped.values()) and mask_or(capped.values())==target
    for j in range(i-H,i+ell):
        assert mask_or(capped.get(z%v,D[z%v]) for z in range(j,j+H+1))==X[(j+H)%v]
        replay_windows+=1

singletons=[]
for bit in range(N):
    positions=sorted(singleton_positions[bit])
    components=sorted(set(cid for cid,i in positions))
    singletons.append(dict(coordinate=bit+1,mask=1<<bit,
        interval_host_count=len(singleton_intervals[bit]),
        interval_length_histogram=dict(sorted(Counter(a[2] for a in singleton_intervals[bit]).items())),
        distinct_position_count=len(positions),distinct_component_count=len(components),
        position_original_height_histogram=dict(sorted(Counter(banks[cid][4] for cid,i in positions).items())),
        position_capped_depth_histogram=dict(sorted(Counter(banks[cid][3] for cid,i in positions).items())),
        components=components,positions=positions,interval_hosts=singleton_intervals[bit]))

report=dict(status='PASS',scope='Individual short caps on the unchanged 146-cycle canonical periodic bank. No simultaneous assignment, upper-rank preservation, or linear-word claim.',
    dimension=N,component_count=len(records),period_positions=initial_owner_checks,
    input_file=str(INPUT),input_sha256=hashlib.sha256(raw).hexdigest(),
    cap_depth='H=min(original invariant height,3)',indexing='zero-based canonical cycle and cyclic position',
    owner_convention='X_i=full complement of stored lower owner; D_i=intersection X_i through X_(i+H); OR D_j through D_(j+H)=X_(j+H)',
    source_positions_by_original_height=dict(sorted(Counter({h:sum(len(b[0]) for b in banks.values() if b[4]==h) for h in range(1,9)}).items())),
    source_positions_by_cap_depth=dict(sorted(Counter({H:sum(len(b[0]) for b in banks.values() if b[3]==H) for H in range(1,4)}).items())),
    owner_windows_reconstructed=initial_owner_checks,pin_exclusion_windows_checked=pin_window_checks,
    all_pins_equal_entry_exit_formula=True,all_pins_nonzero=True,
    short_intervals_checked=interval_count,all_interval_exact_deficits_equal_union_pins=True,
    minimum_cap_owner_windows_rechecked=minimum_owner_checks,
    submasks_enumerated_including_ranks_above_eight=enumerated_count,
    lower_target_host_incidences=sum(host_counts),
    host_incidences_by_original_height=dict(sorted(by_height.items())),host_incidences_by_cap_depth=dict(sorted(by_cap.items())),
    covered_lower_targets=len(covered),covered_rank_counts=dict(sorted(Counter(t.bit_count() for t in covered).items())),
    missing_lower_targets=len(missing),missing_rank_counts=dict(sorted(Counter(t.bit_count() for t in missing).items())),missing_masks=missing,
    distinct_covered_first_hosts_replayed=len(covered),first_host_owner_windows_rechecked=replay_windows,
    singleton_hosts=singletons,resource_caps=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3),
    elapsed_seconds=time.monotonic()-started)
(OUT/'capped_short_host_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'capped_short_target_first_hosts.json').write_text(json.dumps({str(t):first[t] for t in covered})+'\n')
(OUT/'capped_short_target_host_counts.json').write_text(json.dumps({str(t):host_counts[t] for t in covered})+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('missing_masks','singleton_hosts')},indent=2),flush=True)
print('SINGLETONS',json.dumps([{k:v for k,v in d.items() if k not in ('positions','interval_hosts','components')} for d in singletons]),flush=True)
print('MISSING',missing,flush=True)
