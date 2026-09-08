#!/usr/bin/env python3
"""Rank of q1 currents exposed by every contextual two-gadget C8 packet.

The packet roots are obtained by inserting two independently chosen
1100/1010 blocks at two gaps of an outer Dyck word.  For each four-row
packet we exhaust its universal-C8 component and stream all q1 currents
into sparse modular elimination.  Intended execution environment: H100.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product

from search_b9_c8_switch_path_20260821 import canonical, dyck_words, msw_row, switches


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


@lru_cache(maxsize=None)
def cached_switches(row1, row2, r):
    if row2 < row1:
        row1, row2 = row2, row1
    return tuple(switches(row1, row2, r))


class SparseBasis:
    def __init__(self, prime):
        self.prime = prime
        self.rows = {}

    def add(self, sparse):
        p = self.prime
        row = {i: value % p for i, value in sparse.items() if value % p}
        while row:
            pivot = min(row)
            if pivot not in self.rows:
                inverse = pow(row[pivot], -1, p)
                row = {i: (value * inverse) % p for i, value in row.items()}
                self.rows[pivot] = row
                return True
            coefficient = row[pivot]
            base = self.rows[pivot]
            for i, value in base.items():
                new_value = (row.get(i, 0) - coefficient * value) % p
                if new_value:
                    row[i] = new_value
                elif i in row:
                    del row[i]
        return False

    @property
    def rank(self):
        return len(self.rows)


def current(old_pair, new_pair, target_id, k):
    counts = Counter(x for row in new_pair for x in windows(row, k))
    counts.subtract(x for row in old_pair for x in windows(row, k))
    return {target_id[target]: value for target, value in counts.items() if value}


def packet_states(initial, r, target_id, basis, touched, current_keys):
    queue = deque([initial])
    seen = {initial}
    directed_edges = 0
    while queue:
        state = queue.popleft()
        for i, j in combinations(range(len(state)), 2):
            old_pair = (state[i], state[j])
            for new_pair in cached_switches(state[i], state[j], r):
                directed_edges += 1
                delta = current(old_pair, new_pair, target_id, r - 1)
                if delta:
                    first = min(delta)
                    if delta[first] < 0:
                        delta = {x: -value for x, value in delta.items()}
                    key = tuple(sorted(delta.items()))
                    if key not in current_keys:
                        current_keys.add(key)
                        basis.add(delta)
                        touched.update(delta)
                nxt = tuple(
                    sorted(
                        new_pair
                        + tuple(
                            state[t] for t in range(len(state)) if t not in (i, j)
                        )
                    )
                )
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    return len(seen), directed_edges


def weak_gap_tuples(length, parts):
    for cuts in combinations(range(length + parts - 1), parts - 1):
        previous = -1
        answer = []
        for cut in cuts + (length + parts - 1,):
            answer.append(cut - previous - 1)
            previous = cut
        yield tuple(answer)


def run(r, prime, gadgets, show_currents):
    assert r >= 2 * gadgets
    b = 2 * r + 1
    targets = [frozenset(x) for x in combinations(range(1, b + 1), r - 1)]
    target_id = {target: i for i, target in enumerate(targets)}
    basis = SparseBasis(prime)
    touched = set()
    current_keys = set()
    packet_keys = set()
    state_hist = Counter()
    directed_edges = 0
    outer_count = 0
    for outer in dyck_words(r - 2 * gadgets):
        outer_count += 1
        for lengths in weak_gap_tuples(len(outer), gadgets + 1):
            chunks = []
            cursor = 0
            for length in lengths:
                chunks.append(outer[cursor : cursor + length])
                cursor += length
            assert cursor == len(outer)
            roots = []
            for choices in product(("1100", "1010"), repeat=gadgets):
                pieces = [chunks[0]]
                for choice, chunk in zip(choices, chunks[1:]):
                    pieces.extend((choice, chunk))
                roots.append("".join(pieces))
            initial = tuple(sorted(msw_row(root) for root in roots))
            if len(set(initial)) != 2**gadgets or initial in packet_keys:
                continue
            packet_keys.add(initial)
            states, edges = packet_states(
                initial, r, target_id, basis, touched, current_keys
            )
            state_hist[states] += 1
            directed_edges += edges
    catalan_r = len(tuple(dyck_words(r)))
    print(
        {
            "r": r,
            "b": b,
            "gadgets": gadgets,
            "outer_dyck": outer_count,
            "packets": len(packet_keys),
            "packet_state_hist": sorted(state_hist.items()),
            "directed_edges_scanned": directed_edges,
            "distinct_currents": len(current_keys),
            "rank": basis.rank,
            "targets": len(targets),
            "codimension": len(targets) - basis.rank,
            "catalan": catalan_r,
            "codim_over_catalan": (len(targets) - basis.rank) / catalan_r,
            "touched_targets": len(touched),
            "untouched_targets": len(targets) - len(touched),
            "prime": prime,
        },
        flush=True,
    )
    if show_currents:
        for key in sorted(current_keys):
            support = [
                (tuple(sorted(targets[index])), value) for index, value in key
            ]
            core = tuple(sorted(set.intersection(*(set(target) for target, _ in support))))
            pivot = tuple(sorted(set.union(*(set(target) for target, _ in support)) - set(core)))
            print({"current": support, "core": core, "pivot": pivot})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[4, 5, 6, 7, 8])
    parser.add_argument("--prime", type=int, default=1_000_003)
    parser.add_argument("--gadgets", type=int, default=2)
    parser.add_argument("--show-currents", action="store_true")
    args = parser.parse_args()
    for rank in args.r:
        run(rank, args.prime, args.gadgets, args.show_currents)
