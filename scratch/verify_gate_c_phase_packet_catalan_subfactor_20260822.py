#!/usr/bin/env python3
"""Finite audit for the Catalan phase-packet subfactor theorem.

For b=3,...,9 this script constructs every packet in Theorem 5.1, checks
that it has an explicit phase-packet label, checks global vertex
disjointness, and checks the Catalan count.  It also verifies the exact
perfect b=3 and b=5 certificates found by exhaustive search.
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
    ans = 0
    for bit in word:
        if bit:
            h += 1
        else:
            h -= 1
            if h < 0:
                ans += 1
    return ans


def minimum_change_step(word):
    """Return (f(word), added_position, removed_position)."""
    hs = heights(word)
    d0 = sum((not z) and h == 0 for z, h in zip(word, hs))
    touching_down = [
        i for i, (z, h) in enumerate(zip(word, hs))
        if (not z) and h in (0, 1)
    ]
    add = touching_down[d0]
    upper = list(word)
    upper[add] = 1

    hs = heights(upper)
    u1 = sum(z and h == 1 for z, h in zip(upper, hs))
    touching_up = [
        i for i, (z, h) in enumerate(zip(upper, hs))
        if z and h in (0, 1)
    ]
    remove = touching_up[u1 - 1]
    upper[remove] = 0
    return tuple(upper), add, remove


def dyck_words(k):
    for ones in combinations(range(2 * k), k):
        word = tuple(int(i in ones) for i in range(2 * k))
        if flaws(word) == 0:
            yield word


def path_data(word):
    x = word
    states = [frozenset(i for i, bit in enumerate(x) if bit)]
    uppers = []
    adds = []
    removes = []
    for _ in range(sum(word)):
        nxt, add, remove = minimum_change_step(x)
        upper = frozenset(set(states[-1]) | {add})
        assert upper == frozenset(set(i for i, z in enumerate(nxt) if z) | {remove})
        uppers.append(upper)
        adds.append(add)
        removes.append(remove)
        x = nxt
        states.append(frozenset(i for i, bit in enumerate(x) if bit))
    return states, uppers, adds, removes


def canonical_packet(repeated, omitted, X, Y):
    k = len(X)
    out = [frozenset((repeated,) + tuple(X))]
    for i in range(1, k + 1):
        out.append(frozenset(tuple(X[i - 1 :]) + tuple(Y[:i])))
    out.append(frozenset((repeated,) + tuple(Y)))
    assert omitted not in set().union(*out)
    return tuple(out)


def construct(b):
    k = b - 1
    p, q = 2 * k, 2 * k + 1
    R = frozenset(range(2 * k))
    packets = []
    used = set()
    all_upper = set()

    data = []
    for word in dyck_words(k):
        states, uppers, adds, removes = path_data(word)
        assert states[-1] == R - states[0]
        assert set(adds) == R - states[0]
        assert set(removes) == states[0]
        assert len(set(adds + removes)) == 2 * k
        all_upper.update(uppers)
        data.append((word, states, uppers, adds, removes))

        seq = (frozenset({p} | set(states[0])), *uppers,
               frozenset({p} | set(states[-1])))
        labelled = canonical_packet(p, q, removes, adds)
        assert seq == labelled
        assert len(set(seq)) == b + 1
        assert not (set(seq) & used)
        used.update(seq)
        packets.append(seq)

    assert len(all_upper) == comb(2 * k, k + 1)
    assert len(data) == catalan(k)

    zigzag_inner = tuple(z for _ in range(k - 1) for z in (1, 0))
    dual_count = 0
    for word, states, uppers, adds, removes in data:
        # Primitive means the first return is the final coordinate.
        h = 0
        first_return = None
        for i, bit in enumerate(word):
            h += 1 if bit else -1
            if h == 0:
                first_return = i
                break
        if first_return != 2 * k - 1:
            continue
        inner = word[1:-1]
        if inner == zigzag_inner:
            continue
        assert adds[0] == 2 * k - 1
        assert removes[-1] == 0

        U = frozenset((set(states[0]) - {removes[-1]}) | {adds[0]})
        zsets = [R - T for T in uppers]
        seq = (
            frozenset({p} | set(R - U)),
            *(frozenset({p, q} | set(Z)) for Z in zsets),
            frozenset({q} | set(states[0])),
        )
        X = adds[1:] + [p]
        Y = [q] + removes[:-1]
        labelled = canonical_packet(removes[-1], adds[0], X, Y)
        assert seq == labelled
        assert len(set(seq)) == b + 1
        assert not (set(seq) & used)
        used.update(seq)
        packets.append(seq)
        dual_count += 1

    assert dual_count == catalan(k - 1) - 1
    assert len(packets) == catalan(b - 1) + catalan(b - 2) - 1
    assert len(used) == (b + 1) * len(packets)
    return packets


def check_b3_exact_certificate():
    raw = [
        ["010011", "010101", "100011", "100110"],
        ["001011", "011010", "110001", "111000"],
        ["001101", "011001", "100101", "110100"],
        ["000111", "001110", "101001", "101100"],
        ["010110", "011100", "101010", "110010"],
    ]
    edges = [
        frozenset(
            frozenset(i for i, bit in enumerate(word) if bit == "1")
            for word in edge
        )
        for edge in raw
    ]
    all_vertices = set(map(frozenset, combinations(range(6), 3)))
    assert set().union(*edges) == all_vertices
    assert sum(map(len, edges)) == len(all_vertices)

    labels = [
        (3, 2, (0, 4), (5, 1)),
        (5, 3, (0, 1), (2, 4)),
        (1, 4, (0, 3), (5, 2)),
        (5, 1, (0, 2), (3, 4)),
        (2, 5, (0, 4), (1, 3)),
    ]
    for edge, (r, v, X, Y) in zip(edges, labels):
        assert frozenset(canonical_packet(r, v, X, Y)) == edge


def check_b5_exact_extension():
    """The 18-edge Catalan subfactor plus 24 certified residual packets."""
    packets = construct(5)
    labels = [
        (3, 7, (6, 5, 1, 8), (0, 9, 2, 4)),
        (5, 2, (7, 3, 8, 0), (4, 9, 1, 6)),
        (3, 0, (7, 9, 2, 5), (8, 4, 6, 1)),
        (4, 2, (5, 3, 1, 8), (9, 0, 7, 6)),
        (8, 7, (0, 1, 6, 9), (5, 2, 3, 4)),
        (4, 6, (1, 7, 3, 8), (0, 2, 9, 5)),
        (4, 5, (3, 0, 9, 6), (2, 1, 7, 8)),
        (4, 1, (3, 7, 8, 2), (9, 0, 6, 5)),
        (8, 4, (0, 6, 5, 9), (7, 1, 2, 3)),
        (4, 6, (8, 1, 5, 2), (3, 9, 0, 7)),
        (1, 4, (7, 0, 9, 5), (3, 8, 2, 6)),
        (7, 2, (4, 8, 6, 0), (9, 3, 5, 1)),
        (6, 4, (5, 2, 1, 8), (7, 9, 3, 0)),
        (6, 1, (3, 8, 4, 5), (0, 9, 7, 2)),
        (8, 0, (3, 1, 4, 2), (9, 5, 7, 6)),
        (8, 0, (6, 1, 2, 4), (9, 7, 3, 5)),
        (0, 1, (8, 2, 7, 6), (9, 3, 5, 4)),
        (3, 5, (1, 0, 7, 9), (2, 4, 8, 6)),
        (0, 3, (8, 5, 1, 7), (9, 4, 6, 2)),
        (0, 2, (4, 5, 1, 9), (3, 6, 7, 8)),
        (2, 3, (5, 4, 9, 6), (7, 8, 1, 0)),
        (2, 5, (3, 6, 9, 1), (0, 7, 4, 8)),
        (2, 1, (5, 0, 8, 7), (4, 9, 3, 6)),
        (6, 2, (3, 1, 4, 9), (7, 8, 5, 0)),
    ]
    packets.extend(canonical_packet(r, v, X, Y) for r, v, X, Y in labels)
    assert len(packets) == catalan(5) == 42
    vertices = [A for packet in packets for A in packet]
    assert len(vertices) == comb(10, 5)
    assert len(set(vertices)) == comb(10, 5)
    assert set(vertices) == set(map(frozenset, combinations(range(10), 5)))


def main():
    for b in range(3, 10):
        packets = construct(b)
        print(
            f"b={b}: packets={len(packets)}, "
            f"vertices={(b + 1) * len(packets)}, "
            f"fraction={len(packets) / catalan(b):.9f}"
        )
    check_b3_exact_certificate()
    check_b5_exact_extension()
    print("PASS: Catalan subfactor and exact b=3,5 certificates verified")


if __name__ == "__main__":
    main()
