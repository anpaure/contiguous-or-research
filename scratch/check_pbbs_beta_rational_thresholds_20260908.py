#!/usr/bin/env python3
"""Four prescribed exact rational comparisons only. Run on h100."""
import json
import math
import resource
import signal
import sys
from fractions import Fraction
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
signal.alarm(45)
sys.set_int_max_str_digits(0)
out=Path('/home/amodo/exact-b-pbbs-beta-thresholds-20260908')
out.mkdir(exist_ok=True)
scale=10**24
records=[]
for n,q,direction in [(5641,100,1),(5643,100,-1),(6253,1000,1),(6255,1000,-1)]:
    assert n>=5 and n%2==1
    width=math.comb(n,(n-1)//2)
    beta=Fraction(4*n*(n+1)*pow(242,n),pow(243,n))+Fraction(n*pow(99,n),pow(100,n))
    principal=Fraction((1<<(n+2))+2*width,n*n*width)
    value=principal+beta
    comparison=q*value.numerator-value.denominator
    sign=(comparison>0)-(comparison<0)
    assert sign==direction
    lower=value.numerator*scale//value.denominator
    assert Fraction(lower,scale)<=value<Fraction(lower+1,scale)
    record=dict(n=n,threshold_denominator=q,sign_of_q_numerator_minus_denominator=sign,
        comparison_pass=True,R_numerator=str(value.numerator),R_denominator=str(value.denominator),
        lower_scaled_1e24=lower,upper_scaled_1e24=lower+1,interval_denominator=scale,
        lower_decimal=f'{lower//scale}.{lower%scale:024d}',
        upper_decimal=f'{(lower+1)//scale}.{(lower+1)%scale:024d}')
    records.append(record)
    print(json.dumps({k:v for k,v in record.items() if k not in ('R_numerator','R_denominator')},sort_keys=True))
report=dict(status='PASS',formula='W=binom(n,(n-1)/2); beta_n=4*n*(n+1)*(242/243)^n+n*(99/100)^n; R_n=(2^(n+2)+2*W)/(n^2*W)+beta_n',
    exact_arithmetic='Python integers and Fraction; complete reduced numerators and denominators retained; threshold signs by exact cross multiplication.',
    records=records,resource_caps=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=512*1024**2),
    scope='Only the four requested adjacent odd-dimension comparisons; no assertion of global monotonicity or a literal word.')
(out/'pbbs_beta_rational_threshold_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: all four prescribed rational threshold comparisons, with strict signs.')
