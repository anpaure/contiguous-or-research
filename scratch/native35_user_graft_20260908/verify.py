#!/usr/bin/env python3
"""Fixed user witness verification only. Mathematical execution on h100."""
import json
import resource
import signal
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(110)
OUT=Path('/home/amodo/exact-b-native35-user-graft-20260908')
OUT.mkdir(exist_ok=True)
FULL=(1<<17)-1
W=[287,768,4106,16404,5648,3590,2308,4867,20997,8193,65538,21024,4385,68128,5152,416,2704,20880,86272,4610,129,84098,77952,18436,72320,35328,22658,8320,6912,2954,1672,554,440,122,318]
assert len(W)==35 and all(0<x<=FULL for x in W)

def mask(coords):return sum(1<<(x-1) for x in coords)
def rotate(x,t):
    out=x & ~mask(range(9,17))
    for i in range(8):
        if x & (1<<(8+i)):out |=1<<(8+(i+t)%8)
    return out
def update(state,x):
    return (x,)+tuple(y&~x for y in state if y&~x)
def linear_states(word,initial=()):
    state=initial;ans=[]
    for x in word:state=update(state,x);ans.append(state)
    return ans
def cyclic_states(word):
    initial=linear_states(word)[-1]
    assert (lambda st:sum(st))(initial)==FULL
    ans=linear_states(word,initial)
    assert ans[-1]==initial
    return initial,ans
def prefixes(state):
    out=[];v=0
    for a in state:v|=a;out.append(v)
    return out
def targets(word,cyclic):
    n=len(word);seen={}
    for a in range(n):
        v=0
        for width in range(1,(n if cyclic else n-a)+1):
            v|=word[(a+width-1)%n]
            seen.setdefault(v,dict(start=a,length=width,wrap=(a+width>n)))
            if v==FULL:break
    return seen
def windows(word,width,cyclic):
    n=len(word);ans=[]
    for a in range(n if cyclic else n-width+1):
        v=0
        for j in range(width):v|=word[(a+j)%n]
        ans.append(v)
    return ans
def ranks(values):return dict(sorted(Counter(x.bit_count() for x in values).items()))
def write_word(name,word):(OUT/name).write_text('\n'.join(map(str,word))+'\n')
def expected_P(i):
    return (31|(1<<(8+i)),1<<5,1<<6,1<<7)+tuple(1<<(8+(i+j)%8) for j in range(1,8))+(1<<16,)
def expected_Q(i):
    return ((1<<(8+i))|(1<<(8+(i+1)%8)),31,1<<5,1<<6,1<<7)+tuple(1<<(8+(i+j)%8) for j in range(2,8))+(1<<16,)

cycles=[[rotate(x,i) for x in W] for i in range(8)]
cycle_targets=[];cycle_states=[];cycle_reports=[]
for i,cy in enumerate(cycles):
    initial,st=cyclic_states(cy);ts=targets(cy,True)
    tris=windows(cy,3,True);fours=windows(cy,4,True)
    cycle_targets.append(ts);cycle_states.append(st)
    assert set(ts)=={v for state in st for v in prefixes(state)}
    assert st[0]==expected_P(i) and st[1]==expected_Q(i)
    assert update(st[0],cycles[(i-1)%8][1])==expected_Q((i-1)%8)
    cycle_reports.append(dict(component=i,length=len(cy),targets=len(ts),target_rank_counts=ranks(ts),
        lower_than9=sum(v.bit_count()<9 for v in ts),middle9=sum(v.bit_count()==9 for v in ts),
        triple_rank_counts=ranks(tris),four_rank_counts=ranks(fours),
        distinct_triples=len(set(tris)),distinct_fours=len(set(fours)),
        P=list(st[0]),Q=list(st[1])))

route=[(i,j) for i in range(7,-1,-1) for j in list(range(1,35))+[0]]
assert len(route)==len(set(route))==280
joined=[cycles[i][j] for i,j in route]
initial,joined_states=cyclic_states(joined)
assert initial==expected_P(0)
assert all(state==cycle_states[i][j] for state,(i,j) in zip(joined_states,route))
joint_family=set().union(*(set(x) for x in cycle_targets))
joined_targets=targets(joined,True)
triangles=windows(joined,3,True);fourwindows=windows(joined,4,True)

def opening(word,requested):
    ts=set(targets(word,True));n=len(word);tested=[];chosen=None
    order=[requested,(requested+1)%n]+list(range(n))
    for start in dict.fromkeys(order):
        opened=word[start:]+word[:start]
        literal=opened+opened[:3]
        seen=targets(literal,False)
        tested.append(dict(start=start,preceding_cut_edge=(start-1)%n,
            targets=len(seen),missing=len(ts-set(seen)),extra=len(set(seen)-ts)))
        if set(seen)==ts:chosen=(start,literal,seen);break
    assert chosen is not None
    start,literal,seen=chosen
    lower=sum(v.bit_count()<9 for v in ts);middle=sum(v.bit_count()==9 for v in ts)
    delay=0
    while delay*middle+delay*(delay+1)//2<lower:delay+=1
    return dict(period=n,requested_start=requested,selected_start=start,
        selected_preceding_cut_edge=(start-1)%n,tested=tested,length=len(literal),
        target_count=len(seen),lower_than9=lower,middle9=middle,
        endpoint_delay=delay,endpoint_lower_bound=middle+delay,
        exact_target_family_optimal=(len(literal)==middle+delay)),literal,seen

base_open,base_literal,base_seen=opening(W,14)
joined_open,joined_literal,joined_seen=opening(joined,13)

pi=[17,16,15,14,13,12,11,10,8,7,6,1,2,3,4,9,5]
prefix=[mask([x]) for x in pi[:3]]+[mask(pi[j-1:j+5]) for j in range(4,13)]
assert len(prefix)==12 and linear_states(prefix)[-1]==expected_P(0)
rooted=prefix+joined[:-1]
assert len(rooted)==291
root_states=linear_states(rooted)
assert root_states[11]==expected_P(0)
assert root_states[12:]==joined_states[:-1]
root_targets=targets(rooted,False)
root_triples=windows(rooted,3,False);root_fours=windows(rooted,4,False)
assert joint_family<=set(root_targets)
assert set(fourwindows)<=set(root_fours)
assert set(triangles)<=set(root_triples)

def potential(word,states,s):
    bprev=0;seen=set();up=0;loss=0;idle=0;rows=[]
    for j,st in enumerate(states):
        ps=prefixes(st);b=sum(x.bit_count()<s for x in ps)
        at=[x for x in ps if x.bit_count()==s];assert len(at)<=1
        new=bool(at and at[0] not in seen)
        if at:seen.add(at[0])
        delta=b-bprev
        assert delta<=1 and not(delta==1 and new)
        up += delta==1;loss+=max(0,-delta);idle+=(not new and delta<=0)
        rows.append(dict(position=j,b=b,delta=delta,new_rank_target=(at[0] if new else None)))
        bprev=b
    assert len(word)-len(seen)==loss+bprev+idle
    return dict(rank=s,N=len(word),distinct_rank_targets=len(seen),L=loss,b_terminal=bprev,E=idle,
                upward_steps=up,identity_left=len(word)-len(seen),identity_right=loss+bprev+idle),rows

potential_reports=[];rank9_rows=None
for s in range(1,18):
    pot,rows=potential(rooted,root_states,s);potential_reports.append(pot)
    if s==9:rank9_rows=rows
root_lower=sum(x.bit_count()<9 for x in root_targets)
root_middle=sum(x.bit_count()==9 for x in root_targets)
root_delay=0
while root_delay*root_middle+root_delay*(root_delay+1)//2<root_lower:root_delay+=1

checks=dict(each251_targets=all(x['targets']==251 for x in cycle_reports),
    each105_lower35_middle=all(x['lower_than9']==105 and x['middle9']==35 for x in cycle_reports),
    all_base_triples8_fours9=all(x['triple_rank_counts']=={8:35} and x['four_rank_counts']=={9:35} for x in cycle_reports),
    joint1811_targets=(len(joint_family)==1811),joined_target_set_equal=(set(joined_targets)==joint_family),
    joint807_lower280_middle=(sum(x.bit_count()<9 for x in joint_family)==807 and sum(x.bit_count()==9 for x in joint_family)==280),
    joined280_distinct_facets_owners=(ranks(triangles)=={8:280} and ranks(fourwindows)=={9:280} and len(set(triangles))==len(set(fourwindows))==280),
    base38_and_joined283_optimal=(base_open['length']==38 and base_open['exact_target_family_optimal'] and joined_open['length']==283 and joined_open['exact_target_family_optimal']),
    root1876_targets=(len(root_targets)==1876),root288_middle=(ranks(root_fours)=={9:288} and len(set(root_fours))==288),
    root288_facets=(sum(x.bit_count()==8 for x in root_triples)==288 and len({x for x in root_triples if x.bit_count()==8})==288),
    root_rank9_potential=(potential_reports[8]['distinct_rank_targets']==288 and potential_reports[8]['L']==0 and potential_reports[8]['b_terminal']==3 and potential_reports[8]['E']==0))
report=dict(checks=checks,all_claimed_checks_passed=all(checks.values()),cycles=cycle_reports,
    joined=dict(length=280,target_count=len(joined_targets),target_rank_counts=ranks(joined_targets),
        joint_family_target_count=len(joint_family),target_set_missing=sorted(joint_family-set(joined_targets)),
        target_set_extra=sorted(set(joined_targets)-joint_family),triple_rank_counts=ranks(triangles),four_rank_counts=ranks(fourwindows),
        distinct_triples=len(set(triangles)),distinct_fours=len(set(fourwindows)),
        route=[list(x) for x in route]),
    base_opening=base_open,joined_opening=joined_open,
    rooted=dict(length=len(rooted),prefix_permutation=pi,prefix_letters=prefix,target_count=len(root_targets),
        target_rank_counts=ranks(root_targets),triple_rank_counts=ranks(root_triples),four_rank_counts=ranks(root_fours),
        distinct_rank8_triples=len({x for x in root_triples if x.bit_count()==8}),distinct_rank9_fours=len(set(root_fours)),
        no_joint_family_target_dropped=joint_family<=set(root_targets),no_middle_or_facet_dropped=True,
        required_lower_than9=root_lower,required_middle9=root_middle,endpoint_lower_bound=root_middle+root_delay,
        exact_for_its_target_family=(len(rooted)==root_middle+root_delay),potential=potential_reports),
    scope='User supplied fixed35period, eight coordinate rotations, one prescribed reverse-cycle graft, deterministic cut verification, and one fixed291rooted word only. No static24313inventory supplied or checked.',
    resource_caps=dict(cpu_seconds=90,wall_seconds=110,address_space_bytes=1024**3))
(OUT/'native35_graft_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'native35_graft_targets_and_witnesses.json').write_text(json.dumps(dict(
    base={str(x):w for x,w in sorted(cycle_targets[0].items())},
    joined_cyclic={str(x):w for x,w in sorted(joined_targets.items())},
    base38={str(x):w for x,w in sorted(base_seen.items())},
    joined283={str(x):w for x,w in sorted(joined_seen.items())},
    rooted291={str(x):w for x,w in sorted(root_targets.items())}),indent=2)+'\n')
(OUT/'native291_rank9_potential_steps.json').write_text(json.dumps(rank9_rows,indent=2)+'\n')
write_word('native35_base_cycle.word',W)
for i,cy in enumerate(cycles):write_word(f'native35_rotation_{i}_cycle.word',cy)
write_word('native280_joined_cycle.word',joined)
write_word('native38_base_optimal_linear.word',base_literal)
write_word('native283_joint_optimal_linear.word',joined_literal)
write_word('native12_rooting_prefix.word',prefix)
write_word('native291_rooted_word.word',rooted)
print(json.dumps(dict(checks=checks,base_opening=base_open,joined_opening=joined_open,
    joint_target_rank_counts=ranks(joint_family),rooted=report['rooted']),indent=2))
print('PASS' if all(checks.values()) else 'FAIL','fixed user native35 / graft280 / rooted291 verification')
