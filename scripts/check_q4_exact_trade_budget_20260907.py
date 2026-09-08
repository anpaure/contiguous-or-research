"""Exact private-credit and positive-overlap budget for arbitrary local trades."""
from collections import Counter, defaultdict
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from itertools import product
import json
from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]/"scratch"
raw = (root/"q4int_final1280_witness_20260906_f7a91.json").read_bytes()
assert sha256(raw).hexdigest() == "bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36"
rows = json.loads(raw)["rectangles"]
spec = spec_from_file_location("dual",root/"q4int_verify_20260906_f7a91.py")
dual = module_from_spec(spec)
spec.loader.exec_module(dual)
owner = defaultdict(set)
for i,row in enumerate(rows):
    for c,d in product(row["C"],row["D"]):
        point = [0]*6
        for axis,value in zip(row["left"]+row["right"],c+d):point[axis]=value
        owner[tuple(point)].add(i)
assert set(owner) == set(product(range(4),repeat=6))
private_weight = [0]*80
shared = Counter()
for point,ids in owner.items():
    weight = dual.weight12(point)
    if len(ids)==1:
        private_weight[next(iter(ids))] += weight
    elif weight:
        shared[tuple(sorted(ids))] += weight
credit = [12*(len(r["C"])+len(r["D"]))-private_weight[i]
          for i,r in enumerate(rows)]
assert Counter(credit) == Counter({0:50,6:4,16:10,19:16})
expected_pairs = [(14,29),(15,28),(26,55),(27,54),
                  (46,75),(47,74),(60,77),(61,78)]
assert shared == Counter({p:13 for p in expected_pairs})
assert len({i for p in expected_pairs for i in p}) == 16
assert {i for i,c in enumerate(credit) if c==19} == {i for p in expected_pairs for i in p}

# Independent exact-cardinality knapsack on the eight matched components
# and the remaining single-row components verifies the closed formula.
components = [[(0,0),(1,19),(2,25)] for _ in expected_pairs]
components += [[(0,0),(1,c)] for i,c in enumerate(credit) if c!=19]
dp = [0]
for choices in components:
    updated = [-10**9]*(len(dp)+max(n for n,_ in choices))
    for n,value in enumerate(dp):
        for added,gain in choices:
            updated[n+added] = max(updated[n+added],value+gain)
    dp = updated
assert len(dp)==81
for r in range(81):
    formula = (19*r if r<=8 else 152+16*(r-8) if r<=18
               else 312+6*(r-18) if r<=30 else 384)
    assert dp[r]==formula
assert [next(r for r,v in enumerate(dp) if v>=12*saving)
        for saving in (9,20,32)] == [6,14,30]
six_candidates = (comb(8,6)*2**6,
                  comb(8,5)*2**5*10,
                  comb(8,4)*2**4*comb(10,2))
assert six_candidates == (1792,17920,50400)
print("PASS exact trade budget: credits",dict(sorted(Counter(credit).items())))
print("PASS eight disjoint positive-overlap pairs, each scaled weight 13")
print("PASS 81 exact-cardinality maxima; target row-count minima: 6, 14, 30")
print("Six-row sets passing the saving-nine dual threshold:",sum(six_candidates))
