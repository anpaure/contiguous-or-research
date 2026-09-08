#!/usr/bin/env python3
"""One exact forced-support closure and one preselected Hall family; h100 only."""
import gc,hashlib,heapq,itertools,json,resource,signal,time
from array import array
from collections import Counter
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
signal.alarm(150)
started=time.monotonic()
BASE=Path('/home/amodo/exact-b-k17-triple-anchor-menus-20260908')
OUT=Path('/home/amodo/exact-b-k17-anchor-propagation-20260908');OUT.mkdir(exist_ok=True)
raw=(BASE/'canonical_w3_anchor_factorized_menus.json').read_bytes();menu=json.loads(raw)
fixed=set(menu['fixed_target_masks'])
targets=[t for t in range(1,1<<17) if t.bit_count()<=7 and t not in fixed]
target_set=set(targets);blocks=menu['blocks']; B=len(blocks)
options=[]; original_suppliers={t:set() for t in targets}
for block in blocks:
    bid=block['block']; assert bid==len(options)
    row=[]; possible=set()
    for letters in itertools.product(*block['letter_menus']):
        out=letters if len(letters)==1 else (letters[0],letters[1],letters[0]|letters[1])
        assert len(set(out))==len(out)
        row.append(out);possible.update(out)
    assert len(row)==block['option_count']
    options.append(row)
    for t in possible&target_set:original_suppliers[t].add(bid)
assert all(original_suppliers.values())
initial=[]; required=[set() for _ in blocks]
for t in targets:
    if t.bit_count()==7 and len(original_suppliers[t])==1:
        bid=next(iter(original_suppliers[t]));required[bid].add(t);initial.append([t,bid])
assert len(initial)==4441
domains=[]; unions=[]; suppliers={t:set() for t in targets}
for bid,row in enumerate(options):
    dom=array('H',(i for i,out in enumerate(row) if required[bid].issubset(out)))
    assert dom
    domains.append(dom)
    union=set(t for i in dom for t in row[i] if t in target_set);unions.append(union)
    for t in union:suppliers[t].add(bid)
after_initial=sum(map(len,domains))
trace=[];contradiction=None
zero=[t for t in targets if not suppliers[t]]
queue=[t for t in targets if len(suppliers[t])==1];heapq.heapify(queue)
if zero:contradiction=dict(kind='zero_target_after_initial',target=min(zero))
while queue and contradiction is None:
    t=heapq.heappop(queue)
    if len(suppliers[t])!=1:continue
    bid=next(iter(suppliers[t]))
    if t in required[bid]:continue
    required[bid].add(t)
    old=domains[bid]
    new=array('H',(i for i in old if t in options[bid][i]))
    trace.append(dict(target=t,block=bid,before=len(old),after=len(new)))
    domains[bid]=new
    if not new:
        contradiction=dict(kind='empty_block',block=bid,mandatory_targets=sorted(required[bid]));break
    newunion=set(u for i in new for u in options[bid][i] if u in target_set)
    lost=unions[bid]-newunion;unions[bid]=newunion
    lost_zero=[]
    for u in sorted(lost):
        suppliers[u].remove(bid)
        if not suppliers[u]:lost_zero.append(u)
        elif len(suppliers[u])==1:heapq.heappush(queue,u)
    if lost_zero:contradiction=dict(kind='zero_target',target=min(lost_zero),causing_step=len(trace)-1)

summary=dict(stage='support_propagation',initial_forced_rank7=len(initial),options_before=sum(map(len,options)),
    options_after_initial=after_initial,propagation_steps=len(trace),options_after_propagation=sum(map(len,domains)),
    contradiction=contradiction,elapsed_seconds=time.monotonic()-started)
print(json.dumps(summary),flush=True)

# Independent replay: regenerate every domain from ORIGINAL literal options and
# accumulated mandatory targets; recompute each claimed unique support only from
# original supplier lists, without using the producer's incremental support map.
replay_required=[set() for _ in blocks]
for t,bid in initial:
    actual=[b for b in original_suppliers[t] if any(t in out for out in options[b])]
    assert actual==[bid]
    replay_required[bid].add(t)
replay_domains=[array('H',(i for i,out in enumerate(row) if replay_required[b].issubset(out)))
                for b,row in enumerate(options)]
assert all(replay_domains)
for step in trace:
    t=step['target'];bid=step['block']
    actual=sorted(b for b in original_suppliers[t]
                  if any(t in options[b][i] for i in replay_domains[b]))
    assert actual==[bid] and t not in replay_required[bid]
    assert len(replay_domains[bid])==step['before']
    replay_required[bid].add(t)
    replay_domains[bid]=array('H',(i for i,out in enumerate(options[bid]) if replay_required[bid].issubset(out)))
    assert len(replay_domains[bid])==step['after']
assert all(list(a)==list(b) for a,b in zip(domains,replay_domains))
if contradiction:
    if contradiction['kind']=='empty_block':
        assert not replay_domains[contradiction['block']]
    else:
        t=contradiction['target']
        assert not any(t in options[b][i] for b in original_suppliers[t] for i in replay_domains[b])
else:
    # Check the whole fixed point again, not only the logged forced deductions.
    for t in targets:
        actual=[b for b in original_suppliers[t] if any(t in options[b][i] for i in replay_domains[b])]
        assert actual
        if len(actual)==1:assert t in replay_required[actual[0]]
del replay_domains;gc.collect()

# Reconstruct the Cartesian source menus independently from each source D and Pin.
cycles={c['cycle']:c for c in menu['cycles']};source_checks=0
for block in blocks:
    cycle=cycles[block['cycle']]
    for pos,stored in zip(block['positions'],block['letter_menus']):
        D=cycle['source'][pos];P=cycle['pins'][pos];free=D&~P
        sub=free;expected=[]
        while True:
            expected.append(P|sub)
            if not sub:break
            sub=(sub-1)&free
        assert sorted(expected)==stored;source_checks+=1
    rows=block['letter_menus']
    independently_decoded=([(a,) for a in rows[0]] if len(rows)==1 else
                          [(a,b,a|b) for a in rows[0] for b in rows[1]])
    assert independently_decoded==options[block['block']]

hall=None
if contradiction is None:
    hall_raw=Path('/home/amodo/k17_unrestricted_hall_cut_certificate_20260908.json').read_bytes()
    oldhall=json.loads(hall_raw);F=set(oldhall['target_masks'])-fixed
    capacities=[];witness_options=[]
    for bid,dom in enumerate(domains):
        best=-1;arg=None
        for i in dom:
            count=len(set(options[bid][i])&F)
            if count>best:best=count;arg=i
        capacities.append(best);witness_options.append(arg)
    total=sum(capacities)
    # Replay each exact maximum with a differently ordered enumeration.
    assert all(c==max(sum(t in F for t in options[b][i]) for i in reversed(domains[b]))
               for b,c in enumerate(capacities))
    hall=dict(kind='fixed_previous_1768_target_configuration_hall',original_target_count=len(oldhall['target_masks']),
        target_count=len(F),targets=sorted(F),total_configuration_capacity=total,deficiency=len(F)-total,
        block_capacities=capacities,maximizing_option_indices=witness_options,
        source_hall_sha256=hashlib.sha256(hall_raw).hexdigest(),exact_capacities_independently_replayed=True)
    if total<len(F):contradiction=dict(kind='configuration_hall',target_count=len(F),capacity=total,deficiency=len(F)-total)
    print('FIXED_HALL',json.dumps({k:v for k,v in hall.items() if k not in ('targets','block_capacities','maximizing_option_indices')}),flush=True)

report=dict(status='CONTRADICTION' if contradiction else 'PROPAGATION_AND_FIXED_HALL_SURVIVE',
    scope='Exactly one saved canonical width-three anchor CSP. No owner/cut/anchor changes and no search.',
    source_menu_sha256=hashlib.sha256(raw).hexdigest(),target_count=len(targets),block_count=B,
    initial_forced_rank7=initial,propagation_trace=trace,contradiction=contradiction,
    options_before=sum(map(len,options)),options_after_initial=after_initial,
    residual_options=sum(map(len,domains)),new_mandatory_targets=len(trace),
    mandatory_targets_by_block={str(b):sorted(req) for b,req in enumerate(required) if req},
    source_position_menus_reconstructed=source_checks,independent_trace_and_domain_replay=True,
    fixed_hall=hall,elapsed_seconds=time.monotonic()-started,
    resource_caps=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3))
(OUT/'anchor_support_propagation_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'anchor_residual_domain_indices.json').write_text(json.dumps([list(d) for d in domains])+'\n')
print('FINAL',json.dumps({k:v for k,v in report.items() if k not in ('initial_forced_rank7','propagation_trace','mandatory_targets_by_block','fixed_hall')}),flush=True)
