"""h100-only mixed-sign endpoint/anchor inventory; no new row-order enumeration.

Uses the 56-edge base-owner graph, exact coordinate vectors, and at most
120 assignments of five longer supports to the packet's five anchors.
Stores one necessary-certificate witness per surviving source choice.
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
base = json.loads(pathlib.Path(sys.argv[1]).read_text())
rows = base['base_rows']

class InventoryStop(Exception):
    pass

def timed_out(signum, frame):
    raise InventoryStop('14-second internal time limit')

signal.signal(signal.SIGALRM, timed_out)
signal.setitimer(signal.ITIMER_REAL, 14)

def prefixes(order):
    result = [0]
    for bit in map(int, order):
        result.append(result[-1] | (1 << bit))
    return result

def encode_incidence(mask):
    return sum(((mask >> bit) & 1) << (4 * bit) for bit in range(8))

encoded = [encode_incidence(mask) for mask in range(256)]
ones = encoded[255]
rank4_by_code = {encoded[x]: x for x in range(256) if x.bit_count() == 4}
owner = {}
anchors = []
right_shores = []
packet_bits = []
short_bits = []
for row_id, (left, right) in enumerate(rows):
    assert sorted(left + right) == list('01234567')
    cp, dp = prefixes(left), prefixes(right)
    right_shores.append(dp[-1])
    anchors.append([cp[j] | dp[4-j] for j in range(5)])
    family = {c | d for c in cp for d in dp}
    for target in family:
        if target.bit_count() in (3, 4, 5):
            assert target not in owner
            owner[target] = row_id
    packet = {x | z for x in family for z in (0, 256)}
    shorts = [{c | d for c in cp[1:] for d in dp},
              {c | d | 256 for c in cp[:-1] for d in dp}]
    pp = sum(1 << x for x in packet if x.bit_count() in (4, 5))
    ss = [sum(1 << x for x in s if x.bit_count() in (4, 5)) for s in shorts]
    assert pp.bit_count() == 18 and all(x.bit_count() == 8 for x in ss)
    packet_bits.append(pp)
    short_bits.append(ss)

outgoing = [[] for _ in rows]
incoming_counts = [0] * len(rows)
edges = []
for u in range(256):
    if u.bit_count() != 5:
        continue
    a, b = owner[u], owner[255 ^ u]
    assert a != b
    outgoing[a].append((u, b))
    incoming_counts[b] += 1
    edges.append({'rank5_mask': u, 'from_owner': a, 'to_owner': b})
assert len(edges) == 56
assert all(len(es) == 4 for es in outgoing)
assert incoming_counts == [4] * 14

quartets = list(itertools.combinations(range(14), 4))
quartet_code = {q: ones + sum(encoded[right_shores[j]] for j in q) for q in quartets}
anchor_permutations = list(itertools.permutations(range(5)))
report = {
    'host': socket.gethostname(),
    'scope': 'Fixed-left source, four mixed-sign shorts plus one full packet. '
             'Necessary endpoint/incidence/vertical-anchor certificates only; '
             'no internal row orders or all-rank replacement cover checked.',
    'base_rows': rows, 'owner_edges': edges,
    'source_choices_expected': 160160,
    'owners_completed': [], 'owner_counts': [], 'surviving_sources': [],
    'stop_reason': None,
}
active_owner = None
active_source = None
counts = None

try:
    for full_owner in range(14):
        active_owner = full_owner
        counts = {'full_owner': full_owner, 'source_choices_processed': 0,
                  'sources_with_at_least_four_owner_edges': 0,
                  'support_selections_passing_endpoints': 0,
                  'sources_with_endpoint_certificate': 0,
                  'sources_with_anchor_certificate': 0,
                  'survivors_by_number_zero_shorts': [0] * 5}
        report['owner_counts'].append(counts)
        bb = anchors[full_owner]
        for quartet in quartets:
            if full_owner in quartet:
                continue
            target_code = quartet_code[quartet]
            for sign_mask in range(16):
                signs = tuple((sign_mask >> h) & 1 for h in range(4))
                active_source = {'full_owner': full_owner, 'short_owners': quartet,
                                 'short_signs': signs}
                counts['source_choices_processed'] += 1
                s0 = [full_owner]
                s1mask = 1 << full_owner
                source = packet_bits[full_owner]
                for j, sign in zip(quartet, signs):
                    source |= short_bits[j][sign]
                    if sign:
                        s1mask |= 1 << j
                    else:
                        s0.append(j)
                assert source.bit_count() == 50
                available = sorted(u for j in s0 for u, to in outgoing[j]
                                   if s1mask & (1 << to))
                if len(available) < 4:
                    continue
                counts['sources_with_at_least_four_owner_edges'] += 1
                n0 = 4 - sum(signs)
                target_position_sum = 5 + 4 * n0
                saw_endpoint = False
                saved = False
                for uu in itertools.combinations(available, 4):
                    # No coordinate count exceeds5. Base16 encoding has no
                    # carry; every accepted match is also checked componentwise.
                    forced_code = target_code - sum(encoded[u] for u in uu)
                    tt = rank4_by_code.get(forced_code)
                    if tt is None:
                        continue
                    if not (source >> (tt | 256)) & 1:
                        continue
                    if not (source >> (255 ^ tt)) & 1:
                        continue
                    assert all(1 + sum((right_shores[j] >> bit) & 1 for j in quartet)
                               == sum((u >> bit) & 1 for u in uu) + ((tt >> bit) & 1)
                               for bit in range(8))
                    assert all((source >> u) & 1 and (source >> (511 ^ u)) & 1 for u in uu)
                    counts['support_selections_passing_endpoints'] += 1
                    if not saw_endpoint:
                        saw_endpoint = True
                        counts['sources_with_endpoint_certificate'] += 1
                    position_table = [[5 - (b & u).bit_count() for b in bb] for u in uu]
                    position_table.append([1 + (b & tt).bit_count() for b in bb])
                    for assignment in anchor_permutations:
                        positions = [position_table[h][assignment[h]] for h in range(5)]
                        if sum(positions) != target_position_sum:
                            continue
                        assert all(1 <= p <= 4 for p in positions[:4]) and 1 <= positions[4] <= 5
                        witness = {'full_owner': full_owner,
                                   'short_owners': quartet, 'short_signs': signs,
                                   'number_zero_shorts': n0,
                                   'no_z_longer_supports': uu,
                                   'z_longer_support': tt | 256,
                                   'anchors_in_packet_order': bb,
                                   'assigned_anchor_indices_by_support': assignment,
                                   'forced_z_positions_by_support': positions,
                                   'position_sum': sum(positions),
                                   'available_owner_cut_supports': available}
                        report['surviving_sources'].append(witness)
                        counts['sources_with_anchor_certificate'] += 1
                        counts['survivors_by_number_zero_shorts'][n0] += 1
                        saved = True
                        break
                    if saved:
                        break
                if len(report['surviving_sources']) >= 1000:
                    raise InventoryStop('1000-surviving-source reporting cap')
        report['owners_completed'].append(full_owner)
    report['stop_reason'] = 'complete'
except InventoryStop as stop:
    report['stop_reason'] = str(stop)
    report['interrupted_source'] = active_source
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    report['elapsed_seconds'] = time.monotonic() - started
    report['source_choices_processed'] = sum(c['source_choices_processed'] for c in report['owner_counts'])
    report['surviving_source_count'] = len(report['surviving_sources'])
    pathlib.Path(sys.argv[2]).write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps({key: report[key] for key in ('host', 'scope', 'stop_reason',
          'owners_completed', 'source_choices_expected', 'source_choices_processed',
          'owner_counts', 'surviving_source_count', 'elapsed_seconds')}, indent=2))
