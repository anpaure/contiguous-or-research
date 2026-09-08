"""Exact rational dual and elementary rank-layer checks; no SciPy."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial


def lower(ranks):
    gaps = [b-a for a,b in zip(ranks,ranks[1:])]
    if any(a==b==1 for a,b in zip(gaps,gaps[1:])):
        return F(1)
    return F(23,24) if 1 in gaps else F(2,3)


types = [r for size in range(1,6) for r in combinations(range(5),size)]
slacks = []
tight = []
for r,s in combinations_with_replacement(types,2):
    ranks = Counter(i+j for i in r for j in s)
    value = F(5,12)*(ranks[3]+ranks[5])+F(4,3)*ranks[4]
    cost = len(r)*lower(s)+len(s)*lower(r)
    assert value<=cost
    slacks.append(cost-value)
    if value==cost:tight.append((r,s))
assert len(types)==31 and len(slacks)==496
assert len(tight)==9 and min(x for x in slacks if x)>0
assert min(x for x in slacks if x)==F(1,6)
assert F(5,12)*(comb(8,3)+comb(8,5))+F(4,3)*comb(8,4)==140
strong_slacks = []
for r,s in combinations_with_replacement(types,2):
    ranks = Counter(i+j for i in r for j in s)
    slack = (len(r)*lower(s)+len(s)*lower(r)
             -F(1,2)*(ranks[3]+ranks[5])-F(6,5)*ranks[4])
    if r==s==tuple(range(5)):
        assert slack==0
    else:
        assert slack>=F(2,15)
    strong_slacks.append(slack)
assert strong_slacks.count(0)==1 and min(s for s in strong_slacks if s)==F(2,15)
assert F(1,2)*(comb(8,3)+comb(8,5))+F(6,5)*comb(8,4)==140


@lru_cache(None)
def density(d,x):
    if d==1:
        return F(0<=x<1)
    return sum(F((-1)**j*comb(d,j),factorial(d-1))
               *max(F(0),x-j)**(d-1) for j in range(d+1))


@lru_cache(None)
def run_lower(d,a):
    return F(1) if d==1 else sum(density(d,F(d+a,2)-i) for i in range(a+1))


def tube_lower(d,ranks):
    longest = run = 0
    for x,y in zip(ranks,ranks[1:]):
        run = run+1 if y-x==1 else 0
        longest = max(longest,run)
    return run_lower(d,longest)


all_split_count = Counter()
all_split_tight = []
all_split_positive = []
for r in range(1,5):
    s = 8-r
    left = [u for size in range(1,r+2) for u in combinations(range(r+1),size)]
    right = [v for size in range(1,s+2) for v in combinations(range(s+1),size)]
    pairs = combinations_with_replacement(left,2) if r==s else product(left,right)
    for u,v in pairs:
        ranks = Counter(i+j for i in u for j in v)
        slack = (len(u)*tube_lower(s,v)+len(v)*tube_lower(r,u)
                 -F(1,2)*(ranks[3]+ranks[5])-F(6,5)*ranks[4])
        all_split_count[r] += 1
        if r==s==4 and u==v==tuple(range(5)):
            assert slack==0
            all_split_tight.append((r,u,s,v))
        else:
            assert slack>=F(2,15)
            all_split_positive.append(slack)
assert all_split_count==Counter({1:765,2:889,3:945,4:496})
assert sum(all_split_count.values())==3095 and len(all_split_tight)==1
assert min(all_split_positive)==F(2,15)
assert all(tube_lower(4,r)==lower(r) for r in types)

# Independent finite convolution checks of the exact smoothing identity.
smooth_cases = 0
for d in range(1,8):
    for m in range(1,13):
        cube = [1]
        for _ in range(d):
            following = [0]*(len(cube)+m-1)
            for j,value in enumerate(cube):
                for offset in range(m):following[j+offset]+=value
            cube = following
        for a in range(d+1):
            layers = [0]*(len(cube)+a*m)
            for i in range(a+1):
                for j,value in enumerate(cube):layers[i*m+j]+=value
            z = F((d+a)*m,2)
            smooth = sum(value*density(d,z-j)
                         for j,value in enumerate(layers) if 0<=z-j<=d)
            assert smooth==run_lower(d,a)*m**(d-1)
            assert max(layers)>=smooth
            smooth_cases += 1
assert smooth_cases==420
unity_cases = 0
for d in range(1,8):
    for quarter in range(-8,4*d+9):
        z = F(quarter,4)
        assert sum(density(d,z-j) for j in range(-d-3,d+4))==1
        unity_cases += 1
assert unity_cases==231

# Direct rank-polynomial convolution checks all three finite formulas.
for m in range(1,33):
    cube = [1]
    for _ in range(4):
        following = [0]*(len(cube)+m-1)
        for rank,value in enumerate(cube):
            for step in range(m):following[rank+step]+=value
        cube = following
    assert cube[2*m-2]==F(2*m**3+m,3)
    two = [0]*(len(cube)+m)
    three = [0]*(len(cube)+2*m)
    for rank,value in enumerate(cube):
        for offset in (0,m):two[rank+offset]+=value
        for offset in (0,m,2*m):three[rank+offset]+=value
    correction = F(m,6) if m%2==0 else F(m,24)
    assert two[(5*m-4)//2]==F(23,24)*m**3+correction
    assert three[3*m-2]==m**3

rows = [
    ("0461","5723"),("0473","2651"),("0674","3152"),
    ("0726","1435"),("1507","4263"),("1605","7432"),
    ("2104","6375"),("2150","7463"),("3206","7154"),
    ("3210","4567"),("3617","5204"),("4302","6157"),
    ("5034","6721"),("5426","7301"),
]


def prefixes(order):
    result = [0]
    for digit in order:result.append(result[-1]|(1<<int(digit)))
    return result


loads = [0]*256
for left,right in rows:
    assert sorted(left+right)==list("01234567")
    for x in prefixes(left):
        for y in prefixes(right):loads[x|y]+=1
assert all(loads) and sum(loads)==350
assert all(loads[x]==1 for x in range(256) if 3<=x.bit_count()<=5)
assert sum(2*5*lower(tuple(range(5))) for _ in rows)==140
print("PASS 496 exact rational type-pair inequalities; 9 equality pairs")
print("PASS separating dual: 496 inequalities; only full/full tight; gap 2/15")
print("PASS all splits: 3095 rational inequalities; only full balanced 4+4 tight")
print("PASS 420 exact finite smoothing identities and 231 partition-of-unity checks")
print("PASS 96 finite rank-layer formula checks, m=1,...,32")
print("PASS explicit 14-row attainment: 256 targets, weighted charge 140")
