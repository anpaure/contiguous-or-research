#!/usr/bin/env python3
"""Finite audit for the three-Catalan-bank phase-packet matching.

For b=3,...,10, construct the primal, dual-primitive, and shifted-primitive
banks from MATH_THEOREM_GATE_C_PHASE_PACKET_THREE_CATALAN_BANKS_20260823.md.
The script verifies every packet from its label, pairwise disjointness, the
claimed Catalan count, and the structural separation used in the proof.
"""

from itertools import combinations
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def heights(word):
    h = 0
    out = []
    for bit in word:
        out.append(h)
        h += 1 if bit else -1
    return out


def flaws(word):
    h = 0
    answer = 0
    for bit in word:
        h += 1 if bit else -1
        if not bit and h < 0:
            answer += 1
    return answer


def dyck_words(k):
    for ones in combinations(range(2 * k), k):
        word = tuple(int(i in ones) for i in range(2 * k))
        if flaws(word) == 0:
            yield word


def primitive(word):
    h = 0
    for i, bit in enumerate(word):
        h += 1 if bit else -1
        if h == 0:
            return i == len(word) - 1
    raise AssertionError("balanced word has no return")


def minimum_change_step(word):
    """Return (f(word), added_position, removed_position)."""
    hs = heights(word)
    d0 = sum((not bit) and h == 0 for bit, h in zip(word, hs))
    touching_down = [
        i
        for i, (bit, h) in enumerate(zip(word, hs))
        if (not bit) and h in (0, 1)
    ]
    add = touching_down[d0]
    upper = list(word)
    upper[add] = 1

    hs = heights(upper)
    u1 = sum(bit and h == 1 for bit, h in zip(upper, hs))
    touching_up = [
        i for i, (bit, h) in enumerate(zip(upper, hs)) if bit and h in (0, 1)
    ]
    remove = touching_up[u1 - 1]
    upper[remove] = 0
    return tuple(upper), add, remove


def path_data(word):
    current = word
    states = [frozenset(i for i, bit in enumerate(current) if bit)]
    uppers = []
    adds = []
    removes = []
    for _ in range(sum(word)):
        nxt, add, remove = minimum_change_step(current)
        upper = frozenset(set(states[-1]) | {add})
        assert upper == frozenset(
            set(i for i, bit in enumerate(nxt) if bit) | {remove}
        )
        uppers.append(upper)
        adds.append(add)
        removes.append(remove)
        current = nxt
        states.append(frozenset(i for i, bit in enumerate(current) if bit))
    return states, uppers, adds, removes


def canonical_packet(repeated, omitted, X, Y):
    k = len(X)
    vertices = [frozenset((repeated,) + tuple(X))]
    for i in range(1, k + 1):
        vertices.append(frozenset(tuple(X[i - 1 :]) + tuple(Y[:i])))
    vertices.append(frozenset((repeated,) + tuple(Y)))
    assert omitted not in set().union(*vertices)
    return tuple(vertices)


def mapped(S, order):
    return frozenset(order[i] for i in S)


def add_packet(packets, owners, kind, root, sequence, label, omega):
    repeated, omitted, X, Y = label
    k = len(X)
    assert len(omega) == 2 * k + 2
    assert repeated in omega and omitted in omega and repeated != omitted
    assert len(Y) == k
    assert len(set(X)) == k and len(set(Y)) == k
    assert set(X).isdisjoint(Y)
    assert set(X) | set(Y) == set(omega) - {repeated, omitted}
    assert repeated not in X and repeated not in Y
    assert omitted not in X and omitted not in Y
    assert sequence == canonical_packet(repeated, omitted, X, Y)
    assert len(sequence) == k + 2
    assert len(sequence) == len(set(sequence))
    assert all(
        len(vertex) == k + 1 and vertex <= set(omega) for vertex in sequence
    )
    for position, vertex in enumerate(sequence):
        assert vertex not in owners, (kind, root, position, owners.get(vertex))
        owners[vertex] = (kind, root, position)
    packets.append((kind, root, sequence, label))


def construct(b):
    k = b - 1
    a, p, q = 0, 2 * k, 2 * k + 1
    omega = frozenset(range(2 * k + 2))
    R = frozenset(range(2 * k))
    packets = []
    owners = {}
    data = []

    # Complete primal bank on R, with repeated p and omitted q.
    all_uppers = set()
    for root in dyck_words(k):
        states, uppers, adds, removes = path_data(root)
        assert states[-1] == R - states[0]
        all_uppers.update(uppers)
        sequence = (
            frozenset({p} | set(states[0])),
            *uppers,
            frozenset({p} | set(states[-1])),
        )
        add_packet(
            packets,
            owners,
            "P",
            root,
            sequence,
            (p, q, tuple(removes), tuple(adds)),
            omega,
        )
        data.append((root, states, uppers, adds, removes))
    assert all_uppers == set(map(frozenset, combinations(R, k + 1)))

    # Dual primitive bank, omitting the unique zigzag primitive root.
    zigzag_inner = tuple(bit for _ in range(k - 1) for bit in (1, 0))
    dual_count = 0
    for root, states, uppers, adds, removes in data:
        if not primitive(root) or root[1:-1] == zigzag_inner:
            continue
        assert adds[0] == 2 * k - 1
        assert removes[-1] == a
        U = frozenset((set(states[0]) - {removes[-1]}) | {adds[0]})
        complements = [R - upper for upper in uppers]
        sequence = (
            frozenset({p} | set(R - U)),
            *(frozenset({p, q} | set(Z)) for Z in complements),
            frozenset({q} | set(states[0])),
        )
        add_packet(
            packets,
            owners,
            "Q",
            root,
            sequence,
            (
                removes[-1],
                adds[0],
                tuple(adds[1:]) + (p,),
                (q,) + tuple(removes[:-1]),
            ),
            omega,
        )
        dual_count += 1
    assert dual_count == catalan(k - 1) - 1

    # Shifted primitive bank.  Its ground order is 1,...,2k-1,q; hence q
    # is the first added coordinate of every primitive root.
    shifted_order = tuple(range(1, 2 * k)) + (q,)
    shifted_count = 0
    for root in dyck_words(k):
        if not primitive(root):
            continue
        states, uppers, adds, removes = path_data(root)
        assert adds[0] == 2 * k - 1
        sequence = (
            frozenset({p} | set(mapped(states[0], shifted_order))),
            *(mapped(upper, shifted_order) for upper in uppers),
            frozenset({p} | set(mapped(states[-1], shifted_order))),
        )
        add_packet(
            packets,
            owners,
            "A",
            root,
            sequence,
            (
                p,
                a,
                tuple(shifted_order[i] for i in removes),
                tuple(shifted_order[i] for i in adds),
            ),
            omega,
        )
        shifted_count += 1
    assert shifted_count == catalan(k - 1)

    expected = catalan(b - 1) + 2 * catalan(b - 2) - 1
    assert len(packets) == expected
    assert len(owners) == (b + 1) * expected
    return packets, owners


def main():
    for b in range(3, 11):
        packets, owners = construct(b)
        expected = catalan(b - 1) + 2 * catalan(b - 2) - 1
        assert len(packets) == expected
        print(
            f"b={b}: packets={len(packets)}, vertices={len(owners)}, "
            f"fraction={len(packets) / catalan(b):.9f}"
        )
    print("PASS: three Catalan banks are labelled phase packets and disjoint")


if __name__ == "__main__":
    main()
