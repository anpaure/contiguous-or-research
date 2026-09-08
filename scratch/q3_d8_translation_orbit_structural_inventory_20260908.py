"""One <=3s h100 structural inventory; no optimization."""
import os
import json
import time
import resource
from collections import Counter,defaultdict

os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
PATH='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
with open(PATH) as f:
    data=json.load(f)
critical=data['critical']
pos={t:i for i,t in enumerate(critical)}
short=[c for c in data['candidates'] if c['mode']=='short']
selfs=[c for c in short if c['row_count']==4]
generic=[c for c in short if c['row_count']==8]
self_vertices=set(t for c in selfs for t in c['critical'])
missing=set(critical)-self_vertices
assert len(self_vertices)==99 and len(missing)==28


def mask(ts):
    return sum(1<<pos[t] for t in ts)


def reduce(x,basis):
    while x:
        p=x.bit_length()-1
        if p not in basis:
            return x
        x^=basis[p]
    return 0


def make_basis(rows):
    basis={}
    for row in rows:
        x=reduce(row,basis)
        if x:
            basis[x.bit_length()-1]=x
    return basis


def kernel(basis,used):
    answer=[]
    for f in used:
        if f in basis:
            continue
        x=1<<f
        for p in sorted(basis):
            if (basis[p]&x).bit_count()%2:
                x^=1<<p
        assert all((row&x).bit_count()%2==0 for row in basis.values())
        answer.append([critical[i] for i in used if (x>>i)&1])
    return answer


directions={}
ones_distribution=Counter()
for t in critical:
    code=data['reps'][t]
    x=[(code//(3**i))%3 for i in range(8)]
    ds=[]
    for d in range(1,8):
        sums=sorted(x[i]+x[i^d] for i in range(8) if i<(i^d))
        if sums==[1,2,2,2]:
            ds.append(d)
    directions[t]=set(ds)
    ones_distribution[(x.count(1),len(ds))]+=1
    assert bool(ds)==(t in self_vertices)
    if x.count(1)==3:
        A=[i for i,a in enumerate(x) if a==2]
        Z=[i for i,a in enumerate(x) if a==0]
        zero_diffs={a^b for a in Z for b in Z if a!=b}
        assert bool(ds)==((A[0]^A[1]) in zero_diffs)

per_direction=defaultdict(set)
common_dir_counts=Counter()
for c in selfs:
    ds=set.intersection(*(directions[t] for t in c['critical']))
    d=c['word'][-1]^c['v']
    assert d in ds
    common_dir_counts[len(ds)]+=1
    per_direction[d].add(tuple(c['critical']))
triples=set(tuple(c['critical']) for c in selfs)
sixes=set(tuple(c['critical']) for c in generic)
self_basis=make_basis(mask(e) for e in triples)
all_basis=make_basis(mask(c['critical']) for c in short)
missing_mask=mask(missing)
generic_missing_basis=make_basis(mask(c['critical'])&missing_mask for c in generic)
full_reps={(0,0,2,2,3,3,1,1),(0,0,2,3,2,3,1,1)}
full_tests=[]
all_mask=(1<<len(critical))-1
for c in data['candidates']:
    if c['mode']=='full' and c['H']==[0,1,2,3] and c['v']==4 and tuple(c['word']) in full_reps:
        full_tests.append(dict(word=c['word'],rhs_in_all_short_span=not reduce(all_mask^mask(c['critical']),all_basis)))
result=dict(
    elapsed=time.monotonic()-START,
    self_candidate_count=len(selfs),generic_candidate_count=len(generic),
    distinct_self_triples=len(triples),distinct_generic_sixes=len(sixes),
    generic_candidate_missing_vertex_distribution=dict(sorted(Counter(len(set(c['critical'])&missing) for c in generic).items())),
    generic_distinct_six_missing_vertex_distribution=dict(sorted(Counter(len(set(e)&missing) for e in sixes).items())),
    generic_missing_patterns=len({tuple(sorted(set(e)&missing)) for e in sixes}),
    self_vertex_count=len(self_vertices),missing_vertex_count=len(missing),
    self_GF2_rank_on_99=len(self_basis),self_GF2_rank_on_127=len(self_basis),
    all_short_GF2_rank_on_127=len(all_basis),
    generic_missing_GF2_rank_on_28=len(generic_missing_basis),
    missing_all_ones_in_generic_missing_span=not reduce(missing_mask,generic_missing_basis),
    canonical_full_GF2_tests=full_tests,
    self_nullspace_on_99=kernel(self_basis,sorted(pos[t] for t in self_vertices)),
    common_direction_count_per_self_candidate=dict(sorted(common_dir_counts.items())),
    direction_inventory=[dict(direction=d,vertices=sum(d in directions[t] for t in critical),
                              distinct_triples=len(per_direction[d]),
                              GF2_rank=len(make_basis(mask(e) for e in per_direction[d])))
                         for d in range(1,8)],
    ones_direction_distribution=[dict(ones=o,directions=k,count=n) for (o,k),n in sorted(ones_distribution.items())]
)
result['elapsed']=time.monotonic()-START
print(json.dumps(result),flush=True)
