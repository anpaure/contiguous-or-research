"""h100-only exact completion of ALL24 necessary source survivors.

Uses the complete existing98k catalogue. The saved example longer supports
and anchor assignment are deliberately ignored. Every compatible full row
is retained. Exact-cover DFS is independently replayed as a finite proof DAG.
"""
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
catalogue = json.loads(pathlib.Path(sys.argv[1]).read_text())
inventory = json.loads(pathlib.Path(sys.argv[2]).read_text())
output = pathlib.Path(sys.argv[3])

class Stop(Exception):
    pass

def timeout(signum, frame):
    raise Stop('14-second internal time limit')

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 14)

def prefixes(order):
    masks = [0]
    for bit in order:
        masks.append(masks[-1] | (1 << bit))
    return masks

def row_targets(order):
    bits = list(map(int, order))
    assert sorted(bits) == list(range(9))
    return {a | b for a in prefixes(bits[:4]) for b in prefixes(bits[4:])}

def mask_set(values):
    return sum(1 << value for value in set(values))

def first_bit(mask):
    return (mask & -mask).bit_length() - 1

base_load = [0] * 512
for packet in catalogue['packets']:
    for target in packet['full_targets']:
        base_load[target] += 1
assert all(base_load)
groups = [[] for _ in range(14)]
for row in catalogue['candidates']:
    groups[row['full_owner']].append(row)
report = {'host': socket.gethostname(), 'scope': 'All24 fixed-left source choices; '
          'complete98k catalogue filtered only by full owner and fixed short signs; '
          'all512 targets required. No restriction to saved endpoint witnesses.',
          'cases': [], 'witness': None, 'stop_reason': None}

def save():
    report['elapsed_seconds'] = time.monotonic() - started
    temporary = output.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    temporary.replace(output)

def verify_negative_proof(pool, critical, holes, nodes, root):
    """Independent branch-coverage replay, with no recursive search or memo reuse."""
    done = set()
    todo = [root]
    while todo:
        node_id = todo.pop()
        if node_id in done:
            continue
        done.add(node_id)
        node = nodes[node_id]
        covered = node['covered_critical']
        covered_holes = node['covered_holes']
        assert not covered & ~critical and not covered_holes & ~holes
        viable = [i for i, row in enumerate(pool) if not row['critical'] & covered]
        kind = node['kind']
        if kind == 'critical_unavailable':
            target = node['target']
            assert (critical >> target) & 1 and not (covered >> target) & 1
            assert all(not (pool[i]['critical'] >> target) & 1 for i in viable)
        elif kind == 'hole_unavailable':
            target = node['target']
            assert (holes >> target) & 1 and not (covered_holes >> target) & 1
            assert all(not (pool[i]['holes'] >> target) & 1 for i in viable)
        elif kind == 'full_critical_but_hole_missing':
            assert covered == critical and covered_holes != holes
        elif kind == 'branch':
            target = node['target']
            assert (critical >> target) & 1 and not (covered >> target) & 1
            required_rows = {i for i in viable if (pool[i]['critical'] >> target) & 1}
            branches = node['branches']
            assert len(branches) == len(required_rows)
            assert {row_id for row_id, _ in branches} == required_rows
            for row_id, child in branches:
                assert child != node_id
                child_node = nodes[child]
                assert child_node['covered_critical'] == covered | pool[row_id]['critical']
                assert child_node['covered_holes'] == covered_holes | pool[row_id]['holes']
                assert child_node['covered_critical'].bit_count() == covered.bit_count() + 10
                todo.append(child)
        else:
            raise AssertionError(('bad proof node', kind))
    assert nodes[root]['covered_critical'] == nodes[root]['covered_holes'] == 0
    return len(done)

def literal_witness(full_owner, chosen_shorts, orders):
    """Rebuild actual27 rectangles independently of target-bitset DFS."""
    rectangles = []
    for owner, (left, right) in enumerate(catalogue['base_rows']):
        if owner == full_owner:
            continue
        li, ri = list(map(int, left)), list(map(int, right))
        cp, dp = prefixes(li), prefixes(ri)
        sign = chosen_shorts.get(owner, 0)
        if sign == 0:
            long_chain = [0] + [c | 256 for c in cp]
            short_chain = cp[1:]
        else:
            long_chain = cp + [cp[-1] | 256]
            short_chain = [c | 256 for c in cp[:-1]]
        rectangles.append({'source': ['old_long', owner, sign],
                           'left_support': li + [8], 'right_support': ri,
                           'left_chain': long_chain, 'right_chain': dp})
        if owner not in chosen_shorts:
            rectangles.append({'source': ['old_short', owner, sign],
                               'left_support': li + [8], 'right_support': ri,
                               'left_chain': short_chain, 'right_chain': dp})
    for order in orders:
        order = list(map(int, order))
        rectangles.append({'source': ['new_full'],
                           'left_support': order[:4], 'right_support': order[4:],
                           'left_chain': prefixes(order[:4]),
                           'right_chain': prefixes(order[4:])})
    loads = [0] * 512
    charge = 0
    for row in rectangles:
        assert sorted(row['left_support'] + row['right_support']) == list(range(9))
        for side in ('left', 'right'):
            support = sum(1 << bit for bit in row[side + '_support'])
            chain = row[side + '_chain']
            assert chain and all(not member & ~support for member in chain)
            assert all(a != b and not a & ~b for a, b in zip(chain, chain[1:]))
        charge += len(row['left_chain']) + len(row['right_chain'])
        for a in row['left_chain']:
            for b in row['right_chain']:
                loads[a | b] += 1
    assert len(rectangles) == 27 and charge == 279 and all(loads)
    assert all(loads[x] == 1 for x in range(512) if x.bit_count() in (4, 5))
    return {'full_owner': full_owner, 'selected_shorts': sorted(chosen_shorts.items()),
            'new_full_orders': orders, 'rectangles': rectangles,
            'principal_charge': charge, 'all512_loads': loads,
            'literal_independent_replay': 'PASS'}

try:
    assert inventory['stop_reason'] == 'complete'
    assert inventory['surviving_source_count'] == 24
    for source_id, source in enumerate(inventory['surviving_sources']):
        # Do not read source's saved support or anchor witness fields.
        full_owner = source['full_owner']
        chosen = dict(zip(source['short_owners'], source['short_signs']))
        case = {'source_id': source_id, 'full_owner': full_owner,
                'short_owners': source['short_owners'], 'short_signs': source['short_signs'],
                'status': 'RUNNING'}
        report['cases'].append(case)
        residual = base_load.copy()
        for target in catalogue['packets'][full_owner]['full_targets']:
            residual[target] -= 1
        for owner, sign in chosen.items():
            for target in catalogue['shorts'][owner]['full_targets_by_z'][sign]:
                residual[target] -= 1
        assert min(residual) >= 0
        missing = {target for target, load in enumerate(residual) if load == 0}
        holes = mask_set(missing)
        critical = mask_set(target for target in missing if target.bit_count() in (4, 5))
        assert critical.bit_count() == 50
        left, right = catalogue['base_rows'][full_owner]
        cp, dp = prefixes(map(int, left)), prefixes(map(int, right))
        anchors = [cp[i] | dp[4-i] for i in range(5)]
        pool = []
        anchor_counts = [0] * 5
        for candidate in groups[full_owner]:
            if any(chosen.get(owner) != sign for owner, sign in candidate['required_shorts']):
                continue
            targets = row_targets(candidate['order'])
            cc = mask_set(t for t in targets if t.bit_count() in (4, 5))
            assert cc.bit_count() == 10 and not cc & ~critical
            assert set(candidate['critical_targets']) == {t for t in targets if t.bit_count() in (4, 5)}
            aa = [i for i, b in enumerate(anchors) if b in targets and (b | 256) in targets]
            assert len(aa) == 1
            anchor_counts[aa[0]] += 1
            pool.append({'order': candidate['order'], 'critical': cc,
                         'holes': mask_set(targets & missing), 'anchor': aa[0]})
        case['candidate_count'] = len(pool)
        case['candidates_by_anchor'] = anchor_counts
        case['all_rank_holes'] = sorted(missing)
        case['candidate_orders'] = [row['order'] for row in pool]
        nodes = []
        memo = {}

        def dfs(covered, covered_holes, selected):
            key = (covered, covered_holes)
            if key in memo:
                return None, memo[key]
            if len(nodes) >= 100000:
                raise Stop('100000-node reporting cap')
            node_id = len(nodes)
            node = {'covered_critical': covered, 'covered_holes': covered_holes}
            nodes.append(node)
            if covered == critical:
                assert len(selected) == 5
                if covered_holes == holes:
                    return selected, node_id
                node['kind'] = 'full_critical_but_hole_missing'
                memo[key] = node_id
                return None, node_id
            viable = [i for i, row in enumerate(pool) if not row['critical'] & covered]
            union_critical = covered
            union_holes = covered_holes
            for row_id in viable:
                union_critical |= pool[row_id]['critical']
                union_holes |= pool[row_id]['holes']
            if union_critical != critical:
                node.update(kind='critical_unavailable', target=first_bit(critical & ~union_critical))
                memo[key] = node_id
                return None, node_id
            if union_holes != holes:
                node.update(kind='hole_unavailable', target=first_bit(holes & ~union_holes))
                memo[key] = node_id
                return None, node_id
            remaining = critical & ~covered
            best = None
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                choices = [i for i in viable if pool[i]['critical'] & bit]
                if best is None or len(choices) < len(best[1]):
                    best = (bit.bit_length() - 1, choices)
            target, choices = best
            node.update(kind='branch', target=target, branches=[])
            choices.sort(key=lambda i: -(pool[i]['holes'] & ~covered_holes).bit_count())
            for row_id in choices:
                row = pool[row_id]
                witness, child = dfs(covered | row['critical'], covered_holes | row['holes'],
                                     selected + [row_id])
                node['branches'].append([row_id, child])
                if witness is not None:
                    return witness, node_id
            memo[key] = node_id
            return None, node_id

        witness, proof_root = dfs(0, 0, [])
        case['dfs_nodes'] = len(nodes)
        if witness is not None:
            orders = [pool[i]['order'] for i in witness]
            report['witness'] = literal_witness(full_owner, chosen, orders)
            case['status'] = 'VERIFIED_FULL_CUBE_WITNESS'
            report['stop_reason'] = 'first verified charge279 witness'
            save()
            break
        case['status'] = 'INFEASIBLE_PROOF_REPLAY_PENDING'
        case['proof_nodes'] = nodes
        case['proof_root'] = proof_root
        replayed = verify_negative_proof(pool, critical, holes, nodes, proof_root)
        case['proof_nodes_replayed'] = replayed
        case['status'] = 'INFEASIBLE_EXHAUSTIVE_PROOF_REPLAY_PASS'
        if len(nodes) == 1:
            case['direct_unavailable_target'] = nodes[0].get('target')
        save()
    else:
        report['stop_reason'] = 'all24 sources completed'
except Stop as stop:
    report['stop_reason'] = str(stop)
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    save()
    print(json.dumps({'host': report['host'], 'stop_reason': report['stop_reason'],
                      'elapsed_seconds': report['elapsed_seconds'],
                      'witness_found': report['witness'] is not None,
                      'cases': [{key: case[key] for key in ('source_id', 'full_owner',
                                'short_owners', 'short_signs', 'status', 'candidate_count',
                                'candidates_by_anchor', 'dfs_nodes', 'direct_unavailable_target')
                                if key in case} for case in report['cases']]}, indent=2))
