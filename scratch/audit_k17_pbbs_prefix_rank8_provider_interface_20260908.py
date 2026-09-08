#!/usr/bin/env python3
"""Exact five-target check for the frozen306/308 prefix; execute on h100 only."""
import json
from pathlib import Path
P=list(map(int,Path('badsix_relaxed_306_owner_path.word').read_text().split()))
E=list(map(int,Path('badsix_relaxed_308_depth2_source.word').read_text().split()))
H=[21866,43860,46420,70998,92834]
assert len(P)==306 and len(E)==308
assert all(E[i]|E[i+1]|E[i+2]==p for i,p in enumerate(P))
occ={s:[] for s in H}
for i in range(len(E)):
    x=0
    for j in range(i,len(E)):
        x|=E[j]
        if x in occ: occ[x].append([i,j])
        if x==(1<<17)-1: break
required=P[-1]&~E[305]
records={}
for s in H:
    sups=[s|(1<<b) for b in range(17) if not(s>>b&1)]
    inside=[i for i,t in enumerate(P) if s&t==s]
    outside=[t for t in sups if t not in set(P)]
    records[str(s)]={'all_source_witnesses':occ[s],'stable_source_witnesses':[a for a in occ[s] if a[1]<=305],'boundary_dependent_source_witnesses':[a for a in occ[s] if a[1]>=306],'prefix_superowner_positions':inside,'remaining_Q_superowners':outside,'initial_owner_contains':s&P[0]==s,'last_prefix_owner_contains':s&P[-1]==s,'contains_pivot_required_bits':s&required==required}
    assert not occ[s] and len(inside)==2 and len(outside)==7
    assert not records[str(s)]['last_prefix_owner_contains']
    assert not records[str(s)]['contains_pivot_required_bits']
A=E.copy(); A[0]=H[0]
assert all(A[i]|A[i+1]|A[i+2]==p for i,p in enumerate(P))
assert E[1]&1
out={'indexing':'zero based','source_length':len(E),'fixed_positions':[0,305],'attachment_changed_positions':[306,307],'pivot_required_mask':required,'pivot_required_bits':[b for b in range(17) if required>>b&1],'A304':E[304],'A305':E[305],'T304':P[-2],'T305':P[-1],'legal_initial_pin':{'position':0,'target':H[0],'protect_bit':0,'protect_position':1,'all_owner_rows_replayed':306},'targets':records}
Path('prefix_rank8_provider_interface.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
print('PASS: exact five-target absence, seven remaining superowners each, pivot exclusion, and legal initial pin')
