#!/usr/bin/env python3
"""Regression check for the explicit Gate-C one-to-two absorber."""

from itertools import combinations


def cyclic_deck(order: tuple[int, ...], length: int) -> set[frozenset[int]]:
    b = len(order)
    return {
        frozenset(order[(start + offset) % b] for offset in range(length))
        for start in range(b)
    }


def verify(h: int) -> None:
    b = 2 * h + 1
    w, u, v = h - 1, 2 * h - 1, 2 * h

    alpha_0 = tuple(range(b))
    alpha_1 = tuple(range(2 * h - 1)) + (v, u)
    alpha_2 = (
        (u,)
        + tuple(range(h - 2, -1, -1))
        + tuple(range(h, 2 * h - 1))
        + (v, w)
    )

    deck_0 = cyclic_deck(alpha_0, h)
    deck_1 = cyclic_deck(alpha_1, h)
    deck_2 = cyclic_deck(alpha_2, h)
    residual = (deck_0 | deck_2) - deck_1

    assert len(deck_0) == len(deck_1) == len(deck_2) == len(residual) == b
    assert not deck_0 & deck_2
    assert deck_1 <= deck_0 | deck_2
    assert deck_0 | deck_2 == deck_1 | residual
    assert not deck_1 & residual

    degrees = [sum(x in edge for edge in residual) for x in range(b)]
    assert degrees == [h] * b

    codegrees = {
        pair: sum(set(pair) <= edge for edge in residual)
        for pair in combinations(range(b), 2)
    }
    top_partners = [
        x
        for x in range(b)
        if x != u and codegrees[tuple(sorted((u, x)))] == h - 1
    ]
    assert top_partners == [w], (h, top_partners)

    region = deck_0 | deck_2

    def distance_graph_stats(family: set[frozenset[int]], distance: int) -> tuple[int, int]:
        vertices = list(family)
        degrees = [
            sum(len(source - target) == distance for target in vertices if target != source)
            for source in vertices
        ]
        return sum(degrees) // 2, max(degrees)

    assert distance_graph_stats(residual, 1) == (b - 2, 2)
    assert distance_graph_stats(residual, h) == (b - 2, 2)
    assert distance_graph_stats(region, 1) == (2 * b + 17, 5)
    assert distance_graph_stats(region, h) == (2 * b + 3, 3)


def main() -> None:
    for h in range(3, 26):
        verify(h)

    # Exact factor of the local h-layer by residual packets for b=7.
    h, b = 3, 7
    w, u, v = h - 1, 2 * h - 1, 2 * h
    alpha_0 = tuple(range(b))
    alpha_1 = tuple(range(2 * h - 1)) + (v, u)
    alpha_2 = (
        (u,)
        + tuple(range(h - 2, -1, -1))
        + tuple(range(h, 2 * h - 1))
        + (v, w)
    )
    residual = (
        cyclic_deck(alpha_0, h) | cyclic_deck(alpha_2, h)
    ) - cyclic_deck(alpha_1, h)
    factor_permutations = (
        (4, 1, 0, 5, 6, 2, 3),
        (2, 4, 3, 6, 1, 5, 0),
        (1, 3, 4, 6, 0, 2, 5),
        (2, 3, 4, 5, 1, 0, 6),
        (5, 0, 1, 6, 3, 4, 2),
    )
    factor = [
        {frozenset(permutation[x] for x in edge) for edge in residual}
        for permutation in factor_permutations
    ]
    assert all(len(packet) == b for packet in factor)
    assert sum(len(packet) for packet in factor) == len(set().union(*factor))
    assert set().union(*factor) == {
        frozenset(edge) for edge in combinations(range(b), h)
    }

    print("GATE_C_ONE_TO_TWO_PRODUCT_ABSORBER_PASS b=7..51")


if __name__ == "__main__":
    main()
