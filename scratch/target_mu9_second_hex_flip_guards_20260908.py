#!/usr/bin/env python3
"""H100-only targeted second flip, full V deck, capped block CSP only."""
from collections import Counter, defaultdict
from itertools import combinations
from math import factorial
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
    os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30))
    resource.setrlimit(resource.RLIMIT_CPU,(36,36))
    signal.alarm(18)
    os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
    started=time.monotonic()
    spec=importlib.util.spec_from_file_location('inv',Path(__file__).with_name('inventory_mu9_hamilton_hex_flips_20260908.py'))
    inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
    inventory=json.loads(Path(sys.argv[1]).read_text())
    guards=json.loads(Path(sys.argv[2]).read_text())
    byid={r['id']:r for r in inventory['retained_cycles']}
    gc={r['representative_id']:r for r in guards['classes']}
    full6={x for x in range(512) if x.bit_count()==6}
    report={'host':socket.gethostname(),'starting_representatives':[0,1,4],
            'per_start':[],'candidates':[],'partition_cases':[],
            'scope':'targeted second flips destroying both displayed guards; no free row-order solver',
            'enumeration_complete':False,'first_feasible_partition':None}
    output=Path(sys.argv[3])
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        output.write_text(json.dumps(report,indent=2)+'\n')
    save()
    def adjacency(S,U):
        adj={v:set() for v in S+U}
        for i in range(126):
            for s in (S[i],S[(i+1)%126]):
                adj[s].add(U[i]);adj[U[i]].add(s)
        return adj
    def old_guard_survives(g,row,adj,values,counts):
        q=g['q']
        catalogue={row['S'][(w['occurrence']+1)%126]:w for w in g['witnesses']}
        current=[s for s,v in values.items() if v==q]
        if not current:return True  # q itself is already a hole.
        for s in current:
            if s not in catalogue:return False
            w=catalogue[s];start=w['window_start']
            vertices=[row['S'][(start+j+1)%126] for j in range(5)]
            for j in range(4):
                u=row['U'][(start+j+1)%126]
                if u not in adj[vertices[j]] or u not in adj[vertices[j+1]]:return False
            others=[v for v in vertices if v!=s]
            if len(others)!=4 or any(counts[values[v]]!=1 for v in others):return False
        return True
    def any_guard(V):
        counts=Counter(V)
        for q in sorted(counts):
            witnesses=[]
            for x,v in enumerate(V):
                if v!=q:continue
                for back in range(5):
                    start=(x-back)%126
                    others=[(start+j)%126 for j in range(5) if (start+j)%126!=x]
                    if all(counts[V[i]]==1 for i in others):
                        witnesses.append({'occurrence':x,'window_start':start,
                                          'unique_guard_indices':others,
                                          'unique_guard_values':[V[i] for i in others]})
                        break
                else:break
            else:return {'q':q,'witnesses':witnesses}
        return None
    def row_block(s,p,S,U,V):
        b=inv.local_block(s,p,S,U,V)
        if b is None:return None
        ss=[S[(s+j)%126] for j in range(p)]
        adds=[ss[j+1]&~ss[j] for j in range(p-1)]
        removes=[ss[j]&~ss[j+1] for j in range(p-1)]
        common=511
        for v in ss:common&=v
        k=[i for i in range(9) if common&(1<<i)]
        bit=lambda mask:mask.bit_length()-1
        right=k+[bit(v) for v in reversed(removes)]+[bit(U[(s-1)%126]&~ss[0])]
        aa=[bit(v) for v in adds]
        cc=sorted(set(range(9))-set(aa+right))
        left=aa+[9]+cc
        assert len(left)==len(right)==5 and set(left+right)==set(range(10))
        lp=[0];rp=[0]
        for v in left:lp.append(lp[-1]|(1<<v))
        for v in right:rp.append(rp[-1]|(1<<v))
        deck=[a|c for a in lp for c in rp]
        assert len(set(deck))==36
        assert {v for v in deck if v.bit_count()==6 and not v&512}=={V[i] for i in b['retained_V']}
        fixed=[]
        for i in range(p,6):
            for j in range(6):
                if i+j in (4,5,6) and i in (p,5) and (j==0 or j>=len(k)):
                    fixed.append(lp[i]|rp[j])
        assert len(fixed)==len(set(fixed))
        assert (512|S[(s+p-1)%126]) in fixed
        assert (512|(511^U[(s-1)%126])) in fixed
        b.update({'left':left,'right':right,'free_choices':factorial(5-p)**2,
                  'fixed_z_critical':fixed})
        return b
    hexagons=[]
    for core in combinations(range(9),3):
        K=sum(1<<i for i in core)
        for abc in combinations([i for i in range(9) if i not in core],3):
            a,b,c=[1<<i for i in abc]
            ll=[K|a,K|b,K|c];uu=[K|a|b,K|b|c,K|c|a]
            m0={inv.edge(ll[0],uu[0]),inv.edge(ll[1],uu[1]),inv.edge(ll[2],uu[2])}
            m1={inv.edge(ll[1],uu[0]),inv.edge(ll[2],uu[1]),inv.edge(ll[0],uu[2])}
            hexagons.append((core,abc,ll,uu,m0,m1))
    seen=set();survivors=[]
    for rid in (0,1,4):
        row=byid[rid];adj=adjacency(row['S'],row['U'])
        assert inv.extract(adj)==(row['S'],row['U'])
        baseedges={inv.edge(v,w) for v,ns in adj.items() for w in ns}
        basevalues={s:list(adj[s])[0]|list(adj[s])[1] for s in row['S']}
        assert set(basevalues.values())==full6
        oldguards=gc[rid]['guards'];assert len(oldguards)==2
        assert all(old_guard_survives(g,row,adj,basevalues,Counter(basevalues.values())) for g in oldguards)
        stats=Counter({'representative_id':rid,'hexagons':0})
        for core,abc,ll,uu,m0,m1 in hexagons:
            stats['hexagons']+=1
            if m0<=baseedges and not(m1&baseedges):remove,add=m0,m1
            elif m1<=baseedges and not(m0&baseedges):remove,add=m1,m0
            else:continue
            stats['legal_matching_flips']+=1
            if remove=={tuple(e) for e in row['added_edges']} and add=={tuple(e) for e in row['removed_edges']}:
                stats['undo_to_untouched_source_excluded']+=1;continue
            newadj={v:set(ns) for v,ns in adj.items()}
            for v,w in remove:newadj[v].remove(w);newadj[w].remove(v)
            for v,w in add:newadj[v].add(w);newadj[w].add(v)
            assert all(len(ns)==2 for ns in newadj.values())
            values=dict(basevalues)
            for s in ll:values[s]=list(newadj[s])[0]|list(newadj[s])[1]
            counts=Counter(values.values())
            if set(counts)!=full6:stats['lost_rank6_coverage']+=1;continue
            stats['all84_before_connectivity']+=1
            persists=[old_guard_survives(g,row,newadj,values,counts) for g in oldguards]
            if any(persists):
                stats['preserves_at_least_one_displayed_guard']+=1;continue
            stats['destroys_both_displayed_guards']+=1
            cycle=inv.extract(newadj)
            if cycle is None:stats['destroyed_both_but_not_Hamilton']+=1;continue
            ss,us=cycle;vv=[us[i]|us[(i+1)%126] for i in range(126)]
            edges=[inv.edge(v,w) for v,ns in newadj.items() for w in ns if v<w]
            key=min(tuple(sorted(inv.edge(inv.rot(a,t),inv.rot(b,t)) for a,b in edges)) for t in range(9))
            if key in seen:stats['duplicate_up_to_coordinate_rotation']+=1;continue
            seen.add(key)
            candidate={'id':len(report['candidates']),'first_representative_id':rid,
                       'first_core':row['core'],'first_abc':row['abc'],
                       'second_core':list(core),'second_abc':list(abc),
                       'second_removed_edges':sorted(remove),'second_added_edges':sorted(add),
                       'S':ss,'U':us,'V':vv}
            g=any_guard(vv)
            if g is not None:
                candidate['remaining_guard']=g;stats['another_guard_obstructs_full_V_partition']+=1
            else:
                candidate['remaining_guard']=None;stats['partition_candidates']+=1;survivors.append(candidate)
            report['candidates'].append(candidate)
        report['per_start'].append(dict(stats));save()
    report['enumeration_complete']=True;save()
    if survivors:
        from ortools.sat.python import cp_model
        for candidate in survivors:
            for reverse in (False,True):
                if time.monotonic()-started>15.5:
                    report['partition_cap_reached']=True;save();return
                S=candidate['S'];U=candidate['U']
                if reverse:
                    S=[S[-i%126] for i in range(126)];U=[U[(-i-1)%126] for i in range(126)]
                V=[U[i]|U[(i+1)%126] for i in range(126)]
                blocks=[b for s in range(126) for p in range(1,6) if (b:=row_block(s,p,S,U,V)) is not None]
                model=cp_model.CpModel();x=[model.new_bool_var('x%d'%i) for i in range(len(blocks))]
                model.add(sum(x)==42)
                covers=[[] for _ in range(126)];rank6=defaultdict(list);fixed=defaultdict(list)
                np={p:[] for p in range(1,6)}
                for b,var in zip(blocks,x):
                    np[b['p']].append(var)
                    for j in range(b['p']):covers[(b['s']+j)%126].append(var)
                    for i in b['retained_V']:rank6[V[i]].append(var)
                    for v in b['fixed_z_critical']:fixed[v].append(var)
                for vv in covers:model.add(sum(vv)==1)
                for v in full6:model.add(sum(rank6[v])==1)
                for vv in fixed.values():model.add(sum(vv)<=1)
                model.add(sum(np[1])>=1);model.add(sum(np[5])>=1)
                model.add(2*sum(np[1])+sum(np[2])>=9);model.add(sum(np[4])+2*sum(np[5])>=9)
                solver=cp_model.CpSolver();solver.parameters.num_search_workers=2
                solver.parameters.max_time_in_seconds=min(0.8,max(0.05,16-time.monotonic()+started))
                solver.parameters.random_seed=60908
                status=solver.solve(model)
                result={'candidate_id':candidate['id'],'reverse':reverse,
                        'status':solver.status_name(status),'solver_wall_seconds':solver.wall_time,
                        'valid_block_counts':dict(Counter(b['p'] for b in blocks))}
                if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
                    chosen=[b for b,var in zip(blocks,x) if solver.value(var)]
                    cover=Counter((b['s']+j)%126 for b in chosen for j in range(b['p']))
                    target6=Counter(V[i] for b in chosen for i in b['retained_V'])
                    fixedcounts=Counter(v for b in chosen for v in b['fixed_z_critical'])
                    assert len(chosen)==42 and set(cover)==set(range(126)) and set(cover.values())=={1}
                    assert set(target6)==full6 and set(target6.values())=={1}
                    assert max(fixedcounts.values())==1
                    result.update({'blocks':chosen,'S':S,'U':U,'V':V,
                                   'scope':'all84 no-z rank6 and fixed z-critical collisions pass; free row orders unsolved'})
                    report['first_feasible_partition']=result
                report['partition_cases'].append(result);save()
                if report['first_feasible_partition'] is not None:
                    print(json.dumps({'FOUND':True,'candidate_id':candidate['id'],'reverse':reverse,
                                      'elapsed_seconds':report['elapsed_seconds'],'per_start':report['per_start']},indent=2));return
    save()
    print(json.dumps({k:v for k,v in report.items() if k not in ('candidates','first_feasible_partition')},indent=2))


if __name__=='__main__':main()
