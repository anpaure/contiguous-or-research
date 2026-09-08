#!/usr/bin/env python3
"""REVIEW BEFORE RUN: fixed supplied phase, exactly255 targets, h100 only.

No cut is moved or searched. No word is changed. Complete compatible runs
and all inclusion-minimal owner witnesses are reconstructed for each proper
superset of the one removed owner's edge colour.
"""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from collections import Counter
from pathlib import Path

N = 19
FULL = (1 << N) - 1
M = 92378
Q = 3
WORD_SHA = '1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414'


def bits(mask):
    answer = []
    while mask:
        bit = mask & -mask
        answer.append(bit.bit_length() - 1)
        mask ^= bit
    return answer


def union_range(values, left, right):
    answer = 0
    for i in range(left, right):
        answer |= values[i]
    return answer


def minimal_witnesses(start, end, target_bits, owner_bits):
    """All inclusion-minimal intervals inside one complete compatible run.

    For each endpoint keep its latest possible T-covering start. This is
    inclusion-minimal at the right end precisely when that start strictly
    increases from the previous endpoint's latest covering start.
    """
    first = {x: None for x in target_bits}
    last = {x: None for x in target_bits}
    counts = [0] * N
    missing = len(target_bits)
    left = start
    previous_latest = None
    witnesses = []
    for right in range(start, end + 1):
        for x in owner_bits[right % M]:
            if first[x] is None:
                first[x] = right
            last[x] = right
            if counts[x] == 0:
                missing -= 1
            counts[x] += 1
        if missing:
            continue
        while all(counts[x] >= 2 for x in owner_bits[left % M]):
            for x in owner_bits[left % M]:
                counts[x] -= 1
            left += 1
        assert all(counts[x] >= 1 for x in target_bits)
        assert any(counts[x] == 1 for x in owner_bits[left % M])
        if previous_latest is None or left > previous_latest:
            witnesses.append([left, right])
        else:
            assert left == previous_latest
        previous_latest = left
    assert missing == 0 and witnesses
    assert all(first[x] is not None and last[x] is not None for x in target_bits)
    earliest_end = max(first.values())
    latest_start = min(last.values())
    # Independent occurrence-extreme calculation checks the witness extremes.
    assert min(b for a, b in witnesses) == earliest_end
    assert max(a for a, b in witnesses) == latest_start
    return dict(minimal_witnesses=witnesses,
                coordinate_first=[[x, first[x]] for x in target_bits],
                coordinate_last=[[x, last[x]] for x in target_bits],
                earliest_completion=earliest_end, latest_covering_start=latest_start,
                forced_edge_interval=([latest_start + 1, earliest_end]
                                      if latest_start < earliest_end else None))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--word', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    assert platform.node().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256 * 1024**2, 256 * 1024**2))
    signal.alarm(90)
    began = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=False)
    (args.out / 'run_started.json').write_text('{"status":"RUNNING_NOT_CERTIFIED"}\n')
    raw = args.word.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == WORD_SHA
    A = [int(value) for value in raw.split()]
    assert len(A) == M + Q and all(0 < value <= FULL for value in A)
    C = A[:M]
    assert A == C + C[:Q]
    R = [A[i] | A[i+1] | A[i+2] for i in range(M)]
    U = [R[i] | A[i+3] for i in range(M)]
    assert all(value.bit_count() == 9 for value in R) and len(set(R)) == M
    assert all(value.bit_count() == 10 for value in U) and len(set(U)) == M
    assert all(U[(i-1) % M] & U[i] == R[i] for i in range(M))
    V = U[-1] | U[0]
    assert V.bit_count() == 11
    outside = FULL ^ V
    targets = []
    subset = outside
    while True:
        target = V | subset
        if target != FULL:
            targets.append(target)
        if subset == 0:
            break
        subset = (subset - 1) & outside
    targets.sort()
    assert len(targets) == 255 and len(set(targets)) == 255
    owner_bits = [bits(value) for value in U]
    reasons = Counter()
    counts = Counter()
    summaries = []
    failures = []
    witness_file = args.out / 'all_255_run_and_minimal_witness_records.jsonl'
    with witness_file.open('w') as stream:
        for target in targets:
            excluded = FULL ^ target
            # This is an outside-letter anchor used only to enumerate runs.
            # The opening is ALWAYS the original edge U[-1] -> U[0].
            anchor = next(i for i, value in enumerate(U) if value & excluded)
            assert anchor > 0  # U0 is contained in every tested target.
            runs = []
            run_start = None
            run_union = 0
            for j in range(anchor + 1, anchor + M + 1):
                value = U[j % M]
                if not value & excluded:
                    if run_start is None:
                        run_start = j
                    run_union |= value
                elif run_start is not None:
                    runs.append(dict(start=run_start, end=j-1, union=run_union,
                                     complete=(run_union == target)))
                    run_start = None
                    run_union = 0
            assert run_start is None
            crossing = [i for i, run in enumerate(runs) if run['start'] < M <= run['end']]
            assert len(crossing) == 1
            crossing_index = crossing[0]
            complete = [i for i, run in enumerate(runs) if run['complete']]
            assert complete, ('cyclic upper target absent', target)
            target_bits = bits(target)
            all_minimal = []
            for i in complete:
                data = minimal_witnesses(runs[i]['start'], runs[i]['end'], target_bits, owner_bits)
                runs[i].update(data)
                all_minimal.extend([i, a, b] for a, b in data['minimal_witnesses'])
            retained = [[i, a, b] for i, a, b in all_minimal if not (a < M <= b)]
            # The coordinate-extreme classification is independent of choosing
            # a retained witness from the complete minimal-witness catalogue.
            if not runs[crossing_index]['complete']:
                reason = 'crossing_compatible_run_incomplete'
                predicted_safe = True
            elif len(complete) >= 2:
                reason = 'another_complete_compatible_run'
                predicted_safe = True
            else:
                run = runs[crossing_index]
                left_survives = run['earliest_completion'] < M
                right_survives = run['latest_covering_start'] >= M
                predicted_safe = left_survives or right_survives
                if left_survives and right_survives:
                    reason = 'unique_run_both_extremal_sides_survive'
                elif left_survives:
                    reason = 'unique_run_left_extremal_witness'
                elif right_survives:
                    reason = 'unique_run_right_extremal_witness'
                else:
                    reason = 'FATAL_unique_run_core_contains_supplied_cut'
            assert predicted_safe == bool(retained)
            source_witness = None
            if retained:
                block, left, right = retained[0]
                shift = M if left >= M else 0
                owner_left, owner_right = left-shift, right-shift
                assert 0 <= owner_left <= owner_right < M
                assert union_range(U, owner_left, owner_right+1) == target
                source_left = owner_left
                source_right = owner_right + Q + 1  # exclusive endpoint
                assert 0 <= source_left < source_right <= len(A)
                assert union_range(A, source_left, source_right) == target
                source_witness = dict(owner_interval=[owner_left, owner_right+1],
                                      actual_source_interval=[source_left, source_right])
            else:
                failures.append(target)
            reasons[reason] += 1
            counts['compatible_runs'] += len(runs)
            counts['complete_compatible_runs'] += len(complete)
            counts['minimal_witnesses'] += len(all_minimal)
            counts['retained_minimal_witnesses'] += len(retained)
            summary = dict(target=target, rank=target.bit_count(), reason=reason,
                           compatible_runs=len(runs), complete_runs=len(complete),
                           minimal_witnesses=len(all_minimal), retained_minimal_witnesses=len(retained),
                           crossing_run_index=crossing_index, source_witness=source_witness)
            summaries.append(summary)
            json.dump(dict(**summary, enumeration_anchor=anchor, runs=runs), stream,
                      separators=(',', ':'))
            stream.write('\n')
    report = dict(
        status=('PASS_ONE_SUPPLIED_CUT_ALL_255_TARGETS' if not failures
                else 'FIXED_CUT_UPPER_TARGET_FAILURES'),
        scope='Exactly one supplied phase and the255 proper supersets of its removed upper-edge colour; no cut search or word edit.',
        word_sha256=WORD_SHA, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        period=M, source_collar=Q, fixed_owner_cut=[M-1, 0],
        last_owner=U[-1], first_owner=U[0], removed_edge_colour=V,
        target_count=len(targets), survival_reasons=dict(reasons), totals=dict(counts),
        failed_targets=failures, target_summaries=summaries,
        nonfilter_targets='Automatically retain an old owner witness: any split witness contains both removed-edge endpoint owners.',
        full_ground='Covered by the whole original period.',
        short_targets='All source windows of length<=4 are present in C+C[:3].',
        resource_caps=dict(cpu_seconds=60, wall_seconds=90, address_space_bytes=2*1024**3,
                           per_file_bytes=256*1024**2),
        host=platform.node(), elapsed_seconds=time.monotonic()-began)
    (args.out / 'single_cut_255_target_certificate.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report[key] for key in
                     ('status', 'removed_edge_colour', 'survival_reasons', 'totals', 'failed_targets',
                      'elapsed_seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
