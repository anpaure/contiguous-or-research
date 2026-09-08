#!/usr/bin/env python3
"""Fixed five-seam diagnostic. Mathematical execution only on ssh h100."""
import json
from pathlib import Path

base = Path('/home/amodo/exact-b-k17-pbbs-inventory-20260908')
inventory = json.loads((base / 'inventory.json').read_text())
owners = list(map(int, (base / 'badsix_relaxed_306_owner_path.word').read_text().split()))
assert len(owners) == 306
old_exclusive = {}
for rec in inventory['cycles']:
    for target in rec['exclusive_target_cut_cores']:
        target = int(target)
        assert target not in old_exclusive
        old_exclusive[target] = rec['cycle']

rows = []
for i in [50,101,152,203,254]:
    target = owners[i] | owners[i+1]
    lower = owners[i] & owners[i+1]
    rows.append(dict(left_index=i, left=owners[i], right=owners[i+1],
                     union=target, union_rank=target.bit_count(),
                     intersection=lower, intersection_rank=lower.bit_count(),
                     original_exclusive_supplier=old_exclusive.get(target)))
assert sum(row['union_rank'] == 10 for row in rows) == 2

mountain = json.loads(Path('/home/amodo/exact-b-k17-rigid-c6-20260908/rigid_c6.json').read_text())
updated_exclusive = {t: f'old_{cid}' for t,cid in old_exclusive.items() if cid not in [0,1]}
for rec in mountain['new_cycle_cut_reports']:
    for target in rec['exclusive_target_cut_cores']:
        target = int(target)
        assert target not in updated_exclusive
        updated_exclusive[target] = f'mountain_{rec["cycle"]}'
for row in rows:
    row['updated_exclusive_supplier'] = updated_exclusive.get(row['union'])
    row['supplier_is_original_unsafe_cycle'] = row['original_exclusive_supplier'] in inventory['summary']['cycles_with_no_one_cut_global_safe_position']

report = dict(seams=rows,
    original_rank10_exclusive_credits=sum(row['union_rank']==10 and row['original_exclusive_supplier'] is not None for row in rows),
    updated_rank10_exclusive_credits=sum(row['union_rank']==10 and row['updated_exclusive_supplier'] is not None for row in rows),
    original_unsafe_rank10_credits=sum(row['union_rank']==10 and row['supplier_is_original_unsafe_cycle'] for row in rows))
report['upper_pivot_superowners'] = []
for bit in range(17):
    if owners[-1] >> bit & 1:
        continue
    target = owners[-1] | (1 << bit)
    supplier = old_exclusive.get(target)
    report['upper_pivot_superowners'].append(dict(target=target, added_bit=bit,
        original_exclusive_supplier=supplier,
        supplier_is_original_unsafe_cycle=supplier in inventory['summary']['cycles_with_no_one_cut_global_safe_position'],
        updated_exclusive_supplier=updated_exclusive.get(target)))
assert len(report['upper_pivot_superowners']) == 8
Path('prefix_rank10_recapture_credit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
print('PASS: exact fixed-prefix seam rank-ten recapture credit enumerated')
