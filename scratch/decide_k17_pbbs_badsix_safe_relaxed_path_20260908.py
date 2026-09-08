#!/usr/bin/env python3
"""Last exact bounded relaxation of the same 204 k17 port options; h100 only."""
import contextlib,io,json,runpy
from collections import Counter
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    old=runpy.run_path('decide.py')
options=old['options']; cs=old['cs']; bad=old['bad']; FULL=old['FULL']; N=old['N']; bi=old['bi']
def compatible(a,b):
    if a['color']==b['color']: return False
    if any(0<x+y<3 for x,y in zip(a['suffix'],b['prefix'])): return False
    if not(a['path'][-2]&a['path'][-1]&b['path'][0]): return False
    if not(a['path'][-1]&b['path'][0]&b['path'][1]): return False
    return True
edges=[[j for j,b in enumerate(options) if compatible(a,b)] for a in options]
dist={(1<<a['color'],i):0 for i,a in enumerate(options)}; pred={s:None for s in dist}
for size in range(1,6):
    for mask,i in [s for s in dist if s[0].bit_count()==size]:
        for j in edges[i]:
            bit=1<<options[j]['color']
            if mask&bit: continue
            ns=(mask|bit,j)
            cost=dist[mask,i]+int((options[i]['tail']^options[j]['head']).bit_count()!=2)
            if ns not in dist or cost<dist[ns]: dist[ns]=cost; pred[ns]=(mask,i)
terminals=[s for s in dist if s[0]==63]
result={'k':17,'status':'SAT' if terminals else 'UNSAT','oriented_options':len(options),'guarded_option_arcs':sum(map(len,edges)),'reachable_states_by_color_count':dict(sorted(Counter(mask.bit_count() for mask,i in dist).items())),'terminal_states':len(terminals),'minimum_non_johnson_seams':min((dist[s] for s in terminals),default=None),'pair_arcs':{str((bad[a],bad[b])):sum(options[i]['color']==a and options[j]['color']==b for i in range(len(options)) for j in edges[i]) for a in range(6) for b in range(6) if a!=b}}
if terminals:
    z=min(terminals,key=lambda s:(dist[s],s)); chosen=[]
    while z is not None:
        chosen.append(z[1]); z=pred[z]
    chosen.reverse(); word=[a for i in chosen for a in options[i]['path']]
    assert len(word)==len(set(word))==306
    E=[]
    for j in range(len(word)+2):
        a=FULL
        for i in range(max(0,j-2),min(j,len(word)-1)+1): a&=word[i]
        assert a
        E.append(a)
    assert all(E[i]|E[i+1]|E[i+2]==t for i,t in enumerate(word))
    rank8=set(); upp=set()
    for cid,c in enumerate(cs):
        if cid in bi: continue
        w=[FULL^a for a in c]
        rank8.update(a&b for a,b in zip(w,w[1:]+w[:1]))
        for i in range(len(w)):
            a=w[i]
            for q in range(1,len(w)):
                a|=w[(i+q)%len(w)]
                if a==FULL: break
                upp.add(a)
    rank8.update(a&b for a,b in zip(word,word[1:]) if (a&b).bit_count()==8)
    for i in range(len(word)):
        a=0
        for j in range(i,len(word)):
            a|=word[j]
            if a==FULL: break
            upp.add(a)
    expected=set(old['suppliers']); assert expected<=upp
    missing8=[t for t in range(FULL) if t.bit_count()==8 and t not in rank8]
    Path('badsix_relaxed_306_owner_path.word').write_text('\n'.join(map(str,word))+'\n')
    Path('badsix_relaxed_308_depth2_source.word').write_text('\n'.join(map(str,E))+'\n')
    result.update(chosen_options=[{k:v for k,v in options[i].items() if k!='path'} for i in chosen],owner_count=len(word),depth2_source_length=len(E),envelope_min_rank=min(x.bit_count() for x in E),depth2_replay=True,retained_all_global_upper_targets=len(expected),global_rank8_adjacent_palette_missing=len(missing8),missing_rank8_masks=missing8)
certificate={'result':result,'adjacency':edges,'distance_states':[[mask,i,cost] for (mask,i),cost in sorted(dist.items())]}
Path('badsix_relaxed_decision.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('PASS: complete exact relaxed state-space decision; literal source replay if SAT')
