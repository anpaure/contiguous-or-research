#!/usr/bin/env python3
"""Search every simple Johnson-C4 three-splice collar for q1 exactness.

Substantive execution belongs on H100.  Unlike the commuting-square-only
search, this enumerates every edge X--Y for which X--P and Y--Q are Johnson
edges around a fixed router cut P--Q, including the non-induced triangle-type
four-cycles.  It then solves exact aggregate lower/upper q1 current across
the three ports by signature joins rather than a cubic brute force.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict


def add(base, *values):
    return frozenset(base).union(values)


def sub(base, *values):
    return frozenset(base).difference(values)


def is_johnson(a, b):
    return len(a - b) == len(b - a) == 1


def neighbours(value, ground):
    return {
        add(sub(value, removed), inserted)
        for removed in value
        for inserted in ground - value
    }


def lower(edge):
    return edge[0] & edge[1]


def upper(edge):
    return edge[0] | edge[1]


def delta_signature(old_edges, new_edges, resource):
    delta = Counter(map(resource, new_edges))
    delta.subtract(map(resource, old_edges))
    return tuple(sorted(
        ((tuple(sorted(value)), coefficient)
         for value, coefficient in delta.items() if coefficient),
    ))


def negate(signature):
    return tuple((value, -coefficient) for value, coefficient in signature)


def add_signatures(left, right):
    total = Counter({value: coefficient for value, coefficient in left})
    total.update({value: coefficient for value, coefficient in right})
    return tuple(sorted(
        (value, coefficient) for value, coefficient in total.items()
        if coefficient
    ))


def encode(value):
    return "".join(map(str, sorted(value)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, default=7)
    parser.add_argument("--ground", type=int, default=13)
    args = parser.parse_args()
    rank = args.rank
    assert rank >= 5 and args.ground >= rank + 4

    ground = frozenset(range(args.ground))
    K = frozenset(range(rank - 2))
    x1, x2 = 0, 1
    y1, y2, z = rank - 2, rank - 1, rank
    active = (rank + 1, rank + 2, rank + 3)

    cuts = []
    router_owners = set()
    for i in range(3):
        ai = active[i]
        aj = active[(i + 1) % 3]
        P = add(sub(K, x1, x2), y1, y2, ai, aj)
        Q = add(sub(K, x1, x2), y1, y2, z, ai)
        cuts.append((P, Q))
        router_owners.update((
            add(K, z, ai),
            add(K, ai, aj),
            add(sub(K, x1), y1, ai, aj),
            P,
            Q,
            add(sub(K, x2), y2, z, ai),
        ))
    assert len(router_owners) == 18

    candidates = []
    for port, (P, Q) in enumerate(cuts):
        row = []
        for X in neighbours(P, ground):
            if X in (P, Q):
                continue
            for Y in neighbours(Q, ground):
                if Y in (P, Q) or Y == X or not is_johnson(X, Y):
                    continue
                old_edges = ((X, Y), (P, Q))
                new_edges = ((X, P), (Y, Q))
                assert all(is_johnson(*edge) for edge in old_edges + new_edges)
                row.append({
                    "port": port,
                    "X": X,
                    "Y": Y,
                    "lower_delta": delta_signature(old_edges, new_edges, lower),
                    "upper_delta": delta_signature(old_edges, new_edges, upper),
                    "old_lower": tuple(map(lower, old_edges)),
                    "new_lower": tuple(map(lower, new_edges)),
                    "old_upper": tuple(map(upper, old_edges)),
                    "new_upper": tuple(map(upper, new_edges)),
                })
        # Each oriented pair X,Y is a distinct physical collar choice.
        row.sort(key=lambda item: (tuple(sorted(item["X"])), tuple(sorted(item["Y"]))))
        candidates.append(row)

    pair_index = defaultdict(list)
    for left_index, left in enumerate(candidates[0]):
        for middle_index, middle in enumerate(candidates[1]):
            signature = (
                add_signatures(left["lower_delta"], middle["lower_delta"]),
                add_signatures(left["upper_delta"], middle["upper_delta"]),
            )
            pair_index[signature].append((left_index, middle_index))

    signature_matches = 0
    duplicate_context_owner_matches = 0
    router_collision_matches = 0
    six_distinct_context_owner_matches = 0
    six_distinct_with_router_collision = 0
    router_collision_size_histogram = Counter()
    owner_simple = 0
    q1_simple = 0
    witnesses = []
    raw_matches = []
    for right_index, right in enumerate(candidates[2]):
        key = (negate(right["lower_delta"]), negate(right["upper_delta"]))
        for left_index, middle_index in pair_index.get(key, ()):
            signature_matches += 1
            choice = (
                candidates[0][left_index],
                candidates[1][middle_index],
                right,
            )
            context_owners = [item[key2] for item in choice for key2 in ("X", "Y")]
            collisions = set(context_owners) & router_owners
            if len(set(context_owners)) != 6:
                duplicate_context_owner_matches += 1
            else:
                six_distinct_context_owner_matches += 1
            if collisions:
                router_collision_matches += 1
                router_collision_size_histogram[len(collisions)] += 1
                if len(set(context_owners)) == 6:
                    six_distinct_with_router_collision += 1
            if len(raw_matches) < 20:
                raw_matches.append({
                    "choices": [{
                        "port": item["port"],
                        "X": encode(item["X"]),
                        "Y": encode(item["Y"]),
                    } for item in choice],
                    "distinct_context_owners": len(set(context_owners)),
                    "router_owner_collisions": sorted(
                        encode(owner) for owner in collisions
                    ),
                })
            if len(set(context_owners)) != 6:
                continue
            if set(context_owners) & router_owners:
                continue
            owner_simple += 1

            for family in ("old_lower", "new_lower", "old_upper", "new_upper"):
                resources = [resource for item in choice for resource in item[family]]
                if len(resources) != len(set(resources)):
                    break
            else:
                q1_simple += 1
                witnesses.append({
                    "choices": [{
                        "port": item["port"],
                        "X": encode(item["X"]),
                        "Y": encode(item["Y"]),
                    } for item in choice],
                })

    report = {
        "status": "PASS",
        "ground": len(ground),
        "rank": rank,
        "candidates_per_port": [len(row) for row in candidates],
        "distinct_signature_pairs_01": len(pair_index),
        "exact_lower_and_upper_signature_matches": signature_matches,
        "duplicate_context_owner_matches": duplicate_context_owner_matches,
        "router_collision_matches": router_collision_matches,
        "six_distinct_context_owner_matches": six_distinct_context_owner_matches,
        "six_distinct_with_router_collision": six_distinct_with_router_collision,
        "router_collision_size_histogram": dict(sorted(
            router_collision_size_histogram.items()
        )),
        "owner_simple_matches": owner_simple,
        "fully_q1_simple_matches": q1_simple,
        "raw_exact_matches": raw_matches,
        "first_witnesses": witnesses[:20],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
