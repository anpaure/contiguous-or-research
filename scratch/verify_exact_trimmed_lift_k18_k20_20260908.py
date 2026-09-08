#!/usr/bin/env python3
"""Materialize and exhaustively verify one exact trimmed lift; run on h100."""
import argparse
import hashlib
import json
import math
import re
import resource
import signal
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decode_word(raw):
    text = raw.decode('utf-8').strip()
    if text.startswith('['):
        word = json.loads(text)
        require(isinstance(word, list), 'input is not a list')
        require(all(type(x) is int for x in word), 'noninteger input letter')
        return word
    clean = '\n'.join(line.split('#', 1)[0] for line in text.splitlines())
    tokens = [t for t in re.split(r'[\s,]+', clean) if t]
    require(all(re.fullmatch(r'[0-9]+', t) for t in tokens), 'invalid decimal token')
    return [int(t) for t in tokens]


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    signal.alarm(150)
    parser = argparse.ArgumentParser()
    parser.add_argument('source_word', type=Path)
    parser.add_argument('output_directory', type=Path)
    parser.add_argument('--dimension', type=int, required=True)
    parser.add_argument('--source-length', type=int, required=True)
    parser.add_argument('--source-sha256', required=True)
    args = parser.parse_args()
    require(args.dimension in (18, 20), 'this certificate is scoped to k18/k20')
    raw = args.source_word.read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    require(source_hash == args.source_sha256, 'source checksum mismatch')
    source = decode_word(raw)
    old_full = (1 << (args.dimension - 1)) - 1
    require(len(source) == args.source_length and len(source) > 0,
            'incorrect source length')
    require(all(1 <= x <= old_full for x in source), 'invalid source mask')

    # The proven finite lift: old word, the new singleton, all but the
    # last old letter with the new coordinate adjoined.
    new_bit = 1 << (args.dimension - 1)
    constructed = source + [new_bit] + [x | new_bit for x in source[:-1]]
    require(len(constructed) == 2 * len(source), 'incorrect lift accounting')
    args.output_directory.mkdir(parents=True, exist_ok=True)
    name = f'k{args.dimension}_upper{len(constructed)}'
    output_path = args.output_directory / (name + '.word')
    output_path.write_text('\n'.join(map(str, constructed)) + '\n', encoding='ascii')

    # Verify the actual serialized output body, not just the construction list.
    emitted = output_path.read_bytes()
    word = decode_word(emitted)
    require(word == constructed, 'serialization changed the word')
    full = (1 << args.dimension) - 1
    require(all(1 <= x <= full for x in word), 'zero or out-of-range output mask')

    suffix = {}
    witness = {}
    for endpoint, letter in enumerate(word):
        current = {letter: endpoint}
        for previous, start in suffix.items():
            current.setdefault(previous | letter, start)
        require(len(current) <= args.dimension, 'suffix-chain dimension invariant')
        for target, start in current.items():
            witness.setdefault(target, (start, endpoint))
        suffix = current
    missing = [target for target in range(1, full + 1) if target not in witness]

    # Independent literal range-OR implementation, built from the emitted word.
    base = 1
    while base < len(word):
        base *= 2
    tree = [0] * (2 * base)
    tree[base:base + len(word)] = word
    for i in range(base - 1, 0, -1):
        tree[i] = tree[2 * i] | tree[2 * i + 1]

    def range_or(left, right):
        left += base
        right += base + 1
        target = 0
        while left < right:
            if left & 1:
                target |= tree[left]
                left += 1
            if right & 1:
                right -= 1
                target |= tree[right]
            left //= 2
            right //= 2
        return target

    for target, (left, right) in witness.items():
        require(1 <= target <= full, 'invalid target mask')
        require(0 <= left <= right < len(word), 'nonordinary witness endpoints')
        require(range_or(left, right) == target, 'independent range-OR mismatch')

    k = args.dimension
    s = (k + 1) // 2
    width = math.comb(k, s)
    lower_targets = sum(math.comb(k, j) for j in range(1, s))
    delay = 0
    while delay * width + delay * (delay + 1) // 2 < lower_targets:
        delay += 1
    lower_bound = width + delay
    gap = len(word) - lower_bound
    with localcontext() as ctx:
        ctx.prec = 32
        percent = str(Decimal(100 * gap) / Decimal(lower_bound))
    report = {
        'status': 'PASS' if not missing else 'FAIL',
        'dimension': k,
        'construction': 'source + new singleton + new-bit-adjoined source[:-1]',
        'source_length': len(source),
        'source_sha256': source_hash,
        'length': len(word),
        'word_file': output_path.name,
        'word_sha256': hashlib.sha256(emitted).hexdigest(),
        'distinct_nonempty_targets': len(witness),
        'required_nonempty_targets': full,
        'missing_count': len(missing),
        'missing_targets': missing,
        'rank_census': dict(sorted(Counter(t.bit_count() for t in witness).items())),
        'all_letters_nonzero': True,
        'ordinary_interval_witnesses_rechecked_by_segment_tree': len(witness),
        'witness_indexing': 'zero-based inclusive endpoints',
        'width': width,
        'lower_endpoint_bound': lower_bound,
        'lower_bound_delay': delay,
        'gap_above_lower_bound': gap,
        'percent_above_lower_bound': percent,
        'execution_limits': {'cpu_seconds': 120, 'wall_seconds': 150,
                             'address_space_bytes': 2 * 1024**3},
    }
    (args.output_directory / (name + '_verification.json')).write_text(
        json.dumps(report, indent=2) + '\n', encoding='ascii')
    print(json.dumps(report, separators=(',', ':')))
    require(not missing, 'lifted word is not universal')


if __name__ == '__main__':
    main()
