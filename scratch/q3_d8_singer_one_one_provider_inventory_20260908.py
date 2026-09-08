"""One bounded h100 inventory of an explicit, mathematically forced provider family.

No LP/CP or full candidate catalogue. Uses the independently replayed skeleton.
"""
import collections
import itertools
import json
import os
import resource
import time

os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
started = time.monotonic()
source = '/tmp/Q3_D8_SINGER_DIFFERENT_PROFILE_SKELETON_CERTIFICATE_20260908_ternarylift.json'
output = '/tmp/Q3_D8_SINGER_ONE_ONE_PROVIDER_INVENTORY_20260908.json'
with open(source) as f:
    skeleton = json.load(f)
power = [3**i for i in range(8)]
cycle = [1, 2, 4, 3, 6, 7, 5]
groups = skeleton['group_orbits']
gid = [None] * 6561
metadata = []
for group in groups:
    for target in group['points']:
        gid[target] = group['id']
    rank_seven = [t for t in group['points']
                  if sum((t // p) % 3 for p in power) == 7]
    representative = rank_seven[0] if rank_seven else group['rep']
    vector = [(representative // p) % 3 for p in power]
    metadata.append(dict(rank=sum(vector), n1=vector.count(1), x0=vector[0],
                         size=group['size'], load=group['load'],
                         positive=skeleton['qweight'][representative] > 0,
                         representative=representative))

one_ids = [i for i, m in enumerate(metadata) if m['rank'] == 7 and m['n1'] == 1]
assert len(one_ids) == 40
one_index = {g: i for i, g in enumerate(one_ids)}
wanted = sum(1 << one_index[g] for g in one_ids if not metadata[g]['load'])
assert wanted.bit_count() == 26

def chain(word):
    assert len(word) == 8 and sorted(collections.Counter(word).values()) == [2] * 4
    value = 0
    states = [0]
    for coordinate in word:
        value += power[coordinate]
        states.append(value)
    return states[1:8]

def candidate(left, right, kind):
    assert set(left).isdisjoint(right) and set(left) | set(right) == set(range(8))
    counts = collections.Counter(gid[a + b] for a in chain(left) for b in chain(right))
    # A generic C7 x complement bundle has 14 physical rows. Its incidence
    # is constant on each target orbit, so this gives exact per-target loads.
    loads = {g: 14 * count // metadata[g]['size'] for g, count in counts.items()}
    assert all((14 * count) % metadata[g]['size'] == 0 for g, count in counts.items())
    mask = 0
    for g in one_ids:
        if loads.get(g, 0):
            mask |= 1 << one_index[g]
    expected = 12 if kind == 'BB' else 2
    assert sum(count for g, count in counts.items()
               if metadata[g]['rank'] == 7 and metadata[g]['n1'] == 1) == expected
    return dict(kind=kind, left=left, right=right, loads=loads, one_mask=mask)

def admissible(candidates):
    loads = collections.Counter()
    for row in candidates:
        loads.update(row['loads'])
    critical_extra = central_extra = 0
    for g, count in loads.items():
        m = metadata[g]
        if not m['positive']:
            continue
        excess = max(0, m['load'] + count - 1)
        if not excess:
            continue
        if m['rank'] == 7 and m['n1'] == 3 and m['x0'] == 2 and m['size'] == 14:
            critical_extra += excess
        elif m['rank'] == 8 and m['n1'] == 4 and m['x0'] == 1 and m['size'] == 14:
            central_extra += excess
        else:
            return False
    return critical_extra <= 1 and central_extra <= 1

bb_all = []
for c, d, e, f, g, h in itertools.permutations(cycle[1:]):
    a = cycle[0]
    bb_all.append(candidate([a,a,0,0,c,c,d,d], [e,e,f,f,g,g,h,h], 'BB'))
assert len(bb_all) == 720
bb = [c for c in bb_all if c['one_mask'].bit_count() == 12
      and c['one_mask'] & ~wanted == 0 and admissible([c])]

ln_all = []
for zero_role in ('A', 'E'):
    for low in itertools.permutations([cycle[1], cycle[2]]):
        for high in itertools.permutations([cycle[3], cycle[4], cycle[6]]):
            F, G = cycle[0], cycle[5]
            C, D, H = high
            if zero_role == 'A':
                A = 0
                B, E = low
            else:
                E = 0
                A, B = low
            row = candidate([A,B,A,B,C,D,C,D], [E,F,E,G,F,H,G,H], 'LN')
            row['zero_role'] = zero_role
            ln_all.append(row)
assert len(ln_all) == 24
ln = [c for c in ln_all if c['one_mask'].bit_count() == 2
      and c['one_mask'] & ~wanted == 0 and admissible([c])]

by_mask = collections.defaultdict(list)
for index, row in enumerate(bb):
    by_mask[row['one_mask']].append(index)
flag_triples = []
compatible_triples = []
for li, left in enumerate(ln):
    residual = wanted ^ left['one_mask']
    for bi, first in enumerate(bb):
        mask = first['one_mask']
        if mask & ~residual:
            continue
        for bj in by_mask.get(residual ^ mask, []):
            if bj <= bi:
                continue
            triple = (bi, bj, li)
            assert (mask | bb[bj]['one_mask'] | left['one_mask']) == wanted
            assert not (mask & bb[bj]['one_mask'])
            flag_triples.append(triple)
            if admissible([first, bb[bj], left]):
                compatible_triples.append(triple)

report = dict(stage='explicit_one_one_provider_inventory',
              raw_BB=len(bb_all), admissible_BB=len(bb),
              raw_LN=len(ln_all), admissible_LN=len(ln),
              admissible_LN_by_zero_role=dict(collections.Counter(c['zero_role'] for c in ln)),
              exact_flag_triples=len(flag_triples),
              positive_compatible_triples=len(compatible_triples),
              elapsed=time.monotonic()-started, certificate=output)
with open(output, 'w') as f:
    json.dump(dict(report=report, metadata=metadata, one_ids=one_ids,
                   wanted=wanted, BB=bb, LN=ln, raw_LN=ln_all,
                   flag_triples=flag_triples,
                   compatible_triples=compatible_triples), f)
print(json.dumps(report), flush=True)
