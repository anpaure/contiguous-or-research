#!/usr/bin/env python3
"""Refilter the same frozen221 templates after a certified merge. h100 only."""
import argparse
import json
import resource
import signal
from collections import Counter
from pathlib import Path

from audit import cycle_adjacency
from bank import profile, audit_candidate, source_candidate

resource.setrlimit(resource.RLIMIT_CPU, (90,90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3,1024**3))
signal.alarm(110)
BAD_IDS={115,116,118,122,129,138}


def refilter(previous_catalogue_path, previous_audit_path):
    previous=json.loads(Path(previous_catalogue_path).read_text())
    accepted=json.loads(Path(previous_audit_path).read_text())
    assert accepted['all_requested_gates_passed']
    current=previous['current_lower_cycles']
    for cid in accepted['candidate']['affected_component_ids']:
        del current[cid]
    length=len(accepted['new_lower_cycle'])
    giant=f'giant_{length}'
    current[giant]=accepted['new_lower_cycle']
    prefix=previous['prefix_owners']
    ids={a:cid for cid,cy in current.items() for a in cy}
    adj=cycle_adjacency(current.values())
    bad_nodes={a for cid,cy in current.items() if cid in {f'old_{i}' for i in BAD_IDS} for a in cy}
    frozen=json.loads(Path('six_plus_one_parent_catalogue.json').read_text())['records']
    assert len(frozen)==221
    counts=Counter()
    records=[]
    for raw in frozen:
        rec={k:raw[k] for k in ('parent','arms','blocks','rotation','common_pivot','core','pivot','old_edges','new_edges')}
        counts['parents']+=1
        old=rec['old_edges']
        rec['all_six_vertices_in_giant']=all(ids[a]==giant for edge in old for a in edge)
        if rec['all_six_vertices_in_giant']:
            counts['all_six_vertices_in_giant']+=1
        rec['old_shore_present']=all(b in adj[a] for a,b in old)
        if not rec['old_shore_present']:
            records.append(rec)
            continue
        counts['old_shore_present']+=1
        companions=[next(iter(adj[p]-{q})) for p,q in old]
        deleted=[p & ~other for (p,_),other in zip(old,companions)]
        rec['companion_owners']=companions
        rec['companion_deleted_masks']=deleted
        rec['common_companion_deletion']=(len(set(deleted))==1 and deleted[0].bit_count()==1 and bool(deleted[0]&rec['core']))
        if not rec['common_companion_deletion']:
            records.append(rec)
            continue
        counts['common_companion_deletion']+=1
        affected=sorted({ids[a] for edge in old for a in edge})
        rec['affected_component_ids']=affected
        rec['affected_lengths']=[len(current[cid]) for cid in affected]
        rec['touches_giant']=giant in affected
        rec['prefix_untouched']=not ({a for edge in old for a in edge}&bad_nodes)
        rec['three_distinct_components']=len(affected)==3
        if rec['touches_giant']:
            counts['touches_giant']+=1
        if rec['touches_giant'] and rec['three_distinct_components'] and rec['prefix_untouched']:
            counts['three_component_giant_mergers']+=1
            rec['other_profiles']={cid:profile(current[cid][0]) for cid in affected if cid!=giant}
            rec['two_fresh_611_components']=all(p==[3,1,1,1,1,1] for p in rec['other_profiles'].values())
            if rec['two_fresh_611_components']:
                counts['two_fresh_611_mergers']+=1
        records.append(rec)
    eligible=[r for r in records if r.get('touches_giant') and r.get('three_distinct_components') and r.get('prefix_untouched')]
    selected=min(eligible,key=lambda r:(not r.get('two_fresh_611_components',False),r['parent'])) if eligible else None
    report=dict(stage_after_owner_mass=length,previous_catalogue=previous_catalogue_path,previous_audit=previous_audit_path,
        frozen_parent_family='six_plus_one_parent_catalogue.json',counts=dict(counts),records=records,
        selected_candidate=selected,current_lower_cycles=current,prefix_owners=prefix,
        resource_caps=dict(cpu_seconds=90,wall_seconds=110,address_space_bytes=1024**3))
    filename=f'continuation_from_{length}_catalogue.json'
    Path(filename).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(output_file=filename,counts=dict(counts),selected_candidate=selected),indent=2))
    print('PASS: same221 parent templates refiltered against current graph.')


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('phase',choices=['catalogue','audit','source'])
    ap.add_argument('files',nargs='+')
    args=ap.parse_args()
    if args.phase=='catalogue':
        assert len(args.files)==2
        refilter(*args.files)
    elif args.phase=='audit':
        assert len(args.files)==2
        audit_candidate(*args.files)
    else:
        assert len(args.files)==1
        source_candidate(*args.files)
