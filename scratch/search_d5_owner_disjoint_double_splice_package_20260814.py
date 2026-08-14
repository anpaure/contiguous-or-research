#!/usr/bin/env python3
"""Search the minimal owner-disjoint external--cable--router package.

Run on H100 only.  All connections are ordinary two-edge 2-switches; no
owner is identified.  The external and cable are six-owner resident cycles,
and the router is the 18-owner resident C6 box.  The external splice uses
edge 0 of the cable; the router splice uses a nonincident cable edge and the
phase-common P2--Q0 edge of router port 1.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict

import search_d5_rank7_resident_two_channel_cable_router_compatibility_20260814 as src
import audit_d5_cable_router_central_cut_splice_20260814 as aud


def edge(a, b):
    return len(a ^ b) == 2


def legal_pairings(e, f):
    a, b = e
    x, y = f
    result = []
    if edge(a, x) and edge(b, y):
        result.append(((a, x), (b, y)))
    if edge(a, y) and edge(b, x):
        result.append(((a, y), (b, x)))
    return result


def graph_cycles(cycles, removals, additions):
    adjacency = defaultdict(set)
    for cycle in cycles:
        for i, owner in enumerate(cycle):
            successor = cycle[(i + 1) % len(cycle)]
            adjacency[owner].add(successor)
            adjacency[successor].add(owner)
    for a, b in removals:
        adjacency[a].remove(b)
        adjacency[b].remove(a)
    for a, b in additions:
        if not edge(a, b) or b in adjacency[a]:
            return None
        adjacency[a].add(b)
        adjacency[b].add(a)
    if not all(len(values) == 2 for values in adjacency.values()):
        return None
    seen = set()
    result = []
    for start in adjacency:
        if start in seen:
            continue
        cycle = []
        previous = None
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            neighbors = list(adjacency[current])
            nxt = neighbors[0] if neighbors[0] != previous else neighbors[1]
            previous, current = current, nxt
        if current != start:
            return None
        result.append(cycle)
    return result


def minima(cycles, ground):
    owner = [aud.runs(cycle, ground, False) for cycle in cycles]
    upper = [aud.runs(cycle, ground, True) for cycle in cycles]
    return (
        min(value[0] for value in owner),
        min(value[1] for value in owner),
        min(value[0] for value in upper),
        min(value[1] for value in upper),
    )


def random_cable(rng, ground, exterior_edge):
    left, right = exterior_edge
    H = left & right
    u = next(iter(left - right))
    v = next(iter(right - left))
    s = rng.choice(sorted(H))
    t = rng.choice(sorted(ground - H - {u, v}))
    Hc = (H - {s}) | {t}
    anchor = rng.choice(sorted(Hc))
    K = Hc - {anchor}
    x1, x2 = rng.sample(sorted(K), 2)
    available = sorted(ground - K - {u, v, anchor})
    y1, y2 = rng.sample(available, 2)
    cable = src.port_cycle(K, x1, x2, y1, y2, u, anchor, v)
    assert legal_pairings(exterior_edge, (cable[0], cable[1]))
    return cable, (anchor, x1, x2, y1, y2, u, v, s, t)


def random_router(rng, ground, target_edge):
    left, right = target_edge
    H2 = left & right
    u = next(iter(left - right))
    v = next(iter(right - left))
    s = rng.choice(sorted(H2))
    t = rng.choice(sorted(ground - H2 - {u, v}))
    Hr = (H2 - {s}) | {t}
    a1, y1, y2 = rng.sample(sorted(Hr), 3)
    J = Hr - {a1, y1, y2}
    outside = sorted(ground - Hr - {u, v})
    x1, x2 = rng.sample(outside, 2)
    K = J | {x1, x2}
    candidates = sorted(ground - K - {u, v, a1, y1, y2})
    if not candidates:
        return None
    a0 = rng.choice(candidates)
    z, a2 = (u, v) if rng.randrange(2) == 0 else (v, u)
    active = (a0, a1, a2)
    router = tuple(
        src.port_cycle(K, x1, x2, y1, y2, z, active[i], active[(i + 1) % 3])
        for i in range(3)
    )
    assert {router[1][3], router[1][4]} == {left, right} or legal_pairings(
        target_edge, (router[1][3], router[1][4])
    )
    return router, (z, a0, a1, a2, x1, x2, y1, y2, s, t)


def mapped_action(old, new, marks):
    old_map = aud.first_return(old, marks)
    new_map = aud.first_return(new, marks)
    return old_map, new_map


def encode(value):
    if isinstance(value, (set, frozenset, tuple, list)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(encode(key)): encode(item) for key, item in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempts", type=int, default=2000000)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    ground = frozenset(range(13))
    # Normalized external edge.  Its complete resident cycle is chosen anew
    # at each trial but is owner-disjoint from cable and router.
    H = frozenset(range(6))
    ext_left, ext_right = H | {6}, H | {7}
    ext_candidates = src.cable_candidates(
        ground, ext_left, ext_right, {ext_left, ext_right}
    )
    counters = Counter()
    witness = None
    for attempt in range(1, args.attempts + 1):
        exterior_item = rng.choice(ext_candidates)
        exterior = exterior_item["cycle"]
        cable, cable_parameters = random_cable(rng, ground, (ext_left, ext_right))
        cut_index = rng.choice((2, 3, 4))
        cable_router_edge = (cable[cut_index], cable[(cut_index + 1) % 6])
        router_item = random_router(rng, ground, cable_router_edge)
        if router_item is None:
            counters["router_reverse_empty"] += 1
            continue
        router, router_parameters = router_item
        owner_sets = [set(exterior), set(cable), set().union(*map(set, router))]
        if owner_sets[0] & owner_sets[1] or owner_sets[0] & owner_sets[2] or owner_sets[1] & owner_sets[2]:
            counters["owner_collision"] += 1
            continue
        external_pairings = legal_pairings(
            (ext_left, ext_right), (cable[0], cable[1])
        )
        router_pairings = legal_pairings(
            cable_router_edge, (router[1][3], router[1][4])
        )
        if not router_pairings:
            counters["router_splice_nonincident"] += 1
            continue
        old_router = list(router)
        new_router = [aud.new_router_cycle(router)]
        removals = [
            (ext_left, ext_right),
            (cable[0], cable[1]),
            cable_router_edge,
            (router[1][3], router[1][4]),
        ]
        for external_add in external_pairings:
            for router_add in router_pairings:
                additions = list(external_add + router_add)
                old = graph_cycles([exterior, cable] + old_router, removals, additions)
                new = graph_cycles([exterior, cable] + new_router, removals, additions)
                if old is None or new is None:
                    counters["graph_invalid"] += 1
                    continue
                op, np = aud.palettes(old), aud.palettes(new)
                if op is None or np is None:
                    counters["incidence_invalid"] += 1
                    continue
                if not all(len(values) == len(set(values)) for values in op[:3]):
                    counters["q1_not_simple"] += 1
                    continue
                if not all(Counter(op[k]) == Counter(np[k]) for k in range(5)):
                    counters["q2_not_equal"] += 1
                    continue
                old_min = minima(old, ground)
                new_min = minima(new, ground)
                if old_min[0] < 3 or old_min[1] < 3 or old_min[2] < 4 or old_min[3] < 2:
                    counters["old_not_resident"] += 1
                    continue
                if new_min[0] < 3 or new_min[1] < 3 or new_min[2] < 4 or new_min[3] < 2:
                    counters["new_not_resident"] += 1
                    continue
                marks = {router[0][0], router[2][0], ext_left}
                old_map, new_map = mapped_action(old, new, marks)
                if not all(key == value for key, value in old_map.items()):
                    counters["old_action_not_identity"] += 1
                    continue
                if len(new_map) != 3 or len(set(new_map.values())) != 3:
                    counters["new_action_not_cycle"] += 1
                    continue
                witness = {
                    "attempt": attempt,
                    "cut_index": cut_index,
                    "external_parameters": exterior_item["parameters"],
                    "cable_parameters": cable_parameters,
                    "router_parameters": router_parameters,
                    "external_cycle": exterior,
                    "cable_cycle": cable,
                    "router_cycles": router,
                    "additions": additions,
                    "old_cycles": old,
                    "new_cycles": new,
                    "old_minima": old_min,
                    "new_minima": new_min,
                    "old_map": old_map,
                    "new_map": new_map,
                }
                break
            if witness is not None:
                break
        if witness is not None:
            break
        if attempt % 100000 == 0:
            print("progress", attempt, dict(counters), flush=True)
    result = {
        "status": "SAT" if witness is not None else "NO_WITNESS_IN_RANDOM_MENU",
        "rank": 7,
        "ground": 13,
        "attempts": args.attempts if witness is None else witness["attempt"],
        "counters": dict(sorted(counters.items())),
        "witness": witness,
    }
    print(json.dumps(encode(result), indent=2, sort_keys=True))
    if witness is None:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
