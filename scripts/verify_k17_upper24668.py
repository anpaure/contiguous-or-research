#!/usr/bin/env python3
"""Independent literal-word checker. Run mathematical execution on h100.

This checker verifies the supplied24668 word. It enumerates all
suffix unions and independently replays every saved interval witness.
"""
import argparse
import hashlib
import json
import re
import resource
import signal
from collections import Counter
from pathlib import Path


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    signal.alarm(110)
    parser = argparse.ArgumentParser()
    parser.add_argument('word', type=Path)
    parser.add_argument('output_directory', type=Path)
    args = parser.parse_args()
    raw = args.word.read_bytes()
    text = raw.decode('utf-8').strip()
    if text.startswith('['):
        word = json.loads(text)
        assert isinstance(word, list)
        assert all(type(x) is int for x in word)
    else:
        clean = '\n'.join(line.split('#', 1)[0] for line in text.splitlines())
        tokens = [t for t in re.split(r'[\s,]+', clean) if t]
        assert all(re.fullmatch(r'[0-9]+', t) for t in tokens)
        word = [int(t) for t in tokens]
    full = (1 << 17) - 1
    assert len(word) == 24668, ('incorrect length', len(word))
    assert all(1 <= x <= full for x in word), 'zero/out-of-range letter'

    # First calculation: all suffix ORs, with one literal interval each.
    suffix = {}
    witness = {}
    for endpoint, letter in enumerate(word):
        current = {letter: endpoint}
        for previous, start in suffix.items():
            current.setdefault(previous | letter, start)
        assert len(current) <= 17
        for union, start in current.items():
            witness.setdefault(union, (start, endpoint))
        suffix = current
    missing = [target for target in range(1, full + 1) if target not in witness]

    # Second calculation: independent segment-tree OR for every witness.
    base = 1
    while base < len(word):
        base *= 2
    tree = [0] * (2 * base)
    tree[base:base + len(word)] = word
    for i in range(base - 1, 0, -1):
        tree[i] = tree[2*i] | tree[2*i+1]

    def range_or(left, right):
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
            left //= 2
            right //= 2
        return union

    for target, (left, right) in witness.items():
        assert 0 <= left <= right < len(word)
        assert range_or(left, right) == target
    report = {
        'status': 'PASS' if not missing else 'FAIL',
        'input_sha256': hashlib.sha256(raw).hexdigest(),
        'length': len(word), 'dimension': 17,
        'distinct_nonempty_targets': len(witness),
        'missing_count': len(missing), 'missing_targets': missing,
        'rank_census': dict(sorted(Counter(x.bit_count() for x in witness).items())),
        'all_letters_nonempty': True,
        'nonwrapping_witnesses_checked_by_segment_tree': len(witness),
        'witness_indexing': 'zero-based inclusive endpoints',
    }
    args.output_directory.mkdir(parents=True, exist_ok=True)
    (args.output_directory / 'literal24668_verification.json').write_text(
        json.dumps(report, indent=2) + '\n')
    (args.output_directory / 'literal24668_target_witnesses.json').write_text(
        json.dumps({str(t): list(witness[t]) for t in sorted(witness)}) + '\n')
    print(json.dumps(report, separators=(',', ':')))
    assert not missing, 'reported word is not universal'


if __name__ == '__main__':
    main()
