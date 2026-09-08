"""One <=1s read of existing 3024 generic candidates; no search."""
import os,json,time,resource
from functools import reduce
from operator import xor
from collections import Counter,defaultdict
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
with open('/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json') as f:
    data=json.load(f)
P=[3**i for i in range(8)]; rid={r:i for i,r in enumerate(data['reps'])}
classes={}
for t in data['critical']:
    x=[(data['reps'][t]//p)%3 for p in P]
    O=[i for i,v in enumerate(x) if v==1]; b=reduce(xor,O,0)
    T=[i^b for i,v in enumerate(x) if v==2]
    if len(O)==7: cl='A'
    elif len(O)==5: cl='B'
    elif len(O)==3: cl='C' if x[b]==2 else 'D'
    else: cl='E' if reduce(xor,T,0)==0 else 'F'
    classes[t]=cl
X_ids=[]
for normal in range(1,8):
    H=[i for i in range(8) if (i&normal).bit_count()%2==0]
    x=[2 if i==0 else int(i in H) for i in range(8)]
    rep=min(sum(x[i^g]*P[i] for i in range(8)) for g in range(8))
    X_ids.append(rid[rep])
assert len(set(X_ids))==7
predictions={
    (('B',2),('C',1),('D',3)):('BB',1),
    (('C',1),('D',3),('F',2)):('FF',1),
    (('B',1),('C',1),('D',3),('F',1)):('BF',0),
    (('C',2),('D',4)):('X',2),
    (('B',1),('C',2),('D',2),('F',1)):('Y',0),
}
groups=defaultdict(lambda:dict(count=0,DR=Counter(),actual_X=Counter(),examples=[]))
violations=[]; all_generic=0
for i,c in enumerate(data['candidates']):
    if c['mode']!='short' or c['row_count']!=8: continue
    all_generic+=1
    pattern=tuple(sorted(Counter(classes[t] for t in c['critical']).items()))
    dr=sum(w[0]!=w[1] and w[2] in w[:2] for w in c['words'])
    actual=sum(t in c['cover'] for t in X_ids)
    g=groups[pattern];g['count']+=1;g['DR'][dr]+=1;g['actual_X'][actual]+=1
    if len(g['examples'])<1:
        g['examples'].append(dict(candidate_id=i,H=c['H'],v=c['v'],words=c['words'],X_ids=[t for t in X_ids if t in c['cover']]))
    if pattern not in predictions or dr!=predictions[pattern][1] or actual>dr:
        violations.append(dict(candidate_id=i,pattern=dict(pattern),DR=dr,actual_X=actual))
assert all_generic==3024
report=dict(elapsed=time.monotonic()-START,generic_candidates=all_generic,
    rank5_X_orbit_ids=X_ids,predicted_type_count=len(predictions),observed_type_count=len(groups),
    groups=[dict(name=predictions.get(p,('UNEXPECTED',None))[0],pattern=dict(p),count=g['count'],
                 DR_prefix_count_distribution=dict(g['DR']),actual_X_coverage_distribution=dict(g['actual_X']),examples=g['examples'])
            for p,g in groups.items()],violations=violations)
report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
