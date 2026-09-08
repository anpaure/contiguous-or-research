#!/usr/bin/env python3
"""Exact incremental 849 -> 1223 -> 1513 lower-row audit, h100 only."""
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (90,90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3,1024**3))
signal.alarm(110)
BASE=Path('/home/amodo/exact-b-k17-second-c6-20260908')
PREFIX=Path('/home/amodo/exact-b-k17-badsix-all-ports-20260908')
FULL=(1<<17)-1
BAD={f'old_{i}' for i in (115,116,118,122,129,138)}
cats={n:json.loads((BASE/f'continuation_from_{n}_catalogue.json').read_text()) for n in (849,1223,1513)}
audits={n:json.loads((BASE/f'continuation_from_{n}_selected_audit.json').read_text()) for n in (849,1223)}
assert all(x['all_requested_gates_passed'] for x in audits.values())
old_protected=set(json.loads((PREFIX/'good_cycle_lower_bank.json').read_text())['prefix_added_rank7'])
assert len(old_protected)==102
P=list(map(int,(PREFIX/'badsix_all_ports_306_owner_path.word').read_text().split()))
EP=list(map(int,(PREFIX/'badsix_all_ports_308_depth2_source.word').read_text().split()))
assert len(P)==306 and len(EP)==308
assert all(cat['prefix_owners']==P for cat in cats.values())
assert all(EP[i]|EP[i+1]|EP[i+2]==t for i,t in enumerate(P))
prefix7={a for a in EP if a.bit_count()==7}
assert old_protected<=prefix7
all6={sum(1<<i for i in bs) for bs in combinations(range(17),6)}
all7={sum(1<<i for i in bs) for bs in combinations(range(17),7)}

def source(lower):
    T=[FULL^x for x in lower]; L=len(T)
    E=[T[i]&T[(i-1)%L]&T[(i-2)%L]&T[(i-3)%L] for i in range(L)]
    assert min(map(int.bit_count,E))>=6
    pairs=[E[i]|E[(i+1)%L] for i in range(L)]
    assert all(pairs[i]==T[(i-2)%L]&T[(i-1)%L]&T[i] for i in range(L))
    assert all(E[i]|E[(i+1)%L]|E[(i+2)%L]==T[(i-1)%L]&T[i] for i in range(L))
    assert all(E[i]|E[(i+1)%L]|E[(i+2)%L]|E[(i+3)%L]==T[i] for i in range(L))
    return dict(E=E,letters=Counter(E),pairs=Counter(pairs))

current=dict(cats[849]['current_lower_cycles'])
banks={cid:source(cy) for cid,cy in current.items() if cid not in BAD}
letter_count=sum((rec['letters'] for rec in banks.values()),Counter())
pair_count=sum((rec['pairs'] for rec in banks.values()),Counter())

def summary(label):
    letter6={a for a,c in letter_count.items() if c>0 and a.bit_count()==6}
    letter7={a for a,c in letter_count.items() if c>0 and a.bit_count()==7}
    pair7={a for a,c in pair_count.items() if c>0 and a.bit_count()==7}
    assert sum(letter_count.values())==sum(pair_count.values())==24004
    result=dict(stage=label,good_cycles=len(banks),good_source_positions=sum(letter_count.values()),
        good_rank7_pair_targets=len(pair7),good_rank7_letter_targets=len(letter7),
        rank7_pair_plus_original_102_protected_count=len(pair7|old_protected),
        rank7_missing_after_original_102_protected=sorted(all7-(pair7|old_protected)),
        actual_prefix_additional_rank7=sorted(prefix7-pair7),
        actual_prefix_additional_equals_original102=(prefix7-pair7==old_protected),
        all_pair_plus_prefix_rank7_count=len(pair7|prefix7),
        all_literal_rank7_missing=sorted(all7-(pair7|prefix7|letter7)),
        good_rank6_letter_targets=len(letter6),rank6_letter_missing=sorted(all6-letter6),
        good_letter_rank_histogram={r:sum(c for a,c in letter_count.items() if c>0 and a.bit_count()==r) for r in range(1,10)},
        good_pair_rank_histogram={r:sum(c for a,c in pair_count.items() if c>0 and a.bit_count()==r) for r in range(1,10)})
    return result

def replace(previous,nxt):
    rec=audits[previous];affected=rec['candidate']['affected_component_ids']
    oldletter=Counter();oldpair=Counter()
    for cid in affected:
        assert cid not in BAD
        oldletter.update(banks[cid]['letters']);oldpair.update(banks[cid]['pairs'])
        letter_count.subtract(banks[cid]['letters']);pair_count.subtract(banks[cid]['pairs'])
        del banks[cid];del current[cid]
    cy=rec['new_lower_cycle'];assert len(cy)==nxt
    new=source(cy);cid=f'giant_{nxt}'
    assert new['E']==list(map(int,(BASE/f'merged_{nxt}_depth3_source_cycle.word').read_text().split()))
    assert [FULL^a for a in cy]==list(map(int,(BASE/f'merged_{nxt}_upper_owner_cycle.word').read_text().split()))
    banks[cid]=new;current[cid]=cy
    letter_count.update(new['letters']);pair_count.update(new['pairs'])
    assert current==cats[nxt]['current_lower_cycles']
    assert all(c>=0 for c in letter_count.values()) and all(c>=0 for c in pair_count.values())
    old6=Counter({a:c for a,c in oldletter.items() if a.bit_count()==6})
    new6=Counter({a:c for a,c in new['letters'].items() if a.bit_count()==6})
    old7=Counter({a:c for a,c in oldpair.items() if a.bit_count()==7})
    new7=Counter({a:c for a,c in new['pairs'].items() if a.bit_count()==7})
    return dict(from_stage=previous,to_stage=nxt,affected_component_ids=affected,
        local_rank7_pair_lost=sorted(set(old7)-set(new7)),local_rank7_pair_gained=sorted(set(new7)-set(old7)),
        local_rank6_letter_lost=sorted(set(old6)-set(new6)),local_rank6_letter_gained=sorted(set(new6)-set(old6)),
        local_rank7_pair_counter_equal=(old7==new7),local_rank6_letter_counter_equal=(old6==new6),
        local_rank7_pair_occurrence_deltas={str(a):new7[a]-old7[a] for a in sorted(set(old7)|set(new7)) if new7[a]!=old7[a]},
        local_rank6_letter_occurrence_deltas={str(a):new6[a]-old6[a] for a in sorted(set(old6)|set(new6)) if new6[a]!=old6[a]})

stages=[summary(849)];deltas=[]
for old,nxt in ((849,1223),(1223,1513)):
    deltas.append(replace(old,nxt));stages.append(summary(nxt))
result=dict(stages=stages,changed_component_deltas=deltas,original_protected_prefix_rank7_masks=sorted(old_protected),
    source_and_owner_files_verified=True,current_catalogues_verified=True,
    scope='Fixed periodic GOOD sources plus original linear 308-letter prefix, actual849/1223/1513 stages; no host matching or further finite search.')
(BASE/'lower_bank_849_to_1513.json').write_text(json.dumps(result,indent=2)+'\n')
for rec in stages:
    print(json.dumps({k:v for k,v in rec.items() if k!='actual_prefix_additional_rank7'},indent=2))
print(json.dumps(deltas,indent=2))
print('PASS fixed incremental849-to1513 lower support audit; finite checks stop here.')
