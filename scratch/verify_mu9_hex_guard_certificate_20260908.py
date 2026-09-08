#!/usr/bin/env python3
"""Independent h100-only replay of nine physical flips and hole guards."""
from collections import Counter
import json
from pathlib import Path
import resource
import socket
import sys
import time


def main():
    assert socket.gethostname().lower()=="arboghast", "Run only via ssh h100"
    resource.setrlimit(resource.RLIMIT_CPU,(5,5))
    resource.setrlimit(resource.RLIMIT_AS,(256<<20,256<<20))
    started=time.monotonic()
    certificate=json.loads(Path(sys.argv[1]).read_text())
    seed=(3,18,130,258,264,72,96,36,33,48,24,272,144,192)
    A=[]
    for t in range(9):
        for mask in seed:
            A.append(sum(1<<((i+5*t)%9) for i in range(9) if mask&(1<<i)))
    S=[A[i]|A[(i+1)%126]|A[(i+2)%126] for i in range(126)]
    U=[S[i]|A[(i+3)%126] for i in range(126)]
    baseline={v:set() for v in S+U}
    for i in range(126):
        for lo in (S[i],S[(i+1)%126]):
            baseline[lo].add(U[i]);baseline[U[i]].add(lo)
    results=[]
    for entry in certificate['classes']:
        adj={v:set(ns) for v,ns in baseline.items()}
        K=sum(1<<i for i in entry['core'])
        a,b,c=[1<<i for i in entry['abc']]
        L=[K|a,K|b,K|c];H=[K|a|b,K|b|c,K|c|a]
        m0={tuple(sorted((L[0],H[0]))),tuple(sorted((L[1],H[1]))),tuple(sorted((L[2],H[2])))}
        m1={tuple(sorted((L[1],H[0]))),tuple(sorted((L[2],H[1]))),tuple(sorted((L[0],H[2])))}
        removed={tuple(x) for x in entry['removed_edges']};added={tuple(x) for x in entry['added_edges']}
        assert (removed==m0 and added==m1) or (removed==m1 and added==m0)
        for lo,hi in removed:
            assert hi in adj[lo] and lo in adj[hi]
            adj[lo].remove(hi);adj[hi].remove(lo)
        for lo,hi in added:
            assert hi not in adj[lo] and lo not in adj[hi]
            adj[lo].add(hi);adj[hi].add(lo)
        assert all(len(ns)==2 for ns in adj.values())
        start=min(S);path=[start];previous=None;current=start
        while True:
            nxt=min(v for v in adj[current] if v!=previous)
            if nxt==start:break
            assert nxt not in path
            path.append(nxt);previous,current=current,nxt
        assert len(path)==252 and set(path)==set(adj)
        actual_S=path[::2];actual_U=path[1::2]
        assert all(actual_S[i]|actual_S[(i+1)%126]==actual_U[i] for i in range(126))
        V=[actual_U[i]|actual_U[(i+1)%126] for i in range(126)]
        assert V==entry['V'] and all(v.bit_count()==6 for v in V)
        counts=Counter(V)
        absent={v for v in range(512) if v.bit_count()==6 and v not in counts}
        assert absent==set(entry['intrinsically_missing'])==set(entry['rank6_missing'])
        possible=set(absent) if absent else {v for v in range(512) if v.bit_count()==6}
        for guard in entry['guards']:
            q=guard['q'];support={q}
            assert {w['occurrence'] for w in guard['witnesses']}=={i for i,v in enumerate(V) if v==q}
            for witness in guard['witnesses']:
                indices={(witness['window_start']+j)%126 for j in range(5)}
                assert set(witness['unique_guard_indices'])|{witness['occurrence']}==indices
                values=[V[i] for i in witness['unique_guard_indices']]
                assert values==witness['unique_guard_values'] and len(values)==4
                assert all(counts[v]==1 for v in values)
                support.update(values)
            assert support==set(guard['support'])
            possible &= support
        assert not possible
        results.append({'representative_id':entry['representative_id'],'status':'PHYSICAL_CYCLE_AND_GUARDS_PASS'})
    assert len(results)==9
    print(json.dumps({'host':socket.gethostname(),'elapsed_seconds':time.monotonic()-started,
                      'results':results},indent=2))


if __name__=='__main__':main()
