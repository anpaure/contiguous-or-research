#!/usr/bin/env python3
"""One proof-purpose diagnostic; h100 only, no construction search.

Exhaust every nonempty word on the seven nonempty three-coordinate letters
through length six, in both endpoint orientations. Then inspect only tag-run
statistics of the already certified, hash-pinned optimal17/18 literals.
No word is changed and no new universal-word search is performed.
"""
import argparse
import hashlib
import itertools
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path


assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 only'

EXPECTED = {
    17: (24313, '7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'),
    18: (48623, '6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5'),
}
SMALL_FAMILIES = tuple(
    (z, s,
     tuple(d for d in range(1, 8) if not d & z and d.bit_count() == s),
     tuple(d for d in range(1, 8) if d & z and d.bit_count() == s+1))
    for z in (1, 2, 4) for s in (1, 2)
)


def suffix_witnesses(word):
    """One actual witness per present target: first end, latest start there."""
    previous = {}
    witnesses = {}
    for right, letter in enumerate(word):
        current = {letter: right}
        for target, left in previous.items():
            new = target | letter
            current[new] = max(current.get(new, -1), left)
        assert len(current) <= 3
        for target, left in current.items():
            witnesses.setdefault(target, (left, right))
        previous = current
    return witnesses


def check_small_orientation(word, totals):
    witnesses = suffix_witnesses(word)
    n = len(word)
    for z in (1, 2, 4):
        last_mark = -1
        B = 0
        last_marks = []
        run_prefixes = []
        exits = 0
        for t, letter in enumerate(word):
            if letter & z:
                last_mark = t
                B = 0
            else:
                if t and word[t-1] & z:
                    exits += 1
                B |= letter
            last_marks.append(last_mark)
            run_prefixes.append(B)
        for fz, s, old_family, marked_family in SMALL_FAMILIES:
            if fz != z:
                continue
            old_at = {}
            marked_at = {}
            for target in old_family:
                if target in witnesses:
                    left, right = witnesses[target]
                    assert right not in old_at
                    old_at[right] = (target, left)
            for target in marked_family:
                if target in witnesses:
                    left, right = witnesses[target]
                    assert right not in marked_at
                    marked_at[right] = (target, left)
            common = old_at.keys() & marked_at.keys()
            assert len(common) >= len(old_at)+len(marked_at)-n
            used_runs = set()
            for right in common:
                D, old_left = old_at[right]
                E, marked_left = marked_at[right]
                q = last_marks[right]
                assert E == (D | z)
                assert not word[right] & z
                assert 0 <= q < right
                assert marked_left <= q < old_left
                assert run_prefixes[right] == D
                assert (word[q] & ~z) & ~D == 0
                # Different chosen old targets cannot use the same run's
                # sole rank-s prefix value.
                assert q not in used_runs
                used_runs.add(q)
                for target, left in ((D, old_left), (E, marked_left)):
                    literal = 0
                    for letter in word[left:right+1]:
                        literal |= letter
                    assert literal == target
            assert len(used_runs) == len(common) <= exits
            assert len(old_at)+len(marked_at) <= n+exits
            totals['family_orientation_checks'] += 1
            totals['shared_endpoint_events'] += len(common)
            totals['literal_shared_witnesses_replayed'] += 2*len(common)


def enumerate_small():
    totals = Counter()
    lengths = {}
    for n in range(1, 7):
        count = 0
        for word in itertools.product(range(1, 8), repeat=n):
            check_small_orientation(word, totals)
            check_small_orientation(word[::-1], totals)
            count += 1
        assert count == 7**n
        lengths[n] = count
        totals['distinct_words'] += count
        print('SMALL_LENGTH_PASS', json.dumps(dict(length=n, words=count)), flush=True)
    assert totals['distinct_words'] == sum(7**n for n in range(1, 7))
    assert totals['family_orientation_checks'] == 12*totals['distinct_words']
    return dict(status='PASS', lengths=lengths, **totals,
                both_endpoint_orientations=True,
                partial_coverage_used_not_universality=True,
                every_shared_endpoint_injected_into_a_distinct_run=True)


def literal_runs(path, dimension):
    raw = path.read_bytes()
    length, expected_sha = EXPECTED[dimension]
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == expected_sha
    word = [int(x) for x in raw.split()]
    assert len(word) == length
    assert all(0 < x < (1 << dimension) for x in word)
    ranks = [x.bit_count() for x in word]
    rank_hist = Counter(ranks)
    rows = []
    for coordinate in range(dimension):
        z = 1 << coordinate
        M = exits = entrances = runs = 0
        start_ranks = Counter()
        end_ranks = Counter()
        for i, letter in enumerate(word):
            marked = bool(letter & z)
            if not marked:
                M += 1
                if i == 0 or word[i-1] & z:
                    runs += 1
                    start_ranks[ranks[i]] += 1
                if i+1 == length or word[i+1] & z:
                    end_ranks[ranks[i]] += 1
            if i:
                previous_marked = bool(word[i-1] & z)
                exits += previous_marked and not marked
                entrances += not previous_marked and marked
        assert sum(start_ranks.values()) == sum(end_ranks.values()) == runs
        assert exits == runs-int((word[0] & z) == 0)
        assert entrances == runs-int((word[-1] & z) == 0)
        rank_checks = []
        for s in range(1, dimension):
            W = math.comb(dimension-1, s)
            demand = max(0, 2*W-length)
            assert exits >= demand and entrances >= demand
            assert runs-start_ranks[s] <= M-W
            assert runs-end_ranks[s] <= M-W
            new_start_floor = 3*W-length-M
            assert start_ranks[s] >= new_start_floor
            assert end_ranks[s] >= new_start_floor
            old_start_floor = (s+1)*W-length-(s-1)*M
            assert start_ranks[s] >= old_start_floor
            assert end_ranks[s] >= old_start_floor
            rank_checks.append(dict(old_rank=s, target_family_size=W,
                paired_exit_and_entrance_floor=demand,
                rank_s_run_starts=start_ranks[s], rank_s_run_ends=end_ranks[s],
                paired_run_start_floor=max(0,new_start_floor),
                previous_run_start_floor=max(0,old_start_floor)))
        rows.append(dict(coordinate_zero_based=coordinate, unmarked_letters=M,
            marked_letters=length-M, unmarked_runs=runs, exits=exits,
            entrances=entrances, run_start_rank_histogram=dict(sorted(start_ranks.items())),
            run_end_rank_histogram=dict(sorted(end_ranks.items())),
            all_rank_inequalities=rank_checks))
    return dict(status='PASS', dimension=dimension, length=length, sha256=digest,
        literal_rank_histogram=dict(sorted(rank_hist.items())),
        per_coordinate=rows,
        scope='Run statistics and necessary universal-word inequalities only. Full-cube coverage is inherited from earlier hash-pinned literal certificates, not recomputed in this run.')


def arithmetic():
    W16 = math.comb(16, 8)
    W18 = math.comb(18, 9)
    N17 = 24313
    N19 = 92381
    M18 = 48623
    assert 2*W16-N17 == 1427
    assert 2*W18-N19 == 4859
    assert 3*W18-N19-M18 == 4856
    assert 3*W18-N19 == 53479
    assert 53479-M18 == 4856
    assert 10*W18-N19-8*M18 == 4835
    assert 2*W18-1 == 97239
    assert 97239-(M18+W18-9) == 5
    return dict(status='PASS', paired_exits17=1427, paired_exits19=4859,
        run_start_rank9_floor_at_optimal18_trace=4856,
        previous_run_start_rank9_floor=4835,
        no_rank9_minimum_unmarked_letters19=53479,
        extra_unmarked_letters_above48623=4856,
        at_most_one_exit_length_lower_bound19=97239,
        improvement_over_previous_single_block_bound=5)


def main():
    assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    signal.alarm(45)
    started = time.monotonic()
    ap = argparse.ArgumentParser()
    ap.add_argument('--k17', type=Path, required=True)
    ap.add_argument('--k18', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    small = enumerate_small()
    literals = [literal_runs(args.k17,17), literal_runs(args.k18,18)]
    exact = arithmetic()
    report = dict(status='PASS', exhaustive_small_words=small,
        actual_literal_run_checks=literals, exact_arithmetic=exact,
        execution_host=socket.gethostname(),
        limits=dict(cpu_seconds=30,wall_seconds=45,address_space_bytes=1024**3),
        elapsed_seconds=time.monotonic()-started,
        no_construction_search=True,no_word_modified=True,
        proof_is_primary_finite_enumeration_is_diagnostic=True)
    (args.out/'paired_endpoint_run_diagnostic.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINAL_PASS',json.dumps(dict(words=small['distinct_words'],
        family_orientation_checks=small['family_orientation_checks'],
        arithmetic=exact,elapsed_seconds=report['elapsed_seconds'])),flush=True)


if __name__ == '__main__':
    main()
