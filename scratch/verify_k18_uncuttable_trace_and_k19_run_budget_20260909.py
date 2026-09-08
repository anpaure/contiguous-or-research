#!/usr/bin/env python3
"""One bounded h100 check: exact18 critical witnesses and coupled run budget.

No construction search. Every interior gap is certified to break a unique
rank-nine witness when marked letters are inserted into the fixed trace.
"""
import argparse
import hashlib
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path

SHA18 = '6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5'


def main():
    assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    signal.alarm(45)
    started = time.monotonic()
    ap = argparse.ArgumentParser()
    ap.add_argument('word', type=Path)
    ap.add_argument('out', type=Path)
    args = ap.parse_args()
    raw = args.word.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA18
    word = [int(t) for t in raw.split()]
    assert len(word) == 48623 and all(0 < a < (1 << 18) for a in word)
    args.out.mkdir(parents=True, exist_ok=False)

    # For every distinct suffix OR, retain its greatest possible left endpoint.
    # This is its shortest witness at the current right endpoint. The update
    # takes a maximum over ALL predecessor suffix unions giving the same OR.
    suffix = {}
    endpoint = {}
    target_ends = Counter()
    missing_rank_endpoints = []
    for right, letter in enumerate(word):
        current = {letter: right}
        for old, left in suffix.items():
            target = old | letter
            current[target] = max(current.get(target, -1), left)
        ranked = [(target, left) for target, left in current.items()
                  if target.bit_count() == 9]
        assert len(ranked) <= 1
        if ranked:
            target, latest_left = ranked[0]
            endpoint[right] = (target, latest_left)
            target_ends[target] += 1
        else:
            missing_rank_endpoints.append(right)
        suffix = current

    W = math.comb(18, 9)
    assert W == 48620
    assert len(target_ends) == W and set(target_ends.values()) == {1}
    assert missing_rank_endpoints == [0, 1, 2]
    ranks = Counter(a.bit_count() for a in word)
    assert max(ranks) < 9 and ranks.get(9, 0) == 0
    first_target, first_latest = endpoint[3]
    assert first_latest == 0

    # An insertion after gap c blocks every unmarked witness crossing c.
    # The named target is available at only this one original endpoint;
    # its latest allowed left endpoint still lies at or before that gap.
    with (args.out / 'every_interior_gap_certificate.jsonl').open('w') as stream:
        for cut in range(len(word)-1):
            right = 3 if cut < 3 else cut + 1
            target, latest_left = endpoint[right]
            assert target_ends[target] == 1
            assert latest_left <= cut < right
            value = 0
            for letter in word[latest_left:right+1]:
                value |= letter
            assert value == target
            stream.write(json.dumps([cut, target, right, latest_left]) + '\n')

    # Exact arithmetic for the proved joint endpoint/exit inequalities.
    N19 = 92381
    M = len(word)
    s = 9
    required_rank_s_run_starts = (s+1)*W-N19-(s-1)*M
    zero_rank_s_minimum_trace = ((s+1)*W-N19+s-2)//(s-1)
    assert required_rank_s_run_starts == 4835
    assert zero_rank_s_minimum_trace == 49228
    assert zero_rank_s_minimum_trace-M == 605
    # If the unchanged trace cannot be split, R_z <= 1. The original
    # marked-target capacity gives N >= M+W-s.
    unchanged_trace_lower_bound = M+W-s
    assert unchanged_trace_lower_bound == 97234
    assert unchanged_trace_lower_bound-N19 == 4853

    report = dict(
        status='PASS', word_sha256=SHA18, word_length=M,
        literal_rank_histogram=dict(sorted(ranks.items())),
        rank9_targets=W, all_rank9_endpoint_multiplicities_one=True,
        missing_rank9_endpoints=missing_rank_endpoints,
        first_rank9_target=first_target, first_rank9_endpoint=3,
        first_rank9_latest_left=first_latest,
        interior_gaps_certified=len(word)-1,
        every_gap_blocks_every_witness_of_one_named_target=True,
        target_word_length19=N19,
        rank9_run_starts_required_when_trace_length48623=required_rank_s_run_starts,
        minimum_unmarked_trace_without_rank9_letters=zero_rank_s_minimum_trace,
        extra_unmarked_letters_required=zero_rank_s_minimum_trace-M,
        unchanged_trace_superword_length_lower_bound=unchanged_trace_lower_bound,
        excess_over_B19=unchanged_trace_lower_bound-N19,
        scope='Only insertion of new-coordinate marked letters into the fixed supplied18 trace, and arithmetic consequences of the separately proved joint capacity theorem. No restriction on arbitrary19 words is inferred from this trace obstruction.',
        execution_host=socket.gethostname(),
        limits=dict(cpu_seconds=30, wall_seconds=45, address_space_bytes=1024**3),
        elapsed_seconds=time.monotonic()-started,
    )
    (args.out / 'trace_and_joint_run_budget_certificate.json').write_text(
        json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
