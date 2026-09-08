"""One bounded h100-only translation-orbit catalogue and CP-SAT attempt."""
import os
import sys
import time
import json
import resource
from itertools import product, permutations
from collections import Counter

os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (3 * 1024**3, 3 * 1024**3))
START = time.monotonic()
CAT = '/tmp/Q3_D8_TRANSLATION_ORBIT_CATALOGUE_20260908_ternarylift.json'
WITNESS = '/tmp/Q3_D8_TRANSLATION_ORBIT_WITNESS_20260908_ternarylift.json'
POW = [3**i for i in range(8)]


def encode(x):
    return sum(a*b for a, b in zip(x, POW))


def chain(word, shift=0):
    x = [0]*8
    out = [tuple(x)]
    for a in word:
        x[a ^ shift] += 1
        out.append(tuple(x))
    return out


def catalogue():
    vectors = list(product(range(3), repeat=8))
    rep_by_code = [None]*6561
    rank_by_code = [None]*6561
    for x in vectors:
        c = encode(x)
        if rep_by_code[c] is not None:
            continue
        codes = {sum(x[i ^ g]*POW[i] for i in range(8)) for g in range(8)}
        r = min(codes)
        for d in codes:
            rep_by_code[d] = r
            rank_by_code[d] = sum(x)
    reps = sorted(set(rep_by_code))
    rid = {r:i for i,r in enumerate(reps)}
    orbit_id = [rid[r] for r in rep_by_code]
    ranks = [rank_by_code[r] for r in reps]
    sizes = [0]*len(reps)
    for t in orbit_id:
        sizes[t] += 1
    critical = [i for i,r in enumerate(ranks) if r == 7]
    assert len(reps) == 891 and len(critical) == 127
    assert all(sizes[i] == 8 for i in critical)

    candidates = []
    stats = Counter()
    distinct = set()
    for normal in range(1,8):
        H = [a for a in range(8) if (a & normal).bit_count() % 2 == 0]
        outside = [v for v in range(8) if v not in H]
        words = []
        for h in H:
            halves = permutations(H) if h == 0 else product(H, repeat=4)
            for half in halves:
                if half[0] != 0:
                    continue
                w = tuple(half) + tuple(a ^ h for a in reversed(half))
                if any(w.count(a) != 2 for a in H):
                    continue
                words.append((w,h))
        assert len(words) == 78 and len(set(w for w,h in words)) == 78
        for v in outside:
            for w,h in words:
                C, D = chain(w), chain(w, v)
                assert all(tuple(2*(i in H)-C[8-j][i] for i in range(8)) == chain(w,h)[j]
                           for j in range(9))
                for mode in ('short','full'):
                    if mode == 'full' and w[0] != w[1]:
                        continue
                    stats[mode+'_generated'] += 1
                    cs = C[1:8] if mode == 'short' else C
                    ds = D[1:8] if mode == 'short' else D
                    coverage = sorted({orbit_id[encode(a)+encode(b)] for a in cs for b in ds})
                    crit = [i for i in coverage if ranks[i] == 7]
                    wanted = 3 if mode == 'short' else 4
                    if len(crit) != wanted:
                        stats[mode+'_critical_collision'] += 1
                        continue
                    key = (mode, tuple(H), v, w)
                    assert key not in distinct
                    distinct.add(key)
                    stats[mode+'_admissible'] += 1
                    candidates.append(dict(mode=mode, H=H, v=v, h=h,
                                           word=w, cover=coverage, critical=crit))
    assert stats['short_generated'] == 2184 and stats['full_generated'] == 336
    eligible = set(i for c in candidates for i in c['cover'])
    covered_critical = set(i for c in candidates for i in c['critical'])
    incidence = Counter(i for c in candidates for i in c['cover'])
    report = dict(stage='catalogue', elapsed=time.monotonic()-START,
                  target_orbits=len(reps), rank7_orbits=len(critical),
                  stats=dict(stats), eligible_orbits=len(eligible),
                  covered_rank7_orbits=len(covered_critical),
                  missing_orbits=[dict(id=i,code=reps[i],rank=ranks[i],size=sizes[i])
                                  for i in range(len(reps)) if i not in eligible],
                  minimum_target_incidence=min(incidence.values(),default=0),
                  cache=CAT)
    with open(CAT,'w') as f:
        json.dump(dict(reps=reps, ranks=ranks, sizes=sizes, candidates=candidates,
                       critical=critical, report=report),f)
    report['elapsed'] = time.monotonic()-START
    print(json.dumps(report),flush=True)


def replay(selected):
    rows = set()
    for c in selected:
        for g in range(8):
            C, D = chain(c['word'],g), chain(c['word'],g ^ c['v'])
            if c['mode'] == 'short':
                C,D = C[1:8],D[1:8]
            rows.add(tuple(sorted((tuple(C),tuple(D)))))
    loads = [0]*6561
    for C,D in rows:
        for shore in (C,D):
            for a,b in zip(shore,shore[1:]):
                assert all(x<=y for x,y in zip(a,b)) and a != b
            assert len({sum(x) for x in shore}) == len(shore)
        suppC = {i for x in C for i,v in enumerate(x) if v}
        suppD = {i for x in D for i,v in enumerate(x) if v}
        assert len(suppC)==len(suppD)==4 and suppC.isdisjoint(suppD)
        for a in C:
            for b in D:
                x = tuple(u+v for u,v in zip(a,b))
                assert all(0<=v<=2 for v in x)
                loads[encode(x)] += 1
    cost = sum(len(C)+len(D) for C,D in rows)
    assert len(rows)==168 and cost==2368 and min(loads)>=1
    critical_loads = []
    for x in product(range(3),repeat=8):
        if sum(x) in (7,9):
            assert loads[encode(x)] == 1
            critical_loads.append(loads[encode(x)])
    artifact = dict(selected=selected,rows=sorted(rows),loads=loads,cost=cost,
                    row_count=len(rows),minimum_load=min(loads),maximum_load=max(loads))
    with open(WITNESS,'w') as f:
        json.dump(artifact,f)
    return dict(cost=cost,row_count=len(rows),minimum_load=min(loads),
                maximum_load=max(loads),critical_target_count=len(critical_loads),
                witness=WITNESS)


def solve():
    with open(CAT) as f:
        data=json.load(f)
    if data['report']['missing_orbits']:
        print(json.dumps(dict(stage='solver',status='SKIPPED_MISSING_TARGETS')))
        return
    from ortools.sat.python import cp_model
    model=cp_model.CpModel()
    candidates=data['candidates']
    variables=[model.new_bool_var('x'+str(i)) for i in range(len(candidates))]
    by_target=[[] for _ in data['reps']]
    for c,x in zip(candidates,variables):
        for t in c['cover']:
            by_target[t].append(x)
    critical=set(data['critical'])
    for t,vars_ in enumerate(by_target):
        if t in critical:
            model.add(sum(vars_)==1)
        else:
            model.add(sum(vars_)>=1)
    model.add(sum(x for c,x in zip(candidates,variables) if c['mode']=='full')==1)
    model.add(sum(x for c,x in zip(candidates,variables) if c['mode']=='short')==41)
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
        assert len(selected)==42 and sum(c['mode']=='full' for c in selected)==1
        report['replay']=replay(selected)
        report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'catalogue':
        catalogue()
    elif sys.argv[1] == 'solve':
        solve()
    else:
        raise ValueError(sys.argv[1])
