"""Exact GF(2) tight-column diagnostic for a literal invariant core. Remote only."""
import argparse
from itertools import product
import json
from pathlib import Path
import subprocess


def involution(mask):
    return ((mask & 31) << 5) | (mask >> 5)


def support(row):
    assert sorted(list(row[0]) + list(row[1])) == list(range(10))
    prefixes = []
    for order in row:
        values = [0]
        for label in order:
            values.append(values[-1] | (1 << label))
        prefixes.append(values)
    return {x | y for x, y in product(*prefixes)}


parser = argparse.ArgumentParser()
parser.add_argument("core_artifact",type=Path)
parser.add_argument("--catalogue",required=True,type=Path)
parser.add_argument("--output",type=Path)
args = parser.parse_args()
data = json.loads(args.core_artifact.read_text())
core = data["core_rows"]
assert len(core) == 10
core_sets = [support(row) for row in core]
core_union = set.union(*core_sets)
assert {involution(x) for x in core_union} == core_union
core_tight = {x for x in core_union if 4 <= x.bit_count() <= 6}
assert len(core_tight) == 160
assert sum(sum(4 <= x.bit_count() <= 6 for x in s) for s in core_sets) == 160
assert {x for x in range(1024) if involution(x) == x
        and 4 <= x.bit_count() <= 6} <= core_tight
required = [x for x in range(1024) if x <= involution(x)
            and 4 <= x.bit_count() <= 6 and x not in core_union]
assert len(required) == 256
lookup = {x: i for i, x in enumerate(required)}
result = subprocess.run([str(args.catalogue)],
                        input=str(len(core_tight))+" "+" ".join(map(str,sorted(core_tight))),
                        text=True,capture_output=True,check=True)
print(result.stderr.strip(),flush=True)
columns, basis = [], {}
for line in result.stdout.splitlines():
    weight, packed = map(int,line.split())
    assert weight == 2
    permutation = tuple((packed >> (4*i)) & 15 for i in range(10))
    bank = support((permutation[:5],permutation[5:]))
    bank |= {involution(x) for x in tuple(bank)}
    target_ids = [lookup[x] for x in bank if x in lookup]
    assert len(target_ids) == 16
    vector = sum(1 << i for i in target_ids)
    columns.append(vector)
    reduced = vector
    while reduced:
        pivot = reduced.bit_length()-1
        if pivot in basis:
            reduced ^= basis[pivot]
        else:
            basis[pivot] = reduced
            break

demand = (1 << len(required))-1
reduced = demand
for pivot in sorted(basis,reverse=True):
    if reduced >> pivot & 1:
        reduced ^= basis[pivot]
if not reduced:
    print("GF2_CONSISTENT", "columns",len(columns),"rank",len(basis),
          "tight_orbits",len(required),flush=True)
else:
    dual = 1 << (reduced.bit_length()-1)
    for pivot in sorted(basis):
        if (basis[pivot] & dual).bit_count() % 2:
            dual ^= 1 << pivot
    assert all((dual & vector).bit_count() % 2 == 0 for vector in columns)
    assert (dual & demand).bit_count() % 2 == 1
    targets = [mask for i, mask in enumerate(required) if dual >> i & 1]
    certificate = {"core_rows":core,"parity_target_orbits":targets,
                   "column_count":len(columns),"column_rank_gf2":len(basis)}
    if args.output:
        args.output.write_text(json.dumps(certificate,indent=2)+"\n")
    print("EXACT_PARITY_OBSTRUCTION", "columns",len(columns),"rank",len(basis),
          "odd_demand_size",len(targets),"targets",targets,flush=True)
