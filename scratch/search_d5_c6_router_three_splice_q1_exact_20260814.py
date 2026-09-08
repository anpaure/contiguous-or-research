#!/usr/bin/env python3
"""Search a local q1-exact three-splice collar for the resident C6 router.

Substantive execution belongs on H100.  For each canonical port cut
P_(i,2)--Q_(i,0), enumerate every commuting-square opposite edge X_i--Y_i
whose cross pairing X_i--P_i,Y_i--Q_i is Johnson.  Search triples for exact
old/new lower and upper q1 multiset equality, owner simplicity, and q1
simplicity on each phase.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import product


def add(base, *values):
    return frozenset(base).union(values)


def sub(base, *values):
    return frozenset(base).difference(values)


def lower(edge):
    a, b = edge
    return a & b


def upper(edge):
    a, b = edge
    return a | b


def is_johnson(a, b):
    return len(a - b) == len(b - a) == 1


def encode(value):
    return "".join(map(str, sorted(value)))


def main():
    ground = frozenset(range(13))
    K = frozenset({0, 1, 2, 3, 4})
    x1, x2 = 0, 1
    y1, y2, z = 5, 6, 7
    active = (8, 9, 10)

    cuts = []
    router_owners = set()
    for i in range(3):
        ai = active[i]
        aj = active[(i + 1) % 3]
        P = add(sub(K, x1, x2), y1, y2, ai, aj)
        Q = add(sub(K, x1, x2), y1, y2, z, ai)
        assert len(P) == len(Q) == 7 and is_johnson(P, Q)
        cuts.append((P, Q))

        A = add(K, z, ai)
        B = add(K, ai, aj)
        P1 = add(sub(K, x1), y1, ai, aj)
        Q1 = add(sub(K, x2), y2, z, ai)
        owners = (A, B, P1, P, Q, Q1)
        assert len(set(owners)) == 6
        router_owners.update(owners)
    assert len(router_owners) == 18

    candidates = []
    for port, (P, Q) in enumerate(cuts):
        common = P & Q
        exterior = ground - (P | Q)
        port_candidates = []
        for c, d in product(sorted(common), sorted(exterior)):
            X = add(sub(P, c), d)
            Y = add(sub(Q, c), d)
            old_edges = ((X, Y), (P, Q))
            new_edges = ((X, P), (Y, Q))
            assert all(is_johnson(*edge) for edge in old_edges + new_edges)
            port_candidates.append({
                "port": port,
                "removed_common": c,
                "added_exterior": d,
                "X": X,
                "Y": Y,
                "old_edges": old_edges,
                "new_edges": new_edges,
            })
        assert len(port_candidates) == len(common) * len(exterior) == 30
        candidates.append(port_candidates)

    checked = 0
    owner_simple = 0
    exact_lower = 0
    exact_both = 0
    witnesses = []
    for choice in product(*candidates):
        checked += 1
        context_owners = [item[key] for item in choice for key in ("X", "Y")]
        if len(set(context_owners)) != 6:
            continue
        if set(context_owners) & router_owners:
            continue
        owner_simple += 1

        old_edges = [edge for item in choice for edge in item["old_edges"]]
        new_edges = [edge for item in choice for edge in item["new_edges"]]
        old_lower = Counter(map(lower, old_edges))
        new_lower = Counter(map(lower, new_edges))
        if old_lower != new_lower:
            continue
        exact_lower += 1
        old_upper = Counter(map(upper, old_edges))
        new_upper = Counter(map(upper, new_edges))
        if old_upper != new_upper:
            continue
        exact_both += 1

        # Require every q1 resource to occur once on each shore.
        if max(old_lower.values()) != 1 or max(old_upper.values()) != 1:
            continue
        if max(new_lower.values()) != 1 or max(new_upper.values()) != 1:
            continue
        witnesses.append({
            "choices": [{
                "port": item["port"],
                "removed_common": item["removed_common"],
                "added_exterior": item["added_exterior"],
                "X": encode(item["X"]),
                "Y": encode(item["Y"]),
            } for item in choice],
            "lower_resources": sorted(map(encode, old_lower)),
            "upper_resources": sorted(map(encode, old_upper)),
        })

    report = {
        "status": "PASS",
        "ground": 13,
        "rank": 7,
        "candidates_per_port": [len(row) for row in candidates],
        "triples_checked": checked,
        "owner_simple_triples": owner_simple,
        "exact_lower_triples": exact_lower,
        "exact_lower_and_upper_triples": exact_both,
        "fully_simple_q1_exact_witnesses": len(witnesses),
        "first_witnesses": witnesses[:10],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
