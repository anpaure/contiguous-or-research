#!/usr/bin/env python3
"""Explore cyclic shifted primitive Catalan phase-packet banks.

This is an exploratory enumerator, not a proof certificate.  It fixes the
complete primal bank P and the punctured dual bank Q from the audited 7/16
construction, then considers every cyclic shifted bank

    R_j = (j+1,...,2k,1,...,j-1,q),  1 <= j <= 2k,

with repeated coordinate p and every primitive Dyck root of semilength k.
Vertices are represented by bit masks.  The script reports which roots in
each bank survive P union Q, cross-bank conflict counts, and maximum sets of
whole mutually compatible surviving banks.
"""

from collections import defaultdict
from itertools import combinations

from verify_gate_c_phase_packet_three_banks_20260823 import (
    catalan,
    dyck_words,
    path_data,
    primitive,
)


def mask(S):
    answer = 0
    for x in S:
        answer |= 1 << x
    return answer


def mapped_mask(S, order):
    answer = 0
    for i in S:
        answer |= 1 << order[i]
    return answer


def word_string(word):
    return "".join(map(str, word))


def catalog(k):
    """Return fixed vertices and primitive-root path data."""
    p, q = 2 * k, 2 * k + 1
    base = frozenset(range(2 * k))
    zigzag_inner = tuple(bit for _ in range(k - 1) for bit in (1, 0))

    fixed_owner = {}
    primitive_data = []

    def add_fixed(kind, root, position, vertex):
        m = mask(vertex)
        if m in fixed_owner:
            raise AssertionError((kind, word_string(root), position, fixed_owner[m]))
        fixed_owner[m] = (kind, word_string(root), position)

    all_data = []
    for root in dyck_words(k):
        states, uppers, adds, removes = path_data(root)
        all_data.append((root, states, uppers, adds, removes))
        add_fixed("P", root, 0, {p} | set(states[0]))
        for i, upper in enumerate(uppers, 1):
            add_fixed("P", root, i, upper)
        add_fixed("P", root, k + 1, {p} | set(states[-1]))
        if primitive(root):
            primitive_data.append((root, states, uppers, adds, removes))

    for root, states, uppers, adds, removes in primitive_data:
        if root[1:-1] == zigzag_inner:
            continue
        U = (set(states[0]) - {removes[-1]}) | {adds[0]}
        add_fixed("Q", root, 0, {p} | set(base - U))
        for i, upper in enumerate(uppers, 1):
            add_fixed("Q", root, i, {p, q} | set(base - upper))
        add_fixed("Q", root, k + 1, {q} | set(states[0]))

    assert len(primitive_data) == catalan(k - 1)
    return fixed_owner, primitive_data


def shifted_packet(k, j0, datum):
    """Packet for omitted zero-based base coordinate j0."""
    root, states, uppers, adds, removes = datum
    p, q = 2 * k, 2 * k + 1
    order = tuple(range(j0 + 1, 2 * k)) + tuple(range(j0)) + (q,)
    assert len(order) == 2 * k and j0 not in order
    assert adds[0] == 2 * k - 1 and removes[-1] == 0
    return (
        (1 << p) | mapped_mask(states[0], order),
        *(mapped_mask(upper, order) for upper in uppers),
        (1 << p) | mapped_mask(states[-1], order),
    )


def build(k):
    fixed_owner, primitive_data = catalog(k)
    banks = []
    rejected = []
    for j0 in range(2 * k):
        bank = []
        bad = []
        within = set()
        for root_index, datum in enumerate(primitive_data):
            packet = shifted_packet(k, j0, datum)
            assert len(packet) == k + 2 and len(set(packet)) == k + 2
            assert not (set(packet) & within)
            within.update(packet)
            hits = tuple(
                (position, fixed_owner[vertex])
                for position, vertex in enumerate(packet)
                if vertex in fixed_owner
            )
            if hits:
                bad.append((root_index, hits))
            else:
                bank.append((root_index, packet))
        banks.append(bank)
        rejected.append(bad)
    return primitive_data, banks, rejected


def cross_conflicts(banks):
    """Return conflict-edge sets for every pair of banks."""
    occurrence = defaultdict(list)
    for j, bank in enumerate(banks):
        for root_index, packet in bank:
            for position, vertex in enumerate(packet):
                occurrence[vertex].append((j, root_index, position))

    conflicts = defaultdict(set)
    multiplicities = defaultdict(int)
    for owners in occurrence.values():
        for left, right in combinations(owners, 2):
            j, x, _ = left
            ell, y, _ = right
            if j == ell:
                raise AssertionError((j, x, y))
            if j > ell:
                j, ell, x, y = ell, j, y, x
            conflicts[(j, ell)].add((x, y))
            multiplicities[(j, ell)] += 1
    return conflicts, multiplicities


def maximum_whole_bank_sets(banks, conflicts):
    """All maximum independent sets in the graph of conflict-free banks."""
    n = len(banks)
    adjacency = [0] * n
    for (j, ell), edges in conflicts.items():
        if edges:
            adjacency[j] |= 1 << ell
            adjacency[ell] |= 1 << j

    best = []
    best_size = -1

    def search(candidates, chosen):
        nonlocal best_size, best
        if chosen.bit_count() + candidates.bit_count() < best_size:
            return
        if not candidates:
            size = chosen.bit_count()
            if size > best_size:
                best_size = size
                best = [chosen]
            elif size == best_size:
                best.append(chosen)
            return
        v = (candidates & -candidates).bit_length() - 1
        search(candidates & ~(1 << v), chosen)
        search(candidates & ~(1 << v) & ~adjacency[v], chosen | (1 << v))

    search((1 << n) - 1, 0)
    decoded = [tuple(i + 1 for i in range(n) if S >> i & 1) for S in best]
    return best_size, decoded, adjacency


def summarize(b):
    k = b - 1
    primitive_data, banks, rejected = build(k)
    conflicts, multiplicities = cross_conflicts(banks)
    best_size, best_sets, adjacency = maximum_whole_bank_sets(banks, conflicts)
    print(f"b={b}, k={k}, primitive roots={len(primitive_data)}")
    print("survivors after P+Q:", [len(bank) for bank in banks])
    print("rejections:", [len(bad) for bad in rejected])
    print("whole-bank degrees:", [a.bit_count() for a in adjacency])
    print(f"max whole compatible banks={best_size}; examples={best_sets[:20]}")
    print("pair packet-conflict counts (upper triangle):")
    for j in range(2 * k):
        print(
            " ".join(
                "." if ell <= j else str(len(conflicts.get((j, ell), ())))
                for ell in range(2 * k)
            )
        )
    print("rejected roots by bank:")
    for j, bad in enumerate(rejected, 1):
        if not bad:
            continue
        labels = [word_string(primitive_data[x][0]) for x, _ in bad]
        print(j, labels[:30], "..." if len(labels) > 30 else "")
    return primitive_data, banks, rejected, conflicts, multiplicities


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int, nargs="*", default=[3, 4, 5, 6])
    args = parser.parse_args()
    for b in args.b:
        summarize(b)


if __name__ == "__main__":
    main()
