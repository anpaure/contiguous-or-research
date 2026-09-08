#!/usr/bin/env python3
"""Exact defect-vertex-cover patch of a bracelet incumbent (H100 only)."""

from __future__ import annotations

import argparse,json,random,sys
from ortools.sat.python import cp_model

sys.path.insert(0,"scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_quotient_exact_cover_20260814 import verify_development


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--map",required=True); ap.add_argument("--state",required=True)
    ap.add_argument("--sample",type=int,default=0); ap.add_argument("--seed",type=int,default=20260814)
    ap.add_argument("--cover-seed",type=int,default=1)
    ap.add_argument("--cover-size",type=int)
    ap.add_argument("--objective",choices=("weight","count","random"),default="weight")
    ap.add_argument("--time-limit",type=float,default=300); ap.add_argument("--workers",type=int,default=32)
    a=ap.parse_args(); rng=random.Random(a.cover_seed)
    _,S,P=make_instance(a.map,a.sample,a.seed); state=json.load(open(a.state))
    cs=state["self_indices"]; cp=state["pair_indices"]
    vertices=[("s",i) for i in cs]+[("p",i) for i in cp]; vid={v:j for j,v in enumerate(vertices)}
    rows=[[] for _ in range(680)]
    for i in cs:
        for r in S[i][2]: rows[r].append(vid[("s",i)])
    for i in cp:
        for r in P[i][1]: rows[r].append(vid[("p",i)])
    assert {len(x) for x in rows}=={0,1,2} and sum(len(x)==0 for x in rows)==58
    edges=[tuple(x) for x in rows if len(x)==2]; assert len(edges)==58

    cover=cp_model.CpModel(); x=[cover.NewBoolVar(f"v{j}") for j in range(len(vertices))]
    for u,v in edges: cover.Add(x[u]+x[v]>=1)
    if a.cover_size is not None: cover.Add(sum(x)==a.cover_size)
    if a.objective=="weight": coeff=[4 if kind=="s" else 10 for kind,_ in vertices]
    elif a.objective=="count": coeff=[1]*len(vertices)
    else: coeff=[1000+(rng.randrange(997)) for _ in vertices]
    cover.Minimize(sum(c*z for c,z in zip(coeff,x)))
    covsolver=cp_model.CpSolver(); covsolver.parameters.num_search_workers=a.workers
    covsolver.parameters.max_time_in_seconds=30; covsolver.parameters.random_seed=a.seed
    covstatus=covsolver.Solve(cover); assert covstatus==cp_model.OPTIMAL
    R={vertices[j] for j,z in enumerate(x) if covsolver.Value(z)}
    ds=[i for kind,i in R if kind=="s"]; dp=[i for kind,i in R if kind=="p"]
    ss=[i for i in cs if ("s",i) not in R]; sp=[i for i in cp if ("p",i) not in R]
    groups={S[i][0] for i in ds}; assert len(groups)==len(ds)
    outside=set()
    for i in ss:
        assert outside.isdisjoint(S[i][2]); outside.update(S[i][2])
    for i in sp:
        assert outside.isdisjoint(P[i][1]); outside.update(P[i][1])
    F=set(range(680))-outside; assert len(F)==4*len(ds)+10*len(dp)
    ES=[i for i,(g,_,rr) in enumerate(S) if g in groups and set(rr)<=F]
    EP=[i for i,(_,rr) in enumerate(P) if set(rr)<=F]
    m=cp_model.CpModel(); sv={i:m.NewBoolVar(f"s{i}") for i in ES}; pv={i:m.NewBoolVar(f"p{i}") for i in EP}
    group_options={g:[sv[i] for i in ES if S[i][0]==g] for g in groups}
    incidence={r:[] for r in F}
    for i,z in sv.items():
        for r in S[i][2]: incidence[r].append(z)
    for i,z in pv.items():
        for r in P[i][1]: incidence[r].append(z)
    report={"cover_objective":a.objective,"defect_edges":58,"destroyed_self":len(ds),
            "destroyed_pairs":len(dp),"patch_rows":len(F),"eligible_self":len(ES),
            "eligible_pairs":len(EP),"zero_groups":sum(not q for q in group_options.values()),
            "zero_rows":sum(not q for q in incidence.values())}
    if report["zero_groups"] or report["zero_rows"]:
        report["status"]="STRUCTURAL_ZERO"; print(json.dumps(report,indent=2,sort_keys=True)); return
    for q in group_options.values(): m.AddExactlyOne(q)
    for q in incidence.values(): m.AddExactlyOne(q)
    m.Add(sum(pv.values())==len(dp))
    for i,z in sv.items(): m.AddHint(z,int(i in ds))
    for i,z in pv.items(): m.AddHint(z,int(i in dp))
    sol=cp_model.CpSolver(); sol.parameters.max_time_in_seconds=a.time_limit
    sol.parameters.num_search_workers=a.workers; sol.parameters.random_seed=a.seed
    sol.parameters.repair_hint=True; sol.parameters.hint_conflict_limit=200000
    status=sol.Solve(m); report.update({"status":sol.StatusName(status),"wall_time":sol.WallTime(),
        "branches":sol.NumBranches(),"conflicts":sol.NumConflicts(),
        "min_degree":min(map(len,incidence.values())),"max_degree":max(map(len,incidence.values()))})
    if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
        fs=ss+[i for i,z in sv.items() if sol.Value(z)]; fp=sp+[i for i,z in pv.items() if sol.Value(z)]
        assert len(fs)==35 and len(fp)==54
        chosen=[S[i][1] for i in fs]
        for i in fp: chosen.extend(P[i][0])
        loads=[0]*1430
        for c in chosen:
            for v in c["edge"]:loads[v]+=1
        assert set(loads)=={1}
        norm=[{"core":tuple(c["core"]),"order":tuple(c["order"]),"edge":tuple(c["edge"])} for c in chosen]
        rails,owners,point=verify_development(norm)
        report.update({"selected_rail_orbits":143,"developed_rails":rails,"covered_owners":owners,
            "point_degree":sorted(set(point.values())),"certificate":[
            {"core":list(c["core"]),"order":list(c["order"]),"quotient_edge":list(c["edge"])} for c in norm]})
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":main()
