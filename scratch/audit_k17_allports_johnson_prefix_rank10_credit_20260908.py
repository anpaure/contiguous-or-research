#!/usr/bin/env python3
"""Fixed five NEW-prefix seam check; mathematical execution only on h100."""
import json
from pathlib import Path
old=Path('/home/amodo/exact-b-k17-pbbs-inventory-20260908')
new=Path('/home/amodo/exact-b-k17-badsix-all-ports-20260908')
p=json.loads((old/'inventory.json').read_text())
P=list(map(int,(new/'badsix_all_ports_306_owner_path.word').read_text().split()))
assert len(P)==306 and P[-1]==103765
exclusive={int(t):c['cycle'] for c in p['cycles'] for t in c['exclusive_target_cut_cores']}
unsafe=set(p['summary']['cycles_with_no_one_cut_global_safe_position'])
mountain=json.loads(Path('/home/amodo/exact-b-k17-rigid-c6-20260908/rigid_c6.json').read_text())
updated={t:('old',c) for t,c in exclusive.items() if c not in [0,1]}
for c in mountain['new_cycle_cut_reports']:
    for t in c['exclusive_target_cut_cores']:
        assert int(t) not in updated
        updated[int(t)]=('mountain',c['cycle'])
rows=[]
for i in [50,101,152,203,254]:
    t=P[i]|P[i+1]
    supplier=exclusive.get(t); newsupplier=updated.get(t)
    assert t.bit_count()==10
    rows.append({'edge_index':i,'upper_union':t,'lower_intersection':P[i]&P[i+1],
                 'original_exclusive_supplier':supplier,'original_forced_59_credit':supplier in unsafe,
                 'updated_exclusive_supplier':newsupplier,
                 'updated_forced_59_credit':newsupplier is not None and (newsupplier[0]=='mountain' or newsupplier[1] in unsafe)})
out={'prefix':'new all-ports Johnson306','rows':rows,
     'original_distinct_forced_59_credits':len({r['upper_union'] for r in rows if r['original_forced_59_credit']}),
     'updated_distinct_forced_59_credits':len({r['upper_union'] for r in rows if r['updated_forced_59_credit']}),
     'unchanged_last_owner':P[-1],
     'pivot_and_PQ_credit':'zero by the earlier complete eight-superset check, not rerun'}
(new/'rank10_seam_recapture_credit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
