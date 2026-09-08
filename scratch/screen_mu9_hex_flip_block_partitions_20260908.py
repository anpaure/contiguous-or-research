#!/usr/bin/env python3
"""H100-only capped boundary CSP; never solves free row orders."""
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import socket
import sys
import time


def main():
    assert socket.gethostname().lower()=="arboghast", "Run only via ssh h100"
    allowed=sorted(os.sched_getaffinity(0))
    os.sched_setaffinity(0,set(allowed[:2]))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30))
    resource.setrlimit(resource.RLIMIT_CPU,(36,36))
    signal.alarm(18)
    started=time.monotonic()
    os.environ["OPENBLAS_NUM_THREADS"]="1"
    os.environ["OMP_NUM_THREADS"]="1"
    from ortools.sat.python import cp_model
    spec=importlib.util.spec_from_file_location("inventory",Path(__file__).with_name("inventory_mu9_hamilton_hex_flips_20260908.py"))
    inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
    data=json.loads(Path(sys.argv[1]).read_text())
    groups={}
    for row in data["retained_cycles"]:
        edges=[inv.edge(row["S"][i],row["U"][i]) for i in range(126)]
        edges += [inv.edge(row["S"][(i+1)%126],row["U"][i]) for i in range(126)]
        key=min(tuple(sorted(inv.edge(inv.rot(a,t),inv.rot(b,t)) for a,b in edges))
                for t in range(9))
        groups.setdefault(key,[]).append(row)
    out={"host":socket.gethostname(),"rotation_classes":len(groups),
         "class_sizes":[len(g) for g in groups.values()],"cases":[]}
    output=Path(sys.argv[2])
    def save():
        out["elapsed_seconds"]=time.monotonic()-started
        output.write_text(json.dumps(out,indent=2)+"\n")
    save()
    for group in groups.values():
        row=group[0]
        for reverse in (False,True):
            if time.monotonic()-started>16:
                save(); print(json.dumps({k:v for k,v in out.items() if k!="cases"}));return
            if reverse:
                S=[row["S"][-i%126] for i in range(126)]
                U=[row["U"][(-i-1)%126] for i in range(126)]
            else:
                S,U=row["S"],row["U"]
            V=[U[i]|U[(i+1)%126] for i in range(126)]
            blocks=[b for s in range(126) for p in range(1,6)
                    if (b:=inv.local_block(s,p,S,U,V)) is not None]
            model=cp_model.CpModel()
            x=[model.new_bool_var("x_%d_%d"%(b["s"],b["p"])) for b in blocks]
            model.add(sum(x)==42)
            covering=[[] for _ in range(126)]
            retained=[[] for _ in range(126)]
            for b,var in zip(blocks,x):
                for j in range(b["p"]):covering[(b["s"]+j)%126].append(var)
                for i in b["retained_V"]:retained[i].append(var)
            drops=[model.new_bool_var("drop_%d"%i) for i in range(126)]
            for i in range(126):
                model.add(sum(covering[i])==1)
                model.add(sum(retained[i])+drops[i]==1)
            values=sorted(set(V))
            covered=[]
            for v in values:
                z=model.new_bool_var("covered_%d"%v)
                surviving=sum(1-drops[i] for i in range(126) if V[i]==v)
                model.add(surviving>=z)
                model.add(surviving<=V.count(v)*z)
                covered.append(z)
            model.add(sum(covered)>=83)
            model.maximize(sum(covered))
            solver=cp_model.CpSolver()
            solver.parameters.max_time_in_seconds=min(0.65,max(0.05,16-time.monotonic()+started))
            solver.parameters.num_search_workers=2
            solver.parameters.random_seed=60908
            status=solver.solve(model)
            item={"representative_id":row["id"],"represented_ids":[r["id"] for r in group],
                  "reverse":reverse,"source_V_coverage":len(values),
                  "status":solver.status_name(status),"solver_wall_seconds":solver.wall_time,
                  "core":row["core"],"abc":row["abc"]}
            if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
                chosen=[b for b,var in zip(blocks,x) if solver.value(var)]
                assert len(chosen)==42
                coverage=[0]*126; keep=[0]*126
                for b in chosen:
                    for j in range(b["p"]):coverage[(b["s"]+j)%126]+=1
                    for i in b["retained_V"]:keep[i]+=1
                assert set(coverage)=={1} and set(keep)<={0,1} and sum(keep)==84
                kept={V[i] for i in range(126) if keep[i]}
                assert len(kept)>=83
                item.update({"rank6_retained_distinct":len(kept),
                             "missing_rank6":sorted(v for v in range(512) if v.bit_count()==6 and v not in kept),
                             "blocks":[[b["s"],b["p"]] for b in sorted(chosen,key=lambda b:b["s"])],
                             "S":S,"U":U,"V":V})
            out["cases"].append(item); save()
    save()
    print(json.dumps({"rotation_classes":out["rotation_classes"],"class_sizes":out["class_sizes"],
                      "elapsed_seconds":out["elapsed_seconds"],
                      "cases":[{k:v for k,v in c.items() if k not in ("S","U","V","blocks")} for c in out["cases"]]},indent=2))


if __name__=="__main__":main()
