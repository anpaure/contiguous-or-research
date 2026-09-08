#!/usr/bin/env python3
"""H100-only finite saturated-chain audit of a perturbed four-axis stair x chain."""
from collections import Counter,deque
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import socket
import sys
import time


def main():
    assert socket.gethostname().lower()=='arboghast', 'Run only via ssh h100'
    os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
    resource.setrlimit(resource.RLIMIT_AS,(3<<30,3<<30))
    recovery='--recover' in sys.argv[2:]
    resource.setrlimit(resource.RLIMIT_CPU,(4,4) if recovery else (36,36));signal.alarm(2 if recovery else 18)
    os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
    started=time.monotonic()
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import maximum_bipartite_matching
    outdir=Path(sys.argv[1]);outdir.mkdir(parents=True,exist_ok=True)
    report={'host':socket.gethostname(),'cases':[],'aggregates':[],'optional_s6_complete':False,
            'scope':'unit-coordinate Hasse matching; positive gaps do not imply non-Sperner width'}
    if recovery:
        report=json.loads((outdir/'report.json').read_text())
        report['aggregates']=[]
        report['optional_s6_reason']='optional stage stopped at cap; recovery recomputes only largest mandatory case'
    best=None
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        (outdir/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    def case(s,p,delta):
        nonlocal best
        case_started=time.monotonic();d=2*s;shape=(d,)*5
        coords=np.indices(shape,dtype=np.int16).reshape(5,-1).T
        thresholds=np.array([s]*4,dtype=np.int16);thresholds[p-1]+=delta
        bits=coords[:,:4]>=thresholds
        allowed=np.all(bits[:,:-1]>=bits[:,1:],axis=1)
        flats=np.flatnonzero(allowed).astype(np.int32);vertices=coords[allowed]
        count=len(flats);lookup=np.full(d**5,-1,dtype=np.int32);lookup[flats]=np.arange(count,dtype=np.int32)
        source=[];dest=[];rows=np.arange(count,dtype=np.int32)
        for axis in range(5):
            valid=vertices[:,axis]<d-1
            rr=rows[valid];target_flat=flats[valid]+d**(4-axis)
            cc=lookup[target_flat];inside=cc>=0
            source.append(rr[inside]);dest.append(cc[inside])
        src=np.concatenate(source);dst=np.concatenate(dest)
        graph=csr_matrix((np.ones(len(src),dtype=np.int8),(src,dst)),shape=(count,count))
        graph.sort_indices()
        matching=maximum_bipartite_matching(graph,perm_type='column')
        matched=np.flatnonzero(matching>=0);targets=matching[matched]
        assert len(np.unique(targets))==len(targets)
        difference=vertices[targets]-vertices[matched]
        assert np.all(difference>=0) and np.all(difference.sum(axis=1)==1)
        ranks=vertices.sum(axis=1)
        rank_counts=np.bincount(ranks,minlength=5*(d-1)+1)
        peak=int(rank_counts.max());chain_count=count-len(matched)
        assert chain_count>=peak
        entry={'s':s,'position':p,'delta':delta,'threshold_u':s+delta,
               'vertices':count,'hasse_edges':len(src),'matching_size':len(matched),
               'saturated_chain_count':chain_count,'largest_rank_layer':peak,
               'maximizing_ranks':np.flatnonzero(rank_counts==peak).tolist(),
               'gap':chain_count-peak,'rank_layer_counts':rank_counts.tolist(),
               'elapsed_seconds':time.monotonic()-case_started}
        report['cases'].append(entry)
        if best is None or count>best['entry']['vertices']:
            best={'entry':entry,'flats':flats.copy(),'matching':matching.copy(),
                  'indptr':graph.indptr.copy(),'indices':graph.indices.copy()}
        return entry
    if recovery:
        target=max(report['cases'],key=lambda c:c['vertices'])
        check=case(target['s'],target['position'],target['delta'])
        assert check['saturated_chain_count']==target['saturated_chain_count']
        report['cases'].pop()
    else:
        for s in (2,3,4,5):
            for delta in (-1,1):
                for p in range(1,5):case(s,p,delta)
            save()
    # Optional largest scale is taken only while ample verification time remains.
    if not recovery and time.monotonic()-started<7:
        for delta in (-1,1):
            for p in range(1,5):case(6,p,delta)
        report['optional_s6_complete']=True
    elif not recovery:report['optional_s6_reason']='reserved the remaining cap for independent largest-case validation'
    weights=(4,1,7,2)
    for s in sorted({c['s'] for c in report['cases']}):
        for delta in (-1,1):
            cc=sorted((c for c in report['cases'] if c['s']==s and c['delta']==delta),key=lambda c:c['position'])
            if len(cc)==4:
                report['aggregates'].append({'s':s,'delta':delta,'weights':list(weights),
                    'weighted_saturated_chain_count':sum(w*c['saturated_chain_count'] for w,c in zip(weights,cc)),
                    'weighted_largest_rank_layer':sum(w*c['largest_rank_layer'] for w,c in zip(weights,cc)),
                    'weighted_vertices':sum(w*c['vertices'] for w,c in zip(weights,cc)),
                    'baseline_28s4':28*s**4,
                    'weighted_gap_vs_baseline':sum(w*c['saturated_chain_count'] for w,c in zip(weights,cc))-28*s**4})
    save()
    # Recover paths from the largest matching. No rank-level claim substitutes
    # for these actual unit-edge paths.
    b=best;entry=b['entry'];matching=b['matching'];flats=b['flats'];count=len(flats)
    inverse=np.full(count,-1,dtype=np.int32)
    matched=np.flatnonzero(matching>=0);inverse[matching[matched]]=matched
    paths=[];visited=np.zeros(count,dtype=np.bool_)
    for root in np.flatnonzero(inverse<0):
        path=[];v=int(root)
        while v>=0:
            assert not visited[v];visited[v]=True;path.append(int(flats[v]));v=int(matching[v])
        paths.append(path)
    assert bool(visited.all()) and len(paths)==entry['saturated_chain_count']
    # Independently certify matching maximality by a Konig vertex cover.
    zl=np.zeros(count,dtype=np.bool_);zr=np.zeros(count,dtype=np.bool_)
    queue=deque(int(i) for i in np.flatnonzero(matching<0))
    for v in queue:zl[v]=True
    while queue:
        v=queue.popleft()
        for u in b['indices'][b['indptr'][v]:b['indptr'][v+1]]:
            u=int(u)
            if matching[v]==u or zr[u]:continue
            zr[u]=True
            partner=int(inverse[u])
            if partner>=0 and not zl[partner]:zl[partner]=True;queue.append(partner)
    cover_size=int((~zl).sum()+zr.sum())
    assert cover_size==len(matched)
    for v in range(count):
        assert (not zl[v]) or bool(zr[b['indices'][b['indptr'][v]:b['indptr'][v+1]]].all())
    # Independent literal replay uses only paths/thresholds, not the CSR graph
    # or matching. Re-enumerate the original five-tuples and their rank layers.
    d=2*entry['s'];thresholds=[entry['s']]*4;thresholds[entry['position']-1]+=entry['delta']
    def decode(flat):
        out=[0]*5
        for i in range(4,-1,-1):out[i]=flat%d;flat//=d
        assert flat==0
        return tuple(out)
    def is_allowed(point):
        bb=[point[i]>=thresholds[i] for i in range(4)]
        return all(bb[i]>=bb[i+1] for i in range(3))
    seen=set();replayed_ranks=Counter()
    for path in paths:
        previous=None
        for flat in path:
            assert flat not in seen;seen.add(flat)
            point=decode(flat);assert is_allowed(point)
            replayed_ranks[sum(point)]+=1
            if previous is not None:
                diffs=[a-c for a,c in zip(point,previous)]
                assert diffs.count(1)==1 and diffs.count(0)==4
            previous=point
    enumerated=set()
    for point in product(range(d),repeat=5):
        if is_allowed(point):
            flat=0
            for x in point:flat=flat*d+x
            enumerated.add(flat)
    assert seen==enumerated and len(seen)==count
    assert max(replayed_ranks.values())==entry['largest_rank_layer']
    artifact={'entry':entry,'thresholds':thresholds,'flat_encoding':'base 2s, first axis most significant',
              'paths':paths,'konig_cover_size':cover_size,
              'independent_path_and_tuple_replay':'PASS'}
    (outdir/'largest_paths.json').write_text(json.dumps(artifact,separators=(',',':'))+'\n')
    report['largest_case_replay']={**entry,'paths_recovered':len(paths),'vertices_replayed':count,
                                   'konig_cover_size':cover_size,'status':'PASS'}
    report['all_tested_cases_attain_largest_rank']=all(c['gap']==0 for c in report['cases'])
    save()
    summary={k:v for k,v in report.items() if k!='cases'}
    summary['cases']=[{k:v for k,v in c.items() if k not in ('rank_layer_counts','hasse_edges','matching_size','elapsed_seconds')} for c in report['cases']]
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
