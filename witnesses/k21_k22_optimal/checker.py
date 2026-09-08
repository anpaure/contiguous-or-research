#!/usr/bin/env python3
"""One fixed h100 audit of the supplied optimal21/22 words; no search.

Complete suffix families, one independently range-checked witness per
target, all-rank endpoint bounds, cyclic21 opening and periodic-core lift.
"""
import argparse
import gzip
import hashlib
import json
import math
import resource
import signal
import socket
import time
from array import array
from pathlib import Path

INPUTS = (
    (21, 352719, 352719, 'eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2'),
    (22, 705435, 705435, 'a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd'),
)
CAPS = dict(cpu_seconds=120, wall_seconds=150,
            address_space_bytes=3 * 1024**3, file_bytes=512 * 1024**2)


def save(out, name, value):
    (out / name).write_text(json.dumps(value, indent=2) + '\n')


def lower_bounds(k):
    smaller = 0
    rows = []
    for rank in range(1, k + 1):
        width = math.comb(k, rank)

        def capacity(t):
            return t * width + t * (t + 1) // 2

        hi = 1
        while capacity(hi) < smaller:
            hi *= 2
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if capacity(mid) >= smaller:
                hi = mid
            else:
                lo = mid + 1
        assert capacity(lo) >= smaller
        assert lo == 0 or capacity(lo - 1) < smaller
        rows.append(dict(rank=rank, width=width, smaller=smaller,
                         t=lo, lower=width + lo,
                         capacity_at_t_minus_one=capacity(lo - 1) if lo else None))
        smaller += width
    assert smaller == (1 << k) - 1
    bound = max(row['lower'] for row in rows)
    return dict(B=bound, maximizing_ranks=[row['rank'] for row in rows
                                         if row['lower'] == bound], rows=rows)


def verify(base_path, out, k, expected_length, expected_lower, expected_sha):
    raw = (base_path / f'k{k}_optimal{expected_length}.word').read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == expected_sha
    tokens = raw.split()
    assert tokens and all(token.isdigit() for token in tokens)
    word = [int(token) for token in tokens]
    del tokens
    n = len(word)
    full = (1 << k) - 1
    assert n == expected_length and all(0 < letter <= full for letter in word)
    lower = lower_bounds(k)
    assert lower['B'] == expected_lower == n
    starts = array('i', [-1]) * (full + 1)
    ends = array('i', [-1]) * (full + 1)
    assert starts.itemsize == ends.itemsize == 4 and n < 2**31
    previous = {}
    events = distinct = middle_events = middle_duplicates = 0
    middle = (k + 1) // 2
    absent_middle = []
    ranks = [0] * (k + 1)
    for right, letter in enumerate(word):
        current = {letter: right}
        for target, left in previous.items():
            union = target | letter
            current[union] = max(current.get(union, -1), left)
        assert 1 <= len(current) <= k
        has_middle = False
        for target, left in current.items():
            rank = target.bit_count()
            assert 1 <= target <= full and 0 <= left <= right
            if rank == middle:
                assert not has_middle
                has_middle = True
                middle_events += 1
                if starts[target] >= 0:
                    middle_duplicates += 1
            if starts[target] < 0:
                starts[target] = left
                ends[target] = right
                distinct += 1
                ranks[rank] += 1
        if not has_middle:
            absent_middle.append(right)
        events += len(current)
        previous = current
    assert distinct == full
    assert all(starts[target] >= 0 for target in range(1, full + 1))
    assert ranks[1:] == [math.comb(k, rank) for rank in range(1, k + 1)]
    assert middle_events - middle_duplicates == math.comb(k, middle)
    assert absent_middle == [0, 1, 2] and middle_duplicates == 0

    # Independent range-OR calculation from the raw word, not suffix state.
    tree_base = 1
    while tree_base < n:
        tree_base <<= 1
    tree = array('I', [0]) * (2 * tree_base)
    assert tree.itemsize == 4
    tree[tree_base:tree_base+n] = array('I', word)
    for i in range(tree_base - 1, 0, -1):
        tree[i] = tree[2*i] | tree[2*i+1]

    def query(left, right):
        left += tree_base
        right += tree_base + 1
        union = 0
        while left < right:
            if left & 1:
                union |= tree[left]
                left += 1
            if right & 1:
                right -= 1
                union |= tree[right]
            left >>= 1
            right >>= 1
        return union

    maximum_span = 0
    witness_name = f'k{k}_all_target_witnesses.jsonl.gz'
    with gzip.open(out / witness_name, 'wt', encoding='ascii', compresslevel=1) as dst:
        for target in range(1, full + 1):
            left, right = starts[target], ends[target]
            assert 0 <= left <= right < n
            assert query(left, right) == target
            maximum_span = max(maximum_span, right - left + 1)
            dst.write(f'[{target},{left},{right}]\n')
    width = math.comb(k, k // 2)
    report = dict(status='PASS_EXACT_OPTIMUM', k=k, length=n,
                  input_sha256=digest, input_bytes=len(raw),
                  nonempty_targets=full, targets_covered=distinct,
                  missing_targets=0, suffix_union_events=events,
                  separately_rechecked_witnesses=full,
                  maximum_saved_witness_length=maximum_span,
                  witness_file=witness_name,
                  witness_format='JSONL [target,zero-based inclusive start,end], gzip',
                  target_rank_counts=ranks, all_rank_lower_bound=lower,
                  width=width, upper_bound_minus_B=n-lower['B'],
                  upper_bound_relative_excess_over_width=[n-width, width],
                  middle_rank=middle, middle_suffix_events=middle_events,
                  repeated_middle_targets=middle_duplicates,
                  endpoints_without_middle_target=absent_middle,
                  all_letters_nonempty=True, all_witnesses_nonwrapping=True,
                  exact_equality_certified=True)
    save(out, f'k{k}_suffix_range_certificate.json', report)
    print('LITERAL_PASS', json.dumps({key: report[key] for key in
        ('k', 'length', 'targets_covered', 'suffix_union_events',
         'separately_rechecked_witnesses', 'upper_bound_minus_B')}), flush=True)
    return word, raw, report


def cyclic_and_lift(out, w21, r21, w22, raw22):
    M = math.comb(21, 11)
    d = len(w21) - M
    assert M == 352716 and d == 3
    core = w21[:M]
    assert w21 == core + core[:d]
    assert core[:3] == [1499680, 1372192, 1358336]
    assert r21['maximum_saved_witness_length'] <= M
    lower_windows = set()
    upper_windows = set()
    for i in range(M):
        low = w21[i] | w21[i+1] | w21[i+2]
        high = low | w21[i+3]
        assert low.bit_count() == 10 and high.bit_count() == 11
        assert low not in lower_windows and high not in upper_windows
        lower_windows.add(low)
        upper_windows.add(high)
    assert len(lower_windows) == math.comb(21, 10) == M
    assert len(upper_windows) == math.comb(21, 11) == M
    core_raw = ('\n'.join(map(str, core)) + '\n').encode('ascii')
    (out / 'k21_cyclic352716.word').write_bytes(core_raw)
    # All independently range-checked ordinary witnesses occur in C+C[:3]
    # and span at most M. Reducing starts modulo M certifies cyclic coverage.
    # Cyclic endpoint capacity gives the equal lower bound M.
    z = 1 << 21
    generated = w21 + [z] + [core[(d+j) % M] | z for j in range(M-1)]
    generated_raw = ('\n'.join(map(str, generated)) + '\n').encode('ascii')
    assert generated == w22 and generated_raw == raw22
    assert len(generated) == 2*M+d == 705435
    (out / 'k22_regenerated_from_k21.word').write_bytes(generated_raw)
    result = dict(status='PASS_CYCLIC_OPTIMUM_AND_PERIODIC_LIFT',
                  cyclic21_period=M, cyclic21_minimum=M,
                  cyclic21_sha256=hashlib.sha256(core_raw).hexdigest(),
                  cyclic_coverage_basis='Every2097151 independently range-checked ordinary witness lies in C+C[:3] and has length at most M; reducing its start modulo M preserves its interval letters.',
                  distinct_cyclic_rank10_triples=len(lower_windows),
                  distinct_cyclic_rank11_four_windows=len(upper_windows),
                  safe_opening_extra_letters=d, first_three=core[:3],
                  extra_coordinate_mask=z, lifted_updates=M-1,
                  regenerated22_byte_identical=True,
                  regenerated22_length=len(generated),
                  regenerated22_sha256=hashlib.sha256(generated_raw).hexdigest())
    save(out, 'cyclic21_and_periodic_core_lift.json', result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (CAPS['cpu_seconds'],) * 2)
    resource.setrlimit(resource.RLIMIT_AS, (CAPS['address_space_bytes'],) * 2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS['file_bytes'],) * 2)
    signal.alarm(CAPS['wall_seconds'])
    started = time.monotonic()
    cpu_start = time.process_time()
    args.out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).read_bytes()
    (args.out / 'checker.py').write_bytes(source)
    save(args.out, 'run_started.json', dict(status='RUNNING_NOT_CERTIFIED', limits=CAPS))
    try:
        w21, raw21, r21 = verify(args.inputs, args.out, *INPUTS[0])
        w22, raw22, r22 = verify(args.inputs, args.out, *INPUTS[1])
        structure = cyclic_and_lift(args.out, w21, r21, w22, raw22)
        report = dict(status='PASS_EXACT_OPTIMA_CYCLIC21_AND_PERIODIC_LIFT',
                      words=[r21, r22],
                      cyclic_and_lift=structure,
                      next_endpoint_bounds={k: lower_bounds(k) for k in (23, 24)},
                      hostname=socket.gethostname(), limits=CAPS,
                      source_sha256=hashlib.sha256(source).hexdigest(),
                      elapsed_wall_seconds=time.monotonic()-started,
                      elapsed_cpu_seconds=time.process_time()-cpu_start,
                      compact_generator_replayed=False,
                      orbit_hall_certificate_verified=False,
                      any_word_search=False)
        save(args.out, 'complete_suffix_range_cyclic_lift_certificate.json', report)
        print('FINAL_PASS', json.dumps(dict(
            B21=r21['all_rank_lower_bound']['B'], upper21=r21['length'],
            gap21=r21['upper_bound_minus_B'], B22=r22['all_rank_lower_bound']['B'],
            upper22=r22['length'], gap22=r22['upper_bound_minus_B'],
            cyclic_minimum21=structure['cyclic21_minimum'],
            B23=report['next_endpoint_bounds'][23]['B'],
            B24=report['next_endpoint_bounds'][24]['B'],
            elapsed_wall_seconds=report['elapsed_wall_seconds'])), flush=True)
    except Exception as error:
        save(args.out, 'failure_not_certified.json', dict(status='ERROR_NOT_CERTIFIED', error=repr(error)))
        raise


if __name__ == '__main__':
    main()
