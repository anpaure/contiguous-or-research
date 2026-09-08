"""Exact h100-only completion of the three flexible-shore uniform sources.

Generates the complete1152 forced-root row orders per source directly.
It never loads or filters the old fixed-left98k catalogue.
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
data = json.loads(pathlib.Path(sys.argv[1]).read_text())
output = pathlib.Path(sys.argv[2])
assert data['status'] == 'complete' and data['surviving_source_count'] <= 100

class Stop(Exception):
    pass

def timeout(signum, frame):
    raise Stop('13.5-second internal time limit')

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 13.5)

def bits(mask):
    return [j for j in range(9) if (mask >> j) & 1]

def prefixes(order):
    masks = [0]
    for j in order:
        masks.append(masks[-1] | 1 << j)
    return masks

def as_mask(targets):
    return sum(1 << target for target in set(targets))

def targets_of_order(order):
    assert sorted(order) == list(range(9))
    return {a | b for a in prefixes(order[:4]) for b in prefixes(order[4:])}

packets = []
shorts = []
base_load = [0] * 512
for left, right in data['base_rows']:
    cc, dd = prefixes(map(int, left)), prefixes(map(int, right))
    packet = {c | d | z for c in cc for d in dd for z in (0, 256)}
    packets.append(packet)
    shorts.append([{c | d | 256 for c in cc[:-1] for d in dd},
                   {c | d | 256 for c in dd[:-1] for d in cc}])
    for target in packet:
        base_load[target] += 1
assert all(base_load)
report = {'host': socket.gethostname(), 'scope': 'Uniform-z1, flexible absorbed '
          'shores; all forced-root orders and all512 targets; no fixed-left catalogue.',
          'cases': [], 'witness': None, 'stop_reason': None}

def save():
    report['elapsed_seconds'] = time.monotonic() - started
    tmp = output.with_suffix('.tmp')
    tmp.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    tmp.replace(output)

def make_literal_witness(source, chosen_orders):
    chosen = dict(zip(source['short_owners'], source['absorbed_sides']))
    rectangles = []
    for owner, (left, right) in enumerate(data['base_rows']):
        if owner == source['full_owner']:
            continue
        absorbed = chosen.get(owner, 0)
        aa, bb = (left, right) if absorbed == 0 else (right, left)
        aa, bb = list(map(int, aa)), list(map(int, bb))
        cc, dd = prefixes(aa), prefixes(bb)
        long_chain = cc + [cc[-1] | 256]
        short_chain = [c | 256 for c in cc[:-1]]
        rectangles.append({'source': ['old_long', owner, absorbed],
                           'left_support': aa + [8], 'right_support': bb,
                           'left_chain': long_chain, 'right_chain': dd})
        if owner not in chosen:
            rectangles.append({'source': ['old_short', owner, absorbed],
                               'left_support': aa + [8], 'right_support': bb,
                               'left_chain': short_chain, 'right_chain': dd})
    for order in chosen_orders:
        rectangles.append({'source': ['new_full'], 'left_support': list(order[:4]),
                           'right_support': list(order[4:]),
                           'left_chain': prefixes(order[:4]),
                           'right_chain': prefixes(order[4:])})
    loads = [0] * 512
    cost = 0
    for row in rectangles:
        assert sorted(row['left_support'] + row['right_support']) == list(range(9))
        for side in ('left', 'right'):
            chain = row[side + '_chain']
            support = sum(1 << j for j in row[side + '_support'])
            assert chain and all(not x & ~support for x in chain)
            assert all(a != b and not a & ~b for a, b in zip(chain, chain[1:]))
        cost += len(row['left_chain']) + len(row['right_chain'])
        for a in row['left_chain']:
            for b in row['right_chain']:
                loads[a | b] += 1
    assert len(rectangles) == 27 and cost == 279 and all(loads)
    assert all(loads[x] == 1 for x in range(512) if x.bit_count() in (4, 5))
    return {'source': source, 'new_orders': chosen_orders, 'rectangles': rectangles,
            'principal_charge': cost, 'all512_loads': loads, 'literal_replay': 'PASS'}

def replay(pool, critical, holes, nodes):
    pending, seen = [0], set()
    while pending:
        idx = pending.pop()
        if idx in seen:
            continue
        seen.add(idx)
        node = nodes[idx]
        cc, hh, used = node['critical'], node['holes'], node['used_slots']
        viable = [j for j, row in enumerate(pool)
                  if not used & (1 << row['slot']) and not cc & row['critical']]
        reason = node['kind']
        if reason in ('critical_unavailable', 'hole_unavailable'):
            key = 'critical' if reason == 'critical_unavailable' else 'holes'
            need = critical if key == 'critical' else holes
            covered = cc if key == 'critical' else hh
            target = node['target']
            assert (need >> target) & 1 and not (covered >> target) & 1
            assert all(not (pool[j][key] >> target) & 1 for j in viable)
        elif reason == 'full_but_incomplete':
            assert used == 31 and (cc != critical or hh != holes)
        elif reason == 'branch':
            slot = node['slot']
            assert not used & (1 << slot)
            required = {j for j in viable if pool[j]['slot'] == slot}
            assert len(node['branches']) == len(required)
            assert {j for j, child in node['branches']} == required
            for j, child in node['branches']:
                other = nodes[child]
                assert other['critical'] == cc | pool[j]['critical']
                assert other['holes'] == hh | pool[j]['holes']
                assert other['used_slots'] == used | (1 << slot)
                pending.append(child)
        else:
            raise AssertionError(reason)
    assert nodes[0]['critical'] == nodes[0]['holes'] == nodes[0]['used_slots'] == 0
    return len(seen)

try:
    for source_id, source in enumerate(data['surviving_sources']):
        owner, root = source['full_owner'], source['root']
        case = {'source_id': source_id, 'full_owner': owner, 'root': root,
                'short_owners': source['short_owners'], 'absorbed_sides': source['absorbed_sides'],
                'status': 'RUNNING'}
        report['cases'].append(case)
        residual = base_load.copy()
        for target in packets[owner]:
            residual[target] -= 1
        for j, side in zip(source['short_owners'], source['absorbed_sides']):
            for target in shorts[j][side]:
                residual[target] -= 1
        assert min(residual) >= 0
        missing = {x for x, load in enumerate(residual) if load == 0}
        holes = as_mask(missing)
        critical = as_mask(x for x in missing if x.bit_count() in (4, 5))
        assert critical.bit_count() == 50
        assert critical == as_mask(source['critical_source_masks'])
        aa, uu = source['anchors'], source['no_z_rank5_targets']
        generated = [0] * 5
        pool = []

        def retain(order, slot, expected_no_z):
            generated[slot] += 1
            targets = targets_of_order(order)
            cc = as_mask(x for x in targets if x.bit_count() in (4, 5))
            assert cc.bit_count() == 10
            assert {x for x in targets if x.bit_count() in (4, 5) and not x & 256} == expected_no_z
            if cc & ~critical:
                return
            pool.append({'order': order, 'slot': slot, 'critical': cc,
                         'holes': as_mask(targets & missing)})

        for edge, u in enumerate(uu, 1):
            child = edge - 1 if edge <= root else edge
            b = aa[child]
            assert not b & ~u and (u ^ b).bit_count() == 1
            last = bits(u ^ b)[0]
            for q_order in itertools.permutations(bits(255 ^ u)):
                for b_order in itertools.permutations(bits(b)):
                    order = (8,) + q_order + b_order + (last,)
                    retain(order, edge - 1, {b, u})
        b = aa[root]
        for b_order in itertools.permutations(bits(b)):
            for t_order in itertools.permutations(bits(255 ^ b)):
                retain(b_order + (8,) + t_order, 4, {b})
        assert generated == [144, 144, 144, 144, 576]
        case['generated_counts_by_slot'] = generated
        case['retained_counts_by_slot'] = [sum(row['slot'] == slot for row in pool) for slot in range(5)]
        case['candidate_orders'] = [{'order': row['order'], 'slot': row['slot']} for row in pool]
        case['required_targets'] = sorted(missing)
        nodes, failed = [], {}

        def dfs(cc, hh, used, chosen):
            state = (cc, hh, used)
            if state in failed:
                return None, failed[state]
            if len(nodes) >= 100000:
                raise Stop('100000-node reporting cap')
            idx = len(nodes)
            node = {'critical': cc, 'holes': hh, 'used_slots': used}
            nodes.append(node)
            if used == 31:
                if cc == critical and hh == holes:
                    return chosen, idx
                node['kind'] = 'full_but_incomplete'
                failed[state] = idx
                return None, idx
            viable = [j for j, row in enumerate(pool)
                      if not used & (1 << row['slot']) and not cc & row['critical']]
            uc, uh = cc, hh
            for j in viable:
                uc |= pool[j]['critical']
                uh |= pool[j]['holes']
            if uc != critical:
                unavailable = critical & ~uc
                node.update(kind='critical_unavailable', target=(unavailable & -unavailable).bit_length()-1)
                failed[state] = idx
                return None, idx
            if uh != holes:
                unavailable = holes & ~uh
                node.update(kind='hole_unavailable', target=(unavailable & -unavailable).bit_length()-1)
                failed[state] = idx
                return None, idx
            choices = [(slot, [j for j in viable if pool[j]['slot'] == slot])
                       for slot in range(5) if not used & (1 << slot)]
            slot, options = min(choices, key=lambda item: len(item[1]))
            node.update(kind='branch', slot=slot, branches=[])
            for j in options:
                row = pool[j]
                witness, child = dfs(cc | row['critical'], hh | row['holes'],
                                     used | 1 << slot, chosen + [j])
                node['branches'].append([j, child])
                if witness is not None:
                    return witness, idx
            failed[state] = idx
            return None, idx

        witness, proof_root = dfs(0, 0, 0, [])
        assert proof_root == 0
        case['dfs_nodes'] = len(nodes)
        if witness is not None:
            report['witness'] = make_literal_witness(source, [pool[j]['order'] for j in witness])
            case['status'] = 'VERIFIED_FULL_CUBE_WITNESS'
            report['stop_reason'] = 'first verified charge279 witness'
            save()
            break
        case['proof_nodes'] = nodes
        case['status'] = 'INFEASIBLE_PROOF_REPLAY_PENDING'
        case['proof_nodes_replayed'] = replay(pool, critical, holes, nodes)
        case['status'] = 'INFEASIBLE_EXHAUSTIVE_PROOF_REPLAY_PASS'
        if len(nodes) == 1:
            case['unavailable_target'] = nodes[0].get('target')
        save()
    else:
        report['stop_reason'] = 'all flexible-uniform sources completed'
except Stop as stop:
    report['stop_reason'] = str(stop)
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    save()
    print(json.dumps({'host': report['host'], 'stop_reason': report['stop_reason'],
                      'elapsed_seconds': report['elapsed_seconds'],
                      'witness_found': report['witness'] is not None,
                      'cases': [{k: case[k] for k in ('source_id', 'full_owner', 'root',
                                'short_owners', 'absorbed_sides', 'status',
                                'generated_counts_by_slot', 'retained_counts_by_slot',
                                'dfs_nodes', 'unavailable_target') if k in case}
                                for case in report['cases']]}, indent=2))
