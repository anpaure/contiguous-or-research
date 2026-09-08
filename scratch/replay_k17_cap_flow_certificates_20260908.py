#!/usr/bin/env python3
"""Independent assignment/Hall-certificate replay; no optimization. h100 only."""
import hashlib
import json
import resource
import signal
import time
from collections import Counter
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (120,120))
resource.setrlimit(resource.RLIMIT_AS, (2*1024**3,2*1024**3))
signal.alarm(150)
started=time.monotonic()
directory=Path('/home/amodo/exact-b-k17-capped-low-flows-20260908')
source=Path('/home/amodo/exact-b-k17-height-adaptive-20260908/height_adaptive_canonical_cycles.json')
raw=source.read_bytes(); records=json.loads(raw); full=(1<<17)-1
data={}; multiplicity=Counter(); edited=Counter(); anchors=Counter()
for rec in records:
    if rec['height']<3: continue
    X=[full ^ x for x in rec['lower_owners']]; v=len(X)
    assert v % 2 == 1
    for i in range(v):
        D=X[i]&X[(i+1)%v]&X[(i+2)%v]&X[(i+3)%v]
        pin=(X[i]&~X[(i-1)%v]) | (X[(i+3)%v]&~X[(i+4)%v])
        assert D.bit_count()==6 and pin and pin&D==pin
        data[rec['cycle'],i]=(D,pin)
        multiplicity[D]+=1
        if i in range(0,v-1,2): edited[D]+=1
        else: anchors[D]+=1
assignment=json.loads((directory/'unrestricted_assignment.json').read_text())
used_targets=set(); used_positions=set(); group_use=Counter()
for target,cid,i,label,pin in assignment:
    assert 1<=target.bit_count()<=5 and target not in used_targets
    assert (cid,i) not in used_positions
    assert data[cid,i]==(label,pin)
    assert pin&target==pin and target&label==target
    used_targets.add(target); used_positions.add((cid,i)); group_use[label]+=1
assert all(group_use[g]<=multiplicity[g]-1 for g in multiplicity)
hall=json.loads((directory/'unrestricted_hall_cut_certificate.json').read_text())
S=set(hall['target_masks'])
assert len(S)==len(hall['target_masks']) and all(1<=s.bit_count()<=5 for s in S)
# This time test each prescribed target directly against every physical position;
# do not reuse the flow program's submask-edge generator or residual network.
neighbors=set()
for target in S:
    for pos,(D,pin) in data.items():
        if pin&target==pin and target&D==target:
            neighbors.add(pos)
assert neighbors==set(map(tuple,hall['neighbor_positions']))
by_group=Counter(data[pos][0] for pos in neighbors)
capacity=sum(min(count,multiplicity[g]-1) for g,count in by_group.items())
assert capacity==hall['available_capacity']==612
assert len(S)==1768 and len(neighbors)==6256
assert 9401-(len(S)-capacity)==len(assignment)==8245
actual_rows=[[g,by_group[g],multiplicity[g]-1,min(by_group[g],multiplicity[g]-1)] for g in sorted(by_group)]
assert actual_rows==hall['group_rows']
frame_capacity=sum(edited[g] if anchors[g] else edited[g]-1 for g in multiplicity)
assert frame_capacity==7013 and sum(edited.values())==11009
assert sum(multiplicity.values())==22134 and len(multiplicity)==12376
assert sum(1 for g in multiplicity if anchors[g])==8380
frame_rows=[[g,multiplicity[g],edited[g],anchors[g],edited[g] if anchors[g] else edited[g]-1] for g in sorted(multiplicity)]
assert frame_rows==json.loads((directory/'canonical_alternating_group_capacity_certificate.json').read_text())
report=dict(status='PASS_INDEPENDENT_CERTIFICATE_REPLAY',input_sha256=hashlib.sha256(raw).hexdigest(),
    verified_matching_lower_bound=len(assignment),verified_hall_upper_bound=8245,
    exact_unrestricted_maximum=8245,hall_target_count=len(S),hall_neighbor_positions=len(neighbors),hall_capacity=capacity,
    hall_target_rank_counts=dict(sorted(Counter(s.bit_count() for s in S).items())),
    hall_group_count=len(by_group),hall_groups_with_zero_capacity=sum(multiplicity[g]==1 for g in by_group),
    hall_group_usable_capacity_histogram=dict(sorted(Counter(min(count,multiplicity[g]-1) for g,count in by_group.items()).items())),
    canonical_frame_editable_positions=sum(edited.values()),canonical_frame_capacity=frame_capacity,
    canonical_frame_scalar_deficiency=9401-frame_capacity,
    no_optimization_run=True,elapsed_seconds=time.monotonic()-started,
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(directory/'independent_certificate_replay.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True)
