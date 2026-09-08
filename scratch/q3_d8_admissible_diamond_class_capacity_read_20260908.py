"""One <=3s read of saved physical diamond bundles; no enumeration."""
import os,json,time,resource
from functools import reduce
from operator import xor
from collections import Counter,defaultdict
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
PATH='/tmp/Q3_D8_AFFINE_DIAMOND_COMPLEMENT_STRUCTURAL_CATALOGUE_20260908_ternarylift.json'
with open(PATH) as f:data=json.load(f)
P=[3**i for i in range(8)];classes={};W_ids=[]
for t,code in enumerate(data['reps']):
    x=[(code//p)%3 for p in P]
    if x.count(2)==1 and x.count(1)==3:
        support=[i for i,v in enumerate(x) if v]
        if reduce(xor,support,0)==0:W_ids.append(t)
    if t not in data['critical']:continue
    O=[i for i,v in enumerate(x) if v==1];b=reduce(xor,O,0)
    T=[i^b for i,v in enumerate(x) if v==2]
    if len(O)==7:cl='A'
    elif len(O)==5:cl='B'
    elif len(O)==3:cl='C' if x[b]==2 else 'D'
    else:cl='E' if reduce(xor,T,0)==0 else 'F'
    classes[t]=cl
assert len(W_ids)==7
pred={
    (8,(('D',3),('E',1),('F',2))):('V',1),
    (8,(('A',1),('B',3),('D',2))):('W',0),
    (16,(('B',3),('C',3),('D',5),('F',1))):('U',1),
}
groups=defaultdict(lambda:dict(count=0,capacity=Counter(),productive=Counter(),examples=[]))
violations=[];double_end_count=0;generic_count=0
for i,r in enumerate(data['records']):
    if not r['admissible']:continue
    pattern=tuple(sorted(Counter(classes[t] for t in r['critical7']).items()))
    key=(r['row_count'],pattern);g=groups[key];g['count']+=1
    capacity=sum(t in r['cover'] for t in W_ids)
    productive=sum(c['C'][0] in c['C'][1:3] for c in r['components'])
    g['capacity'][capacity]+=1;g['productive'][productive]+=1
    if len(g['examples'])<1:g['examples'].append(dict(record_id=i,H=r['H'],v=r['v'],components=r['components']))
    if key not in pred or capacity!=pred[key][1] or productive!=pred[key][1]:
        violations.append(dict(record_id=i,row_count=r['row_count'],pattern=dict(pattern),W_count=capacity,productive=productive))
    if r['row_count']==16:
        generic_count+=1;w=r['components'][0]['C'];ab=tuple(sorted((w[0],w[-1])))
        edges=[tuple(sorted(w[j:j+2])) for j in (1,3,5)]
        good=(w[0]!=w[-1] and len(set(edges))==2 and
              ((edges[0]==ab and edges[1]==edges[2]) or(edges[2]==ab and edges[0]==edges[1])))
        double_end_count+=good
        if not good:violations.append(dict(record_id=i,wrong_generic_graph=True))
assert sum(g['count'] for g in groups.values())==1176
report=dict(elapsed=time.monotonic()-START,admissible_bundles=1176,rank5_W_orbit_ids=W_ids,
            groups=[dict(name=pred.get(k,('UNEXPECTED',None))[0],row_count=k[0],pattern=dict(k[1]),count=g['count'],
                         actual_W_count_distribution=dict(g['capacity']),productive_constituent_distribution=dict(g['productive']),examples=g['examples'])
                    for k,g in groups.items()],
            generic_count=generic_count,generic_double_edge_ab_outer_count=double_end_count,violations=violations)
report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
