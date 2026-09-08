#!/usr/bin/env python3
"""Audit the central-edge 2-switch interpretation of cable/router splicing.

Run on H100 only.  This consumes the three rank-7 closed-bank compatibility
witnesses, cross-splices the cable and the E-router port at their phase-common
P2--Q0 edges, and checks incidence, q1/q2 banks, residence and marked action.
"""

import argparse
import json
from collections import Counter
from pathlib import Path


def fs(values):
    return frozenset(values)


def palettes(cycles):
    result = [[] for _ in range(5)]
    for cycle in cycles:
        for i, owner in enumerate(cycle):
            one = cycle[(i + 1) % len(cycle)]
            two = cycle[(i + 2) % len(cycle)]
            if len(owner ^ one) != 2:
                return None
            result[0].append(owner)
            result[1].append(owner & one)
            result[2].append(owner | one)
            result[3].append(owner & one & two)
            result[4].append(owner | one | two)
    return result


def splice(cycle_a, edge_a, cycle_b, edge_b, crossed):
    """2-switch two directed cyclic edges; return the resulting cycles."""
    def paths_after_cut(cycle, edge):
        i = edge
        # Removed cycle[i]--cycle[i+1], so path is next ... i.
        return cycle[i + 1:] + cycle[:i + 1]

    pa = paths_after_cut(list(cycle_a), edge_a)
    pb = paths_after_cut(list(cycle_b), edge_b)
    if crossed == 0:
        # Add end(pa)--start(pb), end(pb)--start(pa): one joined cycle.
        joined = pa + pb
    else:
        # Reverse the second path before joining.
        joined = pa + list(reversed(pb))
    return [joined]


def replace_two(cycles, ia, ib, merged):
    return [cycle for i, cycle in enumerate(cycles) if i not in (ia, ib)] + merged


def new_router_cycle(router):
    answer = []
    i = 0
    for _ in range(3):
        answer.append(router[i][0])
        j = (i - 1) % 3
        answer.extend(router[j][1:])
        i = j
    return answer


def runs(cycle, ground, upper):
    trace = [
        cycle[i] | cycle[(i + 1) % len(cycle)] for i in range(len(cycle))
    ] if upper else cycle
    mins = {0: len(trace), 1: len(trace)}
    for x in ground:
        word = [int(x in owner) for owner in trace]
        if all(v == word[0] for v in word):
            continue
        for i, value in enumerate(word):
            if value == word[i - 1]:
                continue
            length = 1
            while word[(i + length) % len(word)] == value:
                length += 1
            mins[value] = min(mins[value], length)
    return mins[1], mins[0]


def first_return(cycles, marked):
    answer = {}
    for cycle in cycles:
        present = [x for x in cycle if x in marked]
        for start in present:
            i = cycle.index(start)
            for step in range(1, len(cycle) + 1):
                value = cycle[(i + step) % len(cycle)]
                if value in marked:
                    answer[start] = value
                    break
    return answer


def decode_witness(w):
    cable = [fs(x) for x in w["cable_cycle"]]
    router = [[fs(x) for x in cycle] for cycle in w["router_cycles"]]
    return cable, router


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("compatibility_output")
    args = parser.parse_args()
    data = json.loads(Path(args.compatibility_output).read_text())
    reports = []
    for endpoint_index, report in enumerate(data["endpoint_reports"]):
        cable, router = decode_witness(report["witness"])
        # The compatibility builder fixes B=A0 and E=A1.
        B, E, U = router[0][0], router[1][0], router[2][0]
        C = cable[0]
        assert cable[1] == E
        old_base = router + [cable]
        new_base = [new_router_cycle(router), cable]
        for orientation in (0, 1):
            # Cable and router port 1 have central edge index 3: P2--Q0.
            old_merged = splice(router[1], 3, cable, 3, orientation)
            old = replace_two(old_base, 1, 3, old_merged)
            # Locate P2_1--Q0_1 in the fused router cycle.
            fused = new_base[0]
            p2, q0 = router[1][3], router[1][4]
            cut = next(
                i for i in range(len(fused))
                if {fused[i], fused[(i + 1) % len(fused)]} == {p2, q0}
            )
            new_merged = splice(fused, cut, cable, 3, orientation)
            new = replace_two(new_base, 0, 1, new_merged)
            op, np = palettes(old), palettes(new)
            if op is None or np is None:
                reports.append({"endpoint": endpoint_index, "orientation": orientation, "incidence": False})
                continue
            ground = set().union(*[set(x) for cycle in old for x in cycle])
            simple = [len(x) == len(set(x)) for x in op]
            equal = [Counter(op[k]) == Counter(np[k]) for k in range(5)]
            old_min = (
                min(runs(c, ground, False)[0] for c in old),
                min(runs(c, ground, False)[1] for c in old),
                min(runs(c, ground, True)[0] for c in old),
                min(runs(c, ground, True)[1] for c in old),
            )
            new_min = (
                min(runs(c, ground, False)[0] for c in new),
                min(runs(c, ground, False)[1] for c in new),
                min(runs(c, ground, True)[0] for c in new),
                min(runs(c, ground, True)[1] for c in new),
            )
            old_map = first_return(old, {B, U, C})
            new_map = first_return(new, {B, U, C})
            reports.append({
                "endpoint": endpoint_index,
                "orientation": orientation,
                "incidence": True,
                "components": [list(map(len, old)), list(map(len, new))],
                "simple": simple,
                "phase_equal": equal,
                "old_minima": old_min,
                "new_minima": new_min,
                "old_return": {str(sorted(k)): sorted(v) for k, v in old_map.items()},
                "new_return": {str(sorted(k)): sorted(v) for k, v in new_map.items()},
                "desired_old_identity": all(k == v for k, v in old_map.items()),
                "desired_new_cycle": len(new_map) == 3 and len(set(new_map.values())) == 3,
            })
    print(json.dumps({"status": "AUDIT", "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
