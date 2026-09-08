#!/usr/bin/env python3
"""Finite exact audit of the all-split torus fragment boundary profile."""

from collections import Counter
from fractions import Fraction
from math import comb


def cycle(
    b: int, shift_a: int = 0, shift_b: int = 0
) -> list[frozenset[tuple[str, int]]]:
    assert b >= 5 and b % 2 == 1
    h = (b - 1) // 2
    # Phase 0 is B, phase 1 is A, ..., and phase b-1 is B.
    tau = ["B" if phase % 2 == 0 else "A" for phase in range(b)]
    counters = {"A": 0, "B": 0}
    out: list[frozenset[tuple[str, int]]] = []
    for time in range(b * b):
        stream = tau[time % b]
        counters[stream] = (counters[stream] + 1) % b
        a = frozenset(
            ("A", (counters["A"] - h + j + shift_a) % b)
            for j in range(h)
        )
        bb = frozenset(
            ("B", (counters["B"] - (h + 1) + j + shift_b) % b)
            for j in range(h + 1)
        )
        out.append(a | bb)
    assert len(set(out)) == b * b
    return out


def g(length: int, circumference: int, distance: int) -> int:
    return max(0, length - distance) + max(
        0, length - (circumference - distance)
    )


def encoded_cycle_edges(
    vertices: list[frozenset[tuple[str, int]]], b: int
) -> frozenset[tuple[int, int]]:
    encoded = []
    for vertex in vertices:
        mask = 0
        for stream, index in vertex:
            offset = index if stream == "A" else b + index
            mask |= 1 << offset
        encoded.append(mask)
    return frozenset(
        (encoded[i], encoded[(i + 1) % len(encoded)])
        for i in range(len(encoded))
    )


def audit(b: int) -> None:
    vertices = cycle(b)
    m = b * b
    relative_phase_cycles = {
        encoded_cycle_edges(cycle(b, shift_a, shift_b), b)
        for shift_a in range(b)
        for shift_b in range(b)
    }
    assert len(relative_phase_cycles) == b
    distance_profile: dict[int, Counter[int]] = {
        d: Counter() for d in range(1, b)
    }
    for t, source in enumerate(vertices):
        for u, target in enumerate(vertices):
            if u == t:
                continue
            johnson = len(source - target)
            cyclic = min((u - t) % m, (t - u) % m)
            distance_profile[johnson][cyclic] += 1

    expected_local = [1] + [4 * min(d, b - d) for d in range(1, b)]
    for d in range(1, b):
        assert sum(distance_profile[d].values()) == m * expected_local[d]

    assert distance_profile[1] == Counter(
        {1: 2 * m, 2 * b - 1: b * (b + 1), 2 * b + 1: b * (b - 1)}
    )
    assert distance_profile[b - 1] == Counter(
        {b - 1: b * (b + 1), b: 2 * m, b + 1: b * (b - 1)}
    )

    lo = 2 * b + 1
    hi = m // 2
    for length in sorted({lo, min(hi, lo + 3), hi}):
        if length > hi:
            continue
        normalized: dict[int, Fraction] = {}
        for d in range(1, b):
            total = sum(
                multiplicity * g(length, m, cyclic)
                for cyclic, multiplicity in distance_profile[d].items()
            )
            mean_weight = Fraction(total, m)
            normalized[d] = mean_weight / (length * comb(b, d) ** 2)

        formula_one = Fraction(4 * length - 4 * b - 2, length * b * b)
        formula_one += Fraction(2, length * b * b * b)
        formula_top = Fraction(4 * length - 4 * b, length * b * b)
        formula_top += Fraction(2, length * b * b * b)
        assert normalized[1] == formula_one
        assert normalized[b - 1] == formula_top
        maximum = max(normalized.values())
        assert maximum == normalized[b - 1]
        assert [d for d, value in normalized.items() if value == maximum] == [
            b - 1
        ]

    print(
        f"b={b:2d} M={m:4d} "
        f"d1={dict(sorted(distance_profile[1].items()))} "
        f"dtop={dict(sorted(distance_profile[b - 1].items()))}"
    )


def main() -> None:
    for b in range(5, 32, 2):
        audit(b)
    print("ALL_SPLIT_TORUS_FRAGMENT_PROFILE_AUDIT_PASS")


if __name__ == "__main__":
    main()
