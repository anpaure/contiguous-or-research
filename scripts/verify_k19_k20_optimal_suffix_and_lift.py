#!/usr/bin/env python3
"""Fixed 19/20 literal certification, independent suffix and range-OR passes.

One bounded h100 run. No PBBS routine, search, or previous verifier is used.
The cyclic19 certificate is deduced from its verified ordinary witnesses;
the supplied20 bytes are regenerated from the literal19 periodic core.
"""
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

BASE = Path('/home/amodo/exact-b-k19-k20-optimal-20260909')
OUT = BASE / 'suffix_and_lift'
INPUTS = (
    (19, 92381, '1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414'),
    (20, 184759, '047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02'),
)


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def lower_bounds(k):
    smaller = 0
    rows = []
    for s in range(1, k + 1):
        width = math.comb(k, s)
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
        rows.append(dict(rank=s, width=width, smaller=smaller,
                         t=lo, lower=width + lo,
                         capacity_at_t_minus_one=capacity(lo - 1) if lo else None))
        smaller += width
    assert smaller == (1 << k) - 1
    bound = max(row['lower'] for row in rows)
    return dict(B=bound, maximizing_ranks=[row['rank'] for row in rows
                                         if row['lower'] == bound], rows=rows)


def serialize(word):
    return ('\n'.join(map(str, word)) + '\n').encode('ascii')


def verify(k, expected_length, expected_sha):
    raw = (BASE / f'k{k}_optimal{expected_length}.word').read_bytes()
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
    assert lower['B'] == n
    starts = array('i', [-1]) * (full + 1)
    ends = array('i', [-1]) * (full + 1)
    assert starts.itemsize == 4 and n < 2**31
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
        assert len(current) <= k
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
    assert ranks[1:] == [math.comb(k, s) for s in range(1, k + 1)]
    assert absent_middle == [0, 1, 2] and middle_duplicates == 0
    assert middle_events == math.comb(k, middle)

    # This is a separate range-OR algorithm on the literal input.
    base = 1
    while base < n:
        base <<= 1
    tree = [0] * (2 * base)
    tree[base:base+n] = word
    for i in range(base - 1, 0, -1):
        tree[i] = tree[2*i] | tree[2*i+1]

    def query(left, right):
        left += base
        right += base + 1
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
    with gzip.open(OUT / witness_name, 'wt', encoding='ascii', compresslevel=1) as dst:
        for target in range(1, full + 1):
            left, right = starts[target], ends[target]
            assert 0 <= left <= right < n
            assert query(left, right) == target
            maximum_span = max(maximum_span, right - left + 1)
            dst.write(f'[{target},{left},{right}]\n')
    report = dict(status='PASS', k=k, length=n, input_sha256=digest,
                  input_bytes=len(raw), nonempty_targets=full, targets_covered=distinct,
                  missing_targets=0, suffix_union_events=events,
                  separately_rechecked_witnesses=full, maximum_saved_witness_length=maximum_span,
                  witness_file=witness_name,
                  witness_format='JSONL [target,zero-based inclusive start,end], gzip',
                  target_rank_counts=ranks, all_rank_lower_bound=lower,
                  middle_rank=middle, middle_suffix_events=middle_events,
                  repeated_middle_targets=middle_duplicates,
                  endpoints_without_middle_target=absent_middle,
                  all_letters_nonempty=True, all_witnesses_nonwrapping=True,
                  exact_equality_certified=True)
    save(f'k{k}_suffix_range_certificate.json', report)
    print('LITERAL_PASS', json.dumps({key: report[key] for key in
        ('k', 'length', 'input_sha256', 'targets_covered', 'suffix_union_events',
         'separately_rechecked_witnesses', 'maximum_saved_witness_length')}), flush=True)
    return word, raw, report


def cyclic_and_lift(word19, raw19, result19, word20, raw20):
    M = math.comb(19, 10)
    d = len(word19) - M
    assert M == 92378 and d == 3
    core = word19[:M]
    assert word19 == core + core[:d]
    assert core[:3] == [364614, 376898, 104514]
    assert result19['maximum_saved_witness_length'] <= M
    middle9 = set()
    middle10 = set()
    for i in range(M):
        a = word19[i] | word19[i+1] | word19[i+2]
        b = a | word19[i+3]
        assert a.bit_count() == 9 and b.bit_count() == 10
        assert a not in middle9 and b not in middle10
        middle9.add(a)
        middle10.add(b)
    assert len(middle9) == math.comb(19, 9) == M
    assert len(middle10) == math.comb(19, 10) == M
    core_raw = serialize(core)
    (OUT / 'k19_cyclic92378.word').write_bytes(core_raw)

    # Every checked linear witness belongs to the periodic core and spans
    # at most one period, so it is an admissible ordinary cyclic witness.
    # Cyclic endpoint capacity gives the matching lower bound M.
    z = 1 << 19
    generated = word19 + [z] + [core[(d+j) % M] | z for j in range(M-1)]
    generated_raw = serialize(generated)
    assert generated == word20 and generated_raw == raw20
    assert len(generated) == 2*M + d == 184759
    (OUT / 'k20_regenerated_from_k19.word').write_bytes(generated_raw)
    result = dict(status='PASS', cyclic19_period=M, cyclic19_minimum=M,
                  cyclic19_sha256=hashlib.sha256(core_raw).hexdigest(),
                  cyclic_coverage_basis='All524287 independently range-checked ordinary witnesses occur in C plus prefix3 and have length at most M; reducing start modulo M preserves their letters and produces admissible cyclic witnesses.',
                  cyclic9_windows=M, cyclic10_windows=M,
                  safe_opening_extra_letters=d, first_three=core[:3],
                  lift_extra_coordinate_mask=z, lift_updates=M-1,
                  regenerated20_length=len(generated), regenerated20_byte_identical=True,
                  regenerated20_sha256=hashlib.sha256(generated_raw).hexdigest(),
                  unprovided_compact19_generator_replayed=False,
                  new_word_search=False)
    save('cyclic19_and_periodic_core_lift.json', result)
    return result


def main():
    assert socket.gethostname().split('.')[0] == 'arboghast'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256*1024**2, 256*1024**2))
    signal.alarm(90)
    started = time.monotonic()
    OUT.mkdir(exist_ok=False)
    try:
        w19, raw19, r19 = verify(*INPUTS[0])
        w20, raw20, r20 = verify(*INPUTS[1])
        structure = cyclic_and_lift(w19, raw19, r19, w20, raw20)
        report = dict(status='PASS', words=[r19, r20], cyclic_and_lift=structure,
                      next_endpoint_bounds={k: lower_bounds(k) for k in (21, 22)},
                      previous_turnover21=(math.comb(20, 10)//11 + 2)//3,
                      paired_run_lower_bound21=math.comb(20, 10)//11 - 3,
                      hostname=socket.gethostname(),
                      source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      limits=dict(cpu_seconds=60, wall_seconds=90, address_space_bytes=2*1024**3),
                      elapsed_wall_seconds=time.monotonic()-started)
        save('complete_suffix_range_cyclic_lift_certificate.json', report)
        print('FINAL_PASS', json.dumps(dict(equality19=r19['length'], equality20=r20['length'],
                    cyclic_minimum19=structure['cyclic19_minimum'],
                    B21=report['next_endpoint_bounds'][21]['B'],
                    B22=report['next_endpoint_bounds'][22]['B'],
                    paired_run_lower_bound21=report['paired_run_lower_bound21'],
                    elapsed_wall_seconds=report['elapsed_wall_seconds'])), flush=True)
    except Exception as error:
        save('failure_not_certified.json', dict(status='ERROR_NOT_CERTIFIED', error=repr(error)))
        raise


if __name__ == '__main__':
    main()
