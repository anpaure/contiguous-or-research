#!/usr/bin/env python3
"""One unrestricted fixed-bank cap decision. REVIEW REQUIRED BEFORE h100 RUN.

No anchors. H1/H2 frozen; every H3 native triple frozen; all lower targets
required. One CaDiCaL195 call, never restarted. Streamed DIMACS/mappings.
"""
import gc,hashlib,json,math,os,resource,shutil,signal,socket,subprocess,sys,time
from array import array
from collections import Counter
from pathlib import Path

BASE=Path('/home/amodo/exact-b-k17-unrestricted-triple-caps-20260908')
SOURCE=Path('/home/amodo/exact-b-k17-height-adaptive-20260908/height_adaptive_canonical_cycles.json')
FULL=(1<<17)-1
EXPECTED_SOURCE_SHA='fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3'
assert socket.gethostname().split('.')[0]=='arboghast','Mathematical execution is restricted to h100/arboghast.'
LIMITS=dict(total_cpu_seconds=120,total_wall_seconds=150,
    driver_address_space_soft_bytes=512*1024**2,worker_address_space_bytes=3584*1024**2,
    worker_single_file_bytes=1024**3,maximum_solver_decision_calls=1,solver_restarts=0)

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def dump(name,value):
    (BASE/name).write_text(json.dumps(value,indent=2)+'\n')

def solver_worker(cpu_limit):
    # The driver reserves CPU for generation/validation. Combined address-space
    # caps are 512 MiB driver + 3584 MiB worker = 4 GiB.
    resource.setrlimit(resource.RLIMIT_AS,(3584*1024**2,3584*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU,(cpu_limit,cpu_limit))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1024**3,1024**3))
    from pysat.solvers import Cadical195
    start=time.monotonic()
    solver=Cadical195(use_timer=True,with_proof=True)
    solver.configure({'seed':0})
    with (BASE/'unrestricted_triple_caps.cnf').open() as f:
        for line in f:
            if line[0] in 'cp':continue
            literals=list(map(int,line.split()))
            assert literals.pop()==0
            solver.add_clause(literals)
    # Exactly ONE solver decision call. Resource exhaustion kills this worker;
    # the driver reports INCONCLUSIVE and does not invoke another solver.
    result=solver.solve()
    stats=solver.accum_stats()
    if result:
        model=solver.get_model()
        (BASE/'solver_model.json').write_text(json.dumps(model)+'\n')
    elif result is False:
        # Preserve PySAT's native binary DRAT stream without materializing a
        # potentially huge text proof. It is NOT called independently verified.
        solver.prfile.flush();solver.prfile.seek(0)
        with (BASE/'solver_raw_proof.drat.bin').open('wb') as dst:
            shutil.copyfileobj(solver.prfile,dst,1024*1024)
    record=dict(result=result,solver='Cadical195',seed=0,decision_calls=1,stats=stats,
        elapsed_seconds=time.monotonic()-start,cpu_seconds=time.process_time(),
        proof_independently_checked=False,worker_cpu_limit=cpu_limit,
        worker_single_file_limit_bytes=1024**3)
    if result is False:record['raw_proof_bytes']=(BASE/'solver_raw_proof.drat.bin').stat().st_size
    dump('solver_result.json',record)
    solver.delete()

if len(sys.argv)>1 and sys.argv[1]=='--solver-worker':
    solver_worker(int(sys.argv[2]));sys.exit(0)

resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,4*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(118,120))
# Refuse an existing output directory: never silently reuse a stale solver
# result or turn this one-decision script into a restart loop.
BASE.mkdir(exist_ok=False)
started=time.monotonic();cpu_started=time.process_time()
deadline=started+150
worker=None
memory_reserve=bytearray(1024*1024)

def finish_inconclusive(reason,extra=None):
    if worker is not None and worker.poll() is None:
        worker.kill();worker.wait()
    record=dict(status='INCONCLUSIVE',reason=reason,solver_restarts=0,
        wall_seconds=time.monotonic()-started,
        driver_cpu_seconds=time.process_time()-cpu_started,
        child_cpu_seconds=resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+
                          resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,
        resource_limits=LIMITS)
    if extra:record.update(extra)
    dump('decision_report.json',record);print(json.dumps(record),flush=True)
    raise SystemExit(0)

def alarm_handler(signum,frame):finish_inconclusive('150-second total wall limit')
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(150)
signal.signal(signal.SIGXCPU,lambda signum,frame:finish_inconclusive('aggregate CPU budget reached'))
def driver_excepthook(kind,value,traceback):
    global memory_reserve
    if issubclass(kind,MemoryError):
        memory_reserve=None;gc.collect()
        try:finish_inconclusive('driver address-space limit reached')
        except SystemExit:os._exit(0)
    sys.__excepthook__(kind,value,traceback)
sys.excepthook=driver_excepthook

source_raw=SOURCE.read_bytes();records=json.loads(source_raw)
assert hashlib.sha256(source_raw).hexdigest()==EXPECTED_SOURCE_SHA
banks=[];fixed=set();next_var=0;cap_count=0
capmap=(BASE/'cap_bits.jsonl').open('w')
for rec in records:
    cid=rec['cycle'];h=rec['height'];H=min(h,3)
    X=[FULL^a for a in rec['lower_owners']];v=len(X);D=[]
    for i in range(v):
        value=FULL
        for j in range(H+1):value &= X[(i+j)%v]
        assert value and value.bit_count()==9-H;D.append(value)
    pin=[0]*v;variables=[{} for _ in range(v)]
    if H==3:
        for i in range(v):
            pin[i]=(X[i]&~X[(i-1)%v])|(X[(i+3)%v]&~X[(i+4)%v])
            assert pin[i] and pin[i]&D[i]==pin[i]
            optional=D[i]&~pin[i]
            while optional:
                bit=optional&-optional;optional-=bit
                next_var+=1;cap_count+=1;variables[i][bit]=next_var
                capmap.write(json.dumps([next_var,cid,i,bit])+'\n')
    else:
        # Frozen lower palette ONLY, never the earlier anchor-frame palette.
        for i in range(v):
            value=0
            for ell in range(1,v+1):
                value |= D[(i+ell-1)%v]
                if value.bit_count()>7:break
                fixed.add(value)
    banks.append(dict(cycle=cid,height=h,H=H,X=X,D=D,pin=pin,variables=variables))
capmap.close()
assert len(banks)==146 and sum(len(b['D']) for b in banks)==24310
assert len(fixed)==1887 and all(t.bit_count()==7 for t in fixed)
required=[t for t in range(1,FULL+1) if t.bit_count()<=7 and t not in fixed]
assert len(required)==39338
selectors={t:array('I') for t in required}
clauses=0;family_counts=Counter();length_counts=Counter()
body=(BASE/'formula_body.tmp').open('w')
def clause(lits,family):
    global clauses
    assert lits and all(type(x) is int and x!=0 for x in lits)
    body.write(' '.join(map(str,lits))+' 0\n')
    clauses+=1;family_counts[family]+=1;length_counts[len(lits)]+=1

triple_count=0
for bank in banks:
    if bank['H']!=3:continue
    D=bank['D'];P=bank['pin'];V=bank['variables'];v=len(D)
    for i in range(v):
        positions=[i,(i+1)%v,(i+2)%v]
        target=D[positions[0]]|D[positions[1]]|D[positions[2]]
        assert target.bit_count()==8
        triple_count+=1
        pending=target
        while pending:
            bit=pending&-pending;pending-=bit
            if any(P[j]&bit for j in positions):continue
            literals=[V[j][bit] for j in positions if D[j]&bit]
            # Sparse run theorem: only all-three-available unpinned clauses remain.
            assert len(literals)==3
            clause(literals,'native_triple')

all_hosts=0;witness_count=0
with (BASE/'witness_selectors.jsonl').open('w') as witness_map:
    for bank in banks:
        if bank['H']!=3:continue
        cid=bank['cycle'];D=bank['D'];P=bank['pin'];V=bank['variables'];v=len(D)
        for start in range(v):
            F=available=0
            for ell in (1,2):
                j=(start+ell-1)%v;F|=P[j];available|=D[j]
                positions=[(start+j)%v for j in range(ell)]
                free=available&~F;sub=free
                while True:
                    target=F|sub;all_hosts+=1
                    assert 1<=target.bit_count()<=7
                    if target not in fixed:
                        next_var+=1;y=next_var;witness_count+=1
                        selectors[target].append(y)
                        witness_map.write(json.dumps([y,target,cid,start,ell])+'\n')
                        # y => every cap on this witness interval is contained in target.
                        for pos in positions:
                            for bit,x in V[pos].items():
                                if not target&bit:clause([-y,-x],'witness_exclusion')
                        # y => every positive target bit appears at least once.
                        pending=target
                        while pending:
                            bit=pending&-pending;pending-=bit
                            if any(P[pos]&bit for pos in positions):continue
                            literals=[V[pos][bit] for pos in positions if D[pos]&bit]
                            assert literals
                            clause([-y]+literals,'witness_inclusion')
                    if sub==0:break
                    sub=(sub-1)&free
assert all_hosts==631992 and triple_count==22134
for target in required:
    assert selectors[target]
    clause(selectors[target],'target_required')
body.close()
cnf=BASE/'unrestricted_triple_caps.cnf'
with cnf.open('w') as dst:
    dst.write(f'p cnf {next_var} {clauses}\n')
    with (BASE/'formula_body.tmp').open() as src:shutil.copyfileobj(src,dst,1024*1024)
(BASE/'formula_body.tmp').unlink()
metadata=dict(scope='All overlapping caps on every H3 position of the fixed canonical bank; H1/H2 frozen; no anchors.',
    source_sha256=hashlib.sha256(source_raw).hexdigest(),variables=next_var,cap_variables=cap_count,
    witness_variables=witness_count,clauses=clauses,clause_families=dict(family_counts),
    clause_length_histogram=dict(sorted(length_counts.items())),required_lower_targets=len(required),
    frozen_target_masks=sorted(fixed),all_short_hosts=all_hosts,native_triples=triple_count,
    cap_mapping_columns=['variable','cycle','position','coordinate_bit_mask'],
    witness_mapping_columns=['variable','target_mask','cycle','cyclic_start','length'],
    cnf_sha256=sha(cnf),generation_wall_seconds=time.monotonic()-started,
    generation_cpu_seconds=time.process_time()-cpu_started,resource_limits=LIMITS)
dump('formula_metadata.json',metadata)
print('FORMULA',json.dumps({k:v for k,v in metadata.items() if k not in ('frozen_target_masks','clause_length_histogram')}),flush=True)
del selectors;gc.collect()

# Reserve ten aggregate CPU seconds for extraction and direct literal replay.
# The worker's hard CPU limit includes loading the CNF and the one solver call.
parent_used=time.process_time()-cpu_started
solver_cpu=int(110-parent_used)
wall_left=deadline-time.monotonic()-2
if solver_cpu<1 or wall_left<5:finish_inconclusive('formula generation consumed the decision budget')
worker=subprocess.Popen([sys.executable,__file__,'--solver-worker',str(solver_cpu)])
try:worker.wait(timeout=wall_left)
except subprocess.TimeoutExpired:finish_inconclusive('single solver worker reached total wall limit')
child_usage=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=child_usage.ru_utime+child_usage.ru_stime
# Tighten the driver's remaining CPU limit after the child, enforcing <=120
# seconds of aggregate accounted CPU, rather than granting another full budget.
remaining_driver_limit=max(1,int(120-child_cpu))
resource.setrlimit(resource.RLIMIT_CPU,(max(1,remaining_driver_limit-1),remaining_driver_limit))
if worker.returncode!=0 or not (BASE/'solver_result.json').exists():
    finish_inconclusive('single solver worker exited without a decision',dict(worker_returncode=worker.returncode))
result=json.loads((BASE/'solver_result.json').read_text())
if result['result'] is not True:
    report=dict(status='SOLVER_REPORTED_UNSAT_UNCHECKED' if result['result'] is False else 'INCONCLUSIVE',
        scope=metadata['scope'],solver=result,proof_independently_checked=False,
        checker_availability='No DRAT/LRAT checker found on PATH or the inspected common directories; no installation attempted.',
        cnf_sha256=metadata['cnf_sha256'],solver_restarts=0,
        wall_seconds=time.monotonic()-started,aggregate_cpu_seconds=child_cpu+time.process_time()-cpu_started,
        resource_limits=LIMITS)
    dump('decision_report.json',report);print(json.dumps(report),flush=True);sys.exit(0)

model=json.loads((BASE/'solver_model.json').read_text())
truth=bytearray(next_var+1)
for literal in model:
    if literal>0:truth[literal]=1
del model
candidate=[]
for bank in banks:
    D=bank['D'];E=D.copy()
    if bank['H']==3:
        for i in range(len(D)):
            E[i]=bank['pin'][i]
            for bit,x in bank['variables'][i].items():
                if truth[x]:E[i]|=bit
            assert E[i] and E[i]&D[i]==E[i]
        for i in range(len(D)):
            assert E[i]|E[(i+1)%len(E)]|E[(i+2)%len(E)]==D[i]|D[(i+1)%len(D)]|D[(i+2)%len(D)]
    candidate.append(dict(cycle=bank['cycle'],letters=E))
dump('sat_capped_cycle_bank.json',dict(cycles=candidate))
print('SAT_CANDIDATE_SAVED',str(BASE/'sat_capped_cycle_bank.json'),flush=True)

# Actual cyclic target census, followed by independent range-OR witness replay.
witnesses={};trees={};periods={}
for bank in candidate:
    cid=bank['cycle'];word=bank['letters'];v=len(word);double=word+word;periods[cid]=v
    suffix={}
    for end in range(2*v-1):
        current={double[end]:end};cutoff=end-v+1
        for target,start in suffix.items():
            if start>=cutoff:
                value=target|double[end]
                if start>current.get(value,-1):current[value]=start
        suffix=current
        if end>=v-1:
            for target,start in current.items():witnesses.setdefault(target,(cid,start,end))
    size=1
    while size<len(double):size*=2
    tree=[0]*(2*size);tree[size:size+len(double)]=double
    for i in range(size-1,0,-1):tree[i]=tree[2*i]|tree[2*i+1]
    trees[cid]=(size,tree)
assert len(witnesses)==FULL and all(1<=t<=FULL for t in witnesses)
for target,(cid,start,end) in witnesses.items():
    assert 0<=start<=end<2*periods[cid] and end-start+1<=periods[cid]
    size,tree=trees[cid];left=start+size;right=end+1+size;value=0
    while left<right:
        if left&1:value|=tree[left];left+=1
        if right&1:right-=1;value|=tree[right]
        left//=2;right//=2
    assert value==target
dump('sat_all_cyclic_target_witnesses.json',{str(t):witnesses[t] for t in sorted(witnesses)})
report=dict(status='SAT_BANK_FULL_CYCLIC_COVERAGE_VERIFIED',scope=metadata['scope'],
    cycles=len(candidate),total_period_positions=sum(len(c['letters']) for c in candidate),
    distinct_cyclic_targets=len(witnesses),independent_range_or_witnesses_replayed=len(witnesses),
    all_letters_nonempty=True,all_native_triples_preserved=True,H1_H2_frozen=True,
    bank_sha256=sha(BASE/'sat_capped_cycle_bank.json'),cnf_sha256=metadata['cnf_sha256'],solver=result,
    solver_restarts=0,wall_seconds=time.monotonic()-started,
    aggregate_cpu_seconds=child_cpu+time.process_time()-cpu_started,
    no_linear_word_claim=True,resource_limits=LIMITS)
dump('decision_report.json',report);print(json.dumps(report),flush=True)
