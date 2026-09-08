#!/usr/bin/env python3
"""Audit the direct punctured-configuration near-clone classification.

Two independent checks are performed.

1. Full permutation enumeration for r=3,4.
2. Polynomial containment-path reconstruction for a configurable range of r.

The second check removes d vertices from the identity containment path,
arranges/orients the resulting path components together with d placeholders,
recovers every forced word position from complete same-start pairs, enumerates
the at most (d+1)! remaining label assignments, and checks the resulting deck.
It therefore mirrors the analytic fixed-defect reconstruction proof rather
than scanning all (2r+1)! words.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter
from math import comb, factorial

Vertex = tuple[int, frozenset[int]]
Word = tuple[int, ...]


def path(word: Word, r: int) -> tuple[Vertex, ...]:
    """Canonical path L_1,M_1,...,L_2r,M_2r."""

    b = 2 * r + 1
    return tuple(
        (length, frozenset(word[(start + offset) % b] for offset in range(length)))
        for start in range(1, b)
        for length in (r - 1, r)
    )


def edge(word: Word, r: int) -> frozenset[Vertex]:
    result = frozenset(path(word, r))
    assert len(result) == 4 * r
    return result


def rho(s: int, b: int) -> Word:
    return tuple((s + j) % b for j in range(b))


def tau(s: int, b: int) -> Word:
    return tuple((s - j) % b for j in range(b))


def exceptional_minus(b: int) -> Word:
    return (0, *range(b - 2, 0, -1), b - 1)


def exceptional_plus(b: int) -> Word:
    return (b - 1, *range(1, b - 1), 0)


def predicted_words(r: int) -> dict[Word, int]:
    """Word -> exact defect for all configurations of defect at most two."""

    b = 2 * r + 1
    answer: dict[Word, int] = {}

    def insert(word: Word, defect: int) -> None:
        assert word not in answer
        answer[word] = defect

    insert(rho(0, b), 0)
    insert(tau(r - 2, b), 1)
    insert(tau(r - 1, b), 1)
    for s in range(1, b):
        insert(rho(s, b), 2)
    for s in range(b):
        if s not in (r - 2, r - 1):
            insert(tau(s, b), 2)
    insert(exceptional_minus(b), 2)
    insert(exceptional_plus(b), 2)
    assert Counter(answer.values()) == Counter({0: 1, 1: 2, 2: 4 * r + 1})
    return answer


def defect(word: Word, r: int, base: frozenset[Vertex] | None = None) -> int:
    if base is None:
        base = edge(tuple(range(2 * r + 1)), r)
    return 4 * r - len(base & edge(word, r))


def audit_intrinsic_middle_path(r: int) -> None:
    """Check the explicit step-r middle-disjointness path and endpoint seams."""

    b = 2 * r + 1
    middle = {
        i: frozenset((i + offset) % b for offset in range(r))
        for i in range(1, b)
    }
    order: list[int] = []
    for offset in range(r):
        order.extend((r - offset, 2 * r - offset))
    assert sorted(order) == list(range(1, b))
    for rank, index in enumerate(order):
        expected_rank = 2 * (r - index) if index <= r else 4 * r - 2 * index + 1
        assert rank == expected_rank

    path_edges = {
        frozenset((order[position], order[position + 1]))
        for position in range(len(order) - 1)
    }
    actual_edges = {
        frozenset((i, j))
        for i in range(1, b)
        for j in range(i + 1, b)
        if middle[i].isdisjoint(middle[j])
    }
    assert actual_edges == path_edges

    common = {i: target for i, target in middle.items() if i != r + 1}
    middle_minus = frozenset((*range(1, r), b - 1))
    middle_plus = frozenset((0, *range(r + 1, b - 1)))
    assert [i for i, target in common.items() if middle_minus.isdisjoint(target)] == [r]
    assert [i for i, target in common.items() if middle_plus.isdisjoint(target)] == [1]


def common_components(n: int, missing: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    missing_set = set(missing)
    components: list[tuple[int, ...]] = []
    pos = 0
    while pos < n:
        if pos in missing_set:
            pos += 1
            continue
        end = pos
        while end + 1 < n and end + 1 not in missing_set:
            end += 1
        components.append(tuple(range(pos, end + 1)))
        pos = end + 1
    return tuple(components)


def reconstruct_at_defect(r: int, d: int) -> set[Word]:
    """Exhaust all canonical containment-path templates at exact defect d."""

    b = 2 * r + 1
    n = 4 * r
    identity = tuple(range(b))
    base_path = path(identity, r)
    base = frozenset(base_path)
    base_index = {vertex: i for i, vertex in enumerate(base_path)}
    found: set[Word] = set()

    for missing in itertools.combinations(range(n), d):
        components = common_components(n, missing)
        c = len(components)
        # Component atoms are 0,...,c-1.  The d labelled placeholder atoms
        # are c,...,c+d-1.  Labelling placeholders only overcounts templates.
        for atom_order in itertools.permutations(range(c + d)):
            # Two different common components cannot touch in the other path:
            # that would add an intrinsic containment edge absent from the
            # induced common graph.
            if any(
                atom_order[j] < c and atom_order[j + 1] < c
                for j in range(c + d - 1)
            ):
                continue
            for reverse_bits in itertools.product((False, True), repeat=c):
                template: list[int | None] = []
                for atom in atom_order:
                    if atom < c:
                        block = components[atom]
                        if reverse_bits[atom]:
                            block = block[::-1]
                        template.extend(block)
                    else:
                        template.append(None)
                assert len(template) == n

                # Canonical path positions alternate lower,middle.  Base-path
                # indices have the same parity/layer convention.
                if any(
                    old_index is not None and old_index % 2 != position % 2
                    for position, old_index in enumerate(template)
                ):
                    continue

                # Every complete canonical same-start pair determines one
                # word position via M_i \ L_i = {w_{i+r-1}}.
                fixed: dict[int, int] = {}
                valid = True
                for pair_index in range(2 * r):
                    lower_index = template[2 * pair_index]
                    middle_index = template[2 * pair_index + 1]
                    if lower_index is None or middle_index is None:
                        continue
                    lower = base_path[lower_index][1]
                    middle = base_path[middle_index][1]
                    difference = middle - lower
                    if len(difference) != 1:
                        valid = False
                        break
                    position = (pair_index + r) % b
                    value = next(iter(difference))
                    if position in fixed and fixed[position] != value:
                        valid = False
                        break
                    fixed[position] = value
                if not valid or len(set(fixed.values())) != len(fixed):
                    continue

                unknown_positions = [position for position in range(b) if position not in fixed]
                unknown_values = [value for value in range(b) if value not in fixed.values()]
                assert len(unknown_positions) == len(unknown_values)
                assert len(unknown_positions) <= d + 1

                wildcard_template = tuple(template)
                for assignment in itertools.permutations(unknown_values):
                    word_list: list[int | None] = [None] * b
                    for position, value in fixed.items():
                        word_list[position] = value
                    for position, value in zip(unknown_positions, assignment):
                        word_list[position] = value
                    assert all(value is not None for value in word_list)
                    word = tuple(int(value) for value in word_list)

                    actual_path = path(word, r)
                    actual_template = tuple(base_index.get(vertex) for vertex in actual_path)
                    if actual_template != wildcard_template:
                        continue
                    assert defect(word, r, base) == d
                    found.add(word)
    return found


def audit_reconstruction(max_r: int) -> None:
    for r in range(3, max_r + 1):
        audit_intrinsic_middle_path(r)
        expected = predicted_words(r)
        base = edge(tuple(range(2 * r + 1)), r)
        for word, expected_defect in expected.items():
            assert defect(word, r, base) == expected_defect

        reconstructed: dict[Word, int] = {}
        for d in range(3):
            words = reconstruct_at_defect(r, d)
            for word in words:
                assert word not in reconstructed
                reconstructed[word] = d
        assert reconstructed == expected

        bound_d2 = comb(4 * r, 2) * 2**3 * factorial(5) * factorial(3)
        assert len(reconstruct_at_defect(r, 2)) <= bound_d2
        print(
            f"PATH_RECONSTRUCTION r={r} "
            f"counts=1,2,{4*r+1} bound_d2={bound_d2} PASS"
        )


def audit_exhaustive(r: int) -> None:
    b = 2 * r + 1
    base = edge(tuple(range(b)), r)
    actual: dict[Word, int] = {}
    high_histogram: Counter[int] = Counter()
    for word in itertools.permutations(range(b)):
        d = defect(word, r, base)
        if d <= 2:
            actual[word] = d
            high_histogram[d] += 1
    expected = predicted_words(r)
    assert actual == expected
    assert high_histogram == Counter({0: 1, 1: 2, 2: 4 * r + 1})
    print(f"FULL_PERMUTATION r={r} words={factorial(b)} histogram={dict(high_histogram)} PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-reconstruction-r", type=int, default=12)
    parser.add_argument("--max-exhaustive-r", type=int, default=4)
    arguments = parser.parse_args()

    audit_reconstruction(arguments.max_reconstruction_r)
    for r in range(3, arguments.max_exhaustive_r + 1):
        audit_exhaustive(r)
    print("PUNCTURED_NEAR_CLONE_AUDIT PASS")


if __name__ == "__main__":
    main()
