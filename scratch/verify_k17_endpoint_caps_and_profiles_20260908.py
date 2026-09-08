#!/usr/bin/env python3
"""REVIEW BEFORE RUN: one fixed endpoint-cap family, h100 only.

Exactly the supplied optimal k17 word, all pair-preserving endpoint caps,
and the first/last/both singleton variants. No interior edit or search.
"""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from array import array
from pathlib import Path


def update(state, letter):
    return (letter,) + tuple(block & ~letter for block in state if block & ~letter)


def encode(word):
    return "".join(f"{letter}\n" for letter in word).encode("ascii")


def full_literal_check(word):
    """Ending-OR completeness plus independent interval-tree witness replay."""
    full = (1 << 17) - 1
    left = array("i", [-1]) * (full + 1)
    right = array("i", [-1]) * (full + 1)
    suffix = {}
    for end, letter in enumerate(word):
        assert 0 < letter <= full
        fresh = {letter: end}
        for value, start in suffix.items():
            value |= letter
            if start > fresh.get(value, -1):
                fresh[value] = start
        suffix = fresh
        for target, start in fresh.items():
            if left[target] < 0:
                left[target], right[target] = start, end
    assert all(left[target] >= 0 for target in range(1, full + 1))
    size = 1
    while size < len(word):
        size <<= 1
    tree = [0] * (2 * size)
    tree[size:size + len(word)] = word
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2*i] | tree[2*i+1]
    for target in range(1, full + 1):
        l, r, value = left[target] + size, right[target] + size + 1, 0
        while l < r:
            if l & 1:
                value |= tree[l]
                l += 1
            if r & 1:
                r -= 1
                value |= tree[r]
            l >>= 1
            r >>= 1
        assert value == target
    return dict(ending_or_targets=full, independent_interval_witnesses_replayed=full)


def endpoint_family(word, orientation, out):
    old, previous = word[-1], word[-2]
    forced = old & ~previous
    interior_duplicates = [i for i in range(1, len(word)-1) if word[i] == old]
    assert forced and interior_duplicates
    before = ()
    for letter in word[:-1]:
        before = update(before, letter)
    original_state = update(before, old)
    all_caps = []
    cap = old
    while cap:
        if cap & forced == forced:
            state = update(before, cap)
            assert previous | cap == previous | old
            profile = [b.bit_count() for b in state]
            expected = [cap.bit_count(), (previous | old).bit_count()-cap.bit_count()] + [b.bit_count() for b in original_state[2:]]
            assert profile == expected
            # Equality of every longer suffix follows from the preserved pair;
            # verify the actual recency prefix masks from the second onward.
            old_prefix, new_prefix = old, cap
            for a,b in zip(original_state[1:],state[1:]):
                old_prefix |= a
                new_prefix |= b
                assert old_prefix == new_prefix
            assert len(state) == len(original_state)
            all_caps.append(dict(mask=cap,rank=cap.bit_count(),terminal_blocks=list(state),profile=profile,
                                 coverage_certified_by_endpoint_lemma=True))
        cap = (cap-1) & old
    all_caps.sort(key=lambda item:(item['rank'],item['mask']))
    representatives = []
    used = set()
    for item in all_caps:
        if item['rank'] in used:
            continue
        used.add(item['rank'])
        changed = word[:-1]+[item['mask']]
        raw = encode(changed)
        filename=f"{orientation}_last_cap_size{item['rank']}.word"
        (out/filename).write_bytes(raw)
        representatives.append(dict(rank=item['rank'],mask=item['mask'],profile=item['profile'],
                                    word=filename,sha256=hashlib.sha256(raw).hexdigest()))
    return dict(orientation=orientation,old_endpoint=old,neighbor=previous,
                forced_mask=forced,interior_duplicate_positions_zero_based=interior_duplicates,
                original_terminal_blocks=list(original_state),original_profile=[b.bit_count() for b in original_state],
                all_caps=all_caps,representatives_by_size=representatives)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    assert platform.node().split('.')[0]=='arboghast','h100 only'
    resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    resource.setrlimit(resource.RLIMIT_AS,(128*1024**2,128*1024**2))
    signal.alarm(15)
    started=time.monotonic()
    raw=args.input.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9'
    word=[int(line) for line in raw.decode('ascii').splitlines() if line.strip()]
    assert len(word)==24313 and all(0<a<(1<<17) for a in word)
    args.out.mkdir(parents=True,exist_ok=False)
    normal=endpoint_family(word,'normal',args.out)
    reverse=endpoint_family(list(reversed(word)),'reversed',args.out)
    assert normal['forced_mask']==16 and reverse['forced_mask']==2
    assert len(normal['all_caps'])==16 and len(reverse['all_caps'])==8
    for family in (normal,reverse):
        for item in family['all_caps']:
            s=item['rank']
            assert item['profile']==[s,7-s]+[1]*10
    variants=[]
    for name,first,last in [('first_singleton',reverse['forced_mask'],word[-1]),
                            ('last_singleton',word[0],normal['forced_mask']),
                            ('both_singletons',reverse['forced_mask'],normal['forced_mask'])]:
        candidate=word.copy();candidate[0]=first;candidate[-1]=last
        assert candidate[0]|candidate[1]==word[0]|word[1]
        assert candidate[-2]|candidate[-1]==word[-2]|word[-1]
        assert word[0] in candidate[1:-1] and word[-1] in candidate[1:-1]
        filename=f'k17_optimal24313_{name}.word'
        encoded=encode(candidate);(args.out/filename).write_bytes(encoded)
        check=full_literal_check(candidate)
        variants.append(dict(name=name,word=filename,length=len(candidate),first=first,last=last,
                             sha256=hashlib.sha256(encoded).hexdigest(),**check))
    report=dict(status='PASS',source_sha256=hashlib.sha256(raw).hexdigest(),source_length=len(word),
                normal_last_family=normal,reversed_last_family=reverse,verified_singleton_variants=variants,
                scope='Only endpoint caps retaining the adjacent pair; no interior changes or search.',
                resource_caps=dict(cpu_seconds=10,wall_seconds=15,address_space_bytes=128*1024**2),
                elapsed_seconds=time.monotonic()-started,host=platform.node())
    (args.out/'endpoint_caps_and_terminal_profiles_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status=report['status'],normal_endpoint=normal['old_endpoint'],normal_neighbor=normal['neighbor'],
                         normal_forced=normal['forced_mask'],normal_cap_count=len(normal['all_caps']),
                         normal_profiles=[r['profile'] for r in normal['representatives_by_size']],
                         reversed_endpoint=reverse['old_endpoint'],reversed_neighbor=reverse['neighbor'],
                         reversed_forced=reverse['forced_mask'],reversed_cap_count=len(reverse['all_caps']),
                         reversed_profiles=[r['profile'] for r in reverse['representatives_by_size']],
                         variants=variants,elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)


if __name__=='__main__':
    main()
