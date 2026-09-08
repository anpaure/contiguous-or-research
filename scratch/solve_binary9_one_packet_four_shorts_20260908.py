"""Authorized 30-second h100-only local trade test; no new catalogue."""
import collections
import json
import os
import pathlib
import resource
import socket
import sys
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (3 * 1024**3, 3 * 1024**3))
started = time.monotonic()
from ortools.sat.python import cp_model

data = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = pathlib.Path(sys.argv[2])
report = {'host': socket.gethostname(), 'cases': [], 'witness': None,
          'scope': 'One full fixed-left packet plus four shorts replaced by five full rows; all512 targets.'}

def save():
    report['elapsed_seconds'] = time.monotonic() - started
    temporary = out.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    temporary.replace(out)

def prefixes(order):
    masks = [0]
    for bit in order:
        masks.append(masks[-1] | 1 << bit)
    return masks

def target_set(order):
    cp, dp = prefixes(order[:4]), prefixes(order[4:])
    return {c | d for c in cp for d in dp}

def literal_witness(full_owner, chosen_shorts, orders):
    """Reconstruct actual remaining macrorectangles, then replay independently."""
    rectangles = []
    for row_id, (left, right) in enumerate(data['base_rows']):
        if row_id == full_owner:
            continue
        li, ri = list(map(int, left)), list(map(int, right))
        cp, dp = prefixes(li), prefixes(ri)
        sign = chosen_shorts.get(row_id, 0)
        if sign == 0:
            long_chain = [0] + [c | 256 for c in cp]
            short_chain = cp[1:]
        else:
            long_chain = cp + [cp[-1] | 256]
            short_chain = [c | 256 for c in cp[:-1]]
        rectangles.append({'source': ['old_long', row_id, sign],
                           'left_support': li + [8], 'right_support': ri,
                           'left_chain': long_chain, 'right_chain': dp})
        if row_id not in chosen_shorts:
            rectangles.append({'source': ['old_short', row_id, sign],
                               'left_support': li + [8], 'right_support': ri,
                               'left_chain': short_chain, 'right_chain': dp})
    for order in orders:
        order = list(map(int, order))
        rectangles.append({'source': ['new_full'],
                           'left_support': order[:4], 'right_support': order[4:],
                           'left_chain': prefixes(order[:4]),
                           'right_chain': prefixes(order[4:])})
    loads = [0] * 512
    cost = 0
    for rectangle in rectangles:
        assert sorted(rectangle['left_support'] + rectangle['right_support']) == list(range(9))
        for side in ('left', 'right'):
            support = sum(1 << b for b in rectangle[side + '_support'])
            chain = rectangle[side + '_chain']
            assert chain and all(not x & ~support for x in chain)
            assert all(a != b and not a & ~b for a, b in zip(chain, chain[1:]))
        cost += len(rectangle['left_chain']) + len(rectangle['right_chain'])
        for c in rectangle['left_chain']:
            for d in rectangle['right_chain']:
                loads[c | d] += 1
    assert len(rectangles) == 27 and cost == 279
    assert all(loads)
    assert all(loads[x] == 1 for x in range(512) if x.bit_count() in (4, 5))
    return {'full_owner': full_owner, 'removed_shorts': sorted(chosen_shorts.items()),
            'new_full_orders': orders, 'rectangles': rectangles,
            'principal_cost': cost, 'loads_all512': loads,
            'literal_verification': 'PASS: complementary supports, strict chains, all512 coverage, exact critical decks'}

groups = collections.defaultdict(list)
for candidate in data['candidates']:
    groups[candidate['full_owner']].append(candidate)
base_load = [0] * 512
for packet in data['packets']:
    for target in packet['full_targets']:
        base_load[target] += 1
assert all(base_load)
save()

owner_sequence = [int(sys.argv[3])] if len(sys.argv) > 3 else range(14)
per_case_seconds = float(sys.argv[4]) if len(sys.argv) > 4 else 1.25
for full_owner in owner_sequence:
    elapsed = time.monotonic() - started
    if elapsed >= 27:
        report['cases'].extend({'full_owner': j, 'status': 'NOT_RUN_GLOBAL_TIME_LIMIT'}
                               for j in range(full_owner, 14))
        break
    case_start = time.monotonic()
    rows = groups[full_owner]
    model = cp_model.CpModel()
    xx = [model.NewBoolVar('x' + str(k)) for k in range(len(rows))]
    yy = {(j, sign): model.NewBoolVar(f'y{j}_{sign}')
          for j in range(14) if j != full_owner for sign in (0, 1)}
    model.Add(sum(xx) == 5)
    model.Add(sum(yy.values()) == 4)
    for j in range(14):
        if j != full_owner:
            model.Add(yy[j, 0] + yy[j, 1] <= 1)
    positive = [[] for _ in range(512)]
    negative = [[] for _ in range(512)]
    for variable, row in zip(xx, rows):
        order = list(map(int, row['order']))
        targets = target_set(order)
        assert len(targets) == 30
        assert set(row['critical_targets']) == {v for v in targets if v.bit_count() in (4, 5)}
        for target in targets:
            positive[target].append(variable)
        for j, sign in row['required_shorts']:
            model.Add(variable <= yy[j, sign])
    for (j, sign), variable in yy.items():
        for target in data['shorts'][j]['full_targets_by_z'][sign]:
            negative[target].append(variable)
    removed_packet = set(data['packets'][full_owner]['full_targets'])
    for target in range(512):
        rhs = 1 - base_load[target] + int(target in removed_packet)
        expression = sum(positive[target]) - sum(negative[target])
        if target.bit_count() in (4, 5):
            model.Add(expression == rhs)
        else:
            model.Add(expression >= rhs)
    remaining = 28 - (time.monotonic() - started)
    if remaining <= 0.05:
        report['cases'].append({'full_owner': full_owner, 'status': 'MODEL_BUILT_NO_SOLVE_TIME'})
        report['cases'].extend({'full_owner': j, 'status': 'NOT_RUN_GLOBAL_TIME_LIMIT'}
                               for j in range(full_owner + 1, 14))
        break
    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 2
    solver.parameters.max_memory_in_mb = 2800
    solver.parameters.max_time_in_seconds = min(per_case_seconds, remaining)
    status = solver.Solve(model)
    record = {'full_owner': full_owner, 'candidate_rows': len(rows),
              'status': solver.StatusName(status), 'solver_wall_seconds': solver.WallTime(),
              'case_elapsed_seconds': time.monotonic() - case_start,
              'branches': solver.NumBranches(), 'conflicts': solver.NumConflicts()}
    report['cases'].append(record)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        selected = [rows[k]['order'] for k, variable in enumerate(xx) if solver.Value(variable)]
        chosen = {j: sign for (j, sign), variable in yy.items() if solver.Value(variable)}
        assert len(selected) == 5 and len(chosen) == 4
        report['witness'] = literal_witness(full_owner, chosen, selected)
        report['stopped_on_first_verified_witness'] = True
        save()
        break
    save()
save()
print(json.dumps({'elapsed_seconds': report['elapsed_seconds'], 'cases': report['cases'],
                  'witness_found': report['witness'] is not None}, indent=2))
