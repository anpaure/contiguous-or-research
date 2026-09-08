"""Literal-only h100 check of four affine ternary repair rows; no search."""
import itertools
import json
import signal
import socket
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
started = time.monotonic()
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('one-second cap')))
signal.setitimer(signal.ITIMER_REAL, 1.0)

def chain(shore, first, last):
    assert first in shore and last in shore and first != last
    result = [tuple(0 for _ in shore),
              tuple(int(i == first) for i in shore),
              tuple(2 * int(i == first) for i in shore),
              tuple(2 * int(i != last) for i in shore),
              tuple(1 if i == last else 2 for i in shore),
              tuple(2 for _ in shore)]
    assert len(set(result)) == 6
    assert all(x != y and all(a <= b for a, b in zip(x, y))
               for x, y in zip(result, result[1:]))
    return result

def row(spec):
    left, right, al, bl, ar, br = spec
    left, right = tuple(map(int, left)), tuple(map(int, right))
    assert sorted(left + right) == list(range(8))
    assert len(left) == len(right) == 4
    c, d = chain(left, al, bl), chain(right, ar, br)
    targets = set()
    for x, y in itertools.product(c, d):
        target = [None] * 8
        for axis, value in zip(left + right, x + y):
            target[axis] = value
        targets.add(tuple(target))
    assert len(targets) == 36
    return {'left_support': left, 'right_support': right,
            'left_chain': c, 'right_chain': d,
            'first_axes': (al, ar), 'last_axes': (bl, br)}, targets

specs = [('0246', '1357', 0, 2, 1, 3),
         ('0145', '2367', 4, 1, 2, 6),
         ('0123', '4567', 3, 0, 5, 7),
         ('0356', '1247', 6, 5, 7, 4)]
parsed = [row(spec) for spec in specs]
rows = [data for data, _ in parsed]
sets = [targets for _, targets in parsed]
assert sorted(i for data in rows for i in data['first_axes']) == list(range(8))
assert sorted(i for data in rows for i in data['last_axes']) == list(range(8))
for a, b in itertools.combinations(rows, 2):
    for sa in (a['left_support'], a['right_support']):
        for sb in (b['left_support'], b['right_support']):
            assert len(set(sa) & set(sb)) == 2
shared = {(0,) * 8, (2,) * 8}
assert all(a & b == shared for a, b in itertools.combinations(sets, 2))
union = set().union(*sets)
assert len(union) == 138

ambient = itertools.product(range(3), repeat=8)
replay, boundary = set(), set()
for target in ambient:
    if sum(v != 0 for v in target) <= 1 or sum(v != 2 for v in target) <= 1:
        boundary.add(target)
    if any(tuple(target[i] for i in data['left_support']) in data['left_chain']
           and tuple(target[i] for i in data['right_support']) in data['right_chain']
           for data in rows):
        replay.add(target)
assert replay == union and len(boundary) == 34 and boundary <= union

old_specs = [('0123', '4567', t, (t+2) % 4,
              t+4, ((t+2) % 4)+4) for t in range(4)]
old_union = set().union(*(row(spec)[1] for spec in old_specs))
assert len(old_union) == 132
histograms = [(a, b, 8-a-b) for a in range(9) for b in range(9-a)]
assert len(histograms) == 45

def histogram(target):
    return tuple(target.count(v) for v in range(3))

old_counts = [sum(histogram(target) == h for target in old_union) for h in histograms]
new_counts = [sum(histogram(target) == h for target in union) for h in histograms]
differences = [b-a for a, b in zip(old_counts, new_counts)]
assert differences == [6 if h == (4, 0, 4) else 0 for h in histograms]
ranks = [sum(sum(target) == rank for target in union) for rank in range(17)]
assert ranks == [1,8,12,8,4,0,8,16,24,16,8,0,4,8,12,8,1]
assert sum(sum(target) == 8 and 1 not in target for target in union) == 16

signal.setitimer(signal.ITIMER_REAL, 0)
report = {'status': 'PASS', 'host': socket.gethostname(),
          'scope': 'Literal finite repair validation only; no optimization or search.',
          'elapsed_seconds': time.monotonic() - started,
          'rows': rows, 'row_occurrence_count': 144, 'principal_charge': 48,
          'union_size': len(union), 'union_targets': sorted(union),
          'pairwise_intersection': sorted(shared), 'rank_counts': ranks,
          'extremal_boundary_size': len(boundary), 'histograms': histograms,
          'old_132_union_histogram_counts': old_counts,
          'new_138_union_histogram_counts': new_counts,
          'histogram_difference': differences,
          'all_6561_targets_membership_replay': 'PASS',
          'inherited_necessary_short_row_histogram_optimum': [500, 3],
          'inherited_optimum_justification': 'Old primal remains feasible because only '
          'the central-corner demand falls by six. The unchanged rank-nine residual '
          '1000, with six targets per short row, retains the exact dual 500/3.'}
print(json.dumps(report, separators=(',', ':')))
