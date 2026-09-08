#!/usr/bin/env python3
"""Exact third overlap moment by three-arc Venn signatures.

For a fixed base configuration e,
    M_3(e) = sum_F binom(|e intersect F|, 3)
           = sum_{T in binom(e,3)} deg(T).
The codegree of three fixed targets is obtained by matching their eight
labelled Venn-cell sizes to those of three retained cyclic positional arcs.
No permutation enumeration is used.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter
from fractions import Fraction


def signature(sets: tuple[int, int, int], b: int) -> tuple[int, ...]:
    counts = [0] * 8
    for point in range(b):
        cell = sum(((sets[j] >> point) & 1) << j for j in range(3))
        counts[cell] += 1
    return tuple(counts)


def positional_signatures(lengths: tuple[int, int, int], b: int) -> Counter[tuple[int, ...]]:
    windows = {}
    all_mask = (1 << b) - 1
    for length in set(lengths):
        rows = []
        for start in range(1, b):
            mask = 0
            for offset in range(length):
                mask |= 1 << ((start + offset) % b)
            rows.append(mask & all_mask)
        windows[length] = rows
    answer: Counter[tuple[int, ...]] = Counter()
    for starts in itertools.product(range(b - 1), repeat=3):
        arcs = tuple(windows[lengths[j]][starts[j]] for j in range(3))
        answer[signature(arcs, b)] += 1
    return answer


def base_vertices(r: int) -> list[tuple[int, int]]:
    b = 2 * r + 1
    rows = []
    for length in (r, r - 1):
        for start in range(1, b):
            mask = 0
            for offset in range(length):
                mask |= 1 << ((start + offset) % b)
            rows.append((length, mask))
    assert len(rows) == 4 * r
    return rows


def third_moment(
    r: int,
) -> tuple[
    int,
    Counter[tuple[int, int]],
    Counter[tuple[tuple[int, int, int], tuple[int, ...]]],
    dict[tuple[tuple[int, int, int], tuple[int, ...]], tuple[int, int, int]],
    dict[int, int],
]:
    b = 2 * r + 1
    vertices = base_vertices(r)
    length_patterns = (
        (r, r, r),
        (r, r, r - 1),
        (r, r - 1, r - 1),
        (r - 1, r - 1, r - 1),
    )
    positional = {lengths: positional_signatures(lengths, b) for lengths in length_patterns}
    answer = 0
    parts: Counter[tuple[int, int]] = Counter()
    signatures: Counter[tuple[tuple[int, int, int], tuple[int, ...]]] = Counter()
    signature_meta: dict[
        tuple[tuple[int, int, int], tuple[int, ...]], tuple[int, int, int]
    ] = {}
    max_codegree_by_components: dict[int, int] = {}
    for indices in itertools.combinations(range(4 * r), 3):
        triple = tuple(vertices[index] for index in indices)
        lengths = tuple(row[0] for row in triple)
        target_signature = signature(tuple(row[1] for row in triple), b)
        placements = positional[lengths][target_signature]
        labelings = math.prod(math.factorial(size) for size in target_signature)
        contribution = placements * labelings
        answer += contribution
        skeleton_edges = 0
        for left, right in itertools.combinations(triple, 2):
            left_length, left_mask = left
            right_length, right_mask = right
            if left_length == right_length == r and left_mask & right_mask == 0:
                skeleton_edges += 1
            elif left_length != right_length:
                lower_mask = left_mask if left_length == r - 1 else right_mask
                middle_mask = right_mask if left_length == r - 1 else left_mask
                skeleton_edges += lower_mask & middle_mask == lower_mask
        lower_count = sum(length == r - 1 for length, _ in triple)
        parts[(lower_count, skeleton_edges)] += contribution
        components = 3 - skeleton_edges
        max_codegree_by_components[components] = max(
            max_codegree_by_components.get(components, 0),
            placements * labelings,
        )
        signature_key = (lengths, target_signature)
        signatures[signature_key] += contribution
        if signature_key in signature_meta:
            multiplicity, old_placements, old_labelings = signature_meta[signature_key]
            assert (old_placements, old_labelings) == (placements, labelings)
            signature_meta[signature_key] = (multiplicity + 1, placements, labelings)
        else:
            signature_meta[signature_key] = (1, placements, labelings)
    return answer, parts, signatures, signature_meta, max_codegree_by_components


def main(first: int, last: int) -> None:
    scaled_history: list[tuple[int, dict[tuple[int, int], Fraction]]] = []
    for r in range(first, last + 1):
        moment, parts, signatures, signature_meta, max_by_components = third_moment(r)
        degree_middle = 2 * r * math.factorial(r) * math.factorial(r + 1)
        normalized = Fraction(moment, degree_middle)
        scaled_history.append((
            r,
            {key: r * r * Fraction(value, degree_middle) for key, value in parts.items()},
        ))
        print({
            "r": r,
            "M3": moment,
            "M3_over_D_M": str(normalized),
            "r_M3_over_D_M": str(r * normalized),
            "float": float(normalized),
            "parts_over_D_M": {
                str(key): str(Fraction(value, degree_middle))
                for key, value in sorted(parts.items())
            },
            "scaled_max_codegree": {
                str(components): str(
                    Fraction(
                        value * r ** (components + 1),
                        degree_middle,
                    )
                )
                for components, value in sorted(max_by_components.items())
            },
        }, flush=True)
        if first == last:
            degree_middle = 2 * r * math.factorial(r) * math.factorial(r + 1)
            top = sorted(signatures.items(), key=lambda row: row[1], reverse=True)[:30]
            for (lengths, venn), value in top:
                multiplicity, placements, labelings = signature_meta[(lengths, venn)]
                print({
                    "lengths": lengths,
                    "venn": venn,
                    "target_multiplicity": multiplicity,
                    "retained_start_placements": placements,
                    "labelings": labelings,
                    "contribution_over_D_M": str(Fraction(value, degree_middle)),
                }, flush=True)
    if len(scaled_history) >= 3:
        rows = scaled_history[-3:]
        extrapolated = {}
        for key in sorted(set().union(*(values for _, values in rows))):
            total = Fraction()
            for index, (r, values) in enumerate(rows):
                x = Fraction(1, r)
                coefficient = Fraction(1)
                for other_index, (other_r, _) in enumerate(rows):
                    if other_index == index:
                        continue
                    other_x = Fraction(1, other_r)
                    coefficient *= -other_x / (x - other_x)
                total += coefficient * values.get(key, Fraction())
            extrapolated[str(key)] = {"exact": str(total), "float": float(total)}
        print({"quadratic_in_1_over_r_extrapolated_r2_parts": extrapolated}, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=int, default=2)
    parser.add_argument("--last", type=int, default=20)
    arguments = parser.parse_args()
    main(arguments.first, arguments.last)
