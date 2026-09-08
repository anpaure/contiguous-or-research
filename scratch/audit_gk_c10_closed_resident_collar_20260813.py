#!/usr/bin/env python3
"""Exact finite audit of the closed resident five-hinge GK C10 collar.

Run substantive instances on h100.  The script checks set identities,
owner/q1 simplicity, positive depth-d residence, topology, and complete
cyclic owner-interval deck inclusion.
"""

from collections import Counter


def union_interval(word, start, length):
    out = frozenset()
    n = len(word)
    for j in range(length):
        out = out | word[(start + j) % n]
    return out


def owner_cycle(source, d):
    return [union_interval(source, i, d + 1) for i in range(len(source))]


def cyclic_deck(cycles):
    deck = set()
    for cyc in cycles:
        n = len(cyc)
        for start in range(n):
            acc = frozenset()
            for length in range(1, n + 1):
                acc = acc | cyc[(start + length - 1) % n]
                deck.add(acc)
    return deck


def q1_colours(cycles):
    lowers = []
    uppers = []
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            if len(a ^ b) != 2:
                raise AssertionError(("non-Johnson", a, b))
            lowers.append(a & b)
            uppers.append(a | b)
    return lowers, uppers


def assert_positive_residence(cycles, d, ground):
    for cyc in cycles:
        n = len(cyc)
        for x in ground:
            trace = [x in a for a in cyc]
            if all(trace) or not any(trace):
                continue
            starts = [i for i in range(n) if trace[i] and not trace[i - 1]]
            for start in starts:
                length = 0
                while trace[(start + length) % n]:
                    length += 1
                assert length >= d + 1, ("short run", x, length, d, trace)


def screens(m):
    alpha, beta, z, u, v, w = 0, 1, m - 1, 2 * m - 2, 2 * m - 1, 2 * m
    X = [
        {z, u, v},
        {alpha, z, u},
        {alpha, beta, z},
        {alpha, z, v},
        {z, v, w},
    ]
    Y = [
        {u, v, w},
        {alpha, u, v},
        {alpha, beta, u},
        {alpha, beta, v},
        {alpha, v, w},
    ]
    return [frozenset(s) for s in X], [frozenset(s) for s in Y]


def audit(m, d):
    assert m >= 5 and 1 <= d <= m - 3
    H = list(range(m, 2 * m - 2))
    fresh = list(range(2, m - 1))
    assert len(H) == m - 2 and len(fresh) == m - 3

    # A deterministic nonempty partition with distinguished x_j in C_j.
    C = [set() for _ in range(d)]
    for j, x in enumerate(H):
        C[j % d].add(x)
    xdel = [min(c) for c in C]
    yadd = fresh[:d]
    Cp = [(c - {x}) | {y} for c, x, y in zip(C, xdel, yadd)]
    C = [frozenset(c) for c in C]
    Cp = [frozenset(c) for c in Cp]

    X, Y = screens(m)
    assert len(set(X + Y)) == 10
    for i in range(5):
        assert (X[i] | Y[i]) == (X[i - 1] | Y[i])
        assert (X[i] & Y[(i + 1) % 5]) == (X[i] & Y[i])

    # P_i begins at Y_i and ends at the common-history cut after X_i,C.
    P = [[Y[i], *Cp, X[i], *C] for i in range(5)]
    old_sources = P
    new_source = [letter for i in range(5) for letter in P[i]]

    old = [owner_cycle(src, d) for src in old_sources]
    new = [owner_cycle(new_source, d)]
    old_owners = Counter(a for cyc in old for a in cyc)
    new_owners = Counter(a for cyc in new for a in cyc)
    assert old_owners == new_owners
    assert len(old_owners) == 5 * (2 * d + 2)

    old_l, old_u = q1_colours(old)
    new_l, new_u = q1_colours(new)
    assert Counter(old_l) == Counter(new_l)
    assert Counter(old_u) == Counter(new_u)
    assert len(set(old_l)) == len(old_l)
    assert len(set(old_u)) == len(old_u)
    assert len(set(new_l)) == len(new_l)
    assert len(set(new_u)) == len(new_u)

    ground = set(range(2 * m + 1))
    assert_positive_residence(old, d, ground)
    assert_positive_residence(new, d, ground)

    old_deck = cyclic_deck(old)
    new_deck = cyclic_deck(new)
    assert old_deck <= new_deck, ("deck casualties", len(old_deck - new_deck))
    return len(old_owners), len(old_deck), len(new_deck)


def main():
    cases = 0
    max_atoms = 0
    for m in range(5, 18):
        for d in range(1, m - 2):
            atoms, _, _ = audit(m, d)
            cases += 1
            max_atoms = max(max_atoms, atoms)
    print(
        "PASS_GK_C10_CLOSED_RESIDENT_COLLAR",
        f"cases={cases}",
        "m=5..17",
        "d=1..m-3",
        f"max_atoms={max_atoms}",
        "owners=q1=simple",
        "residence>=d+1",
        "topology=5_to_1",
        "Deck_cyc(old)<=Deck_cyc(new)",
    )


if __name__ == "__main__":
    main()
