"""One <=5s h100 exact-orbit catalogue plus <=3s fractional LP."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='2'
os.environ['MKL_NUM_THREADS']='1'
import json,time,resource,warnings
from itertools import permutations,combinations_with_replacement
from fractions import Fraction as F
from collections import Counter,defaultdict
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
OUT='/tmp/Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
P=[3**i for i in range(8)]
N=6561
S=(0,2,4,6,3,1,7,5)
T=(0,2,1,3,4,6,5,7)
generators=[tuple(i^d for i in range(8)) for d in (1,2,4)]+[S,T]
identity=tuple(range(8)); group=[identity]; seen={identity}; k=0
while k<len(group):
    a=group[k];k+=1
    for g in generators:
        b=tuple(g[i] for i in a)
        if b not in seen:seen.add(b);group.append(b)
assert len(group)==1344
vectors=[tuple((code//p)%3 for p in P) for code in range(N)]
parent=list(range(N))
def find(a):
    while parent[a]!=a:
        parent[a]=parent[parent[a]];a=parent[a]
    return a
def union(a,b):
    a,b=find(a),find(b)
    if a!=b:parent[b]=a
weights=[[P[g[i]] for i in range(8)] for g in generators]
for code,x in enumerate(vectors):
    for w in weights:union(code,sum(a*b for a,b in zip(x,w)))
components=defaultdict(list)
for code in range(N):components[find(code)].append(code)
orbits=sorted(components.values(),key=lambda a:a[0])
reps=[a[0] for a in orbits];sizes=[len(a) for a in orbits]
orbit_id=[None]*N
for i,orb in enumerate(orbits):
    for c in orb:orbit_id[c]=i
# Independent direct full-group orbit replay and Burnside count.
group_weights=[[P[g[i]] for i in range(8)] for g in group]
for rep,orb in zip(reps,orbits):
    x=vectors[rep]
    actual={sum(a*b for a,b in zip(x,w)) for w in group_weights}
    assert actual==set(orb)
burnside=0
for g in group:
    unseen=set(range(8));cycles=0
    while unseen:
        cycles+=1;a=next(iter(unseen))
        while a in unseen:unseen.remove(a);a=g[a]
    burnside+=3**cycles
assert burnside==1344*len(orbits)
histograms=[tuple(vectors[r].count(a) for a in range(3)) for r in reps]
hist_refinements=defaultdict(list)
for h,size in zip(histograms,sizes):hist_refinements[h].append(size)
assert len(hist_refinements)==45
assert sorted(hist_refinements[(4,0,4)])==[14,56]

def shore_words():
    counts=[1,2,2,2];prefix=[0]
    def rec():
        if len(prefix)==8:
            yield tuple(prefix);return
        for a in range(4):
            if counts[a]:
                counts[a]-=1;prefix.append(a)
                yield from rec()
                prefix.pop();counts[a]+=1
    yield from rec()
all_words=list(shore_words());assert len(all_words)==630
maps=[(0,)+p for p in permutations((1,2,3))]
words=sorted({min(tuple(m[a] for a in w) for m in maps) for w in all_words})
assert len(words)==105
# Independent first-occurrence-order generation/filter.
restricted=[]
for w in all_words:
    first=[]
    for a in w:
        if a not in first:first.append(a)
    if first==[0,1,2,3]:restricted.append(w)
assert set(restricted)==set(words) and len(restricted)==105
intervals=[list(range(9)),list(range(1,9)),list(range(8)),list(range(1,8))]
mode_pairs=list(combinations_with_replacement(range(4),2));assert len(mode_pairs)==10
columns=[];costs=[];rows=[]
for w in words:
    C=[0];D=[0]
    for a in w:C.append(C[-1]+P[a]);D.append(D[-1]+P[a^4])
    for m,n in mode_pairs:
        col=[0]*len(orbits)
        for i in intervals[m]:
            for j in intervals[n]:col[orbit_id[C[i]+D[j]]]+=1
        assert sum(col)==len(intervals[m])*len(intervals[n])
        columns.append(col);costs.append(len(intervals[m])+len(intervals[n]))
        rows.append(dict(word=w,modes=[m,n]))
assert len(columns)==1050
catalogue_report=dict(stage='catalogue',elapsed=time.monotonic()-START,
    group_order=len(group),target_orbits=len(orbits),histograms=len(hist_refinements),
    histogram_orbit_refinement_distribution=dict(Counter(map(len,hist_refinements.values()))),
    target_orbit_size_distribution=dict(Counter(sizes)),canonical_words=len(words),row_types=len(rows),
    all_target_orbits_individually_eligible=all(any(c[i] for c in columns) for i in range(len(orbits))),
    independent_group_orbit_and_burnside_checks=True,independent_word_type_check=True)
print(json.dumps(catalogue_report),flush=True)
from scipy.optimize import linprog,OptimizeWarning
import numpy as np
warnings.filterwarnings('ignore',category=OptimizeWarning)
A=np.array(columns,dtype=np.int64).T
lp_start=time.monotonic()
result=linprog(np.array(costs,dtype=float),A_ub=-A,b_ub=-np.array(sizes,dtype=float),
               bounds=(0,None),method='highs',options={'time_limit':3.0,'threads':2})
report=dict(stage='lp',status=int(result.status),message=result.message,
            lp_elapsed=time.monotonic()-lp_start,elapsed=time.monotonic()-START)
certificate=dict(catalogue=catalogue_report,reps=reps,orbit_sizes=sizes,histograms=histograms,
                 rows=rows,costs=costs,columns=columns,lp_report=report)
if result.success:
    primal={i:F(float(x)).limit_denominator(1000000) for i,x in enumerate(result.x) if x>1e-8}
    dual={i:F(float(-x)).limit_denominator(1000000) for i,x in enumerate(result.ineqlin.marginals) if -x>1e-8}
    primal_cover=[sum(columns[j][i]*x for j,x in primal.items()) for i in range(len(orbits))]
    dual_load=[sum(col[i]*x for i,x in dual.items()) for col in columns]
    pscale=max([F(1)]+[F(sizes[i],1)/value for i,value in enumerate(primal_cover)])
    dscale=min([F(1)]+[F(costs[j],1)/value for j,value in enumerate(dual_load) if value])
    if pscale!=1:primal={j:x*pscale for j,x in primal.items()}
    if dscale!=1:dual={i:x*dscale for i,x in dual.items()}
    assert all(sum(columns[j][i]*x for j,x in primal.items())>=sizes[i] for i in range(len(orbits)))
    assert all(sum(col[i]*x for i,x in dual.items())<=costs[j] for j,col in enumerate(columns))
    upper=sum(costs[j]*x for j,x in primal.items());lower=sum(sizes[i]*x for i,x in dual.items())
    assert lower<=upper
    report.update(numeric_objective=float(result.fun),exact_lower=str(lower),exact_upper=str(upper),
                  exact_optimum=lower==upper,primal_scale=str(pscale),dual_scale=str(dscale),
                  primal_nonzeros=len(primal),dual_nonzeros=len(dual),
                  margin_above_lower_to_gate=str(F(76545,32)-lower),
                  margin_above_upper_to_gate=str(F(76545,32)-upper),
                  exact_primal_and_dual_checks=True)
    certificate.update(primal={str(i):str(x) for i,x in primal.items()},
                       dual={str(i):str(x) for i,x in dual.items()},exact_lower=str(lower),exact_upper=str(upper))
report['elapsed']=time.monotonic()-START
with open(OUT,'w') as f:json.dump(certificate,f)
report['certificate']=OUT;report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
