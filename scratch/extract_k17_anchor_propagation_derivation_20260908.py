#!/usr/bin/env python3
"""Export supplier rows for the already-proved eight-step contradiction; no search."""
import itertools,json,resource,signal
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3));signal.alarm(45)
BASE=Path('/home/amodo/exact-b-k17-anchor-propagation-20260908')
cert=json.loads((BASE/'anchor_support_propagation_certificate.json').read_text())
menu=json.loads(Path('/home/amodo/exact-b-k17-triple-anchor-menus-20260908/canonical_w3_anchor_factorized_menus.json').read_text())
trace=cert['propagation_trace']; zero=cert['contradiction']['target']
relevant={s['target'] for s in trace}|{zero}
providers={t:[] for t in relevant};rows={};initial={b:{t} for t,b in cert['initial_forced_rank7']}
for block in menu['blocks']:
    bid=block['block'];opts=[];seen=set()
    for letters in itertools.product(*block['letter_menus']):
        out=letters if len(letters)==1 else (*letters,letters[0]|letters[1])
        opts.append(out);seen.update(set(out)&relevant)
    if seen:
        rows[bid]=opts
        for t in seen:providers[t].append(bid)
needed_initial={next(iter(initial[b])):b for b in rows if b in initial}
verified_initial={t:[] for t in needed_initial}
for block in menu['blocks']:
    seen=set()
    for letters in itertools.product(*block['letter_menus']):
        out=letters if len(letters)==1 else (*letters,letters[0]|letters[1])
        seen.update(set(out)&needed_initial.keys())
    for t in seen:verified_initial[t].append(block['block'])
assert all(verified_initial[t]==[b] for t,b in needed_initial.items())
requirements={b:set(initial.get(b,())) for b in rows};steps=[]
def provider_record(t,b):
    valid=[out for out in rows[b] if requirements[b].issubset(out)]
    hosts=[out for out in valid if t in out]
    return dict(block=b,mandatory_before=sorted(requirements[b]),remaining_options=len(valid),target_options=len(hosts))
for step in trace:
    t=step['target'];b=step['block']
    records=[provider_record(t,p) for p in providers[t]]
    assert [r['block'] for r in records if r['target_options']]==[b]
    steps.append(dict(target=t,forced_block=b,all_original_providers=records))
    requirements[b].add(t)
zero_records=[provider_record(zero,b) for b in providers[zero]]
assert not any(r['target_options'] for r in zero_records)
cycles={c['cycle']:c for c in menu['cycles']}
source_blocks=[]
for bid in sorted(rows):
    b=menu['blocks'][bid];c=cycles[b['cycle']]
    source_blocks.append(dict(block=bid,cycle=b['cycle'],positions=b['positions'],
        original_letters=[c['source'][i] for i in b['positions']],pins=[c['pins'][i] for i in b['positions']],
        letter_menus=b['letter_menus'],initial_mandatory_rank7=sorted(initial.get(bid,())),
        final_mandatory_targets=sorted(requirements[bid])))
result=dict(scope='Supplier-row expansion of the already certified deterministic trace; no new search or decision.',
    initial_unique_rank7_dependencies=[[t,b] for t,b in sorted(needed_initial.items())],
    initial_dependency_uniqueness_independently_checked=True,steps=steps,
    final_zero_target=zero,final_zero_target_original_providers=zero_records,source_blocks=source_blocks)
(BASE/'anchor_compact_supplier_derivation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(initial_dependencies=len(needed_initial),relevant_blocks=len(rows),steps=steps,
    final_zero_target=zero,final_providers=zero_records),indent=2))
