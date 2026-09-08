#!/usr/bin/env python3
"""Search a literal rank-7 central-cut cable/router splice (H100 only)."""

import json
from collections import Counter, defaultdict

import search_d5_rank7_resident_two_channel_cable_router_compatibility_20260814 as src
import audit_d5_cable_router_central_cut_splice_20260814 as aud


def edge_ok(a, b):
    return len(a ^ b) == 2


def key_pair(a, b):
    return (a & b, a | b)


def candidate_splice(cable, router, orientation):
    if orientation == 0:
        if not (edge_ok(router[1][3], cable[4]) and edge_ok(cable[3], router[1][4])):
            return None
    else:
        if not (edge_ok(router[1][3], cable[3]) and edge_ok(cable[4], router[1][4])):
            return None

    old_base = list(router) + [cable]
    old = aud.replace_two(old_base, 1, 3, aud.splice(router[1], 3, cable, 3, orientation))
    fused = aud.new_router_cycle(router)
    p2, q0 = router[1][3], router[1][4]
    cut = next(i for i in range(len(fused)) if {fused[i], fused[(i + 1) % len(fused)]} == {p2, q0})
    new = aud.splice(fused, cut, cable, 3, orientation)
    op, np = aud.palettes(old), aud.palettes(new)
    if op is None or np is None:
        return None
    if not all(len(x) == len(set(x)) for x in op[:3]):
        return None
    if not all(Counter(op[k]) == Counter(np[k]) for k in range(5)):
        return None
    ground = set(range(13))
    old_min = min(
        min(aud.runs(c, ground, False)) for c in old
    ), min(min(aud.runs(c, ground, True)) for c in old)
    new_min = min(
        min(aud.runs(c, ground, False)) for c in new
    ), min(min(aud.runs(c, ground, True)) for c in new)
    if old_min != (3, 2) or new_min != (3, 2):
        return None
    B, E, U, C = router[0][0], router[1][0], router[2][0], cable[0]
    old_map = aud.first_return(old, {B, U, C})
    new_map = aud.first_return(new, {B, U, C})
    if not all(k == v for k, v in old_map.items()):
        return None
    if len(new_map) != 3 or len(set(new_map.values())) != 3:
        return None
    quotient = aud.first_return(new, {B, C})
    if quotient != {B: C, C: B}:
        return None
    return {
        "cable_parameters": cable,
        "router_parameters": router,
        "old": old,
        "new": new,
        "old_map": old_map,
        "new_map": new_map,
    }


def encode(value):
    if isinstance(value, (set, frozenset, list, tuple)):
        return [encode(x) for x in value]
    return value


def main():
    rank = 7
    ground = frozenset(range(13))
    core = frozenset(range(5))
    p, q, r, s = range(5, 9)
    B = core | {p, q}
    C = core | {r, s}
    T = core | {p, r}
    endpoints = [
        core | {left, right}
        for left in (p, q) for right in (r, s)
        if core | {left, right} != T
    ]
    terminals = {T, B, C}
    reports = []
    for endpoint_index, E in enumerate(endpoints):
        cables = src.cable_candidates(ground, C, E, terminals | {E})
        routers = src.router_candidates(ground, B, E, terminals | {E})
        witness = None
        cross_incident = 0
        for orientation in (0, 1):
            for cable_item in cables:
                cable = cable_item["cycle"]
                for router_item in routers:
                    router = router_item["cycles"]
                    if orientation == 0:
                        incidence = edge_ok(router[1][3], cable[4]) and edge_ok(cable[3], router[1][4])
                    else:
                        incidence = edge_ok(router[1][3], cable[3]) and edge_ok(cable[4], router[1][4])
                    if not incidence:
                        continue
                    cross_incident += 1
                    found = candidate_splice(cable, router, orientation)
                    if found is not None:
                        witness = {
                            "orientation": orientation,
                            "cable_parameters": cable_item["parameters"],
                            "router_parameters": router_item["parameters"],
                            "cable_cycle": cable,
                            "router_cycles": router,
                            "old_cycles": found["old"],
                            "new_cycles": found["new"],
                        }
                        break
                if witness is not None:
                    break
            if witness is not None:
                break
        reports.append({
            "endpoint_index": endpoint_index,
            "endpoint": E,
            "cables": len(cables),
            "routers": len(routers),
            "cross_incident_pairs": cross_incident,
            "witness": witness,
        })
        print("endpoint", endpoint_index, "cross", cross_incident, "sat", witness is not None, flush=True)
    print(json.dumps({"status": "PASS", "reports": encode(reports)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
