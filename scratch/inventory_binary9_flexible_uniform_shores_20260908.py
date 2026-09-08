"""h100-only uniform-z1 inventory with either absorbed old shore; no row orders."""
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
rows = json.loads(pathlib.Path(sys.argv[1]).read_text())['base_rows']

def prefixes(order):
    masks = [0]
    for bit in map(int, order):
        masks.append(masks[-1] | 1 << bit)
    return masks

def code(mask):
    return sum(((mask >> bit) & 1) << (4 * bit) for bit in range(8))

codes = [code(mask) for mask in range(256)]
owners = {}
packets = []
shorts = []
shores = []
paths = []
for owner, (left, right) in enumerate(rows):
    assert sorted(left + right) == list('01234567')
    cc, dd = prefixes(left), prefixes(right)
    family = {c | d for c in cc for d in dd}
    for target in family:
        if target.bit_count() in (3, 4, 5):
            assert target not in owners
            owners[target] = owner
    packets.append({x | z for x in family for z in (0, 256)})
    shorts.append([{a | b | 256 for a in cc[:-1] for b in dd},
                   {a | b | 256 for a in dd[:-1] for b in cc}])
    shores.append([cc[-1], dd[-1]])
    paths.append([cc[j] | dd[4-j] for j in range(5)])

report = {'host': socket.gethostname(), 'scope': 'Uniform-z1 shorts; either '
          'displayed shore may absorb z separately in each selected owner. '
          'Necessary complement-owner, coordinate-balance and root-endpoint tests only.',
          'base_rows': rows, 'owner_counts': [], 'surviving_sources': []}
quartets = list(itertools.combinations(range(14), 4))
for full_owner in range(14):
    bb = paths[full_owner]
    uu = [a | b for a, b in zip(bb, bb[1:])]
    required = {owners[255 ^ u] for u in uu}
    assert full_owner not in required
    by_root_code = {codes[b]: j for j, b in enumerate(bb)}
    total_b_code = sum(codes[b] for b in bb)
    counts = {'full_owner': full_owner, 'required_complement_owners': sorted(required),
              'quartets_containing_required_owners': 0,
              'shore_choices_with_balance': 0, 'surviving_sources': 0}
    for quartet in quartets:
        if full_owner in quartet or not required.issubset(quartet):
            continue
        counts['quartets_containing_required_owners'] += 1
        for side_mask in range(16):
            sides = [(side_mask >> h) & 1 for h in range(4)]
            # side0 absorbs displayedLEFT, so J is displayedRIGHT.
            jj = [shores[owner][1-side] for owner, side in zip(quartet, sides)]
            forced_root_code = total_b_code - sum(codes[j] for j in jj)
            root = by_root_code.get(forced_root_code)
            if root is None:
                continue
            assert all(sum((j >> bit) & 1 for j in jj)
                       == sum((b >> bit) & 1 for t, b in enumerate(bb) if t != root)
                       for bit in range(8))
            counts['shore_choices_with_balance'] += 1
            source = set(packets[full_owner])
            for owner, side in zip(quartet, sides):
                source.update(shorts[owner][side])
            critical = {x for x in source if x.bit_count() in (4, 5)}
            assert len(critical) == 50
            assert all(u in critical and (511 ^ u) in critical for u in uu)
            if (511 ^ bb[root]) not in critical:
                continue
            counts['surviving_sources'] += 1
            report['surviving_sources'].append({
                'full_owner': full_owner, 'root': root,
                'short_owners': quartet, 'absorbed_sides': sides,
                'absorbed_side_labels': ['L' if side == 0 else 'R' for side in sides],
                'old_unabsorbed_shores': jj, 'anchors': bb, 'no_z_rank5_targets': uu,
                'critical_source_masks': sorted(critical),
            })
    report['owner_counts'].append(counts)
report['surviving_source_count'] = len(report['surviving_sources'])
report['elapsed_seconds'] = time.monotonic() - started
report['status'] = 'complete'
pathlib.Path(sys.argv[2]).write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ('host', 'scope', 'status',
      'owner_counts', 'surviving_source_count', 'elapsed_seconds')}, indent=2))
