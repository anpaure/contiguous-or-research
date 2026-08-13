#!/usr/bin/env python3
"""Verify the nonuniform two-period protected role-flow construction.

Substantive execution is H100-only.  The default synthetic direction-count
instance satisfies every numerical hypothesis of the theorem; it checks the
role-flow algebra and materializes the lift-sized shell bank by the
slot-clone edge-colouring construction.  It does not assert that the
synthetic direction vector comes from a particular Gray cycle, and it does
not solve the named owner/lower ordering system.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter


def balanced_counts(total: int, count: int, residue: int, modulus: int) -> list[int]:
    assert (total - count * residue) % modulus == 0
    quotient = (total - count * residue) // modulus
    base, extra = divmod(quotient, count)
    return [residue + modulus * (base + (index < extra)) for index in range(count)]


def fill_bounded(total: int, lower: list[int], upper: list[int], step: int = 1) -> list[int]:
    values = lower[:]
    remaining = total - sum(values)
    assert remaining >= 0 and remaining % step == 0
    for index in range(len(values)):
        capacity = upper[index] - values[index]
        increment = min(capacity // step, remaining // step) * step
        values[index] += increment
        remaining -= increment
    assert remaining == 0
    return values


def distribute_stubs(degrees: list[int], slot_count: int, token_count: int) -> list[list[int]]:
    edges = [[0] * len(degrees) for _ in range(slot_count)]
    slot = 0
    capacity = token_count
    for coordinate, degree in enumerate(degrees):
        remaining = degree
        while remaining:
            take = min(remaining, capacity)
            edges[slot][coordinate] += take
            remaining -= take
            capacity -= take
            if capacity == 0:
                slot += 1
                capacity = token_count
    assert slot == slot_count or (slot == slot_count - 1 and capacity == 0)
    assert all(sum(row) == token_count for row in edges)
    return edges


def perfect_matching(matrix: list[list[int]]) -> list[int]:
    size = len(matrix)
    matched_right = [-1] * size

    def augment(left: int, seen: list[bool]) -> bool:
        for right in range(size):
            if matrix[left][right] == 0 or seen[right]:
                continue
            seen[right] = True
            if matched_right[right] < 0 or augment(matched_right[right], seen):
                matched_right[right] = left
                return True
        return False

    for left in range(size):
        assert augment(left, [False] * size)
    matching = [-1] * size
    for right, left in enumerate(matched_right):
        matching[left] = right
    assert all(right >= 0 for right in matching)
    return matching


def slot_clone_shells(
    core_degrees: list[int],
    support_degrees: list[int],
    core_size: int,
    support_size: int,
    token_count: int,
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    coordinate_count = len(core_degrees)
    assert sum(core_degrees) == core_size * token_count
    assert sum(support_degrees) == support_size * token_count
    assert all(
        core_degrees[x] + support_degrees[x] <= token_count
        for x in range(coordinate_count)
    )
    core_rows = distribute_stubs(core_degrees, core_size, token_count)
    support_rows = distribute_stubs(support_degrees, support_size, token_count)
    matrix = core_rows + support_rows
    dummy_count = coordinate_count - core_size - support_size
    assert dummy_count >= 0
    matrix.extend([[0] * coordinate_count for _ in range(dummy_count)])
    deficits = [
        token_count - core_degrees[x] - support_degrees[x]
        for x in range(coordinate_count)
    ]
    dummy_rows = distribute_stubs(deficits, dummy_count, token_count) if dummy_count else []
    for offset, row in enumerate(dummy_rows):
        matrix[core_size + support_size + offset] = row
    assert all(sum(row) == token_count for row in matrix)
    assert all(sum(matrix[row][x] for row in range(coordinate_count)) == token_count for x in range(coordinate_count))

    shells: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for _ in range(token_count):
        matching = perfect_matching(matrix)
        core = tuple(sorted(matching[:core_size]))
        support = tuple(sorted(matching[core_size : core_size + support_size]))
        assert len(set(core)) == core_size
        assert len(set(support)) == support_size
        assert not set(core) & set(support)
        shells.append((core, support))
        for left, right in enumerate(matching):
            matrix[left][right] -= 1
            assert matrix[left][right] >= 0
    assert all(value == 0 for row in matrix for value in row)
    return shells


def verify() -> dict[str, object]:
    p, q = 15, 2
    k, m = 2 * p + 1, 2 * p
    rank = p + 1
    core_size = rank - q
    e = 1 << p
    n = 2 * q + 2
    heavy_period = n + 1
    width = math.comb(k, rank)
    catalan = width // k

    base_even = 2 * (e // (2 * p))
    direction_counts = [base_even] * p
    for index in range((e - sum(direction_counts)) // 2):
        direction_counts[index] += 2
    assert sum(direction_counts) == e
    assert max(direction_counts) <= e // (q + 4)

    support_pair = [count // 2 for count in direction_counts]
    core_pair = [e // 2 - (q - 1) * value for value in support_pair]
    support_defect = [value for value in support_pair for _ in range(2)]
    weighted_core_defect = [value for value in core_pair for _ in range(2)]
    assert sum(support_defect) == e
    assert sum(weighted_core_defect) == core_size * e

    gap = m - (n + 2)
    b0 = max(
        n * n + n - 2,
        math.ceil(m * (n - 1) / core_size),
        math.ceil(2 * gap * n / (gap - core_size)),
    )
    residue = e % n
    heavy_tokens = b0 + ((residue - b0) % n)
    light_tokens = (e - heavy_period * heavy_tokens) // n
    assert heavy_period * heavy_tokens <= e // (n + 6)
    assert m * heavy_tokens < 5 * e / (n + 6)

    eligible = [x for x, value in enumerate(support_defect) if value >= heavy_tokens]
    q_set = eligible[: n + 2]
    assert len(q_set) == n + 2

    residues = [value % n for value in weighted_core_defect]
    heavy_core = residues[:]
    delta = (core_size * heavy_tokens - sum(heavy_core)) // n
    assert delta >= 0
    for x in range(m):
        if x in q_set:
            continue
        capacity = (heavy_tokens - heavy_core[x]) // n
        increment = min(capacity, delta)
        heavy_core[x] += n * increment
        delta -= increment
    assert delta == 0
    assert sum(heavy_core) == core_size * heavy_tokens
    assert all(0 <= value <= heavy_tokens for value in heavy_core)

    heavy_support = [0] * m
    remaining = heavy_period * heavy_tokens
    for x in q_set:
        take = min(heavy_tokens - heavy_core[x], remaining)
        heavy_support[x] = take
        remaining -= take
    assert remaining == 0
    assert all(heavy_support[x] <= support_defect[x] for x in range(m))

    light_core = [
        (weighted_core_defect[x] - heavy_period * heavy_core[x]) // n
        for x in range(m)
    ]
    light_support = [support_defect[x] - heavy_support[x] for x in range(m)]
    assert sum(light_core) == core_size * light_tokens
    assert sum(light_support) == n * light_tokens
    assert all(value >= 0 for value in light_core + light_support)
    assert all(
        light_core[x] + light_support[x] <= light_tokens for x in range(m)
    )

    heavy_shells = slot_clone_shells(
        heavy_core, heavy_support, core_size, heavy_period, heavy_tokens
    )
    light_shells = slot_clone_shells(
        light_core, light_support, core_size, n, light_tokens
    )
    core_check = Counter()
    support_check = Counter()
    for period, shells in ((heavy_period, heavy_shells), (n, light_shells)):
        for core, support in shells:
            for coordinate in core:
                core_check[coordinate] += period
            support_check.update(support)
    assert [support_check[x] for x in range(m)] == support_defect
    assert [core_check[x] for x in range(m)] == weighted_core_defect

    target = width / (2 * n + 1)
    full_heavy = round(target)
    full_heavy += (width - full_heavy) % n
    full_light = (width - heavy_period * full_heavy) // n
    assert n * full_light + heavy_period * full_heavy == width
    assert full_light > light_tokens and full_heavy > heavy_tokens

    core_residue = (core_size * catalan) % n
    full_heavy_core = balanced_counts(
        core_size * full_heavy, k, core_residue, n
    )
    full_light_core = [
        (core_size * catalan - heavy_period * value) // n
        for value in full_heavy_core
    ]
    support_base, support_extra = divmod(heavy_period * full_heavy, k)
    full_heavy_support = [
        support_base + (x < support_extra) for x in range(k)
    ]
    full_light_support = [catalan - value for value in full_heavy_support]
    assert sum(full_heavy_core) == core_size * full_heavy
    assert sum(full_light_core) == core_size * full_light
    assert sum(full_heavy_support) == heavy_period * full_heavy
    assert sum(full_light_support) == n * full_light

    defect_heavy_core = heavy_core + [0]
    defect_heavy_support = heavy_support + [0]
    defect_light_core = light_core + [0]
    defect_light_support = light_support + [0]
    residual_heavy_core = [
        full_heavy_core[x] - defect_heavy_core[x] for x in range(k)
    ]
    residual_heavy_support = [
        full_heavy_support[x] - defect_heavy_support[x] for x in range(k)
    ]
    residual_light_core = [
        full_light_core[x] - defect_light_core[x] for x in range(k)
    ]
    residual_light_support = [
        full_light_support[x] - defect_light_support[x] for x in range(k)
    ]
    assert all(value >= 0 for value in residual_heavy_core + residual_heavy_support + residual_light_core + residual_light_support)
    assert all(
        residual_heavy_core[x] + residual_heavy_support[x]
        <= full_heavy - heavy_tokens
        for x in range(k)
    )
    assert all(
        residual_light_core[x] + residual_light_support[x]
        <= full_light - light_tokens
        for x in range(k)
    )

    digest = hashlib.sha256()
    for period, shells in ((heavy_period, heavy_shells), (n, light_shells)):
        for core, support in shells:
            digest.update(f"{period}:{core}:{support}\n".encode())

    return {
        "status": "PASS",
        "scope": (
            "synthetic direction-count instance satisfying the theorem; "
            "materializes the lift-sized defect shell bank and checks the "
            "balanced padding degree hypotheses; not a Gray-cycle, named-order, "
            "upper-support, or chronology solver"
        ),
        "parameters": {
            "p": p,
            "q": q,
            "k": k,
            "core_size": core_size,
            "periods": [n, heavy_period],
            "lift_size": e,
            "width": width,
        },
        "direction_counts": direction_counts,
        "direction_bound": e // (q + 4),
        "defect_tokens": {str(n): light_tokens, str(heavy_period): heavy_tokens},
        "defect_shell_digest": digest.hexdigest(),
        "support_defect_total": sum(support_defect),
        "weighted_core_defect_total": sum(weighted_core_defect),
        "full_tokens": {str(n): full_light, str(heavy_period): full_heavy},
        "padding_heavy_capacity_margin": min(
            full_heavy
            - heavy_tokens
            - residual_heavy_core[x]
            - residual_heavy_support[x]
            for x in range(k)
        ),
        "padding_light_capacity_margin": min(
            full_light
            - light_tokens
            - residual_light_core[x]
            - residual_light_support[x]
            for x in range(k)
        ),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))

