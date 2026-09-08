"""One h100-only catalogue and solver attempt for relaxed orbit closure."""
import os
import sys
import time
import json
import resource
from itertools import product
from collections import Counter

os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_TRANSLATION_ORBIT_CATALOGUE_20260908_ternarylift.json'
CAT='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
WIT='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_WITNESS_20260908_ternarylift.json'
POW=[3**i for i in range(8)]


def encode(x):
    return sum(v*p for v,p in zip(x,POW))


def chain_codes(w,shift=0):
    out=[0]
    for a in w:
        out.append(out[-1]+POW[a ^ shift])
    return out


def chain_vectors(w,shift=0):
    x=[0]*8
    out=[tuple(x)]
    for a in w:
        x[a ^ shift]+=1
        out.append(tuple(x))
    return out


def words_on(H):
    counts={a:2 for a in H}
    counts[0]=1
    prefix=[0]
    def rec():
        if len(prefix)==8:
            yield tuple(prefix)
            return
        for a in H:
            if counts[a]:
                counts[a]-=1
                prefix.append(a)
                yield from rec()
                prefix.pop()
                counts[a]+=1
    yield from rec()


def catalogue():
    with open(BASE) as f:
        base=json.load(f)
    reps,ranks,sizes=base['reps'],base['ranks'],base['sizes']
    critical=base['critical']
    orbit_id=[None]*6561
    for i,c in enumerate(reps):
        x=[(c//p)%3 for p in POW]
        for g in range(8):
            orbit_id[sum(x[j ^ g]*POW[j] for j in range(8))]=i
    assert all(i is not None for i in orbit_id)
    stats=Counter()
    candidates=[]
    for normal in range(1,8):
        H=[a for a in range(8) if (a & normal).bit_count()%2==0]
        words=list(words_on(H))
        assert len(words)==630
        for v in range(8):
            if v in H:
                continue
            for w in words:
                reflected=tuple(a ^ w[-1] for a in reversed(w))
                if w>reflected:
                    continue
                orbit_words=[w] if w==reflected else [w,reflected]
                stats['short_generated']+=1
                row_count=4*len(orbit_words)
                stats['short_generated_size'+str(row_count)]+=1
                coverage=set()
                for z in orbit_words:
                    C,D=chain_codes(z),chain_codes(z,v)
                    coverage.update(orbit_id[a+b] for a in C[1:8] for b in D[1:8])
                crit=sorted(i for i in coverage if ranks[i]==7)
                if len(crit)!=3*len(orbit_words):
                    stats['short_critical_collision']+=1
                    continue
                stats['short_admissible']+=1
                stats['short_admissible_size'+str(row_count)]+=1
                candidates.append(dict(mode='short',H=H,v=v,word=w,
                                       words=orbit_words,row_count=row_count,
                                       cover=sorted(coverage),critical=crit))
    assert stats['short_generated']==9912
    for c in base['candidates']:
        if c['mode']=='full':
            c=dict(c)
            c['words']=[c['word']]
            c['row_count']=4
            candidates.append(c)
            stats['full_admissible']+=1
    assert stats['full_admissible']==336
    coverage=set(i for c in candidates for i in c['cover'])
    critcoverage=set(i for c in candidates for i in c['critical'])
    missing=[dict(id=i,code=reps[i],rank=ranks[i],size=sizes[i])
             for i in range(len(reps)) if i not in coverage]
    report=dict(stage='catalogue',elapsed=time.monotonic()-START,
                stats=dict(stats),target_orbits=len(reps),
                eligible_orbits=len(coverage),rank7_orbits=len(critical),
                covered_rank7_orbits=len(critcoverage),missing_orbits=missing,
                previous_missing_203_now_covered=orbit_id[203] in coverage,cache=CAT)
    with open(CAT,'w') as f:
        json.dump(dict(reps=reps,ranks=ranks,sizes=sizes,critical=critical,
                       candidates=candidates,report=report),f)
    report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)


def replay(selected):
    rows=set()
    for c in selected:
        for w in c['words']:
            for g in range(8):
                C,D=chain_vectors(w,g),chain_vectors(w,g ^ c['v'])
                if c['mode']=='short':
                    C,D=C[1:8],D[1:8]
                rows.add(tuple(sorted((tuple(C),tuple(D)))))
    loads=[0]*6561
    for C,D in rows:
        for S in (C,D):
            for a,b in zip(S,S[1:]):
                assert all(x<=y for x,y in zip(a,b)) and a!=b
            assert len({sum(x) for x in S})==len(S)
        suppC={i for x in C for i,v in enumerate(x) if v}
        suppD={i for x in D for i,v in enumerate(x) if v}
        assert len(suppC)==len(suppD)==4 and suppC.isdisjoint(suppD)
        for a in C:
            for b in D:
                x=tuple(u+v for u,v in zip(a,b))
                assert all(0<=v<=2 for v in x)
                loads[encode(x)]+=1
    cost=sum(len(C)+len(D) for C,D in rows)
    assert len(rows)==168 and cost==2368 and min(loads)>=1
    for x in product(range(3),repeat=8):
        if sum(x) in (7,9):
            assert loads[encode(x)]==1
    out=dict(selected=selected,rows=sorted(rows),loads=loads,cost=cost,
             row_count=len(rows),minimum_load=min(loads),maximum_load=max(loads))
    with open(WIT,'w') as f:
        json.dump(out,f)
    return dict(cost=cost,row_count=len(rows),minimum_load=min(loads),
                maximum_load=max(loads),witness=WIT)


def solve():
    with open(CAT) as f:
        data=json.load(f)
    if data['report']['missing_orbits']:
        print(json.dumps(dict(stage='solver',status='SKIPPED_MISSING_TARGETS')))
        return
    from ortools.sat.python import cp_model
    full_reps={(0,0,2,2,3,3,1,1),(0,0,2,3,2,3,1,1)}
    candidates=[c for c in data['candidates'] if c['mode']=='short' or
                (c['H']==[0,1,2,3] and c['v']==4 and tuple(c['word']) in full_reps)]
    assert sum(c['mode']=='full' for c in candidates)==2
    model=cp_model.CpModel()
    variables=[model.new_bool_var('x'+str(i)) for i in range(len(candidates))]
    by_target=[[] for _ in data['reps']]
    for c,x in zip(candidates,variables):
        for t in c['cover']:
            by_target[t].append(x)
    critical=set(data['critical'])
    for t,vs in enumerate(by_target):
        model.add(sum(vs)==1) if t in critical else model.add(sum(vs)>=1)
    model.add(sum(x for c,x in zip(candidates,variables) if c['mode']=='full')==1)
    model.add(sum(c['row_count']*x for c,x in zip(candidates,variables)
                  if c['mode']=='short')==164)
    solver=cp_model.CpSolver()
    solver.parameters.max_time_in_seconds=18.0
    solver.parameters.num_search_workers=2
    solver.parameters.random_seed=0
    solver.parameters.stop_after_first_solution=True
    setup_elapsed=time.monotonic()-START
    status=solver.solve(model)
    report=dict(stage='solver',status=solver.status_name(status),
                setup_elapsed=setup_elapsed,solver_wall_time=solver.wall_time,
                elapsed=time.monotonic()-START,candidates=len(candidates),
                branches=solver.num_branches,conflicts=solver.num_conflicts)
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        selected=[c for c,x in zip(candidates,variables) if solver.value(x)]
        assert sum(c['row_count'] for c in selected)==168
        assert sum(c['mode']=='full' for c in selected)==1
        report['replay']=replay(selected)
        report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)


if __name__=='__main__':
    {'catalogue':catalogue,'solve':solve}[sys.argv[1]]()
