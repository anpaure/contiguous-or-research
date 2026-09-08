"""Remote-only LP-guided column-pool search for a literal binary10 core.

All rank constraints remain active. Restricted-pool infeasibility says nothing
about the complete catalogue. Only a literal 1024-target verification can
produce VERIFIED_FULL_COVER.
"""
import argparse
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import shutil
import subprocess
import time


def involution(mask):
    return ((mask & 31) << 5) | (mask >> 5)


def support(row):
    assert len(row) == 2 and len(row[0]) == len(row[1]) == 5
    assert sorted(list(row[0])+list(row[1])) == list(range(10))
    prefixes = []
    for order in row:
        values = [0]
        for label in order:
            values.append(values[-1] | (1 << label))
        prefixes.append(values)
    bank = {x | y for x, y in product(*prefixes)}
    assert len(bank) == 36
    return bank


def mate_row(row):
    return tuple(tuple((x+5) % 10 for x in order) for order in row)


def check_final(rows):
    """Independent literal enumeration, without consulting the LP incidence."""
    assert len(rows) == 42
    loads = Counter(mask for row in rows for mask in support(row))
    assert set(loads) == set(range(1024))
    assert all(loads[mask] == 1 for mask in range(1024)
               if 4 <= mask.bit_count() <= 6)
    return [loads[mask] for mask in range(1024)]


parser = argparse.ArgumentParser()
parser.add_argument("--core-artifact",required=True,type=Path)
parser.add_argument("--catalogue",required=True,type=Path)
parser.add_argument("--output",required=True,type=Path)
parser.add_argument("--lp-rounds",type=int,default=8)
parser.add_argument("--lp-seconds",type=float,default=30)
parser.add_argument("--cp-seconds",type=float,default=900)
parser.add_argument("--workers",type=int,default=16)
parser.add_argument("--seed",type=int,default=20260913)
args = parser.parse_args()
assert args.output.is_dir() and args.output.name.startswith("run-")
assert 1 <= args.workers <= 16 and 0 < args.cp_seconds <= 900
assert 0 <= args.lp_rounds <= 16
out = args.output.resolve()
started = time.monotonic()
input_bytes = args.core_artifact.read_bytes()
data = json.loads(input_bytes)
core = data["core_rows"]
core_banks = [support(row) for row in core]
assert len(core) == 10
core_union = set.union(*core_banks)
assert {involution(x) for x in core_union} == core_union
core_tight = {x for x in core_union if 4 <= x.bit_count() <= 6}
assert len(core_tight) == 160
assert sum(sum(4 <= x.bit_count() <= 6 for x in bank) for bank in core_banks) == 160
fixed_tight = {x for x in range(1024) if involution(x) == x
               and 4 <= x.bit_count() <= 6}
assert fixed_tight <= core_tight
required = [x for x in range(1024) if x <= involution(x) and x not in core_union]
assert required == data["required_orbits"]
lookup = {x:i for i,x in enumerate(required)}
tight_ids = {i for i,x in enumerate(required) if 4 <= x.bit_count() <= 6}
assert len(tight_ids) == 256
shutil.copy2(args.core_artifact,out/"input_primal.json")
shutil.copy2(__file__,out/Path(__file__).name)
identity = {"input_sha256":sha256(input_bytes).hexdigest(),
            "catalogue_sha256":sha256(args.catalogue.read_bytes()).hexdigest(),
            "parameters":data.get("parameters"),
            "lp_rounds":args.lp_rounds,"lp_seconds":args.lp_seconds,
            "cp_seconds":args.cp_seconds,"workers":args.workers,"seed":args.seed}
(out/"identity.json").write_text(json.dumps(identity,indent=2)+"\n")
print("CHOSEN_CORE",json.dumps(identity,sort_keys=True),flush=True)

raw = subprocess.run([str(args.catalogue.resolve())],
                     input=str(len(core_tight))+" "+" ".join(map(str,sorted(core_tight))),
                     text=True,capture_output=True,check=True)
print(raw.stderr.strip(),flush=True)
columns, rows, by_support = [], [], {}
for line in raw.stdout.splitlines():
    weight, packed = map(int,line.split())
    assert weight == 2
    permutation = tuple((packed >> (4*i)) & 15 for i in range(10))
    row = permutation[:5], permutation[5:]
    seed_bank, mate_bank = support(row), support(mate_row(row))
    seed_tight = {x for x in seed_bank if 4 <= x.bit_count() <= 6}
    mate_tight = {x for x in mate_bank if 4 <= x.bit_count() <= 6}
    assert len(seed_tight) == len(mate_tight) == 16
    assert not seed_tight & mate_tight
    assert not (seed_tight | mate_tight) & core_tight
    ids = tuple(sorted(lookup[x] for x in seed_bank | mate_bank if x in lookup))
    assert len(set(ids) & tight_ids) == 16
    if ids in by_support:
        continue
    by_support[ids] = len(columns)
    columns.append(ids)
    rows.append(row)
print("FULL_CATALOGUE",len(columns),"required_orbits",len(required),flush=True)

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

rr, cc = [], []
for j, bank in enumerate(columns):
    rr.extend(bank)
    cc.extend([j]*len(bank))
matrix = coo_matrix((np.ones(len(rr)),(rr,cc)),
                    shape=(len(required),len(columns))).tocsc()
tight = np.array([i in tight_ids for i in range(len(required))])
pool, scored_solutions = set(), []
baseline = []
for entry in data["active_columns"]:
    if entry["value"] <= 0:
        continue
    row = entry["row"]
    bank = support(row) | support(mate_row(row))
    ids = tuple(sorted(lookup[x] for x in bank if x in lookup))
    j = by_support[ids]
    pool.add(j)
    baseline.append((j,float(entry["value"])))
scored_solutions.append(baseline)
print("INITIAL_POOL",len(pool),flush=True)

def write_candidate(selected, method):
    final = list(core)
    for j in selected:
        final.extend((rows[j],mate_row(rows[j])))
    loads = check_final(final)
    witness = {"rows":final,"target_loads":loads,"method":method,
               "input_sha256":identity["input_sha256"]}
    (out/"verified_witness.json").write_text(json.dumps(witness,indent=2)+"\n")
    print("VERIFIED_FULL_COVER",json.dumps(final),flush=True)

rng = np.random.default_rng(args.seed)
lp_records = []
for round_id in range(args.lp_rounds):
    objective = 2 + 0.01*rng.uniform(-1,1,len(columns))
    result = linprog(objective,A_ub=-matrix[~tight],b_ub=-np.ones((~tight).sum()),
                     A_eq=matrix[tight],b_eq=np.ones(tight.sum()),bounds=(0,None),
                     method="highs",options={"time_limit":args.lp_seconds,"threads":1})
    record = {"round":round_id,"status":int(result.status),"message":result.message,
              "objective":None if result.fun is None else float(result.fun)}
    if result.success:
        active = [(j,float(value)) for j,value in enumerate(result.x) if value > 1e-9]
        new = {j for j,_ in active} - pool
        pool.update(j for j,_ in active)
        scored_solutions.append(active)
        record.update(active=len(active),new_columns=len(new),pool_size=len(pool))
        artifact = {"scope":"binary10 involution residual all-rank randomized LP",
                    "core_rows":core,"required_orbits":required,
                    "parameters":data.get("parameters"),"random_round":round_id,
                    "objective_seed":args.seed,"objective":float(result.fun),
                    "active_columns":[{"row":rows[j],"weight":2,"value":float(value)}
                                      for j,value in enumerate(result.x) if value != 0]}
        (out/f"random-lp-{round_id:02d}.json").write_text(json.dumps(artifact,indent=2)+"\n")
        if all(abs(value-round(value)) < 1e-7 for _,value in active):
            selected = [j for j,value in active if round(value) == 1]
            try:
                write_candidate(selected,"rounded randomized LP, independently checked literally")
            except AssertionError:
                print("ROUNDED_LP_CANDIDATE_FAILED_LITERAL_CHECK",flush=True)
            else:
                raise SystemExit(0)
    lp_records.append(record)
    print("RANDOM_LP",json.dumps(record,sort_keys=True),flush=True)
(out/"lp_records.json").write_text(json.dumps(lp_records,indent=2)+"\n")
selected_pool = sorted(pool)
pool_data = {"core_rows":core,"required_orbits":required,
             "columns":[{"global_id":j,"row":rows[j],"target_ids":columns[j]}
                        for j in selected_pool]}
(out/"restricted_pool.json").write_text(json.dumps(pool_data,indent=2)+"\n")
incidence = [[] for _ in required]
for local,j in enumerate(selected_pool):
    for i in columns[j]:
        incidence[i].append(local)
missing = [required[i] for i, bank in enumerate(incidence) if not bank]
print("RESTRICTED_POOL",len(selected_pool),"missing_target_orbits",missing,flush=True)
if missing:
    print("POOL_INCOMPLETE_NOT_GLOBAL_INFEASIBILITY",flush=True)
    raise SystemExit(0)

from ortools.sat.python import cp_model
model = cp_model.CpModel()
variables = [model.new_bool_var(f"r{j}") for j in selected_pool]
for i, bank in enumerate(incidence):
    available = [variables[local] for local in bank]
    if tight[i]:
        model.add_exactly_one(available)
    else:
        model.add_bool_or(available)
model.add(sum(variables) == 16)
best_hint = []
for solution in scored_solutions:
    used, hint = set(), []
    for j,value in sorted(solution,key=lambda item:-item[1]):
        bank = set(columns[j]) & tight_ids
        if not used & bank:
            used |= bank
            hint.append(j)
    if len(hint) > len(best_hint):
        best_hint = hint
local_ids = {j:local for local,j in enumerate(selected_pool)}
for j in best_hint:
    model.add_hint(variables[local_ids[j]],1)
solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = args.cp_seconds
solver.parameters.num_search_workers = args.workers
solver.parameters.random_seed = args.seed
print("RESTRICTED_CP_START", "columns",len(selected_pool),"hinted_rows",len(best_hint),
      "workers",args.workers,"requested_seconds",args.cp_seconds,flush=True)
status = solver.solve(model)
record = {"status":solver.status_name(status),"seconds":solver.wall_time,
          "scope":"restricted LP-guided pool only","pool_size":len(selected_pool),
          "full_catalogue_size":len(columns),"elapsed_total":time.monotonic()-started}
(out/"integer_status.json").write_text(json.dumps(record,indent=2)+"\n")
print("RESTRICTED_INTEGER_STATUS",json.dumps(record,sort_keys=True),flush=True)
if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
    chosen = [selected_pool[local] for local,variable in enumerate(variables)
              if solver.value(variable)]
    write_candidate(chosen,"integral exact cover from LP-guided restricted pool")
elif status == cp_model.INFEASIBLE:
    print("RESTRICTED_POOL_INFEASIBLE_NOT_GLOBAL_INFEASIBILITY",flush=True)
