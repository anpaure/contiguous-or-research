"""One <=5s h100 provider-only finite inventory.

Input: the independently replayed fixed29-row Singer skeleton, and nothing
else. No LP, CP, higher-profile enumeration, or resumed previous job.

Literal pairs: BB=AABBCCDD/EEFFGGHH; BL=AABBCCDD/EFEFGHGH;
BU=AABBCCDD/EFGEFGHH. Embed the eight distinct axis roles bijectively in
coordinates0..7. Normalize the first nonzero axis in role order to global1
under Singer, then enumerate the remaining6! assignments. There are12960
normalized ordered embeddings: BB8*720, BL6*720, BU4*720. Quotient shore
exchange and global reversal with Singer re-normalization. The exact
canonical pools are nine placement classes of720, total6480:
BB interior/endpoint; BL B-interior/L-interior/L-endpoint;
BU B-A/B-B/B-D/U-H. Every physical G=C7 x complement bundle has14 rows.

Only the five proved position patterns in Section4 of the amended ledger
are joined. Each result selects one BB, one BL, one BU and partitions the
26 residual n1=1 critical G-orbits exactly. Positive-load caps permit one
critical excess unit at n1=3 and the pattern's x0 in{1,2}, plus at most one
central n1=2 excess unit with x0=1 and one with x0 in{0,2}. All other
positive-weight repetitions are forbidden. These are necessary provider
conditions, not a full-cube cover claim. All actual words and exact G loads,
every feasible triple, and enlarged-union availability screens are saved.

The internal4.15s deadline reserves time for serialization; an unfinished
enumeration is explicitly INCOMPLETE, never an obstruction certificate.
Run only after root/direct static audits, under an external timeout5s.
"""
import collections
import itertools
import json
import os
import resource
import time

os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
SOURCE='/tmp/Q3_D8_SINGER_DIFFERENT_PROFILE_SKELETON_CERTIFICATE_20260908_ternarylift.json'
OUT='/tmp/Q3_D8_SINGER_BB_BL_BU_PROVIDER_INVENTORY_20260908_ternarylift.json'
with open(SOURCE) as f:skeleton=json.load(f)
assert skeleton['report']['cost']==424 and skeleton['report']['zero_positive_weight_overlap']
POW=[3**i for i in range(8)]
CYCLE=(1,2,4,3,6,7,5)
S=(0,2,4,6,3,1,7,5)
assert tuple(skeleton['singer'])==S and tuple(skeleton['coordinate_cycle'])==CYCLE
groups=skeleton['group_orbits'];gid=[None]*6561;metadata=[]
for group in groups:
    assert group['id']==len(metadata)
    for code in group['points']:gid[code]=group['id']
    rank7=[z for z in group['points'] if sum(z//p%3 for p in POW)==7]
    rep=rank7[0] if rank7 else group['rep']
    vector=tuple(rep//p%3 for p in POW)
    metadata.append(dict(rep=rep,target=vector,rank=sum(vector),n1=vector.count(1),
                         x0=vector[0],size=group['size'],load=group['load'],
                         qweight=skeleton['qweight'][rep]))
assert len(groups)==473 and all(g is not None for g in gid)
assert all(m['load']<=1 for m in metadata if m['qweight'])
one_ids=[g for g,m in enumerate(metadata) if m['rank']==7 and m['n1']==1]
assert len(one_ids)==40
one_index={g:i for i,g in enumerate(one_ids)}
wanted=sum(1<<one_index[g] for g in one_ids if not metadata[g]['load'])
assert wanted.bit_count()==26
shift_to_one={}
for a in CYCLE:
    k=CYCLE.index(a)
    shift_to_one[a]=tuple(0 if x==0 else CYCLE[(CYCLE.index(x)-k)%7] for x in range(8))

def normalize(left,right):
    merged=tuple(left)+tuple(right)
    shift=shift_to_one[next(a for a in merged if a)]
    return tuple(shift[a] for a in left),tuple(shift[a] for a in right)

def canonical(left,right):
    return min(normalize(left,right),normalize(right,left),
               normalize(left[::-1],right[::-1]),normalize(right[::-1],left[::-1]))

chain_cache={}
def chain(word):
    word=tuple(word)
    if word not in chain_cache:
        assert len(word)==8 and sorted(collections.Counter(word).values())==[2]*4
        states=[0]
        for a in word:states.append(states[-1]+POW[a])
        chain_cache[word]=states[1:8]
    return chain_cache[word]

PATTERNS=[
    dict(id=1,critical_x0=1,BB=('interior',),BL=('B-interior',),BU=('B-B',)),
    dict(id=2,critical_x0=2,BB=('endpoint',),BL=('L-interior',),BU=('B-B',)),
    dict(id=3,critical_x0=2,BB=('interior',),BL=('L-endpoint',),BU=('B-B',)),
    dict(id=4,critical_x0=2,BB=('interior',),BL=('B-interior',),BU=('B-A','U-H')),
    dict(id=5,critical_x0=2,BB=('interior',),BL=('L-interior',),BU=('B-D',)),
]
LEFT=(0,0,1,1,2,2,3,3)
RIGHTS={'BB':(4,4,5,5,6,6,7,7),'BL':(4,5,4,5,6,7,6,7),'BU':(4,5,6,4,5,6,7,7)}
ZERO_ROLES={'BB':tuple(range(8)),'BL':(1,2,4,5,6,7),'BU':(0,1,3,7)}
EXPECTED_ONE={'BB':12,'BL':8,'BU':6}

def placement(kind,zero_role):
    if kind=='BB':return 'interior' if zero_role%4 in(1,2) else 'endpoint'
    if kind=='BL':return 'B-interior' if zero_role in(1,2) else 'L-interior' if zero_role in(5,6) else 'L-endpoint'
    return {0:'B-A',1:'B-B',3:'B-D',7:'U-H'}[zero_role]

def make_candidate(left,right,kind,place,key):
    assert set(left).isdisjoint(right) and set(left)|set(right)==set(range(8))
    assert tuple(left)!=tuple(left[::-1]) or tuple(right)!=tuple(right[::-1])
    counts=collections.Counter(gid[a+b] for a in chain(left) for b in chain(right))
    # Averaging the14 distinct physical rows gives these exact per-point
    # loads on G target orbits, including the fixed-point orbits if present.
    loads={g:14*n//metadata[g]['size'] for g,n in counts.items()}
    assert all(14*n%metadata[g]['size']==0 for g,n in counts.items())
    assert sum(metadata[g]['size']*n for g,n in loads.items())==14*49
    critical_one=sum(n for g,n in counts.items() if metadata[g]['rank']==7 and metadata[g]['n1']==1)
    assert critical_one==EXPECTED_ONE[kind]
    mask=sum(1<<one_index[g] for g in one_ids if loads.get(g,0))
    return dict(id=len(candidates),kind=kind,placement=place,left=list(left),right=list(right),
                canonical=[list(key[0]),list(key[1])],loads=loads,one_mask=mask,
                flag_eligible=mask.bit_count()==EXPECTED_ONE[kind] and not(mask&~wanted))

def caps(candidate_ids,critical_x0):
    summed=collections.Counter()
    for i in candidate_ids:summed.update(candidates[i]['loads'])
    excess=[0,0,0]
    for g,n in summed.items():
        m=metadata[g]
        if not m['qweight']:continue
        e=max(0,m['load']+n-1)
        if not e:continue
        if m['rank']==7 and m['n1']==3 and m['x0']==critical_x0 and m['size']==14:
            slot=0
        elif m['rank']==8 and m['n1']==2 and m['size']==14:
            slot=1 if m['x0']==1 else 2
        else:return None
        excess[slot]+=e
        if excess[slot]>1:return None
    return tuple(excess)

class BudgetExpired(Exception):pass
def check_time():
    if time.monotonic()-START>4.15:raise BudgetExpired

candidates=[];lookup={};normalized_embeddings=0
catalogue_complete=False;join_complete=False
individual={};pattern_reports=[];solutions=[];checked_pairs=0
stage='catalogue'
try:
    for kind in ('BB','BL','BU'):
        for zr in ZERO_ROLES[kind]:
            first=next(i for i in range(8) if i!=zr)
            free=[i for i in range(8) if i not in(zr,first)]
            for perm in itertools.permutations(CYCLE[1:]):
                normalized_embeddings+=1
                if normalized_embeddings%256==0:check_time()
                assignment=[None]*8;assignment[zr]=0;assignment[first]=1
                for i,a in zip(free,perm):assignment[i]=a
                left=tuple(assignment[i] for i in LEFT)
                right=tuple(assignment[i] for i in RIGHTS[kind])
                key=canonical(left,right);tag=placement(kind,zr)
                if key in lookup:
                    old=candidates[lookup[key]]
                    assert old['kind']==kind and old['placement']==tag
                    continue
                c=make_candidate(left,right,kind,tag,key)
                lookup[key]=c['id'];candidates.append(c)
    assert normalized_embeddings==12960 and len(candidates)==6480
    placement_counts=collections.Counter((c['kind'],c['placement']) for c in candidates)
    assert len(placement_counts)==9 and set(placement_counts.values())=={720}
    catalogue_complete=True;stage='individual_filters'
    for c in candidates:
        if c['id']%256==0:check_time()
        if c['flag_eligible']:
            for x0 in (1,2):individual[(c['id'],x0)]=caps([c['id']],x0)
    stage='exact_flag_joins'
    for pattern in PATTERNS:
        check_time();x0=pattern['critical_x0']
        pools={kind:[c['id'] for c in candidates if c['kind']==kind and c['placement'] in pattern[kind]
                     and c['flag_eligible'] and individual.get((c['id'],x0)) is not None]
               for kind in ('BB','BL','BU')}
        union=0
        for ids in pools.values():
            for i in ids:union|=candidates[i]['one_mask']
        missing=[g for g in one_ids if wanted&(1<<one_index[g]) and not union&(1<<one_index[g])]
        pr=dict(pattern=pattern['id'],critical_x0=x0,pool_ids=pools,
                pool_counts={k:len(v) for k,v in pools.items()},missing_flag_group_ids=missing,
                missing_flag_targets=[metadata[g] for g in missing],flag_triples=0,
                cap_passing_triples=0,join_complete=False)
        pattern_reports.append(pr)
        if missing or any(not ids for ids in pools.values()):
            pr['join_complete']=True;pr['status']='ENLARGED_UNION_AVAILABILITY_OBSTRUCTION'
            continue
        by_mask=collections.defaultdict(list)
        for i in pools['BU']:by_mask[candidates[i]['one_mask']].append(i)
        for bi in pools['BB']:
            bm=candidates[bi]['one_mask']
            for li in pools['BL']:
                checked_pairs+=1
                if checked_pairs%1024==0:check_time()
                lm=candidates[li]['one_mask']
                if bm&lm:continue
                wanted_bu=wanted^(bm|lm)
                for ui in by_mask.get(wanted_bu,[]):
                    pr['flag_triples']+=1
                    total_caps=caps([bi,li,ui],x0)
                    if total_caps is None:continue
                    assert bm|lm|candidates[ui]['one_mask']==wanted
                    assert not(bm&candidates[ui]['one_mask']) and not(lm&candidates[ui]['one_mask'])
                    pr['cap_passing_triples']+=1
                    solutions.append(dict(pattern=pattern['id'],BB=bi,BL=li,BU=ui,
                                          excess_critical=total_caps[0],
                                          excess_central_x0_1=total_caps[1],
                                          excess_central_x0_02=total_caps[2]))
        pr['join_complete']=True
        pr['status']='FEASIBLE_PROVIDER_TRIPLES' if pr['cap_passing_triples'] else 'NO_PROVIDER_TRIPLES'
    join_complete=True
except BudgetExpired:
    pass

report=dict(stage='BB_BL_BU_provider_inventory',status='COMPLETE' if catalogue_complete and join_complete else 'TIME_LIMIT_INCOMPLETE',
            last_stage=stage,catalogue_complete=catalogue_complete,join_complete=join_complete,
            normalized_embeddings=normalized_embeddings,canonical_candidates=len(candidates),
            placement_counts=[dict(kind=k[0],placement=k[1],count=v) for k,v in
                              sorted(collections.Counter((c['kind'],c['placement']) for c in candidates).items())],
            checked_BB_BL_pairs=checked_pairs,feasible_provider_triples=len(solutions),
            pattern_counts=[{k:p[k] for k in('pattern','critical_x0','pool_counts','missing_flag_group_ids',
                                             'flag_triples','cap_passing_triples','join_complete')}
                            for p in pattern_reports],elapsed=time.monotonic()-START,certificate=OUT,
            full_cover_claim=False)
certificate=dict(scope=__doc__,source=SOURCE,singer=S,metadata=metadata,one_ids=one_ids,wanted=wanted,
                 patterns=PATTERNS,candidates=candidates,pattern_reports=pattern_reports,
                 feasible_provider_triples=solutions,report=report)
with open(OUT,'w') as f:json.dump(certificate,f)
report['elapsed']=time.monotonic()-START
print(json.dumps(report),flush=True)
