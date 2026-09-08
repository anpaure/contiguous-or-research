"""Try exact rational verification of a saved numerical binary10 residual LP.

No successful print occurs unless all literal row, tight-equality, other-rank
coverage, nonnegativity, and charge checks pass exactly. Run on ssh h100.
"""
import argparse
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def involution(mask):
    return ((mask & 31) << 5) | (mask >> 5)


def support(row):
    assert sorted(row[0] + row[1]) == list(range(10))
    assert len(row[0]) == len(row[1]) == 5
    prefixes = []
    for order in row:
        values = [0]
        for label in order:
            values.append(values[-1] | (1 << label))
        prefixes.append(values)
    result = {x | y for x, y in product(*prefixes)}
    assert len(result) == 36
    return result


parser = argparse.ArgumentParser()
parser.add_argument("primal",type=Path)
parser.add_argument("--output",type=Path)
parser.add_argument("--exact-basis",action="store_true",
                    help="If rounding fails, select a basis by QR and solve it exactly with FLINT.")
args = parser.parse_args()
data = json.loads(args.primal.read_text())
core_sets = [support(row) for row in data["core_rows"]]
assert len(core_sets) == 10
core_union = set.union(*core_sets)
assert {involution(x) for x in core_union} == core_union
core_tight = {x for x in core_union if 4 <= x.bit_count() <= 6}
assert len(core_tight) == 160
assert sum(sum(4 <= x.bit_count() <= 6 for x in s) for s in core_sets) == 160
required = [x for x in range(1024) if x <= involution(x) and x not in core_union]
assert required == data["required_orbits"]
lookup = {x: i for i, x in enumerate(required)}
banks, raw = [], []
for entry in data["active_columns"]:
    assert entry["weight"] == 2
    seed = support(entry["row"])
    mate = {involution(x) for x in seed}
    tight_seed = {x for x in seed if 4 <= x.bit_count() <= 6}
    tight_mate = {x for x in mate if 4 <= x.bit_count() <= 6}
    assert len(tight_seed) == len(tight_mate) == 16
    assert not (tight_seed & tight_mate)
    assert not ((tight_seed | tight_mate) & core_tight)
    bank = [lookup[x] for x in seed | mate if x in lookup]
    assert sum(4 <= required[i].bit_count() <= 6 for i in bank) == 16
    banks.append(bank)
    raw.append(entry["value"])

verified = False
candidates = []
if "rational_values" in data:
    assert len(data["rational_values"]) == len(raw)
    candidates.append(("stored exact certificate",[Fraction(value) for value in data["rational_values"]]))
else:
    for denominator in (10, 100, 1000, 10000, 100000, 1000000, 10000000):
        candidates.append((denominator,[Fraction(value).limit_denominator(denominator) for value in raw]))
for denominator, values in candidates:
    if any(value < 0 for value in values):
        continue
    loads = [Fraction(0) for _ in required]
    for value, bank in zip(values, banks):
        for i in bank:
            loads[i] += value
    valid = all(load == 1 if 4 <= mask.bit_count() <= 6 else load >= 1
                for mask, load in zip(required, loads))
    if not valid:
        continue
    assert 2 * sum(values) == 32
    if args.output:
        data["verification"] = "exact literal fractional coverage, residual physical charge 32"
        data["rational_values"] = [str(value) for value in values]
        args.output.write_text(json.dumps(data,indent=2)+"\n")
    print("EXACT_FRACTIONAL_VERIFIED", "denominator_bound", denominator,
          "columns", len(values), "physical_charge", 32, flush=True)
    verified = True
    break
if not verified and args.exact_basis:
    import numpy as np
    from scipy.linalg import qr
    from flint import fmpq_mat

    active = [i for i, value in enumerate(raw) if value > 1e-9]
    matrix = np.zeros((len(required),len(active)),dtype=np.int64)
    for j, original in enumerate(active):
        for i in banks[original]:
            matrix[i,j] = 1
    numerical_loads = matrix @ np.array([raw[i] for i in active])
    candidates = [i for i, mask in enumerate(required)
                  if 4 <= mask.bit_count() <= 6 or abs(numerical_loads[i]-1) < 1e-6]
    _, triangular, pivot = qr(matrix[candidates].T.astype(float),mode="economic",pivoting=True)
    rank = sum(abs(value) > 1e-9 for value in np.diag(triangular))
    print("BASIS_CANDIDATE", "columns",len(active),"equations",len(candidates),
          "numerical_rank",int(rank),flush=True)
    if rank == len(active):
        basis = [candidates[int(i)] for i in pivot[:len(active)]]
        lhs = fmpq_mat(matrix[basis].tolist())
        rhs = fmpq_mat([[1] for _ in active])
        try:
            solution = lhs.solve(rhs,algorithm="dixon")
        except ZeroDivisionError:
            print("EXACT_BASIS_SINGULAR",flush=True)
        else:
            values = [Fraction(0) for _ in raw]
            for j, original in enumerate(active):
                values[original] = Fraction(str(solution[j,0]))
            loads = [Fraction(0) for _ in required]
            for value, bank in zip(values,banks):
                for i in bank:
                    loads[i] += value
            valid = (all(value >= 0 for value in values)
                     and all(load == 1 if 4 <= mask.bit_count() <= 6 else load >= 1
                             for mask, load in zip(required,loads))
                     and 2*sum(values) == 32)
            if valid:
                verified = True
                if args.output:
                    data["verification"] = "exact literal fractional coverage, residual physical charge 32"
                    data["rational_values"] = [str(value) for value in values]
                    data["basis_target_orbits"] = [required[i] for i in basis]
                    args.output.write_text(json.dumps(data,indent=2)+"\n")
                print("EXACT_FRACTIONAL_VERIFIED", "method","QR-selected integer basis / FLINT exact solve",
                      "columns",len(active),"physical_charge",32,
                      "max_denominator_digits",max(len(str(value.denominator)) for value in values),flush=True)
            else:
                print("EXACT_BASIS_FAILS_FULL_CONSTRAINTS",flush=True)
if not verified:
    print("RATIONAL_RECONSTRUCTION_NOT_VERIFIED", "columns",len(raw),flush=True)
