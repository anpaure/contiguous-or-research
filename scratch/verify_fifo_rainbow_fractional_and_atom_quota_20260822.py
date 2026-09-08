#!/usr/bin/env python3
"""Finite checks for the FIFO fractional-circulation and product-atom formulas."""

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def falling(x, j):
    out = 1
    for i in range(j):
        out *= x - i
    return out


def check_fifo_fractional(n=7, k=3, g=5):
    alphabet = tuple(range(n))
    arcs = list(permutations(alphabet, g))
    Rk = factorial(k) * falling(n - k, g - k)
    W = comb(n, k)

    colours = Counter(tuple(sorted(a[-k:])) for a in arcs)
    assert set(colours.values()) == {Rk}
    assert len(colours) == W
    assert len(arcs) == W * Rk

    indeg = Counter(a[1:] for a in arcs)
    outdeg = Counter(a[:-1] for a in arcs)
    assert indeg == outdeg
    assert set(indeg.values()) == {n - g + 1}

    rank_counts = {}
    for s in range(1, g + 1):
        counts = Counter(tuple(sorted(a[-s:])) for a in arcs)
        expected = factorial(s) * falling(n - s, g - s)
        assert len(counts) == comb(n, s)
        assert set(counts.values()) == {expected}
        assert expected * comb(n, s) == len(arcs)
        # Dividing by Rk gives W / C(n,s).
        assert expected * comb(n, s) == Rk * W
        rank_counts[s] = expected
    return len(arcs), Rk, rank_counts


def cyclic_orders(items):
    """Directed cyclic orders modulo rotation, canonically rooted at min(items)."""
    root = min(items)
    rest = tuple(x for x in items if x != root)
    for p in permutations(rest):
        yield (root,) + p


def atom_word(A, alpha, beta):
    b = len(A)
    h = (b - 1) // 2
    flat_types = [x for _ in range(h) for x in ("B", "A")] + ["B"]
    ia = ib = 0
    out = []
    for t in range(b * b):
        typ = flat_types[t % b]
        if typ == "A":
            out.append(alpha[ia % b])
            ia += 1
        else:
            out.append(beta[ib % b])
            ib += 1
    return tuple(out)


def cyclic_windows(word, s):
    L = len(word)
    return [tuple(word[(i + j) % L] for j in range(s)) for i in range(L)]


def min_cyclic_gap(word):
    L = len(word)
    pos = {}
    for i, x in enumerate(word):
        pos.setdefault(x, []).append(i)
    ans = L
    for inds in pos.values():
        inds = sorted(inds)
        gaps = [inds[i + 1] - inds[i] for i in range(len(inds) - 1)]
        gaps.append(L + inds[0] - inds[-1])
        ans = min(ans, min(gaps))
    return ans


def check_product_atom_orbit(b=3):
    assert b % 2 == 1
    omega = tuple(range(2 * b))
    W = comb(2 * b, b)
    Dhat = b * factorial(b) ** 2

    central = Counter()
    ranks = {s: Counter() for s in range(1, 2 * b - 1)}
    atom_count = 0
    first_word = None

    for A_tuple in combinations(omega, b):
        A = frozenset(A_tuple)
        B = frozenset(set(omega) - set(A))
        for alpha in cyclic_orders(A):
            for beta0 in cyclic_orders(B):
                for rho in range(b):
                    beta = beta0[rho:] + beta0[:rho]
                    word = atom_word(A, alpha, beta)
                    if first_word is None:
                        first_word = word
                    atom_count += 1
                    mids = [tuple(sorted(w)) for w in cyclic_windows(word, b)]
                    assert len(set(mids)) == b * b
                    central.update(mids)
                    for s in ranks:
                        ranks[s].update(
                            tuple(sorted(w)) for w in cyclic_windows(word, s)
                        )

    assert atom_count == b * W * factorial(b - 1) ** 2
    assert min_cyclic_gap(first_word) >= 2 * b - 2
    assert len(central) == W
    assert set(central.values()) == {Dhat}

    rank_values = {}
    for s, counts in ranks.items():
        assert len(counts) == comb(2 * b, s)
        assert len(set(counts.values())) == 1
        raw = next(iter(counts.values()))
        assert raw * comb(2 * b, s) == atom_count * b * b
        # Weighted by 1/Dhat, the load is W / C(2b,s).
        assert raw * comb(2 * b, s) == Dhat * W
        rank_values[s] = raw
    # Separately check a b=5 word in the nonempty H-safe range g=b+H+2.
    b5 = 5
    A5 = frozenset(range(b5))
    B5 = frozenset(range(b5, 2 * b5))
    word5 = atom_word(A5, tuple(sorted(A5)), tuple(sorted(B5)))
    assert len(set(tuple(sorted(w)) for w in cyclic_windows(word5, b5))) == b5 * b5
    assert min_cyclic_gap(word5) >= 2 * b5 - 2
    return atom_count, Dhat, min_cyclic_gap(first_word), rank_values


def check_overflow_identity():
    # Three illustrative ranks/load profiles.  Quotas have the same total.
    examples = [
        ([0, 1, 1, 2, 2], [1, 1, 1, 1, 2]),
        ([0, 0, 3, 3], [1, 1, 2, 2]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]
    checked = []
    for loads, quotas in examples:
        assert sum(loads) == sum(quotas)
        overflow = sum(max(a - q, 0) for a, q in zip(loads, quotas))
        deficit = sum(max(q - a, 0) for a, q in zip(loads, quotas))
        holes = sum(a == 0 for a in loads)
        assert overflow == deficit
        assert holes <= overflow
        N = len(loads)
        M = sum(loads)
        collision = sum(max(a - 1, 0) for a in loads)
        assert holes == N - M + collision
        checked.append((holes, overflow, collision))
    return checked


def main():
    fifo = check_fifo_fractional()
    atom = check_product_atom_orbit()
    overflow = check_overflow_identity()
    print(
        "FIFO_RAINBOW_FRACTIONAL_AND_ATOM_QUOTA_PASS",
        f"fifo_arcs={fifo[0]}",
        f"central_reps={fifo[1]}",
        f"atoms={atom[0]}",
        f"atom_degree={atom[1]}",
        f"min_gap={atom[2]}",
        f"overflow_examples={overflow}",
    )


if __name__ == "__main__":
    main()
