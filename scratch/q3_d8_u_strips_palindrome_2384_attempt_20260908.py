"""One h100-only 25s process: actual U strips + selected P4 upgrade.

No catalogue enumeration, one <=3s LP, then at most one <=18s CP-SAT.
All row and endpoint coverage is taken literally; replay expands 6561 points.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='2'
os.environ['MKL_NUM_THREADS']='1'
import json,time,resource,warnings
from collections import Counter
from functools import reduce
from operator import xor
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
DIAM='/tmp/Q3_D8_AFFINE_DIAMOND_COMPLEMENT_STRUCTURAL_CATALOGUE_20260908_ternarylift.json'
OUT='/tmp/Q3_D8_U_STRIPS_PALINDROME_2384_CERTIFICATE_20260908_ternarylift.json'
WIT='/tmp/Q3_D8_U_STRIPS_PALINDROME_2384_WITNESS_20260908_ternarylift.json'
with open(BASE) as f:base=json.load(f)
with open(DIAM) as f:diam=json.load(f)
assert diam['reps']==base['reps'] and diam['critical']==base['critical']
P=[3**i for i in range(8)]
reps=base['reps'];critical=set(base['critical']);oid=[None]*6561
for t,rep in enumerate(reps):
    x=[(rep//p)%3 for p in P]
    for g in range(8):oid[sum(x[j^g]*P[j] for j in range(8))]=t
assert len(reps)==891 and len(critical)==127 and all(t is not None for t in oid)
classes={};Wset=set()
for t,rep in enumerate(reps):
    x=[(rep//p)%3 for p in P]
    if x.count(2)==1 and x.count(1)==3 and reduce(xor,(i for i,v in enumerate(x) if v),0)==0:
        Wset.add(t)
    if t not in critical:continue
    ones=[i for i,v in enumerate(x) if v==1];b=reduce(xor,ones,0)
    twos=[i^b for i,v in enumerate(x) if v==2]
    classes[t]=('A' if len(ones)==7 else 'B' if len(ones)==5 else
                ('C' if x[b]==2 else 'D') if len(ones)==3 else
                'E' if reduce(xor,twos,0)==0 else 'F')
assert len(Wset)==7
EH=oid[P[0]+2*sum(P[i] for i in (1,2,3))]
WH=oid[2*P[0]+sum(P[i] for i in (1,2,3))]
assert classes[EH]=='E' and WH in Wset

def chain(w,g=0):
    out=[0]
    for a in w:out.append(out[-1]+P[a^g])
    return out

def diamond_key(c,d):
    direct=tuple(sorted((tuple(c),tuple(d))))
    h=c[-1]
    reflected=tuple(sorted((tuple(a^h for a in reversed(c)),tuple(a^h for a in reversed(d)))))
    return min(direct,reflected)

type_by_pattern={
    (('B',2),('C',1),('D',3)):'p',
    (('C',1),('D',3),('F',2)):'q',
    (('B',1),('C',1),('D',3),('F',1)):'r',
    (('C',2),('D',4)):'t',
    (('B',1),('C',2),('D',2),('F',1)):'z',
    (('B',3),('C',3),('D',5),('F',1)):'u',
    (('D',3),('E',1),('F',2)):'v',
    (('A',1),('B',3),('D',2)):'w',
}
candidates=[]
for i,c in enumerate(base['candidates']):
    if c['mode']!='short':continue
    candidates.append(dict(family='copy',source_id=i,row_count=c['row_count'],
                           critical=c['critical'],cover=c['cover'],source=c))
assert len(candidates)==5208
for i,c in enumerate(diam['records']):
    if not c['admissible']:continue
    candidates.append(dict(family='diamond',source_id=i,row_count=c['row_count'],
                           critical=c['critical7'],cover=c['cover'],source=c))
assert len(candidates)==6384
for c in candidates:
    pat=tuple(sorted(Counter(classes[t] for t in c['critical']).items()))
    c['type']='s' if c['family']=='copy' and c['row_count']==4 else type_by_pattern[pat]
    assert len(set(c['critical']))==3*c['row_count']//4
raw_count=len(candidates)
candidates=[c for c in candidates if EH not in c['critical']]
for i,c in enumerate(candidates):c['id']=i
nshort=len(candidates)

# Normalize the two relative orientations of the generic outer-ab diamonds.
literals=[([0,1,0,2,3,2,3,1],[0,0,1,3,2,3,2,1]),
          ([0,1,0,2,3,3,2,1],[0,0,1,3,2,2,3,1])]
repairs=[]
for cword,dword in literals:
    matches=[c for c in candidates if c['family']=='diamond' and c['type']=='u'
             and c['source']['H']==[0,1,2,3] and c['source']['v']==4
             and diamond_key(c['source']['components'][0]['C'],c['source']['components'][0]['D'])==diamond_key(cword,dword)]
    assert len(matches)==1
    # The restored zero lies on C; D starts with the repeated axis 0.
    assert dword[:2]==[0,0]
    D=chain(dword,4)
    extra=sorted({oid[a] for a in D[1:8]}|{oid[6560-a] for a in D[1:8]})
    assert set(extra)&critical=={EH} and set(extra)&Wset=={WH}
    repairs.append(dict(short_id=matches[0]['id'],C=cword,D=dword,H=[0,1,2,3],v=4,extra=extra))
assert len({r['short_id'] for r in repairs})==2

palindromes=[]
for c in candidates:
    s=c['source']
    if c['family']!='copy' or c['row_count']!=4 or s['word']!=list(reversed(s['word'])):continue
    if s['H']==[0,1,2,3]:continue
    C=chain(s['word']);D=chain(s['word'],s['v'])
    full={oid[a+b] for a in C for b in D}
    extra=sorted(full-set(c['cover']))
    EK=oid[P[0]+2*sum(P[i] for i in s['H'] if i)]
    WK=oid[2*P[0]+sum(P[i] for i in s['H'] if i)]
    assert EK!=EH and WK!=WH and set(extra)&critical=={EK} and set(extra)&Wset=={WK}
    assert oid[0] in extra and oid[6560] in extra
    palindromes.append(dict(short_id=c['id'],H=s['H'],v=s['v'],word=s['word'],extra=extra,EK=EK,WK=WK))
assert len(palindromes)==144

# Availability enlarges each source's possible completion: retain every short
# bundle disjoint from its forced U critical edge, and every eligible P upgrade.
availability=[]
for r in repairs:
    forced=candidates[r['short_id']];edge=set(forced['critical'])
    allowed={c['id'] for c in candidates if c['id']==forced['id'] or not edge.intersection(c['critical'])}
    pp=[p for p in palindromes if p['short_id'] in allowed]
    cover=set(r['extra'])
    for i in allowed:cover.update(candidates[i]['cover'])
    for p in pp:cover.update(p['extra'])
    missing=[t for t in range(891) if t not in cover]
    availability.append(dict(U_short_id=r['short_id'],compatible_short_count=len(allowed),
                             compatible_P_count=len(pp),missing_target_ids=missing))
good={a['U_short_id'] for a in availability if not a['missing_target_ids'] and a['compatible_P_count']}
repairs=[r for r in repairs if r['short_id'] in good]
report=dict(stage='setup',raw_short_bundles=raw_count,short_bundles_after_EH_exclusion=nshort,
            normalized_U_count=len(repairs),P_count=len(palindromes),EH=EH,WH=WH,
            availability=availability,elapsed=time.monotonic()-START)
print(json.dumps(report),flush=True)
if not repairs:
    with open(OUT,'w') as f:json.dump(dict(report=report,status='AVAILABILITY_OBSTRUCTION'),f)
    raise SystemExit

# One shared integer constraint list is used by both optimization backends.
variables=[dict(kind='short',family=c['family'],source_id=c['source_id'],type=c['type']) for c in candidates]
for r in repairs:r['var']=len(variables);variables.append(dict(kind='U_repair',short_id=r['short_id']))
for p in palindromes:p['var']=len(variables);variables.append(dict(kind='P_upgrade',short_id=p['short_id']))
constraints=[]
def add(name,terms,sense,rhs):
    constraints.append(dict(name=name,terms=list(terms),sense=sense,rhs=rhs))
by_target=[[] for _ in reps]
for c in candidates:
    for t in c['cover']:by_target[t].append((c['id'],1))
for r in repairs:
    for t in r['extra']:by_target[t].append((r['var'],1))
for p in palindromes:
    for t in p['extra']:by_target[t].append((p['var'],1))
for t in range(891):add('target_'+str(t),by_target[t],'>=',1)
for t in sorted(critical):
    terms=((c['id'],1) for c in candidates if t in c['critical'])
    add('short_critical_'+str(t),terms,'=',0 if t==EH else 1)
add('short_physical_rows',((c['id'],c['row_count']) for c in candidates),'=',168)
add('one_U_repair',((r['var'],1) for r in repairs),'=',1)
add('one_P_upgrade',((p['var'],1) for p in palindromes),'=',1)
for r in repairs:add('U_selected_'+str(r['var']),[(r['short_id'],1),(r['var'],-1)],'>=',0)
for p in palindromes:add('P_selected_'+str(p['var']),[(p['short_id'],1),(p['var'],-1)],'>=',0)
add('integer_cut_r_z_u',((c['id'],1) for c in candidates if c['type'] in ('r','z','u')),'=',12)
add('integer_cut_r_v',((c['id'],-1) for c in candidates if c['type'] in ('r','v')),'>=',-1)
# The ledger bounds all short W capacity by five. The two distinct endpoint
# witnesses therefore force exact W coverage and prohibit overlap there.
for t in sorted(Wset):add('exact_W_'+str(t),by_target[t],'=',1)
cert=dict(report=report,scope='168 whole short rows; exact short critical cover excluding E_H; one normalized U16 strip repair and one selected palindrome P4 full upgrade on K != H',
          base_catalogue=BASE,diamond_catalogue=DIAM,variables=variables,
          constraints=constraints,repairs=repairs,palindromes=palindromes)
with open(OUT,'w') as f:json.dump(cert,f)

from scipy.optimize import linprog,OptimizeWarning
from scipy.sparse import coo_matrix
import numpy as np
warnings.filterwarnings('ignore',category=OptimizeWarning)
def matrix(sense):
    rows=[c for c in constraints if c['sense']==sense];ii=[];jj=[];vv=[]
    for i,c in enumerate(rows):
        for j,v in c['terms']:ii.append(i);jj.append(j);vv.append(v if sense=='=' else -v)
    return coo_matrix((vv,(ii,jj)),shape=(len(rows),len(variables))).tocsr(),np.array([c['rhs'] if sense=='=' else -c['rhs'] for c in rows],dtype=float)
Aeq,beq=matrix('=');Aub,bub=matrix('>=')
then=time.monotonic()
res=linprog(np.zeros(len(variables)),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,
            bounds=(0,1),method='highs',options={'time_limit':3.0,'threads':2})
lp=dict(stage='LP',status=int(res.status),message=res.message,solver_seconds=time.monotonic()-then,
        variables=len(variables),constraints=len(constraints),elapsed=time.monotonic()-START)
if res.success:
    lp['max_equality_residual']=float(np.max(np.abs(Aeq@res.x-beq)))
    lp['max_inequality_violation']=float(max(0,np.max(Aub@res.x-bub)))
    assert lp['max_equality_residual']<1e-6 and lp['max_inequality_violation']<1e-6
    cert['lp_nonzeros']={str(i):float(v) for i,v in enumerate(res.x) if v>1e-9}
cert['LP']=lp
with open(OUT,'w') as f:json.dump(cert,f)
print(json.dumps(lp),flush=True)
if not res.success:raise SystemExit

def replay(selected,U,Pup):
    def vectors(w,g):
        x=[0]*8;out=[tuple(x)]
        for a in w:x[a^g]+=1;out.append(tuple(x))
        return out
    def rowkey(C,D):return tuple(sorted((tuple(C),tuple(D))))
    rows={};source_rows={}
    for c in selected:
        s=c['source'];keys=set()
        components=([(w,w) for w in s['words']] if c['family']=='copy' else [(d['C'],d['D']) for d in s['components']])
        for cw,dw in components:
            for g in range(8):
                C=vectors(cw,g)[1:8];D=vectors(dw,g^s['v'])[1:8]
                k=rowkey(C,D);rows[k]=k;keys.add(k)
        assert len(keys)==c['row_count']
        source_rows[c['id']]=keys
    assert len(rows)==168 and sum(len(a)+len(b) for a,b in rows)==2352
    # Replace eight original U rows and their actual global complements.
    touched=set()
    for g in range(8):
        C=vectors(U['C'],g);D=vectors(U['D'],g^U['v'])
        old=rowkey(C[1:8],D[1:8]);new=rowkey(C[:8],D[1:8])
        assert old in source_rows[U['short_id']] and old not in touched
        touched.add(old);del rows[old];rows[new]=new
        # Complement a vector only on its own shore, then reverse its chain.
        suppC={a^g for a in U['C']};suppD={a^g^U['v'] for a in U['D']}
        CC=[tuple(2-x[i] if i in suppC else 0 for i in range(8)) for x in reversed(C)]
        DD=[tuple(2-x[i] if i in suppD else 0 for i in range(8)) for x in reversed(D)]
        old=rowkey(CC[1:8],DD[1:8]);new=rowkey(CC[1:9],DD[1:8])
        assert old in source_rows[U['short_id']] and old not in touched
        touched.add(old);del rows[old];rows[new]=new
    assert len(touched)==16
    pkeys=set()
    for g in range(8):
        C=vectors(Pup['word'],g);D=vectors(Pup['word'],g^Pup['v'])
        old=rowkey(C[1:8],D[1:8]);new=rowkey(C,D)
        if old in pkeys:continue
        pkeys.add(old);assert old in source_rows[Pup['short_id']] and old in rows
        del rows[old];rows[new]=new
    assert len(pkeys)==4 and len(rows)==168
    loads=[0]*6561
    for C,D in rows:
        for Q in (C,D):
            for a,b in zip(Q,Q[1:]):
                delta=[y-x for x,y in zip(a,b)]
                assert delta.count(1)==1 and delta.count(0)==7
            assert all(all(v in (0,1,2) for v in x) for x in Q)
        suppC={i for x in C for i,v in enumerate(x) if v}
        suppD={i for x in D for i,v in enumerate(x) if v}
        assert len(suppC)==len(suppD)==4 and not suppC.intersection(suppD)
        for a in C:
            for b in D:loads[sum((u+v)*p for u,v,p in zip(a,b,P))]+=1
    cost=sum(len(a)+len(b) for a,b in rows)
    assert cost==2384 and min(loads)>=1
    with open(WIT,'w') as f:json.dump(dict(rows=sorted(rows),loads=loads,cost=cost,row_count=len(rows),
         selected=[dict(family=c['family'],source_id=c['source_id']) for c in selected],U=U,P=Pup),f)
    return dict(witness=WIT,row_count=len(rows),cost=cost,min_load=min(loads),max_load=max(loads))

from ortools.sat.python import cp_model
model=cp_model.CpModel();xs=[model.new_bool_var('x'+str(i)) for i in range(len(variables))]
for c in constraints:
    expr=cp_model.LinearExpr.weighted_sum([xs[j] for j,v in c['terms']],[v for j,v in c['terms']])
    model.add(expr==c['rhs']) if c['sense']=='=' else model.add(expr>=c['rhs'])
solver=cp_model.CpSolver()
solver.parameters.max_time_in_seconds=min(18.0,max(0.01,23.5-(time.monotonic()-START)))
solver.parameters.num_search_workers=2;solver.parameters.random_seed=0
solver.parameters.stop_after_first_solution=True
limit=solver.parameters.max_time_in_seconds
then=time.monotonic();status=solver.solve(model)
cp=dict(stage='CP',status=solver.status_name(status),limit_seconds=limit,
        solver_seconds=time.monotonic()-then,branches=solver.num_branches,conflicts=solver.num_conflicts,
        elapsed=time.monotonic()-START)
if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
    chosen=[c for c in candidates if solver.value(xs[c['id']])]
    U=next(r for r in repairs if solver.value(xs[r['var']]))
    Pup=next(p for p in palindromes if solver.value(xs[p['var']]))
    assert sum(c['row_count'] for c in chosen)==168
    cp['replay']=replay(chosen,U,Pup);cp['elapsed']=time.monotonic()-START
cert['CP']=cp
with open(OUT,'w') as f:json.dump(cert,f)
print(json.dumps(cp),flush=True)
