#!/usr/bin/env python3
"""Verify the q=2 distance-one bridge one-owner/common-reserve certificate.

The symbolic construction has a common (c-1)-set C0.  After suppressing
C0, an owner is a triple and a rail with centre r and toggle cycle sigma
has the cyclic triples {r, sigma_i, sigma_{i+1}}.  The first part checks
the reduced certificate.  The second part instantiates the smallest full
case c=3, M=8 and checks every named-owner collision in the specialized
insertion/star macro and in both common-reserve states.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import chain


ReducedRail = tuple[int, tuple[int, ...]]
Owner = tuple[int, ...]


A_PLUS: tuple[ReducedRail, ...] = (
    (0, (1, 2, 4, 6, 8, 5)),
    (0, (2, 6, 3, 7, 4, 8)),
    (1, (2, 4, 8, 6, 3, 7, 5)),
    (2, (1, 3, 5, 6, 4, 8, 7)),
    (3, (1, 4, 2, 6, 7, 8)),
    (5, (0, 3, 8, 2, 4, 7)),
    (6, (1, 4, 3, 8, 2, 7)),
    (8, (0, 1, 5, 6, 4, 7)),
)

A_MINUS: tuple[ReducedRail, ...] = (
    (0, (1, 5, 3, 7, 4, 6, 8)),
    (1, (2, 5, 8, 4, 3, 7)),
    (2, (0, 4, 6, 3, 5, 8)),
    (3, (1, 2, 4, 6, 7, 8)),
    (4, (1, 2, 5, 7, 8, 6)),
    (6, (0, 2, 5, 8, 1, 3)),
    (7, (0, 5, 1, 6, 2, 8)),
    (8, (0, 4, 2, 6, 3, 5)),
)

H_REDUCED = (0, 1, 2)
DELTA_SMALL_CYCLE = (2, 3, 4, 5, 6, 7)
DELTA_BIG_CYCLE = (2, 1, 3, 4, 5, 6, 7)


def owner(*labels: int) -> Owner:
    return tuple(sorted(labels))


def reduced_deck(rail: ReducedRail) -> tuple[Owner, ...]:
    centre, cycle = rail
    assert centre not in cycle
    assert len(cycle) == len(set(cycle))
    n = len(cycle)
    return tuple(owner(centre, cycle[i], cycle[(i + 1) % n]) for i in range(n))


def reduced_collection(rails: tuple[ReducedRail, ...]) -> Counter[Owner]:
    return Counter(chain.from_iterable(reduced_deck(rail) for rail in rails))


def full_deck(core: frozenset[int], cycle: tuple[int, ...]) -> tuple[Owner, ...]:
    assert core.isdisjoint(cycle)
    assert len(cycle) == len(set(cycle))
    n = len(cycle)
    return tuple(
        owner(*core, cycle[i], cycle[(i + 1) % n])
        for i in range(n)
    )


def full_collection(
    rails: tuple[tuple[frozenset[int], tuple[int, ...]], ...]
) -> Counter[Owner]:
    return Counter(chain.from_iterable(full_deck(core, cycle) for core, cycle in rails))


def assert_simple(deck: Counter[Owner], expected_size: int) -> None:
    assert sum(deck.values()) == expected_size
    assert len(deck) == expected_size
    assert set(deck.values()) == {1}


def point_degrees(deck: Counter[Owner]) -> Counter[int]:
    ans: Counter[int] = Counter()
    for value, multiplicity in deck.items():
        for x in value:
            ans[x] += multiplicity
    return ans


def main() -> None:
    # Reduced bridge certificate.
    plus = reduced_collection(A_PLUS)
    minus = reduced_collection(A_MINUS)
    assert [len(cycle) for _, cycle in A_PLUS] == [6, 6, 7, 7, 6, 6, 6, 6]
    assert [len(cycle) for _, cycle in A_MINUS] == [7, 6, 6, 6, 6, 6, 6, 6]
    assert_simple(plus, 50)
    assert_simple(minus, 49)
    assert plus - minus == Counter({H_REDUCED: 1})
    assert not (minus - plus)

    reserve_without_h = tuple(sorted(minus))
    expected_reserve_without_h = tuple(
        owner(*map(int, word))
        for word in (
            "015 018 024 026 028 035 036 037 046 047 048 057 058 068 078 "
            "123 124 125 127 134 136 137 138 146 148 157 158 167 168 "
            "234 235 236 245 246 248 256 258 267 268 278 346 358 367 "
            "368 378 457 468 478 568"
        ).split()
    )
    assert reserve_without_h == expected_reserve_without_h

    delta_small_reduced = Counter(reduced_deck((0, DELTA_SMALL_CYCLE)))
    delta_big_reduced = Counter(reduced_deck((0, DELTA_BIG_CYCLE)))
    assert delta_big_reduced - delta_small_reduced == Counter(
        {(0, 1, 2): 1, (0, 1, 3): 1}
    )
    assert delta_small_reduced - delta_big_reduced == Counter({(0, 2, 3): 1})
    assert not (minus & (delta_small_reduced | delta_big_reduced))

    # Full boundary instance c=3, M=8.  Here C0={9,10}, C=C0+0,
    # P={1,2}, S={1,2,3,4}, z=5, and E={0,6,7,8,9,10}.
    c0 = frozenset({9, 10})
    c_core = c0 | {0}
    h_full = owner(*c0, 0, 1, 2)

    def lift(rails: tuple[ReducedRail, ...]):
        return tuple((c0 | {centre}, cycle) for centre, cycle in rails)

    a_plus_full_rails = lift(A_PLUS)
    a_minus_full_rails = lift(A_MINUS)
    a_plus_full = full_collection(a_plus_full_rails)
    a_minus_full = full_collection(a_minus_full_rails)
    assert_simple(a_plus_full, 50)
    assert_simple(a_minus_full, 49)
    assert a_plus_full - a_minus_full == Counter({h_full: 1})
    assert not (a_minus_full - a_plus_full)

    delta_small = (c_core, DELTA_SMALL_CYCLE)
    delta_big = (c_core, DELTA_BIG_CYCLE)

    s = frozenset({1, 2, 3, 4})
    phi_1_small_cycle = (0, 9, 6, 10, 7, 8)
    phi_1_big_cycle = (0, 5, 9, 6, 10, 7, 8)
    phi_2_small_cycle = (0, 10, 6, 9, 7, 8)
    phi_2_big_cycle = (0, 5, 10, 6, 9, 7, 8)
    phi_1_small = (s - {1}, phi_1_small_cycle)
    phi_1_big = (s - {1}, phi_1_big_cycle)
    phi_2_small = (s - {2}, phi_2_small_cycle)
    phi_2_big = (s - {2}, phi_2_big_cycle)

    # Y = Delta + Phi_1 - Phi_2.
    y_plus_rails = (delta_big, phi_1_big, phi_2_small)
    y_minus_rails = (delta_small, phi_1_small, phi_2_big)
    y_plus = full_collection(y_plus_rails)
    y_minus = full_collection(y_minus_rails)
    assert_simple(y_plus, 20)   # 7 + 7 + 6
    assert_simple(y_minus, 19)  # 6 + 6 + 7
    assert y_plus[h_full] == 1
    assert y_minus[h_full] == 0

    b_plus = y_minus
    b_minus = y_plus - Counter({h_full: 1})
    assert_simple(b_plus, 19)
    assert_simple(b_minus, 19)
    assert point_degrees(b_plus) == point_degrees(b_minus)

    # The common owner reserve is A+ = A- disjoint-union {H}.
    common_reserve = a_plus_full
    assert not (b_plus & common_reserve)
    assert not (b_minus & common_reserve)

    state_from_b_plus = b_plus + common_reserve
    state_from_b_minus = b_minus + common_reserve
    state_b_plus_decomposition = full_collection(y_minus_rails + a_plus_full_rails)
    state_b_minus_decomposition = full_collection(y_plus_rails + a_minus_full_rails)
    assert_simple(state_b_plus_decomposition, 69)
    assert_simple(state_b_minus_decomposition, 69)
    assert state_from_b_plus == state_b_plus_decomposition
    assert state_from_b_minus == state_b_minus_decomposition

    canonical = " ".join("".join(map(str, value)) for value in reserve_without_h)
    digest = sha256(canonical.encode()).hexdigest()
    print("PASS q=2 near-C bridge certificate")
    print("A+ periods:", [len(cycle) for _, cycle in A_PLUS], "owners:", len(plus))
    print("A- periods:", [len(cycle) for _, cycle in A_MINUS], "owners:", len(minus))
    print("A+ \\ A-:", sorted(plus - minus))
    print("A- \\ A+:", sorted(minus - plus))
    print("reserve without H:", canonical)
    print("reserve-list sha256:", digest)
    print("boundary full-state owner counts:", len(state_from_b_plus), len(state_from_b_minus))


if __name__ == "__main__":
    main()
