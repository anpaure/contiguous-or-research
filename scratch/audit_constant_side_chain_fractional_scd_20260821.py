#!/usr/bin/env python3
"""Finite audit for constant-side fractional laws and the SCD support lemma."""

from fractions import Fraction
from itertools import combinations
from math import comb


def recursive_scd(n):
    """Return a symmetric chain decomposition of subsets as bit masks."""
    chains = [[0]]
    for x in range(n):
        bit = 1 << x
        new = []
        for chain in chains:
            first = [*chain, chain[-1] | bit]
            new.append(first)
            second = [u | bit for u in chain[:-1]]
            if second:
                new.append(second)
        chains = new
    return chains


def audit_scd(n):
    chains = recursive_scd(n)
    flat = [u for chain in chains for u in chain]
    assert len(flat) == 1 << n and len(set(flat)) == 1 << n
    for chain in chains:
        ranks = [u.bit_count() for u in chain]
        assert ranks == list(range(ranks[0], ranks[-1] + 1))
        assert ranks[0] + ranks[-1] == n
        assert all((chain[i] & chain[i + 1]) == chain[i]
                   for i in range(len(chain) - 1))

    owner = {}
    top = {}
    for chain in chains:
        for u in chain:
            owner[u] = chain
            top[u] = chain[-1].bit_count()

    for r in range(n + 1):
        layer = [u for u in flat if u.bit_count() == r]
        ordered = sorted(layer, key=lambda u: top[u], reverse=True)
        for h in range(n - r + 1):
            e_sets = []
            for q in range(h + 1):
                e = {u for u in layer if top[u] >= r + q}
                assert len(e) == min(comb(n, r), comb(n, r + q))
                e_sets.append(e)
            assert all(e_sets[q + 1] <= e_sets[q]
                       for q in range(len(e_sets) - 1))
            for count in range(len(layer) + 1):
                selected = set(ordered[:count])
                for q, e in enumerate(e_sets):
                    assert len(selected & e) == min(count, len(e))


def audit_loads(b, h):
    c = [comb(b, j) for j in range(b + 1)]
    for q in range(1, h + 1):
        for s in range(q, b + 1):
            t = s - q
            if t < h or s > b - h:
                continue
            a_ratio = Fraction(comb(s, q), comb(b - t, q))
            b_ratio = Fraction(comb(b + q - s, q), comb(s, q))
            assert a_ratio == Fraction(c[t], c[s])
            assert b_ratio == Fraction(c[s], c[t])
            assert (a_ratio + b_ratio) / 2 >= 1

            alpha = Fraction(t - h + 1, b)
            beta = Fraction(b - s - h + 1, b)
            load = alpha * a_ratio + beta * b_ratio
            capacity = Fraction(
                (b - s - h + 1) * c[s] ** 2
                + (s - q - h + 1) * c[t] ** 2,
                b,
            )
            assert load * c[s] * c[t] == capacity


def predecessors(b, target, h):
    """All (source,side) pairs that can have target as their first step."""
    full_a = (1 << b) - 1
    full_b = full_a << b
    out = set()
    for x in range(2 * b):
        if not (target >> x) & 1:
            continue
        source = target ^ (1 << x)
        if source.bit_count() != b:
            continue
        side_mask = full_a if x < b else full_b
        missing_after = (side_mask & ~target).bit_count()
        if missing_after >= h - 1:
            out.add((source, "A" if x < b else "B"))
    return out


def audit_extreme(b, h):
    full_a = (1 << b) - 1
    full_b = full_a << b
    for a in range(b):
        target = full_b | (1 << a)
        assert predecessors(b, target, h) == {(full_b, "A")}
    for x in range(b, 2 * b):
        target = full_a | (1 << x)
        assert predecessors(b, target, h) == {(full_a, "B")}


def layer(n, r):
    return [sum(1 << x for x in xs) for xs in combinations(range(n), r)]


def audit_wider_side_cover(b, h):
    chains = recursive_scd(b)
    owner = {}
    position = {}
    bottom = {}
    for chain in chains:
        low = chain[0].bit_count()
        for i, u in enumerate(chain):
            owner[u] = chain
            position[u] = i
            bottom[u] = low

    layers = [layer(b, r) for r in range(b + 1)]
    covered = {q: set() for q in range(1, h + 1)}
    for r in range(h, b - h + 1):
        for x in layers[r]:
            chain_x = owner[x]
            ix = position[x]
            for y in layers[r]:
                chain_y = owner[y]
                iy = position[y]
                if bottom[x] <= bottom[y]:
                    current = x
                    additions = []
                    for nxt in chain_x[ix + 1:]:
                        additions.append(nxt ^ current)
                        current = nxt
                    additions.extend(
                        1 << z for z in range(b) if not (current >> z) & 1
                    )
                    assert len(additions) >= h
                    current = x
                    for q, bit in enumerate(additions[:h], 1):
                        current |= bit
                        covered[q].add((current, y))
                else:
                    current = y
                    removals = []
                    for prev in reversed(chain_y[:iy]):
                        removals.append(current ^ prev)
                        current = prev
                    removals.extend(
                        1 << z for z in range(b) if (current >> z) & 1
                    )
                    assert len(removals) >= h
                    current = y
                    for q, bit in enumerate(removals[:h], 1):
                        current ^= bit
                        covered[q].add((x, current))

    for q in range(1, h + 1):
        expected = set()
        for s in range(q, b + 1):
            t = s - q
            if t < h or s > b - h:
                continue
            expected.update((x, y) for x in layers[s] for y in layers[t])
        assert expected <= covered[q]
        print("PASS wider-side", b, h, q, len(expected))


def main():
    for b in range(3, 14):
        for h in range(1, min(4, b // 2 + 1)):
            audit_loads(b, h)
        print("PASS loads", b)
    for n in range(1, 10):
        audit_scd(n)
        print("PASS SCD", n)
    for b in range(3, 10):
        for h in range(1, min(4, b // 2 + 1)):
            audit_wider_side_cover(b, h)
    for b in range(2, 10):
        audit_extreme(b, 2)
        print("PASS extreme", b)
    print("ALL CONSTANT-SIDE FRACTIONAL/SCD CHECKS PASS")


if __name__ == "__main__":
    main()
