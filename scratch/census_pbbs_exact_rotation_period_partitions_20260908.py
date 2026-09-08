#!/usr/bin/env python3
"""Exact odd3..101 profile/signature/cycle census; one deterministic h100 run."""
import hashlib,itertools,json,math,resource,signal,time
from collections import Counter
from functools import lru_cache
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(300,300))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.alarm(360)
started=time.monotonic()
OUT=Path('/home/amodo/exact-b-rotation-period-census-20260908');OUT.mkdir(exist_ok=True)

@lru_cache(None)
def divisors(p):return tuple(d for d in range(1,p+1) if p%d==0)

@lru_cache(None)
def row_classes(p,ell):
    chi={}
    for d in divisors(p):
        repeats=p//d
        F=math.comb(ell//repeats+d-1,d-1) if ell%repeats==0 else 0
        value=F-sum(a for q,a in chi.items() if d%q==0)
        assert value>=0
        chi[d]=value
    assert sum(chi.values())==math.comb(ell+p-1,p-1)
    if ell==0:assert {d:a for d,a in chi.items() if a}=={1:1}
    if p==1:assert chi=={1:1}
    return tuple((d,a) for d,a in chi.items() if a)

def partitions(n,ceiling=None,prefix=()):
    if not n:
        yield prefix;return
    ceiling=n if ceiling is None else min(n,ceiling)
    for first in range(ceiling,0,-1):
        yield from partitions(n-first,first,prefix+(first,))

def decimal_enclosure(a,b,places=30):
    scale=10**places;q=a*scale//b
    def text(value):return str(value//scale)+'.'+str(value%scale).zfill(places)
    return dict(numerator=a,denominator=b,decimal_places=places,
                lower=text(q),upper=text(q+1),lower_scaled=q,upper_scaled=q+1)

def endpoint(n,W):
    rank=(n+1)//2
    below=sum(math.comb(n,j) for j in range(1,rank))
    d=0
    while d*W+d*(d+1)//2<below:d+=1
    assert d==0 or (d-1)*W+(d-1)*d//2<below
    return dict(rank=rank,lower_rank_target_count=below,delay=d,B=W+d)

quoted={17:(24310,892),31:(300540195,1355845),41:(269128937220,327229518),
        61:(232714176627630544,33239463842328),
        101:(199804427433372226016001220056,1187277484185535019897550)}
rows=[];total_profiles=0;total_signatures=0;example=None
for r in range(1,51):
    n=2*r+1;W=math.comb(n,r);cat=math.comb(2*r,r)//(r+1)
    profile_count=signature_count=root_total=cycles_total=height_sum=overhead=0
    height_cycles=Counter();period_cycles=Counter()
    for m in partitions(r):
        profile_count+=1;h=len(m);tail=r;nprev=n
        snum=0;sden=1;base_v=1;base_mass=1;branch_rows=[];profile_expected=1
        for s,peak in enumerate(m):
            tail-=peak;p=2*tail+1
            ell=peak-(m[s+1] if s+1<h else 0)
            den=nprev*p
            snum=snum*den+sden;sden*=den
            g=math.gcd(snum,sden);snum//=g;sden//=g
            choices=[]
            classes=row_classes(p,ell)
            profile_expected*=math.comb(ell+p-1,p-1)
            for d,mass in classes:
                e=p//d
                # Since snum/sden is reduced, den(e*sigma)=sden/gcd(sden,e).
                vfactor=sden//math.gcd(sden,e)
                choices.append((vfactor,mass,d))
            if len(choices)==1:
                vfactor,mass,d=choices[0]
                base_v=math.lcm(base_v,vfactor);base_mass*=mass
            else:branch_rows.append(tuple(choices))
            nprev=p
        assert tail==0 and nprev==1
        profile_roots=0;example_classes=[]
        for choices in itertools.product(*branch_rows):
            v=base_v;mass=base_mass
            for vfactor,multiplicity,d in choices:
                v=math.lcm(v,vfactor);mass*=multiplicity
            assert v%2==1 and v%n==0
            states=n*mass
            assert states%v==0,(n,m,choices,mass,v)
            cycles=states//v
            signature_count+=1;profile_roots+=mass;cycles_total+=cycles
            height_sum+=h*cycles;overhead+=(2*h-1)*cycles
            height_cycles[h]+=cycles;period_cycles[v]+=cycles
            if n==17 and m==(4,1,1,1,1):
                example_classes.append(dict(root_multiplicity=mass,physical_period=v,cycle_count=cycles))
        assert profile_roots==profile_expected,(n,m,profile_roots,profile_expected)
        root_total+=profile_roots
        if n==17 and m==(4,1,1,1,1):
            example=dict(peak_partition=m,root_count=profile_roots,classes=example_classes)
    assert root_total==cat and n*root_total==W
    assert sum(v*c for v,c in period_cycles.items())==W
    assert sum(height_cycles.values())==cycles_total
    assert overhead==2*height_sum-cycles_total
    assert overhead==sum((2*h-1)*c for h,c in height_cycles.items())
    if n in quoted:assert (W,overhead)==quoted[n],(n,W,overhead,quoted[n])
    if n==17:assert (cycles_total,height_sum,overhead)==(146,519,892)
    if n==19:assert (cycles_total,height_sum,overhead)==(360,1384,2408)
    ep=endpoint(n,W)
    row=dict(n=n,r=r,width=W,profile_count=profile_count,least_period_signature_count=signature_count,
        counted_roots=root_total,catalan=cat,counted_physical_states=n*root_total,
        every_signature_integral_cycle_quotient=True,all_periods_odd_and_multiple_of_n=True,
        cycles=cycles_total,height_sum=height_sum,overhead=overhead,upper_length=W+overhead,
        endpoint_lower=ep,upper_minus_endpoint_lower=W+overhead-ep['B'],
        relative_overhead=decimal_enclosure(overhead,W),
        cycle_counts_by_height=dict(sorted(height_cycles.items())),cycle_counts_by_period=dict(sorted(period_cycles.items())),
        percentage_tests={str(q):dict(strictly_below= q*overhead<W,exact_margin=W-q*overhead) for q in (100,1000,10000)})
    rows.append(row);total_profiles+=profile_count;total_signatures+=signature_count
    (OUT/'partial_census.json').write_text(json.dumps(dict(completed_through=n,total_profiles=total_profiles,rows=rows))+'\n')
    if n in (17,19,21,27,29,31,41,55,57,61,85,87,101) or r%5==0:
        print(json.dumps({k:row[k] for k in ('n','profile_count','least_period_signature_count','cycles','height_sum','width','overhead','upper_length')}|dict(elapsed_seconds=time.monotonic()-started)),flush=True)

assert total_profiles==1295970 and rows[-1]['profile_count']==204226
assert rows[-1]['upper_length']==199805614710856411551021117606
assert 1_000_000*rows[-1]['overhead']<6*rows[-1]['width']
assert sorted((a['physical_period'],a['root_multiplicity'],a['cycle_count']) for a in example['classes'])==[(51,3,1),(153,162,18)]
by_n={row['n']:row for row in rows}
ranges=[]
for start,q in ((29,100),(57,1000),(87,10000)):
    checks=[]
    for k in range(start,103):
        odd=k if k%2 else k-1;source=by_n[odd];factor=1 if k%2 else 2
        width=math.comb(k,k//2);upper=factor*source['upper_length'];C=upper-width
        assert width==factor*source['width'] and q*C<width
        checks.append(dict(k=k,odd_source=odd,width=width,upper_length=upper,overhead=C,exact_margin=width-q*C))
    ranges.append(dict(start=start,end=102,reciprocal_error=q,all_cases_strict=True,checks=checks))
extract_dims=(17,19,21,27,29,31,41,55,57,61,85,87,101)
extractions=[{k:by_n[n][k] for k in ('n','width','overhead','upper_length','endpoint_lower','upper_minus_endpoint_lower','relative_overhead','percentage_tests')} for n in extract_dims]
report=dict(status='PASS',scope='Exact profile/row-period census of the proved height-adaptive construction. No enormous word materialized, no optimization, no claim that this construction length equals nu.',
    proof_note='scratch/PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md',
    dimensions='every odd n from3 through101, with exact even lifts through102',
    total_profiles=total_profiles,total_least_period_signatures=total_signatures,
    every_profile_root_product_verified=True,every_signature_cycle_quotient_integral=True,
    every_dimension_root_sum_equals_catalan=True,every_dimension_state_sum_equals_width=True,
    canonical_17_19_cycle_and_height_checks=True,quoted_entries_all_match=True,
    mixed_symmetry_example=example,rows=rows,finite_percentage_ranges=ranges,requested_extractions=extractions,
    resource_caps=dict(cpu_seconds=300,wall_seconds=360,address_space_bytes=4*1024**3),
    elapsed_seconds=time.monotonic()-started)
out=(json.dumps(report,indent=2)+'\n').encode();(OUT/'exact_rotation_period_census.json').write_bytes(out)
(OUT/'requested_plain_numbers.json').write_text(json.dumps(dict(extractions=extractions,total_profiles=total_profiles,
    n101_profile_count=rows[-1]['profile_count'],n101_strict_six_ppm=True),indent=2)+'\n')
print('FINAL',json.dumps(dict(status=report['status'],total_profiles=total_profiles,total_signatures=total_signatures,
    n101_width=rows[-1]['width'],n101_overhead=rows[-1]['overhead'],n101_upper=rows[-1]['upper_length'],
    n101_lower=rows[-1]['endpoint_lower'],n101_upper_minus_lower=rows[-1]['upper_minus_endpoint_lower'],
    n101_relative_overhead=rows[-1]['relative_overhead'],report_sha256=hashlib.sha256(out).hexdigest(),
    elapsed_seconds=report['elapsed_seconds'])),flush=True)
