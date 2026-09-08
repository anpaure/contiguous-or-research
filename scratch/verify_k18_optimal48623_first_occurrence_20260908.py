#!/usr/bin/env python3
"""Independent ordinary-interval OR census by first coordinate occurrences."""
import hashlib
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(45)
started = time.monotonic()
SOURCE = Path('/home/amodo/k18_optimal48623_first_occurrence_input.word')
OUT = Path('/home/amodo/exact-b-k18-optimal48623-first-occurrence-20260908')
OUT.mkdir(exist_ok=False)
FULL = (1 << 18) - 1
raw = SOURCE.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
word = [int(token) for token in raw.split()]
assert len(word) == 48623
assert all(1 <= x <= FULL for x in word)

# For a fixed start i, coordinate c enters the interval OR exactly at its
# first occurrence at or after i. All coordinates with the same occurrence
# position must be added together. The OR is constant between event positions.
next_position = [len(word)] * 18
witnesses = {}
event_count = 0
for left in range(len(word)-1, -1, -1):
    letter = word[left]
    for c in range(18):
        if letter & (1 << c):
            next_position[c] = left
    events = {}
    for c, right in enumerate(next_position):
        if right < len(word):
            events[right] = events.get(right, 0) | (1 << c)
    union = 0
    for right in sorted(events):
        union |= events[right]
        assert 0 <= left <= right < len(word)
        witnesses.setdefault(union, (left, right))
        event_count += 1

missing = [target for target in range(1, FULL+1) if target not in witnesses]
rank_counts = dict(sorted(Counter(target.bit_count() for target in witnesses).items()))
status = 'PASS' if not missing else 'FAIL_MISSING_TARGETS'
assert rank_counts == {r: math.comb(18, r) for r in range(1, 19)} if not missing else True
report = dict(status=status, length=len(word), sha256=sha,
              targets=len(witnesses), expected_targets=FULL,
              missing_target_count=len(missing), missing_targets=missing,
              target_rank_counts=rank_counts, first_occurrence_events=event_count,
              all_letters_nonzero_and_in_18_cube=True,
              algorithm='Independent first-occurrence endpoint enumeration. Coordinates with identical first-occurrence positions are grouped before recording OR. Every ordinary interval OR is one recorded event OR; no suffix recurrence, wrapping, or segment tree is used.',
              resource_caps=dict(cpu_seconds=30, wall_seconds=45,
                                 address_space_bytes=1024**3),
              elapsed_seconds=time.monotonic()-started)
(OUT / 'k18_optimal48623_first_occurrence_certificate.json').write_text(json.dumps(report, indent=2)+'\n')
(OUT / 'k18_optimal48623.word').write_bytes(raw)
with (OUT / 'k18_optimal48623_first_occurrence_witnesses.jsonl').open('w') as stream:
    for target in sorted(witnesses):
        stream.write(json.dumps([target, *witnesses[target]])+'\n')
print(json.dumps(report), flush=True)
