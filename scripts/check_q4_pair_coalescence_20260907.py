"""Exhaust all containing-product coalescences of the saved 1280 cover.

Checks every unordered rectangle pair and all 31 unordered nonempty splits.
This is a local certificate, not an integral-optimum proof.
"""

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


source = (Path(__file__).resolve().parents[1] / "scratch" /
          "q4int_final1280_witness_20260906_f7a91.json")
raw = source.read_bytes()
assert sha256(raw).hexdigest() == (
    "bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36"
)
data = json.loads(raw)
assert data["q"] == 4 and data["dimension"] == 6
rows = data["rectangles"]


def is_chain(points):
    ordered = sorted(set(map(tuple, points)), key=lambda p: (sum(p), p))
    return all(all(a <= b for a, b in zip(x, y))
               for x, y in zip(ordered, ordered[1:]))


supports = []
old_splits = []
for row in rows:
    left, right = tuple(row["left"]), tuple(row["right"])
    assert left and right and sorted(left + right) == list(range(6))
    for axes, chain in ((left, row["C"]), (right, row["D"])):
        assert chain and len(chain) == len(set(map(tuple, chain)))
        assert all(len(p) == len(axes) and all(0 <= x < 4 for x in p)
                   for p in chain)
        assert is_chain(chain)
        # Every coordinate varies, so the row's conflict graph is precisely
        # the complete bipartite graph on its two displayed shores.
        assert all(len({p[j] for p in chain}) > 1 for j in range(len(axes)))
    points = set()
    for x, y in product(row["C"], row["D"]):
        p = [0]*6
        for axis, value in zip(left + right, x + y):
            p[axis] = value
        points.add(tuple(p))
    supports.append(points)
    old_splits.append(tuple(sorted(left if 0 in left else right)))

assert len(rows) == 80
assert sum(len(r["C"]) + len(r["D"]) for r in rows) == data["cost"] == 1280
assert set.union(*supports) == set(product(range(4), repeat=6))

splits = [(tuple(i for i in range(6) if mask >> i & 1),
           tuple(i for i in range(6) if not (mask >> i & 1)))
          for mask in range(1, 63, 2)]
assert len(splits) == 31
projections = [[({tuple(p[i] for i in left) for p in support},
                 {tuple(p[i] for i in right) for p in support})
                for left, right in splits] for support in supports]

tests = 0
legal = []
triangle_types = Counter()
for i, j in combinations(range(len(rows)), 2):
    current_split_result = None
    for z, (left, right) in enumerate(splits):
        c1, d1 = projections[i][z]
        c2, d2 = projections[j][z]
        left_ok, right_ok = is_chain(c1 | c2), is_chain(d1 | d2)
        tests += 1
        if left_ok and right_ok:
            legal.append((i, j, left, len(c1 | c2) + len(d1 | d2)))
        if left == old_splits[i] == old_splits[j]:
            current_split_result = left_ok, right_ok
    if old_splits[i] != old_splits[j]:
        triangle_types["different_original_splits"] += 1
    else:
        assert current_split_result is not None
        assert current_split_result != (True, True)
        triangle_types[str(current_split_result)] += 1

assert tests == 97960
assert not legal, legal
assert triangle_types == Counter({
    "different_original_splits": 2560,
    "(False, False)": 360,
    "(True, False)": 120,
    "(False, True)": 120,
})
print("PASS: 80 rectangles, 4096 targets, principal charge 1280")
print("PASS: 97,960 pair/split tests; zero containing-product coalescences")
print("Triangle-certificate classes:", dict(triangle_types))

# Stronger test: deleting rows need not retain their redundant incidences.
# Only points whose full original covering multiplicity is removed matter.
coverage = Counter(p for support in supports for p in support)
private = [{p for p in support if coverage[p] == 1} for support in supports]
for row, core in zip(rows, private):
    assert core
    edges = set()
    for x, y in combinations(core, 2):
        up = [i for i in range(6) if x[i] < y[i]]
        down = [i for i in range(6) if x[i] > y[i]]
        edges.update(tuple(sorted((i, j))) for i in up for j in down)
    expected = {tuple(sorted((i, j)))
                for i in row["left"] for j in row["right"]}
    assert edges == expected
    assert {tuple(p[i] for i in row["left"]) for p in core} == set(map(tuple, row["C"]))
    assert {tuple(p[i] for i in row["right"]) for p in core} == set(map(tuple, row["D"]))

critical_tests = 0
legal_critical = Counter()
for size in (1, 2):
    for ids in combinations(range(len(rows)), size):
        critical = set.union(*(private[i] for i in ids))
        if size == 2:
            critical.update(p for p in supports[ids[0]] & supports[ids[1]]
                            if coverage[p] == 2)
        assert critical
        old_cost = sum(len(rows[i]["C"]) + len(rows[i]["D"]) for i in ids)
        for left, right in splits:
            c = {tuple(p[i] for i in left) for p in critical}
            d = {tuple(p[i] for i in right) for p in critical}
            critical_tests += 1
            if is_chain(c) and is_chain(d):
                legal_critical[size] += 1
                assert size == 1
                assert left == old_splits[ids[0]]
                assert len(c) + len(d) == old_cost
assert critical_tests == 100440
assert legal_critical == Counter({1: 80})
print("PASS: 100,440 critical-target replacement tests; no cheaper replacement")
print("PASS: all 80 private cores force their full original rectangles")
