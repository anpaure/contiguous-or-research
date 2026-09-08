#!/usr/bin/env python3
"""H100-only exact Boolean certificates for the two guard-free cycles."""
import importlib.util
import json
from itertools import combinations
from pathlib import Path
import resource
import socket
import sys
import time


def prove(clauses):
    known={};trace=[];reason={}
    while True:
        changed=False
        for ci,clause in enumerate(clauses):
            if any(abs(l) in known and known[abs(l)]==(l>0) for l in clause):continue
            free=[l for l in clause if abs(l) not in known]
            if not free:
                needed=set()
                def visit_clause(c,unit=None):
                    if c in needed:return
                    needed.add(c)
                    for l in clauses[c]:
                        if l!=unit:
                            prevci,prevlit=reason[abs(l)]
                            visit_clause(prevci,prevlit)
                visit_clause(ci)
                return {'trace':trace,'contradiction_clause':ci,'dependency_core':sorted(needed)}
            if len(free)==1:
                l=free[0];known[abs(l)]=(l>0);reason[abs(l)]=(ci,l)
                trace.append([ci,l]);changed=True
        if not changed:return None


def replay(clauses,proof):
    known={}
    for ci,l in proof['trace']:
        assert abs(l) not in known and l in clauses[ci]
        assert all(abs(x) in known and known[abs(x)]!=(x>0) for x in clauses[ci] if x!=l)
        known[abs(l)]=(l>0)
    assert all(abs(x) in known and known[abs(x)]!=(x>0) for x in clauses[proof['contradiction_clause']])


def main():
    assert socket.gethostname().lower()=='arboghast'
    resource.setrlimit(resource.RLIMIT_CPU,(5,5));resource.setrlimit(resource.RLIMIT_AS,(256<<20,256<<20))
    started=time.monotonic()
    spec=importlib.util.spec_from_file_location('inv',Path(__file__).with_name('inventory_mu9_hamilton_hex_flips_20260908.py'))
    inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
    source=json.loads(Path(sys.argv[1]).read_text());ablation=json.loads(Path(sys.argv[2]).read_text())
    report={'cases':[],'scope':'exact Boolean clauses, no SAT/CP-SAT import'}
    for candidate in source['candidates']:
        if candidate['id'] not in (0,2):continue
        for reverse in ((False,True) if candidate['id']==0 else (False,)):
            S,U=candidate['S'],candidate['U']
            if reverse:S=[S[-i%126] for i in range(126)];U=[U[(-i-1)%126] for i in range(126)]
            V=[U[i]|U[(i+1)%126] for i in range(126)]
            clauses=[];meta=[]
            def add(clause,why):clauses.append(clause);meta.append(why)
            for s in range(126):add([1+(s+j)%126 for j in range(5)],{'type':'five_window_drop','start':s})
            for value in sorted(set(V)):
                positions=[i for i,v in enumerate(V) if v==value]
                add([-(i+1) for i in positions],{'type':'target_at_least_one_retained','target':value,'positions':positions})
                for i,j in combinations(positions,2):
                    add([i+1,j+1],{'type':'target_at_most_one_retained','target':value,'positions':[i,j]})
            if candidate['id']==0:
                for d in range(126):
                    for p in range(1,6):
                        s=(d+2)%126;e=(d+p)%126
                        if inv.local_block(s,p,S,U,V) is None:
                            add([-(d+1),-(e+1)]+[1+(d+j)%126 for j in range(1,p)],
                                {'type':'invalid_consecutive_drop_pair','d':d,'e':e,'block_start':s,'p':p})
            proof=prove(clauses)
            if proof:replay(clauses,proof)
            report['cases'].append({'candidate_id':candidate['id'],'reverse':reverse,
                                    'clauses':clauses,'clause_meanings':meta,'proof':proof,
                                    'core_meanings':[meta[i] for i in proof['dependency_core']] if proof else None})
    raw=next(c for c in ablation['cases'] if c['candidate_id']==0 and c['model']=='A_drop_spacing_only')
    dd=raw['dropped_indices'];candidate=next(c for c in source['candidates'] if c['id']==0)
    witness=[]
    for d,e in zip(dd,dd[1:]+[dd[0]+126]):
        p=e-d;s=(d+2)%126
        witness.append({'s':s,'p':p,'locally_valid':inv.local_block(s,p,candidate['S'],candidate['U'],candidate['V']) is not None})
    report['candidate0_raw_fullV_partition']=witness
    report['candidate0_raw_invalid_blocks']=[b for b in witness if not b['locally_valid']]
    report['elapsed_seconds']=time.monotonic()-started
    Path(sys.argv[3]).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'elapsed_seconds':report['elapsed_seconds'],
                      'raw_invalid_blocks':report['candidate0_raw_invalid_blocks'],
                      'cases':[{'candidate_id':c['candidate_id'],'reverse':c['reverse'],
                                'unit_proof_pass':c['proof'] is not None,
                                'core_meanings':c['core_meanings']} for c in report['cases']]},indent=2))


if __name__=='__main__':main()
