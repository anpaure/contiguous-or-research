"""h100-only endpoint-availability certificate for six fixed uniform sources."""
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
catalogue = json.loads(pathlib.Path(sys.argv[1]).read_text())
balance = json.loads(pathlib.Path(sys.argv[2]).read_text())

def prefixes(order):
    result = [0]
    for bit in map(int, order):
        result.append(result[-1] | (1 << bit))
    return result

owner = {}
literal_packets = []
literal_shorts = []
for row_id, (left, right) in enumerate(catalogue['base_rows']):
    cp, dp = prefixes(left), prefixes(right)
    family = {c | d for c in cp for d in dp}
    for target in family:
        if target.bit_count() in (3, 4, 5):
            assert target not in owner
            owner[target] = row_id
    packet = {x | bit for x in family for bit in (0, 256)}
    short = {c | d | 256 for c in cp[:-1] for d in dp}
    assert packet == set(catalogue['packets'][row_id]['full_targets'])
    assert short == set(catalogue['shorts'][row_id]['full_targets_by_z'][1])
    literal_packets.append(packet)
    literal_shorts.append(short)

cases = []
for balance_case in balance['cases']:
    for quartet in balance_case['surviving_quartets']:
        full_owner = balance_case['full_owner']
        root = balance_case['root']
        path = balance_case['middle_path']
        upper = [a | b for a, b in zip(path, path[1:])]
        assert len(set(upper)) == 4 and all(u.bit_count() == 5 for u in upper)
        source = set(literal_packets[full_owner])
        for j in quartet:
            source.update(literal_shorts[j])
        critical_source = {x for x in source if x.bit_count() in (4, 5)}
        assert len(critical_source) == 50
        requirements = []
        for edge, u in enumerate(upper, 1):
            triple = 255 ^ u
            target = triple | 256
            triple_owner = owner[triple]
            assert triple_owner != full_owner
            present = target in critical_source
            assert present == (triple_owner in quartet)
            requirements.append({'edge': edge, 'no_z_rank5_mask': u,
                                 'complement_rank3_mask': triple,
                                 'required_z1_rank4_mask': target,
                                 'required_old_owner': triple_owner,
                                 'available': present})
        root_complement = 511 ^ path[root]
        root_requirement = {'root_rank4_mask': path[root],
                            'required_z1_rank5_mask': root_complement,
                            'available': root_complement in critical_source}
        missing = [entry for entry in requirements if not entry['available']]
        passes = not missing and root_requirement['available']
        cases.append({'full_owner': full_owner, 'root': root,
                      'short_owners': quartet,
                      'required_upper_complements': requirements,
                      'root_complement': root_requirement,
                      'missing_upper_complement_certificate': missing[0] if missing else None,
                      'passes_all_endpoint_availability': passes})
assert len(cases) == 6
report = {'host': socket.gethostname(), 'scope': 'Literal endpoint-availability only; no solver.',
          'cases': cases,
          'surviving_cases': [c for c in cases if c['passes_all_endpoint_availability']],
          'elapsed_seconds': time.monotonic() - started}
pathlib.Path(sys.argv[3]).write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
