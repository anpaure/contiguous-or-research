#!/usr/bin/env python3
"""Complete PPS, PSS, and SSS depth-three exchange oracle for a finite face."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def mask(rows) -> int:
    value = 0
    for row in rows:
        value |= 1 << int(row)
    return value


def hist(loads: np.ndarray) -> dict[str, int]:
    return {str(v): int(n) for v, n in sorted(Counter(loads).items())}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--instance", required=True)
    ap.add_argument("--state", required=True)
    ap.add_argument("--output-state", required=True)
    ap.add_argument("--report", required=True)
    ap.add_argument("--progress-every", type=int, default=5_000)
    args = ap.parse_args()
    started = time.time()

    _, _, self_raw, pair_raw = read_instance(args.instance)
    pr = np.asarray(pair_raw, dtype=np.int16)
    sr = np.asarray([x[1] for x in self_raw], dtype=np.int16)
    sg = np.asarray([x[0] for x in self_raw], dtype=np.int16)
    pm = [mask(x) for x in pair_raw]
    sm = [mask(x[1]) for x in self_raw]
    groups = [np.flatnonzero(sg == g) for g in range(35)]
    state = json.loads(Path(args.state).read_text())
    sp = np.asarray(state["pair_indices"], dtype=np.int32)
    ss = np.asarray(sorted(state["self_indices"], key=lambda i: self_raw[i][0]), dtype=np.int32)
    if len(sp) != 54 or [self_raw[i][0] for i in ss] != list(range(35)):
        raise ValueError("invalid selected configuration profile")
    loads = np.zeros(680, dtype=np.int16)
    for i in ss: loads[sr[i]] += 1
    for i in sp: loads[pr[i]] += 1
    energy = int(((loads - 1) ** 2).sum())
    if energy != state["energy"]: raise ValueError("state energy replay mismatch")

    psel, ssel = pr[sp], sr[ss]
    pa = (2 * loads[pr] - 1).sum(1).astype(np.int16)
    sa = (2 * loads[sr] - 1).sum(1).astype(np.int16)
    prem = (3 - 2 * loads[psel]).sum(1).astype(np.int16)
    srem = (3 - 2 * loads[ssel]).sum(1).astype(np.int16)
    pvp = np.empty((len(pr), 54), np.uint8)
    svp = np.empty((len(sr), 54), np.uint8)
    for j, rows in enumerate(psel):
        pvp[:, j] = np.isin(pr, rows).sum(1)
        svp[:, j] = np.isin(sr, rows).sum(1)
    pvs = np.empty((len(pr), 35), np.uint8)
    svs = np.empty((len(sr), 35), np.uint8)
    for g, rows in enumerate(ssel):
        pvs[:, g] = np.isin(pr, rows).sum(1)
        svs[:, g] = np.isin(sr, rows).sum(1)
    unp = np.ones(len(pr), bool); unp[sp] = False

    best = None
    counts = {"pps_faces": 0, "pss_faces": 0, "sss_faces": 0,
              "pps_survivors": 0, "pss_survivors": 0, "sss_survivors": 0,
              "pps_tests": 0, "pss_tests": 0, "sss_tests": 0}
    audit = []
    face_no = 0

    # Two reflected pairs plus one group-preserving self lift.
    for a, b in itertools.combinations(range(54), 2):
        for g in range(35):
            face_no += 1; counts["pps_faces"] += 1
            if args.progress_every and face_no % args.progress_every == 0:
                print(json.dumps({"faces": face_no, "elapsed": time.time()-started,
                                  "tests": sum(counts[k] for k in ("pps_tests","pss_tests","sss_tests"))}),
                      file=sys.stderr, flush=True)
            c = int(prem[a] + prem[b] + srem[g]
                    + 2*((pm[sp[a]] & pm[sp[b]]).bit_count()
                         +(pm[sp[a]] & sm[ss[g]]).bit_count()
                         +(pm[sp[b]] & sm[ss[g]]).bit_count()))
            hp = pa - 2*pvp[:,a] - 2*pvp[:,b] - 2*pvs[:,g]
            hp[sp] = 30000
            hs = sa - 2*svp[:,a] - 2*svp[:,b] - 2*svs[:,g]
            alt = groups[g][groups[g] != ss[g]]
            mins = np.argpartition(hp, 1)[:2]
            mins = sorted(map(int, mins), key=lambda x:(int(hp[x]),x))
            m1,m2 = map(lambda x:int(hp[x]), mins)
            ms = int(hs[alt].min())
            if c+m1+m2+ms >= 0: continue
            keep = unp & (c+hp+m1+ms < 0)
            keep[mins[0]] = c+int(hp[mins[0]])+m2+ms < 0
            pc = np.flatnonzero(keep)
            sc = alt[c+hs[alt]+m1+m2 < 0]
            counts["pps_survivors"] += 1
            face_best = None
            for ix,n in enumerate(pc):
                n=int(n)
                for m in pc[ix+1:]:
                    m=int(m); q=int(hp[n]+hp[m]+2*(pm[n]&pm[m]).bit_count())
                    if c+q+ms >= 0: continue
                    for t in sc:
                        t=int(t)
                        if hs[t] >= -c-q: continue
                        counts["pps_tests"] += 1
                        d=int(c+q+hs[t]+2*((pm[n]&sm[t]).bit_count()+(pm[m]&sm[t]).bit_count()))
                        cand=(d,"PPS",int(sp[a]),int(sp[b]),int(ss[g]),n,m,t)
                        if face_best is None or cand<face_best: face_best=cand
                        if best is None or cand<best: best=cand
            audit.append({"kind":"PPS","out":[int(sp[a]),int(sp[b]),int(ss[g])],
                          "pc":len(pc),"sc":len(sc),"best":None if face_best is None else face_best[0]})

    # One reflected pair plus two group-preserving self lifts.
    for a in range(54):
        for g,h in itertools.combinations(range(35),2):
            face_no += 1; counts["pss_faces"] += 1
            if args.progress_every and face_no % args.progress_every == 0:
                print(json.dumps({"faces": face_no, "elapsed": time.time()-started,
                                  "tests": sum(counts[k] for k in ("pps_tests","pss_tests","sss_tests"))}),
                      file=sys.stderr, flush=True)
            c=int(prem[a]+srem[g]+srem[h]
                  +2*((pm[sp[a]]&sm[ss[g]]).bit_count()+(pm[sp[a]]&sm[ss[h]]).bit_count()
                      +(sm[ss[g]]&sm[ss[h]]).bit_count()))
            hp=pa-2*pvp[:,a]-2*pvs[:,g]-2*pvs[:,h]; hp[sp]=30000
            hs=sa-2*svp[:,a]-2*svs[:,g]-2*svs[:,h]
            ag=groups[g][groups[g]!=ss[g]]; ah=groups[h][groups[h]!=ss[h]]
            mp=int(hp.min()); mg=int(hs[ag].min()); mh=int(hs[ah].min())
            if c+mp+mg+mh>=0: continue
            pc=np.flatnonzero(unp&(c+hp+mg+mh<0))
            gc=ag[c+hs[ag]+mp+mh<0]; hc=ah[c+hs[ah]+mp+mg<0]
            counts["pss_survivors"] += 1; face_best=None
            for n in pc:
                n=int(n)
                for t in gc:
                    t=int(t); q=int(hp[n]+hs[t]+2*(pm[n]&sm[t]).bit_count())
                    if c+q+mh>=0: continue
                    for u in hc:
                        u=int(u)
                        if hs[u]>=-c-q: continue
                        counts["pss_tests"] += 1
                        d=int(c+q+hs[u]+2*((pm[n]&sm[u]).bit_count()+(sm[t]&sm[u]).bit_count()))
                        cand=(d,"PSS",int(sp[a]),int(ss[g]),int(ss[h]),n,t,u)
                        if face_best is None or cand<face_best: face_best=cand
                        if best is None or cand<best: best=cand
            audit.append({"kind":"PSS","out":[int(sp[a]),int(ss[g]),int(ss[h])],
                          "pc":len(pc),"gc":len(gc),"hc":len(hc),"best":None if face_best is None else face_best[0]})

    # Three group-preserving self lifts.
    for g,h,k in itertools.combinations(range(35),3):
        face_no += 1; counts["sss_faces"] += 1
        hs=sa-2*svs[:,g]-2*svs[:,h]-2*svs[:,k]
        ag=groups[g][groups[g]!=ss[g]]; ah=groups[h][groups[h]!=ss[h]]; ak=groups[k][groups[k]!=ss[k]]
        mg=int(hs[ag].min()); mh=int(hs[ah].min()); mk=int(hs[ak].min())
        c=int(srem[g]+srem[h]+srem[k]+2*((sm[ss[g]]&sm[ss[h]]).bit_count()
              +(sm[ss[g]]&sm[ss[k]]).bit_count()+(sm[ss[h]]&sm[ss[k]]).bit_count()))
        if c+mg+mh+mk>=0: continue
        gc=ag[c+hs[ag]+mh+mk<0]; hc=ah[c+hs[ah]+mg+mk<0]; kc=ak[c+hs[ak]+mg+mh<0]
        counts["sss_survivors"] += 1; face_best=None
        for t in gc:
            t=int(t)
            for u in hc:
                u=int(u); q=int(hs[t]+hs[u]+2*(sm[t]&sm[u]).bit_count())
                if c+q+mk>=0: continue
                for v in kc:
                    v=int(v)
                    if hs[v]>=-c-q: continue
                    counts["sss_tests"] += 1
                    d=int(c+q+hs[v]+2*((sm[t]&sm[v]).bit_count()+(sm[u]&sm[v]).bit_count()))
                    cand=(d,"SSS",int(ss[g]),int(ss[h]),int(ss[k]),t,u,v)
                    if face_best is None or cand<face_best: face_best=cand
                    if best is None or cand<best: best=cand
        audit.append({"kind":"SSS","out":[int(ss[g]),int(ss[h]),int(ss[k])],
                      "gc":len(gc),"hc":len(hc),"kc":len(kc),"best":None if face_best is None else face_best[0]})

    solution=None; oh=None
    if best is not None and best[0]<0:
        d,kind,*vals=best; pairs=list(map(int,sp)); selfs=list(map(int,ss)); replay=loads.copy()
        old=vals[:3]; new=vals[3:]
        types={"PPS":("P","P","S"),"PSS":("P","S","S"),"SSS":("S","S","S")}[kind]
        for typ,i in zip(types,old):
            (pairs if typ=="P" else selfs).remove(i); replay[(pr if typ=="P" else sr)[i]]-=1
        for typ,i in zip(types,new):
            (pairs if typ=="P" else selfs).append(i); replay[(pr if typ=="P" else sr)[i]]+=1
        pairs.sort(); selfs.sort(); re=int(((replay-1)**2).sum())
        if re!=energy+d: raise ValueError("mixed3 replay mismatch")
        solution=dict(state); solution.update(energy=re,pair_indices=pairs,self_indices=selfs,status="EXACT_MIXED_THREE_EXCHANGE")
        Path(args.output_state).write_text(json.dumps(solution,indent=2,sort_keys=True)+"\n"); oh=hist(replay)
    report={"status":"PASS" if solution else "NO_NEGATIVE_MIXED_THREE_EXCHANGE",
            "scope":"complete PPS/PSS/SSS depth-three oracle in finite face",
            "instance":args.instance,"source_state":args.state,"source_energy":energy,
            "source_histogram":hist(loads),"pair_options":len(pr),"self_options":len(sr),
            **counts,"outgoing_faces":face_no,"best_exchange":None if best is None else
            {"delta":best[0],"kind":best[1],"remove":list(best[2:5]),"add":list(best[5:8])},
            "output_state":args.output_state if solution else None,"output_histogram":oh,
            "face_audit":audit,"elapsed_seconds":time.time()-started}
    Path(args.report).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__ == "__main__": main()
