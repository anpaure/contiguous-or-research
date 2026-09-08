#!/usr/bin/env python3
"""Outward-rational certification of only the specified harmonic-period numbers.

Execute on h100 only. No floating point is used in a mathematical premise.
"""
import hashlib
import json
import resource
import signal
import time
from fractions import Fraction
from math import isqrt
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (120,120))
resource.setrlimit(resource.RLIMIT_AS, (2*1024**3,2*1024**3))
signal.alarm(150)
started=time.monotonic()
OUT=Path('/home/amodo/harmonic-period-three-rows-20260908')
OUT.mkdir(parents=True,exist_ok=True)
B=10**40
TERMS=64
calls=0

def ceildiv(a,b):
    return -((-a)//b)

def fixed(a):
    sign='-' if a<0 else ''
    a=abs(a)
    return sign+str(a//B)+'.'+str(a%B).zfill(40)

def rational(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator)}

def unit_log(n,d):
    """Enclose log(n/d) for 1<=n/d<=2, in units of 1/B.

    2*sum_{j=0}^{63} y^(2j+1)/(2j+1), y=(n-d)/(n+d),
    with each positive operation rounded outwards. The remaining tail
    is at most 3^(-128), since 0<=y<=1/3.
    """
    assert d<=n<=2*d
    if n==d: return 0,0
    lo=(n-d)*B//(n+d); hi=ceildiv((n-d)*B,n+d)
    sqlo=lo*lo//B; sqhi=ceildiv(hi*hi,B)
    a,b=lo,hi; sl=su=0
    for j in range(TERMS):
        sl+=a//(2*j+1); su+=ceildiv(b,2*j+1)
        a=a*sqlo//B; b=ceildiv(b*sqhi,B)
    return 2*sl,2*su+ceildiv(B,3**(2*TERMS))

LN2=unit_log(2,1)

def logq(n,d=1):
    """Enclose natural log of an arbitrary positive rational exactly."""
    global calls
    calls+=1
    assert n>0 and d>0
    exponent=n.bit_length()-d.bit_length()
    if exponent>=0: nn,dd=n,d<<exponent
    else: nn,dd=n<<(-exponent),d
    while nn<dd:
        nn*=2; exponent-=1
    while nn>=2*dd:
        dd*=2; exponent+=1
    lo,hi=unit_log(nn,dd)
    if exponent>=0:
        return lo+exponent*LN2[0],hi+exponent*LN2[1]
    return lo+exponent*LN2[1],hi+exponent*LN2[0]

def atan_reciprocal(a):
    lo=hi=0
    for j in range(TERMS):
        den=(2*j+1)*a**(2*j+1)
        tl,tu=B//den,ceildiv(B,den)
        if j%2==0: lo+=tl; hi+=tu
        else: lo-=tu; hi-=tl
    # TERMS is even: partial sum below atan, next positive term bounds remainder.
    hi+=ceildiv(B,(2*TERMS+1)*a**(2*TERMS+1))
    return lo,hi

at5=atan_reciprocal(5); at239=atan_reciprocal(239)
PI=(16*at5[0]-4*at239[1],16*at5[1]-4*at239[0])
assert 3*B<PI[0]<PI[1]<4*B

def sqrtq_upper(n,d):
    """ceil(B*sqrt(n/d)), determined by integer square comparison."""
    assert n>=0 and d>0
    a=isqrt(n*B*B//d)
    if a*a*d<n*B*B: a+=1
    assert a*a*d>=n*B*B and (a==0 or (a-1)*(a-1)*d<n*B*B)
    return a

def primes_to(n):
    sieve=bytearray(b'\x01')*(n+1); sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

LN10=logq(10)
rows=[]
for r,L,M,digits in [(10**12,1100,790,330),(10**14,3500,2250,950),(10**16,10200,6150,2600)]:
    root=isqrt(r); assert root*root==r
    Q=4*(r+1)*root
    delta=Fraction(1,10)
    guard_depth=delta*root/(L+2)
    guard_mu=Fraction(18*r,10*(L+2)**3)
    assert guard_depth>=4 and guard_mu>=1000
    primes=primes_to(M)
    alo=ahi=B
    for p in primes:
        lo,hi=logq(p)
        alo+=lo//(p-1); ahi+=ceildiv(hi,p-1)
    sumloghi=0; capped=0; b_bounds=[]
    for s in range(L):
        # rho^2 = 1001^2 (s+2)^3 / (1000^2 * 4*pi*(9r/10)).
        # Using the LOWER pi enclosure gives an UPPER rho enclosure.
        rhohi=sqrtq_upper(1001**2*(s+2)**3*10*B,1000**2*4*PI[0]*9*r)
        y=Fraction(36*r,10*(s+2))-Fraction(22*r,10*(s+3))+1
        lylo,lyhi=logq(y.numerator,y.denominator)
        assert lylo>0
        numerator=ahi+M*rhohi
        if numerator>=lylo:
            capped+=1
            lbhi=0
        else:
            lblo,lbhi=logq(numerator,lylo)
            assert lbhi<0
        sumloghi+=lbhi
        if s in (0,L-1):
            b_bounds.append(dict(s=s,rho_upper=fixed(rhohi),log_y_lower=fixed(lylo),
                                 b_upper=rational(min(Fraction(1),Fraction(numerator,lylo))),
                                 log_b_upper=fixed(lbhi)))
    # Upper bound on log[4*10^d*Q*(1+M)*product b_s].
    product_log_hi=logq(4*Q*(1+M))[1]+digits*LN10[1]+sumloghi
    assert product_log_hi<0
    terms=[('short_period',4*root,Fraction(M)),
           ('depth',2*(L+1),(guard_depth-4)**2/6),
           ('nonprimitive',Q*L*(3*r+1),Fraction(36*r,30*(L+2)**3))]
    other=[]
    for name,C,E in terms:
        lower_margin=E.numerator*B//E.denominator-logq(4*C)[1]-digits*LN10[1]
        assert lower_margin>0
        other.append(dict(name=name,prefactor=str(C),exponent=rational(E),
                          lower_margin_E_minus_log4C_minus_dlog10=fixed(lower_margin),
                          certified_term_less_than_quarter_ten_to_minus_d=True))
    rows.append(dict(r=str(r),L=L,M=M,d=digits,Q=str(Q),prime_count=len(primes),
                     depth_guard=rational(guard_depth),nb_mean_guard=rational(guard_mu),
                     A_z_lower=fixed(alo),A_z_upper=fixed(ahi),
                     b_factors=L,b_factors_capped_at_one=capped,endpoint_bounds=b_bounds,
                     sum_log_b_upper=fixed(sumloghi),
                     upper_log_four_times_ten_to_d_times_harmonic_term=fixed(product_log_hi),
                     harmonic_term_certified_less_than_quarter_ten_to_minus_d=True,
                     other_terms=other,all_four_sum_strictly_less_than_ten_to_minus_d=True))
    print(json.dumps({'r':str(r),'L':L,'M':M,'d':digits,'harmonic_log_margin_upper':fixed(product_log_hi),
                      'other_lower_margins':[x['lower_margin_E_minus_log4C_minus_dlog10'] for x in other]}),flush=True)

# Exact right-endpoint Riemann lower sum after t=(i/1000)^2.
# q_i=.251+.38*t_i^(3/2); 0<q_i<1. A 32-term -log expansion is a lower bound.
cells=[]; cell_sum=0
for i in range(1,1251):
    q=Fraction(251,1000)+Fraction(19*i**3,50*1000**3)
    assert 0<q<1
    u=1-q; power=u; series=Fraction(0)
    for j in range(1,33):
        series+=power/j; power*=u
    cell=Fraction(2*i-1,10**6)*series
    down=cell.numerator*10**18//cell.denominator
    cells.append(down); cell_sum+=down
assert cell_sum==1074181933864880728
assert 1000*cell_sum>1073*10**18
(OUT/'integral_1250_downward_cells.json').write_text(json.dumps(cells)+'\n')

coefficient_squared=(Fraction(1001,1000)*Fraction(107,100))**2/(Fraction(7999,10000)**2*4*Fraction(157,50)*Fraction(99,100))
coefficient_margin=Fraction(19,50)**2-coefficient_squared
conversion_margin=Fraction(1,2)-Fraction(930,1069)**5
assert coefficient_margin>0 and conversion_margin>0
integral=dict(status='PASS',cells=1250,log_series_terms_per_cell=32,
              exact_sum_of_downward_1e18_cells=str(cell_sum),denominator=str(10**18),
              certified_integral_strictly_greater_than='1073/1000',
              margin_above_1073_over_1000=rational(Fraction(cell_sum,10**18)-Fraction(1073,1000)),
              coefficient_squared=rational(coefficient_squared),coefficient_margin_below_038_squared=rational(coefficient_margin),
              conversion_fifth_power=rational(Fraction(930,1069)**5),conversion_margin_below_one_half=rational(conversion_margin))
report=dict(status='PASS_ALL_SPECIFIED_RATIONAL_CERTIFICATES',fixed_point_scale=str(B),
            logarithm_atanh_terms=TERMS,logarithm_tail_bound='3^(-128)',
            pi_method='Machin identity 16 atan(1/5)-4 atan(1/239), 64 alternating terms each',
            pi_lower=fixed(PI[0]),pi_upper=fixed(PI[1]),
            natural_log10_lower=fixed(LN10[0]),natural_log10_upper=fixed(LN10[1]),
            rows=rows,integral=integral,natural_log_calls=calls,
            no_floating_point_mathematical_premises=True,no_optimization_or_parameter_search=True,
            resource_caps=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3),
            elapsed_seconds=time.monotonic()-started,
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT/'rational_certificate_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'integral':integral,'natural_log_calls':calls,'elapsed_seconds':report['elapsed_seconds']}),flush=True)
