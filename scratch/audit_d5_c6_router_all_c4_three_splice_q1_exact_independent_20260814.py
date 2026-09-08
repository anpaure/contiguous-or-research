#!/usr/bin/env python3
"""Independent rank-11 audit of the canonical three-bare-C4 splice census.

Run substantively on H100 only.  Candidate collars are generated from the
closed formula for common neighbours in a Johnson graph, rather than by the
neighbour-pair loops used in the search script.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict


RANK = 11
GROUND_SIZE = 23
GROUND_MASK = (1 << GROUND_SIZE) - 1


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def is_johnson(left, right):
    return (left ^ right).bit_count() == 2


def johnson_neighbours(value):
    outside = GROUND_MASK ^ value
    return {
        value ^ removed ^ inserted
        for removed in bits(value)
        for inserted in bits(outside)
    }


def common_neighbours(left, right):
    """All rank-RANK common Johnson neighbours of two sets at distance <=2."""
    left_only = left & ~right
    right_only = right & ~left
    distance = left_only.bit_count()
    core = left & right
    if distance == 1:
        union = left | right
        values = {core | new for new in bits(GROUND_MASK ^ union)}
        x = next(bits(left_only))
        y = next(bits(right_only))
        values.update((core ^ removed) | x | y for removed in bits(core))
        return values
    if distance == 2:
        return {
            core | x | y for x in bits(left_only) for y in bits(right_only)
        }
    return set()


def delta_signature(old_edges, new_edges, resource):
    delta = Counter(resource(*edge) for edge in new_edges)
    delta.subtract(resource(*edge) for edge in old_edges)
    return tuple(sorted((value, count) for value, count in delta.items() if count))


def add_signatures(*signatures):
    total = Counter()
    for signature in signatures:
        total.update(dict(signature))
    return tuple(sorted((value, count) for value, count in total.items() if count))


def negate(signature):
    return tuple((value, -count) for value, count in signature)


def make_router():
    K = sum(1 << value for value in range(RANK - 2))
    x1, x2 = 0, 1
    y1, y2, z = RANK - 2, RANK - 1, RANK
    active = (RANK + 1, RANK + 2, RANK + 3)

    cuts = []
    owners = set()
    for index, ai in enumerate(active):
        aj = active[(index + 1) % 3]
        P = (K & ~(1 << x1) & ~(1 << x2)) | (1 << y1) | (1 << y2) | (1 << ai) | (1 << aj)
        Q = (K & ~(1 << x1) & ~(1 << x2)) | (1 << y1) | (1 << y2) | (1 << z) | (1 << ai)
        cuts.append((P, Q))
        owners.update((
            K | (1 << z) | (1 << ai),
            K | (1 << ai) | (1 << aj),
            (K & ~(1 << x1)) | (1 << y1) | (1 << ai) | (1 << aj),
            P,
            Q,
            (K & ~(1 << x2)) | (1 << y2) | (1 << z) | (1 << ai),
        ))
    assert len(owners) == 18
    return cuts, owners


def candidates_for_cut(P, Q):
    assert is_johnson(P, Q)
    result = set()
    for X in johnson_neighbours(P) - {Q}:
        for Y in common_neighbours(X, Q) - {P}:
            assert len({P, Q, X, Y}) == 4
            assert is_johnson(P, X)
            assert is_johnson(X, Y)
            assert is_johnson(Y, Q)
            result.add((X, Y))
    expected = ((GROUND_SIZE - 2) * (GROUND_SIZE - 3)
                + 3 * (RANK - 1) * (GROUND_SIZE - RANK - 1))
    assert len(result) == expected == 750
    return sorted(result)


def collar_record(P, Q, X, Y):
    old_edges = ((X, Y), (P, Q))
    new_edges = ((X, P), (Y, Q))
    return {
        "X": X,
        "Y": Y,
        "lower": delta_signature(old_edges, new_edges, lambda a, b: a & b),
        "upper": delta_signature(old_edges, new_edges, lambda a, b: a | b),
    }


def main():
    cuts, router_owners = make_router()
    rows = []
    for P, Q in cuts:
        rows.append([
            collar_record(P, Q, X, Y)
            for X, Y in candidates_for_cut(P, Q)
        ])

    pairs = defaultdict(list)
    for left in rows[0]:
        for middle in rows[1]:
            key = (
                add_signatures(left["lower"], middle["lower"]),
                add_signatures(left["upper"], middle["upper"]),
            )
            pairs[key].append((left, middle))

    exact = 0
    duplicate_context = 0
    router_collision = 0
    six_distinct = 0
    six_distinct_collision = 0
    collision_size_histogram = Counter()
    for right in rows[2]:
        key = (negate(right["lower"]), negate(right["upper"]))
        for left, middle in pairs.get(key, ()):
            exact += 1
            context = [
                value for item in (left, middle, right)
                for value in (item["X"], item["Y"])
            ]
            distinct = len(set(context)) == 6
            collision = set(context) & router_owners
            duplicate_context += not distinct
            six_distinct += distinct
            router_collision += bool(collision)
            six_distinct_collision += distinct and bool(collision)
            collision_size_histogram[len(collision)] += 1

    assert exact == 40
    assert router_collision == exact
    assert six_distinct_collision == six_distinct
    assert exact - duplicate_context - six_distinct_collision == 0

    print(json.dumps({
        "status": "PASS",
        "rank": RANK,
        "ground": GROUND_SIZE,
        "candidate_formula": "(N-2)(N-3)+3(r-1)(N-r-1)",
        "candidates_per_port": list(map(len, rows)),
        "distinct_pair_signatures": len(pairs),
        "exact_lower_upper_q1_matches": exact,
        "duplicate_context_owner_matches": duplicate_context,
        "six_distinct_context_owner_matches": six_distinct,
        "router_collision_matches": router_collision,
        "six_distinct_with_router_collision": six_distinct_collision,
        "owner_simple_matches": 0,
        "collision_size_histogram": dict(sorted(collision_size_histogram.items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
