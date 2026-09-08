"""One <=5s h100 structural catalogue of physical diamond bundles."""
import os,json,time,resource
from functools import reduce
from operator import xor
from collections import Counter
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
OUT='/tmp/Q3_D8_AFFINE_DIAMOND_COMPLEMENT_STRUCTURAL_CATALOGUE_20260908_ternarylift.json'
with open(BASE) as f:base=json.load(f)
P=[3**i for i in range(8)];oid=[None]*6561
for i,rep in enumerate(base['reps']):
    x=[(rep//p)%3 for p in P]
    for g in range(8):oid[sum(x[j^g]*P[j] for j in range(8))]=i
assert all(i is not None for i in oid)
critical=set(base['critical']);Cset=set()
for t in critical:
    x=[(base['reps'][t]//p)%3 for p in P]
    O=[i for i,v in enumerate(x) if v==1]
    if len(O)==3 and x[reduce(xor,O,0)]==2:Cset.add(t)
assert len(critical)==127 and len(Cset)==28
def partner(w):
    d=list(w)
    for i in (1,3,5):d[i],d[i+1]=d[i+1],d[i]
    return tuple(d)
def canonical(w):return min(tuple(w),partner(w))
def reflected(w):return canonical(tuple(a^w[-1] for a in reversed(w)))
counts=[1,2,2,2];prefix=[0];words=[]
def rec():
    if len(prefix)==8:
        words.append(tuple(prefix));return
    for a in range(4):
        if counts[a]:
            counts[a]-=1;prefix.append(a);rec();prefix.pop();counts[a]+=1
rec();assert len(words)==630
filtered=[w for w in words if w[1]!=w[2] and w[3]!=w[4] and w[5]!=w[6]]
assert len(filtered)==408
translation_reps=sorted({canonical(w) for w in filtered})
assert len(translation_reps)==204
assert all(reflected(reflected(w))==w for w in translation_reps)
abstract_bundles=[];visited=set()
for w in translation_reps:
    if w in visited:continue
    r=reflected(w);assert r in translation_reps
    comp=[w] if r==w else [w,r]
    visited.update(comp);abstract_bundles.append(comp)
assert len(visited)==204 and len(abstract_bundles)==117
assert sum(len(b)==1 for b in abstract_bundles)==30
def chain(w,H,shift=0):
    out=[0]
    for a in w:out.append(out[-1]+P[H[a]^shift])
    return out
records=[];stats=Counter();before_C=Counter();after_C=Counter();union7=set();union9=set()
first_C=None
for normal in range(1,8):
    H=[a for a in range(8) if (a&normal).bit_count()%2==0]
    for v in range(8):
        if v in H:continue
        for bundle in abstract_bundles:
            size=8*len(bundle);stats['generated_size'+str(size)]+=1
            critical7=[];critical9=[];cover=set();actual_words=[]
            for w in bundle:
                d=partner(w);C=chain(w,H);D=chain(d,H,v)
                c7=[oid[C[i]+D[7-i]] for i in range(1,7)]
                c9=[oid[C[i]+D[9-i]] for i in range(2,8)]
                assert len(set(c7))==len(set(c9))==6
                critical7+=c7;critical9+=c9
                cover.update(oid[a+b] for a in C[1:8] for b in D[1:8])
                actual_words.append(dict(C=[H[a] for a in w],D=[H[a] for a in d]))
            Ccount=len(set(critical7)&Cset);before_C[(size,Ccount)]+=1
            admitted=len(set(critical7))==6*len(bundle)
            assert admitted==(len(set(critical9))==6*len(bundle))
            record=dict(H=H,v=v,row_count=size,components=actual_words,
                        critical7=critical7,critical9=critical9,cover=sorted(cover),
                        class_C_count=Ccount,admissible=admitted)
            records.append(record)
            if admitted:
                stats['admissible_size'+str(size)]+=1;after_C[(size,Ccount)]+=1
                union7.update(critical7);union9.update(critical9)
                if Ccount and first_C is None:first_C=record
            else:stats['rejected_size'+str(size)]+=1
assert len(records)==3276
assert stats['generated_size8']==840 and stats['generated_size16']==2436
assert all(r['class_C_count']==0 for r in records if r['row_count']==8)
cert=dict(records=records,reps=base['reps'],ranks=base['ranks'],sizes=base['sizes'],
          critical=base['critical'],class_C=sorted(Cset))
with open(OUT,'w') as f:json.dump(cert,f)
missing=sorted(critical-union7)
summary=dict(elapsed=time.monotonic()-START,physical_translation8_orbits=5712,
    complement_bundles=len(records),statistics=dict(stats),
    class_C_counts_before_filter=[dict(row_count=n,C_count=c,count=k) for (n,c),k in sorted(before_C.items())],
    class_C_counts_after_filter=[dict(row_count=n,C_count=c,count=k) for (n,c),k in sorted(after_C.items())],
    covered_rank7_orbits=len(union7),covered_rank9_orbits=len(union9),
    covered_class_C_orbits=len(union7&Cset),C_covering_admissible_bundle_exists=first_C is not None,
    first_C_covering_admissible_bundle=first_C,
    missing_rank7=[dict(id=t,code=base['reps'][t],target=[(base['reps'][t]//p)%3 for p in P]) for t in missing],
    certificate=OUT)
summary['elapsed']=time.monotonic()-START
print(json.dumps(summary),flush=True)
