#!/usr/bin/env python3
"""Audit undilated residence of the Catalan T0V two-hex tensor.

Substantive execution belongs on H100.  For each requested semilength this
rebuilds the canonical MSW incidence factor, tensors the two frozen
hexagons over every Dyck suffix, restores the fixed odd lifted closure, and
scans owner and immediate-upper cyclic run/gap minima on both rank shores.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict


def bits(word: str) -> int:
    return sum((char == "1") << index for index, char in enumerate(word))


def bitword(value: int, width: int) -> str:
    return format(value, f"0{width}b")[::-1]


def dyck_words(m: int):
    def rec(position, balance, ones, prefix):
        if position == 2 * m:
            if balance == 0:
                yield "".join(prefix)
            return
        if ones < m:
            prefix.append("1")
            yield from rec(position + 1, balance + 1, ones + 1, prefix)
            prefix.pop()
        zeros = position - ones
        if zeros < ones:
            prefix.append("0")
            yield from rec(position + 1, balance - 1, ones, prefix)
            prefix.pop()

    yield from rec(0, 0, 0, [])


def dyck(value: int, m: int) -> bool:
    height = 0
    for index in range(2 * m):
        height += 1 if value >> index & 1 else -1
        if height < 0:
            return False
    return height == 0


def g(value: int, m: int) -> int:
    before = []
    height = down_zero = 0
    for index in range(2 * m):
        before.append(height)
        if not (value >> index & 1) and height == 0:
            down_zero += 1
        height += 1 if value >> index & 1 else -1
    seen = 0
    for index in range(2 * m):
        if not (value >> index & 1) and before[index] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return value | 1 << index
    raise AssertionError


def hmap(value: int, m: int) -> int:
    before = []
    height = up_one = 0
    for index in range(2 * m):
        before.append(height)
        if value >> index & 1 and height == 1:
            up_one += 1
        height += 1 if value >> index & 1 else -1
    seen = 0
    for index in range(2 * m):
        if value >> index & 1 and before[index] in (0, 1):
            seen += 1
            if seen == up_one:
                return value & ~(1 << index)
    raise AssertionError


def canonical_edges(m: int):
    selected = set()
    for root in range(1 << (2 * m)):
        if root.bit_count() != m or not dyck(root, m):
            continue
        current = root
        for _ in range(m):
            colour = g(current, m)
            nxt = hmap(colour, m)
            selected.add((current, colour))
            selected.add((nxt, colour))
            current = nxt
    return selected


H1 = [
    ("101010001101", "101011001101", "101010001111"),
    ("100011001101", "100011001111", "101011001101"),
    ("100010001111", "101010001111", "100011001111"),
]
H2 = [
    ("101011000101", "101011010101", "101011001101"),
    ("101001010101", "101001011101", "101011010101"),
    ("101001001101", "101011001101", "101001011101"),
]


def apply_tensor(selected, m: int):
    changed_owners = set()
    packets = 0
    for suffix_word in dyck_words(m - 6):
        suffix = bits(suffix_word) << 12
        packets += 1
        for owner, old, new in H1 + H2:
            owner_value = bits(owner) | suffix
            old_edge = (owner_value, bits(old) | suffix)
            new_edge = (owner_value, bits(new) | suffix)
            assert old_edge in selected and new_edge not in selected
            assert owner_value not in changed_owners
            changed_owners.add(owner_value)
            selected.remove(old_edge)
            selected.add(new_edge)
    return packets, changed_owners


def lifted_edges(current, canonical, n_even: int):
    z = 1 << n_even
    mask = z - 1
    edges = list(current)
    edges.extend(
        (z | (mask ^ colour), z | (mask ^ owner))
        for owner, colour in canonical
    )
    owner_load = defaultdict(int)
    for owner, _ in canonical:
        owner_load[owner] += 1
    endpoints = [owner for owner, load in owner_load.items() if load == 1]
    edges.extend((owner, z | owner) for owner in endpoints)
    return edges


def projected_cycles(edges, owner_rank: int):
    by_owner = defaultdict(list)
    by_label = defaultdict(list)
    for left, right in edges:
        if left.bit_count() == owner_rank:
            owner, label = left, right
        else:
            assert right.bit_count() == owner_rank
            owner, label = right, left
        by_owner[owner].append(label)
        by_label[label].append(owner)
    assert all(len(values) == 2 for values in by_owner.values())
    assert all(len(values) == 2 for values in by_label.values())

    seen = set()
    cycles = []
    for start in by_owner:
        if start in seen:
            continue
        owners = []
        owner = start
        previous_label = None
        while True:
            seen.add(owner)
            owners.append(owner)
            label = next(value for value in by_owner[owner] if value != previous_label)
            owner_next = next(value for value in by_label[label] if value != owner)
            previous_label, owner = label, owner_next
            if owner == start:
                break
        cycles.append(owners)
    return cycles


def run_minimum(cycles, ground_size: int, immediate_upper: bool):
    best = {0: ground_size + 1, 1: ground_size + 1}
    witness = {0: None, 1: None}
    for cycle_index, owners in enumerate(cycles):
        trace = owners
        if immediate_upper:
            trace = [
                owners[index] | owners[(index + 1) % len(owners)]
                for index in range(len(owners))
            ]
        length = len(trace)
        for coordinate in range(ground_size):
            values = [int(bool(value >> coordinate & 1)) for value in trace]
            if all(value == values[0] for value in values):
                continue
            for start, value in enumerate(values):
                if values[start - 1] == value:
                    continue
                run = 1
                while values[(start + run) % length] == value:
                    run += 1
                if run < best[value]:
                    best[value] = run
                    witness[value] = {
                        "cycle_index": cycle_index,
                        "cycle_owner_length": len(owners),
                        "coordinate": coordinate,
                        "value": value,
                        "run": run,
                        "trace_window": [
                            bitword(trace[(start + offset) % length], ground_size)
                            for offset in range(-2, run + 2)
                        ],
                        "owner_window": [
                            bitword(owners[(start + offset) % length], ground_size)
                            for offset in range(-2, run + 3)
                        ],
                    }
    return {"minimum": best, "witness": witness}


def audit(m: int):
    canonical = canonical_edges(m)
    selected = set(canonical)
    packets, changed_owners = apply_tensor(selected, m)
    lifted = lifted_edges(selected, canonical, 2 * m)
    shores = {}
    for rank in (m, m + 1):
        cycles = projected_cycles(lifted, rank)
        shores[str(rank)] = {
            "cycles": len(cycles),
            "cycle_length_histogram": {
                str(length): count
                for length, count in sorted(__import__("collections").Counter(
                    map(len, cycles)
                ).items())
            },
            "owner_runs": run_minimum(cycles, 2 * m + 1, False),
            "immediate_upper_runs": run_minimum(cycles, 2 * m + 1, True),
        }
    return {
        "m": m,
        "dyck_suffix_packets": packets,
        "changed_owners": len(changed_owners),
        "expected_component_count": len(list(dyck_words(m))) - 4 * packets,
        "shores": shores,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    assert all(value >= 6 for value in args.m)
    print(json.dumps({"status": "PASS", "runs": [audit(value) for value in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
