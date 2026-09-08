#!/usr/bin/env python3
"""One exact finite k18 seam gate; mathematical execution is h100-only.

Family: five four-letter end trims of the fixed optimal17 word, either
orientation; left word A or reverse(A), pair-preserving terminal caps with
a literal duplicate backup, then an arbitrary relative coordinate permutation.
No cut optimization, solver, randomization, or iterative deletion is used.
"""
import hashlib
import itertools
import json
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
signal.alarm(90)
STARTED = time.monotonic()
SOURCE = Path('/home/amodo/k17_optimal24313_forward_input.word')
OUT = Path('/home/amodo/exact-b-k18-four-end-cuts-one-seam-20260908')
OUT.mkdir(exist_ok=False)
EXPECTED_SHA = '7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
FULL = (1 << 17) - 1
Z = 1 << 17
REPORT_PATH = OUT / 'one_seam_relative_relabeling_decision.json'


def bits(mask):
    return [i for i in range(17) if mask & (1 << i)]


def ranks(values):
    return dict(sorted(Counter(x.bit_count() for x in values).items()))


def forward_coverage(word):
    """Ordinary intervals only; once FULL is hit, longer intervals add nothing."""
    covered = bytearray(FULL + 1)
    scanned = 0
    for left in range(len(word)):
        value = 0
        for right in range(left, len(word)):
            value |= word[right]
            covered[value] = 1
            scanned += 1
            if value == FULL:
                break
    return covered, scanned


def recency_blocks(word):
    seen = 0
    blocks = []
    for value in reversed(word):
        new = value & ~seen
        if new:
            blocks.append(new)
            seen |= new
            if seen == FULL:
                break
    assert seen == FULL
    return blocks


def graph_for(tail, defects):
    successor = [0] * 17
    predecessor = [0] * 17
    arc_defect = {}
    rows = []
    for target in defects:
        prefix_union = 0
        prefix_length = 0
        for letter in tail:
            if letter & ~target:
                break
            prefix_union |= letter
            prefix_length += 1
        required = target & ~prefix_union
        # A nonempty defect cannot already be an internal prefix union.
        assert required
        excluded = FULL ^ target
        for x in bits(required):
            successor[x] |= excluded
            for y in bits(excluded):
                predecessor[y] |= 1 << x
                arc_defect.setdefault((x, y), target)
        rows.append(dict(target=target, rank=target.bit_count(),
                         maximal_compatible_prefix_length=prefix_length,
                         maximal_compatible_prefix_union=prefix_union,
                         required_suffix_coordinates=required))
    return successor, predecessor, arc_defect, rows


def directed_cycle(successor):
    color = [0] * 17
    stack = []
    found = None

    def visit(v):
        nonlocal found
        color[v] = 1
        stack.append(v)
        for w in bits(successor[v]):
            if color[w] == 0:
                if visit(w):
                    return True
            elif color[w] == 1:
                found = stack[stack.index(w):] + [w]
                return True
        stack.pop()
        color[v] = 2
        return False

    for v in range(17):
        if not color[v] and visit(v):
            return found
    return None


def minima(predecessor, remaining):
    return [v for v in bits(remaining) if not predecessor[v] & remaining]


def check_blocks(successor, blocks):
    assert sum(x.bit_count() for x in blocks) == 17
    assert sum(blocks) == FULL
    owner = {}
    for j, block in enumerate(blocks):
        for x in bits(block):
            assert x not in owner
            owner[x] = j
    return all(owner[x] < owner[y]
               for x in range(17) for y in bits(successor[x]))


def decide_profile(successor, predecessor, profile):
    """Complete for two nonsingleton blocks followed by singleton blocks.

    Enumerate the first block. Once the second block is chosen from current
    minima, ANY such choice leaves a DAG, whose singleton remainder can always
    be topologically sorted. Thus only its available count matters.
    """
    first_size, second_size = profile[:2]
    assert tuple(profile[2:]) == (1,) * 10 and first_size + second_size == 7
    first_minima = minima(predecessor, FULL)
    tested = []
    result = dict(profile=list(profile), initial_minimal_vertices=first_minima,
                  required_first_size=first_size,
                  required_second_size=second_size)
    for selection in itertools.combinations(first_minima, first_size):
        first = sum(1 << v for v in selection)
        remaining = FULL ^ first
        second_minima = minima(predecessor, remaining)
        tested.append(dict(first_block=first, second_minimal_vertices=second_minima))
        if len(second_minima) < second_size:
            continue
        second = sum(1 << v for v in second_minima[:second_size])
        blocks = [first, second]
        remaining ^= second
        while remaining:
            available = minima(predecessor, remaining)
            assert available  # caller already excluded every directed cycle
            block = 1 << available[0]
            blocks.append(block)
            remaining ^= block
        assert tuple(x.bit_count() for x in blocks) == tuple(profile)
        assert check_blocks(successor, blocks)
        result.update(status='FEASIBLE', target_blocks=blocks,
                      first_blocks_tested=len(tested), first_block_trials=tested)
        return result
    result.update(status='INFEASIBLE_PROFILE', first_blocks_tested=len(tested),
                  first_block_trials=tested)
    return result


def suffix_witnesses_and_independent_replay(word, full):
    """O(kN) suffix census, then independently query every stored interval."""
    previous = {}
    witnesses = {}
    endpoint_states = 0
    for right, letter in enumerate(word):
        current = {letter: right}
        for old, left in previous.items():
            current.setdefault(old | letter, left)
        assert len(current) <= 18
        for target, left in current.items():
            witnesses.setdefault(target, (left, right))
        endpoint_states += len(current)
        previous = current
    assert len(witnesses) == full
    assert all(target in witnesses for target in range(1, full + 1))
    size = 1
    while size < len(word):
        size <<= 1
    tree = [0] * (2 * size)
    tree[size:size + len(word)] = word
    for j in range(size - 1, 0, -1):
        tree[j] = tree[2 * j] | tree[2 * j + 1]
    for target, (left, right) in witnesses.items():
        assert 0 <= left <= right < len(word)
        a, b = left + size, right + size + 1
        value = 0
        while a < b:
            if a & 1:
                value |= tree[a]
                a += 1
            if b & 1:
                b -= 1
                value |= tree[b]
            a //= 2
            b //= 2
        assert value == target
    return witnesses, endpoint_states


def run():
    raw = SOURCE.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == EXPECTED_SHA
    word = [int(token) for token in raw.split()]
    assert len(word) == 24313 and all(1 <= x <= FULL for x in word)
    full_coverage, base_scans = forward_coverage(word)
    assert all(full_coverage[1:])
    source_cap_records = []
    representatives = {}
    for orientation, oriented in [('forward', word), ('reverse', word[::-1])]:
        last, previous = oriented[-1], oriented[-2]
        backup = oriented[:-1].index(last)
        mandatory = last & ~previous
        caps = []
        sub = last
        while sub:
            if sub & mandatory == mandatory:
                caps.append(sub)
            sub = (sub - 1) & last
        caps.sort(key=lambda c: (c.bit_count(), c))
        for cap in caps:
            assert cap and cap & ~last == 0
            assert previous | cap == previous | last
            assert oriented[backup] == last and backup < len(oriented) - 1
            capped = oriented[:-1] + [cap]
            blocks = recency_blocks(capped)
            shape = tuple(b.bit_count() for b in blocks)
            assert shape == (cap.bit_count(), 7 - cap.bit_count()) + (1,) * 10
            record = dict(source_orientation=orientation, original_last=last,
                          previous_letter=previous, mandatory_cap=mandatory,
                          cap=cap, backup_zero_based_position=backup,
                          profile=list(shape), recency_blocks=blocks)
            source_cap_records.append(record)
            representatives.setdefault(shape, (record, capped))
    assert sorted(representatives) == [(s, 7-s) + (1,) * 10 for s in range(1, 6)]
    # Positive control: no search or relabeling, exactly the verified trimmed lift.
    control_tail = word[:-1]
    control_cov, control_scans = forward_coverage(control_tail)
    control_defects = [d for d in range(1, FULL + 1) if not control_cov[d]]
    cs, cp, ca, cr = graph_for(control_tail, control_defects)
    original_blocks = recency_blocks(word)
    assert check_blocks(cs, original_blocks)
    control_witnesses = []
    for row in cr:
        target = row['target']
        suffix = 0
        suffix_length = 0
        for letter in reversed(word):
            if letter & ~target:
                break
            suffix |= letter
            suffix_length += 1
        assert suffix | row['maximal_compatible_prefix_union'] == target
        control_witnesses.append(dict(target=target, suffix_length=suffix_length,
                                      suffix_union=suffix, **{
                                          'prefix_length': row['maximal_compatible_prefix_length'],
                                          'prefix_union': row['maximal_compatible_prefix_union']}))
    print('POSITIVE_CONTROL_PASS', json.dumps(dict(defects=len(control_defects),
          original_profile=[b.bit_count() for b in original_blocks],
          source_cap_profiles=len(representatives))), flush=True)
    cases = []
    success = None
    for prefix_cut in range(5):
        suffix_cut = 4 - prefix_cut
        stop = len(word) - suffix_cut
        base_tail = word[prefix_cut:stop]
        assert len(base_tail) == 24309
        coverage, scanned = forward_coverage(base_tail)
        defects = [d for d in range(1, FULL + 1) if not coverage[d]]
        intersection = FULL
        for target in defects:
            intersection &= target
        for orientation, tail in [('forward', base_tail), ('reverse', base_tail[::-1])]:
            successor, predecessor, arc_defect, rows = graph_for(tail, defects)
            assert sum(1 << v for v in minima(predecessor, FULL)) == intersection
            cycle = directed_cycle(successor)
            case = dict(prefix_cut=prefix_cut, suffix_cut=suffix_cut,
                        tail_orientation=orientation, tail_length=len(tail),
                        internal_target_count=sum(coverage),
                        direct_forward_intervals=scanned,
                        defects=defects, defect_rank_counts=ranks(defects),
                        defect_intersection=intersection,
                        maximal_prefix_rows=rows,
                        successor_masks=successor, predecessor_masks=predecessor,
                        graph_arc_count=sum(x.bit_count() for x in successor))
            if cycle is not None:
                assert all(successor[x] & (1 << y) for x, y in zip(cycle, cycle[1:]))
                case.update(status='INFEASIBLE_DIRECTED_CYCLE', directed_cycle=cycle,
                            cycle_arc_defects=[arc_defect[x, y]
                                               for x, y in zip(cycle, cycle[1:])])
            else:
                decisions = []
                for shape in sorted(representatives):
                    decision = decide_profile(successor, predecessor, shape)
                    decisions.append(decision)
                    if decision['status'] == 'FEASIBLE' and success is None:
                        record, capped = representatives[shape]
                        target_blocks = decision['target_blocks']
                        permutation = [-1] * 17
                        for original, target in zip(record['recency_blocks'], target_blocks):
                            for x, y in zip(bits(original), bits(target)):
                                permutation[x] = y
                        assert sorted(permutation) == list(range(17))
                        relabeled = [sum(1 << permutation[x] for x in bits(a)) for a in capped]
                        assert recency_blocks(relabeled) == target_blocks
                        candidate = relabeled + [Z] + [letter | Z for letter in tail]
                        assert len(candidate) == 48623
                        witnesses, states = suffix_witnesses_and_independent_replay(candidate, (1 << 18)-1)
                        literal = ('\n'.join(map(str, candidate)) + '\n').encode()
                        literal_name = 'k18_optimal48623_one_seam.word'
                        (OUT / literal_name).write_bytes(literal)
                        with (OUT / 'k18_optimal48623_one_seam_witnesses.jsonl').open('w') as stream:
                            for target in sorted(witnesses):
                                stream.write(json.dumps([target, *witnesses[target]]) + '\n')
                        success = dict(prefix_cut=prefix_cut, suffix_cut=suffix_cut,
                                       tail_orientation=orientation, source_cap=record,
                                       target_blocks=target_blocks,
                                       permutation_zero_based=permutation,
                                       length=len(candidate), target_count=len(witnesses),
                                       endpoint_states_scanned=states,
                                       all_witnesses_independently_range_or_checked=True,
                                       literal_file=literal_name,
                                       literal_sha256=hashlib.sha256(literal).hexdigest())
                        print('LITERAL_SUCCESS', json.dumps(success), flush=True)
                case.update(status=('FEASIBLE' if any(d['status']=='FEASIBLE' for d in decisions)
                                    else 'INFEASIBLE_ALL_CAP_PROFILES'), profile_decisions=decisions)
            cases.append(case)
            print('CASE', json.dumps({k:case[k] for k in
                  ('prefix_cut','suffix_cut','tail_orientation','status','defect_rank_counts',
                   'defect_intersection','graph_arc_count')}), flush=True)
    report = dict(status='SAT_LITERAL_VERIFIED' if success else 'COMPLETE_SPECIFIED_FAMILY_INFEASIBLE',
                  source_sha256=digest, source_length=len(word), source_forward_scans=base_scans,
                  scope='Exactly the five total-four end trims, both tail orientations, and A/reverse(A) with all pair-preserving duplicate-backed terminal caps, followed by arbitrary relative coordinate relabeling. No broader impossibility claim.',
                  source_cap_records=source_cap_records,
                  distinct_cap_profiles=[list(s) for s in sorted(representatives)],
                  positive_control=dict(status='PASS', tail_length=len(control_tail),
                      defects=control_defects, original_recency_blocks=original_blocks,
                      forward_scans=control_scans, literal_seam_projection_witnesses=control_witnesses),
                  cases=cases, success=success,
                  resource_caps=dict(cpu_seconds=60,wall_seconds=90,address_space_bytes=1024**3),
                  elapsed_seconds=time.monotonic()-STARTED)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + '\n')
    print('FINAL', json.dumps({k:report[k] for k in
          ('status','distinct_cap_profiles','success','elapsed_seconds')}), flush=True)


if __name__ == '__main__':
    try:
        run()
    except MemoryError:
        REPORT_PATH.write_text(json.dumps(dict(status='INCONCLUSIVE_MEMORY_LIMIT',
            elapsed_seconds=time.monotonic()-STARTED))+'\n')
        raise
