from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
rows = [
('0461','5723','0461'),('0473','2651','2651'),
('0674','3152',None),('0726','1435','1435'),
('1507','4263',None),('1605','7432','1605'),
('2104','6375','2104'),('2150','7463','7463'),
('3206','7154','3206'),('3210','4567','4567'),
('3617','5204','3617'),('4302','6157','4302'),
('5034','6721','5034'),('5426','7301','7301')]
def prefixes(word):
    out=[0]
    for ch in word:
        out.append(out[-1] | (1 << int(ch)))
    return out
multiplicity=[0]*256
for left,right,selected in rows:
    assert sorted(left+right)==list('01234567')
    masks={a|b for a in prefixes(left) for b in prefixes(right)}
    assert len(masks)==25
    if selected is not None:
        assert selected in (left,right)
        masks.difference_update(prefixes(selected)[:3])
        assert len(masks)==22
    for mask in masks:
        multiplicity[mask]+=1
assert min(multiplicity)==1 and sum(multiplicity)==314
print('PASS: all 256 masks retained; total multiplicity 314, minimum 1.')
N=1000
scale=10**40
def J_upper(q):
    total=0
    for j in range(N):
        term=F(512*factorial(q)*comb(j+8,8),(2*j+9)**(q+1))
        total+=(scale*term.numerator+term.denominator-1)//term.denominator
    tail=F(2)**(8-q)*F(factorial(q),factorial(8)*(q-8))*F(2*N+7,2)**(-(q-8))
    return F(total,scale)+tail
J10=J_upper(10)
J13=J_upper(13)
def atan_interval(q,n):
    partial=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
    next_term=F((-1)**n,(2*n+1)*q**(2*n+1))
    return min(partial,partial+next_term),max(partial,partial+next_term)
a5,b5=atan_interval(5,40)
a239,b239=atan_interval(239,12)
pilo=16*a5-4*b239
pihi=16*b5-4*a239
M1bound=F('0.348224')
M25bound=F('0.077681')
assert J10<M1bound
assert 4*J13**2<18*pilo*M25bound**2
assert pilo>8*F('0.62665')**2
c9upper=(564480*pihi**2-1105440*pilo**4+723296*pihi**6-62475*pilo**8)/393216
assert c9upper<F('1.1807038039')
gammalower=3-F(33,4)*M1bound
assert gammalower==F('0.127152') and gammalower>0
certified=F('1.1807038039')-F('0.62665')*gammalower**2/(48*M25bound)
assert certified<F('1.177987')
print('PASS: 1000 upward-rounded rational terms plus full analytic tail give M1 < 0.348224.')
print('PASS: rational squared comparison gives M5/2 < 0.077681.')
print('PASS: Machin intervals give sqrt(pi/8) > 0.62665 and c9 < 1.1807038039.')
print('PASS: gamma > 0.127152 and the exact rational coefficient bound is < 1.177987.')
print('Exact rational upper bound:',certified)
print('Verifier path:',Path(__file__).resolve())
