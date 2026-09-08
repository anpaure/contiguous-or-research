#!/usr/bin/env python3
"""One fixed native-bank port census; all mathematical execution is on h100."""
import hashlib
import json
import resource
import signal
import time
from collections import Counter, defaultdict
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
signal.alarm(150)
started = time.monotonic()
INPUT = Path('/home/amodo/exact-b-k17-triple-anchor-menus-20260908/canonical_w3_anchor_factorized_menus.json')
OUT = Path('/home/amodo/exact-b-k17-rank6-context-ports-20260908')
OUT.mkdir(parents=True, exist_ok=True)
raw = INPUT.read_bytes()
data = json.loads(raw)
assert hashlib.sha256(raw).hexdigest() == 'bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642'

def onebits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit

def union(values):
    result = 0
    for value in values:
        result |= value
    return result

def windows(word, width):
    return Counter(union(word[(i+j) % len(word)] for j in range(width)) for i in range(len(word)))

def coverage(word):
    # Direct forward cyclic intervals, never longer than one period.
    # Once the full period union is reached, longer intervals add nothing.
    full = union(word)
    seen = set()
    for start in range(len(word)):
        value = 0
        for length in range(1, len(word) + 1):
            value |= word[(start + length - 1) % len(word)]
            seen.add(value)
            if value == full:
                break
    return seen

groups = defaultdict(dict)
source_by_cycle = {}
ports = 0
pin_cap_replays = 0
for rec in data['cycles']:
    cid = rec['cycle']
    D, pin = rec['source'], rec['pins']
    v = len(D)
    source_by_cycle[cid] = D
    for i in range(v):
        j = (i + 1) % v
        original_pair = D[i] | D[j]
        P = D[(i-1) % v] | original_pair
        Q = original_pair | D[(i+2) % v]
        u, following = P & ~original_pair, Q & ~original_pair
        assert original_pair.bit_count() == 7
        assert P.bit_count() == Q.bit_count() == 8
        assert u.bit_count() == following.bit_count() == 1 and u != following
        assert (P | Q).bit_count() == 9
        removable = D[i] & D[j] & ~(pin[i] | pin[j])
        for a in onebits(removable):
            E, F = D[i] & ~a, D[j] & ~a
            K = E | F
            assert E.bit_count() == F.bit_count() == 5 and K.bit_count() == 6
            assert P == K | a | u and Q == K | a | following
            # Independent literal triple replays, not only the pin criterion.
            for start in range(i-2, i+2):
                old = union(D[z % v] for z in range(start, start+3))
                new = union(E if z % v == i else F if z % v == j else D[z % v]
                            for z in range(start, start+3))
                assert old == new
                pin_cap_replays += 1
            key = (E, F, u)
            assert a not in groups[key], 'Unique native rank-eight flank violated'
            groups[key][a] = dict(cycle=cid, position=i, removed=a,
                                 next_removed=following, E=E, F=F, K=K,
                                 left8=P, right8=Q, middle9=P | Q)
            ports += 1

cycles = []
for key in sorted(groups):
    edges = groups[key]
    finished = set()
    for start in sorted(edges):
        if start in finished:
            continue
        path, loc = [], {}
        current = start
        while current in edges and current not in finished and current not in loc:
            loc[current] = len(path)
            path.append(current)
            current = edges[current]['next_removed']
        if current in loc:
            loop = path[loc[current]:]
            if len(loop) >= 3:
                selected = [edges[a] for a in loop]
                cycles.append(dict(context=list(key), ports=selected,
                                   distinct_components=len({p['cycle'] for p in selected}) == len(selected)))
        finished.update(path)

usable = [row for row in cycles if row['distinct_components']]
report = dict(status='PASS', scope='One exact fixed-bank literal rank-six-context directed-cycle census, not a full-cube construction.',
              input_sha256=hashlib.sha256(raw).hexdigest(), eligible_ports=ports,
              exact_literal_triple_replays=pin_cap_replays, context_groups=len(groups),
              group_size_histogram=dict(sorted(Counter(len(g) for g in groups.values()).items())),
              directed_cycles_at_least_three=len(cycles), distinct_component_cycles=len(usable),
              directed_cycle_lengths=dict(sorted(Counter(len(c['ports']) for c in cycles).items())))

if usable:
    selected = usable[0]['ports']  # One prescribed lexicographically first witness, no search.
    originals, capped, pieces = [], [], []
    for port in selected:
        D = list(source_by_cycle[port['cycle']])
        originals.append(D)
        C = list(D)
        i, v = port['position'], len(C)
        C[i], C[(i+1) % v] = port['E'], port['F']
        capped.append(C)
        cut = (i+2) % v
        pieces.append(C[cut:] + C[:cut])
    order = [0] + list(range(len(pieces)-1, 0, -1))
    joined = [letter for j in order for letter in pieces[j]]
    for width in range(1, 5):
        old = Counter()
        for word in capped:
            old.update(windows(word, width))
        assert old == windows(joined, width)
    old_targets = set().union(*(coverage(w) for w in originals))
    cap_targets = set().union(*(coverage(w) for w in capped))
    joined_targets = coverage(joined)
    report['first_witness'] = dict(port_count=len(selected), period_length=len(joined),
        capped_width_one_through_four_multisets_preserved=True,
        original_targets=len(old_targets), capped_targets=len(cap_targets), joined_targets=len(joined_targets),
        preliminary_cap_lost=sorted(old_targets-cap_targets),
        splice_lost=sorted(cap_targets-joined_targets), splice_gained=sorted(joined_targets-cap_targets),
        splice_lost_rank_counts=dict(sorted(Counter(t.bit_count() for t in cap_targets-joined_targets).items())))
    (OUT/'first_joined_cycle.word').write_text(' '.join(map(str, joined))+'\n')
    (OUT/'first_join_certificate.json').write_text(json.dumps(dict(ports=selected, piece_order=order),indent=2)+'\n')

(OUT/'all_directed_port_cycles.json').write_text(json.dumps(cycles,indent=2)+'\n')
report['resource_caps'] = dict(cpu_seconds=120, wall_seconds=150, address_space_bytes=2*1024**3)
report['elapsed_seconds'] = time.monotonic()-started
(OUT/'rank6_context_port_census.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
