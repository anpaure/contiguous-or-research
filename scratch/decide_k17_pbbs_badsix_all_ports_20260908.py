#!/usr/bin/env python3
"""Complete 612-option fixed-six-cycle decision. Execute only on h100."""
import contextlib
import io
import json
import resource
import runpy
import signal
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (90,90))
resource.setrlimit(resource.RLIMIT_AS, (2*1024**3,2*1024**3))
signal.alarm(110)
with contextlib.redirect_stdout(io.StringIO()):
    old=runpy.run_path("/home/amodo/exact-b-k17-pbbs-inventory-20260908/audit.py")
cs=old["cycles"]
FULL=old["FULL"]
N=old["N"]
bad=sorted(old["summary"]["bad_sector_components"])
bi={c:i for i,c in enumerate(bad)}
options=[]
for cid in bad:
    w=[FULL^a for a in cs[cid]]
    assert len(w)==51
    for cut in range(len(w)):
        base=w[cut:]+w[:cut]
        for reverse in (False,True):
            path=base[::-1] if reverse else base
            prefix=[]
            suffix=[]
            for bit in range(N):
                p=s=0
                while p<len(path) and path[p]>>bit&1:
                    p+=1
                while s<len(path) and path[-1-s]>>bit&1:
                    s+=1
                assert p<len(path) and s<len(path)
                prefix.append(p)
                suffix.append(s)
            options.append(dict(cycle=cid,color=bi[cid],cut=cut,reverse=reverse,
                                head=path[0],tail=path[-1],prefix=prefix,suffix=suffix,path=path))
assert len(options)==612

def compatible(a,b):
    if a["color"]==b["color"]:
        return False
    if any(0<x+y<3 for x,y in zip(a["suffix"],b["prefix"])):
        return False
    if not (a["path"][-2]&a["path"][-1]&b["path"][0]):
        return False
    if not (a["path"][-1]&b["path"][0]&b["path"][1]):
        return False
    return True

edges=[[j for j,b in enumerate(options) if compatible(a,b)] for a in options]
distance={(1<<o["color"],i):0 for i,o in enumerate(options)}
predecessor={state:None for state in distance}
for size in range(1,6):
    for mask,i in [s for s in distance if s[0].bit_count()==size]:
        for j in edges[i]:
            bit=1<<options[j]["color"]
            if mask&bit:
                continue
            new=(mask|bit,j)
            cost=distance[mask,i]+int((options[i]["tail"]^options[j]["head"]).bit_count()!=2)
            if new not in distance or cost<distance[new]:
                distance[new]=cost
                predecessor[new]=(mask,i)
terminals=[state for state in distance if state[0]==63]
result=dict(k=17,bad_cycles=bad,oriented_options=len(options),
            guarded_option_arcs=sum(map(len,edges)),
            reachable_states_by_color_count=dict(sorted(Counter(m.bit_count() for m,i in distance).items())),
            terminal_states=len(terminals),
            minimum_non_johnson_seams=min((distance[s] for s in terminals),default=None),
            resource_cap=dict(cpu_seconds=90,wall_seconds=110,memory_bytes=2*1024**3))
if terminals:
    state=min(terminals,key=lambda s:(distance[s],s))
    chosen=[]
    while state is not None:
        chosen.append(state[1])
        state=predecessor[state]
    chosen.reverse()
    word=[v for i in chosen for v in options[i]["path"]]
    assert len(word)==len(set(word))==306
    internal_runs=Counter()
    for bit in range(N):
        i=0
        while i<len(word):
            if not (word[i]>>bit&1):
                i+=1
                continue
            j=i+1
            while j<len(word) and word[j]>>bit&1:
                j+=1
            if i>0 and j<len(word):
                internal_runs[j-i]+=1
                assert j-i>=3
            i=j
    source=[]
    for p in range(308):
        acc=FULL
        for i in range(max(0,p-2),min(p,305)+1):
            acc &= word[i]
        assert acc
        source.append(acc)
    assert all(source[i]|source[i+1]|source[i+2]==word[i] for i in range(306))
    outside_upper=set()
    outside_facets=Counter()
    for cid,c in enumerate(cs):
        if cid in bi:
            continue
        w=[FULL^a for a in c]
        for a,b in zip(w,w[1:]+w[:1]):
            color=a&b
            assert color.bit_count()==8
            outside_facets[color]+=1
        for i in range(len(w)):
            acc=w[i]
            for q in range(1,len(w)):
                acc |= w[(i+q)%len(w)]
                if acc==FULL:
                    break
                outside_upper.add(acc)
    prefix_upper=set()
    for i in range(len(word)):
        acc=word[i]
        for j in range(i+1,len(word)):
            acc |= word[j]
            if acc==FULL:
                break
            if acc.bit_count()>=10:
                prefix_upper.add(acc)
    prefix_facets=Counter(a&b for a,b in zip(word,word[1:]) if (a&b).bit_count()==8)
    allfacets=outside_facets+prefix_facets
    missing_facets=sorted(set(old["states"])-set(allfacets))
    expected_upper=set(old["suppliers"])
    missing_upper=sorted(expected_upper-(outside_upper|prefix_upper))
    only_bad={t for t,s in old["suppliers"].items() if set(s)<=set(bad)}
    assert len(only_bad)==102
    b=sum((a^c).bit_count()!=2 for a,c in zip(word,word[1:]))
    e=sum(prefix_facets.values())-len(prefix_facets)
    Path("badsix_all_ports_306_owner_path.word").write_text("\n".join(map(str,word))+"\n")
    Path("badsix_all_ports_308_depth2_source.word").write_text("\n".join(map(str,source))+"\n")
    result.update(chosen_option_indices=chosen,
        chosen_options=[{k:v for k,v in options[i].items() if k!="path"} for i in chosen],
        owner_count=len(word),source_length=len(source),source_minimum_rank=min(v.bit_count() for v in source),
        depth2_replay=True,internal_positive_run_histogram=dict(sorted(internal_runs.items())),
        actual_non_johnson_count=b,prefix_rank8_occurrences=sum(prefix_facets.values()),
        prefix_distinct_rank8=len(prefix_facets),prefix_internal_rank8_duplicate_excess=e,
        prefix_necessary_facet_charge=b+e,
        prefix_repeated_rank8={str(t):q for t,q in prefix_facets.items() if q>1},
        global_rank8_palette_missing_count=len(missing_facets),global_rank8_palette_missing_masks=missing_facets,
        global_rank8_duplicate_excess=sum(allfacets.values())-len(allfacets),
        global_proper_upper_retained_count=len(expected_upper-set(missing_upper)),
        global_proper_upper_missing_masks=missing_upper,
        global_proper_upper_missing_by_rank=dict(sorted(Counter(t.bit_count() for t in missing_upper).items())),
        only_bad_upper_targets_retained=len(only_bad&prefix_upper),
        only_bad_upper_targets_missing=sorted(only_bad-prefix_upper))

certificate=dict(result=result,
    options=[{k:v for k,v in o.items() if k!="path"} for o in options],
    adjacency=edges,
    distance_states=[[mask,i,cost] for (mask,i),cost in sorted(distance.items())])
Path("badsix_all_ports_decision.json").write_text(json.dumps(certificate,indent=2)+"\n")
print(json.dumps(result,indent=2))
print("PASS: exact all-ports state-space decision completed; no random search")
