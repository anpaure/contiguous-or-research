"""Bounded literal full-row catalogue for one packet plus four shorts.

No solver. The displayed base left shore absorbs coordinate z=8.
The two choices for each short are its constant z value, 0 or 1.
Run only through ssh h100; output both summary and the complete catalogue.
"""
import itertools
import json
import os
import pathlib
import resource
import signal
import socket
import sys
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(19)
started = time.monotonic()

ROWS = [
    ('0461', '5723'), ('0473', '2651'), ('0674', '3152'),
    ('0726', '1435'), ('1507', '4263'), ('1605', '7432'),
    ('2104', '6375'), ('2150', '7463'), ('3206', '7154'),
    ('3210', '4567'), ('3617', '5204'), ('4302', '6157'),
    ('5034', '6721'), ('5426', '7301'),
]

def prefixes(order):
    result = [0]
    for coordinate in order:
        result.append(result[-1] | (1 << coordinate))
    return result

owner = {}
meta = {}
packets = []
shorts = []
all_base = set()
for row_id, (left, right) in enumerate(ROWS):
    assert sorted(left + right) == list('01234567')
    cp = prefixes(map(int, left))
    dp = prefixes(map(int, right))
    full = {c | d | bit for c in cp for d in dp for bit in (0, 256)}
    all_base.update(c | d for c in cp for d in dp)
    critical = sorted(x for x in full if x.bit_count() in (4, 5))
    assert len(critical) == 18
    ss = [sorted({c | d for c in cp[1:] for d in dp}),
          sorted({c | d | 256 for c in cp[:-1] for d in dp})]
    ssc = [set(x for x in part if x.bit_count() in (4, 5)) for part in ss]
    assert all(len(part) == 8 for part in ssc)
    for ci, c in enumerate(cp):
        for d in dp:
            base = c | d
            if base.bit_count() in (3, 4, 5):
                assert base not in owner
                owner[base] = row_id
    for x in critical:
        assert x not in meta
        sign = int(bool(x & 256))
        meta[x] = (row_id, sign if x in ssc[sign] else -1)
    packets.append({'owner': row_id, 'full_targets': sorted(full),
                    'critical_targets': critical})
    shorts.append({'owner': row_id, 'full_targets_by_z': ss,
                   'critical_targets_by_z': [sorted(p) for p in ssc]})
assert len(all_base) == 256
assert len(meta) == 252

candidates = []
counts_by_owner = [0] * 14
counts_by_required_short_owners = [0] * 5
tested = 0
for order in itertools.permutations(range(9)):
    tested += 1
    cp = prefixes(order[:4])
    dp = prefixes(order[4:])
    zp = order.index(8)
    if zp < 4:
        p = zp + 1
        base = cp[p - 1] | dp[5 - p]
    else:
        p = zp - 3
        base = cp[5 - p] | dp[p - 1]
    assert not base & 256 and base.bit_count() == 4
    full_owner = owner[base]
    required = {}
    critical = [cp[i] | dp[rank - i]
                for rank in (4, 5) for i in range(5)]
    feasible = True
    for target in critical:
        target_owner, sign = meta[target]
        if target_owner == full_owner:
            continue
        previous = required.get(target_owner, sign)
        if sign < 0 or previous != sign:
            feasible = False
            break
        required[target_owner] = sign
        if len(required) > 4:
            feasible = False
            break
    if not feasible:
        continue
    assert base in critical and (base | 256) in critical
    counts_by_owner[full_owner] += 1
    counts_by_required_short_owners[len(required)] += 1
    candidates.append({
        'order': ''.join(map(str, order)),
        'full_owner': full_owner,
        'required_shorts': sorted(required.items()),
        'critical_targets': sorted(critical),
    })
assert tested == 362880

report = {
    'host': socket.gethostname(),
    'scope': 'All 9! full ordered 4+5 prefix rectangles; no solver. '
             'Exactly one forced fully freed base owner; all others '
             'must fit at most four fixed-left short hooks.',
    'base_rows': ROWS,
    'z': 8,
    'tested_full_rows': tested,
    'candidate_count': len(candidates),
    'counts_by_full_owner': counts_by_owner,
    'counts_by_required_short_owners': counts_by_required_short_owners,
    'elapsed_seconds': time.monotonic() - started,
    'packets': packets,
    'shorts': shorts,
    'candidates': candidates,
}
output = pathlib.Path(sys.argv[1])
output.write_text(json.dumps(report, separators=(',', ':')) + '\n')
summary = {key: report[key] for key in (
    'host', 'scope', 'tested_full_rows', 'candidate_count',
    'counts_by_full_owner', 'counts_by_required_short_owners',
    'elapsed_seconds')}
print(json.dumps(summary, indent=2))
