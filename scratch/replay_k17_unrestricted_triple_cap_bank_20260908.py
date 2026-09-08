#!/usr/bin/env python3
"""Independent literal replay of a candidate full capped bank; h100 only."""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from math import comb
from pathlib import Path


def unions(values):
    value = 0
    for x in values:
        value |= x
    return value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--canonical', type=Path, required=True)
    ap.add_argument('--caps', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    assert platform.node().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    signal.alarm(110)
    started = time.monotonic()
    source_raw, caps_raw = args.canonical.read_bytes(), args.caps.read_bytes()
    assert hashlib.sha256(source_raw).hexdigest() == 'fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3'
    canonical = json.loads(source_raw)
    # Candidate schema: {"cycles":[{"cycle":id,"letters":[masks...]}]}.
    candidate = json.loads(caps_raw)
    rows = candidate['cycles'] if isinstance(candidate, dict) else candidate
    proposed = {row['cycle']: row['letters'] for row in rows}
    assert len(rows) == len(proposed) == len(canonical) == 146
    full = (1 << 17) - 1
    witnesses = [None] * (full + 1)
    trees, lengths = {}, {}
    middle8, middle9 = [], []
    triple_checks = 0
    total = 0
    for rec in canonical:
        cid, h = rec['cycle'], min(rec['height'], 3)
        owners = [full ^ a for a in rec['lower_owners']]
        v = len(owners)
        D = []
        for i in range(v):
            value = full
            for j in range(h+1):
                value &= owners[(i+j) % v]
            D.append(value)
        E = proposed[cid]
        assert len(E) == v
        assert all(isinstance(e, int) and 0 < e <= full and (e | d) == d for e, d in zip(E, D))
        if h < 3:
            assert E == D
        else:
            for i in range(v):
                assert unions(E[(i+j) % v] for j in range(3)) == unions(D[(i+j) % v] for j in range(3))
                triple_checks += 1
        for i in range(v):
            a = unions(E[(i-j) % v] for j in range(h))
            b = unions(E[(i-j) % v] for j in range(h+1))
            assert a.bit_count() == 8 and b.bit_count() == 9 and b == owners[i]
            middle8.append(a)
            middle9.append(b)
        total += v
        doubled = E + E
        # Ending-suffix recurrence, retaining a latest start for every union.
        suffixes = []
        for end, letter in enumerate(doubled):
            new = [(letter, end)]
            for value, start in suffixes:
                value |= letter
                if value != new[-1][0]:
                    new.append((value, start))
            suffixes = new
            if end >= v:
                for value, start in new:
                    if start < end-v+1:
                        # Such a suffix covers at least one full cycle and
                        # has the same union as the most recent whole cycle.
                        start = end-v+1
                    if witnesses[value] is None:
                        witnesses[value] = [cid, start % v, end-start+1]
        size = 1
        while size < len(doubled):
            size *= 2
        tree = [0] * (2*size)
        tree[size:size+len(doubled)] = doubled
        for i in range(size-1, 0, -1):
            tree[i] = tree[2*i] | tree[2*i+1]
        trees[cid], lengths[cid] = (size, tree), v
    assert total == comb(17, 8) == 24310
    assert len(set(middle8)) == len(set(middle9)) == total
    missing = [s for s in range(1, full+1) if witnesses[s] is None]
    replays = 0
    for target, witness in enumerate(witnesses):
        if witness is None:
            continue
        cid, start, length = witness
        assert 0 <= start < lengths[cid] and 1 <= length <= lengths[cid]
        size, tree = trees[cid]
        left, right, value = start+size, start+length+size, 0
        while left < right:
            if left & 1:
                value |= tree[left]
                left += 1
            if right & 1:
                right -= 1
                value |= tree[right]
            left //= 2
            right //= 2
        assert value == target
        replays += 1
    args.out.mkdir(parents=True, exist_ok=True)
    report = dict(status='PASS' if not missing else 'INCOMPLETE_COVER', period_positions=total,
                  components=len(canonical), preserved_h3_triples=triple_checks,
                  rank8_and_rank9_endpoint_bijections=True, covered=full-len(missing),
                  missing_masks=missing, independently_rechecked_witnesses=replays,
                  source_sha256=hashlib.sha256(source_raw).hexdigest(),
                  candidate_sha256=hashlib.sha256(caps_raw).hexdigest(),
                  scope='A complete periodic bank is not yet a single cyclic or ordinary optimal word.',
                  resource_caps=dict(cpu_seconds=90, wall_seconds=110, address_space_bytes=2*1024**3),
                  elapsed_seconds=time.monotonic()-started)
    (args.out/'independent_bank_replay.json').write_text(json.dumps(report, indent=2)+'\n')
    (args.out/'cyclic_bank_target_witnesses.json').write_text(json.dumps(witnesses, separators=(',', ':'))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'missing_masks'}, indent=2), flush=True)
    assert not missing, f'{len(missing)} targets missing'


if __name__ == '__main__':
    main()
