"""Independently verify the complete streamed alternative-split certificate.

Checks odd cycles and implication paths against literal projected points;
does not call the C++ 2-SAT routine or trust its SAT/UNSAT labels.
"""
from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]/"scratch"
raw = (root/"q4int_final1280_witness_20260906_f7a91.json").read_bytes()
assert sha256(raw).hexdigest() == "bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36"
rows = json.loads(raw)["rectangles"]


def normalize(row):
    shores = []
    for axes, chain in ((row["left"],row["C"]),(row["right"],row["D"])):
        order = sorted(range(len(axes)),key=lambda j:axes[j])
        shores.append((tuple(axes[j] for j in order),
                       tuple(tuple(p[j] for j in order) for p in chain)))
    return tuple(sorted(shores))


old = json.loads((root/"q4int_local2_witness_20260906_f7a91.json").read_text())
assert set(map(normalize,rows)) == set(map(normalize,old["rectangles"]))
spec = spec_from_file_location("dual",root/"q4int_verify_20260906_f7a91.py")
dual = module_from_spec(spec)
spec.loader.exec_module(dual)
supports = []
old_splits = []
for row in rows:
    support = set()
    for c,d in product(row["C"],row["D"]):
        p = [0]*6
        for axis,value in zip(row["left"]+row["right"],c+d):p[axis]=value
        support.add(tuple(p))
    supports.append(support)
    mask = sum(1<<i for i in row["left"])
    old_splits.append(mask if mask&1 else mask^63)
assert set.union(*supports) == set(product(range(4),repeat=6))
assert sum(len(r["C"])+len(r["D"]) for r in rows) == 1280
coverage = Counter(p for support in supports for p in support)
private = [{p for p in support if coverage[p]==1} for support in supports]
split_masks = list(range(1,63,2))
axes = [(tuple(i for i in range(6) if mask>>i&1),
         tuple(i for i in range(6) if not(mask>>i&1))) for mask in split_masks]
census = Counter()
saving_limits = Counter()


def line():
    data = sys.stdin.readline()
    assert data, "certificate ended early"
    return data.split()


for i,j in combinations(range(80),2):
    critical = private[i]|private[j]|{p for p in supports[i]&supports[j] if coverage[p]==2}
    old_cost = sum(len(rows[z]["C"])+len(rows[z]["D"]) for z in (i,j))
    lower = (sum(dual.weight12(p) for p in critical)+11)//12
    saving_limits[old_cost-lower] += 1
    header = line()
    if lower>=old_cost:
        assert header == ["P",str(i),str(j)]
        census["pruned"] += 1
        continue
    points = sorted(critical,key=lambda p:sum(v<<(2*z) for z,v in enumerate(p)))
    n = len(points)
    assert header == ["R",str(i),str(j),str(n)]
    census["residuals"] += 1
    cache = {}

    def incompatible(split,x,y):
        if x>y:x,y=y,x
        key = split,x,y
        if key not in cache:
            a,b = points[x],points[y]
            bad = False
            for shore in axes[split]:
                if not(all(a[z]<=b[z] for z in shore) or
                       all(a[z]>=b[z] for z in shore)):
                    bad = True
                    break
            cache[key] = bad
        return cache[key]

    for s in range(31):
        for t in range(s,31):
            record = line()
            assert record[1:3] == [str(s),str(t)]
            census["tests"] += 1
            kind = record[0]
            if kind == "O":
                length = int(record[3])
                cycle = list(map(int,record[4:]))
                assert len(cycle)==length and length>=3 and length%2
                assert all(0<=v<n for v in cycle)
                for x,y in zip(cycle,cycle[1:]+cycle[:1]):
                    assert incompatible(s,x,y) and incompatible(t,x,y)
                census["odd_cycles"] += 1
            elif kind == "U":
                a = int(record[3])
                first = list(map(int,record[4:4+a]))
                b = int(record[4+a])
                second = list(map(int,record[5+a:]))
                assert len(first)==a and len(second)==b
                assert first[0]^1==first[-1]
                assert second[0]==first[-1] and second[-1]==first[0]
                for path in (first,second):
                    assert all(0<=v<2*n for v in path)
                    for x,y in zip(path,path[1:]):
                        assert (x&1)!=(y&1)
                        assert incompatible(s if x&1 else t,x//2,y//2)
                census["implication_cycles"] += 1
            elif kind == "S":
                assert len(record)==4 and len(record[3])==n
                assignment = [int(v) for v in record[3]]
                assert set(assignment)<= {0,1}
                for value,split in ((1,s),(0,t)):
                    chosen = [points[z] for z in range(n) if assignment[z]==value]
                    for shore in axes[split]:
                        projected = sorted({tuple(p[z] for z in shore) for p in chosen},
                                           key=lambda p:(sum(p),p))
                        assert all(all(u<=v for u,v in zip(a,b))
                                   for a,b in zip(projected,projected[1:]))
                assert sorted((split_masks[s],split_masks[t])) == sorted((old_splits[i],old_splits[j]))
                census["satisfying_assignments"] += 1
            else:
                raise AssertionError(record)

summary = line()
assert summary[0]=="SUMMARY"
limits = line()
assert limits[0]=="DUAL_SAVING_LIMITS"
assert not sys.stdin.read().strip()
assert census == Counter(pruned=1425,residuals=1735,tests=860560,
                         odd_cycles=848775,implication_cycles=10050,
                         satisfying_assignments=1735)
assert saving_limits == Counter({0:1425,1:1346,2:277,3:112})
print("PASS independent streamed certificate:",dict(census))
print("PASS current and archived local-two witness row sets are identical")
