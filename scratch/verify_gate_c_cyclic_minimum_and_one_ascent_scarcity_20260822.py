#!/usr/bin/env python3
"""Finite audit for cyclic-minimum intersections and one-ascent scarcity."""

from collections import Counter
from itertools import combinations, permutations
from math import comb


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def bracket(mask, n):
    stack = []
    zeros = []
    for position in range(n):
        if mask & (1 << position):
            stack.append(position)
        elif stack:
            stack.pop()
        else:
            zeros.append(position)
    return tuple(zeros), tuple(stack)


def is_dyck(mask, n):
    height = 0
    first_return = None
    for position in range(n):
        height += 1 if mask & (1 << position) else -1
        if height < 0:
            return False, None
        if height == 0 and first_return is None:
            first_return = position + 1
    return height == 0, first_return


def is_primitive_dyck(mask, n):
    dyck, first_return = is_dyck(mask, n)
    return dyck and first_return == n


def repaired_factor(b):
    """Construct the Catalan-switched central factor."""
    n = 2 * b
    flags = set()
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        zeros, ones = bracket(middle, n)
        if not zeros:
            continue
        p, q = ones[0], zeros[-1]
        lower = middle ^ (1 << p)
        upper = middle | (1 << q)
        if (p, q) == (n - 1, 0):
            middle = lower | 1
        flags.add((lower, middle, upper))
    assert len(flags) == comb(n, b - 1)
    return flags


def criterion(flag, b):
    """Theorem 1.1's cyclic-Dyck membership test."""
    lower, middle, upper = flag
    n = 2 * b
    p = (middle ^ lower).bit_length() - 1
    q = (upper ^ middle).bit_length() - 1
    rotated = 0
    for offset in range(n):
        if middle & (1 << ((p + offset) % n)):
            rotated |= 1 << offset
    dyck, first_return = is_dyck(rotated, n)
    original = (
        q < p
        and (p, q) != (n - 1, 0)
        and dyck
        and first_return == n - p + q + 1
    )
    switched = (
        (p, q) == (0, n - 1)
        and is_primitive_dyck(middle, n)
    )
    assert not (original and switched)
    return original or switched


def canonical_tour_flags(b):
    """Internal coherent flags in coordinates 2j,2j+1."""
    flags = []
    state = 0
    all_bits = (1 << b) - 1
    for s in range(b):
        for t in range(1, b):
            lower = 0
            for u in range(1, b):
                pair = (s + u) % b
                bit = ((state >> pair) & 1) ^ (u < t)
                lower |= 1 << (2 * pair + bit)
            doubled = (s + t) % b
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
            flags.append((lower, middle, upper))
        state ^= all_bits ^ (1 << s)
    return tuple(flags)


def relabel_mask(mask, mapping):
    answer = 0
    while mask:
        bit = (mask & -mask).bit_length() - 1
        answer |= 1 << mapping[bit]
        mask &= mask - 1
    return answer


def relabel_canonical(cycle, b, phase):
    n = 2 * b
    shifted = cycle[phase:] + cycle[:phase]
    mapping = [None] * n
    for j in range(b):
        mapping[2 * j] = shifted[j]
        mapping[2 * j + 1] = shifted[j + b]
    return tuple(
        tuple(relabel_mask(mask, mapping) for mask in flag)
        for flag in canonical_tour_flags(b)
    )


def template_flags(cycle, b, phase):
    """Equations (2.1)--(2.2)."""
    n = 2 * b
    flags = []
    for s in range(b):
        offset = (phase + s * (b + 1)) % n
        for t in range(1, b):
            indices = [
                (offset + u) % n
                for u in (*range(t, b), *range(b + 1, b + t + 1))
            ]
            middle = mask_of(cycle[index] for index in indices)
            r = (offset + b + t) % n
            p = cycle[r]
            q = cycle[(r + 1) % n]
            flags.append((middle ^ (1 << p), middle, middle | (1 << q)))
    return tuple(flags)


def audit_factor_criterion(b):
    n = 2 * b
    factor = repaired_factor(b)
    assert all(criterion(flag, b) for flag in factor)
    assert all(
        ((middle ^ lower).bit_length() - 1) % 2
        != ((upper ^ middle).bit_length() - 1) % 2
        for lower, middle, upper in factor
    )

    # Exhaust every possible three-rank flag.
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        for p in chosen:
            for q in range(n):
                if middle & (1 << q):
                    continue
                flag = (middle ^ (1 << p), middle, middle | (1 << q))
                assert criterion(flag, b) == (flag in factor)


def audit_template(b):
    n = 2 * b
    cycles = [
        tuple(range(n)),
        tuple(reversed(range(n))),
        tuple((7 * j + 3) % n for j in range(n))
        if n % 7 else tuple((5 * j + 3) % n for j in range(n)),
    ]
    for cycle in cycles:
        assert len(set(cycle)) == n
        for phase in (0, 1):
            assert template_flags(cycle, b, phase) == relabel_canonical(
                cycle, b, phase
            )
            arcs = Counter()
            for lower, middle, upper in template_flags(cycle, b, phase):
                p = (middle ^ lower).bit_length() - 1
                q = (upper ^ middle).bit_length() - 1
                arcs[(p, q)] += 1
            expected = Counter()
            for j in range(n):
                expected[(cycle[j], cycle[(j + 1) % n])] = (b - 1) // 2
            assert arcs == expected


def cyclic_runs(bits):
    runs = []
    start = 0
    for index in range(1, len(bits) + 1):
        if index == len(bits) or bits[index] != bits[index - 1]:
            runs.append((start, index, bits[index - 1]))
            start = index
    return runs


def odd_internal_runs(mask, n):
    bits = [(mask >> value) & 1 for value in range(1, n)]
    return sum(
        (right - left) % 2
        for left, right, _ in cyclic_runs(bits)
        if left > 0 and right < len(bits)
    )


def same_parity_edges(cycle):
    return sum(
        cycle[j] % 2 == cycle[(j + 1) % len(cycle)] % 2
        for j in range(len(cycle))
    )


def one_ascent_cycle(mask, n):
    chosen = [value for value in range(n - 1, 0, -1) if mask & (1 << value)]
    other = [value for value in range(n - 1, 0, -1) if not mask & (1 << value)]
    return tuple([0, *chosen, *other])


def genuine_one_ascent(mask, n):
    chosen = [value for value in range(1, n) if mask & (1 << value)]
    other = [value for value in range(1, n) if not mask & (1 << value)]
    return bool(other) and min(chosen) < max(other)


def audit_one_ascent(b, compute_overlap):
    n = 2 * b
    h = (b - 1) // 2
    qsize = b * (b - 1)
    factor = repaired_factor(b) if compute_overlap else None
    cycle_set = set()
    genuine_count = 0
    histograms = [Counter(), Counter()]

    for lower_mask in range(1 << (n - 2)):
        mask = (1 << (n - 1)) | (lower_mask << 1)
        cycle = one_ascent_cycle(mask, n)
        cycle_set.add(cycle)
        genuine = genuine_one_ascent(mask, n)
        if genuine:
            genuine_count += 1
        omega = odd_internal_runs(mask, n)
        same = same_parity_edges(cycle)
        assert same >= omega

        if compute_overlap:
            for phase in (0, 1):
                flags = template_flags(cycle, b, phase)
                overlap = sum(flag in factor for flag in flags)
                assert overlap == sum(criterion(flag, b) for flag in flags)
                assert overlap <= qsize - h * same
                if genuine:
                    histograms[phase][overlap] += 1

    assert genuine_count == 2 ** (n - 2) - (n - 1)
    assert len(cycle_set) == genuine_count + 1
    return histograms


def count_words_by_odd_runs(m):
    counts = Counter()
    for mask in range(1 << m):
        bits = [(mask >> value) & 1 for value in range(m)]
        omega = sum(
            (right - left) % 2
            for left, right, _ in cyclic_runs(bits)
            if left > 0 and right < m
        )
        counts[omega] += 1
    return counts


def gf_counts(m):
    """Direct run-composition version of the generating function."""
    counts = Counter()

    def compositions(total, prefix=()):
        if total == 0:
            yield prefix
            return
        for first in range(1, total + 1):
            yield from compositions(total - first, (*prefix, first))

    for lengths in compositions(m):
        internal = lengths[1:-1]
        omega = sum(length % 2 for length in internal)
        counts[omega] += 2
    return counts


def main():
    for b in range(2, 9):
        audit_factor_criterion(b)
    for b in range(3, 16, 2):
        audit_template(b)
    one_ascent_histograms = {}
    for b in range(3, 10, 2):
        one_ascent_histograms[b] = audit_one_ascent(b, compute_overlap=True)
    for m in range(1, 13):
        assert count_words_by_odd_runs(m) == gf_counts(m)

    for b in (3, 5, 7, 9):
        histograms = one_ascent_histograms[b]
        qsize = b * (b - 1)
        summaries = []
        for histogram in histograms:
            best = max(histogram)
            summaries.append(
                (best, histogram[best], sum(v for k, v in histogram.items()
                                            if k >= qsize - 3 * b))
            )
        print(f"b={b}: phase summaries (max, maximizers, >=q-3b) = {summaries}")

    print("PASS: exact D* cyclic-minimum criterion for 2<=b<=8")
    print("PASS: coherent template and h-fold Hamilton arcs for odd 3<=b<=15")
    print("PASS: odd-run obstruction and exact cycle count for odd 3<=b<=9")
    print("PASS: run-composition generating function through word length 12")


if __name__ == "__main__":
    main()
