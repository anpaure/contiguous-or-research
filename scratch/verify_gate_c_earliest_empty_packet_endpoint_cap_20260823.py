#!/usr/bin/env python3
"""Finite audit for the earliest-empty phase-packet endpoint cap.

The proof in the accompanying note is symbolic.  This script independently
checks its two finite combinatorial inputs:

1. the exact doubled-pair histogram of S_(m,r); and
2. the position cap for every partial matching of constrained coordinate
   pairs among the 2m packet slots, through m=6.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb, log


def active(slot: int, i: int, m: int) -> bool:
    """Whether x_1..x_m,y_1..y_m slot is in internal core C_i (1-based i)."""
    if slot < m:  # x_(slot+1)
        return slot + 1 >= i
    return slot - m + 1 <= i  # y_(slot-m+1)


def partial_matchings(vertices: tuple[int, ...]):
    """Yield every (not necessarily perfect) matching on the vertex tuple."""
    if not vertices:
        yield ()
        return
    first = vertices[0]
    rest = vertices[1:]
    # first is unconstrained
    for tail in partial_matchings(rest):
        yield tail
    # first belongs to one constrained pair
    for index, second in enumerate(rest):
        remaining = rest[:index] + rest[index + 1 :]
        for tail in partial_matchings(remaining):
            yield ((first, second),) + tail


def audit_position_cap(max_m: int = 6) -> int:
    checked_safe = 0
    for m in range(1, max_m + 1):
        for matching in partial_matchings(tuple(range(2 * m))):
            safe = all(
                all(active(a, i, m) or active(b, i, m) for i in range(1, m + 1))
                for a, b in matching
            )
            if not safe:
                continue
            checked_safe += 1
            doubled = []
            for i in range(1, m + 1):
                value = sum(active(a, i, m) and active(b, i, m) for a, b in matching)
                doubled.append(value)
                assert value <= 1 + min(i, m + 1 - i), (m, matching, i, value)
            assert doubled[0] <= 2 and doubled[-1] <= 2
    return checked_safe


def brute_histogram(m: int, r: int) -> Counter[int]:
    result: Counter[int] = Counter()
    for chosen in combinations(range(2 * m), m + 1):
        mask = sum(1 << value for value in chosen)
        if any(not (mask & (3 << (2 * h))) for h in range(r)):
            continue
        doubled = sum((mask & (3 << (2 * h))) == (3 << (2 * h)) for h in range(r))
        result[doubled] += 1
    return result


def formula_histogram(m: int, r: int) -> Counter[int]:
    n = m - r
    return Counter(
        {
            d: comb(r, d) * 2 ** (r - d) * comb(2 * n, n + 1 - d)
            for d in range(r + 1)
            if 0 <= n + 1 - d <= 2 * n
        }
    )


def explicit_safe_extension(m: int, r: int, core: int) -> tuple[int, list[int]]:
    """Construct Lemma 2.2's slots and return its position and core sequence."""
    doubled = [h for h in range(r) if core & (3 << (2 * h)) == 3 << (2 * h)]
    split = [h for h in range(r) if h not in doubled]
    d = len(doubled)
    assert r + d <= m - 1
    i = d + 1
    slots: list[int | None] = [None] * (2 * m)

    for k, h in enumerate(doubled):
        a, b = 2 * h, 2 * h + 1
        slots[m + k] = a  # y_(k+1)
        slots[(i + k) - 1] = b  # x_(i+k)

    for k, h in enumerate(split):
        a, b = 2 * h, 2 * h + 1
        selected, unselected = (a, b) if core >> a & 1 else (b, a)
        t = i + d + k
        slots[t - 1] = selected  # x_t
        slots[m + t] = unselected  # y_(t+1)

    constrained = set(range(2 * r))
    free_inside = [v for v in range(2 * m) if v not in constrained and core >> v & 1]
    free_outside = [v for v in range(2 * m) if v not in constrained and not (core >> v & 1)]
    active_empty = [s for s, value in enumerate(slots) if value is None and active(s, i, m)]
    inactive_empty = [s for s, value in enumerate(slots) if value is None and not active(s, i, m)]
    assert len(active_empty) == len(free_inside)
    assert len(inactive_empty) == len(free_outside)
    for slot, value in zip(active_empty, free_inside):
        slots[slot] = value
    for slot, value in zip(inactive_empty, free_outside):
        slots[slot] = value
    assert all(value is not None for value in slots)

    concrete = [int(value) for value in slots]
    cores = [
        sum(1 << concrete[s] for s in range(2 * m) if active(s, position, m))
        for position in range(1, m + 1)
    ]
    assert cores[i - 1] == core
    assert all(all(value & (3 << (2 * h)) for h in range(r)) for value in cores)
    return i, cores


def audit_histograms(max_m: int = 8) -> int:
    cases = 0
    for m in range(1, max_m + 1):
        for r in range(m + 1):
            actual = brute_histogram(m, r)
            expected = formula_histogram(m, r)
            assert actual == expected, (m, r, actual, expected)
            cases += 1
    return cases


def audit_explicit_extensions(max_m: int = 8) -> int:
    cases = 0
    for m in range(2, max_m + 1):
        for r in range(m + 1):
            for chosen in combinations(range(2 * m), m + 1):
                core = sum(1 << value for value in chosen)
                if any(not (core & (3 << (2 * h))) for h in range(r)):
                    continue
                d = sum(core & (3 << (2 * h)) == 3 << (2 * h) for h in range(r))
                if r + d <= m - 1:
                    explicit_safe_extension(m, r, core)
                    cases += 1
    return cases


def main() -> None:
    histogram_cases = audit_histograms()
    safe_matchings = audit_position_cap()
    extension_cases = audit_explicit_extensions()
    threshold = 1 / log(3 / 2)
    print(f"histogram_cases={histogram_cases}")
    print(f"safe_slot_matchings_checked={safe_matchings}")
    print(f"explicit_safe_extensions_checked={extension_cases}")
    print(f"endpoint_threshold_constant={threshold:.12f}")
    print("all earliest-empty endpoint-cap audits passed")


if __name__ == "__main__":
    main()
