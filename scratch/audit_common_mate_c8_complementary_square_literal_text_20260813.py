#!/usr/bin/env python3
"""Replay the displayed one-neutral-label construction in the theorem text."""

from collections import Counter, defaultdict


def insert_fixed(base, fixed, length):
    """Fill a 1-indexed fixed-position prescription, retaining base order."""
    out = []
    it = iter(base)
    for pos in range(1, length + 1):
        out.append(fixed[pos] if pos in fixed else next(it))
    try:
        next(it)
        raise AssertionError("unused base entry")
    except StopIteration:
        return out


def build(m, q):
    assert q >= 5 and m >= max(q + 8, 2 * q + 2)
    C = [("c", i) for i in range(m - 3)]
    Q = [("q", i) for i in range(4)]
    Z = [("z", i) for i in range(m - 3)]
    a = ("a", 0)
    ground = set(C + Q + [a] + Z)
    n = m - 1
    w = n - q
    paths = []

    for j in range(4):
        p = C[j]
        t = C[j + q]
        d = Z[m - 4 - j]
        U = set(C + [a, Q[j], Q[(j + 1) % 4]])
        missing = [Q[(j + 2) % 4], Q[(j + 3) % 4]]
        alpha = next(x for x in missing if x[1] % 2 == 0)
        beta = next(x for x in missing if x[1] % 2 == 1)

        gamma = [C[(j + s) % len(C)] for s in range(1, len(C))]
        assert gamma[q - 1] == t
        f_dep = gamma + [a, Q[j], Q[(j + 1) % 4]]
        f_arr = Z + [alpha, beta]
        forward = [U]
        for x, y in zip(f_dep, f_arr):
            forward.append((forward[-1] - {x}) | {y})

        B = {p} | (ground - U)
        assert forward[-1] == B

        rho_base = [x for x in gamma if x != t]
        if j < 3:
            rho = insert_fixed(rho_base, {w: Q[j]}, n - 3)
        else:
            rho_base = [x for x in rho_base if x not in {C[1], C[2]}]
            rho = insert_fixed(
                rho_base, {w: Q[j], w + 1: C[1], w + 2: C[2]}, n - 3
            )
        r_dep = [x for x in Z if x != d] + [Q[(j + 3) % 4], d, Q[(j + 2) % 4]]
        r_arr = rho + [Q[(j + 1) % 4], t, a]
        assert len(r_dep) == len(r_arr) == n
        ret = [B]
        for x, y in zip(r_dep, r_arr):
            ret.append((ret[-1] - {x}) | {y})

        R = set(C + [Q[j], Q[(j + 1) % 4], Q[(j + 2) % 4]])
        assert ret[-4] == (set(C) - {t}) | {d, Q[j], Q[(j + 2) % 4], Q[(j + 3) % 4]}
        assert ret[-3] == (set(C) - {t}) | {d, Q[j], Q[(j + 1) % 4], Q[(j + 2) % 4]}
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

    # Residence and exact repeat witnesses.
    min_run = 2 * n
    for path in paths:
        for x in ground:
            bits = [x in owner for owner in path]
            if all(bits) or not any(bits):
                continue
            for value in (False, True):
                starts = [i for i in range(2 * n) if bits[i] == value and bits[i - 1] != value]
                assert len(starts) == 1
                run = 0
                while bits[(starts[0] + run) % (2 * n)] == value:
                    run += 1
                min_run = min(min_run, run)

    # Switched phase: R_i is reconnected to U_(i+1), so the four owner paths
    # concatenate in cyclic order 0,1,2,3.  Audit every cyclic run again.
    switched = sum(paths, [])
    switched_min_run = len(switched)
    switched_bad = []
    for x in ground:
        bits = [x in owner for owner in switched]
        if all(bits) or not any(bits):
            continue
        for value in (False, True):
            starts = [
                i for i in range(len(switched))
                if bits[i] == value and bits[i - 1] != value
            ]
            for start in starts:
                run = 0
                while bits[(start + run) % len(switched)] == value:
                    run += 1
                switched_min_run = min(switched_min_run, run)
                if run < q:
                    switched_bad.append((x, value, start, run))

    # Exposure as defined in the source theorem.
    lower_exposure = defaultdict(int)
    for owner in owners:
        for x in owner:
            lower_exposure[frozenset(set(owner) - {x})] += 1
    alpha = max((v for x, v in lower_exposure.items() if x not in lowers), default=0)
    upper_exposure = defaultdict(int)
    for lower in lowers:
        for x in ground - set(lower):
            upper_exposure[frozenset(set(lower) | {x})] += 1
    beta = max(upper_exposure.values(), default=0)

    # The all-width proof uses only forward prefixes.
    prefix_ok = True
    for i in range(4):
        R = set(C + [Q[i], Q[(i + 1) % 4], Q[(i + 2) % 4]])
        old = set(R)
        new = set(R)
        for s in range(n + 1):
            old |= paths[i][s]
            new |= paths[(i + 1) % 4][s]
            prefix_ok &= old == new
        prefix_ok &= old == ground

    return {
        "m": m,
        "q": q,
        "owner_max": max(owners.values()),
        "lower_max": max(lowers.values()),
        "upper_max": max(uppers.values()),
        "min_run": min_run,
        "switched_min_run": switched_min_run,
        "switched_bad": switched_bad,
        "alpha": alpha,
        "beta": beta,
        "prefix_ok": prefix_ok,
    }


if __name__ == "__main__":
    for m in range(18, 81):
        q = max(5, int(m**0.5) + 1)
        if m >= max(q + 8, 2 * q + 2):
            print(build(m, q))
