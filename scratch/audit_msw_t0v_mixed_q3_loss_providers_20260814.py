#!/usr/bin/env python3
"""Trace providers of the mixed tensor's unique base span-four q3 loss.

Substantive execution belongs on H100.  For each Dyck suffix V, enumerate
all old and new linear three-colour windows whose union is
W3[V]=110111001111[V], retaining the four owners, three colours, and old
canonical root/position names.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as tensor


W3 = "110111001111"


def canonical_named(m):
    selected = set()
    names = {}
    for root_word in base.dyck_words(m):
        root = base.bits(root_word)
        owner = root
        assert owner not in names
        names[owner] = (root_word, 0)
        for position in range(m):
            colour = base.g(owner, m)
            next_owner = base.hmap(colour, m)
            selected.add((owner, colour))
            selected.add((next_owner, colour))
            owner = next_owner
            assert owner not in names
            names[owner] = (root_word, position + 1)
    return selected, names


def paths(selected):
    adjacency = defaultdict(list)
    for owner, colour in selected:
        adjacency[(0, owner)].append((1, colour))
        adjacency[(1, colour)].append((0, owner))
    endpoints = [vertex for vertex, neighbours in adjacency.items() if len(neighbours) == 1]
    seen = set()
    result = []
    for start in endpoints:
        if start in seen:
            continue
        vertices = []
        previous = None
        current = start
        while True:
            seen.add(current)
            vertices.append(current)
            following = [vertex for vertex in adjacency[current] if vertex != previous]
            if not following:
                break
            previous, current = current, following[0]
        assert vertices[0][0] == vertices[-1][0] == 0
        owners = [value for kind, value in vertices if kind == 0]
        colours = [value for kind, value in vertices if kind == 1]
        result.append((owners, colours))
    assert len(seen) == len(adjacency)
    return result


def providers(path_bank, names, target, width):
    answer = []
    for path_index, (owners, colours) in enumerate(path_bank):
        for start in range(len(colours) - 2):
            value = colours[start] | colours[start + 1] | colours[start + 2]
            if value != target:
                continue
            answer.append({
                "path_index": path_index,
                "start": start,
                "owners": [base.bitword(value, width) for value in owners[start:start + 4]],
                "owner_names": [names[value] for value in owners[start:start + 4]],
                "colours": [base.bitword(value, width) for value in colours[start:start + 3]],
            })
    return answer


def audit(m):
    canonical, names = canonical_named(m)
    selected = set(canonical)
    packets, _, _, _ = tensor.apply_tensor(selected, m)
    old_paths = paths(canonical)
    new_paths = paths(selected)
    rows = []
    for suffix_word in base.dyck_words(m - 6):
        suffix = base.bits(suffix_word) << 12
        target = base.bits(W3) | suffix
        old = providers(old_paths, names, target, 2 * m)
        new = providers(new_paths, names, target, 2 * m)
        rows.append({
            "suffix": suffix_word,
            "target": base.bitword(target, 2 * m),
            "old_load": len(old),
            "new_load": len(new),
            "old_providers": old,
            "new_providers": new,
        })
    return {
        "m": m,
        "packets": packets,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "runs": [audit(m) for m in args.m]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
