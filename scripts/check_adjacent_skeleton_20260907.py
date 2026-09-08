"""Finite checks for the four-uniform adjacent-skeleton incidence counts."""

from collections import Counter
from itertools import combinations


def check(b):
    n = 2 * b
    full = (1 << n) - 1
    lower = [sum(1 << i for i in C) for C in combinations(range(n), b - 1)]
    middle = [sum(1 << i for i in C) for C in combinations(range(n), b)]
    folded = sorted({min(S, full ^ S) for S in middle})
    fold_id = {S: i for i, S in enumerate(folded)}

    def fold(S):
        return fold_id[min(S, full ^ S)]

    lower_id = {S: i for i, S in enumerate(lower)}
    edges = set()
    for i, L in enumerate(lower):
        available = full ^ L
        for J in combinations([x for x in range(n) if available >> x & 1], b - 1):
            Lp = sum(1 << x for x in J)
            j = lower_id[Lp]
            if i >= j:
                continue
            leftover = full ^ (L | Lp)
            x, y = [z for z in range(n) if leftover >> z & 1]
            U, V = fold(L | (1 << x)), fold(L | (1 << y))
            assert U != V
            # The two lower colours of the folded Johnson edge are L,L'.
            S, T = L | (1 << x), L | (1 << y)
            assert {S & T, full ^ (S | T)} == {L, Lp}
            for su in range(2):
                for sv in range(2):
                    edges.add((i, j, len(lower) + 2 * U + su,
                               len(lower) + 2 * V + sv))

    degree = Counter()
    codegree = Counter()
    for edge in edges:
        assert len(set(edge)) == 4
        for v in edge:
            degree[v] += 1
        for x, y in combinations(sorted(edge), 2):
            codegree[x, y] += 1

    lower_degrees = {degree[i] for i in range(len(lower))}
    slot_degrees = {
        degree[len(lower) + i] for i in range(2 * len(folded))
    }
    assert lower_degrees == {2 * b * (b + 1)}
    assert slot_degrees == {2 * b * b}
    assert max(codegree.values()) == 2 * b
    return len(lower), len(folded), len(edges)


def check_bad_geodesic(b):
    n = 2 * b
    full = (1 << n) - 1
    K = sum(1 << i for i in range(b - 3))
    shown = [1 << (b - 3 + i) for i in range(6)]
    one, two, three, four, five, six = shown
    A = K | one | two | three
    B = K | two | three | four
    C = K | three | four | five
    D = K | one | three | five
    path = [A, B, C, D]
    colours = []
    for S, T in zip(path, path[1:]):
        assert (S ^ T).bit_count() == 2
        colours.extend((S & T, full ^ (S | T)))
    assert len(set(colours)) == 6
    assert (A ^ D).bit_count() == 2


def main():
    for b in (3, 4):
        print("b", b, "counts", check(b))
        check_bad_geodesic(b)
    print("PASS: adjacent-skeleton degrees, codegrees, colours, obstruction")


if __name__ == "__main__":
    main()
