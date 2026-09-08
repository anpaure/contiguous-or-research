#!/usr/bin/env python3
"""H100-only exact unit-proof and guarded-target certificate extraction."""
from collections import Counter
import json
from pathlib import Path
import resource
import socket
import sys
import time


def clauses_for(V,hole):
    clauses=[[1+(start+j)%126 for j in range(5)] for start in range(126)]
    for value in range(512):
        if value.bit_count()==6 and value!=hole:
            clauses.append([-(i+1) for i,v in enumerate(V) if v==value])
    return clauses


def unit_proof(clauses):
    known={}; trace=[]
    while True:
        changed=False
        for ci,clause in enumerate(clauses):
            if any(abs(lit) in known and known[abs(lit)]==(lit>0) for lit in clause):
                continue
            free=[lit for lit in clause if abs(lit) not in known]
            if not free:
                return {"trace":trace,"contradiction_clause":ci}
            if len(free)==1:
                lit=free[0]
                known[abs(lit)]=(lit>0)
                trace.append([ci,lit]);changed=True
        if not changed:
            return None


def verify_proof(clauses,proof):
    known={}
    for ci,lit in proof["trace"]:
        assert abs(lit) not in known and lit in clauses[ci]
        others=[x for x in clauses[ci] if x!=lit]
        assert all(abs(x) in known and known[abs(x)]!=(x>0) for x in others)
        known[abs(lit)]=(lit>0)
    assert all(abs(x) in known and known[abs(x)]!=(x>0)
               for x in clauses[proof["contradiction_clause"]])


def guard_certificates(V):
    multiplicity=Counter(V)
    candidates=[]
    for q in sorted(multiplicity):
        witnesses=[];support={q}
        for x,value in enumerate(V):
            if value!=q:continue
            choices=[]
            for back in range(4,-1,-1):
                start=(x-back)%126
                indices=[(start+j)%126 for j in range(5)]
                other=[i for i in indices if i!=x]
                if len(other)==4 and all(multiplicity[V[i]]==1 for i in other):
                    choices.append((len(support|{V[i] for i in other}),start,other))
            if not choices:break
            _,start,other=min(choices)
            witnesses.append({"occurrence":x,"window_start":start,
                              "unique_guard_indices":other})
            support.update(V[i] for i in other)
        else:
            candidates.append({"q":q,"support":sorted(support),"witnesses":witnesses})
    missing={v for v in range(512) if v.bit_count()==6 and v not in multiplicity}
    possible=set(missing) if missing else {v for v in range(512) if v.bit_count()==6}
    chosen=[]
    while possible:
        useful=[c for c in candidates if len(possible&set(c["support"]))<len(possible)]
        if not useful:break
        cert=min(useful,key=lambda c:(len(possible&set(c["support"])),len(c["support"]),c["q"]))
        chosen.append(cert)
        possible &= set(cert["support"])
    return {"intrinsically_missing":sorted(missing),"chosen":chosen,
            "possible_single_hole_after_guards":sorted(possible),
            "guard_proof_complete":not possible,
            "periodic_target_guards":[c for c in candidates if c["q"] in (219,365,438)]}


def main():
    assert socket.gethostname().lower()=="arboghast", "Run only via ssh h100"
    resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30))
    started=time.monotonic()
    inventory=json.loads(Path(sys.argv[1]).read_text())
    partitions=json.loads(Path(sys.argv[2]).read_text())
    reps=[c for c in partitions["cases"] if not c["reverse"]]
    byid={row["id"]:row for row in inventory["retained_cycles"]}
    certs=[]
    for case in reps:
        row=byid[case["representative_id"]];V=row["V"]
        absent=[v for v in range(512) if v.bit_count()==6 and v not in V]
        holes=absent if absent else [v for v in range(512) if v.bit_count()==6]
        proofs=[];stalled=[]
        for hole in holes:
            clauses=clauses_for(V,hole)
            proof=unit_proof(clauses)
            if proof is None:stalled.append(hole)
            else:
                verify_proof(clauses,proof)
                proofs.append({"allowed_hole":hole,**proof})
        guards=guard_certificates(V)
        certs.append({"representative_id":row["id"],"represented_ids":case["represented_ids"],
                      "core":row["core"],"abc":row["abc"],"V":V,
                      "unit_proof_cases":proofs,"unit_proof_stalled_holes":stalled,
                      "guard_certificate":guards})
    report={"host":socket.gethostname(),"elapsed_seconds":time.monotonic()-started,
            "scope":"independent necessary drop-spacing clauses, ignoring local row feasibility and exactly42 blocks",
            "all_classes_unit_refuted":all(not c["unit_proof_stalled_holes"] for c in certs),
            "all_classes_guard_refuted":all(c["guard_certificate"]["guard_proof_complete"] for c in certs),
            "certificates":certs}
    Path(sys.argv[3]).write_text(json.dumps(report,indent=2)+"\n")
    summary={k:v for k,v in report.items() if k!="certificates"}
    summary["classes"]=[{"representative_id":c["representative_id"],
                         "stalled_holes":c["unit_proof_stalled_holes"],
                         "guard_certificate":c["guard_certificate"]} for c in certs]
    print(json.dumps(summary,indent=2))


if __name__=="__main__":main()
