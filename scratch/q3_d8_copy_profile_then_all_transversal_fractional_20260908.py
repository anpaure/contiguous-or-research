"""One <=5s h100 process: small S8 gate, conditional full AGL gate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='2';os.environ['MKL_NUM_THREADS']='1'
import json,time,resource,warnings
from fractions import Fraction as F
from itertools import combinations_with_replacement,combinations
from math import factorial
from collections import Counter
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic();GATE=F(76545,32)
BASE='/tmp/Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
S8OUT='/tmp/Q3_D8_S8_COPY_PROFILE_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
AGLOUT='/tmp/Q3_D8_ALL_TRANSLATION_TRANSVERSAL_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
with open(BASE) as f:base=json.load(f)
words=[tuple(base['rows'][i]['word']) for i in range(0,1050,10)]
assert len(set(words))==105
intervals=[list(range(9)),list(range(1,9)),list(range(8)),list(range(1,8))]
modes=list(combinations_with_replacement(range(4),2));assert len(modes)==10
profiles=[]
def dyck(opened,closed,heights):
    if closed==4:profiles.append(tuple(heights));return
    if opened<4:dyck(opened+1,closed,heights+[opened+1-closed])
    if closed<opened:dyck(opened,closed+1,heights+[opened-closed-1])
dyck(0,0,[0]);assert len(profiles)==14
actual_profiles={}
for word in words:
    x=[0]*4;heights=[0]
    for a in word:x[a]+=1;heights.append(x.count(1))
    actual_profiles.setdefault(tuple(heights),word)
assert set(actual_profiles)==set(profiles)
hists=[(a,b,8-a-b) for a in range(9) for b in range(9-a)]
assert len(hists)==45
hid={h:i for i,h in enumerate(hists)}
demands=[factorial(8)//(factorial(a)*factorial(b)*factorial(c)) for a,b,c in hists]
assert sum(demands)==6561
cols=[];costs=[];rows=[]
for k,heights in enumerate(profiles):
    shore=[(4-(r+h)//2,h,(r-h)//2) for r,h in enumerate(heights)]
    for m,n in modes:
        col=[0]*45
        for i in intervals[m]:
            for j in intervals[n]:
                col[hid[tuple(a+b for a,b in zip(shore[i],shore[j]))]]+=1
        assert sum(col)==len(intervals[m])*len(intervals[n])
        cols.append(col);costs.append(len(intervals[m])+len(intervals[n]))
        rows.append(dict(profile=k,heights=heights,word=actual_profiles[heights],modes=[m,n]))
assert len(cols)==140
print(json.dumps(dict(stage='S8_catalogue',elapsed=time.monotonic()-START,
                     profiles=14,row_types=140,target_histograms=45,
                     independent_physical_profile_check=True)),flush=True)
from scipy.optimize import linprog,OptimizeWarning
import numpy as np
warnings.filterwarnings('ignore',category=OptimizeWarning)


def solve(stage,columns,costs,demands,rowmeta,targetmeta,limit,outpath):
    then=time.monotonic()
    A=np.array(columns,dtype=np.int64).T
    res=linprog(np.array(costs,dtype=float),A_ub=-A,b_ub=-np.array(demands,dtype=float),
                bounds=(0,None),method='highs',options={'time_limit':limit,'threads':2})
    report=dict(stage=stage,status=int(res.status),message=res.message,
                lp_elapsed=time.monotonic()-then,elapsed=time.monotonic()-START,
                row_types=len(columns),target_orbits=len(demands))
    cert=dict(rows=rowmeta,targets=targetmeta,demands=demands,costs=costs,columns=columns,report=report)
    upper=lower=None
    if res.success:
        p={i:F(float(x)).limit_denominator(1000000) for i,x in enumerate(res.x) if x>1e-8}
        y={i:F(float(-x)).limit_denominator(1000000) for i,x in enumerate(res.ineqlin.marginals) if -x>1e-8}
        pc=[sum(columns[j][i]*x for j,x in p.items()) for i in range(len(demands))]
        dl=[sum(c[i]*x for i,x in y.items()) for c in columns]
        ps=max([F(1)]+[F(d)/v for d,v in zip(demands,pc)])
        ds=min([F(1)]+[F(c)/v for c,v in zip(costs,dl) if v])
        p={i:x*ps for i,x in p.items()};y={i:x*ds for i,x in y.items()}
        assert all(sum(columns[j][i]*x for j,x in p.items())>=demands[i] for i in range(len(demands)))
        assert all(sum(c[i]*x for i,x in y.items())<=costs[j] for j,c in enumerate(columns))
        upper=sum(costs[i]*x for i,x in p.items());lower=sum(demands[i]*x for i,x in y.items())
        assert lower<=upper
        report.update(numeric_objective=float(res.fun),exact_lower=str(lower),exact_upper=str(upper),
                      exact_optimum=lower==upper,primal_scale=str(ps),dual_scale=str(ds),
                      primal_nonzeros=len(p),dual_nonzeros=len(y),
                      margin_lower_to_gate=str(GATE-lower),margin_upper_to_gate=str(GATE-upper),
                      exact_primal_dual_checks=True)
        cert.update(primal={str(i):str(x) for i,x in p.items()},dual={str(i):str(x) for i,x in y.items()})
    with open(outpath,'w') as f:json.dump(cert,f)
    report['certificate']=outpath;report['elapsed']=time.monotonic()-START
    print(json.dumps(report),flush=True)
    return lower,upper


lower,upper=solve('S8_profile_LP',cols,costs,demands,rows,hists,1.0,S8OUT)
if lower is None or lower>GATE or upper>GATE:
    print(json.dumps(dict(stage='decision',AGL_expansion_run=False,
                         reason='global_copy_family_gate_closed' if lower is not None and lower>GATE else 'first_stage_not_certified_below_gate',
                         elapsed=time.monotonic()-START)),flush=True)
    raise SystemExit(0)

# The first stage left room. Generate the complete affine group only now.
S=(0,2,4,6,3,1,7,5);T=(0,2,1,3,4,6,5,7)
gens=[tuple(i^d for i in range(8)) for d in (1,2,4)]+[S,T]
identity=tuple(range(8));group=[identity];seen={identity};k=0
while k<len(group):
    a=group[k];k+=1
    for g in gens:
        b=tuple(g[i] for i in a)
        if b not in seen:seen.add(b);group.append(b)
assert len(group)==1344
P=[3**i for i in range(8)];orbit_id=[None]*6561
for i,rep in enumerate(base['reps']):
    x=[(rep//p)%3 for p in P]
    orb={sum(x[j]*P[g[j]] for j in range(8)) for g in group}
    assert len(orb)==base['orbit_sizes'][i]
    for c in orb:
        assert orbit_id[c] in(None,i);orbit_id[c]=i
assert all(i is not None for i in orbit_id)
HA={0,1,2,3};HN={0,1,2,4}
imagesA={tuple(sorted(g[i] for i in HA)) for g in group}
imagesN={tuple(sorted(g[i] for i in HN)) for g in group}
assert len(imagesA)==14 and len(imagesN)==56 and not(imagesA&imagesN)
assert imagesA|imagesN==set(combinations(range(8),4))
for shore in combinations(range(8),4):
    A=set(shore);partners=[v for v in range(1,8) if {a^v for a in A}==set(range(8))-A]
    if tuple(shore) in imagesA:assert len(partners)==4
    else:
        v=0
        for a in A:v^=a
        assert partners==[v]
stabilizer=[g for g in group if {g[i] for i in HN}==HN]
assert len(stabilizer)==24 and len({tuple(g[i] for i in sorted(HN)) for g in stabilizer})==24
assert sum(g[0]==0 for g in stabilizer)==6
newcols=list(base['columns']);newcosts=list(base['costs'])
newrows=[dict(c,shore_type='affine',axes=[0,1,2,3],partner=4) for c in base['rows']]
axes=[0,1,2,4]
for word in words:
    C=[0];D=[0]
    physical=[axes[a] for a in word]
    for a in physical:C.append(C[-1]+P[a]);D.append(D[-1]+P[a^7])
    for m,n in modes:
        col=[0]*60
        for i in intervals[m]:
            for j in intervals[n]:col[orbit_id[C[i]+D[j]]]+=1
        assert sum(col)==len(intervals[m])*len(intervals[n])
        newcols.append(col);newcosts.append(len(intervals[m])+len(intervals[n]))
        newrows.append(dict(word=physical,modes=[m,n],shore_type='nonaffine',axes=axes,partner=7))
assert len(newcols)==2100
print(json.dumps(dict(stage='all_transversal_catalogue',elapsed=time.monotonic()-START,
    group_order=1344,target_orbits=60,row_types=2100,affine_shores=14,nonaffine_shores=56,
    nonaffine_S4_normalization_checked=True,all_translation_partners_checked=True)),flush=True)
solve('all_transversal_AGL_LP',newcols,newcosts,base['orbit_sizes'],newrows,
      [dict(rep=r,histogram=h) for r,h in zip(base['reps'],base['histograms'])],2.0,AGLOUT)
