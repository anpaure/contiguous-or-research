#!/usr/bin/env python3
"""Fixed k17 canonical PBBS census. Run mathematical code only on h100."""
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

R=8; N=17; FULL=(1<<N)-1

def root(mask):
    for u in range(N):
        if mask>>u&1: continue
        h=0
        for j in range(1,N):
            h += 1 if mask>>((u+j)%N)&1 else -1
            if h<0: break
        else:
            assert h==0
            return u
    raise AssertionError('no canonical root')

states=[sum(1<<i for i in c) for c in combinations(range(N),R)]
fm={a:FULL^a^(1<<root(a)) for a in states}
assert len(set(fm.values()))==len(states)
unseen=set(states); cycles=[]
while unseen:
    a=min(unseen); p=a; c=[]
    while p in unseen:
        c.append(p); unseen.remove(p); p=fm[fm[p]]
    assert p==a
    cycles.append(c)

locals_=[]; suppliers=defaultdict(list); records=[]
for cid,c in enumerate(cycles):
    w=[FULL^a for a in c]; L=len(w); cores={}; occurrences=Counter()
    runs=Counter()
    for b in range(N):
        starts=[i for i in range(L) if w[i]>>b&1 and not (w[i-1]>>b&1)]
        assert starts
        for i in starts:
            q=0
            while w[(i+q)%L]>>b&1: q+=1
            assert q<L
            runs[q]+=1
    for i in range(L):
        acc=w[i]; fatal=0
        for q in range(1,L):
            fatal |= 1<<((i+q)%L)
            prev=acc; acc |= w[(i+q)%L]
            if acc==FULL: break
            if acc==prev: continue
            assert acc.bit_count()>=10
            if acc in cores: cores[acc] &= fatal
            else: cores[acc]=fatal
            occurrences[acc]+=1
        else: raise AssertionError('cycle does not cover full universe')
    locals_.append(cores)
    for t in cores: suppliers[t].append(cid)
    u=root(c[0]); ds=''.join('1' if c[0]>>((u+j)%N)&1 else '0' for j in range(1,N))
    height=0; h=0
    for x in ds:
        h += 1 if x=='1' else -1; height=max(height,h)
    records.append(dict(cycle=cid,length=L,first_lower_owner=c[0],root=u,root_dyck=ds,height=height,positive_run_counts=dict(sorted(runs.items())),bad_sector=runs[3]>0,local_target_rank_counts=dict(sorted(Counter(t.bit_count() for t in cores).items())),changed_interval_occurrences=sum(occurrences.values())))

for cid,cores in enumerate(locals_):
    L=len(cycles[cid]); allfatal=0; exclusivefatal=0
    exclusives_by_rank=Counter(); forcedlost=[Counter() for _ in range(L)]
    exclusivecores={}; exclzero=Counter()
    for t,bits in cores.items():
        allfatal |= bits
        if len(suppliers[t])!=1: continue
        rk=t.bit_count(); exclusives_by_rank[rk]+=1
        exclusivefatal |= bits
        if not bits: exclzero[rk]+=1
        exclusivecores[str(t)]=hex(bits)
        x=bits
        while x:
            low=x&-x; j=low.bit_length()-1
            forcedlost[j][rk]+=1; x-=low
    rec=records[cid]
    rec.update(exclusive_target_rank_counts=dict(sorted(exclusives_by_rank.items())),exclusive_targets_with_empty_cut_core=dict(sorted(exclzero.items())),one_cut_global_safe_positions=[i for i in range(L) if not(exclusivefatal>>i&1)],all_local_targets_safe_positions=[i for i in range(L) if not(allfatal>>i&1)],forced_exclusive_losses_min=min(sum(x.values()) for x in forcedlost),forced_exclusive_losses_max=max(sum(x.values()) for x in forcedlost),forced_exclusive_loss_rank_totals=dict(sorted(sum(forcedlost,Counter()).items())))
    rec['forced_exclusive_losses_by_position']=[dict(sorted(x.items())) for x in forcedlost]
    rec['exclusive_target_cut_cores']=exclusivecores

expected=Counter()
for bits in combinations(range(N),10): pass
# Every proper upper target must be present in the canonical complete-shadow factor.
for t in range(1,FULL):
    if t.bit_count()>=10: expected[t.bit_count()]+=1; assert t in suppliers
summary=dict(k=N,owner_count=len(states),component_count=len(cycles),component_length_histogram=dict(sorted(Counter(map(len,cycles)).items())),bad_sector_components=[r['cycle'] for r in records if r['bad_sector']],bad_sector_owners=sum(r['length'] for r in records if r['bad_sector']),positive_run3_count=sum(r['positive_run_counts'].get(3,0) for r in records),upper_target_rank_counts=dict(sorted(expected.items())),target_supplier_component_histogram=dict(sorted(Counter(len(c) for c in suppliers.values()).items())),cycles_with_no_one_cut_global_safe_position=[r['cycle'] for r in records if not r['one_cut_global_safe_positions']],cycles_with_no_all_local_safe_position=[r['cycle'] for r in records if not r['all_local_targets_safe_positions']],all_one_cut_global_safe_positions=sum(len(r['one_cut_global_safe_positions']) for r in records))
assert summary['bad_sector_owners']==306
assert summary['positive_run3_count']==119
out=dict(summary=summary,cycles=records,method='canonical original f by root scan; all changing interval ORs until full; targetwise intersection of fatal cut sets; exclusive suppliers counted globally')
Path('inventory.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('COMPACT CYCLE RECORDS')
for r in records:
    print(json.dumps({k:r[k] for k in ['cycle','length','root_dyck','height','bad_sector','exclusive_target_rank_counts','one_cut_global_safe_positions','forced_exclusive_losses_min','forced_exclusive_losses_max']},sort_keys=True))
print('PASS: complete proper upper target census and exact per-cycle cut-core record written to inventory.json')
