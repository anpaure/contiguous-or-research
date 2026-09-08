"""One h100-only complete9! inventory plus14-owner Boolean OR-zeta.

Tests only critical union availability for five whole old packets replaced
by nine full4+5 rows. No row selection, exact cover, or old partial catalogue.
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
started = time.monotonic()
rows = json.loads(pathlib.Path(sys.argv[1]).read_text())['base_rows']
output = pathlib.Path(sys.argv[2])

class Stop(Exception):
    pass

def timeout(signum, frame):
    raise Stop('4.5-second internal time limit')

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 4.5)

def prefixes(order):
    result = [0]
    for bit in map(int, order):
        result.append(result[-1] | 1 << bit)
    return result

owners = {}
packet_critical = []
for row_id, (left, right) in enumerate(rows):
    assert sorted(left + right) == list('01234567')
    cc, dd = prefixes(left), prefixes(right)
    family = {a | b for a in cc for b in dd}
    for target in family:
        if target.bit_count() in (3, 4, 5):
            assert target not in owners
            owners[target] = row_id
    critical = {x | z for x in family for z in (0, 256)
                if (x | z).bit_count() in (4, 5)}
    assert len(critical) == 18
    packet_critical.append(sum(1 << target for target in critical))
owner_bit = [0] * 512
target_bit = [1 << target for target in range(512)]
for target in range(512):
    if target.bit_count() in (4, 5):
        owner_bit[target] = 1 << owners[target & 255]

exact_unions = [0] * (1 << 14)
exact_counts = [0] * (1 << 14)
examples = {}
histogram = [0] * 15
bit = [1 << coordinate for coordinate in range(9)]
report = {'host': socket.gethostname(), 'scope': 'All full4+5 rows grouped by '
          'exact old-owner mask, followed by full Boolean OR-zeta; necessary '
          'critical availability for all five-whole-packet sources only.',
          'base_rows': rows, 'enumerated_full_rows': 0,
          'source_count_expected': 2002, 'source_results': [],
          'surviving_sources': [], 'phase': 'enumerate', 'status': 'RUNNING'}

try:
    for order in itertools.permutations(range(9)):
        # Ten critical cells form the alternating geodesic from the whole
        # shorter shore to the whole longer shore. This lists exactly the
        # two anti-diagonals of the full5-by6 prefix rectangle.
        current = bit[order[0]] | bit[order[1]] | bit[order[2]] | bit[order[3]]
        owner_mask = owner_bit[current]
        targets = target_bit[current]
        for j in range(4):
            current |= bit[order[4+j]]
            owner_mask |= owner_bit[current]
            targets |= target_bit[current]
            current ^= bit[order[3-j]]
            owner_mask |= owner_bit[current]
            targets |= target_bit[current]
        current |= bit[order[8]]
        owner_mask |= owner_bit[current]
        targets |= target_bit[current]
        assert targets.bit_count() == 10
        exact_unions[owner_mask] |= targets
        exact_counts[owner_mask] += 1
        examples.setdefault(owner_mask, ''.join(map(str, order)))
        histogram[owner_mask.bit_count()] += 1
        report['enumerated_full_rows'] += 1
    assert report['enumerated_full_rows'] == 362880
    report['phase'] = 'zeta'
    all_unions = exact_unions.copy()
    all_counts = exact_counts.copy()
    for coordinate in range(14):
        step = 1 << coordinate
        for mask in range(1 << 14):
            if mask & step:
                all_unions[mask] |= all_unions[mask ^ step]
                all_counts[mask] += all_counts[mask ^ step]
    assert all_counts[-1] == 362880
    report['phase'] = 'sources'
    for selected in itertools.combinations(range(14), 5):
        mask = sum(1 << owner for owner in selected)
        required = 0
        for owner in selected:
            required |= packet_critical[owner]
        assert required.bit_count() == 90
        available = all_unions[mask]
        assert not available & ~required
        missing = required & ~available
        record = {'owners': selected, 'owner_mask': mask,
                  'compatible_full_rows': all_counts[mask],
                  'covered_critical_targets': available.bit_count(),
                  'missing_critical_count': missing.bit_count(),
                  'one_missing_target': (missing & -missing).bit_length()-1 if missing else None}
        report['source_results'].append(record)
        if not missing:
            report['surviving_sources'].append(record)
    assert len(report['source_results']) == 2002
    report['status'] = 'COMPLETE'
    report['phase'] = 'done'
except Stop as stop:
    report['status'] = str(stop)
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    report['owner_mask_size_histogram'] = histogram
    report['exact_owner_mask_records'] = [
        {'owner_mask': mask, 'row_count': exact_counts[mask],
         'critical_union': exact_unions[mask], 'example_order': examples[mask]}
        for mask in examples]
    report['surviving_source_count'] = len(report['surviving_sources'])
    report['elapsed_seconds'] = time.monotonic() - started
    output.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps({key: report[key] for key in ('host', 'scope', 'status', 'phase',
          'enumerated_full_rows', 'owner_mask_size_histogram', 'source_count_expected',
          'surviving_source_count', 'elapsed_seconds')}, indent=2))
