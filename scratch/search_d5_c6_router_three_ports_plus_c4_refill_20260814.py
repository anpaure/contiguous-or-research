#!/usr/bin/env python3
"""Search three C6-router collars plus one commuting C4 q1 refiller.

Substantive execution belongs on H100.  The router is the canonical rank-7
resident C6 router on 13 labels.  Each port collar ranges over every simple
Johnson C4 about P_(i,2)--Q_(i,0).  The fourth atom ranges over every
oriented commuting Johnson square.  Meet-in-the-middle finds exact aggregate
lower and upper q1 current and then enforces full owner and q1 simplicity.
"""

from __future__ import annotations

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
        (tuple(sorted(value)), coefficient)
        for value, coefficient in delta.items() if coefficient
    ))


def add_signatures(left, right):
    total = Counter({value: coefficient for value, coefficient in left})
    total.update({value: coefficient for value, coefficient in right})
    return tuple(sorted(
        (value, coefficient) for value, coefficient in total.items()
        if coefficient
    ))


def negate(signature):
    return tuple((value, -coefficient) for value, coefficient in signature)


def signature(item):
    return (item["lower_delta"], item["upper_delta"])


def add_joint(left, right):
    return (
        add_signatures(left[0], right[0]),
        add_signatures(left[1], right[1]),
    )


def negate_joint(value):
    return (negate(value[0]), negate(value[1]))


def encode(value):
    return "".join(map(str, sorted(value)))


def make_item(old_edges, new_edges, owners, kind, metadata):
    return {
        "kind": kind,
        "metadata": metadata,
        "owners": tuple(owners),
        "old_edges": tuple(old_edges),
        "new_edges": tuple(new_edges),
        "old_lower": tuple(map(lower, old_edges)),
        "new_lower": tuple(map(lower, new_edges)),
        "old_upper": tuple(map(upper, old_edges)),
        "new_upper": tuple(map(upper, new_edges)),
        "lower_delta": delta_signature(old_edges, new_edges, lower),
        "upper_delta": delta_signature(old_edges, new_edges, upper),
    }


def decode_commuting_refill(joint_signature, rank):
    """Return the unique commuting square for a q1 current, if any."""
    lower_signature, upper_signature = joint_signature
    if len(lower_signature) != 4:
        return None
    if sorted(coefficient for _, coefficient in lower_signature) != [-1, -1, 1, 1]:
        return None
    lower_values = [frozenset(value) for value, _ in lower_signature]
    if any(len(value) != rank - 1 for value in lower_values):
        return None
    core = frozenset.intersection(*lower_values)
    if len(core) != rank - 2:
        return None
    extras = []
    positive = []
    negative = []
    for (value_tuple, coefficient), value in zip(lower_signature, lower_values):
        extra = value - core
        if len(extra) != 1:
            return None
        label = next(iter(extra))
        extras.append(label)
        (positive if coefficient == 1 else negative).append(label)
    if len(set(extras)) != 4:
        return None
    p, q = positive
    s, t = negative

    expected_upper = Counter()
    expected_upper[frozenset(core | {p, s, t})] += 1
    expected_upper[frozenset(core | {q, s, t})] += 1
    expected_upper[frozenset(core | {p, q, s})] -= 1
    expected_upper[frozenset(core | {p, q, t})] -= 1
    expected_signature = tuple(sorted(
        (tuple(sorted(value)), coefficient)
        for value, coefficient in expected_upper.items() if coefficient
    ))
    if expected_signature != upper_signature:
        return None

    A = frozenset(core | {p, s})
    B = frozenset(core | {q, s})
    C = frozenset(core | {p, t})
    D = frozenset(core | {q, t})
    old_edges = ((A, B), (C, D))
    new_edges = ((A, C), (B, D))
    refill = make_item(
        old_edges,
        new_edges,
        (A, B, C, D),
        "refill",
        {
            "core": encode(core),
            "positive_lower_extras": sorted(positive),
            "negative_lower_extras": sorted(negative),
        },
    )
    assert signature(refill) == joint_signature
    return refill


def main():
    ground = frozenset(range(13))
    rank = 7
    K = frozenset(range(rank - 2))
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

    ports = []
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
                row.append(make_item(
                    old_edges,
                    new_edges,
                    (X, Y),
                    "port",
                    {"port": port, "X": encode(X), "Y": encode(Y)},
                ))
        row.sort(key=lambda item: (item["metadata"]["X"], item["metadata"]["Y"]))
        assert len(row) == 200
        ports.append(row)

    pair_index = defaultdict(list)
    for left_index, left in enumerate(ports[0]):
        for middle_index, middle in enumerate(ports[1]):
            pair_index[add_joint(signature(left), signature(middle))].append(
                (left_index, middle_index)
            )

    signature_hits = 0
    owner_simple_hits = 0
    q1_simple_hits = 0
    witnesses = []
    pair_signatures = list(pair_index.items())
    joint_port_signatures_tested = 0
    for right_index, right in enumerate(ports[2]):
        right_signature = signature(right)
        for pair_signature, pair_choices in pair_signatures:
            residual = negate_joint(add_joint(pair_signature, right_signature))
            joint_port_signatures_tested += 1
            refill = decode_commuting_refill(residual, rank)
            if refill is None:
                continue
            signature_hits += len(pair_choices)
            for left_index, middle_index in pair_choices:
                chosen = (ports[0][left_index], ports[1][middle_index], right, refill)
                all_owners = [owner for item in chosen for owner in item["owners"]]
                if len(all_owners) != len(set(all_owners)):
                    continue
                if set(all_owners) & router_owners:
                    continue
                owner_simple_hits += 1
                for family in ("old_lower", "new_lower", "old_upper", "new_upper"):
                    resources = [resource for item in chosen for resource in item[family]]
                    if len(resources) != len(set(resources)):
                        break
                else:
                    q1_simple_hits += 1
                    if len(witnesses) < 20:
                        witnesses.append({
                            "ports": [item["metadata"] for item in chosen[:3]],
                            "refill": refill["metadata"],
                            "refill_owners": [encode(owner) for owner in refill["owners"]],
                        })

    report = {
        "status": "PASS",
        "ground": len(ground),
        "rank": rank,
        "port_candidates": [len(row) for row in ports],
        "joint_port_signatures_tested": joint_port_signatures_tested,
        "signature_hits": signature_hits,
        "owner_simple_hits": owner_simple_hits,
        "fully_q1_simple_hits": q1_simple_hits,
        "first_witnesses": witnesses,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
