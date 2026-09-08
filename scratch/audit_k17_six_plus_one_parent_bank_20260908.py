#!/usr/bin/env python3
"""Exhaust one explicit 221-parent family; all mathematical execution on h100."""
import argparse
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from pathlib import Path

from audit import root, cycle_adjacency, components, switch, upper, palette, runs

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(110)
FULL = (1 << 17)-1
BAD_IDS = {115,116,118,122,129,138}


def stage():
    initial = json.loads(Path('second_c6_topology.json').read_text())
    second = json.loads(Path('second_c6_audit.json').read_text())
    assert second['all_requested_gates_passed']
    current = initial['current_lower_cycles']
    for cid in second['affected_component_ids']:
        del current[cid]
    current['giant_475'] = second['new_lower_cycle']
    assert len(current) == 144
    return current, initial['prefix_owners']


def profile(a):
    u = root(a)
    word = ''.join('1' if a >> ((u+j) % 17) & 1 else '0' for j in range(1,17))
    answer = []
    while word:
        hits = {i for i in range(len(word)-1) if word[i:i+2] == '10'}
        assert hits
        answer.append(len(hits))
        remove = hits | {i+1 for i in hits}
        word = ''.join(c for i,c in enumerate(word) if i not in remove)
    return answer


def parent_bank():
    shapes = ['1'*6+'0'*j+'1'+'0'*(7-j) for j in range(1,7)]
    shapes += ['1'*j+'0'+'1'*(7-j)+'0'*6 for j in range(1,6)]
    assert len(set(shapes)) == 11
    triples = []
    for shape in shapes:
        for slot in range(3):
            blocks = ['', '', '']
            blocks[slot] = shape
            triples.append(tuple(blocks))
    for high in range(3):
        for low in range(3):
            if high == low:
                continue
            blocks = ['', '', '']
            blocks[high] = '1'*6+'0'*6
            blocks[low] = '10'
            triples.append(tuple(blocks))
    assert len(set(triples)) == 39
    parents = {}
    multiplicity = Counter()
    for blocks in triples:
        word = '0'+blocks[0]+'0'+blocks[1]+'0'+blocks[2]
        assert len(word) == 17 and word.count('1') == 7
        cuts = [0, 1+len(blocks[0]), 2+len(blocks[0])+len(blocks[1])]
        for rotation in range(17):
            h = sum(1 << ((j+rotation) % 17) for j,c in enumerate(word) if c == '1')
            arms = [(a+rotation) % 17 for a in cuts]
            multiplicity[h] += 1
            parents.setdefault(h, dict(parent=h, arms=arms, blocks=list(blocks), rotation=rotation))
    assert len(parents) == 221 and set(multiplicity.values()) == {3}
    return parents


def catalogue():
    current, prefix = stage()
    ids = {a: cid for cid,cy in current.items() for a in cy}
    adj = cycle_adjacency(current.values())
    bad_nodes = {a for cid,cy in current.items() if cid in {f'old_{i}' for i in BAD_IDS} for a in cy}
    assert not (set(current['giant_475']) & bad_nodes)
    states = [sum(1 << b for b in bits) for bits in combinations(range(17),8)]
    f = {a: FULL ^ a ^ (1 << root(a)) for a in states}
    invf = {b:a for a,b in f.items()}
    parents = parent_bank()
    records = []
    counts = Counter()
    for h, raw in sorted(parents.items()):
        rec = dict(raw)
        counts['parents'] += 1
        arms = rec['arms']
        centers = [h | (1 << a) for a in arms]
        pivots = [FULL ^ z ^ invf[z] for z in centers]
        assert all(x.bit_count() == 1 for x in pivots)
        rec['common_pivot'] = len(set(pivots)) == 1
        if not rec['common_pivot']:
            records.append(rec)
            continue
        counts['common_pivot'] += 1
        pivot = pivots[0]
        arm_mask = sum(1 << a for a in arms)
        core = FULL ^ (h | arm_mask | pivot)
        assert core.bit_count() == 6 and not (pivot & (h | arm_mask))
        ps = [core | (1 << arms[i]) | (1 << arms[(i+1) % 3]) for i in range(3)]
        qs = [core | (1 << arms[i]) | pivot for i in range(3)]
        old = [[ps[i],qs[i]] for i in range(3)]
        new = [[ps[i],qs[(i+1) % 3]] for i in range(3)]
        rec.update(core=core, pivot=pivot.bit_length()-1, old_edges=old, new_edges=new)
        rec['old_shore_present'] = all(b in adj[a] for a,b in old)
        if not rec['old_shore_present']:
            records.append(rec)
            continue
        counts['old_shore_present'] += 1
        companions = [next(iter(adj[p] - {q})) for p,q in old]
        deleted = [p & ~other for (p,_),other in zip(old,companions)]
        rec['common_companion_deletion'] = (len(set(deleted)) == 1 and deleted[0].bit_count() == 1
                                               and bool(deleted[0] & core))
        rec['companion_deleted_masks'] = deleted
        rec['companion_owners'] = companions
        if not rec['common_companion_deletion']:
            records.append(rec)
            continue
        counts['common_companion_deletion'] += 1
        affected = sorted({ids[a] for edge in old for a in edge})
        rec['affected_component_ids'] = affected
        rec['affected_lengths'] = [len(current[c]) for c in affected]
        rec['touches_giant'] = 'giant_475' in affected
        rec['prefix_untouched'] = not (set(ps+qs) & bad_nodes)
        rec['three_distinct_components'] = len(affected) == 3
        if rec['touches_giant']:
            counts['touches_giant'] += 1
        if rec['touches_giant'] and rec['three_distinct_components'] and rec['prefix_untouched']:
            counts['three_component_giant_mergers'] += 1
            others = [cid for cid in affected if cid != 'giant_475']
            rec['other_profiles'] = {cid:profile(current[cid][0]) for cid in others}
            rec['two_fresh_611_components'] = all(p == [3,1,1,1,1,1] for p in rec['other_profiles'].values())
            if rec['two_fresh_611_components']:
                counts['two_fresh_611_mergers'] += 1
        records.append(rec)
    eligible = [rec for rec in records if rec.get('touches_giant') and rec.get('three_distinct_components')
                and rec.get('prefix_untouched')]
    selected = min(eligible, key=lambda r:(not r.get('two_fresh_611_components',False),r['parent'])) if eligible else None
    report = dict(counts=dict(counts), records=records, selected_candidate=selected,
                  current_lower_cycles=current, prefix_owners=prefix,
                  resource_caps=dict(cpu_seconds=90,wall_seconds=110,address_space_bytes=1024**3))
    Path('six_plus_one_parent_catalogue.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(counts=dict(counts),selected_candidate=selected),indent=2))
    print('PASS: exhaustive explicit39-block/221-parent topology catalogue completed.')


def audit_candidate(catalogue_path='six_plus_one_parent_catalogue.json', audit_path='six_plus_one_selected_audit.json'):
    catalogue = json.loads(Path(catalogue_path).read_text())
    candidate = catalogue['selected_candidate']
    assert candidate is not None
    current = catalogue['current_lower_cycles']
    affected = candidate['affected_component_ids']
    affected_adj = cycle_adjacency([current[cid] for cid in affected])
    switch(affected_adj,candidate['old_edges'],candidate['new_edges'])
    merged = components(affected_adj)
    assert len(merged) == 1
    old_witness = {}
    for cid in affected:
        old_witness.update(upper([FULL ^ a for a in current[cid]],True,cid))
    new_witness = upper([FULL ^ a for a in merged[0]],True,'merged')
    outside = upper(catalogue['prefix_owners'],False,'actual_306_prefix')
    banned = {f'old_{i}' for i in BAD_IDS}
    for cid, cy in current.items():
        if cid not in affected and cid not in banned:
            outside.update(upper([FULL ^ a for a in cy],True,cid))
    old_global = set(old_witness) | set(outside)
    new_global = set(new_witness) | set(outside)
    assert len(old_global) == 41225
    lower_equal = palette([current[cid] for cid in affected]) == palette(merged)
    assert lower_equal
    hist,short,constant = runs(merged[0])
    lost = set(old_witness) - set(new_witness)
    gained = set(new_witness) - set(old_witness)
    global_lost = old_global - new_global
    passed = not global_lost and not short
    rec = dict(candidate=candidate,new_lengths=list(map(len,merged)),new_lower_cycle=merged[0],
               local_upper_lost=sorted(lost),local_upper_gained=sorted(gained),
               global_upper_lost=sorted(global_lost),
               global_proper_upper_targets_after=len(new_global),
               outside_backup_for_local_losses={str(a):outside[a] for a in sorted(lost) if a in outside},
               old_local_lost_witnesses={str(a):old_witness[a] for a in sorted(lost)},
               local_upper_transport={str(a):dict(old=old_witness[a],new=new_witness[a])
                                      for a in sorted(set(old_witness)&set(new_witness))},
               lower_rank8_pair_multiset_preserved=lower_equal,
               positive_run_histogram=hist,short_positive_runs=short,
               constant_positive_coordinates=constant,all_requested_gates_passed=passed)
    Path(audit_path).write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({k:rec[k] for k in ('new_lengths','local_upper_lost','local_upper_gained',
           'global_upper_lost','global_proper_upper_targets_after','lower_rank8_pair_multiset_preserved',
           'positive_run_histogram','short_positive_runs','all_requested_gates_passed')},indent=2))
    print('PASS' if passed else 'FAIL','one deterministically selected parent-bank merger.')


def source_candidate(audit_path='six_plus_one_selected_audit.json'):
    rec=json.loads(Path(audit_path).read_text())
    assert rec['all_requested_gates_passed']
    owners=[FULL ^ a for a in rec['new_lower_cycle']]
    n=len(owners)
    envelope=[]
    for p in range(n):
        value=FULL
        for j in range(4):
            value &= owners[(p-j) % n]
        assert value
        envelope.append(value)
    for i in range(n):
        owner=0
        face=0
        for j in range(4):
            owner |= envelope[(i+j) % n]
            if j<3:
                face |= envelope[(i+j) % n]
        assert owner == owners[i]
        assert face == owners[i-1] & owners[i]
    owner_file=f'merged_{n}_upper_owner_cycle.word'
    source_file=f'merged_{n}_depth3_source_cycle.word'
    Path(owner_file).write_text('\n'.join(map(str,owners))+'\n')
    Path(source_file).write_text('\n'.join(map(str,envelope))+'\n')
    rec['source_certificate']=dict(period=n,source_depth=3,owner_file=owner_file,source_file=source_file,
        minimum_source_letter_rank=min(map(int.bit_count,envelope)),
        all_owner_four_windows_verified=True,all_rank8_three_windows_verified=True)
    Path(audit_path).write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec['source_certificate'],indent=2))
    print('PASS: literal source verified.')


if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('phase',choices=['catalogue','audit','source'])
    args=ap.parse_args()
    {'catalogue':catalogue,'audit':audit_candidate,'source':source_candidate}[args.phase]()
