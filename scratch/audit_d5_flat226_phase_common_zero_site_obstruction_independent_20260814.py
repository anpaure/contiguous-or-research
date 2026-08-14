#!/usr/bin/env python3
"""Independent replay of the D5 phase-common zero-site obstruction.

Substantive execution belongs on H100.  This file imports neither the flat
atlas constructor nor the site analyzer.  It rebuilds the canonical m=11
factor, applies T2 and the frozen 41-circuit toggle, verifies the flat word,
finds the moved head tokens of phase-common projected degree zero, and
independently checks the lifted 372-to-1 component action.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from collections import Counter, defaultdict
from pathlib import Path


T2 = [
    ("101010001101", "101011001101", "101010001111"),
    ("100011001101", "100011001111", "101011001101"),
    ("100010001111", "101010001111", "100011001111"),
    ("101011000101", "101011010101", "101011001101"),
    ("101001010101", "101001011101", "101011010101"),
    ("101001001101", "101011001101", "101001011101"),
]


def bits(value: str) -> int:
    return sum((char == "1") << index for index, char in enumerate(value))


def word(value: int, width: int = 22) -> str:
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
    heights = []
    height = down_zero = 0
    for index in range(2 * m):
        heights.append(height)
        if not (value >> index & 1) and height == 0:
            down_zero += 1
        height += 1 if value >> index & 1 else -1
    seen = 0
    for index in range(2 * m):
        if not (value >> index & 1) and heights[index] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return value | 1 << index
    raise AssertionError


def hmap(value: int, m: int) -> int:
    heights = []
    height = up_one = 0
    for index in range(2 * m):
        heights.append(height)
        if value >> index & 1 and height == 1:
            up_one += 1
        height += 1 if value >> index & 1 else -1
    seen = 0
    for index in range(2 * m):
        if value >> index & 1 and heights[index] in (0, 1):
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


def apply_t2(selected, m_suffix: int):
    for suffix_word in dyck_words(m_suffix):
        suffix = bits(suffix_word) << 12
        for owner, old, new in T2:
            old_edge = (bits(owner) | suffix, bits(old) | suffix)
            new_edge = (bits(owner) | suffix, bits(new) | suffix)
            assert old_edge in selected and new_edge not in selected
            selected.remove(old_edge)
            selected.add(new_edge)


def cycle_action(cycle):
    return {
        value: cycle[(index + 1) % len(cycle)]
        for index, value in enumerate(cycle)
    }


def apply_word(value, factors):
    for factor in reversed(factors):
        value = cycle_action(factor).get(value, value)
    return value


def selection_rows(selection):
    cycles = []
    target = {}
    changed_owners = set()
    tokens = set()
    for item in selection["selection"]:
        owners = [bits(value) for value in item["candidate"]["owners"]]
        heads = [bits(value) for value in item["candidate"]["new_colours"]]
        assert len(owners) == len(heads) == len(set(owners)) == len(set(heads))
        assert tokens.isdisjoint(heads)
        tokens.update(heads)
        target.update(cycle_action(heads))
        rows = [
            (owners[index], heads[index - 1], heads[index])
            for index in range(len(owners))
        ]
        for owner, _, _ in rows:
            assert owner not in changed_owners
            changed_owners.add(owner)
        cycles.append(rows)
    assert len(cycles) == 41 and len(tokens) == len(changed_owners) == 477
    return cycles, target, tokens, changed_owners


def restricted_maps(factor, relevant_colours, relevant_owners):
    by_colour = defaultdict(list)
    for owner, colour in factor:
        if colour in relevant_colours:
            by_colour[colour].append(owner)
    incident_owners = set(relevant_owners)
    for owners in by_colour.values():
        incident_owners.update(owners)
    by_owner = defaultdict(list)
    for owner, colour in factor:
        if owner in incident_owners:
            by_owner[owner].append(colour)
    assert all(len(values) == 2 for values in by_colour.values())
    assert all(len(values) in (1, 2) for values in by_owner.values())
    return by_colour, by_owner


class DenseDSU:
    """Dense bit-mask union-find; -1 is absent and roots are <= -2."""

    def __init__(self, universe_size: int):
        self.parent = array("i", [-1]) * universe_size

    def add(self, value: int):
        if self.parent[value] == -1:
            self.parent[value] = -2

    def find(self, value: int) -> int:
        parent = self.parent
        assert parent[value] != -1
        root = value
        while parent[root] >= 0:
            root = parent[root]
        while value != root:
            nxt = parent[value]
            parent[value] = root
            value = nxt
        return root

    def union(self, left: int, right: int):
        self.add(left)
        self.add(right)
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        # More negative means larger.
        if self.parent[left] > self.parent[right]:
            left, right = right, left
        self.parent[left] += self.parent[right] + 1
        self.parent[right] = left


def lifted_dsu(current, canonical, n_even: int):
    z = 1 << n_even
    mask = z - 1
    dsu = DenseDSU(1 << (n_even + 1))
    for owner, colour in current:
        dsu.union(owner, colour)
    endpoint_load = Counter()
    for owner, colour in canonical:
        endpoint_load[owner] += 1
        dsu.union(z | (mask ^ colour), z | (mask ^ owner))
    endpoints = [owner for owner, load in endpoint_load.items() if load == 1]
    for owner in endpoints:
        dsu.union(owner, z | owner)
    return dsu, len(endpoints)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("flat_certificate")
    args = parser.parse_args()

    selection_bytes = Path(args.selection).read_bytes()
    flat_bytes = Path(args.flat_certificate).read_bytes()
    selection = json.loads(selection_bytes)
    flat = json.loads(flat_bytes)
    assert selection["status"] == "SAT" and flat["status"] == "PASS"
    assert flat["selection_sha256"] == hashlib.sha256(selection_bytes).hexdigest()

    cycles, target, tokens, changed_owners = selection_rows(selection)
    factors = [tuple(bits(value) for value in factor) for factor in flat["factors"]]
    appearances = Counter(token for factor in factors for token in factor)
    assert len(factors) == 226 and sum(appearances.values()) == 678
    assert set(appearances) == tokens and max(appearances.values()) == 3
    assert all(apply_word(token, factors) == target[token] for token in tokens)

    canonical = canonical_edges(11)
    pre = set(canonical)
    apply_t2(pre, 5)
    pre_by_colour, pre_by_owner = restricted_maps(pre, tokens, changed_owners)

    post = set(pre)
    for cycle in cycles:
        for owner, old, new in cycle:
            assert (owner, old) in post and (owner, new) not in post
            post.remove((owner, old))
            post.add((owner, new))
    post_by_colour, post_by_owner = restricted_maps(post, tokens, changed_owners)

    common_degrees = {}
    for token in tokens:
        degree = 0
        for owner in set(pre_by_colour[token]) & set(post_by_colour[token]):
            old_pair = tuple(sorted(pre_by_owner.get(owner, ())))
            new_pair = tuple(sorted(post_by_owner.get(owner, ())))
            if len(old_pair) == 2 and old_pair == new_pair:
                degree += 1
        common_degrees[token] = degree
    observed_degrees = Counter(common_degrees.values())
    assert observed_degrees == Counter({1: 457, 0: 20}), observed_degrees
    isolated = sorted(token for token, degree in common_degrees.items() if degree == 0)
    isolated_causes = Counter()
    for token in isolated:
        stable = set(pre_by_colour[token]) & set(post_by_colour[token])
        assert len(stable) == 1
        owner = next(iter(stable))
        if owner in changed_owners:
            isolated_causes["stable_incidence_is_changed_tail_owner"] += 1
        else:
            assert len(pre_by_owner[owner]) == len(post_by_owner[owner]) == 1
            isolated_causes["stable_incidence_is_degree_one_endpoint"] += 1
    isolated_flat_demands = Counter(appearances[token] for token in isolated)

    witness = isolated[0]
    incident = []
    for owner in sorted(set(pre_by_colour[witness]) | set(post_by_colour[witness])):
        old_pair = tuple(sorted(pre_by_owner.get(owner, ())))
        new_pair = tuple(sorted(post_by_owner.get(owner, ())))
        incident.append({
            "edge_owner": word(owner),
            "pre_head_pair": [word(value) for value in old_pair],
            "post_head_pair": [word(value) for value in new_pair],
            "common": old_pair == new_pair and len(old_pair) == 2,
        })
    assert incident and not any(row["common"] for row in incident)
    assert target[witness] != witness and appearances[witness] >= 1

    before_dsu, vertical_endpoints = lifted_dsu(pre, canonical, 22)
    touched_before = {before_dsu.find(owner) for owner in changed_owners}
    del before_dsu
    after_dsu, vertical_endpoints_after = lifted_dsu(post, canonical, 22)
    touched_after = {after_dsu.find(owner) for owner in changed_owners}
    assert vertical_endpoints_after == vertical_endpoints
    assert (len(touched_before), len(touched_after)) == (372, 1)

    report = {
        "status": "PASS_ZERO_SITE_OBSTRUCTION",
        "selection_sha256": hashlib.sha256(selection_bytes).hexdigest(),
        "flat_certificate_sha256": hashlib.sha256(flat_bytes).hexdigest(),
        "flat_word_factors": len(factors),
        "flat_word_port_appearances": sum(appearances.values()),
        "flat_word_maximum_token_appearances": max(appearances.values()),
        "flat_word_product_verified_on_all_477_tokens": True,
        "phase_common_projected_degree_histogram_on_moved_tokens": {
            str(degree): count
            for degree, count in sorted(Counter(common_degrees.values()).items())
        },
        "isolated_moved_tokens": len(isolated),
        "isolated_moved_token_values": [word(token) for token in isolated],
        "isolated_moved_token_cause_histogram": dict(sorted(isolated_causes.items())),
        "isolated_flat_word_port_demand": sum(appearances[token] for token in isolated),
        "isolated_flat_word_demand_histogram": {
            str(demand): count
            for demand, count in sorted(isolated_flat_demands.items())
        },
        "minimum_hall_cut": {"demand": 1, "supply": 0},
        "witness": {
            "token": word(witness),
            "target_image": word(target[witness]),
            "flat_word_appearances": appearances[witness],
            "incident_projected_edges": incident,
        },
        "lifted_touched_components_before": len(touched_before),
        "lifted_touched_components_after": len(touched_after),
        "lifted_component_reduction": len(touched_before) - len(touched_after),
        "canonical_vertical_endpoints": vertical_endpoints,
        "scope": (
            "literal rank-12 head-shore projected Johnson cuts already "
            "present in both frozen phases; added dilation is not excluded"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
