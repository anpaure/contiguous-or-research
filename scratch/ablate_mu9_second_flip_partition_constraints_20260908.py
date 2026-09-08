#!/usr/bin/env python3
"""H100-only small ablation on the two guard-free second-flip cycles."""
from collections import defaultdict,Counter
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
    assert socket.gethostname().lower()=='arboghast'
    os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30));resource.setrlimit(resource.RLIMIT_CPU,(16,16))
    signal.alarm(8);os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
    started=time.monotonic()
    from ortools.sat.python import cp_model
    spec=importlib.util.spec_from_file_location('inv',Path(__file__).with_name('inventory_mu9_hamilton_hex_flips_20260908.py'))
    inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
    data=json.loads(Path(sys.argv[1]).read_text())
    report={'host':socket.gethostname(),'cases':[]}
    def fixed_targets(block,S,U):
        s,p=block['s'],block['p'];ss=[S[(s+j)%126] for j in range(p)]
        add=[(ss[j+1]&~ss[j]).bit_length()-1 for j in range(p-1)]
        rem=[(ss[j]&~ss[j+1]).bit_length()-1 for j in range(p-1)]
        common=511
        for a in ss:common&=a
        K=[i for i in range(9) if common&(1<<i)]
        right=K+list(reversed(rem))+[(U[(s-1)%126]&~ss[0]).bit_length()-1]
        left=add+[9]+sorted(set(range(9))-set(add+right))
        lp=[0];rp=[0]
        for i in left:lp.append(lp[-1]|(1<<i))
        for i in right:rp.append(rp[-1]|(1<<i))
        return {lp[i]|rp[j] for i in range(p,6) for j in range(6)
                if i+j in (4,5,6) and i in (p,5) and (j==0 or j>=len(K))}
    def solve(model):
        solver=cp_model.CpSolver();solver.parameters.num_search_workers=2
        solver.parameters.max_time_in_seconds=.5;solver.parameters.random_seed=60908
        status=solver.solve(model)
        return solver,status
    for candidate in data['candidates']:
        if candidate['remaining_guard'] is not None:continue
        V=candidate['V'];model=cp_model.CpModel();drop=[model.new_bool_var('d%d'%i) for i in range(126)]
        model.add(sum(drop)==42)
        for s in range(126):model.add(sum(drop[(s+j)%126] for j in range(5))>=1)
        for v in set(V):model.add(sum(1-drop[i] for i,x in enumerate(V) if x==v)==1)
        solver,status=solve(model)
        item={'candidate_id':candidate['id'],'model':'A_drop_spacing_only','status':solver.status_name(status),
              'wall_seconds':solver.wall_time}
        if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
            dd=[i for i,x in enumerate(drop) if solver.value(x)]
            assert len(dd)==42 and all(any((s+j)%126 in dd for j in range(5)) for s in range(126))
            assert len({V[i] for i in range(126) if i not in dd})==84
            item['dropped_indices']=dd
        report['cases'].append(item)
        if status==cp_model.INFEASIBLE:continue
        for reverse in (False,True):
            S,U=candidate['S'],candidate['U']
            if reverse:S=[S[-i%126] for i in range(126)];U=[U[(-i-1)%126] for i in range(126)]
            V=[U[i]|U[(i+1)%126] for i in range(126)]
            blocks=[b for s in range(126) for p in range(1,6) if (b:=inv.local_block(s,p,S,U,V)) is not None]
            for mode in ('B_local_rows','C_fixed_z','D_extreme_capacities'):
                model=cp_model.CpModel();x=[model.new_bool_var('x%d'%i) for i in range(len(blocks))]
                model.add(sum(x)==42);covers=[[] for _ in range(126)];targets=defaultdict(list);fixed=defaultdict(list);np=defaultdict(list)
                for b,var in zip(blocks,x):
                    np[b['p']].append(var)
                    for j in range(b['p']):covers[(b['s']+j)%126].append(var)
                    for i in b['retained_V']:targets[V[i]].append(var)
                    if mode=='C_fixed_z':
                        for v in fixed_targets(b,S,U):fixed[v].append(var)
                for xs in covers:model.add(sum(xs)==1)
                for v in set(V):model.add(sum(targets[v])==1)
                if mode=='C_fixed_z':
                    for xs in fixed.values():model.add(sum(xs)<=1)
                if mode=='D_extreme_capacities':
                    model.add(sum(np[1])>=1);model.add(sum(np[5])>=1)
                    model.add(2*sum(np[1])+sum(np[2])>=9);model.add(sum(np[4])+2*sum(np[5])>=9)
                solver,status=solve(model)
                item={'candidate_id':candidate['id'],'reverse':reverse,'model':mode,
                      'status':solver.status_name(status),'wall_seconds':solver.wall_time}
                if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
                    chosen=[b for b,var in zip(blocks,x) if solver.value(var)]
                    assert len(chosen)==42
                    assert Counter((b['s']+j)%126 for b in chosen for j in range(b['p']))==Counter(range(126))
                    assert set(Counter(V[i] for b in chosen for i in b['retained_V']).values())=={1}
                    item['blocks']=[[b['s'],b['p']] for b in chosen]
                report['cases'].append(item)
                if mode=='B_local_rows' and status==cp_model.INFEASIBLE:break
    report['elapsed_seconds']=time.monotonic()-started
    Path(sys.argv[2]).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({**report,'cases':[{k:v for k,v in c.items() if k not in ('blocks','dropped_indices')} for c in report['cases']]},indent=2))


if __name__=='__main__':main()
