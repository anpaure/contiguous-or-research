#!/usr/bin/env python3
"""Two prescribed exact cap-flow decisions. Execute only on h100."""
import hashlib
import json
import resource
import signal
import sys
import time
from collections import Counter, deque
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
signal.alarm(150)
sys.setrecursionlimit(100000)
started = time.monotonic()
INPUT = Path('/home/amodo/exact-b-k17-height-adaptive-20260908/height_adaptive_canonical_cycles.json')
OUT = Path('/home/amodo/exact-b-k17-capped-low-flows-20260908')
OUT.mkdir(parents=True, exist_ok=True)
raw = INPUT.read_bytes()
records = json.loads(raw)
FULL = (1 << 17) - 1
targets = [s for s in range(1, FULL + 1) if s.bit_count() <= 5]
assert len(targets) == 9401
banks = {}
positions = []
groups = {}

def or_all(values):
    a = 0
    for x in values:
        a |= x
    return a

for rec in records:
    cid, h, v = rec['cycle'], rec['height'], rec['length']
    H = min(h, 3)
    X = [FULL ^ a for a in rec['lower_owners']]
    assert v == len(X) and v % 2 == 1
    D = [FULL] * v
    for i in range(v):
        for j in range(H + 1):
            D[i] &= X[(i + j) % v]
        assert D[i].bit_count() == 9 - H
    pins = []
    for i in range(v):
        pin = (X[i] & ~X[(i - 1) % v]) | (X[(i + H) % v] & ~X[(i + H + 1) % v])
        assert pin and pin & D[i] == pin
        assert or_all(D[(i + j) % v] for j in range(H + 1)) == X[(i + H) % v]
        # Independent indispensable-coordinate definition, not merely the formula.
        deficit = 0
        for start in range(i - H, i + 1):
            others = or_all(D[j % v] for j in range(start, start + H + 1) if j % v != i)
            deficit |= X[(start + H) % v] & ~others
        assert deficit == pin
        pins.append(pin)
        if H == 3:
            pid = len(positions)
            frame = i % 2 == 0 and i <= v - 3
            positions.append((cid, i, D[i], pin, frame))
            groups.setdefault(D[i], []).append(pid)
    banks[cid] = (X, D, pins, H, h)
assert len(records) == 146 and sum(len(b[0]) for b in banks.values()) == 24310
assert len(positions) == 22134 and len(groups) == 12376
assert set(groups) == {s for s in range(1, FULL + 1) if s.bit_count() == 6}

class Dinic:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]
        self.to, self.cap, self.original = [], [], []
    def add(self, u, v, cap):
        e = len(self.to)
        self.to.extend((v, u)); self.cap.extend((cap, 0)); self.original.extend((cap, 0))
        self.adj[u].append(e); self.adj[v].append(e + 1)
        return e
    def reachable(self, source):
        seen = [False] * len(self.adj)
        seen[source] = True; todo = deque([source])
        while todo:
            u = todo.popleft()
            for e in self.adj[u]:
                v = self.to[e]
                if self.cap[e] and not seen[v]:
                    seen[v] = True; todo.append(v)
        return seen
    def solve(self, source, sink):
        total = 0
        while True:
            level = [-1] * len(self.adj); level[source] = 0; todo = deque([source])
            while todo:
                u = todo.popleft()
                for e in self.adj[u]:
                    v = self.to[e]
                    if self.cap[e] and level[v] < 0:
                        level[v] = level[u] + 1; todo.append(v)
            if level[sink] < 0:
                return total
            it = [0] * len(self.adj)
            def push(u, amount):
                if u == sink:
                    return amount
                while it[u] < len(self.adj[u]):
                    e = self.adj[u][it[u]]; v = self.to[e]
                    if self.cap[e] and level[v] == level[u] + 1:
                        sent = push(v, min(amount, self.cap[e]))
                        if sent:
                            self.cap[e] -= sent; self.cap[e ^ 1] += sent
                            return sent
                    it[u] += 1
                return 0
            while True:
                sent = push(source, len(targets))
                if not sent:
                    break
                total += sent

def literal_check(name, assignment):
    capped = {cid: list(b[1]) for cid, b in banks.items()}
    for s, pid in assignment.items():
        cid, i, D, pin, frame = positions[pid]
        assert pin & s == pin and s & D == s and 1 <= s.bit_count() <= 5
        capped[cid][i] = s
    pair_losses, owner_losses, triple_losses = [], [], []
    global_seen = bytearray(FULL + 1)
    witnesses = {}
    for cid, (X, D, pins, H, h) in banks.items():
        E = capped[cid]; v = len(E)
        for i in range(v):
            assert E[i] and E[i] & D[i] == E[i] and E[i] & pins[i] == pins[i]
            if (E[i] | E[(i + 1) % v]) != (D[i] | D[(i + 1) % v]):
                pair_losses.append([cid, i])
            if or_all(E[(i + j) % v] for j in range(H + 1)) != X[(i + H) % v]:
                owner_losses.append([cid, i])
            if H == 3 and or_all(E[(i + j) % v] for j in range(3)) != or_all(D[(i + j) % v] for j in range(3)):
                triple_losses.append([cid, i])
        # All cyclic intervals, with start in the first period and length <= v.
        suffix = {}
        for end in range(2 * v - 1):
            letter = E[end % v]
            new = {letter: end} if end < v else {}
            for old, start in suffix.items():
                if start < end - v + 1:
                    continue
                val = old | letter
                if start > new.get(val, -1):
                    new[val] = start
            assert len(new) <= 17
            suffix = new
            for val, start in suffix.items():
                if not global_seen[val]:
                    global_seen[val] = 1
                    witnesses[val] = [cid, start, end - start + 1]
    # Separate range-OR segment-tree replay of every retained global witness.
    trees = {}
    for cid, E in capped.items():
        doubled = E + E
        base = 1
        while base < len(doubled):
            base *= 2
        tree = [0] * (2 * base)
        tree[base:base + len(doubled)] = doubled
        for i in range(base - 1, 0, -1):
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        trees[cid] = (tree, base)
    for val, (cid, start, length) in witnesses.items():
        assert 0 <= start < len(capped[cid]) and 1 <= length <= len(capped[cid])
        tree, base = trees[cid]; l, rr = base + start, base + start + length; result = 0
        while l < rr:
            if l & 1: result |= tree[l]; l += 1
            if rr & 1: rr -= 1; result |= tree[rr]
            l //= 2; rr //= 2
        assert result == val
    missing = [s for s in range(1, FULL + 1) if not global_seen[s]]
    rank6_present = {s for E in capped.values() for s in E if s.bit_count() == 6}
    assert rank6_present == set(groups)
    assert all(global_seen[s] for s in targets)
    artifact = OUT / (name + '_capped_periodic_bank.json')
    artifact.write_text(json.dumps([dict(cycle=cid, height=banks[cid][4], H=banks[cid][3], letters=E) for cid, E in capped.items()]) + '\n')
    detail = dict(pair_loss_positions=pair_losses, rank8_triple_loss_positions=triple_losses,
                  middle_owner_loss_positions=owner_losses, missing_masks=missing)
    (OUT / (name + '_literal_check_details.json')).write_text(json.dumps(detail) + '\n')
    return dict(bank_file=str(artifact), bank_sha256=hashlib.sha256(artifact.read_bytes()).hexdigest(),
                period_positions=24310, pair_occurrences_changed=len(pair_losses), rank8_triples_changed=len(triple_losses),
                middle_owner_windows_changed=len(owner_losses), literal_rank6_targets_retained=len(rank6_present),
                covered_targets=len(witnesses), missing_targets=len(missing),
                missing_rank_counts=dict(sorted(Counter(s.bit_count() for s in missing).items())),
                independent_range_or_witnesses_replayed=len(witnesses),
                complete_cyclic_bank=not missing,
                all_prescribed_middle_windows_preserved=not owner_losses,
                all_native_pair_ors_preserved=not pair_losses,
                linear_word_claim=False)

def solve_instance(name, anchored):
    selected = [pid for pid, p in enumerate(positions) if not anchored or p[4]]
    selected_set = set(selected)
    capacities = {}
    group_records = []
    for label, members in sorted(groups.items()):
        editable = sum(pid in selected_set for pid in members)
        anchors = len(members) - editable
        cap = editable if anchors else editable - 1
        assert cap >= 0
        capacities[label] = cap
        group_records.append([label, len(members), editable, anchors, cap])
    capacity = sum(capacities.values())
    scalar = dict(name=name, targets=len(targets), editable_positions=len(selected), rank6_groups=len(groups),
                  total_group_capacity=capacity, capacity_minus_demand=capacity - len(targets),
                  groups_with_fixed_anchor=sum(row[3] > 0 for row in group_records),
                  eligibility='Pin_i subset S subset D_i; rank(S) in 1..5',
                  group_columns=['rank6_mask','all_occurrences','editable_occurrences','anchor_occurrences','capacity'])
    (OUT / (name + '_group_capacity_certificate.json')).write_text(json.dumps(group_records) + '\n')
    if anchored and capacity < len(targets):
        scalar.update(status='IMPOSSIBLE_BY_TOTAL_CAPACITY', flow_run=False,
                      flow_upper_bound=capacity, deficiency_at_least=len(targets)-capacity)
        print(json.dumps(scalar), flush=True)
        return scalar
    T0, P0 = 1, 1 + len(targets)
    G0 = P0 + len(selected); sink = G0 + len(groups)
    graph = Dinic(sink + 1)
    target_node = {s: T0 + j for j, s in enumerate(targets)}
    position_node = {pid: P0 + j for j, pid in enumerate(selected)}
    group_node = {label: G0 + j for j, label in enumerate(sorted(groups))}
    tedges = {s: [] for s in targets}
    for s in targets:
        graph.add(0, target_node[s], 1)
    for pid in selected:
        cid, i, D, pin, frame = positions[pid]
        free = D & ~pin; sub = free
        while True:
            s = pin | sub
            if s.bit_count() <= 5:
                edge = graph.add(target_node[s], position_node[pid], 1)
                tedges[s].append((pid, edge))
            if not sub: break
            sub = (sub - 1) & free
        graph.add(position_node[pid], group_node[D], 1)
    for label in sorted(groups):
        graph.add(group_node[label], sink, capacities[label])
    flow = graph.solve(0, sink)
    assignment = {}
    used = set(); group_used = Counter()
    for s in targets:
        occupied = [pid for pid, edge in tedges[s] if graph.cap[edge] == 0]
        assert len(occupied) <= 1
        if occupied:
            pid = occupied[0]
            assert pid not in used
            used.add(pid); assignment[s] = pid; group_used[positions[pid][2]] += 1
    assert len(assignment) == flow and all(group_used[g] <= capacities[g] for g in groups)
    assignment_rows = [[s, positions[pid][0], positions[pid][1], positions[pid][2], positions[pid][3]]
                       for s, pid in sorted(assignment.items())]
    (OUT / (name + '_assignment.json')).write_text(json.dumps(assignment_rows) + '\n')
    reach = graph.reachable(0)
    assert not reach[sink]
    cut_count = 0; cut_types = Counter()
    for u, adjacency in enumerate(graph.adj):
        if not reach[u]: continue
        for e in adjacency:
            if e % 2 == 0 and not reach[graph.to[e]]:
                cut_count += graph.original[e]
                if u == 0: kind = 'source_target'
                elif u < P0: kind = 'target_position'
                elif u < G0: kind = 'position_group'
                else: kind = 'group_sink'
                cut_types[kind] += graph.original[e]
    assert cut_count == flow
    hall_targets = [s for s in targets if reach[target_node[s]]]
    neighbors = {pid for s in hall_targets for pid, edge in tedges[s]}
    neighbor_by_group = Counter(positions[pid][2] for pid in neighbors)
    hall_capacity = sum(min(capacities[g], count) for g, count in neighbor_by_group.items())
    assert len(hall_targets) - hall_capacity == len(targets) - flow
    hall = dict(target_masks=hall_targets,
                neighbor_positions=[[positions[pid][0], positions[pid][1]] for pid in sorted(neighbors)],
                group_rows=[[g, neighbor_by_group[g], capacities[g], min(neighbor_by_group[g], capacities[g])]
                            for g in sorted(neighbor_by_group)],
                group_columns=['rank6_mask','neighbor_positions','group_capacity','usable_capacity'],
                target_count=len(hall_targets), neighbor_count=len(neighbors),
                available_capacity=hall_capacity, deficiency=len(hall_targets)-hall_capacity,
                minimum_cut_capacity=cut_count, minimum_cut_edge_capacity_by_type=dict(cut_types))
    (OUT / (name + '_hall_cut_certificate.json')).write_text(json.dumps(hall) + '\n')
    scalar.update(status='SATURATED_ASSIGNMENT' if flow == len(targets) else 'IMPOSSIBLE_BY_EXACT_MAX_FLOW',
                  flow_run=True, flow=flow, deficiency=len(targets)-flow,
                  eligibility_edges=sum(map(len, tedges.values())),
                  zero_host_targets=[s for s in targets if not tedges[s]],
                  hall_target_count=len(hall_targets), hall_neighbor_count=len(neighbors),
                  hall_capacity=hall_capacity, minimum_cut_capacity=cut_count,
                  assignment_columns=['target_mask','cycle','cyclic_position','original_rank6_mask','pin_mask'])
    if flow == len(targets):
        scalar['literal_check'] = literal_check(name, assignment)
        scalar['scope'] = ('Anchored assignment is sufficient for pair and all longer native OR preservation; literal bank independently checked.'
                           if anchored else 'Unrestricted flow is a necessary relaxation only. Its one selected cap assignment is independently checked; no other assignment search.')
    print(json.dumps(scalar), flush=True)
    return scalar

results = [solve_instance('unrestricted', False), solve_instance('canonical_alternating', True)]
report = dict(status='COMPLETED_TWO_PRESCRIBED_EXACT_DECISIONS',
              input_file=str(INPUT), input_sha256=hashlib.sha256(raw).hexdigest(),
              source_cycle_count=len(records), source_period_positions=24310,
              dimension=17, frozen_apertures=[1,2], editable_aperture=3,
              canonical_alternating_frame='For each stored odd H3 cycle of length v: indices 0,2,...,v-3. All others fixed.',
              no_additional_frames_or_assignment_search=True, results=results,
              resource_caps=dict(cpu_seconds=120,wall_seconds=150,address_space_bytes=2*1024**3),
              elapsed_seconds=time.monotonic()-started,
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT / 'two_flow_report.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'status':report['status'],'elapsed_seconds':report['elapsed_seconds']}),flush=True)
