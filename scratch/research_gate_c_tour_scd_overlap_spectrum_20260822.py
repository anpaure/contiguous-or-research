#!/usr/bin/env python3
"""Exact/sampled overlap spectrum: coherent-tour flags versus the repaired GK SCD.

This is exploratory.  A directed Hamilton cycle h_0,...,h_(2b-1) determines
the coherent pairing h_j~h_(j+b), hence its internal flag support.  We compare
that support with the Catalan diamond-switched SCD D*.
"""

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial
from random import Random


def mask_of(items):
    ans = 0
    for item in items:
        ans |= 1 << item
    return ans


def bracket(mask, n):
    stack = []
    zeros = []
    for j in range(n):
        if mask & (1 << j):
            stack.append(j)
        elif stack:
            stack.pop()
        else:
            zeros.append(j)
    return tuple(zeros), tuple(stack)


def is_dyck(mask, n):
    height = 0
    for j in range(n):
        height += 1 if mask & (1 << j) else -1
        if height < 0:
            return False
    return height == 0


def repaired_scd_flags(b):
    n = 2 * b
    sources = {}
    for chosen in combinations(range(n - 2), b - 1):
        core = mask_of(chosen)
        if is_dyck(core, n - 2):
            source = (core << 1) | (1 << (n - 1))
            target = (core << 1) | 1
            sources[source] = target

    flags = set()
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        zeros, ones = bracket(middle, n)
        if not zeros:
            continue
        q = zeros[-1]
        p = ones[0]
        lower = middle ^ (1 << p)
        upper = middle | (1 << q)
        if middle in sources:
            middle = sources[middle]
        flags.add((lower, middle, upper))
    assert len(flags) == comb(n, b - 1)
    return flags


def canonical_tour_flags(b):
    """Internal flags in canonical coordinates 2j,2j+1."""
    ans = []
    state = 0
    all_bits = (1 << b) - 1
    for s in range(b):
        packet_middles = []
        packet_lowers = []
        packet_uppers = []
        for t in range(1, b):
            doubled = (s + t) % b
            lower = 0
            for q in range(1, b):
                pair = (s + q) % b
                bit = ((state >> pair) & 1) ^ (q < t)
                lower |= 1 << (2 * pair + bit)
            middle = lower | (
                1 << (2 * doubled + 1 - ((state >> doubled) & 1))
            )
            if t < b - 1:
                nxt = (s + t + 1) % b
                upper = middle | (
                    1 << (2 * nxt + 1 - ((state >> nxt) & 1))
                )
            else:
                upper = middle | (1 << (2 * s + ((state >> s) & 1)))
            packet_middles.append(middle)
            packet_lowers.append(lower)
            packet_uppers.append(upper)
        ans.extend(zip(packet_lowers, packet_middles, packet_uppers))
        state ^= all_bits ^ (1 << s)
    assert len(ans) == b * (b - 1)
    return tuple(ans)


def relabel_mask(mask, mapping):
    ans = 0
    while mask:
        bit = (mask & -mask).bit_length() - 1
        ans |= 1 << mapping[bit]
        mask &= mask - 1
    return ans


def overlap_for_cycle(canonical, cycle, b, factor):
    mapping = [None] * (2 * b)
    for j in range(b):
        mapping[2 * j] = cycle[j]
        mapping[2 * j + 1] = cycle[j + b]
    hits = []
    for idx, flag in enumerate(canonical):
        mapped = tuple(relabel_mask(mask, mapping) for mask in flag)
        if mapped in factor:
            hits.append(idx)
    return tuple(hits)


def exact_audit(b):
    n = 2 * b
    factor = repaired_scd_flags(b)
    canonical = canonical_tour_flags(b)
    hist = Counter()
    joint = Counter()
    best_by_bad = {}
    arc_support = {(p, q) for lower, middle, upper in factor
                   for p in range(n) if middle ^ lower == 1 << p
                   for q in range(n) if upper ^ middle == 1 << q}
    max_examples = []
    best = -1
    for tail in permutations(range(1, n)):
        cycle = (0,) + tail
        hits = overlap_for_cycle(canonical, cycle, b, factor)
        score = len(hits)
        bad = sum(
            (cycle[j], cycle[(j + 1) % n]) not in arc_support
            for j in range(n)
        )
        hist[score] += 1
        joint[(bad, score)] += 1
        best_by_bad[bad] = max(best_by_bad.get(bad, -1), score)
        if score > best:
            best = score
            max_examples = [(cycle, hits)]
        elif score == best and len(max_examples) < 4:
            max_examples.append((cycle, hits))
    assert sum(hist.values()) == factorial(n - 1)
    mean_num = sum(score * count for score, count in hist.items())
    # A random tour has q flags; a full SCD owns fraction 1/[b(b+1)] of
    # all flags, so the exact mean is (b-1)/(b+1).
    assert mean_num * (b + 1) == factorial(n - 1) * (b - 1)
    return hist, best, max_examples, joint, best_by_bad


def sampled_audit(b, trials, seed=20260822):
    n = 2 * b
    factor = repaired_scd_flags(b)
    canonical = canonical_tour_flags(b)
    rng = Random(seed + b)
    hist = Counter()
    best = -1
    example = None
    tail = list(range(1, n))
    for _ in range(trials):
        rng.shuffle(tail)
        cycle = (0,) + tuple(tail)
        hits = overlap_for_cycle(canonical, cycle, b, factor)
        hist[len(hits)] += 1
        if len(hits) > best:
            best = len(hits)
            example = (cycle, hits)
    return hist, best, example


def main():
    for b in (3, 5):
        hist, best, examples, joint, best_by_bad = exact_audit(b)
        print(f"b={b} exact cycles={factorial(2*b-1)} hist={dict(sorted(hist.items()))}")
        print(f"b={b} best={best}/{b*(b-1)} examples={examples[:2]}")
        print(f"b={b} best_by_bad_arc_count={dict(sorted(best_by_bad.items()))}")
        if b == 5:
            print(f"b=5 joint_bad_overlap={dict(sorted(joint.items()))}")
    hist, best, example = sampled_audit(7, 20000)
    print(f"b=7 sample=20000 hist={dict(sorted(hist.items()))}")
    print(f"b=7 sample_best={best}/42 example={example}")


if __name__ == "__main__":
    main()
