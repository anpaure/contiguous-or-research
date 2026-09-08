#!/usr/bin/env python3
"""Exact finite DP gate, canonical k17 only. Mathematical execution: h100 only."""
import contextlib,io,json,runpy
from collections import Counter
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path('audit.py')
cs=m['cycles']; records=m['records']; cores=m['locals_']; suppliers=m['suppliers']; FULL=m['FULL']; N=m['N']
bad=sorted(m['summary']['bad_sector_components']); bi={c:i for i,c in enumerate(bad)}
onlybad={t for t,v in suppliers.items() if set(v)<=set(bad)}
assert len(onlybad)==102
options=[]; jointports={}
for c in bad:
    fatal=0
    for t in onlybad: fatal |= cores[c].get(t,0)
    safe=[i for i in range(len(cs[c])) if not(fatal>>i&1)]
    assert len(safe)==17
    jointports[c]=safe
    w=[FULL^a for a in cs[c]]
    for cut in safe:
        base=w[cut:]+w[:cut]
        for rev in [False,True]:
            p=base[::-1] if rev else base
            pref=[]; suff=[]
            for b in range(N):
                a=0
                while a<len(p) and (p[a]>>b&1): a+=1
                z=0
                while z<len(p) and (p[-1-z]>>b&1): z+=1
                assert a<len(p) and z<len(p)
                pref.append(a); suff.append(z)
            options.append(dict(cycle=c,color=bi[c],cut=cut,reverse=rev,head=p[0],tail=p[-1],prefix=pref,suffix=suff,path=p))

def compatible(a,b):
    if a['color']==b['color']: return False
    if (a['tail']^b['head']).bit_count()!=2: return False
    for x,y in zip(a['suffix'],b['prefix']):
        if 0<x+y<3: return False
    return True
edges=[[j for j,b in enumerate(options) if compatible(a,b)] for a in options]
reach={}
for i,o in enumerate(options): reach[(1<<o['color'],i)]=None
levels=Counter({1:len(reach)})
for size in range(1,6):
    current=[s for s in reach if s[0].bit_count()==size]
    for mask,i in current:
        for j in edges[i]:
            bit=1<<options[j]['color']
            if mask&bit: continue
            ns=(mask|bit,j)
            if ns not in reach: reach[ns]=(mask,i)
    levels[size+1]=sum(mask.bit_count()==size+1 for mask,i in reach)
terminals=[s for s in reach if s[0]==63]
result={'k':17,'bad_cycles':bad,'joint_safe_ports':jointports,'only_bad_supplied_upper_targets':102,'only_bad_supplier_pair_counts':{','.join(map(str,a)):v for a,v in Counter(tuple(suppliers[t]) for t in onlybad).items()},'oriented_options':len(options),'directed_compatible_option_pairs':sum(map(len,edges)),'compatibility_cycle_pair_counts':{str((bad[a],bad[b])):sum(options[i]['color']==a and options[j]['color']==b for i in range(len(options)) for j in edges[i]) for a in range(6) for b in range(6) if a!=b},'reachable_states_by_color_count':dict(levels),'terminal_state_count':len(terminals),'status':'SAT' if terminals else 'UNSAT'}
if terminals:
    z=min(terminals); chain=[]
    while z is not None:
        chain.append(z[1]); z=reach[z]
    chain.reverse(); word=[a for o in chain for a in options[o]['path']]
    assert len(word)==len(set(word))==306
    assert all(a.bit_count()==9 for a in word)
    assert all((a^b).bit_count()==2 for a,b in zip(word,word[1:]))
    for b in range(N):
        i=0
        while i<len(word):
            if not(word[i]>>b&1): i+=1; continue
            j=i+1
            while j<len(word) and word[j]>>b&1: j+=1
            if i>0 and j<len(word): assert j-i>=3
            i=j
    covered=set()
    for cid,c in enumerate(cs):
        if cid in bi: continue
        w=[FULL^a for a in c]
        for i in range(len(w)):
            a=w[i]
            for q in range(1,len(w)):
                a|=w[(i+q)%len(w)]
                if a==FULL: break
                covered.add(a)
    for i in range(len(word)):
        a=0
        for j in range(i,len(word)):
            a|=word[j]
            if a==FULL: break
            covered.add(a)
    expected={t for t in suppliers}
    assert expected<=covered
    Path('badsix_306_owner_path.word').write_text('\n'.join(map(str,word))+'\n')
    result['chosen_options']=[{k:v for k,v in options[i].items() if k!='path'} for i in chain]
    result['retained_all_global_upper_targets']=len(expected)
# Complete adjacency and reachable state certificates support deterministic replay in either case.
certificate={'result':result,'options':[{k:v for k,v in o.items() if k!='path'} for o in options],'adjacency':edges,'reachable_states':[list(s) for s in sorted(reach)]}
Path('badsix_decision.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('PASS: exact gate and independent literal replay completed' if terminals else 'PASS: exact finite DP exhausted every color/last-option state; no admissible path on this port bank')
