#!/usr/bin/env python3
"""Reviewed fixed-family diagnostic, not an OR-word construction search.

Individually revert exactly the1,216 recorded three-circuits of the pinned
literal19 incoming matching. No candidate is based on another candidate.
Save the outcome of every candidate. Fully replay only the first candidate
that is Hamiltonian, satisfies both residence exclusions, and loses a
rank11 upper-interval target. If none exists, that is only this family's
outcome, not a theorem of automatic upper support.
"""
import hashlib
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path

K = 19
FULL = (1 << K) - 1
M = 92378
BASE = Path('/home/amodo/exact-b-k19-k20-optimal-20260909')
STRUCTURE = BASE / 'literal19_structure'
OUT = Path('/home/amodo/exact-b-k19-phi-upper-three-circuit-diagnostic-20260909')
INPUTS = {
    'word': (BASE / 'k19_optimal92381.word',
             '1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414'),
    'canonical': (Path('/home/amodo/exact-b-k19-height-adaptive-20260908/height_adaptive_canonical_cycles.json'),
                  '5e44113db3152b216af7761766f69a7b389db54b5c1f5dce9ac227ba6e6e71cd'),
    'circuits': (STRUCTURE / 'incoming_matching_alternating_circuits.json',
                 '3006706c5a0072b0e60386f7754008b4327b87f7cd53a09a74e84cb4859bd629'),
    'report': (STRUCTURE / 'literal19_structural_reconstruction_certificate.json',
               '68c2187cd9ec3d7ccf14c35588265e32fb96daacafe48e63d1325b3f2e02c566'),
}


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def phi(lower):
    level = minimum = 0
    root = None
    for coordinate in range(K):
        level += 1 if lower & (1 << coordinate) else -1
        if level < minimum:
            minimum = level
            root = coordinate
    assert level == -1 and root is not None
    assert not lower & (1 << root)
    return lower | (1 << root)


def single_bit(value):
    return value > 0 and value & (value - 1) == 0


def component_count_at_cuts(heads, successors):
    """Exact topology on the three unchanged arcs between the cut heads."""
    ordered = sorted(heads)
    head_index = {head: index for index, head in enumerate(ordered)}
    block_next = []
    for index in range(3):
        tail = (ordered[(index + 1) % 3] - 1) % M
        block_next.append(head_index[successors[tail]])
    assert sorted(block_next) == [0, 1, 2]
    seen = set()
    count = 0
    for start in range(3):
        if start in seen:
            continue
        count += 1
        current = start
        while current not in seen:
            seen.add(current)
            current = block_next[current]
        assert current == start
    return count, block_next


def full_replay(selected, lower, upper, native_incoming):
    """Full materialized replay, independent of the local screening tests."""
    modifications = {int(tail): int(head) for tail, head in selected['new_successor_edges']}
    successor = [(i + 1) % M for i in range(M)]
    for tail, head in modifications.items():
        successor[tail] = head
    assert sorted(successor) == list(range(M))
    order = []
    visited = set()
    current = 0
    for _ in range(M):
        assert current not in visited
        visited.add(current)
        order.append(current)
        current = successor[current]
    assert current == 0 and len(visited) == M
    L = [lower[index] for index in order]
    U = [phi(value) for value in L]
    assert U == [upper[index] for index in order]
    assert len(set(L)) == M and len(set(U)) == M
    assert all(value.bit_count() == 9 for value in L)
    assert all(value.bit_count() == 10 for value in U)

    additions = []
    deletions = []
    changed_incoming = []
    for i in range(M):
        following = L[(i + 1) % M]
        assert L[i] | following == U[i]
        assert U[(i - 1) % M] & U[i] == L[i]
        additions.append(following & ~L[i])
        deletions.append(L[i] & ~following)
        old_position = order[i]
        if U[(i - 1) % M] != upper[(old_position - 1) % M]:
            changed_incoming.append(L[i])
            assert U[(i - 1) % M] == native_incoming[L[i]]
    assert sorted(changed_incoming) == sorted(selected['lower_circuit'])
    assert len(changed_incoming) == 3
    assert all(single_bit(a) and single_bit(d) for a, d in zip(additions, deletions))
    assert all(additions[i] != deletions[(i + 1) % M] and
               additions[i] != deletions[(i + 2) % M] for i in range(M))

    colors = Counter(U[i] | U[(i + 1) % M] for i in range(M))
    assert all(value.bit_count() == 11 for value in colors)
    target = selected['lost_rank11_targets'][0]
    assert target.bit_count() == 11 and colors[target] == 0
    # Excludes EVERY longer cyclic interval, not just the pair row:
    # a union equal to target can use only upper letters contained in target.
    # There are exactly11 such rank10 letters, and every one is isolated.
    # A length1 interval has rank10, while length>=2 would contain a pair
    # of consecutive contained letters. Hence no interval represents target.
    contained = [i for i, value in enumerate(U) if value & ~target == 0]
    assert len(contained) == 11
    contained_set = set(contained)
    assert all((i + 1) % M not in contained_set for i in contained)
    absence = [dict(position=i, upper=U[i],
                    preceding_outside_bit=U[(i - 1) % M] & ~target,
                    following_outside_bit=U[(i + 1) % M] & ~target)
               for i in contained]
    assert all(row['preceding_outside_bit'] and row['following_outside_bit']
               for row in absence)
    files = {}
    for name, values in (('counterexample_lower_cycle.word', L),
                         ('counterexample_upper_cycle.word', U)):
        raw = ('\n'.join(map(str, values)) + '\n').encode('ascii')
        (OUT / name).write_bytes(raw)
        files[name] = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    replay = dict(status='PASS_COUNTEREXAMPLE_FULL_REPLAY',
                  period=M, rank9_states=M, rank10_states=M,
                  every_outgoing_edge_is_canonical_phi=True,
                  both_residence_exclusions_at_every_position=True,
                  one_hamilton_cycle=True, changed_incoming_labels=changed_incoming,
                  missing_rank11_target=target,
                  missing_rank11_coordinates_one_based=[c+1 for c in range(K) if target & (1 << c)],
                  rank11_pair_colors=len(colors),
                  ordinary_and_cyclic_upper_interval_absence=True,
                  all_contained_rank10_positions=absence, files=files)
    save('counterexample_full_replay.json', replay)
    return replay


def run():
    pinned = {}
    data = {}
    for name, (path, expected) in INPUTS.items():
        raw = path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        assert sha == expected, (name, sha)
        pinned[name] = dict(path=str(path), sha256=sha, bytes=len(raw))
        data[name] = raw
    report = json.loads(data['report'])
    assert report['status'] == 'PASS_LITERAL19_STRUCTURAL_RECONSTRUCTION'
    assert report['word19_sha256'] == INPUTS['word'][1]
    assert report['canonical_sha256'] == INPUTS['canonical'][1]
    word = [int(value) for value in data['word'].split()]
    assert len(word) == M + 3 and all(0 < value <= FULL for value in word)
    core = word[:M]
    assert word == core + core[:3]
    lower = [word[i] | word[i+1] | word[i+2] for i in range(M)]
    upper = [lower[i] | word[i+3] for i in range(M)]
    assert all(value.bit_count() == 9 for value in lower) and len(set(lower)) == M
    assert all(value.bit_count() == 10 for value in upper) and len(set(upper)) == M
    assert M == math.comb(K, 9) == math.comb(K, 10)
    assert all(phi(lower[i]) == upper[i] for i in range(M))
    position = {value: i for i, value in enumerate(lower)}
    upper_position = {value: i for i, value in enumerate(upper)}
    added = [lower[(i+1) % M] & ~lower[i] for i in range(M)]
    deleted = [lower[i] & ~lower[(i+1) % M] for i in range(M)]
    assert all(single_bit(a) and single_bit(d) for a, d in zip(added, deleted))
    assert all(lower[i] | lower[(i+1) % M] == upper[i] for i in range(M))
    assert all(added[i] != deleted[(i+1) % M] and
               added[i] != deleted[(i+2) % M] for i in range(M))
    colors = Counter(upper[i] | upper[(i+1) % M] for i in range(M))
    assert all(value.bit_count() == 11 for value in colors)
    assert len(colors) == math.comb(K, 11)

    native_incoming = {}
    for cycle in json.loads(data['canonical']):
        owners = cycle['lower_owners']
        assert len(owners) == cycle['length']
        assert all(value.bit_count() == 9 for value in owners)
        native_upper = [FULL ^ value for value in owners]
        for j, incoming in enumerate(native_upper):
            outgoing = native_upper[(j+1) % len(native_upper)]
            value = incoming & outgoing
            assert value.bit_count() == 9 and value not in native_incoming
            assert phi(value) == outgoing and incoming != outgoing
            native_incoming[value] = incoming
    assert set(native_incoming) == set(position)
    assert len(set(native_incoming.values())) == M

    raw_circuits = json.loads(data['circuits'])
    family = sorted([(index, row) for index, row in enumerate(raw_circuits)
                     if len(row['lower_cycle']) == 3],
                    key=lambda item: tuple(item[1]['lower_cycle']))
    assert len(family) == 1216
    used_labels = set()
    outcomes = []
    first_selected = None
    totals = Counter()
    for family_index, (source_index, row) in enumerate(family):
        labels = row['lower_cycle']
        assert len(set(labels)) == 3 and not (used_labels & set(labels))
        used_labels.update(labels)
        heads = [position[value] for value in labels]
        old = [native_incoming[value] for value in labels]
        actual = [upper[(index-1) % M] for index in heads]
        assert old == row['old_incoming'] and actual == row['new_incoming']
        assert actual == old[1:] + old[:1]
        successors = {upper_position[native_incoming[value]]: position[value]
                      for value in labels}
        assert len(successors) == 3
        assert set(successors) == {(head-1) % M for head in heads}
        assert set(successors.values()) == set(heads)
        assert all(tail != head and (tail+1) % M != head for tail, head in successors.items())
        assert all(lower[tail] | lower[head] == upper[tail]
                   for tail, head in successors.items())
        predecessors = {head: tail for tail, head in successors.items()}

        def nxt(index):
            return successors.get(index, (index+1) % M)

        def prev(index):
            return predecessors.get(index, (index-1) % M)

        # A newly failing three-edge residence test must touch a changed
        # tail. Its start is within two NEW predecessors of such a tail.
        # The old predecessors are included too as harmless redundancy.
        affected = set(successors)
        for tail in successors:
            affected.update((prev(tail), prev(prev(tail)),
                             (tail-1) % M, (tail-2) % M))
        bad = []
        for start in sorted(affected):
            v, w = nxt(start), nxt(nxt(start))
            x = nxt(w)
            insertion = lower[v] & ~lower[start]
            deletion1 = lower[v] & ~lower[w]
            deletion2 = lower[w] & ~lower[x]
            assert single_bit(insertion) and single_bit(deletion1) and single_bit(deletion2)
            if insertion == deletion1 or insertion == deletion2:
                bad.append(dict(start=start, insertion=insertion,
                                deletion1=deletion1, deletion2=deletion2))
        components, block_next = component_count_at_cuts(heads, successors)
        old_colors = Counter(upper[tail] | upper[(tail+1) % M] for tail in successors)
        new_colors = Counter(upper[tail] | upper[head] for tail, head in successors.items())
        assert all(target.bit_count() == 11 for target in new_colors)
        lost = sorted(target for target in old_colors
                      if colors[target] - old_colors[target] + new_colors[target] == 0)
        qualifies = components == 1 and not bad and bool(lost)
        result = dict(family_index=family_index, source_circuit_index=source_index,
                      lower_circuit=labels, original_positions=heads,
                      new_successor_edges=sorted(successors.items()),
                      abstract_block_successor=block_next, component_count=components,
                      residence_violations=bad, affected_guard_starts=sorted(affected),
                      old_rank11_colors=sorted(old_colors.items()),
                      new_rank11_colors=sorted(new_colors.items()),
                      lost_rank11_targets=lost, qualifies_as_counterexample=qualifies)
        outcomes.append(result)
        totals['candidates'] += 1
        totals['hamilton'] += components == 1
        totals['residence'] += not bad
        totals['hamilton_and_residence'] += components == 1 and not bad
        totals['counterexamples'] += qualifies
        if qualifies and first_selected is None:
            first_selected = result

    assert totals['candidates'] == 1216 and len(used_labels) == 3*1216
    save('all_1216_candidate_outcomes.json', outcomes)
    replay = (full_replay(first_selected, lower, upper, native_incoming)
              if first_selected is not None else None)
    result = dict(status=('COUNTEREXAMPLE_FULLY_REPLAYED' if replay is not None
                          else 'NO_COUNTEREXAMPLE_IN_THIS_FIXED_FAMILY'),
                  scope='Only the1216 recorded disjoint incoming three-circuits, each reverted independently on the original supplied19 carrier. No subsequent variant or search.',
                  inputs=pinned, baseline_period=M,
                  baseline_rank11_palette_size=len(colors),
                  baseline_rank11_palette_complete=True,
                  family_counts=dict(totals), first_selected=first_selected,
                  full_replay=replay,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return result


def main():
    assert socket.gethostname().split('.')[0] == 'arboghast'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256*1024**2, 256*1024**2))
    signal.alarm(90)
    wall_begin = time.monotonic()
    cpu_begin = time.process_time()
    OUT.mkdir(exist_ok=False)
    save('run_started.json', dict(status='RUNNING_NOT_CERTIFIED', hostname=socket.gethostname()))
    try:
        result = run()
    except MemoryError:
        save('incomplete.json', dict(status='INCONCLUSIVE_MEMORY_LIMIT'))
        raise
    except Exception as error:
        save('incomplete.json', dict(status='ERROR_NOT_CERTIFIED', error=repr(error)))
        raise
    result.update(resource_caps=dict(cpu_seconds=60, wall_seconds=90,
                                     address_space_bytes=2*1024**3,
                                     maximum_file_bytes=256*1024**2),
                  elapsed_cpu_seconds=time.process_time()-cpu_begin,
                  elapsed_wall_seconds=time.monotonic()-wall_begin)
    save('complete_diagnostic_certificate.json', result)
    print(json.dumps(dict(status=result['status'], counts=result['family_counts'],
                          first_missing_target=(result['full_replay']['missing_rank11_target']
                                                if result['full_replay'] else None),
                          cpu_seconds=result['elapsed_cpu_seconds'],
                          wall_seconds=result['elapsed_wall_seconds'])), flush=True)


if __name__ == '__main__':
    main()
