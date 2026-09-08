#!/usr/bin/env python3
"""One prescribed canonical PBBS surgery; mathematical execution only on h100."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

R = 8
N = 2*R+1
FULL = (1 << N)-1

def root(a):
    for u in range(N):
        if a >> u & 1:
            continue
        height = 0
        for j in range(1,N):
            height += 1 if a >> ((u+j) % N) & 1 else -1
            if height < 0:
                break
        else:
            assert height == 0
            return u
    raise AssertionError(a)

states = [sum(1 << i for i in bits) for bits in combinations(range(N), R)]
f = {a: FULL ^ a ^ (1 << root(a)) for a in states}
assert len(set(f.values())) == len(states)
g = {a: f[f[a]] for a in states}
unseen = set(states)
old_cycles = []
old_ids = {}
while unseen:
    a = min(unseen)
    p = a
    cycle = []
    while p in unseen:
        old_ids[p] = len(old_cycles)
        unseen.remove(p)
        cycle.append(p)
        p = g[p]
    assert p == a
    old_cycles.append(cycle)

core = sum(1 << j for j in range(1,R-1))
arms = [R-1,R,R+1]
P = [core | (1 << arms[i]) | (1 << arms[(i+1)%3]) for i in range(3)]
Q = [core | (1 << arms[i]) | 1 for i in range(3)]
adj = {a:set() for a in states}
for a,b in g.items():
    adj[a].add(b)
    adj[b].add(a)
assert all(len(v)==2 for v in adj.values())
old_edges = [[P[i],Q[i]] for i in range(3)]
new_edges = [[P[i],Q[(i+1)%3]] for i in range(3)]
affected_ids = sorted({old_ids[a] for a in P+Q})
for a,b in old_edges:
    assert b in adj[a], (a,b)
    adj[a].remove(b)
    adj[b].remove(a)
for a,b in new_edges:
    assert b not in adj[a]
    adj[a].add(b)
    adj[b].add(a)
assert all(len(v)==2 for v in adj.values())

affected_states = {a for cid in affected_ids for a in old_cycles[cid]}
unseen = set(affected_states)
new_cycles = []
while unseen:
    start = min(unseen)
    prev = None
    p = start
    cycle = []
    while p in unseen:
        unseen.remove(p)
        cycle.append(p)
        ns = sorted(adj[p])
        nxt = ns[0] if prev is None or ns[0] != prev else ns[1]
        prev,p = p,nxt
    assert p == start, (start,p)
    new_cycles.append(cycle)

def upper(cycles, keep_witness=False):
    support = set()
    witness = {}
    for cid,cycle in enumerate(cycles):
        owners = [FULL ^ a for a in cycle]
        length = len(owners)
        for i in range(length):
            acc = owners[i]
            for width in range(2,length+1):
                previous = acc
                acc |= owners[(i+width-1)%length]
                if acc == FULL:
                    break
                if acc == previous:
                    continue
                assert acc.bit_count() >= R+2
                support.add(acc)
                if keep_witness:
                    witness.setdefault(acc,dict(cycle=cid,start=i,width=width))
            else:
                raise AssertionError("cycle fails to reach full union")
    return support,witness

def pair_palette(cycles):
    return Counter((FULL^cycle[i]) & (FULL^cycle[(i+1)%len(cycle)])
                   for cycle in cycles for i in range(len(cycle)))

def short_runs(cycles):
    answer=[]
    histogram=Counter()
    for cid,cycle in enumerate(cycles):
        owners=[FULL ^ a for a in cycle]
        length=len(owners)
        for x in range(N):
            for i in range(length):
                if not (owners[i]>>x&1) or owners[i-1]>>x&1:
                    continue
                width=1
                while owners[(i+width)%length]>>x&1:
                    width+=1
                    assert width<length
                histogram[width]+=1
                if width<=3:
                    answer.append(dict(cycle=cid,coordinate=x,start=i,length=width,
                                       owners=[owners[(i+j)%length] for j in range(-2,width+2)]))
    return histogram,answer

def cut_cores(cycle):
    owners=[FULL ^ a for a in cycle]
    length=len(owners)
    cores={}
    for i in range(length):
        acc=owners[i]
        fatal=0
        for width in range(2,length+1):
            fatal |= 1 << ((i+width-1)%length)
            previous=acc
            acc |= owners[(i+width-1)%length]
            if acc==FULL:
                break
            if acc==previous:
                continue
            cores[acc] = cores.get(acc,fatal) & fatal
    return cores

affected_old=[old_cycles[i] for i in affected_ids]
outside=[c for i,c in enumerate(old_cycles) if i not in affected_ids]
old_upper,old_witness=upper(affected_old,True)
new_upper,new_witness=upper(new_cycles,True)
outside_upper,_=upper(outside)
lost=old_upper-new_upper
gained=new_upper-old_upper
lost_global=lost-outside_upper
assert len(old_upper|outside_upper)==41225
assert pair_palette(affected_old)==pair_palette(new_cycles)
old_hist,old_short=short_runs(affected_old)
new_hist,new_short=short_runs(new_cycles)
assert old_upper == new_upper
assert not new_short
new_cores=[cut_cores(c) for c in new_cycles]
cut_reports=[]
for ci,cores in enumerate(new_cores):
    outside_support=outside_upper | set().union(*(set(cs) for cj,cs in enumerate(new_cores) if cj!=ci))
    exclusive={t:bits for t,bits in cores.items() if t not in outside_support}
    loss=[sorted(t for t,bits in exclusive.items() if bits>>j&1) for j in range(len(new_cycles[ci]))]
    cut_reports.append(dict(cycle=ci,length=len(new_cycles[ci]),
        exclusive_target_rank_counts=dict(sorted(Counter(t.bit_count() for t in exclusive).items())),
        exclusive_target_cut_cores={str(t):hex(bits) for t,bits in exclusive.items()},
        globally_safe_cut_positions=[j for j,ts in enumerate(loss) if not ts],
        min_forced_exclusive_loss=min(map(len,loss)),
        forced_exclusive_loss_counts=list(map(len,loss)),
        forced_exclusive_losses_by_cut=loss))

def rank_list(targets):
    return {str(r):sorted(t for t in targets if t.bit_count()==r)
            for r in sorted({t.bit_count() for t in targets})}

report=dict(
    k=N,template="MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md",
    old_edges=old_edges,new_edges=new_edges,
    affected_old_cycle_ids=affected_ids,
    affected_old_lengths=[len(c) for c in affected_old],
    new_lengths=[len(c) for c in new_cycles],
    affected_old_lower_cycles=affected_old,new_lower_cycles=new_cycles,
    local_upper_lost_by_rank=rank_list(lost),local_upper_gained_by_rank=rank_list(gained),
    local_upper_target_rank_counts=dict(sorted(Counter(t.bit_count() for t in old_upper).items())),
    global_upper_lost_by_rank=rank_list(lost_global),
    local_old_witnesses={str(t):old_witness[t] for t in lost},
    local_new_witnesses={str(t):new_witness[t] for t in gained},
    complete_local_upper_transport={str(t):dict(old=old_witness[t],new=new_witness[t])
                                    for t in sorted(old_upper & new_upper)},
    old_positive_run_histogram=dict(sorted(old_hist.items())),
    new_positive_run_histogram=dict(sorted(new_hist.items())),
    old_short_positive_runs=old_short,new_short_positive_runs=new_short,
    lower_rank8_pair_multiset_preserved=True,
    global_proper_upper_targets_after=len(new_upper|outside_upper),
    all_owner_degrees_two=True,
    new_cycle_cut_reports=cut_reports,
)
Path("rigid_c6.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({k:report[k] for k in (
    "affected_old_cycle_ids","affected_old_lengths","new_lengths",
    "global_upper_lost_by_rank","old_positive_run_histogram","new_positive_run_histogram",
    "lower_rank8_pair_multiset_preserved","global_proper_upper_targets_after")},indent=2))
print("local lost counts", dict(Counter(t.bit_count() for t in lost)))
print("local gained counts", dict(Counter(t.bit_count() for t in gained)))
print("new short runs",json.dumps(new_short))
for rec in cut_reports:
    print("CUT REPORT",json.dumps({k:rec[k] for k in ("cycle","length","exclusive_target_rank_counts","globally_safe_cut_positions","min_forced_exclusive_loss")}))
print("local upper rank counts",report["local_upper_target_rank_counts"])
print("PASS prescribed-surgery verification completed; full exact record rigid_c6.json")
