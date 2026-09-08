#!/usr/bin/env python3
"""Independent exact height-moment audit and ONE fully replayed r=68 frontier.

No supplied verifier is imported. No finite-band enumeration, sparse omitted
families, approximate symmetry correction, word search, or retry is performed.
"""
import gc
import hashlib
import heapq
import itertools
import json
import math
import resource
import signal
import socket
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
resource.setrlimit(resource.RLIMIT_FSIZE,(512*1024**2,512*1024**2))
signal.alarm(90)
START_CPU=time.process_time()
START_WALL=time.monotonic()
OUT=Path('/home/amodo/exact-b-moment-prefix-structural-and-r68-20260909')
REFERENCE=Path('/home/amodo/exact-b-rotation-period-census-20260908/exact_rotation_period_census.json')
REFERENCE_SHA='43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2'
MAX_REFINEMENTS=10000
MAX_NODES=1000000
BUILD_CPU=30
BUILD_WALL=40
KT={}
HT={}


def line(stream,value):
    stream.write(json.dumps(value,separators=(',',':'))+'\n')


def cdiv(a,b):
    assert a>=0 and b>0
    return (a+b-1)//b


def ceil_fraction(value):
    return cdiv(value.numerator,value.denominator)


def enclosure(a,b,places=30):
    scale=10**places;q=a*scale//b
    def render(v):
        return str(v//scale)+'.'+str(v%scale).zfill(places)
    return dict(numerator=a,denominator=b,lower=render(q),upper=render(q+1),places=places)


@lru_cache(None)
def divisors(p):
    return tuple(d for d in range(1,p+1) if p%d==0)


@lru_cache(None)
def classes(p,ell):
    result={}
    for d in divisors(p):
        e=p//d
        fixed=math.comb(ell//e+d-1,d-1) if ell%e==0 else 0
        count=fixed-sum(c for q,c in result.items() if d%q==0)
        assert count>=0
        result[d]=count
    assert sum(result.values())==math.comb(ell+p-1,p-1)
    if p==1 or ell==0:
        assert [(d,c) for d,c in result.items() if c]==[(1,1)]
    return tuple((d,c) for d,c in result.items() if c)


def height_table():
    with (OUT/'exact_height_table_through100.jsonl').open('w') as stream:
        for a in range(1,101):
            for b in range(a):
                numerator=math.comb(a,b)*math.comb(a,b+1)
                assert numerator%a==0
                KT[a,b]=numerator//a
                if b==0:
                    HT[a,b]=1
                else:
                    lo=max(0,2*b-a)
                    coefficient=math.comb(a+lo,2*b)
                    mass=0;height=0
                    for c in range(lo,b):
                        mass+=coefficient*KT[b,c]
                        height+=coefficient*HT[b,c]
                        if c+1<b:
                            top=coefficient*(a+c+1)
                            bottom=a+c+1-2*b
                            assert top%bottom==0
                            coefficient=top//bottom
                    assert mass==KT[a,b]
                    HT[a,b]=mass+height
                assert KT[a,b]<=HT[a,b]<=(b+1)*KT[a,b]
                line(stream,[a,b,KT[a,b],HT[a,b]])
            assert sum(KT[a,b] for b in range(a))==math.comb(2*a,a)//(a+1)
    mean=enclosure(HT[100,50],KT[100,50])
    nearest_eight=(2*HT[100,50]*10**8+KT[100,50])//(2*KT[100,50])
    assert abs(HT[100,50]*10**8-1642824502*KT[100,50])<KT[100,50]
    return dict(cells=len(KT),maximum_a=100,
        illustrative_H100_50=HT[100,50],illustrative_K100_50=KT[100,50],
        illustrative_conditional_mean=mean,nearest_eight_decimal_scaled=nearest_eight,
        supplied_illustration_within_one_unit_in_eighth_decimal=True,
        old_class_height_cap=51,all_mass_identities_checked=True)


def dyck_words(a):
    def generate(prefix,up,down):
        if up==down==a:
            yield tuple(prefix);return
        if up<a:
            prefix.append(1)
            yield from generate(prefix,up+1,down)
            prefix.pop()
        if down<up:
            prefix.append(0)
            yield from generate(prefix,up,down+1)
            prefix.pop()
    yield from generate([],0,0)


def dyck_checks():
    roots={0:{():0}}
    total=0;rows=[]
    for a in range(1,11):
        root_heights={};counts=Counter();height_sums=Counter()
        for word in dyck_words(a):
            balance=height=0
            for bit in word:
                balance+=1 if bit else -1
                assert balance>=0
                height=max(height,balance)
            assert balance==0
            pruned=[];i=0
            while i<len(word):
                if i+1<len(word) and word[i:i+2]==(1,0):
                    i+=2
                else:
                    pruned.append(word[i]);i+=1
            b=len(pruned)//2
            assert len(pruned)==2*b and b<a
            assert tuple(pruned) in roots[b]
            assert height==roots[b][tuple(pruned)]+1
            counts[b]+=1;height_sums[b]+=height;root_heights[word]=height
        roots[a]=root_heights
        assert len(root_heights)==math.comb(2*a,a)//(a+1)
        for b in range(a):
            assert counts[b]==KT[a,b] and height_sums[b]==HT[a,b]
        rows.append(dict(a=a,roots=len(root_heights),height_sum=sum(height_sums.values()),
                         all_pruning_classes_match=True))
        total+=len(root_heights)
    assert total==23713
    return roots,dict(total_nonempty_dyck_roots=total,through_semilength=10,
        every_pruning_class_count_and_height_total_exact=True,
        every_pruning_step_lowers_height_by_one=True,rows=rows)


def reflection_checks(roots):
    total_bridges=0;bridge_rows=[]
    for a in range(1,10):
        n=2*a+1;maximum=Counter();negative_minimum=Counter();root_frequency=Counter()
        for positions in itertools.combinations(range(n),a):
            word=[0]*n
            for i in positions:word[i]=1
            balance=hi=lo=0;first_minimum=0
            for i,bit in enumerate(word):
                balance+=1 if bit else -1
                hi=max(hi,balance)
                if balance<lo:
                    lo=balance;first_minimum=i+1
            assert balance==-1
            rotated=word[first_minimum:]+word[:first_minimum]
            assert rotated[-1]==0
            root=tuple(rotated[:-1])
            assert root in roots[a]
            assert roots[a][root]<=hi-lo
            root_frequency[root]+=1;maximum[hi]+=1;negative_minimum[-lo]+=1
        assert set(root_frequency.values())=={n}
        assert len(root_frequency)==len(roots[a])
        def choose(k):
            return math.comb(n,k) if 0<=k<=n else 0
        for j in range(a+3):
            assert sum(c for x,c in maximum.items() if x>=j)==choose(a-j)
            assert sum(c for x,c in negative_minimum.items() if x>=j)==choose(a+1-j)
        count=sum(maximum.values())
        assert count==math.comb(n,a)
        total_bridges+=count
        bridge_rows.append(dict(a=a,bridges=count,all_root_rotation_fibres_have_size=n,
            both_reflection_tail_formulas_exact=True))
    assert total_bridges==125475
    tail_cases=class_cases=0
    for a in range(1,101):
        n=2*a+1
        cumulative=[];running=0
        for j in range(a+1):
            running+=math.comb(n,j);cumulative.append(running)
        for t in range(a):
            j=a-t
            B=Fraction(cumulative[j]+cumulative[j-1],n)
            G=geometric_tail(a,t)
            assert B<=G
            for b in range(a):
                assert HT[a,b]<=2*t*KT[a,b]+B
                class_cases+=1
            if a<=10:
                exact_excess=sum(max(0,h-2*t) for h in roots[a].values())
                assert exact_excess<=B
            tail_cases+=1
        cat=math.comb(2*a,a)//(a+1)
        for b in range(a):
            q=0
            while (1<<q)*KT[a,b]<cat:q+=1
            t=math.isqrt((a+1)*(q+2))+1
            bound=(b+1)*KT[a,b]
            if t<a:
                bound=min(bound,2*t*KT[a,b]+ceil_fraction(geometric_tail(a,t)))
            assert HT[a,b]<=bound<=(b+1)*KT[a,b]
    return dict(middle_bridges_through_semilength9=total_bridges,bridge_rows=bridge_rows,
        rational_binomial_tail_cases=tail_cases,conditional_height_tail_comparisons=class_cases,
        all_geometric_tail_bounds_pass=True,all_heuristic_integer_Hhat_caps_pass=True)


def geometric_tail(a,t):
    assert 0<=t<a
    return Fraction(math.comb(2*a+1,a-t),2*a+1)*(
        Fraction(a+t+2,2*t+2)+Fraction((a-t)*(a+t+3),(a+t+2)*(2*t+4)))


def weak_compositions(total,p):
    if p==1:
        yield (total,);return
    for first in range(total+1):
        for tail in weak_compositions(total-first,p-1):
            yield (first,)+tail


def ordered_row_checks():
    keys=set()
    for a in range(2,10):
        for b in range(1,a):
            for c in range(max(0,2*b-a),b):
                keys.add((2*b+1,a-2*b+c))
    vectors=0
    for p,ell in sorted(keys):
        counted=Counter()
        for row in weak_compositions(ell,p):
            d=next(d for d in divisors(p) if all(row[i]==row[i%d] for i in range(p)))
            counted[d]+=1;vectors+=1
        assert dict(counted)==dict(classes(p,ell))
    return dict(distinct_slot_mass_cases=len(keys),composition_vectors=vectors,
        every_direct_minimal_period_histogram_matches=True,source_a_through=9)


@lru_cache(None)
def row_moments(a,b):
    assert b>0
    result=defaultdict(lambda:[0,0])
    for c in range(max(0,2*b-a),b):
        for d,count in classes(2*b+1,a-2*b+c):
            result[d][0]+=count*KT[b,c]
            result[d][1]+=count*HT[b,c]
    assert sum(M for M,R in result.values())==KT[a,b]
    assert sum(R for M,R in result.values())==HT[a,b]-KT[a,b]
    return tuple((d,M,R) for d,(M,R) in sorted(result.items()))


def beta_update(a,b,num,den):
    numerator=den+(2*b+1)*num;denominator=(2*a+1)*den
    common=math.gcd(numerator,denominator)
    return numerator//common,denominator//common


def period_after(P,num,den,d):
    return math.lcm(P,den*d//math.gcd(num,d))


def derive(state,n,check_identity=False):
    s,a,b,w,P,num,den=state
    assert 0<=b<a<=100 and w>0 and P%n==0 and math.gcd(num,den)==1
    mass=w*KT[a,b]
    effective=P
    if b==0:
        bn,bd=beta_update(a,0,num,den)
        effective=math.lcm(P,bd)
    old=cdiv(mass*(2*s+2*b+1),effective)
    moment_numerator=w*((2*s-1)*KT[a,b]+2*HT[a,b])
    moment_exact=Fraction(moment_numerator,effective)
    if b==0:
        integrated=moment_exact
    else:
        bn,bd=beta_update(a,b,num,den)
        moments=row_moments(a,b)
        integrated=sum((Fraction(w*((2*s+1)*M+2*R),period_after(P,bn,bd,d))
                        for d,M,R in moments),Fraction(0))
        assert integrated<=moment_exact
        if check_identity:
            primitive_period=period_after(P,bn,bd,2*b+1)
            correction=Fraction(0)
            for d,M,R in moments:
                Pd=period_after(P,bn,bd,d)
                assert primitive_period%Pd==0
                if d<2*b+1:
                    correction+=w*((2*s+1)*M+2*R)*(Fraction(1,Pd)-Fraction(1,primitive_period))
            assert integrated==Fraction(moment_numerator,primitive_period)+correction
            assert correction>=0
    moment=ceil_fraction(moment_exact)
    one_row=ceil_fraction(integrated)
    assert one_row<=moment<=old
    return mass,effective,old,moment,one_row,one_row


def child_states(state):
    s,a,b,w,P,num,den=state
    assert b>0
    bn,bd=beta_update(a,b,num,den)
    return [(s+1,b,c,w*count,period_after(P,bn,bd,d),bn,bd)
            for c in range(max(0,2*b-a),b)
            for d,count in classes(2*b+1,a-2*b+c)]


def small_prefix_checks(reference):
    rows=[];prefixes=0;identities=0
    for r in range(1,10):
        n=2*r+1
        states=[(0,r,b,1,n,0,1) for b in range(r)]
        terminals=[]
        while states:
            state=states.pop();prefixes+=1
            derived=derive(state,n,True)
            s,a,b,w,P,num,den=state
            if b:
                identities+=1
                children=child_states(state)
                assert sum(derive(child,n)[0] for child in children)==derived[0]
                states.extend(children)
            else:
                terminals.append((state,derived))
        assert sum(d[0] for state,d in terminals)==reference[r]['catalan']
        exact=Fraction(0);cycles=0;heights=Counter();periods=Counter()
        for state,d in terminals:
            s,a,b,w,P,num,den=state
            v=d[1];h=s+1
            assert n*w%v==0
            count=n*w//v
            exact+=Fraction(w*(2*h-1),v)
            cycles+=count;heights[h]+=count;periods[v]+=count
        assert n*exact==reference[r]['overhead']
        assert cycles==reference[r]['cycles']
        assert dict(heights)=={int(k):v for k,v in reference[r]['cycle_counts_by_height'].items()}
        assert dict(periods)=={int(k):v for k,v in reference[r]['cycle_counts_by_period'].items()}
        rows.append(dict(r=r,terminal_classes=len(terminals),cycles=cycles,
                         native_overhead=reference[r]['overhead'],all_comparisons_exact=True))
    return dict(prefix_states=prefixes,integrated_period_correction_identities=identities,
        every_integrated_charge_at_most_moment_charge=True,
        complete_small_period_height_histograms_match=True,rows=rows)


@dataclass(slots=True)
class Node:
    id:int
    state:tuple
    data:tuple

    def row(self):
        return [self.id,*self.state,*self.data]


def replay_derive(state,n):
    """Independent Fraction updates and direct c/d height-weight summation."""
    s,a,b,w,P,num,den=state
    assert 0<=b<a<=100 and w>0 and P%n==0
    beta=Fraction(num,den)
    assert (beta.numerator,beta.denominator)==(num,den)
    numerator=math.comb(a,b)*math.comb(a,b+1)
    assert numerator%a==0
    K=numerator//a;mass=w*K
    effective=P
    if b==0:effective=math.lcm(P,((1+beta)/(2*a+1)).denominator)
    old=cdiv(mass*(2*s+2*b+1),effective)
    moment=Fraction(w*((2*s-1)*K+2*HT[a,b]),effective)
    if b==0:
        integrated=moment
    else:
        bn=(1+(2*b+1)*beta)/(2*a+1)
        contributions=defaultdict(int)
        for c in range(max(0,2*b-a),b):
            # Recompute weak-composition divisor inversion in replay.
            p=2*b+1;ell=a-2*b+c;counts={}
            for d in divisors(p):
                repeats=p//d
                count=math.comb(ell//repeats+d-1,d-1) if ell%repeats==0 else 0
                count-=sum(value for e,value in counts.items() if d%e==0)
                assert count>=0;counts[d]=count
                if count:
                    period=math.lcm(P,(bn/d).denominator)
                    contributions[period]+=w*count*((2*s+1)*KT[b,c]+2*HT[b,c])
            assert sum(counts.values())==math.comb(ell+p-1,p-1)
        integrated=sum((Fraction(value,period) for period,value in contributions.items()),Fraction(0))
    assert integrated<=moment
    result=(mass,effective,old,ceil_fraction(moment),ceil_fraction(integrated),ceil_fraction(integrated))
    assert result[5]<=result[3]<=result[2]
    return result


def replay_frontier(directory,expected):
    with (directory/'splits.jsonl').open() as stream:
        header=json.loads(next(stream));r=header['r'];n=2*r+1
        assert r==68 and header['kind']=='initialize'
        cat=math.comb(2*r,r)//(r+1)
        assert header['catalan']==cat
        active={b:(0,r,b,1,n,0,1) for b in range(r)}
        mass=sum(replay_derive(state,n)[0] for state in active.values())
        U=sum(replay_derive(state,n)[5] for state in active.values())
        assert mass==cat and U==header['U']
        next_id=r;refinements=0
        for raw in stream:
            event=json.loads(raw)
            assert event['kind']=='split' and event['first_child_id']==next_id
            state=active.pop(event['parent'])
            parent_data=replay_derive(state,n)
            s,a,b,w,P,num,den=state
            assert b>0
            beta_next=(1+(2*b+1)*Fraction(num,den))/(2*a+1)
            child_mass=child_cost=child_count=0
            for c in range(max(0,2*b-a),b):
                p=2*b+1;ell=a-2*b+c;counts={}
                for d in divisors(p):
                    repeat=p//d
                    fixed=math.comb(ell//repeat+d-1,d-1) if ell%repeat==0 else 0
                    count=fixed-sum(v for q,v in counts.items() if d%q==0)
                    assert count>=0;counts[d]=count
                    if not count:continue
                    newP=math.lcm(P,(beta_next/d).denominator)
                    child=(s+1,b,c,w*count,newP,beta_next.numerator,beta_next.denominator)
                    values=replay_derive(child,n)
                    active[next_id]=child;next_id+=1;child_count+=1
                    child_mass+=values[0];child_cost+=values[5]
                assert sum(counts.values())==math.comb(ell+p-1,p-1)
            assert child_mass==parent_data[0]==event['child_mass']
            assert child_cost==event['child_cost'] and child_count==event['child_count']
            U+=child_cost-parent_data[5]
            assert U==event['U']
            refinements+=1
    final_mass=final_U=leaf_count=0
    with (directory/'final_leaves.jsonl').open() as stream:
        for raw in stream:
            row=json.loads(raw);node_id=row[0]
            state=active.pop(node_id)
            values=replay_derive(state,n)
            assert row==[node_id,*state,*values]
            final_mass+=values[0];final_U+=values[5];leaf_count+=1
    assert not active
    assert final_mass==cat==expected['mass'] and final_U==U==expected['U']
    assert refinements==expected['refinements'] and next_id==expected['generated_nodes']
    assert leaf_count==expected['final_leaves']
    return dict(status='PASS',priority_not_used=True,all_splits_regenerated=True,
        final_mass=final_mass,final_U=final_U,final_leaves=leaf_count,
        refinements=refinements,generated_nodes=next_id)


def r68_attempt():
    directory=OUT/'r68_frontier';directory.mkdir()
    r=68;n=137;D=100000;cat=math.comb(2*r,r)//(r+1)
    active={};heap=[];next_id=0
    for b in range(r):
        state=(0,r,b,1,n,0,1);data=derive(state,n)
        node=Node(next_id,state,data);active[next_id]=node
        if b:heapq.heappush(heap,(-data[5],next_id))
        next_id+=1
    U=sum(node.data[5] for node in active.values())
    assert sum(node.data[0] for node in active.values())==cat
    initial_U=U;refinements=0;increases=0
    with (directory/'splits.jsonl').open('w') as stream:
        line(stream,dict(kind='initialize',r=r,catalan=cat,U=U,
            node_columns=['id','s','a','b','w','P','beta_num','beta_den','mass',
                          'charge_period','old_ceil','moment_ceil','integrated_ceil','chosen_ceil'],
            priority='largest chosen integer charge, smallest node id'))
        while True:
            if D*U<cat:reason='TARGET_CERTIFIED';break
            if not heap:reason='ALL_TERMINAL';break
            if refinements>=MAX_REFINEMENTS:reason='REFINEMENT_CAP';break
            if time.process_time()-START_CPU>=BUILD_CPU:reason='BUILD_CPU_RESERVE';break
            if time.monotonic()-START_WALL>=BUILD_WALL:reason='BUILD_WALL_RESERVE';break
            parent=active[heap[0][1]]
            children=child_states(parent.state)
            if next_id+len(children)>MAX_NODES:reason='GENERATED_NODE_CAP';break
            first_id=next_id;prepared=[]
            for state in children:
                node=Node(next_id,state,derive(state,n));prepared.append(node);next_id+=1
            child_mass=sum(node.data[0] for node in prepared)
            child_cost=sum(node.data[5] for node in prepared)
            assert child_mass==parent.data[0]
            heapq.heappop(heap);del active[parent.id]
            if child_cost>parent.data[5]:increases+=1
            U+=child_cost-parent.data[5]
            for node in prepared:
                active[node.id]=node
                if node.state[2]:heapq.heappush(heap,(-node.data[5],node.id))
            refinements+=1
            line(stream,dict(kind='split',parent=parent.id,first_child_id=first_id,
                child_count=len(prepared),child_mass=child_mass,child_cost=child_cost,U=U))
            if refinements%100==0:
                print('R68_PROGRESS',json.dumps(dict(refinements=refinements,nodes=next_id,
                    upper=enclosure(U,cat,12),cpu=time.process_time()-START_CPU)),flush=True)
    fresh_mass=sum(node.data[0] for node in active.values())
    fresh_U=sum(node.data[5] for node in active.values())
    assert fresh_mass==cat and fresh_U==U
    with (directory/'final_leaves.jsonl').open('w') as stream:
        for node_id in sorted(active):line(stream,active[node_id].row())
    result=dict(r=r,n=n,reason=reason,catalan=cat,mass=fresh_mass,U=U,
        initial_U=initial_U,relative_overhead_upper=enclosure(U,cat),
        target_reciprocal=D,target_certified=D*U<cat,exact_target_margin=cat-D*U,
        width=n*cat,word_length_integer_upper=n*(cat+U),refinements=refinements,
        generated_nodes=next_id,final_leaves=len(active),
        unfinished_leaves=sum(bool(node.state[2]) for node in active.values()),
        max_depth=max(node.state[0] for node in active.values()),
        rounded_charge_increases=increases,all_final_rows_freshly_summed=True,
        all_next_size_and_row_period_classes_retained=True,
        exact_height_table_used=True,exact_symmetry_classes_used=True,
        sparse_reserves_used=False)
    (directory/'pre_replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('R68_STOP',json.dumps({k:result[k] for k in
        ('reason','target_certified','U','catalan','relative_overhead_upper','refinements',
         'generated_nodes','final_leaves')}),flush=True)
    del active,heap
    gc.collect()
    result['replay']=replay_frontier(directory,result)
    (directory/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


def run():
    OUT.mkdir(exist_ok=False)
    raw=REFERENCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==REFERENCE_SHA
    reference={row['r']:row for row in json.loads(raw)['rows']}
    table=height_table()
    roots,dyck=dyck_checks()
    reflection=reflection_checks(roots)
    ordered=ordered_row_checks()
    prefixes=small_prefix_checks(reference)
    structural=dict(status='PASS',height_table=table,dyck=dyck,reflection=reflection,
        ordered_rows=ordered,period_integrated_prefix_checks=prefixes,
        inherited_fibre_bijection_scope='The numerical period-height sums use the already audited inverse-pruning fibre; no independent all-dimensional corridor proof is claimed.')
    (OUT/'structural_certificate.json').write_text(json.dumps(structural,indent=2)+'\n')
    print('STRUCTURAL_PASS',json.dumps(dict(mean=table['illustrative_conditional_mean'],
        dyck_roots=dyck['total_nonempty_dyck_roots'],bridges=reflection['middle_bridges_through_semilength9'],
        ordered_rows=ordered,small_prefixes=prefixes['prefix_states'],
        cpu=time.process_time()-START_CPU)),flush=True)
    del roots
    gc.collect()
    attempt=r68_attempt()
    report=dict(status=('PASS_SINGLE_R68_TARGET' if attempt['target_certified']
                        else 'STRUCTURAL_PASS_VALID_SINGLE_FRONTIER_BOUND'),
        scope='Exact structural checks and one r68 attempt only; not the claimed3356-case band or the predecessor r67.',
        reference_census_sha256=REFERENCE_SHA,structural=structural,r68=attempt,
        limits=dict(cpu_seconds=60,wall_seconds=90,address_space_bytes=1024**3,
            max_refinements=MAX_REFINEMENTS,max_generated_nodes=MAX_NODES,
            build_cpu_reserve=BUILD_CPU,build_wall_reserve=BUILD_WALL),
        elapsed_cpu_seconds=time.process_time()-START_CPU,
        elapsed_wall_seconds=time.monotonic()-START_WALL)
    (OUT/'moment_prefix_complete_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINAL',json.dumps(dict(status=report['status'],r=68,
        target_certified=attempt['target_certified'],ratio=attempt['relative_overhead_upper'],
        margin=attempt['exact_target_margin'],refinements=attempt['refinements'],
        generated_nodes=attempt['generated_nodes'],replay=attempt['replay']['status'],
        cpu=report['elapsed_cpu_seconds'],wall=report['elapsed_wall_seconds'])),flush=True)


if __name__=='__main__':
    try:
        run()
    except MemoryError:
        if OUT.is_dir():
            (OUT/'resource_failure.json').write_text(json.dumps(dict(
                status='INCONCLUSIVE_MEMORY_LIMIT',completed_frontier_replay_not_claimed=True))+'\n')
        raise
