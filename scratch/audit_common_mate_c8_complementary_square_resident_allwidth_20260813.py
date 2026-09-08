#!/usr/bin/env python3
"""Literal replay of the complementary-square resident all-width C8 bank."""

from collections import Counter, defaultdict
import sys


def build(m: int, q: int):
    assert q >= 5 and m >= max(q + 8, 2 * q + 2)
    C = [("c", x) for x in range(m - 3)]
    Q = [("q", x) for x in range(4)]
    Z = [("z", x) for x in range(m - 3)]
    a0 = ("a", 0)
    ground = set(C + Q + Z + [a0])
    n = m - 1
    paths = []

    for j in range(4):
        p = C[j]
        t = C[j + q]
        d = Z[-1 - j]
        U = set(C + [a0, Q[j], Q[(j + 1) % 4]])
        missing = [Q[(j + 2) % 4], Q[(j + 3) % 4]]
        alpha = next(x for x in missing if x[1] % 2 == 0)
        beta = next(x for x in missing if x[1] % 2 == 1)

        gamma = [C[(j + s) % len(C)] for s in range(1, len(C))]
        assert gamma[q - 1] == t
        departures = gamma + [a0, Q[j], Q[(j + 1) % 4]]
        arrivals = Z + [alpha, beta]
        forward = [U]
        for x, y in zip(departures, arrivals):
            forward.append((forward[-1] - {x}) | {y})

        B = {p} | (ground - U)
        assert forward[-1] == B
        core_arrivals = [x for x in gamma if x != t]
        special = []
        if j == 3:
            special = [C[1], C[2]]
            core_arrivals = [x for x in core_arrivals if x not in special]
        w = n - q
        first_arrivals = []
        core_iter = iter(core_arrivals)
        for s in range(1, n - 2):
            if s == w:
                first_arrivals.append(Q[j])
            elif j == 3 and s == w + 1:
                first_arrivals.append(C[1])
            elif j == 3 and s == w + 2:
                first_arrivals.append(C[2])
            else:
                first_arrivals.append(next(core_iter))
        assert next(core_iter, None) is None
        return_departures = (
            [x for x in Z if x != d]
            + [Q[(j + 3) % 4], d, Q[(j + 2) % 4]]
        )
        return_arrivals = first_arrivals + [Q[(j + 1) % 4], t, a0]
        ret = [B]
        for x, y in zip(return_departures, return_arrivals):
            ret.append((ret[-1] - {x}) | {y})

        R = set(C + [Q[j], Q[(j + 1) % 4], Q[(j + 2) % 4]])
        assert ret[-2] == R
        assert ret[-1] == U
        paths.append(forward + ret[1:-1])

    owners = Counter()
    lowers = Counter()
    uppers = Counter()
    for path in paths:
        assert len(path) == 2 * n
        for i, owner in enumerate(path):
            nxt = path[(i + 1) % len(path)]
            assert len(owner) == m and len(owner ^ nxt) == 2
            owners[frozenset(owner)] += 1
            lowers[frozenset(owner & nxt)] += 1
            uppers[frozenset(owner | nxt)] += 1
    assert max(owners.values()) == max(lowers.values()) == max(uppers.values()) == 1

    # Exact cyclic run census in the four old cycles.
    for path in paths:
        length = len(path)
        for x in ground:
            bits = [x in owner for owner in path]
            if all(bits) or not any(bits):
                continue
            for value in (False, True):
                starts = [
                    i for i in range(length)
                    if bits[i] == value and bits[i - 1] != value
                ]
                assert len(starts) == 1
                run = 0
                while bits[(starts[0] + run) % length] == value:
                    run += 1
                assert run >= q, (m, q, x, value, run)

    # The switch concatenates output paths 0,1,2,3 into one cycle.
    switched = [owner for path in paths for owner in path]
    length = len(switched)
    for x in ground:
        bits = [x in owner for owner in switched]
        if all(bits) or not any(bits):
            continue
        for value in (False, True):
            starts = [
                i for i in range(length)
                if bits[i] == value and bits[i - 1] != value
            ]
            for start in starts:
                run = 0
                while bits[(start + run) % length] == value:
                    run += 1
                assert run >= q, ("switched", m, q, x, value, run)

    lower_exposure = defaultdict(int)
    for owner in owners:
        for x in owner:
            lower_exposure[frozenset(set(owner) - {x})] += 1
    alpha = max(
        (degree for lower, degree in lower_exposure.items() if lower not in lowers),
        default=0,
    )
    upper_exposure = defaultdict(int)
    for lower in lowers:
        for x in ground - set(lower):
            upper_exposure[frozenset(set(lower) | {x})] += 1
    beta = max(upper_exposure.values(), default=0)
    assert alpha <= 8 and beta <= 8

    # Prefix equality for the four switched incoming sockets.
    for i in range(4):
        R = set(C + [Q[i], Q[(i + 1) % 4], Q[(i + 2) % 4]])
        old_union = set(R)
        new_union = set(R)
        for s in range(n + 1):
            old_union |= paths[i][s]
            new_union |= paths[(i + 1) % 4][s]
            assert old_union == new_union
        assert old_union == ground

    return {
        "m": m,
        "q": q,
        "owners": len(owners),
        "incidence_edges": 2 * len(lowers),
        "alpha": alpha,
        "beta": beta,
    }


if __name__ == "__main__":
    if len(sys.argv) == 3:
        cases = [(int(sys.argv[1]), int(sys.argv[2]))]
    else:
        cases = [(m, max(5, int(m**0.5) + 1)) for m in range(16, 121)]
        cases = [
            (m, q) for m, q in cases
            if m >= max(q + 8, 2 * q + 2)
        ]
    for case in cases:
        print(build(*case))
