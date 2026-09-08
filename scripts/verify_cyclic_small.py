#!/usr/bin/env python3
"""Exact verifier for the small cyclic OR certificates in master section 2.3.

Masks 1,...,31 represent the nonempty subsets of a five-element ground set.
The lower-bound search uses the structural reduction proved in the handoff:

* a mixed length-11 candidate has one block of pair letters and one block of
  singleton letters;
* the singleton block is an edge-simple trail through all five vertices;
* the pair letters, in arbitrary order, are precisely the complementary
  edges of K_5;
* an all-singleton candidate is an arbitrary length-11 cyclic word using all
  five vertices.

Coordinate permutations are quotiented by restricted-growth strings (RGS):
the first occurring singleton is 0, and each later new vertex receives the
next unused label.  In the mixed case the unique singleton block supplies the
distinguished linear start.  In the all-singleton case fixing any cyclic start
can only overcount cyclic equivalence classes, never omit one.
"""

from __future__ import annotations

import hashlib
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Iterable, Iterator, Sequence


K = 5
FULL = (1 << K) - 1
N = 11
EDGES = frozenset(combinations(range(K), 2))
CERTIFICATE = (1, 4, 17, 24, 18, 1, 2, 4, 16, 12, 10, 8)
EXPECTED_TRAILS = (22, 22, 23, 16, 6, 1)
EXPECTED_MIXED = (22, 44, 138, 384, 720, 720)
SEED7 = (3, 5, 64, 20, 36)
SEED9 = (1, 130, 136, 12, 36, 48, 80, 272, 18, 17, 9, 65, 96, 68)
MISSING9 = (59, 118, 199, 219, 236, 285, 355, 365, 398, 433, 438, 472)


def cyclic_unions(word: Sequence[int]) -> set[int]:
    """Return unions of all nonempty cyclic intervals of at most one period."""
    n = len(word)
    seen: set[int] = set()
    for start in range(n):
        union = 0
        for offset in range(n):
            union |= word[(start + offset) % n]
            seen.add(union)
    return seen


def linear_unions(word: Sequence[int]) -> set[int]:
    """Return unions of all nonempty ordinary intervals."""
    ending: set[int] = set()
    seen: set[int] = set()
    for letter in word:
        ending = {letter} | {old | letter for old in ending}
        seen |= ending
    return seen


def rotate_mask(mask: int, dimension: int) -> int:
    return ((mask << 1) & ((1 << dimension) - 1)) | (mask >> (dimension - 1))


def develop(seed: Sequence[int], dimension: int) -> tuple[int, ...]:
    """Concatenate whole coordinate-rotated copies of one seed."""
    block = tuple(seed)
    word: tuple[int, ...] = ()
    for _ in range(dimension):
        word += block
        block = tuple(rotate_mask(x, dimension) for x in block)
    return word


def bordered_lift(word: Sequence[int], dimension: int, border: int) -> tuple[int, ...]:
    """The overlap-sensitive top-bit splice from master equation (2.2)."""
    assert tuple(word[:border]) == tuple(word[-border:]) if border else True
    top = 1 << dimension
    return tuple(word) + (top,) + tuple(x | top for x in word[border:-1])


def rgs_surjections(length: int, alphabet_size: int) -> Iterator[tuple[int, ...]]:
    """Generate canonical words using every symbol, modulo symbol renaming."""
    assert length >= alphabet_size >= 1
    word = [0] * length

    def visit(position: int, maximum: int) -> Iterator[tuple[int, ...]]:
        if position == length:
            if maximum == alphabet_size - 1:
                yield tuple(word)
            return

        # Even one new symbol per remaining position must suffice.
        if maximum + (length - position) < alphabet_size - 1:
            return
        for symbol in range(min(maximum + 1, alphabet_size - 1) + 1):
            word[position] = symbol
            yield from visit(position + 1, max(maximum, symbol))

    yield from visit(1, 0)


def trail_edges(vertices: Sequence[int], cyclic: bool = False) -> list[tuple[int, int]]:
    stop = len(vertices) if cyclic else len(vertices) - 1
    edges = []
    for i in range(stop):
        x, y = vertices[i], vertices[(i + 1) % len(vertices)]
        if x != y:
            edges.append(tuple(sorted((x, y))))
    return edges


def mixed_candidates(pair_count: int) -> Iterable[tuple[int, ...]]:
    """Generate all canonical mixed candidates surviving the rank-two count."""
    singleton_count = N - pair_count
    for trail in rgs_surjections(singleton_count, K):
        used = trail_edges(trail)
        if len(used) != singleton_count - 1 or len(set(used)) != len(used):
            continue
        missing = EDGES.difference(used)
        assert len(missing) == pair_count
        for ordered_pairs in permutations(missing):
            pair_masks = tuple((1 << x) | (1 << y) for x, y in ordered_pairs)
            singleton_masks = tuple(1 << x for x in trail)
            yield pair_masks + singleton_masks


def pad_after(word: Sequence[int], position: int) -> tuple[int, ...]:
    """Insert an adjacent duplicate, which preserves every old cyclic union.

    For an old witnessing arc, include the duplicate exactly when the inserted
    edge lies inside that arc.  Its OR is unchanged because the adjacent old
    letter has the same mask.  Iteration pads any shorter universal cycle to
    length 11.
    """
    assert 0 <= position < len(word)
    return tuple(word[: position + 1]) + (word[position],) + tuple(word[position + 1 :])


def verify_padding_samples() -> None:
    # Exhaust all words of length at most four over the seven nonzero 3-bit
    # masks and every insertion site.  The comment in pad_after is the proof;
    # this assertion protects its implementation and cyclic endpoint cases.
    for length in range(1, 5):
        for word in product(range(1, 8), repeat=length):
            old = cyclic_unions(word)
            for position in range(length):
                assert old <= cyclic_unions(pad_after(word, position))


def main() -> None:
    all_targets = set(range(1, FULL + 1))

    # Positive length-12 certificate.
    assert len(CERTIFICATE) == 12
    assert all(0 < letter <= FULL for letter in CERTIFICATE)
    assert cyclic_unions(CERTIFICATE) == all_targets

    # Mixed length-11 candidates.  The canonical trail and candidate totals
    # are part of the independently checkable enumeration contract.
    trail_totals: list[int] = []
    candidate_totals: list[int] = []
    mixed_universal = 0
    for pair_count in range(1, 7):
        singleton_count = N - pair_count
        trails = 0
        for trail in rgs_surjections(singleton_count, K):
            edges = trail_edges(trail)
            if len(edges) == singleton_count - 1 and len(set(edges)) == len(edges):
                trails += 1
        candidates = 0
        for word in mixed_candidates(pair_count):
            candidates += 1
            assert len(word) == N
            if cyclic_unions(word) == all_targets:
                mixed_universal += 1
        trail_totals.append(trails)
        candidate_totals.append(candidates)

    assert tuple(trail_totals) == EXPECTED_TRAILS
    assert tuple(candidate_totals) == EXPECTED_MIXED
    assert sum(candidate_totals) == 2028
    assert mixed_universal == 0

    # All-singleton candidates.  S(11,5)=246730 canonical surjections.  Only
    # candidates covering all ten pairs can possibly be universal.
    singleton_total = 0
    singleton_pair_complete = 0
    singleton_universal = 0
    for vertices in rgs_surjections(N, K):
        singleton_total += 1
        if set(trail_edges(vertices, cyclic=True)) != EDGES:
            continue
        singleton_pair_complete += 1
        word = tuple(1 << x for x in vertices)
        if cyclic_unions(word) == all_targets:
            singleton_universal += 1

    assert singleton_total == 246730
    assert singleton_pair_complete == 242
    assert singleton_universal == 0

    verify_padding_samples()

    # The human-checkable width cycle for k=7 and its linear consequences.
    word7 = develop(SEED7, 7)
    assert len(word7) == 35
    assert cyclic_unions(word7) == set(range(1, 128))
    linear7 = word7 + SEED7[:2]
    assert len(linear7) == 37
    assert linear_unions(linear7) == set(range(1, 128))
    linear8 = bordered_lift(linear7, 7, 2)
    assert len(linear8) == 72
    assert linear_unions(linear8) == set(range(1, 256))

    # The exact twelve-hole width-length cycle for k=9.
    word9 = develop(SEED9, 9)
    seen9 = cyclic_unions(word9)
    assert len(word9) == 126
    assert tuple(sorted(set(range(1, 512)) - seen9)) == MISSING9
    assert [sum(x.bit_count() == rank for x in seen9) for rank in range(1, 10)] == [
        9, 36, 84, 126, 117, 81, 36, 9, 1
    ]

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("certificate_length=12 certificate_targets=31")
    print(f"mixed_trails={trail_totals}")
    print(f"mixed_candidates={candidate_totals} total={sum(candidate_totals)} universal=0")
    print(
        "singleton_candidates="
        f"{singleton_total} pair_complete={singleton_pair_complete} universal=0"
    )
    print("padding_sample_check=passed")
    print("mu7=35 linear7=37 bordered_lift8=72")
    print("k9_length=126 targets=499 holes=12")
    print(f"sha256={digest}")
    print("VERIFIED: mu(5)=12")


if __name__ == "__main__":
    main()
