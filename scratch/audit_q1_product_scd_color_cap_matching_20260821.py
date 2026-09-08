#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from math import comb


def scd(n):
    """Recursive symmetric chain decomposition of B_n."""
    chains = [(frozenset(),)]
    for new in range(n):
        lifted = []
        for chain in chains:
            first = list(chain) + [chain[-1] | {new}]
            lifted.append(tuple(first))
            second = tuple(x | {new} for x in chain[:-1])
            if second:
                lifted.append(second)
        chains = lifted
    universe = {frozenset(x for x in range(n) if mask >> x & 1) for mask in range(1 << n)}
    flat = [x for chain in chains for x in chain]
    assert len(flat) == len(universe) == len(set(flat))
    assert set(flat) == universe
    for chain in chains:
        assert len(chain[0]) + len(chain[-1]) == n
        assert all(chain[i] < chain[i + 1] for i in range(len(chain) - 1))
    return chains


def explicit_matching(b):
    chains_a = scd(b)
    chains_b = scd(b)
    by_rank_a = [{len(x): x for x in chain} for chain in chains_a]
    by_rank_b = [{len(x): x for x in chain} for chain in chains_b]
    matched_sources = set()
    matched_targets = set()
    color_count = Counter()

    for ia, chain_a in enumerate(chains_a):
        a = len(chain_a[0])
        for ib, chain_b in enumerate(chains_b):
            c = len(chain_b[0])
            if a == c:
                continue
            d = max(a, c)
            for r in range(d, b - d + 1):
                source = (by_rank_a[ia][r], by_rank_b[ib][b - r])
                if a < c:
                    target = (by_rank_a[ia][r + 1], by_rank_b[ib][b - r])
                    side = "A"
                else:
                    target = (by_rank_a[ia][r], by_rank_b[ib][b - r + 1])
                    side = "B"
                assert source not in matched_sources
                assert target not in matched_targets
                assert source[0] <= target[0] and source[1] <= target[1]
                assert len(target[0]) + len(target[1]) == b + 1
                matched_sources.add(source)
                matched_targets.add(target)
                color_count[r, side] += 1

    cvals = [comb(b, d) - (comb(b, d - 1) if d else 0) for d in range((b - 1) // 2 + 1)]
    exact_loss = sum(c * c * (b - 2 * d) for d, c in enumerate(cvals))
    assert len(matched_targets) == comb(2 * b, b + 1) - exact_loss

    for r in range(b + 1):
        t = min(r, b - r)
        s = comb(b, t)
        e = sum(c * c for c in cvals[: t + 1])
        f = (s * s - e) // 2
        assert color_count[r, "A"] == color_count[r, "B"] == f
        assert color_count[r, "A"] <= Fraction(r * comb(b, r) ** 2, b)
        assert color_count[r, "B"] <= Fraction((b - r) * comb(b, r) ** 2, b)

    print(
        "explicit PASS",
        b,
        "matching",
        len(matched_targets),
        "loss",
        exact_loss,
        "loss/W",
        float(Fraction(exact_loss, comb(2 * b, b))),
    )


def formula_checks():
    for b in (5, 7, 11, 23, 43, 101, 503, 1009):
        h = (b - 1) // 2
        cvals = [comb(b, d) - (comb(b, d - 1) if d else 0) for d in range(h + 1)]
        for t in range(h + 1):
            s = comb(b, t)
            e = sum(c * c for c in cvals[: t + 1])
            assert b * e >= (b - 2 * t) * s * s
            assert (s * s - e) // 2 <= Fraction(t * s * s, b)
        loss = sum(c * c * (b - 2 * d) for d, c in enumerate(cvals))
        w = comb(2 * b, b)
        print(
            "formula PASS",
            b,
            "loss/W",
            float(Fraction(loss, w)),
            "sqrt(b)*loss/W",
            float(Fraction(loss * int(b**0.5), w)),
        )


if __name__ == "__main__":
    for block_size in (5, 7, 9, 11):
        explicit_matching(block_size)
    formula_checks()
    print("ALL Q=1 PRODUCT-SCD COLOR-CAP CHECKS PASS")
