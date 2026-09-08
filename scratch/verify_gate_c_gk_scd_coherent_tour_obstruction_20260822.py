#!/usr/bin/env python3
"""Finite audit for the Greene--Kleitman coherent-tour obstruction."""

from collections import Counter
from itertools import combinations
from math import comb


def mask_of(items):
    ans = 0
    for item in items:
        ans |= 1 << item
    return ans


def gk_middle_flags(b):
    """Return (L,C,U,p,q) for all GK chains crossing b-1,b,b+1."""
    n = 2 * b
    flags = []
    for chosen in combinations(range(n), b):
        C = mask_of(chosen)
        stack = []
        paired = 0
        for position in range(n):
            if C & (1 << position):
                stack.append(position)
            elif stack:
                opener = stack.pop()
                paired |= (1 << opener) | (1 << position)
        unpaired_zero = [i for i in range(n)
                         if not (paired & (1 << i)) and not (C & (1 << i))]
        unpaired_one = [i for i in range(n)
                        if not (paired & (1 << i)) and (C & (1 << i))]
        assert len(unpaired_zero) == len(unpaired_one)
        if not unpaired_zero:
            continue
        assert max(unpaired_zero) < min(unpaired_one)
        q = max(unpaired_zero)
        p = min(unpaired_one)
        L = C ^ (1 << p)
        U = C | (1 << q)
        flags.append((L, C, U, p, q))
    return flags


def audit_gk(b):
    flags = gk_middle_flags(b)
    expected = comb(2 * b, b - 1)
    assert len(flags) == expected
    assert len({L for L, _, _, _, _ in flags}) == expected
    assert len({C for _, C, _, _, _ in flags}) == expected
    assert len({U for _, _, U, _, _ in flags}) == expected
    for L, C, U, p, q in flags:
        assert L.bit_count() == b - 1
        assert C.bit_count() == b
        assert U.bit_count() == b + 1
        assert L & C == L and C & U == C
        assert C ^ L == 1 << p
        assert U ^ C == 1 << q
        assert q < p
    W = comb(2 * b, b)
    assert W - expected == W // (b + 1)


def coherent_internal_flags(b):
    """Construct all internal packet flags of the normalized coherent tour."""
    all_state_bits = (1 << b) - 1
    state = 0
    flags = []
    ending_queues = []
    for s in range(b):
        u = 2 * s + ((state >> s) & 1)
        nonspecial = [(s + r) % b for r in range(1, b)]
        X = [2 * j + ((state >> j) & 1) for j in nonspecial]
        Y = [2 * j + (1 - ((state >> j) & 1)) for j in nonspecial]
        windows = [mask_of([u] + X)]
        for i in range(1, b):
            windows.append(mask_of(X[i - 1:] + Y[:i]))
        windows.append(mask_of(Y + [u]))
        assert len(windows) == b + 1
        ending_queues.append(Y + [u])
        for i in range(1, b):
            C = windows[i]
            L = windows[i - 1] & C
            U = C | windows[i + 1]
            p_mask = C ^ L
            q_mask = U ^ C
            assert p_mask.bit_count() == q_mask.bit_count() == 1
            p = p_mask.bit_length() - 1
            q = q_mask.bit_length() - 1
            flags.append((L, C, U, p, q))
        state ^= all_state_bits ^ (1 << s)
    assert state == 0
    return flags, ending_queues


def audit_tour(b):
    flags, queues = coherent_internal_flags(b)
    qsize = b * (b - 1)
    assert len(flags) == qsize
    arcs = Counter((p, q) for _, _, _, p, q in flags)
    queue_arcs = Counter()
    for queue in queues:
        queue_arcs.update(zip(queue, queue[1:]))
    assert arcs == queue_arcs

    cycle = [2 * j for j in range(b)] + [2 * j + 1 for j in range(b)]
    expected = Counter()
    h = (b - 1) // 2
    for i, p in enumerate(cycle):
        expected[(p, cycle[(i + 1) % (2 * b)])] = h
    assert arcs == expected
    assert sum(arcs.values()) == 2 * b * h == qsize

    # No total order can make all projected arcs descend: the support is a
    # directed Hamilton cycle.
    successor = {p: q for p, q in expected}
    seen = []
    current = cycle[0]
    while current not in seen:
        seen.append(current)
        current = successor[current]
    assert current == cycle[0] and len(seen) == 2 * b


def audit_non_gk_scope_example():
    chains = [
        [0, mask_of([0]), mask_of([0, 3]), mask_of([0, 2, 3]), mask_of(range(4))],
        [mask_of([1]), mask_of([0, 1]), mask_of([0, 1, 3])],
        [mask_of([2]), mask_of([1, 2]), mask_of([0, 1, 2])],
        [mask_of([3]), mask_of([2, 3]), mask_of([1, 2, 3])],
        [mask_of([0, 2])],
        [mask_of([1, 3])],
    ]
    all_sets = [mask for chain in chains for mask in chain]
    assert len(all_sets) == len(set(all_sets)) == 16
    for chain in chains:
        ranks = [mask.bit_count() for mask in chain]
        assert ranks == list(range(ranks[0], 5 - ranks[0]))
        assert all(a & c == a and (c ^ a).bit_count() == 1
                   for a, c in zip(chain, chain[1:]))
    arcs = []
    for chain in chains[:4]:
        middle_index = [mask.bit_count() for mask in chain].index(2)
        L, C, U = chain[middle_index - 1:middle_index + 2]
        p = (C ^ L).bit_length() - 1
        q = (U ^ C).bit_length() - 1
        arcs.append((p, q))
    assert set(arcs) == {(0, 3), (3, 2), (2, 1), (1, 0)}


def main():
    for b in range(2, 11):
        audit_gk(b)
    for b in range(3, 32, 2):
        audit_tour(b)
    audit_non_gk_scope_example()
    print("PASS: GK middle flags are exact, disjoint, and strictly descending for 2<=b<=10")
    print("PASS: coherent flag arcs are h-fold directed Hamilton cycles for odd 3<=b<=31")
    print("PASS: the non-GK B4 scope example is an exact SCD with Hamilton flag projection")


if __name__ == "__main__":
    main()
