#!/usr/bin/env python3
"""Fixed hole-pair catalogue only. Execute mathematical code on h100."""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import importlib.util
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(110)
base=Path('/home/amodo/exact-b-k17-height-adaptive-20260908')
out=base/'binary_forest_repair';out.mkdir(exist_ok=True)
old=json.loads((base/'height_adaptive_fixed_certificate.json').read_text())
holes=sorted(old['trimmed']['missing_targets']);pool=set(holes)
assert len(holes)==128
candidates=[]
for a,b in combinations(holes,2):
    parent=a|b
    if parent in pool and parent!=a and parent!=b:
        assert a.bit_count()<parent.bit_count() and b.bit_count()<parent.bit_count()
        candidates.append([parent,a,b])
candidates.sort(key=lambda t:(t[0].bit_count(),t[0],t[1],t[2]))
summary=dict(holes=len(holes),candidate_pairs=len(candidates),
    eligible_parents=len({p for p,a,b in candidates}),
    eligible_parent_rank_counts=dict(sorted(Counter(p.bit_count() for p in {p for p,a,b in candidates}).items())),
    candidate_rank_types=dict(sorted(Counter(','.join(map(str,(p.bit_count(),a.bit_count(),b.bit_count()))) for p,a,b in candidates).items())),
    scipy_installed=importlib.util.find_spec('scipy') is not None,
    methodology='Exhaust all unordered distinct pairs of the128fixed holes; require their union to be a strictly larger hole.')
(out/'binary_forest_candidate_catalogue.json').write_text(json.dumps(dict(summary=summary,holes=holes,candidates=candidates),indent=2)+'\n')
print(json.dumps(summary,indent=2))
