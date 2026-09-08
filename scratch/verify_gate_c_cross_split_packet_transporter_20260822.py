#!/usr/bin/env python3
"""Regression checks for the Gate-C cross-split packet transporter."""


def cyclic_deck(order: tuple[int, ...], length: int) -> set[frozenset[int]]:
    b = len(order)
    return {
        frozenset(order[(start + offset) % b] for offset in range(length))
        for start in range(b)
    }


def image(family: set[frozenset[int]], permutation: tuple[int, ...]) -> set[frozenset[int]]:
    return {
        frozenset(permutation[x] for x in member)
        for member in family
    }


def gadget(b: int):
    h = (b - 1) // 2
    block_a = set(range(b))
    block_b = set(range(b, 2 * b))
    w, u, v = h - 1, 2 * h - 1, 2 * h

    alpha_0 = tuple(range(b))
    alpha_1 = tuple(range(2 * h - 1)) + (v, u)
    alpha_2 = (
        (u,)
        + tuple(range(h - 2, -1, -1))
        + tuple(range(h, 2 * h - 1))
        + (v, w)
    )
    beta = tuple(range(b, 2 * b))

    deck_0 = cyclic_deck(alpha_0, h)
    deck_1 = cyclic_deck(alpha_1, h)
    deck_2 = cyclic_deck(alpha_2, h)
    residual = (deck_0 | deck_2) - deck_1
    deck_y = cyclic_deck(beta, h + 1)

    def product(first):
        return {left | right for left in first for right in deck_y}

    edge_0 = product(deck_0)
    edge_1 = product(deck_1)
    edge_2 = product(deck_2)
    packet = product(residual)
    domain = edge_1 | packet

    assert not deck_0 & deck_2
    assert deck_0 | deck_2 == deck_1 | residual
    assert not deck_1 & residual
    assert edge_0 | edge_2 == edge_1 | packet
    assert not edge_0 & edge_2
    assert not edge_1 & packet
    assert len(domain) == 2 * b * b

    return block_a, block_b, edge_0, edge_1, edge_2, packet, domain


def verify_explicit(b: int, permutation: tuple[int, ...]) -> None:
    block_a, block_b, edge_0, edge_1, edge_2, packet, domain = gadget(b)
    moved_domain = image(domain, permutation)
    assert not domain & moved_domain
    assert set(permutation[x] for x in block_a) not in (block_a, block_b)

    moved_0 = image(edge_0, permutation)
    moved_1 = image(edge_1, permutation)
    moved_2 = image(edge_2, permutation)
    moved_packet = image(packet, permutation)

    matching_minus = [edge_1, moved_0, moved_2]
    matching_plus = [edge_0, edge_2, moved_1]
    assert sum(map(len, matching_minus)) == len(set().union(*matching_minus))
    assert sum(map(len, matching_plus)) == len(set().union(*matching_plus))
    assert set().union(*matching_minus) == edge_1 | moved_1 | moved_packet
    assert set().union(*matching_plus) == edge_1 | moved_1 | packet
    assert (set().union(*matching_minus) - set().union(*matching_plus)) == moved_packet
    assert (set().union(*matching_plus) - set().union(*matching_minus)) == packet


def verify_doubled(b: int, permutation: tuple[int, ...]) -> None:
    block_a, block_b, edge_0, edge_1, edge_2, packet, domain = gadget(b)
    omega = set(range(2 * b))

    def complement(family):
        return {frozenset(omega - member) for member in family}

    doubled_domain = domain | complement(domain)
    assert len(doubled_domain) == 4 * b * b
    assert not doubled_domain & image(doubled_domain, permutation)
    assert set(permutation[x] for x in block_a) not in (block_a, block_b)

    moved_0 = image(edge_0, permutation)
    moved_1 = image(edge_1, permutation)
    moved_2 = image(edge_2, permutation)
    minus = [edge_1, moved_0, moved_2]
    plus = [edge_0, edge_2, moved_1]

    # Form complemented atom families without flattening their vertices.
    minus_families = minus + [complement(family) for family in minus]
    plus_families = plus + [complement(family) for family in plus]
    minus_union = set().union(*minus_families)
    plus_union = set().union(*plus_families)
    assert sum(map(len, minus_families)) == len(minus_union)
    assert sum(map(len, plus_families)) == len(plus_union)
    moved_packet = image(packet, permutation)
    assert minus_union - plus_union == moved_packet | complement(moved_packet)
    assert plus_union - minus_union == packet | complement(packet)


def main() -> None:
    for b in range(5, 32, 2):
        gadget(b)

    verify_explicit(5, (5, 0, 1, 2, 4, 7, 3, 8, 6, 9))
    verify_explicit(7, (12, 4, 0, 9, 13, 6, 8, 7, 10, 2, 11, 1, 5, 3))
    verify_doubled(7, (0, 11, 1, 13, 8, 12, 9, 10, 7, 3, 6, 5, 2, 4))
    verify_doubled(9, (8, 13, 2, 5, 10, 14, 1, 7, 11, 15, 4, 9, 16, 0, 3, 17, 12, 6))
    print("GATE_C_CROSS_SPLIT_PACKET_TRANSPORTER_PASS")


if __name__ == "__main__":
    main()
