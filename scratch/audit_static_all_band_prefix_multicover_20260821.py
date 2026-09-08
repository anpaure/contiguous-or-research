#!/usr/bin/env python3
"""Finite audit for the static all-band prefix multicover theorem."""

from itertools import combinations


def layer(n, k):
    out = []
    for c in combinations(range(n), k):
        mask = 0
        for x in c:
            mask |= 1 << x
        out.append(mask)
    return out


def saturate_targets(token_locations, targets, compatible):
    adjacency = [
        [i for i, loc in enumerate(token_locations) if compatible(loc, target)]
        for target in targets
    ]
    owner = [-1] * len(token_locations)

    def augment(j, seen):
        for i in adjacency[j]:
            if seen[i]:
                continue
            seen[i] = True
            if owner[i] < 0 or augment(owner[i], seen):
                owner[i] = j
                return True
        return False

    for j in range(len(targets)):
        assert augment(j, [False] * len(token_locations))

    target_for_token = {}
    for i, j in enumerate(owner):
        if j >= 0:
            target_for_token[i] = targets[j]
    return target_for_token


def audit(n):
    assert n % 2 == 1
    m = (n - 1) // 2
    full = (1 << n) - 1
    middle = layer(n, m)
    w = len(middle)
    chains = [[None] * (n + 1) for _ in range(w)]
    for i, u in enumerate(middle):
        chains[i][m] = u

    upper_middle = layer(n, m + 1)
    central = saturate_targets(
        middle, upper_middle, lambda u, v: (u & v) == u
    )
    assert len(central) == w
    for i in range(w):
        chains[i][m + 1] = central[i]

    for k in range(m, 0, -1):
        loc = [chains[i][k] for i in range(w)]
        targets = layer(n, k - 1)
        chosen = saturate_targets(loc, targets, lambda s, t: (s & t) == t)
        for i, s in enumerate(loc):
            if i in chosen:
                chains[i][k - 1] = chosen[i]
            else:
                chains[i][k - 1] = s & (s - 1)

    for k in range(m + 1, n):
        loc = [chains[i][k] for i in range(w)]
        targets = layer(n, k + 1)
        chosen = saturate_targets(loc, targets, lambda s, t: (s & t) == s)
        for i, s in enumerate(loc):
            if i in chosen:
                chains[i][k + 1] = chosen[i]
            else:
                missing = full ^ s
                chains[i][k + 1] = s | (missing & -missing)

    for i in range(w):
        assert chains[i][0] == 0
        assert chains[i][n] == full
        for k in range(1, n + 1):
            assert chains[i][k - 1] & chains[i][k] == chains[i][k - 1]
            assert chains[i][k].bit_count() == k

    for k in range(n + 1):
        support = {chains[i][k] for i in range(w)}
        assert support == set(layer(n, k))
    assert len({chains[i][m] for i in range(w)}) == w
    assert len({chains[i][m + 1] for i in range(w)}) == w
    return w


if __name__ == "__main__":
    checks = {n: audit(n) for n in (3, 5, 7, 9, 11)}
    print("PASS", checks)
