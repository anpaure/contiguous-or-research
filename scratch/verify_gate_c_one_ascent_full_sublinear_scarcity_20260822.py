#!/usr/bin/env python3
"""Finite audit for full-sublinear one-ascent scarcity."""

from collections import Counter
from itertools import combinations
from math import comb, floor, log2


def runs(bits):
    answer = []
    left = 0
    for right in range(1, len(bits) + 1):
        if right == len(bits) or bits[right] != bits[right - 1]:
            answer.append((left, right))
            left = right
    return answer


def odd_internal_runs(bits):
    return sum(
        (right - left) % 2
        for left, right in runs(bits)
        if left > 0 and right < len(bits)
    )


def exhaustive_run_counts(m):
    counts = Counter()
    for mask in range(1 << m):
        bits = tuple((mask >> index) & 1 for index in range(m))
        counts[odd_internal_runs(bits)] += 1
    return counts


def nonconstant_gf_coefficient(m, j):
    remaining = m - j - 2
    if remaining < 0:
        return 0
    total = 0
    for r in range(remaining // 2 + 1):
        tail_degree = remaining - 2 * r
        tail_coefficient = 1 if tail_degree == 0 else 2
        total += 2 * tail_coefficient * comb(r + j, j) * (2 ** r)
    return total


def gf_run_count(m, j):
    return nonconstant_gf_coefficient(m, j) + (2 if j == 0 else 0)


def audit_generating_function():
    for m in range(1, 16):
        actual = exhaustive_run_counts(m)
        expected = Counter({j: gf_run_count(m, j) for j in range(m + 1)})
        expected += Counter()
        assert actual == expected

        for j in range(m + 1):
            r = (m - j - 2) // 2
            if r < 0:
                continue
            coefficient = nonconstant_gf_coefficient(m, j)
            atom = (2 ** r) * comb(r + j, j)
            assert 2 * atom <= coefficient <= 8 * atom
    print("PASS: exact run GF and coefficient sandwich through length 15")


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


def repaired_factor(b):
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


def template_flags(cycle, b, phase):
    n = 2 * b
    flags = []
    for stage in range(b):
        offset = (phase + stage * (b + 1)) % n
        for t in range(1, b):
            indices = [
                (offset + value) % n
                for value in (*range(t, b), *range(b + 1, b + t + 1))
            ]
            middle = mask_of(cycle[index] for index in indices)
            r = (offset + b + t) % n
            p = cycle[r]
            q = cycle[(r + 1) % n]
            flags.append((middle ^ (1 << p), middle, middle | (1 << q)))
    return tuple(flags)


def one_ascent_cycle(mask, n):
    chosen = [value for value in range(n - 1, 0, -1) if mask & (1 << value)]
    other = [value for value in range(n - 1, 0, -1) if not mask & (1 << value)]
    return tuple([0, *chosen, *other])


def same_parity_edges(cycle):
    return sum(
        cycle[index] % 2 == cycle[(index + 1) % len(cycle)] % 2
        for index in range(len(cycle))
    )


def audit_actual_overlap():
    for b in (3, 5):
        n = 2 * b
        qsize = b * (b - 1)
        h = (b - 1) // 2
        factor = repaired_factor(b)
        high_overlap_counts = Counter()
        parity_upper_counts = Counter()

        for lower_mask in range(1 << (n - 2)):
            mask = (1 << (n - 1)) | (lower_mask << 1)
            word = tuple((mask >> position) & 1 for position in range(1, n))
            omega = odd_internal_runs(word)
            cycle = one_ascent_cycle(mask, n)
            same = same_parity_edges(cycle)
            assert same >= omega
            for phase in (0, 1):
                overlap = sum(
                    flag in factor for flag in template_flags(cycle, b, phase)
                )
                assert overlap <= qsize - h * same <= qsize - h * omega
                high_overlap_counts[qsize - overlap] += 1
                parity_upper_counts[h * omega] += 1

        for loss in range(qsize + 1):
            actual_candidates = sum(
                count for actual_loss, count in high_overlap_counts.items()
                if actual_loss <= loss
            )
            parity_candidates = sum(
                count for forced_loss, count in parity_upper_counts.items()
                if forced_loss <= loss
            )
            assert actual_candidates <= parity_candidates
    print("PASS: actual D* overlap is contained in the parity candidate set for b=3,5")


def audit_threshold_values():
    for b in (31, 101, 301):
        m = 2 * b - 1
        k = max(1, floor(b / log2(b)))
        count = sum(gf_run_count(m, j) for j in range(k + 1))
        required_log2 = 2 * b - 2.5 * log2(b)
        assert log2(count) < required_log2
        print(
            f"b={b}, K={k}: log2 candidates={log2(count):.3f}, "
            f"log2(4^b/b^(5/2))={required_log2:.3f}"
        )
    print("PASS: finite b/log b entropy comparison")


if __name__ == "__main__":
    audit_generating_function()
    audit_actual_overlap()
    audit_threshold_values()
