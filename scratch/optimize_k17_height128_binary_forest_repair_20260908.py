#!/usr/bin/env python3
"""One <=30-second fixed-forest MILP, then exact literal verification; h100 only."""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import hashlib
import json
import resource
import signal
import warnings
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(110)
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

base=Path('/home/amodo/exact-b-k17-height-adaptive-20260908')
out=base/'binary_forest_repair'
catalogue=json.loads((out/'binary_forest_candidate_catalogue.json').read_text())
holes=catalogue['holes'];candidates=catalogue['candidates'];index={t:i for i,t in enumerate(holes)}
assert len(holes)==128 and len(candidates)==56
rows=[];columns=[]
for j,(p,a,b) in enumerate(candidates):
    rows.extend([index[p],128+index[a],128+index[b]])
    columns.extend([j,j,j])
matrix=coo_matrix((np.ones(len(rows)),(rows,columns)),shape=(256,len(candidates))).tocsc()
options=dict(time_limit=30,mip_rel_gap=0.0,presolve=True,threads=1,random_seed=0)
with warnings.catch_warnings():
    warnings.simplefilter('ignore',RuntimeWarning)
    result=milp(c=-np.ones(len(candidates)),integrality=np.ones(len(candidates)),
        bounds=Bounds(np.zeros(len(candidates)),np.ones(len(candidates))),
        constraints=LinearConstraint(matrix,np.zeros(256),np.ones(256)),options=options)
assert result.x is not None, ('No feasible forest returned within fixed MILP cap',str(result.message))
selected=[candidates[j] for j,x in enumerate(result.x) if x>0.5]
selected.sort()
parents={};used_children=set()
for p,a,b in selected:
    assert p not in parents and a!=b and a not in used_children and b not in used_children
    assert a|b==p and a.bit_count()<p.bit_count() and b.bit_count()<p.bit_count()
    parents[p]=(a,b);used_children.update((a,b))
roots=sorted(set(holes)-used_children)
leaves=[];hole_witnesses={};visited=set()
def visit(target):
    assert target not in visited
    visited.add(target);start=len(leaves)
    if target in parents:
        a,b=parents[target];visit(a);visit(b)
    else:leaves.append(target)
    finish=len(leaves)-1;value=0
    for letter in leaves[start:finish+1]:value|=letter
    assert value==target
    hole_witnesses[target]=(start,finish)
for target in roots:visit(target)
assert visited==set(holes)
assert len(leaves)==128-len(selected)
prefix=list(map(int,(base/'k17_height_trimmed24829.word').read_text().split()))
assert len(prefix)==24829
word=prefix+leaves;full=(1<<17)-1
assert all(1<=a<=full for a in word)
suffix={};witnesses={}
for end,letter in enumerate(word):
    current={letter:end}
    for target,start in suffix.items():current.setdefault(target|letter,start)
    assert len(current)<=17
    for target,start in current.items():witnesses.setdefault(target,(start,end))
    suffix=current
missing=[t for t in range(1,full+1) if t not in witnesses]
assert not missing

# Independent literal range-OR verification of every complete-word witness.
size=1
while size<len(word):size*=2
tree=[0]*(2*size);tree[size:size+len(word)]=word
for i in range(size-1,0,-1):tree[i]=tree[2*i]|tree[2*i+1]
def range_or(left,right):
    assert 0<=left<=right<len(word)
    left+=size;right+=size+1;value=0
    while left<right:
        if left&1:value|=tree[left];left+=1
        if right&1:right-=1;value|=tree[right]
        left//=2;right//=2
    return value
for target,(start,end) in witnesses.items():assert range_or(start,end)==target
for target,(start,end) in hole_witnesses.items():assert range_or(24829+start,24829+end)==target

label='k17_height_forest'+str(len(word))
raw=('\n'.join(map(str,word))+'\n').encode()
(out/(label+'.word')).write_bytes(raw)
(out/'binary_forest_repair_suffix.word').write_text('\n'.join(map(str,leaves))+'\n')
(out/(label+'_target_witnesses.json')).write_text(json.dumps({str(t):witnesses[t] for t in sorted(witnesses)})+'\n')
eligible=sorted({p for p,a,b in candidates})
report=dict(status='PASS',prefix_length=24829,prefix_unchanged=True,original_hole_count=128,
    candidate_pairs=len(candidates),eligible_internal_targets=eligible,
    exact_internal_node_upper_bound=len(eligible),selected_internal_nodes=len(selected),
    exact_model_optimality_certified=(len(selected)==len(eligible)),
    optimality_scope='Only rank-decreasing binary forests on the fixed128hole-targets, each child used at most once; exact upper bound is the exhaustive count of eligible internal targets.',
    selected_parent_child_triples=selected,roots=roots,leaf_word=leaves,
    repair_length=len(leaves),letters_saved=len(selected),word_file=label+'.word',length=len(word),
    input_sha256=hashlib.sha256(raw).hexdigest(),all_letters_nonzero=True,
    distinct_nonempty_targets=len(witnesses),missing_count=0,
    segment_tree_witnesses_rechecked=len(witnesses),
    target_rank_counts=dict(sorted(Counter(t.bit_count() for t in witnesses).items())),
    all_hole_tree_witnesses={str(t):dict(suffix_start=s,suffix_end=e,word_start=24829+s,word_end=24829+e) for t,(s,e) in sorted(hole_witnesses.items())},
    solver=dict(name='scipy.optimize.milp / HiGHS',status=int(result.status),message=str(result.message),
        success=bool(result.success),objective=(None if result.fun is None else float(result.fun)),
        options=options,mip_gap=float(getattr(result,'mip_gap',-1)),mip_node_count=int(getattr(result,'mip_node_count',-1))),
    resource_caps=dict(cpu_seconds=90,wall_seconds=110,address_space_bytes=1024**3),
    no_cut_order_or_deletion_search=True)
(out/'binary_forest_repair_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('all_hole_tree_witnesses','leaf_word','roots')},indent=2))
print('PASS: fixed binary forest, all hole-subtree witnesses, full universal word, and independent range-OR replay.')
