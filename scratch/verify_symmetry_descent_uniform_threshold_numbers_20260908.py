#!/usr/bin/env python3
"""Four exact outward-root envelopes and stored finite-band replay; h100 only."""
import hashlib,json,math,resource,signal,socket,sys,time
from fractions import Fraction
from pathlib import Path
assert socket.gethostname().split('.')[0]=='arboghast'
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
signal.alarm(45)
sys.set_int_max_str_digits(0)
started=time.monotonic()
OUT=Path('/home/amodo/exact-b-symmetry-descent-thresholds-20260908');OUT.mkdir(exist_ok=True)
INPUT=Path('/home/amodo/exact-b-rotation-period-census-20260908/exact_rotation_period_census.json')
EXPECTED='43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2'
raw=INPUT.read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED
data=json.loads(raw);assert data['status']=='PASS'
by_r={row['r']:row for row in data['rows']}
SCALE=10**60

def fraction_record(x):return dict(numerator=x.numerator,denominator=x.denominator)

def decimal_interval(x,places=45):
    scale=10**places;q=x.numerator*scale//x.denominator
    def render(z):return str(z//scale)+'.'+str(z%scale).zfill(places)
    return dict(lower=render(q),upper=render(q+1),decimal_places=places,
                lower_scaled=q,upper_scaled=q+1)

def root_upper(x):
    a=x.numerator;b=x.denominator;scaled=a*SCALE*SCALE
    q=math.isqrt(scaled//b)
    if q*q*b<scaled:q+=1
    assert (q-1)*(q-1)*b<scaled<=q*q*b
    return Fraction(q,SCALE),dict(radicand=fraction_record(x),ceiling_scaled_root=q,
        scale=SCALE,lower_square_strict=True,upper_square_valid=True)

analytic=[]
for r,claimed,target in ((45,Fraction(9272,10**6),Fraction(1,100)),
                        (163,Fraction(992,10**6),Fraction(1,1000)),
                        (741,Fraction(9987,10**8),Fraction(1,10000)),
                        (3424,Fraction(9999,10**9),Fraction(1,100000))):
    cat=math.comb(2*r,r)//(r+1)
    J=Fraction(3*r+49,3*r*(r+2)*(r+3))+Fraction(43,72*cat)
    assert J==Fraction(1,r*(r+2))+Fraction(40,3*r*(r+2)*(r+3))+Fraction(43,72*cat)
    first,first_certificate=root_upper(2*J/(2*r+1))
    root_r,second_certificate=root_upper(Fraction(r))
    first_term=2*first
    second_term=86*(r+1)*root_r*Fraction(25,36)**r
    upper=first_term+second_term
    assert upper<claimed<target
    record=dict(r=r,odd_dimension=2*r+1,catalan=cat,J=fraction_record(J),
        first_root_certificate=first_certificate,sqrt_r_certificate=second_certificate,
        first_term_upper=fraction_record(first_term),second_term_upper=fraction_record(second_term),
        E_upper=fraction_record(upper),E_upper_decimal=decimal_interval(upper),
        claimed_upper=fraction_record(claimed),target=fraction_record(target),
        exact_positive_margin_below_claim=fraction_record(claimed-upper),
        strict_comparison_pass=True)
    analytic.append(record)
    print('ENVELOPE',json.dumps({k:record[k] for k in ('r','odd_dimension','E_upper_decimal','claimed_upper','target','strict_comparison_pass')}),flush=True)

band=[]
for r in range(14,45):
    row=by_r[r];C=row['overhead'];W=row['width']
    assert row['n']==2*r+1 and 125*C<W
    band.append(dict(r=r,n=row['n'],W=W,C=C,N=row['upper_length'],
        ratio=fraction_record(Fraction(C,W)),strict_margin=W-125*C))
maximum=max(band,key=lambda row:Fraction(row['C'],row['W']))
assert len(band)==31 and maximum['r']==16
max_ratio=Fraction(maximum['C'],maximum['W'])
assert max_ratio==Fraction(4479616,583401555)<Fraction(1,125)<Fraction(1,100)
assert sum(Fraction(row['C'],row['W'])==max_ratio for row in band)==1
row97=by_r[48]
assert row97['n']==97
assert row97['width']==12738806129490428451365214300
assert row97['overhead']==99533441612804133661134
assert 100000*row97['overhead']<row97['width']
quoted97=dict(n=97,r=48,W=row97['width'],C=row97['overhead'],N=row97['upper_length'],
    ratio=fraction_record(Fraction(row97['overhead'],row97['width'])),
    ratio_decimal=decimal_interval(Fraction(row97['overhead'],row97['width'])),
    strict_margin_below_one_part_in_100000=row97['width']-100000*row97['overhead'])
report=dict(status='PASS',scope='Exact numerical inequalities only; analytic envelope, monotonicity and construction theorem are separate proof inputs.',
    input_census_file=str(INPUT),input_census_sha256=EXPECTED,input_hash_verified=True,
    no_partition_census_rerun=True,no_solver_execution=True,
    root_scale=SCALE,analytic_envelopes=analytic,
    finite_band=dict(r_first=14,r_last=44,count=31,all_125C_less_than_W=True,rows=band,
        unique_maximum=maximum,maximum_decimal=decimal_interval(max_ratio)),
    quoted_dimension97=quoted97,
    resource_caps=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=512*1024**2),
    elapsed_seconds=time.monotonic()-started)
out=(json.dumps(report,indent=2)+'\n').encode()
(OUT/'symmetry_descent_threshold_numeric_certificate.json').write_bytes(out)
print('BAND_MAX',json.dumps(maximum),flush=True)
print('N97',json.dumps(quoted97),flush=True)
print('FINAL',json.dumps(dict(status='PASS',report_sha256=hashlib.sha256(out).hexdigest(),
    elapsed_seconds=report['elapsed_seconds'],finite_cases=31,analytic_cases=4)),flush=True)
