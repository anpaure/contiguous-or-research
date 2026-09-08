"""h100-only necessary coordinate-balance inventory; no solver or row search."""
import itertools
import json
import os
import pathlib
import resource
import socket
import sys
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
started = time.monotonic()
rows = [
    ('0461', '5723'), ('0473', '2651'), ('0674', '3152'),
    ('0726', '1435'), ('1507', '4263'), ('1605', '7432'),
    ('2104', '6375'), ('2150', '7463'), ('3206', '7154'),
    ('3210', '4567'), ('3617', '5204'), ('4302', '6157'),
    ('5034', '6721'), ('5426', '7301'),
]

def prefixes(order):
    result = [0]
    for bit in map(int, order):
        result.append(result[-1] | (1 << bit))
    return result

def incidence(masks):
    return tuple(sum((mask >> bit) & 1 for mask in masks) for bit in range(8))

right_shores = []
middle_paths = []
for left, right in rows:
    assert sorted(left + right) == list('01234567')
    cp, dp = prefixes(left), prefixes(right)
    right_shores.append(dp[-1])
    path = [cp[i] | dp[4 - i] for i in range(5)]
    assert all(mask.bit_count() == 4 for mask in path)
    middle_paths.append(path)

by_signature = {}
quartets = list(itertools.combinations(range(14), 4))
assert len(quartets) == 1001
for quartet in quartets:
    signature = incidence([right_shores[k] for k in quartet])
    by_signature.setdefault(signature, []).append(quartet)

cases = []
counts = []
for owner, path in enumerate(middle_paths):
    row_counts = []
    for root in range(5):
        target = incidence([mask for i, mask in enumerate(path) if i != root])
        found = [q for q in by_signature.get(target, []) if owner not in q]
        for quartet in found:
            assert len(set(quartet)) == 4 and owner not in quartet
            assert incidence([right_shores[k] for k in quartet]) == target
        cases.append({'full_owner': owner, 'root': root,
                      'middle_path': path, 'target_coordinate_counts': target,
                      'surviving_quartets': found})
        row_counts.append(len(found))
    counts.append(row_counts)
report = {
    'host': socket.gethostname(),
    'scope': 'Necessary balance only: all four old shorts have z=1; '
             'z is absorbed into each displayed left shore; no row orders searched.',
    'base_rows': rows, 'old_longer_varying_right_shore_masks': right_shores,
    'full_owners': 14, 'roots_per_owner': 5,
    'eligible_quartets_per_owner_root': 715,
    'counts_by_owner_then_root': counts,
    'total_surviving_owner_root_quartets': sum(map(sum, counts)),
    'cases': cases, 'elapsed_seconds': time.monotonic() - started,
}
pathlib.Path(sys.argv[1]).write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('host', 'scope',
      'counts_by_owner_then_root', 'total_surviving_owner_root_quartets',
      'elapsed_seconds')}, indent=2))
