"""One <=3s h100 verification of a fixed29-row skeleton; no search."""
import os,json,time,resource
from collections import Counter
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
OUT='/tmp/Q3_D8_SINGER_DIFFERENT_PROFILE_SKELETON_CERTIFICATE_20260908_ternarylift.json'
P=[3**i for i in range(8)]
S=(0,2,4,6,3,1,7,5)
powers=[tuple(range(8))]
for _ in range(6):powers.append(tuple(S[a] for a in powers[-1]))
assert tuple(S[a] for a in powers[-1])==powers[0] and len(set(powers))==7
END_C=[0,0,1,1,2,2,4,4]
END_D=[3,3,7,7,6,6,5,5]
SEED_C=[0,1,2,3,1,2,3,0]
SEED_D=[4,6,7,4,6,5,7,5]

def chain(w,g):
    assert sorted(Counter(w).values())==[2,2,2,2]
    x=[0]*8;out=[tuple(x)]
    for a in w:x[g[a]]+=1;out.append(tuple(x))
    return out

def key(C,D):return tuple(sorted((tuple(C),tuple(D))))

rows={}
def add(C,D,role):
    k=key(C,D)
    assert k not in rows
    rows[k]=role

for g in powers:
    add(chain(END_C,g)[:8],chain(END_D,g)[:8],'lower_endpoint')
    add(chain(END_C[::-1],g)[1:9],chain(END_D[::-1],g)[1:9],'upper_endpoint')
    add(chain(SEED_C,g)[1:8],chain(SEED_D,g)[1:8],'seed')
    add(chain(SEED_C[::-1],g)[1:8],chain(SEED_D[::-1],g)[1:8],'seed_complement')
lineC=[tuple([a]+[0]*7) for a in range(3)]
lineD=[tuple([0]+[1]*7)]
add(lineC,lineD,'central_line')
assert len(rows)==29 and Counter(rows.values())==dict(lower_endpoint=7,upper_endpoint=7,seed=7,seed_complement=7,central_line=1)

def encode(x):return sum(v*p for v,p in zip(x,P))

def complement_chain(Q):
    support={i for x in Q for i,v in enumerate(x) if v}
    return [tuple(2-x[i] if i in support else 0 for i in range(8)) for x in reversed(Q)]

def move_chain(Q,g):
    out=[]
    for x in Q:
        y=[0]*8
        for i,v in enumerate(x):y[g[i]]=v
        out.append(tuple(y))
    return out

loads=[0]*6561;role_loads={r:[0]*6561 for r in set(rows.values())}
cost=0
for (C,D),role in rows.items():
    cost+=len(C)+len(D)
    for Q in (C,D):
        assert all(all(v in (0,1,2) for v in x) for x in Q)
        for a,b in zip(Q,Q[1:]):
            delta=[y-x for x,y in zip(a,b)]
            assert delta.count(1)==1 and delta.count(0)==7
    A={i for x in C for i,v in enumerate(x) if v};B={i for x in D for i,v in enumerate(x) if v}
    assert not A.intersection(B) and A|B==set(range(8))
    if role=='central_line':assert sorted((len(A),len(B)))==[1,7]
    else:assert len(A)==len(B)==4
    assert key(move_chain(C,S),move_chain(D,S)) in rows
    assert key(complement_chain(C),complement_chain(D)) in rows
    for a in C:
        for b in D:
            x=tuple(u+v for u,v in zip(a,b));assert all(v in (0,1,2) for v in x)
            z=encode(x);loads[z]+=1;role_loads[role][z]+=1
assert cost==424

vectors=[tuple((z//p)%3 for p in P) for z in range(6561)]
ranks=[sum(x) for x in vectors]
qweight=[sum(ranks[z]-v==7 for v in x) for z,x in enumerate(vectors)]
assert sum(qweight)==9432
excess4=sum(q*max(n-1,0) for q,n in zip(qweight,loads))
assert excess4==0
assert all(n<=1 for q,n in zip(qweight,loads) if q)
assert sum(q*n for q,n in zip(qweight,loads))==1690
assert sum(q*n for q,n in zip(qweight,role_loads['central_line']))==10
extremes={0,6560}|{a*p for p in P for a in (1,2)}|{6560-a*p for p in P for a in (1,2)}
assert len(extremes)==34 and all(loads[z] for z in extremes)
fixed={a+b*sum(P[1:]) for a in range(3) for b in range(3)}
assert len(fixed)==9 and all(loads[z] for z in fixed)
assert loads[sum(P)]==1

# Inventory all targets under the fixed seven-coordinate cycle only.
oid=[None]*6561;orbits=[]
for z in range(6561):
    if oid[z] is not None:continue
    x=vectors[z]
    orb=sorted({sum(x[i]*P[g[i]] for i in range(8)) for g in powers})
    assert len(orb) in (1,7) and orb[0]==z
    t=len(orbits)
    for a in orb:oid[a]=t
    assert len({loads[a] for a in orb})==1
    orbits.append(dict(id=t,rep=z,target=x,rank=ranks[z],n1=x.count(1),x0=x[0],size=len(orb),
                       qweight=qweight[z],load=loads[z],points=orb))
assert len(orbits)==945
for t in orbits:t['complement_orbit']=oid[6560-t['rep']]
group_orbits=[]
for t in orbits:
    u=orbits[t['complement_orbit']]
    if t['id']>u['id']:continue
    assert t['load']==u['load']
    points=sorted(set(t['points'])|set(u['points']))
    group_orbits.append(dict(id=len(group_orbits),singer_orbits=sorted({t['id'],u['id']}),
                             rep=points[0],points=points,size=len(points),load=t['load']))
assert len(group_orbits)==473 and Counter(t['size'] for t in group_orbits)=={14:468,2:4,1:1}
critical=[t for t in orbits if t['rank']==7 and t['size']==7]
assert len(critical)==145
assert Counter(t['n1'] for t in critical)=={1:40,3:80,5:24,7:1}
assert Counter(t['n1'] for t in critical if t['load'])=={1:14,3:5,5:6,7:1}
classes=[]
for n1 in (1,3,5,7):
    for x0 in (0,1,2):
        cc=[t for t in critical if t['n1']==n1 and t['x0']==x0]
        if not cc:continue
        classes.append(dict(n1=n1,x0=x0,total_orbits=len(cc),
                            raw_orbit_occurrences=sum(t['load'] for t in cc),
                            distinct_covered_orbits=sum(t['load']>0 for t in cc),
                            residual_orbits=sum(t['load']==0 for t in cc),
                            raw_point_occurrences=sum(t['size']*t['load'] for t in cc),
                            distinct_covered_points=sum(t['size'] for t in cc if t['load'])))
central=[t for t in orbits if t['rank']==8 and t['qweight'] and t['size']==7]
pure_central=[t for t in orbits if t['rank']==8 and not t['qweight']]
assert len(central)==148 and sum(t['load']>0 for t in central)==22
assert len(pure_central)==10 and sum(t['load']>0 for t in pure_central)==6
role_critical={}
for role,rl in role_loads.items():
    group=[]
    for n1 in (1,3,5,7):
        for x0 in (0,1,2):
            ids=[z for z,x in enumerate(vectors) if ranks[z]==7 and x.count(1)==n1 and x[0]==x0]
            raw=sum(rl[z] for z in ids)
            if raw:group.append(dict(n1=n1,x0=x0,raw_points=raw,distinct_points=sum(rl[z]>0 for z in ids),
                                     distinct_orbits=len({oid[z] for z in ids if rl[z]})))
    role_critical[role]=group
report=dict(stage='fixed_skeleton_verification',row_count=len(rows),regular_row_count=28,cost=cost,
            projected_charge='845/2',weighted_excess='0',residual_projection_weight='3871/2',
            covered_points=sum(n>0 for n in loads),maximum_load=max(loads),
            target_orbits=len(orbits),covered_target_orbits=sum(t['load']>0 for t in orbits),
            residual_target_orbits=sum(t['load']==0 for t in orbits),
            target_group_orbits=len(group_orbits),residual_group_orbits=sum(t['load']==0 for t in group_orbits),
            critical_nonfixed_total=145,critical_nonfixed_covered=26,critical_nonfixed_residual=119,
            critical_classes=classes,central_positive_nonfixed_total=148,central_positive_nonfixed_covered=22,
            central_positive_nonfixed_residual=126,central_pure_total=10,central_pure_covered=6,
            all_extremes_covered=True,all_fixed_targets_covered=True,chain_checks=True,
            singer_and_complement_closed=True,zero_positive_weight_overlap=True,
            elapsed=time.monotonic()-START,certificate=OUT)
certificate=dict(words=dict(endpoint_C=END_C,endpoint_D=END_D,seed_C=SEED_C,seed_D=SEED_D),
                 singer=S,coordinate_cycle=[1,2,4,3,6,7,5],
                 rows=[dict(C=C,D=D,role=role) for (C,D),role in rows.items()],
                 loads=loads,qweight=qweight,orbits=orbits,group_orbits=group_orbits,
                 residual_targets=[z for z,n in enumerate(loads) if n==0],
                 residual_orbit_ids=[t['id'] for t in orbits if not t['load']],
                 residual_group_orbit_ids=[t['id'] for t in group_orbits if not t['load']],
                 role_critical_counts=role_critical,report=report)
with open(OUT,'w') as f:json.dump(certificate,f)
report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
