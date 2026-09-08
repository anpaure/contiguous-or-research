"""Read-only residual LP/exact-cover test for the explicit ten-row core.

No feasible result is a theorem until the literal full-cube check passes.
"""
import argparse
from collections import Counter
from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from itertools import product
import json
import os
from pathlib import Path
import subprocess
import sys


def involution(mask):
    return ((mask&31)<<5)|(mask>>5)


def support(row):
    prefix = []
    for order in row:
        p = [0]
        for label in order:p.append(p[-1]|(1<<label))
        prefix.append(p)
    return {x|y for x,y in product(*prefix)}


parser = argparse.ArgumentParser()
parser.add_argument("--global-model",action="store_true")
parser.add_argument("--seconds",type=float,default=30)
parser.add_argument("--lp-threads",type=int,default=None,
                    help="Optional HiGHS thread count, useful for parallel core screens.")
parser.add_argument("--lp-artifact",type=Path,default=None,
                    help="Save the active primal columns and values for later exact checking.")
parser.add_argument("--integer-seconds",type=float,default=0)
parser.add_argument("--catalogue",type=Path,default=None,
                    help="Catalogue executable; default is the sibling binary.")
parser.add_argument("--core",type=Path,default=None,
                    help="Core-generator module; default is the sibling SCD core.")
parser.add_argument("--workers",type=int,default=4)
parser.add_argument("--seed",type=int,default=20260907)
args = parser.parse_args()
if args.workers < 1:
    parser.error("--workers must be positive")
if args.lp_threads is not None and args.lp_threads < 1:
    parser.error("--lp-threads must be positive")
root = Path(__file__).resolve().parent
core_path = args.core or root/"binary10_involution_scd_core_20260907.py"
spec = spec_from_file_location("core",core_path.resolve())
core_module = module_from_spec(spec)
spec.loader.exec_module(core_module)
capture = StringIO()
with redirect_stdout(capture):core_module.main()
core_rows = []
for line in capture.getvalue().splitlines():
    if "|" in line:
        core_rows.append(tuple(tuple(map(int,part.split())) for part in line.split("|")))
assert len(core_rows)==10
core_supports = [support(row) for row in core_rows]
core_union = set.union(*core_supports)
core_tight = {x for x in core_union if 4<=x.bit_count()<=6}
assert len(core_tight)==160
assert sum(sum(4<=x.bit_count()<=6 for x in s) for s in core_supports)==160
catalogue = args.catalogue or root/"binary10_involution_catalogue_20260907"
command = [str(catalogue.resolve())]
if args.global_model:command.append("--all")
raw = subprocess.run(command,input=str(len(core_tight))+" "+" ".join(map(str,sorted(core_tight))),
                     text=True,capture_output=True,check=True)
print(raw.stderr.strip(),flush=True)
representatives = [x for x in range(1024) if x<=involution(x)]
assert len(representatives)==528
rank_counts = Counter(x.bit_count() for x in representatives)
assert (rank_counts[4],rank_counts[5],rank_counts[6])==(110,126,110)
required = representatives if args.global_model else [x for x in representatives if x not in core_union]
lookup = {x:i for i,x in enumerate(required)}
columns,weights,packed_rows = [],[],[]
seen_columns = set()
for line in raw.stdout.splitlines():
    weight,packed = map(int,line.split())
    permutation = tuple((packed>>(4*i))&15 for i in range(10))
    assert sorted(permutation)==list(range(10))
    s = support((permutation[:5],permutation[5:]))
    s |= {involution(x) for x in tuple(s)}
    ids = tuple(sorted(lookup[x] for x in s if x in lookup))
    key = weight,ids
    if key in seen_columns:continue
    seen_columns.add(key)
    columns.append(ids);weights.append(weight);packed_rows.append(permutation)
print("COLUMN_SUMMARY",len(columns),"required_orbits",len(required),
      "tight_orbits",sum(4<=x.bit_count()<=6 for x in required),flush=True)
degree = Counter(i for column in columns for i in column)
missing = [required[i] for i in range(len(required)) if not degree[i]]
if missing:
    print("INFEASIBLE missing-orbit certificate",missing,flush=True)
    sys.exit(0)

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

rr,cc = [],[]
for j,column in enumerate(columns):
    rr.extend(column);cc.extend([j]*len(column))
matrix = coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(required),len(columns))).tocsc()
tight = np.array([4<=x.bit_count()<=6 for x in required])
lp_options = {"time_limit":args.seconds}
if args.lp_threads is not None:
    lp_options["threads"] = args.lp_threads
result = linprog(np.array(weights,dtype=float),A_ub=-matrix[~tight],b_ub=-np.ones((~tight).sum()),
                 A_eq=matrix[tight],b_eq=np.ones(tight.sum()),bounds=(0,None),method="highs",
                 options=lp_options)
print("LP_STATUS",result.status,result.message,"objective",result.fun,
      "expected",42 if args.global_model else 32,flush=True)
if result.success:
    active = [(i,float(v)) for i,v in enumerate(result.x) if v>1e-7]
    if args.lp_artifact is not None:
        payload = {"scope":"binary10 involution residual all-rank LP",
                   "status":int(result.status), "objective":float(result.fun),
                   "core_rows":[] if args.global_model else core_rows,
                   "required_orbits":required,
                   "parameters":{name:os.environ.get(name) for name in
                                 ("BINARY10_FIXED_MATCHING","BINARY10_MATCHING_INDEX",
                                  "BINARY10_CORE_FIRST_ORDER","BINARY10_LAST_VARIANT")},
                   "active_columns":[{"row":(packed_rows[i][:5],packed_rows[i][5:]),
                                      "weight":weights[i],"value":float(value)}
                                     for i,value in enumerate(result.x) if value != 0]}
        args.lp_artifact.write_text(json.dumps(payload,indent=2)+"\n")
        print("LP_ARTIFACT",str(args.lp_artifact),flush=True)
    print("LP_ACTIVE",len(active),"integral",all(abs(v-round(v))<1e-7 for _,v in active),flush=True)
    if all(abs(v-round(v))<1e-7 for _,v in active):
        final = [] if args.global_model else list(core_rows)
        for i,value in active:
            assert round(value)==1
            p = packed_rows[i]
            row = p[:5],p[5:]
            final.append(row)
            if weights[i]==2:
                final.append(tuple(tuple((x+5)%10 for x in order) for order in row))
        loads = Counter(x for row in final for x in support(row))
        assert len(final)==42 and set(loads)==set(range(1024))
        assert all(loads[x]==1 for x in range(1024) if 4<=x.bit_count()<=6)
        print("VERIFIED_FULL_COVER",final,flush=True)
    elif args.integer_seconds:
        from ortools.sat.python import cp_model
        model = cp_model.CpModel()
        variables = [model.new_bool_var(f"r{i}") for i in range(len(columns))]
        incidence = [[] for _ in required]
        for j,column in enumerate(columns):
            for i in column:incidence[i].append(variables[j])
        for i,available in enumerate(incidence):
            if tight[i]:model.add_exactly_one(available)
            else:model.add_bool_or(available)
        model.add(sum(weight*variable for weight,variable in zip(weights,variables))
                  == (42 if args.global_model else 32))
        # A compatible partial packing gives hints, not additional constraints.
        used = set()
        hinted = []
        for j,_ in sorted(active,key=lambda item:-item[1]):
            bank = {i for i in columns[j] if tight[i]}
            if not used&bank:
                model.add_hint(variables[j],1)
                used |= bank
                hinted.append(j)
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.integer_seconds
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed
        status = solver.solve(model)
        print("INTEGER_STATUS",solver.status_name(status),"seconds",solver.wall_time,
              "hinted_orbits",len(hinted),flush=True)
        if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
            selected = [j for j,v in enumerate(variables) if solver.value(v)]
            final = [] if args.global_model else list(core_rows)
            for j in selected:
                p = packed_rows[j]
                row = p[:5],p[5:]
                final.append(row)
                if weights[j]==2:
                    final.append(tuple(tuple((x+5)%10 for x in order) for order in row))
            loads = Counter(x for row in final for x in support(row))
            assert len(final)==42 and set(loads)==set(range(1024))
            assert all(loads[x]==1 for x in range(1024) if 4<=x.bit_count()<=6)
            print("VERIFIED_FULL_COVER",final,flush=True)
