#!/usr/bin/env python3
"""One fixed pre-fusion lower-bank census; all mathematical execution on h100."""
import json
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
old=Path('/home/amodo/exact-b-k17-pbbs-inventory-20260908')
new=Path('/home/amodo/exact-b-k17-badsix-all-ports-20260908')
inventory=json.loads((old/'inventory.json').read_text())
N=17; FULL=(1<<N)-1; bad=set(inventory['summary']['bad_sector_components'])
cache={}
def f(a):
    if a in cache:return cache[a]
    for u in range(N):
        if a>>u&1:continue
        h=0
        for j in range(1,N):
            h += 1 if a>>((u+j)%N)&1 else -1
            if h<0:break
        else:
            assert h==0
            cache[a]=FULL^a^(1<<u)
            return cache[a]
    raise AssertionError('no root')

banks=[]; covered_owner_masks=set()
for rec in inventory['cycles']:
    if rec['cycle'] in bad:continue
    a=rec['first_lower_owner']; q=a; owners=[]
    while q not in covered_owner_masks:
        covered_owner_masks.add(q); owners.append(FULL^q);q=f(f(q))
    assert q==a and len(owners)==rec['length']
    L=len(owners)
    E=[owners[(j-3)%L]&owners[(j-2)%L]&owners[(j-1)%L]&owners[j] for j in range(L)]
    assert all(x.bit_count()==6 for x in E)
    assert all((E[j]|E[(j+1)%L]).bit_count()==7 for j in range(L))
    assert all((E[j]|E[(j+1)%L]|E[(j+2)%L]).bit_count()==8 for j in range(L))
    assert all(E[j]|E[(j+1)%L]|E[(j+2)%L]|E[(j+3)%L]==owners[j] for j in range(L))
    banks.append((rec['cycle'],True,E))
assert len(banks)==140 and sum(len(E) for _,_,E in banks)==24004
P=list(map(int,(new/'badsix_all_ports_306_owner_path.word').read_text().split()))
EP=list(map(int,(new/'badsix_all_ports_308_depth2_source.word').read_text().split()))
assert len(P)==306 and len(EP)==308
assert all(EP[i]|EP[i+1]|EP[i+2]==p for i,p in enumerate(P))
assert min(x.bit_count() for x in EP)==7
assert all((a|b).bit_count()>=8 for a,b in zip(EP,EP[1:]))
banks.append(('prefix',False,EP))

letters=Counter(); pairs=Counter(); good_pairs=set(); prefix7=set()
host_count=[0]*(1<<N); core_hist=Counter(); singleton_hosts=defaultdict(list)
for cid,cyclic,E in banks:
    L=len(E); letters.update(E)
    if cid=='prefix':prefix7={x for x in E if x.bit_count()==7}
    for j in range(L if cyclic else L-1):
        v=E[j]|E[(j+1)%L];pairs[v]+=1
        if cyclic:good_pairs.add(v)
    for i,a in enumerate(E):
        core=0
        if cyclic or i>0:core |= a&~E[(i-1)%L]
        if cyclic or i<L-1:core |= a&~E[(i+1)%L]
        core_hist[(str(cid)=='prefix',core.bit_count())]+=1
        free=a&~core; z=free
        while True:
            S=core|z
            if S and S.bit_count()<=6:
                host_count[S]+=1
                if S.bit_count()==1:singleton_hosts[S].append([cid,i])
            if z==0:break
            z=(z-1)&free

missing6=[t for t in range(1,FULL) if t.bit_count()==6 and t not in letters]
covered7={t for t in pairs if t.bit_count()==7}|{t for t in letters if t.bit_count()==7}
missing7=[t for t in range(1,FULL) if t.bit_count()==7 and t not in covered7]
stats={};zero_hosts={}
for rank in range(1,7):
    ts=[t for t in range(1,FULL) if t.bit_count()==rank]
    assert len(ts)==comb(N,rank)
    vals=[host_count[t] for t in ts]
    zero_hosts[rank]=[t for t in ts if not host_count[t]]
    stats[rank]={'targets':len(ts),'zero_host_targets':sum(v==0 for v in vals),'min_hosts':min(vals),'max_hosts':max(vals),'incidences':sum(vals)}
summary={'good_cycles':140,'cyclic_source_positions':24004,'prefix_source_positions':308,'total_indexed_source_positions':24312,'good_pair_rank7_targets':len(good_pairs),'prefix_rank7_letter_targets':len(prefix7),'prefix_additional_rank7_targets':len(prefix7-good_pairs),'rank7_covered':len(covered7),'rank7_missing_count':len(missing7),'rank6_literal_letter_targets':sum(t.bit_count()==6 for t in letters),'rank6_missing_count':len(missing6),'letter_rank_histogram':dict(sorted(Counter({r:sum(c for t,c in letters.items() if t.bit_count()==r) for r in range(1,10)}).items())),'pair_rank_histogram':{r:sum(c for t,c in pairs.items() if t.bit_count()==r) for r in range(1,11)},'individual_single_letter_host_statistics':stats,'minimum_core_size_histogram':{str(k):v for k,v in sorted(core_hist.items())},'singleton_host_count_by_coordinate':{s.bit_length()-1:len(v) for s,v in singleton_hosts.items()}}
result={'summary':summary,'missing_rank7':missing7,'missing_rank6_letters':missing6,'prefix_added_rank7':sorted(prefix7-good_pairs),'zero_host_targets':zero_hosts,'singleton_hosts':{str(s):v for s,v in singleton_hosts.items()},'scope':'indexed collection of140periodic good-cycle depth3 antecedents plusone308letter prefix; before any Q fusion; individual hosts are not simultaneous caps'}
(new/'good_cycle_lower_bank.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2));print('missing_rank7',missing7)
print('PASS fixed pre-fusion lower-bank identities and individual legal-host census')
