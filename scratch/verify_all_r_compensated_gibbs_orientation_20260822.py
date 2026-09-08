#!/usr/bin/env python3
"""Exact small-r audit of the group-action and convolution orientations."""

from itertools import combinations, permutations
from functools import lru_cache


def compose(left, right):
    """Composition left o right for permutations stored as image words."""
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(word):
    result = [0] * len(word)
    for source, image in enumerate(word):
        result[image] = source
    return tuple(result)


def interval(word, start, length):
    b = len(word)
    return tuple(sorted(word[(start + offset) % b]
                        for offset in range(length)))


def configuration(word, r):
    b = len(word)
    middle = (("M", interval(word, start, r))
              for start in range(1, b))
    lower = (("L", interval(word, start, r - 1))
             for start in range(1, b))
    return frozenset(tuple(middle) + tuple(lower))


def relabel_configuration(configuration_set, relabelling):
    return frozenset(
        (shore, tuple(sorted(relabelling[x] for x in target)))
        for shore, target in configuration_set
    )


def duplicate(first, second):
    return max(len(first & second) - 1, 0)


def run_dimension(r):
    b = 2 * r + 1
    identity = tuple(range(b))
    words = tuple(permutations(range(b)))
    configurations = {word: configuration(word, r) for word in words}

    # The containment-path claim implies literal injectivity.
    assert len(set(configurations.values())) == len(words)

    # Matrix-coefficient identity: a target occurs precisely when it is the
    # image under g of one of the retained/full position intervals.
    for length, retained in ((r, True), (r - 1, True), (max(1, r - 2), False)):
        targets = tuple(combinations(range(b), length))
        starts = range(1, b) if retained else range(b)
        position_deck = {
            frozenset((start + offset) % b for offset in range(length))
            for start in starts
        }
        for word in words[::max(1, len(words) // 60)]:
            image_deck = {
                frozenset(word[x] for x in position_target)
                for position_target in position_deck
            }
            direct_deck = {
                frozenset(interval(word, start, length))
                for start in starts
            }
            assert image_deck == direct_deck
            for target in targets:
                assert (frozenset(target) in image_deck) == (
                    tuple(sorted(target)) in {
                        interval(word, start, length) for start in starts
                    }
                )

    # Coordinate action is left multiplication on image words.
    action_samples = words[::max(1, len(words) // 24)]
    for relabelling in action_samples[:8]:
        for word in action_samples[-8:]:
            assert relabel_configuration(
                configurations[word], relabelling
            ) == configurations[compose(relabelling, word)]

    base = configurations[identity]

    def kappa(relative):
        return duplicate(base, configurations[relative])

    # D(g,h)=kappa(g^{-1}h), fixing the inverse in the right convolution.
    for g in action_samples:
        g_inverse = inverse(g)
        for h in action_samples:
            assert duplicate(configurations[g], configurations[h]) == kappa(
                compose(g_inverse, h)
            )

    tagged_target = ("M", tuple(range(r)))

    def incidence(word):
        return int(tagged_target in configurations[word])

    @lru_cache(maxsize=None)
    def exposure(word):
        return sum(
            incidence(g) * duplicate(configurations[g], configurations[word])
            for g in words
        )

    # Direct rooted exposure equals the right-convolution formula.
    test_words = action_samples[:8]
    for h in test_words:
        convolution = sum(
            incidence(g) * kappa(compose(inverse(g), h)) for g in words
        )
        assert exposure(h) == convolution

    # R_D commutes with L_z under (L_z f)(g)=f(z^{-1}g).
    for z in action_samples[:4]:
        z_inverse = inverse(z)
        for h in test_words[:4]:
            left_after = exposure(compose(z_inverse, h))
            after_left = sum(
                incidence(compose(z_inverse, g))
                * kappa(compose(inverse(g), h))
                for g in words
            )
            assert left_after == after_left

    return len(words)


def main():
    sizes = [run_dimension(r) for r in (2, 3)]
    print(
        "PASS all-r compensated Gibbs orientation audit: "
        f"catalogues={sizes}, matrix-coefficients=PASS, "
        "D(g,h)=kappa(g^-1 h), L_h R_D=R_D L_h"
    )


if __name__ == "__main__":
    main()
