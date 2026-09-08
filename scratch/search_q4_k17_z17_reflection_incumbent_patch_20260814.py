#!/usr/bin/env python3
"""Exact LNS patch around a low-energy reflection incumbent (H100 only)."""

from __future__ import annotations

import argparse
import json
import sys

from ortools.sat.python import cp_model

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_quotient_exact_cover_20260814 import verify_development


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--time-limit", type=float, default=300)
    parser.add_argument("--workers", type=int, default=32)
    args = parser.parse_args()
    _, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    state = json.load(open(args.state, encoding="utf-8"))
    chosen_self = state["self_indices"]
    chosen_pairs = state["pair_indices"]
    loads = [0] * 680
    for i in chosen_self:
        for row in self_options[i][2]: loads[row] += 1
    for i in chosen_pairs:
        for row in pairs[i][1]: loads[row] += 1
    assert sum((load-1)**2 for load in loads) == state["energy"] == 116

    stable_self = [i for i in chosen_self
                   if all(loads[row] == 1 for row in self_options[i][2])]
    stable_pairs = [i for i in chosen_pairs
                    if all(loads[row] == 1 for row in pairs[i][1])]
    destroyed_self = [i for i in chosen_self if i not in set(stable_self)]
    destroyed_pairs = [i for i in chosen_pairs if i not in set(stable_pairs)]
    destroyed_groups = {self_options[i][0] for i in destroyed_self}
    assert len(stable_self)==18 and len(stable_pairs)==9
    assert len(destroyed_self)==17 and len(destroyed_pairs)==45
    assert len(destroyed_groups)==17

    outside = set()
    for i in stable_self:
        assert outside.isdisjoint(self_options[i][2]); outside.update(self_options[i][2])
    for i in stable_pairs:
        assert outside.isdisjoint(pairs[i][1]); outside.update(pairs[i][1])
    patch_rows = set(range(680)) - outside
    assert len(outside)==162 and len(patch_rows)==518

    eligible_self = [i for i,(group,_,rows) in enumerate(self_options)
                     if group in destroyed_groups and set(rows) <= patch_rows]
    eligible_pairs = [i for i,(_,rows) in enumerate(pairs)
                      if set(rows) <= patch_rows]
    self_vars = {i: None for i in eligible_self}
    pair_vars = {i: None for i in eligible_pairs}
    model = cp_model.CpModel()
    for i in self_vars: self_vars[i]=model.NewBoolVar(f"self_{i}")
    for i in pair_vars: pair_vars[i]=model.NewBoolVar(f"pair_{i}")
    for group in destroyed_groups:
        options=[self_vars[i] for i in eligible_self if self_options[i][0]==group]
        assert options; model.AddExactlyOne(options)
    incidence={row:[] for row in patch_rows}
    for i,var in self_vars.items():
        for row in self_options[i][2]: incidence[row].append(var)
    for i,var in pair_vars.items():
        for row in pairs[i][1]: incidence[row].append(var)
    assert all(incidence.values())
    for row in incidence.values(): model.AddExactlyOne(row)
    model.Add(sum(pair_vars.values()) == 45)
    for i,var in self_vars.items(): model.AddHint(var,int(i in destroyed_self))
    for i,var in pair_vars.items(): model.AddHint(var,int(i in destroyed_pairs))

    solver=cp_model.CpSolver()
    solver.parameters.max_time_in_seconds=args.time_limit
    solver.parameters.num_search_workers=args.workers
    solver.parameters.random_seed=args.seed
    solver.parameters.repair_hint=True
    solver.parameters.hint_conflict_limit=200000
    status=solver.Solve(model)
    report={
        "status":solver.StatusName(status), "patch_rows":len(patch_rows),
        "stable_self":len(stable_self), "stable_pairs":len(stable_pairs),
        "destroyed_self":len(destroyed_self), "destroyed_pairs":len(destroyed_pairs),
        "eligible_self":len(eligible_self), "eligible_pairs":len(eligible_pairs),
        "min_patch_degree":min(map(len,incidence.values())),
        "max_patch_degree":max(map(len,incidence.values())),
        "wall_time":solver.WallTime(), "branches":solver.NumBranches(),
        "conflicts":solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        final_self=stable_self+[i for i,v in self_vars.items() if solver.Value(v)]
        final_pairs=stable_pairs+[i for i,v in pair_vars.items() if solver.Value(v)]
        assert len(final_self)==35 and len(final_pairs)==54
        chosen=[self_options[i][1] for i in final_self]
        for i in final_pairs: chosen.extend(pairs[i][0])
        assert len(chosen)==143
        owner_load=[0]*1430
        for column in chosen:
            for vertex in column["edge"]: owner_load[vertex]+=1
        assert set(owner_load)=={1}
        normalized=[
            {"core":tuple(column["core"]),"order":tuple(column["order"]),
             "edge":tuple(column["edge"])} for column in chosen
        ]
        rails,owners,point=verify_development(normalized)
        report.update({
            "selected_rail_orbits":143,"developed_rails":rails,
            "covered_owners":owners,"point_degree":sorted(set(point.values())),
            "certificate":[
                {"core":list(column["core"]),"order":list(column["order"]),
                 "quotient_edge":list(column["edge"])} for column in normalized
            ],
        })
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=="__main__": main()
