#!/usr/bin/env python3
"""Exact pruning-prefix frontiers, complete split logs, and priority-free replay.

One authorized run: full validation at r=1,...,8, then one r=163 target
10000*U<Cat_r attempt. No other r, priority variation, or restart is used.
All mathematical execution is restricted to h100.
"""
import gc
import hashlib
import heapq
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024**3, 1024**3))
signal.alarm(150)
START_WALL = time.monotonic()
START_CPU = time.process_time()
OUT = Path('/home/amodo/exact-b-pbbs-forward-prefix-r163-20260908')
CENSUS = Path('/home/amodo/exact-b-rotation-period-census-20260908/exact_rotation_period_census.json')
CENSUS_SHA = '43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2'
MAX_REFINEMENTS = 10000
MAX_GENERATED_NODES = 1000000
# Reserve the remaining hard budget for serializing and replaying a valid
# stopping frontier. Reaching a soft limit does not discard any leaf.
BUILD_CPU_SECONDS = 65
BUILD_WALL_SECONDS = 85
NODE_COLUMNS = ['id', 's', 'a', 'b', 'w', 'P', 'beta_num', 'beta_den',
                'mass', 'height_cap', 'charge_period', 'ceil_charge']


def dump_line(stream, obj):
    stream.write(json.dumps(obj, separators=(',', ':')) + '\n')


def ceil_div(a, b):
    assert a >= 0 and b > 0
    return (a+b-1)//b


def decimal_interval(a, b, places=30):
    scale = 10**places
    q = a*scale//b
    def render(v):
        return str(v//scale)+'.'+str(v % scale).zfill(places)
    return dict(numerator=a, denominator=b, lower=render(q), upper=render(q+1),
                decimal_places=places)


@lru_cache(None)
def K(a, b):
    assert a >= 1 and 0 <= b < a
    product = math.comb(a, b)*math.comb(a, b+1)
    assert product % a == 0
    return product//a


@lru_cache(None)
def divisors(p):
    return tuple(d for d in range(1, p+1) if p % d == 0)


@lru_cache(None)
def row_classes(p, ell):
    """Exact counts of ordered rows with least cyclic period d; no quotient."""
    assert p >= 1 and p % 2 == 1 and ell >= 0
    counts = {}
    for d in divisors(p):
        repeats = p//d
        fixed = math.comb(ell//repeats+d-1, d-1) if ell % repeats == 0 else 0
        exact = fixed-sum(count for q, count in counts.items() if d % q == 0)
        assert exact >= 0
        counts[d] = exact
    assert sum(counts.values()) == math.comb(ell+p-1, p-1)
    if p == 1 or ell == 0:
        assert [(d,c) for d,c in counts.items() if c] == [(1,1)]
    return tuple((d,c) for d,c in counts.items() if c)


def next_beta(a, b, num, den):
    new_num = den+(2*b+1)*num
    new_den = (2*a+1)*den
    g = math.gcd(new_num, new_den)
    return new_num//g, new_den//g


def divided_denominator(num, den, d):
    assert math.gcd(num, den) == 1 and d >= 1
    return den*d//math.gcd(num, d)


@dataclass(slots=True)
class Node:
    id: int
    s: int
    a: int
    b: int
    w: int
    P: int
    beta_num: int
    beta_den: int
    mass: int
    height_cap: int
    charge_period: int
    ceil_charge: int

    def row(self):
        return [self.id,self.s,self.a,self.b,self.w,self.P,self.beta_num,self.beta_den,
                self.mass,self.height_cap,self.charge_period,self.ceil_charge]


def make_node(node_id, s, a, b, w, P, beta_num, beta_den, n):
    assert 0 <= b < a and w >= 1 and P % n == 0
    assert math.gcd(beta_num,beta_den) == 1 and beta_den >= 1 and beta_num >= 0
    mass = w*K(a,b)
    H = s+b+1
    effective_P = P
    if b == 0:
        # The incoming final row has one slot, total mass a, least period 1.
        # Keep beta_s and P_s in the state, but charge with the completed period.
        final_num, final_den = next_beta(a,0,beta_num,beta_den)
        assert final_num > 0
        effective_P = math.lcm(P,final_den)
    charge = ceil_div(mass*(2*H-1),effective_P)
    assert effective_P % P == 0 and effective_P % 2 == 1
    return Node(node_id,s,a,b,w,P,beta_num,beta_den,mass,H,effective_P,charge)


def child_specifications(parent):
    assert parent.b > 0
    specs = []
    b = parent.b
    beta_num,beta_den = next_beta(parent.a,b,parent.beta_num,parent.beta_den)
    for c in range(max(0,2*b-parent.a),b):
        ell = parent.a-2*b+c
        for d,count in row_classes(2*b+1,ell):
            P = math.lcm(parent.P,divided_denominator(beta_num,beta_den,d))
            specs.append((parent.s+1,b,c,parent.w*count,P,beta_num,beta_den))
    assert specs
    return specs


class Frontier:
    def __init__(self,r,directory):
        self.r=r
        self.n=2*r+1
        self.cat=math.comb(2*r,r)//(r+1)
        self.directory=directory
        directory.mkdir()
        self.active={}
        self.heap=[]
        self.next_id=0
        for b in range(r):
            node=make_node(self.next_id,0,r,b,1,self.n,0,1,self.n)
            self.active[node.id]=node
            if b:
                heapq.heappush(self.heap,(-node.ceil_charge,node.id))
            self.next_id+=1
        self.U=sum(node.ceil_charge for node in self.active.values())
        self.mass=sum(node.mass for node in self.active.values())
        assert self.mass==self.cat
        self.refinements=0
        self.rounded_increases=0
        self.max_depth=0
        self.stream=(directory/'splits.jsonl').open('w')
        dump_line(self.stream,dict(kind='initialize',r=r,n=self.n,catalan=self.cat,
            root_count=r,initial_U=self.U,node_columns=NODE_COLUMNS,
            priority='largest integer ceil charge; smallest node id breaks ties'))

    def split(self,parent,specs):
        assert parent.id in self.active and parent.b>0
        first_id=self.next_id
        children=[]
        for spec in specs:
            child=make_node(self.next_id,*spec,self.n)
            self.next_id+=1
            assert child.charge_period % parent.charge_period==0
            assert child.height_cap<=parent.height_cap
            # This per-root charge domination plus exact child mass summation
            # proves the unrounded split inequality, without large aggregate LCMs.
            assert ((2*child.height_cap-1)*parent.charge_period
                    <= (2*parent.height_cap-1)*child.charge_period)
            children.append(child)
        child_mass=sum(node.mass for node in children)
        child_U=sum(node.ceil_charge for node in children)
        assert child_mass==parent.mass
        if child_U>parent.ceil_charge:
            self.rounded_increases+=1
        self.U+=child_U-parent.ceil_charge
        self.mass+=child_mass-parent.mass
        assert self.mass==self.cat
        del self.active[parent.id]
        for child in children:
            self.active[child.id]=child
            if child.b:
                heapq.heappush(self.heap,(-child.ceil_charge,child.id))
            self.max_depth=max(self.max_depth,child.s)
        self.refinements+=1
        dump_line(self.stream,dict(kind='split',parent_id=parent.id,first_child_id=first_id,
            child_count=len(children),child_mass=child_mass,child_ceil_sum=child_U,
            frontier_U=self.U,frontier_mass=self.mass))

    def finish(self,reason,D=None):
        self.stream.flush()
        self.stream.close()
        fresh_mass=sum(node.mass for node in self.active.values())
        fresh_U=sum(node.ceil_charge for node in self.active.values())
        assert fresh_mass==self.cat and fresh_U==self.U
        with (self.directory/'final_leaves.jsonl').open('w') as stream:
            for node_id in sorted(self.active):
                dump_line(stream,self.active[node_id].row())
        result=dict(r=self.r,n=self.n,catalan=self.cat,width=self.n*self.cat,
            reason=reason,U=self.U,relative_overhead_upper=decimal_interval(self.U,self.cat),
            construction_overhead_integer_upper=self.n*self.U,
            word_length_integer_upper=self.n*(self.cat+self.U),
            frontier_mass=fresh_mass,frontier_leaf_count=len(self.active),
            nonterminal_leaf_count=sum(bool(node.b) for node in self.active.values()),
            terminal_leaf_count=sum(not node.b for node in self.active.values()),
            generated_nodes=self.next_id,refinements=self.refinements,
            rounded_charge_increases=self.rounded_increases,max_depth=self.max_depth,
            every_split_exact_mass_conserving=True,
            every_split_unrounded_charge_nonincreasing=True,
            rounded_U_freshly_summed=True,terminal_final_row_included=True)
        if D is not None:
            result.update(reciprocal_error_target=D,target_certified=D*self.U<self.cat,
                          exact_target_margin=self.cat-D*self.U)
        return result


# This replay reads the chosen parent-id transcript; it never reconstructs or
# assumes the priority queue. It uses Fraction for beta and terminal updates,
# and independently reconstructs all children and final leaf charges.
@lru_cache(None)
def replay_row_classes(p,ell):
    divs=[d for d in range(1,p+1) if p%d==0]
    exact=[]
    for d in divs:
        repetition=p//d
        count=0
        if ell%repetition==0:
            count=math.comb(ell//repetition+d-1,d-1)
        for e,previous in exact:
            if d%e==0:
                count-=previous
        assert count>=0
        exact.append((d,count))
    assert sum(c for d,c in exact)==math.comb(ell+p-1,p-1)
    return tuple((d,c) for d,c in exact if c)


def replay_derived(state,n):
    s,a,b,w,P,num,den=state
    assert a>0 and 0<=b<a and w>0 and P%n==0
    beta=Fraction(num,den)
    assert (beta.numerator,beta.denominator)==(num,den)
    numerator=math.comb(a,b)*math.comb(a,b+1)
    assert numerator%a==0
    mass=w*(numerator//a)
    H=s+b+1
    effective=P
    if b==0:
        final_beta=(1+beta)/(2*a+1)
        effective=math.lcm(P,final_beta.denominator)
    charge=(mass*(2*H-1)+effective-1)//effective
    return mass,H,effective,charge


def replay_frontier(directory,expected):
    with (directory/'splits.jsonl').open() as stream:
        header=json.loads(next(stream))
        assert header['kind']=='initialize'
        r=header['r'];n=2*r+1;cat=math.comb(2*r,r)//(r+1)
        assert header['n']==n and header['catalan']==cat
        active={b:(0,r,b,1,n,0,1) for b in range(r)}
        next_id=r
        mass=sum(replay_derived(state,n)[0] for state in active.values())
        U=sum(replay_derived(state,n)[3] for state in active.values())
        assert mass==cat and U==header['initial_U']
        splits=0
        for line in stream:
            event=json.loads(line)
            assert event['kind']=='split'
            parent_id=event['parent_id']
            state=active.pop(parent_id)
            s,a,b,w,P,num,den=state
            assert b>0 and event['first_child_id']==next_id
            parent_mass,parent_H,parent_period,parent_charge=replay_derived(state,n)
            beta_next=(1+(2*b+1)*Fraction(num,den))/(2*a+1)
            children=[]
            for c in range(max(0,2*b-a),b):
                for d,count in replay_row_classes(2*b+1,a-2*b+c):
                    new_period=math.lcm(P,(beta_next/d).denominator)
                    child=(s+1,b,c,w*count,new_period,beta_next.numerator,beta_next.denominator)
                    children.append(child)
            child_mass=child_U=0
            for child in children:
                cm,ch,cp,cu=replay_derived(child,n)
                assert cp%parent_period==0 and ch<=parent_H
                assert (2*ch-1)*parent_period <= (2*parent_H-1)*cp
                active[next_id]=child
                next_id+=1
                child_mass+=cm;child_U+=cu
            assert child_mass==parent_mass==event['child_mass']
            assert child_U==event['child_ceil_sum'] and len(children)==event['child_count']
            mass+=child_mass-parent_mass
            U+=child_U-parent_charge
            assert mass==cat==event['frontier_mass'] and U==event['frontier_U']
            splits+=1
    assert next_id==expected['generated_nodes'] and splits==expected['refinements']
    final_count=final_mass=final_U=0
    # Pop every recorded final leaf once, so duplicates and omissions both fail.
    with (directory/'final_leaves.jsonl').open() as stream:
        for line in stream:
            row=json.loads(line)
            node_id=row[0]
            state=active.pop(node_id)
            s,a,b,w,P,num,den=state
            derived=replay_derived(state,n)
            assert row==[node_id,s,a,b,w,P,num,den,*derived]
            final_count+=1;final_mass+=derived[0];final_U+=derived[3]
    assert not active
    assert final_count==expected['frontier_leaf_count']
    assert final_mass==cat==expected['frontier_mass']
    assert final_U==U==expected['U']
    return dict(status='PASS',priority_order_not_used=True,
        every_recorded_split_completely_regenerated=True,
        replayed_splits=splits,replayed_generated_nodes=next_id,
        final_leaf_count=final_count,final_mass=final_mass,final_U=final_U,
        final_leaf_records_all_checked=True)


def validate_small_r(r,reference):
    directory=OUT/('validation_r%03d'%r)
    frontier=Frontier(r,directory)
    while frontier.heap:
        _,node_id=heapq.heappop(frontier.heap)
        parent=frontier.active[node_id]
        frontier.split(parent,child_specifications(parent))
    result=frontier.finish('FULL_EXACT_CENSUS')
    assert result['nonterminal_leaf_count']==0
    raw_charge=Fraction(0)
    cycles=height_sum=overhead=0
    periods=Counter();heights=Counter()
    for node in frontier.active.values():
        assert node.b==0 and node.mass==node.w
        assert frontier.n*node.mass%node.charge_period==0
        count=frontier.n*node.mass//node.charge_period
        raw_charge+=Fraction(node.mass*(2*node.height_cap-1),node.charge_period)
        cycles+=count;height_sum+=node.height_cap*count
        overhead+=(2*node.height_cap-1)*count
        periods[node.charge_period]+=count;heights[node.height_cap]+=count
    assert frontier.n*raw_charge==overhead==reference['overhead']
    assert cycles==reference['cycles'] and height_sum==reference['height_sum']
    assert len(frontier.active)==reference['least_period_signature_count']
    assert dict(periods)=={int(k):v for k,v in reference['cycle_counts_by_period'].items()}
    assert dict(heights)=={int(k):v for k,v in reference['cycle_counts_by_height'].items()}
    result.update(exact_native_overhead=overhead,exact_cycles=cycles,exact_height_sum=height_sum,
        exact_unrounded_charge=[raw_charge.numerator,raw_charge.denominator],
        complete_signature_count_matches=True,all_period_and_height_histograms_match=True,
        rounded_U_not_assumed_equal_to_exact_charge=True)
    del frontier
    gc.collect()
    result['replay']=replay_frontier(directory,result)
    (directory/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


def attempt_r163():
    r=163;D=10000
    directory=OUT/'attempt_r163'
    frontier=Frontier(r,directory)
    while True:
        if D*frontier.U<frontier.cat:
            reason='TARGET_CERTIFIED';break
        if not frontier.heap:
            reason='FULL_EXACT_CENSUS_TARGET_NOT_CERTIFIED_BY_ROUNDED_U';break
        if frontier.refinements>=MAX_REFINEMENTS:
            reason='REFINEMENT_CAP';break
        if time.process_time()-START_CPU>=BUILD_CPU_SECONDS:
            reason='BUILD_CPU_RESERVE';break
        if time.monotonic()-START_WALL>=BUILD_WALL_SECONDS:
            reason='BUILD_WALL_RESERVE';break
        _,node_id=frontier.heap[0]
        parent=frontier.active[node_id]
        specs=child_specifications(parent)
        if frontier.next_id+len(specs)>MAX_GENERATED_NODES:
            reason='GENERATED_NODE_CAP';break
        heapq.heappop(frontier.heap)
        frontier.split(parent,specs)
        if frontier.refinements%100==0:
            print('PROGRESS',json.dumps(dict(r=r,refinements=frontier.refinements,
                nodes=frontier.next_id,leaves=len(frontier.active),
                relative_upper=decimal_interval(frontier.U,frontier.cat,12),
                elapsed_cpu_seconds=time.process_time()-START_CPU)),flush=True)
    result=frontier.finish(reason,D)
    print('VALID_STOPPING_FRONTIER',json.dumps({k:result[k] for k in
        ('r','reason','U','catalan','target_certified','refinements','generated_nodes',
         'frontier_leaf_count','relative_overhead_upper')}),flush=True)
    (directory/'pre_replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    del frontier
    gc.collect()
    result['replay']=replay_frontier(directory,result)
    (directory/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


def run():
    OUT.mkdir(exist_ok=False)
    raw=CENSUS.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==CENSUS_SHA
    old=json.loads(raw)
    by_r={row['r']:row for row in old['rows']}
    validations=[]
    for r in range(1,9):
        result=validate_small_r(r,by_r[r])
        validations.append(result)
        print('VALIDATION_PASS',json.dumps(dict(r=r,overhead=result['exact_native_overhead'],
            cycles=result['exact_cycles'],refinements=result['refinements'],
            generated_nodes=result['generated_nodes'])),flush=True)
    attempt=attempt_r163()
    report=dict(status=('PASS_TARGET_CERTIFICATE' if attempt['target_certified']
                        else 'VALID_UPPER_BOUND_AT_FIXED_STOP'),
        scope='Independent small-r validation and one fixed r=163 prefix-frontier attempt only; not the user-reported 713-case band.',
        source_census_sha256=CENSUS_SHA,small_r_validations=validations,r163=attempt,
        exact_mass_partition=True,integer_ceiling_semantics=True,
        terminal_final_row_included=True,priority_free_replay_complete=True,
        limits=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3,
            maximum_refinements=MAX_REFINEMENTS,maximum_generated_nodes=MAX_GENERATED_NODES,
            build_cpu_reserve_cutoff=BUILD_CPU_SECONDS,build_wall_reserve_cutoff=BUILD_WALL_SECONDS),
        elapsed_wall_seconds=time.monotonic()-START_WALL,
        elapsed_cpu_seconds=time.process_time()-START_CPU)
    (OUT/'forward_prefix_r163_complete_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINAL',json.dumps(dict(status=report['status'],r=163,
        target_certified=attempt['target_certified'],U=attempt['U'],catalan=attempt['catalan'],
        margin=attempt['exact_target_margin'],relative_upper=attempt['relative_overhead_upper'],
        refinements=attempt['refinements'],generated_nodes=attempt['generated_nodes'],
        replay=attempt['replay']['status'],elapsed_wall_seconds=report['elapsed_wall_seconds'],
        elapsed_cpu_seconds=report['elapsed_cpu_seconds'])),flush=True)


if __name__=='__main__':
    try:
        run()
    except MemoryError:
        if OUT.is_dir():
            (OUT/'resource_failure.json').write_text(json.dumps(dict(
                status='INCONCLUSIVE_MEMORY_LIMIT',complete_replay_not_claimed=True,
                elapsed_wall_seconds=time.monotonic()-START_WALL))+'\n')
        raise
