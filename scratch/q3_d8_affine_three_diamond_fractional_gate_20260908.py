"""One <=5s h100 LP adding affine three-diamond chain pairs."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='2';os.environ['MKL_NUM_THREADS']='1'
import json,time,resource,warnings
from fractions import Fraction as F
from collections import Counter
from itertools import product
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_ALL_TRANSLATION_TRANSVERSAL_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
AFF='/tmp/Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
OUT='/tmp/Q3_D8_AFFINE_THREE_DIAMOND_FRACTIONAL_CERTIFICATE_20260908_ternarylift.json'
with open(BASE) as f:base=json.load(f)
with open(AFF) as f:aff=json.load(f)
P=[3**i for i in range(8)]
S=(0,2,4,6,3,1,7,5);T=(0,2,1,3,4,6,5,7)
gens=[tuple(i^d for i in range(8)) for d in (1,2,4)]+[S,T]
identity=tuple(range(8));group=[identity];seen={identity};k=0
while k<len(group):
    a=group[k];k+=1
    for g in gens:
        b=tuple(g[i] for i in a)
        if b not in seen:seen.add(b);group.append(b)
assert len(group)==1344
orbit_id=[None]*6561
for i,t in enumerate(base['targets']):
    x=[(t['rep']//p)%3 for p in P]
    orb={sum(x[j]*P[g[j]] for j in range(8)) for g in group}
    assert len(orb)==base['demands'][i]
    for c in orb:
        assert orbit_id[c] in(None,i);orbit_id[c]=i
assert all(i is not None for i in orbit_id)
trans_cache={}
def translation_rep(code):
    if code not in trans_cache:
        x=[(code//p)%3 for p in P]
        cs={sum(x[i^g]*P[i] for i in range(8)) for g in range(8)}
        r=min(cs)
        for c in cs:trans_cache[c]=r
    return trans_cache[code]
def chain(w,g=0):
    codes=[0];vectors=[(0,0,0,0)];x=[0]*4
    for a in w:
        codes.append(codes[-1]+P[a^g]);x[a]+=1;vectors.append(tuple(x))
    return codes,vectors
words=[tuple(aff['rows'][i]['word']) for i in range(0,1050,10)]
assert len(set(words))==105
eligible=[w for w in words if w[1]!=w[2] and w[3]!=w[4] and w[5]!=w[6]]
assert len(eligible)==68
intervals=[list(range(9)),list(range(1,9)),list(range(8)),list(range(1,8))]
columns=list(base['columns']);costs=list(base['costs']);rows=list(base['rows'])
statistics=Counter();pair_metadata=[]
for w in eligible:
    d=list(w)
    for i in (1,3,5):d[i],d[i+1]=d[i+1],d[i]
    d=tuple(d)
    C,Cv=chain(w);D0,Dv=chain(d);D,_=chain(d,4)
    assert all(Cv[r]==Dv[r] for r in (0,1,3,5,7,8))
    assert all(Cv[r]!=Dv[r] for r in (2,4,6))
    assert len({tuple(sorted((tuple(a^g for a in w),tuple(a^4^g for a in d)))) for g in range(8)})==8
    crit7=[translation_rep(C[i]+D[7-i]) for i in range(1,7)]
    crit9=[translation_rep(C[i]+D[9-i]) for i in range(2,8)]
    full7=[translation_rep(C[i]+D[7-i]) for i in range(8)]
    assert len(set(crit7))==6 and len(set(crit9))==6
    assert full7[0]==full7[-1] and full7[0] not in crit7
    assert sorted(Counter(full7).values())==[1,1,1,1,1,1,2]
    edges=[tuple(sorted(w[i:i+2])) for i in (1,3,5)]
    degrees=Counter(a for e in edges for a in e)
    assert all(degrees[a]==2-int(w[0]==a)-int(w[-1]==a) for a in range(4))
    if w[0]==w[-1]:
        kind='triangle';assert len(set(edges))==3
        assert sum(Cv[4]==(1,1,1,1) for _ in [0])+sum(Dv[4]==(1,1,1,1) for _ in [0])==1
    elif len(set(edges))==3:kind='Hamilton_path'
    else:kind='edge_plus_double'
    statistics[kind]+=1
    preserve=[];swap=[]
    for h in range(4):
        if tuple(reversed(w))==tuple(a^h for a in w) and tuple(reversed(d))==tuple(a^h for a in d):preserve.append(h)
        if tuple(reversed(w))==tuple(a^h for a in d) and tuple(reversed(d))==tuple(a^h for a in w):swap.append(h)
    assert not swap
    if preserve:
        assert preserve==[w[0]^w[-1]] and w[0]!=w[-1]
        statistics['self_complement_closed']+=1
        if w[0]==w[1] or d[0]==d[1]:statistics['closed_full_extremal_repair']+=1
    pair_metadata.append(dict(word=w,partner_word=d,graph_type=kind,complement_shift=preserve))
    for m,n in product(range(4),repeat=2):
        col=[0]*60
        for i in intervals[m]:
            for j in intervals[n]:col[orbit_id[C[i]+D[j]]]+=1
        assert sum(col)==len(intervals[m])*len(intervals[n])
        columns.append(col);costs.append(len(intervals[m])+len(intervals[n]))
        rows.append(dict(family='affine_three_diamond',word=w,partner_word=d,axes=[0,1,2,3],partner=4,modes=[m,n]))
assert len(columns)==3188
catalogue=dict(stage='catalogue',elapsed=time.monotonic()-START,
    existing_copy_columns=2100,normalized_diamond_pairs=len(eligible),ordered_modes=16,
    diamond_columns=len(eligible)*16,total_columns=len(columns),target_orbits=60,
    omitted_target_orbits=[i for i in range(60) if not any(c[i] for c in columns)],
    structural_statistics=dict(statistics),all_odd_even_state_checks=True,
    all_translation_critical_and_endpoint_checks=True)
print(json.dumps(catalogue),flush=True)
from scipy.optimize import linprog,OptimizeWarning
import numpy as np
warnings.filterwarnings('ignore',category=OptimizeWarning)
then=time.monotonic();A=np.array(columns,dtype=np.int64).T
res=linprog(np.array(costs,dtype=float),A_ub=-A,b_ub=-np.array(base['demands'],dtype=float),
            bounds=(0,None),method='highs',options={'time_limit':3.0,'threads':2})
report=dict(stage='LP',status=int(res.status),message=res.message,lp_elapsed=time.monotonic()-then,
            elapsed=time.monotonic()-START)
cert=dict(catalogue=catalogue,pair_metadata=pair_metadata,rows=rows,costs=costs,columns=columns,
          targets=base['targets'],demands=base['demands'],report=report)
if res.success:
    p={i:F(float(x)).limit_denominator(1000000) for i,x in enumerate(res.x) if x>1e-8}
    y={i:F(float(-x)).limit_denominator(1000000) for i,x in enumerate(res.ineqlin.marginals) if -x>1e-8}
    pc=[sum(columns[j][i]*x for j,x in p.items()) for i in range(60)]
    dl=[sum(c[i]*x for i,x in y.items()) for c in columns]
    ps=max([F(1)]+[F(d)/v for d,v in zip(base['demands'],pc)])
    ds=min([F(1)]+[F(c)/v for c,v in zip(costs,dl) if v])
    p={i:x*ps for i,x in p.items()};y={i:x*ds for i,x in y.items()}
    assert all(sum(columns[j][i]*x for j,x in p.items())>=base['demands'][i] for i in range(60))
    assert all(sum(c[i]*x for i,x in y.items())<=costs[j] for j,c in enumerate(columns))
    upper=sum(costs[i]*x for i,x in p.items());lower=sum(base['demands'][i]*x for i,x in y.items())
    assert lower<=upper
    report.update(numeric_objective=float(res.fun),exact_lower=str(lower),exact_upper=str(upper),
                  exact_optimum=lower==upper,primal_scale=str(ps),dual_scale=str(ds),
                  primal_nonzeros=len(p),dual_nonzeros=len(y),
                  margin_lower_to_gate=str(F(76545,32)-lower),margin_upper_to_gate=str(F(76545,32)-upper),
                  exact_primal_dual_checks=True)
    cert.update(primal={str(i):str(x) for i,x in p.items()},dual={str(i):str(x) for i,x in y.items()})
with open(OUT,'w') as f:json.dump(cert,f)
report['certificate']=OUT;report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
