#!/usr/bin/env python3
"""Exact lower-row deltas for the fixed mountain -> 475 -> 849 stages.

Mathematical execution only on h100. No search or assignment solver.
"""
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(110)
BASE = Path('/home/amodo/exact-b-k17-second-c6-20260908')
PREFIX = Path('/home/amodo/exact-b-k17-badsix-all-ports-20260908')
FULL = (1 << 17)-1
BAD = {f'old_{i}' for i in (115,116,118,122,129,138)}
topology = json.loads((BASE/'second_c6_topology.json').read_text())
first = json.loads((BASE/'second_c6_audit.json').read_text())
catalogue = json.loads((BASE/'six_plus_one_parent_catalogue.json').read_text())
second = json.loads((BASE/'six_plus_one_selected_audit.json').read_text())
assert first['all_requested_gates_passed'] and second['all_requested_gates_passed']
P = list(map(int,(PREFIX/'badsix_all_ports_306_owner_path.word').read_text().split()))
EP = list(map(int,(PREFIX/'badsix_all_ports_308_depth2_source.word').read_text().split()))
assert P == topology['prefix_owners'] == catalogue['prefix_owners']
assert len(P)==306 and len(EP)==308
assert all(EP[i]|EP[i+1]|EP[i+2]==t for i,t in enumerate(P))
rank_targets = {r:{sum(1<<b for b in bs) for bs in combinations(range(17),r)} for r in (6,7)}

def row(lower):
    T=[FULL^a for a in lower]
    L=len(T)
    E=[T[i]&T[(i-1)%L]&T[(i-2)%L]&T[(i-3)%L] for i in range(L)]
    assert min(map(int.bit_count,E))>=6
    pairs=[E[i]|E[(i+1)%L] for i in range(L)]
    assert all(pairs[i]==T[(i-2)%L]&T[(i-1)%L]&T[i] for i in range(L))
    assert all(E[i]|E[(i+1)%L]|E[(i+2)%L]==T[(i-1)%L]&T[i] for i in range(L))
    assert all(E[i]|E[(i+1)%L]|E[(i+2)%L]|E[(i+3)%L]==T[i] for i in range(L))
    return dict(E=E,letters=Counter(E),pairs=Counter(pairs))

current=dict(topology['current_lower_cycles'])
banks={cid:row(cy) for cid,cy in current.items() if cid not in BAD}
letters=sum((r['letters'] for r in banks.values()),Counter())
pairs=sum((r['pairs'] for r in banks.values()),Counter())
prefix_letters=Counter(EP)
prefix_pairs=Counter(a|b for a,b in zip(EP,EP[1:]))
prefix7={a for a in EP if a.bit_count()==7}

def hosts(S):
    answer=[]
    for cid,rec in list(banks.items())+[('prefix',dict(E=EP))]:
        E=rec['E']; L=len(E); cyc=cid!='prefix'
        for i,a in enumerate(E):
            if S & ~a:continue
            core=0
            if cyc or i>0:core |= a & ~E[(i-1)%L]
            if cyc or i<L-1:core |= a & ~E[(i+1)%L]
            if not core & ~S:answer.append([cid,i,a,core])
    return answer

def summary(label):
    good7={a for a,c in pairs.items() if c>0 and a.bit_count()==7}
    literal7={a for a,c in letters.items() if c>0 and a.bit_count()==7}
    literal6={a for a,c in letters.items() if c>0 and a.bit_count()==6}
    pair_prefix7=good7|prefix7
    all7=pair_prefix7|literal7
    missing_pair_prefix=rank_targets[7]-pair_prefix7
    missing7=rank_targets[7]-all7
    missing6=rank_targets[6]-literal6
    # Targets already present as a new rank-seven cycle letter are distinguished
    # from genuine missing rank-seven targets before testing legal cap hosts.
    host7={str(S):hosts(S) for S in sorted(missing7)}
    result=dict(stage=label,good_cycles=len(banks),cyclic_positions=sum(len(x['E']) for x in banks.values()),
                good_pair_rank7_targets=len(good7),good_rank7_letter_targets=len(literal7),
                prefix_rank7_letter_targets=len(prefix7),prefix_additional_rank7=len(prefix7-good7),
                pair_plus_prefix_rank7_count=len(pair_prefix7),pair_plus_prefix_rank7_missing=sorted(missing_pair_prefix),
                missing_pair_prefix_supplied_by_cycle_letters=sorted(missing_pair_prefix&literal7),
                all_literal_rank7_count=len(all7),all_literal_rank7_missing=sorted(missing7),
                good_rank6_letter_targets=len(literal6),rank6_letter_missing=sorted(missing6),
                rank7_hole_individual_legal_hosts=host7,
                rank7_holes_without_legal_host=[int(S) for S,h in host7.items() if not h],
                good_letter_rank_histogram=dict(sorted(Counter({r:sum(c for a,c in letters.items() if c>0 and a.bit_count()==r) for r in range(1,10)}).items())),
                good_pair_rank_histogram=dict(sorted(Counter({r:sum(c for a,c in pairs.items() if c>0 and a.bit_count()==r) for r in range(1,10)}).items())))
    assert sum(c for c in letters.values())==24004
    return result

def replace(affected,lower,cid):
    old_letter=Counter();old_pair=Counter()
    for name in affected:
        assert name not in BAD
        old_letter.update(banks[name]['letters']);old_pair.update(banks[name]['pairs'])
        letters.subtract(banks[name]['letters']);pairs.subtract(banks[name]['pairs'])
        del banks[name];del current[name]
    new=row(lower)
    banks[cid]=new;current[cid]=lower
    letters.update(new['letters']);pairs.update(new['pairs'])
    assert all(c>=0 for c in letters.values()) and all(c>=0 for c in pairs.values())
    return dict(affected=affected,new_component=cid,new_length=len(lower),
        local_rank7_pair_lost=sorted(a for a,c in old_pair.items() if a.bit_count()==7 and c and not new['pairs'][a]),
        local_rank7_pair_gained=sorted(a for a,c in new['pairs'].items() if a.bit_count()==7 and c and not old_pair[a]),
        local_rank6_letter_lost=sorted(a for a,c in old_letter.items() if a.bit_count()==6 and c and not new['letters'][a]),
        local_rank6_letter_gained=sorted(a for a,c in new['letters'].items() if a.bit_count()==6 and c and not old_letter[a]))

reports=[summary('mountain_before475')]
deltas=[replace(first['affected_component_ids'],first['new_lower_cycle'],'giant_475')]
assert current==catalogue['current_lower_cycles']
assert banks['giant_475']['E']==list(map(int,(BASE/'merged_475_depth3_source_cycle.word').read_text().split()))
reports.append(summary('after475'))
deltas.append(replace(second['candidate']['affected_component_ids'],second['new_lower_cycle'],'giant_849'))
assert banks['giant_849']['E']==list(map(int,(BASE/'merged_849_depth3_source_cycle.word').read_text().split()))
reports.append(summary('after849'))
result=dict(stages=reports,changed_component_deltas=deltas,
    scope='Actual fixed periodic GOOD cycles plus active linear 306-owner/308-source prefix; after mountain,475,849; no Q opening/final cap assignment.',
    host_record_fields=['component_id','source_index','maximal_letter','minimum_pair_preserving_core'],
    all_source_identities_checked=True,incremental_counter_updates_checked=True)
(BASE/'lower_bank_after_fusions.json').write_text(json.dumps(result,indent=2)+'\n')
for rec in reports:
    print(json.dumps({k:v for k,v in rec.items() if k!='rank7_hole_individual_legal_hosts'},indent=2))
print('PASS exact fixed-stage lower-bank audit; no solver or additional surgery search.')
