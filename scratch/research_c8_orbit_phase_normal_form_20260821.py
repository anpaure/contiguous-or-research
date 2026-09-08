#!/usr/bin/env python3
"""Test whether the physical C8 orbit stays in the canonical flaw-layer normal form.

The canonical layer of an r-set is recovered intrinsically from the MSW
factor: the path rooted at the Dyck word visits one set in every layer.
Intended execution environment: H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import combinations
from math import comb

from research_msw_c8_shadow_anneal_20260821 import dyck_words, msw_row, switches


def cyclic_windows(row, r):
    b = len(row)
    return tuple(
        frozenset(row[(start + offset) % b] for offset in range(r))
        for start in range(b)
    )


def odd_cycle(row, r):
    windows = cyclic_windows(row, r)
    b = len(row)
    return tuple(windows[(step * r) % b] for step in range(b))


def rooted_x_path(row, r, root, anchor):
    cycle = odd_cycle(row, r)
    index = cycle.index(root)
    forward_has_anchor = anchor in cycle[(index + 1) % len(cycle)]
    backward_has_anchor = anchor in cycle[(index - 1) % len(cycle)]
    assert forward_has_anchor != backward_has_anchor
    direction = 1 if forward_has_anchor else -1
    path = tuple(cycle[(index + 2 * direction * t) % len(cycle)] for t in range(r + 1))
    assert all(anchor not in target for target in path)
    assert path[-1] == frozenset(set(range(1, 2 * r + 1)) - set(root))
    return path


def canonical_layers(r):
    anchor = 2 * r + 1
    layer = {}
    layer_counts = Counter()
    row_roots = {}
    for word in dyck_words(r):
        row = msw_row(word)
        root = frozenset(i + 1 for i, bit in enumerate(word) if bit == "1")
        path = rooted_x_path(row, r, root, anchor)
        row_roots[row] = root
        for phase, target in enumerate(path):
            assert target not in layer or layer[target] == phase
            layer[target] = phase
            layer_counts[phase] += 1
    assert len(layer) == comb(2 * r, r)
    assert set(layer_counts) == set(range(r + 1))
    return layer, row_roots, layer_counts


def row_signature(row, r, layer):
    anchor = 2 * r + 1
    cycle = odd_cycle(row, r)
    roots = []
    for index, target in enumerate(cycle):
        if anchor in target or layer[target] != 0:
            continue
        forward_has_anchor = anchor in cycle[(index + 1) % len(cycle)]
        backward_has_anchor = anchor in cycle[(index - 1) % len(cycle)]
        if forward_has_anchor != backward_has_anchor:
            roots.append(target)
    signatures = []
    for root in roots:
        path = rooted_x_path(row, r, root, anchor)
        signatures.append(tuple(layer[target] for target in path))
    return tuple(signatures)


def neighbours(state, r):
    for i, j in combinations(range(len(state)), 2):
        left, right = state[i], state[j]
        for new_pair in switches(left, right):
            nxt = tuple(
                sorted(
                    new_pair
                    + tuple(state[t] for t in range(len(state)) if t not in (i, j))
                )
            )
            if len(set(nxt)) == len(state):
                yield nxt


def audit(r, max_states):
    layer, _, layer_counts = canonical_layers(r)
    start = tuple(sorted(msw_row(word) for word in dyck_words(r)))
    queue = deque([start])
    seen = {start}
    state_bad_hist = Counter()
    row_signature_hist = Counter()
    distinct_rows = set()
    while queue and len(seen) <= max_states:
        state = queue.popleft()
        bad_rows = 0
        for row in state:
            signature = row_signature(row, r, layer)
            row_signature_hist[signature] += 1
            distinct_rows.add(row)
            if signature != (tuple(range(r + 1)),):
                bad_rows += 1
        state_bad_hist[bad_rows] += 1
        for nxt in neighbours(state, r):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
                if len(seen) > max_states:
                    break
    distinct_row_hist = Counter(row_signature(row, r, layer) for row in distinct_rows)
    return {
        "r": r,
        "canonical_layer_sizes": dict(layer_counts),
        "states": len(seen),
        "queue_remaining": len(queue),
        "state_bad_row_hist": dict(state_bad_hist),
        "distinct_rows": len(distinct_rows),
        "distinct_row_signature_hist": {
            str(key): value for key, value in distinct_row_hist.items()
        },
        "occurrence_signature_hist": {
            str(key): value for key, value in row_signature_hist.items()
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--max-states", type=int, default=100_000)
    args = parser.parse_args()
    for r in args.r:
        print("C8_ORBIT_PHASE_NORMAL_FORM", audit(r, args.max_states), flush=True)


if __name__ == "__main__":
    main()
