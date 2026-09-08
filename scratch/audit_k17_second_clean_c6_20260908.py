#!/usr/bin/env python3
"""One analytically prescribed C6 after the mountain switch; h100 only."""
import argparse
import json
import resource
import signal
from collections import Counter
from itertools import combinations
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(110)

KDIM = 17
RANK = 8
FULL = (1 << KDIM) - 1
BAD_IDS = {115, 116, 118, 122, 129, 138}
PREFIX_PATH = Path('/home/amodo/exact-b-k17-badsix-all-ports-20260908/badsix_all_ports_306_owner_path.word')


def root(a):
    for u in range(KDIM):
        if a >> u & 1:
            continue
        height = 0
        for j in range(1, KDIM):
            height += 1 if a >> ((u + j) % KDIM) & 1 else -1
            if height < 0:
                break
        else:
            assert height == 0
            return u
    raise AssertionError(a)


def cycle_adjacency(cycles):
    adj = {}
    for cycle in cycles:
        for i, a in enumerate(cycle):
            adj[a] = {cycle[i-1], cycle[(i+1) % len(cycle)]}
    assert all(len(v) == 2 for v in adj.values())
    return adj


def components(adj):
    unseen = set(adj)
    answer = []
    while unseen:
        start = min(unseen)
        a, prev = start, None
        cycle = []
        while a in unseen:
            unseen.remove(a)
            cycle.append(a)
            ns = sorted(adj[a])
            nxt = ns[0] if prev is None or ns[0] != prev else ns[1]
            prev, a = a, nxt
        assert a == start
        answer.append(cycle)
    return answer


def switch(adj, old_edges, new_edges):
    for a, b in old_edges:
        assert b in adj[a] and a in adj[b], ('missing old edge', a, b)
        adj[a].remove(b)
        adj[b].remove(a)
    for a, b in new_edges:
        assert b not in adj[a] and a not in adj[b], ('existing new edge', a, b)
        adj[a].add(b)
        adj[b].add(a)
    assert all(len(v) == 2 for v in adj.values())


def topology():
    states = [sum(1 << b for b in bits) for bits in combinations(range(KDIM), RANK)]
    f = {a: FULL ^ a ^ (1 << root(a)) for a in states}
    assert len(set(f.values())) == len(states)
    g = {a: f[f[a]] for a in states}
    unseen = set(states)
    original = []
    while unseen:
        start = min(unseen)
        a = start
        cycle = []
        while a in unseen:
            unseen.remove(a)
            cycle.append(a)
            a = g[a]
        assert a == start
        original.append(cycle)
    assert len(original) == 146
    assert [len(original[i]) for i in (0, 1)] == [17, 221]
    mountain_adj = cycle_adjacency([original[0], original[1]])
    switch(mountain_adj, [(510, 255), (894, 383), (766, 639)],
           [(510, 383), (894, 639), (766, 255)])
    mountain = components(mountain_adj)
    assert sorted(map(len, mountain)) == [103, 135]
    current = {f'old_{i}': c for i, c in enumerate(original) if i not in (0, 1)}
    for c in mountain:
        current[f'mountain_{len(c)}'] = c
    ids = {a: cid for cid, cy in current.items() for a in cy}
    current_adj = cycle_adjacency(current.values())

    # August 5's explicit three-component connector, unrotated, m=8.
    core = (1 << 3) | sum(1 << j for j in range(12, 17))
    arms = [0, 1, 4]
    center = 11
    ps = [core | (1 << arms[i]) | (1 << arms[(i+1) % 3]) for i in range(3)]
    qs = [core | (1 << arms[i]) | (1 << center) for i in range(3)]
    old_edges = [[ps[i], qs[i]] for i in range(3)]
    new_edges = [[ps[i], qs[(i+1) % 3]] for i in range(3)]
    affected = sorted({ids[a] for edge in old_edges for a in edge})
    old_memberships = [b in current_adj[a] for a, b in old_edges]
    bad_nodes = {a for i in BAD_IDS for a in original[i]}
    assert len(bad_nodes) == 306
    disjoint_prefix = not (set(ps + qs) & bad_nodes)
    assert all(old_memberships)
    assert len(affected) == 3 and any(cid.startswith('mountain_') for cid in affected)
    assert disjoint_prefix
    assert all(not (set(current[cid]) & bad_nodes) for cid in affected)
    prefix = [int(s) for s in PREFIX_PATH.read_text().split()]
    assert len(prefix) == len(set(prefix)) == 306
    assert {FULL ^ a for a in prefix} == bad_nodes
    affected_adj = cycle_adjacency([current[cid] for cid in affected])
    switch(affected_adj, old_edges, new_edges)
    merged = components(affected_adj)
    assert len(merged) == 1
    report = dict(k=KDIM, candidate_count=1,
                  template='MATH_THEOREM_PBBS_EXPLICIT_THREE_COMPONENT_Q2_NEUTRAL_C6_20260805.md',
                  core=core, arms=arms, center=center,
                  old_edges=old_edges, new_edges=new_edges,
                  old_edge_memberships=old_memberships,
                  affected_component_ids=affected,
                  affected_lengths=[len(current[c]) for c in affected],
                  new_lengths=list(map(len, merged)),
                  prefix_untouched=disjoint_prefix,
                  bad_ids=sorted(BAD_IDS), prefix_owners=prefix,
                  current_lower_cycles=current,
                  new_lower_cycles=merged,
                  resource_caps=dict(cpu_seconds=90, wall_seconds=110, address_space_bytes=1024**3))
    Path('second_c6_topology.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('candidate_count', 'old_edges', 'new_edges',
          'old_edge_memberships', 'affected_component_ids', 'affected_lengths', 'new_lengths',
          'prefix_untouched', 'resource_caps')}, indent=2))
    print('PASS: specified old edges exist; three GOOD components merge to one; prefix untouched.')


def upper(cycle_or_path, cyclic, label):
    owners = cycle_or_path
    n = len(owners)
    witness = {}
    for start in range(n):
        acc = owners[start]
        stop = n if cyclic else n-start
        for width in range(2, stop+1):
            previous = acc
            acc |= owners[(start+width-1) % n]
            if acc == FULL:
                break
            if acc != previous and acc.bit_count() >= 10:
                witness.setdefault(acc, dict(component=label, start=start, width=width, cyclic=cyclic))
    return witness


def palette(cycles):
    return Counter((FULL ^ cy[i]) & (FULL ^ cy[(i+1) % len(cy)])
                   for cy in cycles for i in range(len(cy)))


def runs(cycle):
    owners = [FULL ^ a for a in cycle]
    n = len(owners)
    histogram = Counter()
    short = []
    constant = []
    for x in range(KDIM):
        if all(a >> x & 1 for a in owners):
            histogram[n] += 1
            constant.append(x)
            continue
        for start in range(n):
            if not owners[start] >> x & 1 or owners[start-1] >> x & 1:
                continue
            length = 1
            while owners[(start+length) % n] >> x & 1:
                length += 1
                assert length < n
            histogram[length] += 1
            if length < 4:
                short.append(dict(coordinate=x, start=start, length=length))
    return dict(sorted(histogram.items())), short, constant


def audit():
    state = json.loads(Path('second_c6_topology.json').read_text())
    current = state['current_lower_cycles']
    affected = state['affected_component_ids']
    banned = {f'old_{i}' for i in state['bad_ids']}
    old_witness = {}
    for cid in affected:
        old_witness.update(upper([FULL ^ a for a in current[cid]], True, cid))
    new_witness = upper([FULL ^ a for a in state['new_lower_cycles'][0]], True, 'merged')
    outside = upper(state['prefix_owners'], False, 'actual_306_prefix')
    for cid, cy in current.items():
        if cid not in affected and cid not in banned:
            outside.update(upper([FULL ^ a for a in cy], True, cid))
    old_global = set(old_witness) | set(outside)
    new_global = set(new_witness) | set(outside)
    assert len(old_global) == 41225
    local_lost = set(old_witness) - set(new_witness)
    local_gained = set(new_witness) - set(old_witness)
    global_lost = old_global - new_global
    old_palette = palette([current[cid] for cid in affected])
    new_palette = palette(state['new_lower_cycles'])
    assert old_palette == new_palette
    hist, short, constant = runs(state['new_lower_cycles'][0])
    preserved = (set(old_witness) & set(new_witness))
    rec = dict(topology_file='second_c6_topology.json',
               affected_component_ids=affected,
               affected_lengths=state['affected_lengths'],
               new_lengths=state['new_lengths'],
               local_upper_lost=sorted(local_lost),
               local_upper_gained=sorted(local_gained),
               global_upper_lost=sorted(global_lost),
               global_upper_support_before=len(old_global),
               global_upper_support_after=len(new_global),
               old_upper_rank_counts=dict(sorted(Counter(a.bit_count() for a in old_witness).items())),
               new_upper_rank_counts=dict(sorted(Counter(a.bit_count() for a in new_witness).items())),
               local_upper_transport={str(a): dict(old=old_witness[a], new=new_witness[a])
                                      for a in sorted(preserved)},
               old_local_lost_witnesses={str(a): old_witness[a] for a in sorted(local_lost)},
               outside_backup_for_local_losses={str(a): outside[a] for a in sorted(local_lost) if a in outside},
               lower_rank8_pair_multiset_preserved=True,
               positive_run_histogram=hist,
               short_positive_runs=short,
               constant_positive_coordinates=constant,
               new_lower_cycle=state['new_lower_cycles'][0],
               prefix_untouched=state['prefix_untouched'],
               all_requested_gates_passed=not global_lost and not short)
    Path('second_c6_audit.json').write_text(json.dumps(rec, indent=2) + '\n')
    print(json.dumps({k: rec[k] for k in ('affected_component_ids', 'affected_lengths', 'new_lengths',
          'global_upper_lost', 'global_upper_support_before', 'global_upper_support_after',
          'lower_rank8_pair_multiset_preserved', 'positive_run_histogram', 'short_positive_runs',
          'prefix_untouched', 'all_requested_gates_passed')}, indent=2))
    print('local lost/gained counts', len(local_lost), len(local_gained))
    print('outside-backed local losses', len(rec['outside_backup_for_local_losses']))
    print('PASS' if rec['all_requested_gates_passed'] else 'FAIL', 'specified second clean-C6 gates')


def source():
    rec = json.loads(Path('second_c6_audit.json').read_text())
    assert rec['all_requested_gates_passed']
    owners = [FULL ^ a for a in rec['new_lower_cycle']]
    n = len(owners)
    envelope = []
    for p in range(n):
        mask = FULL
        for j in range(4):
            mask &= owners[(p-j) % n]
        assert mask
        envelope.append(mask)
    for i in range(n):
        owner = 0
        for j in range(4):
            owner |= envelope[(i+j) % n]
        assert owner == owners[i]
        face = 0
        for j in range(3):
            face |= envelope[(i+j) % n]
        assert face == owners[i-1] & owners[i]
    Path('merged_475_upper_owner_cycle.word').write_text('\n'.join(map(str, owners)) + '\n')
    Path('merged_475_depth3_source_cycle.word').write_text('\n'.join(map(str, envelope)) + '\n')
    rec['source_certificate'] = dict(
        period=n, source_depth=3,
        owner_file='merged_475_upper_owner_cycle.word',
        source_file='merged_475_depth3_source_cycle.word',
        minimum_source_letter_rank=min(map(int.bit_count, envelope)),
        all_owner_four_windows_verified=True,
        all_rank8_three_windows_verified=True,
        scope='cyclic component source, not a universal full-cube word')
    Path('second_c6_audit.json').write_text(json.dumps(rec, indent=2) + '\n')
    print(json.dumps(rec['source_certificate'], indent=2))
    print('local lost target backup', json.dumps(rec['outside_backup_for_local_losses'], indent=2))
    print('PASS: literal 475-letter depth-three cyclic source and all owners/facets verified.')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('phase', choices=['topology', 'audit', 'source'])
    args = ap.parse_args()
    {'topology': topology, 'audit': audit, 'source': source}[args.phase]()
