#!/usr/bin/env python3
"""Standalone exact certificate verification; standard library, h100 only.

Enumerate every interval OR by an ending-suffix recurrence, then check
one ordinary nonwrapping witness for every target by a separate range tree.
No PBBS, construction certificate, solver or imported verifier is used.
"""
import argparse
import gzip
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import signal
import socket
import time


def main():
    assert socket.gethostname().split('.')[0] == 'arboghast', 'Mathematical execution: h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    signal.alarm(45)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('word', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    raw = args.word.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == '7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
    tokens = raw.split()
    assert all(token.isdigit() for token in tokens), 'Expected decimal mask tokens'
    word = [int(token) for token in tokens]
    k = 17
    full = (1 << k) - 1
    assert len(word) == 24313, ('incorrect length', len(word))
    assert all(1 <= letter <= full for letter in word)

    # Inductively, suffix maps every distinct suffix union at this endpoint
    # to a genuine starting position. Keeping one start per union is exact.
    suffix = {}
    witnesses = [None] * (full + 1)
    max_suffixes = 0
    for right, letter in enumerate(word):
        current = {letter: right}
        for previous, left in suffix.items():
            current.setdefault(previous | letter, left)
        assert len(current) <= k
        max_suffixes = max(max_suffixes, len(current))
        for target, left in current.items():
            if witnesses[target] is None:
                witnesses[target] = [left, right]
        suffix = current
    missing = [t for t in range(1, full + 1) if witnesses[t] is None]

    # Independently built tree: inclusive interval query, no suffix states.
    base = 1
    while base < len(word):
        base *= 2
    tree = [0] * (2 * base)
    tree[base:base + len(word)] = word
    for pos in range(base - 1, 0, -1):
        tree[pos] = tree[2 * pos] | tree[2 * pos + 1]

    def range_or(left, right):
        left += base
        right += base + 1
        result = 0
        while left < right:
            if left & 1:
                result |= tree[left]
                left += 1
            if right & 1:
                right -= 1
                result |= tree[right]
            left //= 2
            right //= 2
        return result

    rank_counts = [0] * (k + 1)
    rechecked = 0
    for target in range(1, full + 1):
        if witnesses[target] is None:
            continue
        left, right = witnesses[target]
        assert 0 <= left <= right < len(word)
        assert range_or(left, right) == target, (target, left, right)
        rank_counts[target.bit_count()] += 1
        rechecked += 1
    width = comb(17, 9)
    lower_targets = sum(comb(17, rank) for rank in range(1, 9))
    delay = 0
    while delay * width + delay * (delay + 1) // 2 < lower_targets:
        delay += 1
    assert (width, lower_targets, delay, width + delay) == (24310, 65535, 3, 24313)
    args.output.mkdir(parents=True, exist_ok=True)
    report = dict(status='PASS' if not missing else 'FAIL', dimension=k,
                  length=len(word), sha256=sha,
                  covered=rechecked, missing_count=len(missing), missing_targets=missing,
                  all_letters_nonempty=True, all_witnesses_nonwrapping=True,
                  segment_tree_witnesses_rechecked=rechecked,
                  rank_counts=rank_counts, max_distinct_suffix_unions=max_suffixes,
                  endpoint_lower_bound=width+delay, width=width,
                  lower_rank_targets=lower_targets, optimality_delay=delay,
                  gap_to_endpoint_lower_bound=len(word)-width-delay,
                  witness_indexing='zero-based inclusive',
                  execution_host=socket.gethostname(),
                  elapsed_seconds=time.monotonic()-started,
                  limits=dict(cpu_seconds=30, wall_seconds=45,
                              address_space_bytes=1024**3))
    (args.output/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    with gzip.open(args.output/'all_target_witnesses.json.gz', 'wt', encoding='utf-8') as stream:
        json.dump(dict(k=k, sha256=sha, indexing='zero-based inclusive',
                       witness_by_mask=witnesses), stream, separators=(',', ':'))
    print(json.dumps(report,indent=2),flush=True)
    assert not missing
    assert rank_counts == [0] + [comb(k, rank) for rank in range(1, k+1)]
    assert rechecked == full


if __name__ == '__main__':
    main()
