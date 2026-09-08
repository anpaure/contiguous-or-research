#!/usr/bin/env python3
"""Finite identity audit for the clean-package tight-row normal form."""


def audit(R, d, q):
    m = R - 1
    n = 2 * m + 1
    D = tuple(range(0, q))
    C = tuple(range(q, m))
    I = tuple(range(m, m + q))
    S = tuple(range(m + q, n))
    pi = D + C + I + S

    def win(start, length):
        return frozenset(pi[(start + j) % n] for j in range(length))

    def L(t):
        return win(t, m)

    def A(t):
        return win(t - 1, m + 1)

    ground = frozenset(range(n))
    for j in range(q + 1):
        expected = frozenset(C + D[j:] + I[:j])
        assert L(j) == expected
    for t in range(n):
        assert ground - L(t) == A(m + t + 1)
        assert ground - A(t) == L(m + t)

    def changes(indices):
        deleted, inserted = [], []
        for a, b in zip(indices, indices[1:]):
            old, new = A(a), A(b)
            assert len(old - new) == len(new - old) == 1
            deleted.append(next(iter(old - new)))
            inserted.append(next(iter(new - old)))
        return deleted, inserted

    dl, il = changes(list(range(m + 1, m - d - 1, -1)))
    assert dl == list(reversed(S[-(d + 1):]))
    assert il == list(reversed(C[-(d + 1):]))

    dr, ir = changes(list(range(m + q + 1, m + q + d + 3)))
    assert dr == list(S[:d + 1])
    assert ir == list(C[:d + 1])

    ul_d, ul_i = changes(list(range(1, -d - 1, -1)))
    assert ul_d == [I[0]] + list(reversed(C[-d:]))
    assert ul_i == list(reversed(S[-(d + 1):]))

    ur_d, ur_i = changes(list(range(q, q + d + 2)))
    assert ur_d == [D[-1]] + list(C[:d])
    assert ur_i == list(S[:d + 1])

    uowners = {x % n for x in range(-d, q + d + 2)}
    vowners = {x % n for x in range(m - d, m + q + d + 3)}
    assert uowners.isdisjoint(vowners)
    ufacets = {x % n for x in range(-d, q + d + 1)}
    vfacets = {x % n for x in range(m - d, m + q + d + 2)}
    assert ufacets.isdisjoint(vfacets)


def main():
    count = 0
    for d in range(1, 25):
        for R in range(3 * d + 3, 4 * d + 12):
            for q in range(1, d + 1):
                audit(R, d, q)
                count += 1
    print("PASS", count, "parameter triples")


if __name__ == "__main__":
    main()
