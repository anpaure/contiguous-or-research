#!/usr/bin/env python3
"""Explore the Johnson-distance census of one coherent FIFO tour."""

from collections import Counter, defaultdict
from itertools import permutations
from math import comb


def targets(b: int, x: int = 0):
    """Return ((empty, doubled), actual b-set mask) for the natural cyclic order."""
    out = []
    state = x
    # Ground points are (pair, bit), encoded as 2*pair+bit.
    for s in range(b):
        j = s
        for t in range(1, b):
            i = (s + t) % b
            mask = (1 << (2 * i)) | (1 << (2 * i + 1))
            for q in range(1, b):
                k = (s + q) % b
                if k == i:
                    continue
                bit = ((state >> k) & 1) ^ (q < t)
                mask |= 1 << (2 * k + bit)
            out.append(((j, i), mask))
        # A packet flips every nonspecial bit.
        state ^= ((1 << b) - 1) ^ (1 << j)
    return out


def adjacent_tokens(b: int, x: int = 0):
    lower, middle, upper = [], [], []
    state = x
    for s in range(b):
        j = s
        for t in range(1, b):
            i = (s + t) % b
            lo = 0
            for q in range(1, b):
                k = (s + q) % b
                bit = ((state >> k) & 1) ^ (q < t)
                lo |= 1 << (2 * k + bit)
            mid = lo | (1 << (2 * i + (1 - ((state >> i) & 1))))
            # The middle already contains both bits at i. Add the next
            # emitted point (or the retained special point at packet end).
            if t < b - 1:
                k = (s + t + 1) % b
                old_bit = (state >> k) & 1
                up = mid | (1 << (2 * k + (1 - old_bit)))
            else:
                up = mid | (1 << (2 * s + ((state >> s) & 1)))
            lower.append(lo)
            middle.append(mid)
            upper.append(up)
        state ^= ((1 << b) - 1) ^ (1 << j)
    return lower, middle, upper


def targets_order(b: int, order, x: int = 0):
    out = []
    state = x
    for s in range(b):
        j = order[s]
        for t in range(1, b):
            i = order[(s + t) % b]
            mask = (1 << (2 * i)) | (1 << (2 * i + 1))
            for q in range(1, b):
                k = order[(s + q) % b]
                if k == i:
                    continue
                bit = ((state >> k) & 1) ^ (q < t)
                mask |= 1 << (2 * k + bit)
            out.append(((j, i), mask))
        state ^= ((1 << b) - 1) ^ (1 << j)
    return out


def support_duplicates_fixed_pairing(b: int):
    multiplicities = Counter()
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        for x in range(1 << b):
            support = tuple(sorted(mask for _, mask in targets_order(b, order, x)))
            multiplicities[support] += 1
    return Counter(multiplicities.values())


def census(b: int):
    ts = targets(b)
    low, mid, up = adjacent_tokens(b)
    assert [mask for _, mask in ts] == mid
    print(" adjacent distinct", len(set(low)), len(set(mid)), len(set(up)))
    assert len(ts) == b * (b - 1)
    assert len({mask for _, mask in ts}) == len(ts)
    counts = Counter()
    by_type = defaultdict(Counter)
    by_relation = defaultdict(Counter)
    min_pairs = defaultdict(list)
    for a, (ta, A) in enumerate(ts):
        for c, (tc, C) in enumerate(ts):
            d = b - (A & C).bit_count()
            counts[d] += 1
            by_type[ta][d] += 1
            j, i = ta
            ell, k = tc
            if ta == tc:
                rel = "same"
            elif j == ell:
                rel = "same_empty"
            elif i == k:
                rel = "same_double"
            elif j == k and i == ell:
                rel = "reverse"
            elif j == k or i == ell:
                rel = "one_cross"
            elif j == i or ell == k:
                raise AssertionError
            else:
                rel = "disjoint"
            by_relation[rel][d] += 1
            if a != c and d <= 3:
                min_pairs[d].append((ta, tc))
    q = len(ts)
    n = {d: v / q for d, v in sorted(counts.items())}
    ratios = {d: n[d] / comb(b, d) ** 2 for d in n if d}
    print("b", b, "q", q, "n", n)
    print("max ratio", max(ratios.items(), key=lambda z: z[1]))
    print("profiles", len({tuple(sorted(c.items())) for c in by_type.values()}))
    point_pair_counts = Counter()
    point_pair_examples = defaultdict(list)
    for a in range(2 * b):
        for c in range(a + 1, 2 * b):
            val = sum(bool(mask & (1 << a)) and bool(mask & (1 << c)) for _, mask in ts)
            kind = "paired" if a // 2 == c // 2 else "cross"
            point_pair_counts[(kind, val)] += 1
            point_pair_examples[(kind, val)].append((a, c))
    print(" point-pair census", dict(sorted(point_pair_counts.items())))
    if b <= 9:
        base = {mask for _, mask in ts}
        same_x = [x for x in range(1 << b) if {mask for _, mask in targets(b, x)} == base]
        print(" same-x supports", same_x)
    if b <= 11:
        print(" relations", {rel: dict(sorted(c.items())) for rel, c in by_relation.items()})
    for d in range(1, min(4, b + 1)):
        print(" d", d, "ordered total", len(min_pairs[d]), "sample", min_pairs[d][:12])


if __name__ == "__main__":
    for small_b in (3, 5):
        print("fixed-pairing duplicate histogram", small_b,
              support_duplicates_fixed_pairing(small_b))
    for odd_b in range(3, 18, 2):
        census(odd_b)
