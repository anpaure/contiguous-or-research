"""One <=1s existing-matrix GF(2) read; no optimization."""
import os,json,time,resource
from functools import reduce
from operator import xor
from collections import Counter
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
with open('/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json') as f:
    data=json.load(f)
critical=data['critical']; pos={t:i for i,t in enumerate(critical)}
meta={}
for t in critical:
    code=data['reps'][t]; x=[(code//(3**i))%3 for i in range(8)]
    O=[i for i,v in enumerate(x) if v==1]; b=reduce(xor,O,0)
    T=[i^b for i,v in enumerate(x) if v==2]
    if len(O)==7: cls='A'
    elif len(O)==5: cls='B'
    elif len(O)==3: cls='C' if x[b]==2 else 'D'
    else: cls='E' if reduce(xor,T,0)==0 else 'F'
    meta[t]=dict(cls=cls,direction=reduce(xor,T,0) if cls=='F' else None)
def mask(ts): return sum(1<<pos[t] for t in ts)
def basis(rows):
    out={}
    for z in rows:
        while z and z.bit_length()-1 in out: z^=out[z.bit_length()-1]
        if z: out[z.bit_length()-1]=z
    return out
def kernel(B,used):
    out=[]
    for f in used:
        if f in B: continue
        z=1<<f
        for p in sorted(B):
            if (B[p]&z).bit_count()%2: z^=1<<p
        assert all((z&r).bit_count()%2==0 for r in B.values())
        out.append(z)
    return out
short=[c for c in data['candidates'] if c['mode']=='short']
selfs=[c for c in short if c['row_count']==4]
rows=[mask(c['critical']) for c in short]; selfrows=[mask(c['critical']) for c in selfs]
B=basis(rows); SB=basis(selfrows)
K=kernel(B,range(127)); assert len(K)==1
z=K[0]; support=[t for t in critical if (z>>pos[t])&1]
checks={}
ab=mask(t for t in critical if meta[t]['cls'] in ('A','B'))
checks['A_union_B']=all((ab&r).bit_count()%2==0 for r in selfrows)
for d in range(1,8):
    fd=mask(t for t in critical if meta[t]['cls']=='F' and meta[t]['direction']==d)
    checks['F_direction_'+str(d)]=all((fd&r).bit_count()%2==0 for r in selfrows)
SK=kernel(SB,sorted(pos[t] for t in {t for c in selfs for t in c['critical']}))
out=dict(elapsed=time.monotonic()-START,all_short_rank=len(B),self_rank=len(SB),
         class_sizes=dict(Counter(m['cls'] for m in meta.values())),
         global_nullvector_hex=hex(z),global_nullvector_target_ids=support,
         global_nullvector_class_counts=dict(Counter(meta[t]['cls'] for t in support)),
         proposed_self_relation_checks=checks,
         extracted_self_relations=[dict(weight=k.bit_count(),
             classes=dict(Counter(meta[t]['cls'] for t in critical if (k>>pos[t])&1)),
             F_directions=dict(Counter(meta[t]['direction'] for t in critical if (k>>pos[t])&1 and meta[t]['cls']=='F')))
             for k in SK])
out['elapsed']=time.monotonic()-START
print(json.dumps(out),flush=True)
