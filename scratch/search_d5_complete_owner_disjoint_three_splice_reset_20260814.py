#!/usr/bin/env python3
"""Add the second external head to the owner-disjoint cable/router witness.

Run on H100 only.  The input witness already externalizes one router port
through a six-owner cable using two 2-switches.  This search attaches a
second owner-disjoint resident exterior cycle directly to router port zero
by a third ordinary 2-switch.  The third router port remains the hidden
auxiliary.  Suppressing it must swap the two external marks.
"""

import argparse
import json
import random
from itertools import combinations
from collections import Counter
from pathlib import Path

import search_d5_rank7_resident_two_channel_cable_router_compatibility_20260814 as src
import audit_d5_cable_router_central_cut_splice_20260814 as aud
import search_d5_owner_disjoint_double_splice_package_20260814 as pkg


def decode_cycle(value):
    return tuple(frozenset(owner) for owner in value)


def opposite_cycle(rng, ground, target_edge):
    left, right = target_edge
    H = left & right
    u = next(iter(left - right))
    v = next(iter(right - left))
    s = rng.choice(sorted(H))
    t = rng.choice(sorted(ground - H - {u, v}))
    He = (H - {s}) | {t}
    anchor = rng.choice(sorted(He))
    K = He - {anchor}
    x1, x2 = rng.sample(sorted(K), 2)
    available = sorted(ground - K - {u, v, anchor})
    y1, y2 = rng.sample(available, 2)
    cycle = src.port_cycle(K, x1, x2, y1, y2, u, anchor, v)
    pairings = pkg.legal_pairings(target_edge, (cycle[0], cycle[1]))
    assert pairings
    return cycle, pairings, (anchor, x1, x2, y1, y2, u, v, s, t)


def encode(value):
    if isinstance(value, (set, frozenset, tuple, list)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(encode(key)): encode(item) for key, item in value.items()}
    return value


def terminal_choice(exterior_b, exterior_c, all_owners, ground, distance):
    for phase_b, mark_b in enumerate(exterior_b):
        for phase_c, mark_c in enumerate(exterior_c):
            if len(mark_b - mark_c) != distance:
                continue
            for raw_tail in combinations(sorted(ground), len(mark_b)):
                tail = frozenset(raw_tail)
                if tail in all_owners:
                    continue
                if len(tail - mark_b) == len(tail - mark_c) == 1:
                    expected_intersection = len(mark_b) - (1 if distance == 1 else 2)
                    if len(tail & mark_b & mark_c) != expected_intersection:
                        continue
                    if len(tail | mark_b | mark_c) != len(mark_b) + 2:
                        continue
                    return phase_b, phase_c, mark_b, mark_c, tail
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("double_splice_output")
    parser.add_argument("--attempts", type=int, default=1000000)
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--head-distance", type=int, choices=(1, 2))
    args = parser.parse_args()
    data = json.loads(Path(args.double_splice_output).read_text())
    w = data["witness"]
    exterior_c = decode_cycle(w["external_cycle"])
    cable = decode_cycle(w["cable_cycle"])
    router = tuple(decode_cycle(cycle) for cycle in w["router_cycles"])
    additions_c = tuple(tuple(map(frozenset, edge)) for edge in w["additions"])
    cut_index = w["cut_index"]
    ground = frozenset(range(13))
    router_b_edge = (router[0][3], router[0][4])
    router_c_edge = (router[1][3], router[1][4])
    exterior_c_edge = (exterior_c[0], exterior_c[1])
    cable_ext_edge = (cable[0], cable[1])
    cable_router_edge = (cable[cut_index], cable[(cut_index + 1) % 6])

    fixed_owners = set(exterior_c) | set(cable) | set().union(*map(set, router))
    counters = Counter()
    rng = random.Random(args.seed)
    witness = None
    for attempt in range(1, args.attempts + 1):
        exterior_b, pairings_b, parameters = opposite_cycle(rng, ground, router_b_edge)
        if set(exterior_b) & fixed_owners:
            counters["owner_collision"] += 1
            continue
        removals = [
            exterior_c_edge, cable_ext_edge, cable_router_edge, router_c_edge,
            (exterior_b[0], exterior_b[1]), router_b_edge,
        ]
        old_router = list(router)
        new_router = [aud.new_router_cycle(router)]
        for additions_b in pairings_b:
            additions = list(additions_c) + list(additions_b)
            old = pkg.graph_cycles(
                [exterior_b, exterior_c, cable] + old_router,
                removals, additions,
            )
            new = pkg.graph_cycles(
                [exterior_b, exterior_c, cable] + new_router,
                removals, additions,
            )
            if old is None or new is None:
                counters["graph_invalid"] += 1
                continue
            op, np = aud.palettes(old), aud.palettes(new)
            if not all(len(values) == len(set(values)) for values in op[:3]):
                counters["q1_not_simple"] += 1
                continue
            if not all(Counter(op[k]) == Counter(np[k]) for k in range(5)):
                counters["q2_not_equal"] += 1
                continue
            old_min = pkg.minima(old, ground)
            new_min = pkg.minima(new, ground)
            if old_min != (3, 3, 4, 2):
                counters["old_not_resident"] += 1
                continue
            if new_min != (3, 3, 4, 2):
                counters["new_not_resident"] += 1
                continue
            all_owners = set().union(*(set(cycle) for cycle in (exterior_b, exterior_c, cable) + router))
            choice = terminal_choice(
                exterior_b, exterior_c, all_owners, ground, args.head_distance
            ) if args.head_distance else (0, 0, exterior_b[0], exterior_c[0], None)
            if choice is None:
                counters["terminal_type_absent"] += 1
                continue
            phase_b, phase_c, mark_b, mark_c, tail = choice
            mark_u = router[2][0]
            old_map = aud.first_return(old, {mark_b, mark_c, mark_u})
            new_map = aud.first_return(new, {mark_b, mark_c, mark_u})
            if not all(key == value for key, value in old_map.items()):
                counters["old_action_not_identity"] += 1
                continue
            if len(new_map) != 3 or len(set(new_map.values())) != 3:
                counters["new_action_not_cycle"] += 1
                continue
            quotient = aud.first_return(new, {mark_b, mark_c})
            if quotient != {mark_b: mark_c, mark_c: mark_b}:
                counters["marked_quotient_not_swap"] += 1
                continue
            witness = {
                "attempt": attempt,
                "external_b_parameters": parameters,
                "external_b_cycle": exterior_b,
                "external_c_cycle": exterior_c,
                "cable_cycle": cable,
                "router_cycles": router,
                "additions": additions,
                "old_cycles": old,
                "new_cycles": new,
                "old_minima": old_min,
                "new_minima": new_min,
                "old_map": old_map,
                "new_map": new_map,
                "marked_quotient": quotient,
                "terminal_phase_indices": (phase_b, phase_c),
                "terminal_heads": (mark_b, mark_c),
                "terminal_tail": tail,
                "terminal_signature": None if tail is None else (
                    len(tail - mark_b), len(tail - mark_c), len(mark_b - mark_c),
                    len(tail & mark_b & mark_c), len(tail | mark_b | mark_c),
                ),
            }
            break
        if witness is not None:
            break
        if attempt % 100000 == 0:
            print("progress", attempt, dict(counters), flush=True)
    result = {
        "status": "SAT" if witness else "NO_WITNESS_IN_RANDOM_MENU",
        "rank": 7,
        "ground": 13,
        "required_head_distance": args.head_distance,
        "attempts": witness["attempt"] if witness else args.attempts,
        "counters": dict(sorted(counters.items())),
        "witness": witness,
    }
    print(json.dumps(encode(result), indent=2, sort_keys=True))
    if witness is None:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
