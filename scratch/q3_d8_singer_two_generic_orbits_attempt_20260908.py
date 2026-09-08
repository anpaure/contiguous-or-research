"""One Singer-family inventory, with one optional bounded solver stage."""
import os,sys,json,time,resource
from collections import Counter
from itertools import combinations,product
from functools import reduce
from operator import xor
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
CAT='/tmp/Q3_D8_SINGER_TWO_GENERIC_ORBITS_CATALOGUE_20260908_ternarylift.json'
WIT='/tmp/Q3_D8_SINGER_TWO_GENERIC_ORBITS_WITNESS_20260908_ternarylift.json'
S=[0,2,4,6,3,1,7,5]
POW=[3**i for i in range(8)]


def metadata(data):
    out={}
    for t in data['critical']:
        code=data['reps'][t]; x=[(code//p)%3 for p in POW]
        O=[i for i,v in enumerate(x) if v==1]; b=reduce(xor,O,0)
        T=[i^b for i,v in enumerate(x) if v==2]
        if len(O)==7: cls='A'
        elif len(O)==5: cls='B'
        elif len(O)==3: cls='C' if x[b]==2 else 'D'
        else: cls='E' if reduce(xor,T,0)==0 else 'F'
        out[t]=dict(cls=cls,direction=reduce(xor,T,0) if cls=='F' else None,
                    L=sorted(i^b for i in O) if cls=='C' else None,
                    a=next((a for a in T if a),None) if cls=='C' else None)
    return out


def canonical_key(H,v,w):
    w=tuple(w)
    reflected=tuple(a^w[-1] for a in reversed(w))
    return tuple(sorted(H)),v,min(w,reflected)


def catalogue():
    with open(BASE) as f: data=json.load(f)
    candidates=data['candidates']; meta=metadata(data)
    critical=set(data['critical']); Cnodes={t for t in critical if meta[t]['cls']=='C'}
    rels=[{t for t in critical if meta[t]['cls'] in ('A','B')}]
    rels += [{t for t in critical if meta[t]['cls']=='F' and meta[t]['direction']==d} for d in range(1,8)]
    generic=[i for i,c in enumerate(candidates) if c['mode']=='short' and c['row_count']==8
             and len(set(c['critical'])&Cnodes)==2]
    assert len(generic)==1008
    lookup={canonical_key(candidates[i]['H'],candidates[i]['v'],candidates[i]['word']):i for i in generic}
    edge_counts=Counter(); class_patterns=Counter()
    for i in generic:
        c=candidates[i]; edge=tuple(sorted(set(c['critical'])&Cnodes)); edge_counts[edge]+=1
        class_patterns[tuple(sorted(Counter(meta[t]['cls'] for t in c['critical']).items()))]+=1
    adjacency={t:set() for t in Cnodes}
    for a,b in edge_counts:
        adjacency[a].add(b); adjacency[b].add(a)
    antiflag_matches=all(((a,b) in edge_counts)==(meta[a]['a'] in meta[b]['L'] and meta[b]['a'] in meta[a]['L'])
                        for a,b in combinations(sorted(Cnodes),2))
    visited=set(); aggregates=[]; aggregate_class_patterns=Counter(); rejected=0
    for i in generic:
        if i in visited: continue
        orbit=[]; j=i
        for _ in range(7):
            assert j not in orbit
            orbit.append(j)
            c=candidates[j]
            key=canonical_key([S[a] for a in c['H']],S[c['v']],[S[a] for a in c['word']])
            j=lookup[key]
        assert j==i and not(set(orbit)&visited)
        visited.update(orbit)
        crit=[t for j in orbit for t in candidates[j]['critical']]
        if len(set(crit))!=42:
            rejected+=1
            continue
        assert len(set(crit)&Cnodes)==14
        cover=sorted(set(t for j in orbit for t in candidates[j]['cover']))
        aggregates.append(dict(candidate_ids=orbit,critical=sorted(crit),cover=cover))
        aggregate_class_patterns[tuple(sorted(Counter(meta[t]['cls'] for t in crit).items()))]+=1
    assert len(visited)==1008 and len(aggregates)+rejected==144
    full_ids=[i for i,c in enumerate(candidates) if c['mode']=='full']
    self_ids=[i for i,c in enumerate(candidates) if c['mode']=='short' and c['row_count']==4]
    pairs=[]; disjoint_pairs=0; parity_pairs=0; no_full=0; core_classes=Counter()
    for a,b in combinations(range(len(aggregates)),2):
        ca=set(aggregates[a]['critical']); cb=set(aggregates[b]['critical'])
        if ca&cb: continue
        union=ca|cb; assert Cnodes<=union
        disjoint_pairs+=1
        if any(len(union&r)%2 for r in rels): continue
        parity_pairs+=1
        compatible=[i for i in full_ids if not(set(candidates[i]['critical'])&union)]
        if not compatible:
            no_full+=1
            continue
        core=critical-union
        cover=sorted(set(aggregates[a]['cover'])|set(aggregates[b]['cover']))
        pairs.append(dict(aggregates=[a,b],critical=sorted(union),core=sorted(core),
                          compatible_full_ids=compatible,cover=cover))
        core_classes[tuple(sorted(Counter(meta[t]['cls'] for t in core).items()))]+=1
    report=dict(stage='catalogue',elapsed=time.monotonic()-START,
                generic_two_C_count=len(generic),C_graph_edges=len(edge_counts),
                C_graph_degree_distribution=dict(Counter(map(len,adjacency.values()))),
                C_graph_edge_multiplicity_distribution=dict(Counter(edge_counts.values())),
                C_graph_equals_mutual_antiflag_incidence=antiflag_matches,
                generic_class_patterns=[dict(pattern=dict(p),count=n) for p,n in class_patterns.items()],
                singer_aggregates_before_filter=144,internally_disjoint_aggregates=len(aggregates),
                rejected_aggregates=rejected,
                aggregate_class_patterns=[dict(pattern=dict(p),count=n) for p,n in aggregate_class_patterns.items()],
                critical_disjoint_pairs=disjoint_pairs,parity_passing_pairs=parity_pairs,
                parity_pairs_without_compatible_full=no_full,source_pairs=len(pairs),
                core_class_patterns=[dict(pattern=dict(p),count=n) for p,n in core_classes.items()],
                compatible_full_count_distribution=dict(Counter(len(p['compatible_full_ids']) for p in pairs)),cache=CAT)
    with open(CAT,'w') as f:
        json.dump(dict(aggregates=aggregates,pairs=pairs,report=report),f)
    report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)


def replay(selected):
    def chain(w,g):
        x=[0]*8; out=[tuple(x)]
        for a in w:
            x[a^g]+=1; out.append(tuple(x))
        return out
    rows=set()
    for c in selected:
        for w in c['words']:
            for g in range(8):
                C,D=chain(w,g),chain(w,g^c['v'])
                if c['mode']=='short': C,D=C[1:8],D[1:8]
                rows.add(tuple(sorted((tuple(C),tuple(D)))))
    loads=[0]*6561
    for C,D in rows:
        for Q in (C,D):
            assert len({sum(x) for x in Q})==len(Q)
            for a,b in zip(Q,Q[1:]): assert all(u<=v for u,v in zip(a,b)) and a!=b
        A={i for x in C for i,v in enumerate(x) if v}; B={i for x in D for i,v in enumerate(x) if v}
        assert len(A)==len(B)==4 and A.isdisjoint(B)
        for a in C:
            for b in D:
                x=tuple(u+v for u,v in zip(a,b)); assert all(0<=v<=2 for v in x)
                loads[sum(v*p for v,p in zip(x,POW))]+=1
    cost=sum(len(C)+len(D) for C,D in rows)
    assert len(rows)==168 and cost==2368 and min(loads)>=1
    for x in product(range(3),repeat=8):
        if sum(x) in (7,9): assert loads[sum(v*p for v,p in zip(x,POW))]==1
    with open(WIT,'w') as f:
        json.dump(dict(selected=selected,rows=sorted(rows),loads=loads,cost=cost),f)
    return dict(row_count=len(rows),cost=cost,minimum_load=min(loads),maximum_load=max(loads),witness=WIT)


def solve():
    with open(BASE) as f: base=json.load(f)
    with open(CAT) as f: data=json.load(f)
    pairs=data['pairs']; assert 0<len(pairs)<=100
    from ortools.sat.python import cp_model
    candidates=base['candidates']
    row_ids=[i for i,c in enumerate(candidates) if c['mode']=='full' or(c['mode']=='short' and c['row_count']==4)]
    model=cp_model.CpModel()
    x=[model.new_bool_var('x'+str(i)) for i in row_ids]
    p=[model.new_bool_var('p'+str(i)) for i in range(len(pairs))]
    model.add(sum(p)==1)
    model.add(sum(z for i,z in zip(row_ids,x) if candidates[i]['mode']=='full')==1)
    model.add(sum(z for i,z in zip(row_ids,x) if candidates[i]['mode']=='short')==13)
    bytarget=[[] for _ in base['reps']]
    for i,z in zip(row_ids,x):
        for t in candidates[i]['cover']: bytarget[t].append(z)
    for pair,z in zip(pairs,p):
        for t in pair['cover']: bytarget[t].append(z)
    critical=set(base['critical'])
    for t,zs in enumerate(bytarget):
        model.add(sum(zs)==1) if t in critical else model.add(sum(zs)>=1)
    solver=cp_model.CpSolver(); solver.parameters.max_time_in_seconds=10.0
    solver.parameters.num_search_workers=2; solver.parameters.random_seed=0
    solver.parameters.stop_after_first_solution=True
    setup=time.monotonic()-START; status=solver.solve(model)
    report=dict(stage='solver',status=solver.status_name(status),setup_elapsed=setup,
                solver_wall_time=solver.wall_time,elapsed=time.monotonic()-START,
                source_pairs=len(pairs),branches=solver.num_branches,conflicts=solver.num_conflicts)
    if status in(cp_model.OPTIMAL,cp_model.FEASIBLE):
        chosen=next(pair for pair,z in zip(pairs,p) if solver.value(z))
        ids=[i for i,z in zip(row_ids,x) if solver.value(z)]
        ids += [i for a in chosen['aggregates'] for i in data['aggregates'][a]['candidate_ids']]
        assert len(ids)==28 and len(set(ids))==28
        selected=[candidates[i] for i in ids]
        report['replay']=replay(selected); report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)


if __name__=='__main__': {'catalogue':catalogue,'solve':solve}[sys.argv[1]]()
