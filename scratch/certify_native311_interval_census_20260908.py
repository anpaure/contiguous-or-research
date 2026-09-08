#!/usr/bin/env python3
"""Fixed 311-letter witness census only. Execute on h100, never locally."""
import json
import resource
import signal
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(110)
base = Path('/home/amodo/exact-b-native35-user-graft-20260908')
word = list(map(int, (base/'native291_singletons_extended.word').read_text().split()))
old = list(map(int, (base/'native291_rooted_word.word').read_text().split()))
assert len(word) == 311 and word[:291] == old
records = {}
old_targets = set()
intervals = 0
for start in range(len(word)):
    value = 0
    for end in range(start, len(word)):
        value |= word[end]
        intervals += 1
        if end < 291:
            old_targets.add(value)
        if value not in records:
            records[value] = dict(mask=value, rank=value.bit_count(),
                first_witness=dict(start_zero_based=start, end_zero_based=end), occurrences=0)
        records[value]['occurrences'] += 1
rank_counts = Counter(x.bit_count() for x in records)
assert len(records) == 1979 and len(old_targets) == 1876
assert old_targets <= records.keys()
assert rank_counts[8] == rank_counts[9] == 308
assert sum(v for k,v in rank_counts.items() if k < 8) == 585
assert sum(v for k,v in rank_counts.items() if k < 9) == 893
assert all((1 << i) in records for i in range(17))
assert intervals == len(word)*(len(word)+1)//2
out = dict(word_file='native311_all_singletons.word', length=len(word),
    complete_interval_count=intervals, distinct_targets=len(records),
    rank_counts={str(k): rank_counts[k] for k in range(1,18)},
    old_prefix_length=291, old_targets=len(old_targets), old_targets_retained=True,
    new_target_count=len(records)-len(old_targets),
    targets=[records[x] for x in sorted(records)],
    new_target_masks=sorted(records.keys()-old_targets))
(base/'native311_all_singletons.word').write_text('\n'.join(map(str,word))+'\n')
(base/'native20_singleton_extension.word').write_text('\n'.join(map(str,word[291:]))+'\n')
(base/'native311_all_interval_witness_census.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('targets','new_target_masks')},indent=2))
print('PASS: every ordinary interval enumerated; every target has an exact retained witness.')
