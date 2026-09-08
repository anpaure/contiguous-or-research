#!/usr/bin/env python3
"""Exact finite audit for the non-GK SCD Hamilton-flag repair theorem."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def mask_of(items):
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def bracket(mask, n):
    """Return paired positions, unpaired zeros, and unpaired ones."""
    stack = []
    paired = 0
    unpaired_zeros = []
    for position in range(n):
        if mask & (1 << position):
            stack.append(position)
        elif stack:
            opener = stack.pop()
            paired |= (1 << opener) | (1 << position)
        else:
            unpaired_zeros.append(position)
    return paired, tuple(unpaired_zeros), tuple(stack)


def is_dyck(mask, n):
    height = 0
    for position in range(n):
        height += 1 if mask & (1 << position) else -1
        if height < 0:
            return False
    return height == 0


def is_primitive_dyck(mask, n):
    height = 0
    for position in range(n):
        height += 1 if mask & (1 << position) else -1
        if position + 1 < n and height <= 0:
            return False
    return height == 0


def gk_chains(n):
    """Generate the ordered Greene--Kleitman SCD without storing it."""
    for bottom in range(1 << n):
        _, unpaired_zeros, unpaired_ones = bracket(bottom, n)
        if unpaired_ones:
            continue
        chain = [bottom]
        current = bottom
        for position in reversed(unpaired_zeros):
            current |= 1 << position
            chain.append(current)
        yield chain


def check_chain(chain, n):
    ranks = [mask.bit_count() for mask in chain]
    assert ranks == list(range(ranks[0], ranks[-1] + 1))
    assert ranks[0] + ranks[-1] == n
    assert all(
        lower & upper == lower and (lower ^ upper).bit_count() == 1
        for lower, upper in zip(chain, chain[1:])
    )


def primitive_switch_bank(b):
    """Map every source 0 D' 1 to its primitive-Dyck target 1 D' 0."""
    n = 2 * b
    bank = {}
    for chosen in combinations(range(n - 2), b - 1):
        core = mask_of(chosen)
        if not is_dyck(core, n - 2):
            continue
        source = (core << 1) | (1 << (n - 1))
        target = (core << 1) | 1
        assert not is_dyck(source, n)
        assert is_primitive_dyck(target, n)
        _, unpaired_zeros, unpaired_ones = bracket(source, n)
        assert unpaired_zeros == (0,)
        assert unpaired_ones == (n - 1,)
        alternate = (source ^ (1 << (n - 1))) | 1
        assert alternate == target
        bank[source] = target
    expected = comb(2 * b - 2, b - 1) // b
    assert len(bank) == expected
    assert len(set(bank.values())) == expected
    assert set(bank).isdisjoint(bank.values())
    return bank


def central_flags(b):
    """Return the ordered GK central flags and singleton middle sets."""
    n = 2 * b
    flags = []
    singletons = set()
    for chosen in combinations(range(n), b):
        middle = mask_of(chosen)
        _, unpaired_zeros, unpaired_ones = bracket(middle, n)
        assert len(unpaired_zeros) == len(unpaired_ones)
        if not unpaired_zeros:
            singletons.add(middle)
            continue
        q = unpaired_zeros[-1]
        p = unpaired_ones[0]
        lower = middle ^ (1 << p)
        upper = middle | (1 << q)
        alternate = lower | (1 << q)
        flags.append((lower, middle, upper, p, q, alternate))
    return flags, singletons


def audit_full_scd_and_switches(b):
    n = 2 * b
    bank = primitive_switch_bank(b)
    sources = set(bank)
    targets = set(bank.values())
    seen_original = bytearray(1 << n)
    seen_switched = bytearray(1 << n)
    original_chain_count = 0
    switched_chain_count = 0

    for chain in gk_chains(n):
        original_chain_count += 1
        check_chain(chain, n)
        for mask in chain:
            seen_original[mask] += 1

        if len(chain) == 1 and chain[0] in targets:
            continue

        changed = list(chain)
        central = next((mask for mask in chain if mask.bit_count() == b), None)
        if central in sources:
            assert len(chain) == 3
            changed[1] = bank[central]
        check_chain(changed, n)
        switched_chain_count += 1
        for mask in changed:
            seen_switched[mask] += 1

    for source in sources:
        chain = [source]
        check_chain(chain, n)
        switched_chain_count += 1
        seen_switched[source] += 1

    assert original_chain_count == comb(n, b)
    assert switched_chain_count == original_chain_count
    assert seen_original.count(1) == 1 << n
    assert seen_switched.count(1) == 1 << n
    assert not (set(seen_original) - {1})
    assert not (set(seen_switched) - {1})

    flags, singletons = central_flags(b)
    middle = {middle for _, middle, _, _, _, _ in flags}
    assert len(flags) == comb(n, b - 1)
    assert len(middle) == len(flags)
    assert len(singletons) == comb(n, b) // (b + 1)
    assert sources <= middle
    assert targets <= singletons

    # The switch criterion: alternate images are injective and land outside
    # every unchanged central owner.
    phi = {middle_set: alternate
           for _, middle_set, _, _, _, alternate in flags}
    assert all(phi[source] == bank[source] for source in sources)
    assert len({phi[source] for source in sources}) == len(sources)
    assert {phi[source] for source in sources}.isdisjoint(middle - sources)

    arcs = Counter((p, q) for _, _, _, p, q, _ in flags)
    catalan = comb(2 * b - 2, b - 1) // b
    dyck_cores = [
        (target >> 1) & ((1 << (n - 2)) - 1)
        for target in targets
    ]
    for j in range(1, n):
        assert arcs[(j, j - 1)] == catalan
        # Lemma 4.1's explicit inverse: D=B A maps to A 0 1 B.
        length_a = j - 1
        length_b = n - j - 1
        constructed = set()
        for dyck in dyck_cores:
            word_b = dyck & ((1 << length_b) - 1)
            word_a = dyck >> length_b
            assert word_a < (1 << length_a)
            middle_set = word_a | (1 << j) | (word_b << (j + 1))
            _, unpaired_zeros, unpaired_ones = bracket(middle_set, n)
            assert unpaired_zeros[-1] == j - 1
            assert unpaired_ones[0] == j
            constructed.add(middle_set)
        expected_middles = {
            middle_set
            for _, middle_set, _, p, q, _ in flags
            if (p, q) == (j, j - 1)
        }
        assert constructed == expected_middles
    assert arcs[(n - 1, 0)] == catalan

    switched_arcs = arcs.copy()
    switched_arcs[(n - 1, 0)] -= catalan
    switched_arcs[(0, n - 1)] += catalan
    assert switched_arcs[(n - 1, 0)] == 0
    hamilton_arcs = [(0, n - 1)]
    hamilton_arcs.extend((j, j - 1) for j in range(n - 1, 0, -1))
    assert len(hamilton_arcs) == len(set(hamilton_arcs)) == n
    assert all(switched_arcs[arc] == catalan for arc in hamilton_arcs)

    if b >= 3 and b % 2 == 1:
        h = (b - 1) // 2
        tours = catalan // h
        retained = b * (b - 1) * tours
        total_flags = comb(n, b - 1)
        assert Fraction(2 * b * catalan, total_flags) == Fraction(
            b + 1, 2 * b - 1
        )
        assert Fraction(retained, total_flags) >= (
            Fraction(b + 1, 2 * b - 1)
            - Fraction(b * (b - 1), total_flags)
        )


def audit_fractional_identities(b):
    n = 2 * b
    lower_count = comb(n, b - 1)
    middle_count = comb(n, b)
    flag_count = lower_count * b * (b + 1)
    assert flag_count == middle_count * b * b

    weight = Fraction(1, b * (b + 1))
    assert b * (b + 1) * weight == 1
    assert b * b * weight == Fraction(b, b + 1)
    assert Fraction(lower_count, flag_count) == weight

    arc_flag_count = comb(n - 2, b - 1)
    assert n * (n - 1) * arc_flag_count == flag_count
    hamilton_count = factorial(n - 1)
    cycles_per_arc = factorial(n - 2)
    assert Fraction(cycles_per_arc, hamilton_count) == Fraction(1, n - 1)
    theta = Fraction(arc_flag_count, 1) * weight / cycles_per_arc

    if b >= 3 and b % 2 == 1:
        h = (b - 1) // 2
        # Uniform h-subsets on each Hamilton arc give this flag marginal.
        assert theta / h * Fraction(h, arc_flag_count) == (
            weight / cycles_per_arc
        )
        projected_tour_mass = hamilton_count * theta / h
        assert projected_tour_mass == Fraction(lower_count, b * (b - 1))


def repaired_factor_contains(flag, b):
    """Membership in the Catalan-switched central factor, without enumeration."""
    lower, middle, upper = flag
    n = 2 * b
    _, unpaired_zeros, unpaired_ones = bracket(middle, n)
    if not unpaired_zeros:
        if not is_primitive_dyck(middle, n):
            return False
        return (
            lower == (middle ^ 1)
            and upper == (middle | (1 << (n - 1)))
        )

    p = unpaired_ones[0]
    q = unpaired_zeros[-1]
    if (p, q) == (n - 1, 0):
        return False
    return (
        lower == (middle ^ (1 << p))
        and upper == (middle | (1 << q))
    )


def cyclic_interval_mask(start, length, n):
    return mask_of((start + offset) % n for offset in range(length))


def audit_two_near_tours(b):
    """Audit Theorem 5.1 directly from its cyclic-window formula."""
    n = 2 * b
    qsize = b * (b - 1)
    h = (b - 1) // 2
    retained_by_phase = []

    for phase in (0, 1):
        packets = []
        flags = []
        arcs = Counter()
        for s in range(b):
            a = (phase + (s + 1) * (b - 1)) % n
            windows = []
            for t in range(b + 1):
                start = (a - t + 1) % n
                window = cyclic_interval_mask(start, b + 1, n)
                window ^= 1 << ((a + 1) % n)
                assert window.bit_count() == b
                windows.append(window)

            next_a = (phase + (s + 2) * (b - 1)) % n
            next_boundary = cyclic_interval_mask((next_a + 1) % n, b + 1, n)
            next_boundary ^= 1 << ((next_a + 1) % n)
            assert windows[-1] == next_boundary

            for t, middle in enumerate(windows[1:-1], 1):
                pair_loads = [
                    ((middle >> j) & 1) + ((middle >> (j + b)) & 1)
                    for j in range(b)
                ]
                assert Counter(pair_loads) == Counter({0: 1, 1: b - 2, 2: 1})
                assert pair_loads[(a + 1) % b] == 0
                assert pair_loads[(a - t + 1) % b] == 2

                lower = windows[t - 1] & middle
                upper = middle | windows[t + 1]
                r = (a - t + 1) % n
                assert lower == (middle ^ (1 << r))
                assert upper == (middle | (1 << ((r - 1) % n)))

                rotated = [
                    (middle >> ((r + offset) % n)) & 1
                    for offset in range(n)
                ]
                expected = (
                    [1] * t + [0] + [1] * (b - t) + [0] * (b - 1)
                )
                assert rotated == expected

                flag = (lower, middle, upper)
                belongs = repaired_factor_contains(flag, b)
                assert belongs == (t >= 2)
                flags.append(flag)
                arcs[(r, (r - 1) % n)] += 1
            packets.append(windows)

        for s in range(b):
            assert packets[s][-1] == packets[(s + 1) % b][0]
        assert len(flags) == len(set(flags)) == qsize
        assert set(arcs.values()) == {h}
        assert set(arcs) == {(r, (r - 1) % n) for r in range(n)}
        retained = {
            flag for index, flag in enumerate(flags)
            if index % (b - 1) != 0
        }
        assert len(retained) == b * (b - 2)
        retained_by_phase.append(retained)

    assert retained_by_phase[0].isdisjoint(retained_by_phase[1])
    combined = retained_by_phase[0] | retained_by_phase[1]
    for coordinate in range(3):
        targets = [flag[coordinate] for flag in combined]
        assert len(targets) == len(set(targets))


def main():
    for b in range(2, 11):
        audit_full_scd_and_switches(b)
    for b in range(2, 31):
        audit_fractional_identities(b)
    for b in range(3, 102, 2):
        audit_two_near_tours(b)
    print("PASS: full GK SCD and simultaneous Catalan switch bank for 2<=b<=10")
    print("PASS: consecutive arcs and repaired Hamilton multiplicities for 2<=b<=10")
    print("PASS: all fractional incidence and Hamilton identities for 2<=b<=30")
    print("PASS: two q-b coherent-tour overlaps and exact missing flags for odd 3<=b<=101")


if __name__ == "__main__":
    main()
