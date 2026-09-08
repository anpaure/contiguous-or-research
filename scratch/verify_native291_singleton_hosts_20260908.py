#!/usr/bin/env python3
"""One fixed singleton-host census; execute mathematical work on h100 only."""
import json
import resource
import signal
from collections import defaultdict
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
signal.alarm(40)
ROOT = Path('/home/amodo/exact-b-native35-user-graft-20260908')
word = [int(x) for x in (ROOT / 'native291_rooted_word.word').read_text().split()]
assert len(word) == 291
full = (1 << 17) - 1
witnesses = defaultdict(list)
for a in range(len(word)):
    union = 0
    for b in range(a, len(word)):
        union |= word[b]
        witnesses[union].append((a, b))
        if union == full:
            break
assert len(witnesses) == 1876
missing = [x for x in range(1, 18) if (1 << (x - 1)) not in witnesses]
assert missing == list(range(1, 15))
report = {'word_length': len(word), 'missing_singletons': missing,
          'pair_preserving_hosts': {}, 'whole_family_safe_hosts': {},
          'unsafe_host_original_targets': {}}
for coordinate in missing:
    bit = 1 << (coordinate - 1)
    hosts, safe, unsafe = [], [], []
    for i, original in enumerate(word):
        if not original & bit:
            continue
        if i and (word[i-1] | bit) != (word[i-1] | original):
            continue
        if i+1 < len(word) and (bit | word[i+1]) != (original | word[i+1]):
            continue
        hosts.append(i)
        alternate = [(a, b) for a, b in witnesses[original]
                     if a != i or b != i]
        if alternate:
            safe.append({'position_zero_based': i, 'old_letter': original,
                         'protected_old_target_witness': list(alternate[0])})
        else:
            unsafe.append({'position_zero_based': i, 'old_letter': original})
    report['pair_preserving_hosts'][str(coordinate)] = hosts
    report['whole_family_safe_hosts'][str(coordinate)] = safe
    report['unsafe_host_original_targets'][str(coordinate)] = unsafe
(ROOT / 'native291_singleton_host_census.json').write_text(
    json.dumps(report, indent=2) + '\n')
print(json.dumps(report, separators=(',', ':')))
