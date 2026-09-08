#!/usr/bin/env python3
"""Search rank-7 compatibility of a resident doubled lead and marked C6.

Substantive execution belongs on H100 only.  The search fixes a normalized
distance-two D5 terminal triple, tries each of its three unused common
neighbours E, enumerates all six-owner resident cables with ports C,E and
all three-port marked-C6 routers with marked ports B,E, and asks for
resource-disjoint interiors.  Sharing the boundary owner E is intentional;
the result is a cut-open compatibility certificate, not a union of the two
closed cycles (which would give E degree four).
"""

from __future__ import annotations

import json
from itertools import permutations


def port_cycle(K, x1, x2, y1, y2, z, a0, a1):
    def add(base, *labels):
        return frozenset(set(base).union(labels))

    A = add(K, z, a0)
    B = add(K, a0, a1)
    P1 = add(set(K) - {x1}, y1, a0, a1)
    P2 = add(set(K) - {x1, x2}, y1, y2, a0, a1)
    Q0 = add(set(K) - {x1, x2}, y1, y2, z, a0)
    Q1 = add(set(K) - {x2}, y2, z, a0)
    return (A, B, P1, P2, Q0, Q1)


def palettes(cycles):
    owners = []
    lower1 = []
    upper1 = []
    lower2 = []
    upper2 = []
    for cycle in cycles:
        size = len(cycle)
        for index, owner in enumerate(cycle):
            successor = cycle[(index + 1) % size]
            successor2 = cycle[(index + 2) % size]
            assert len(owner) == len(successor)
            assert len(owner ^ successor) == 2
            owners.append(owner)
            lower1.append(owner & successor)
            upper1.append(owner | successor)
            lower2.append(owner & successor & successor2)
            upper2.append(owner | successor | successor2)
    return tuple(map(frozenset, (owners, lower1, upper1, lower2, upper2)))


def cyclic_run_minimum(cycle, ground, upper=False):
    if upper:
        trace = [
            cycle[index] | cycle[(index + 1) % len(cycle)]
            for index in range(len(cycle))
        ]
    else:
        trace = cycle
    minima = {False: len(trace), True: len(trace)}
    for coordinate in ground:
        bits = [coordinate in owner for owner in trace]
        if all(bits) or not any(bits):
            continue
        for value in (False, True):
            starts = [
                index for index in range(len(bits))
                if bits[index] == value and bits[index - 1] != value
            ]
            for start in starts:
                length = 0
                while bits[(start + length) % len(bits)] == value:
                    length += 1
                minima[value] = min(minima[value], length)
    return minima[True], minima[False]


def cable_candidates(ground, C, E, terminals):
    H = C & E
    z = next(iter(C - E))
    b = next(iter(E - C))
    answer = []
    for a in sorted(H):
        K = H - {a}
        for x1, x2 in permutations(sorted(K), 2):
            exterior = sorted(ground - K - {z, a, b})
            for y1, y2 in permutations(exterior, 2):
                cycle = port_cycle(K, x1, x2, y1, y2, z, a, b)
                assert cycle[0] == C and cycle[1] == E
                banks = palettes([cycle])
                if any(len(bank) != 6 for bank in banks):
                    continue
                if set(cycle) & terminals != {C, E}:
                    continue
                if cyclic_run_minimum(cycle, ground) != (3, 3):
                    continue
                if cyclic_run_minimum(cycle, ground, upper=True) != (4, 2):
                    continue
                answer.append({
                    "cycle": cycle,
                    "banks": banks,
                    "parameters": (a, x1, x2, y1, y2, z, b),
                })
    return answer


def router_candidates(ground, B, E, terminals):
    H = B & E
    b0 = next(iter(B - E))
    b1 = next(iter(E - B))
    answer = []
    for z in sorted(H):
        K = H - {z}
        available_ports = sorted(ground - H - {b0, b1})
        for b2 in available_ports:
            for x1, x2 in permutations(sorted(K), 2):
                exterior = sorted(ground - K - {z, b0, b1, b2})
                for y1, y2 in permutations(exterior, 2):
                    cycles = tuple(
                        port_cycle(
                            K, x1, x2, y1, y2, z, active[index],
                            active[(index + 1) % 3],
                        )
                        for index in range(3)
                        for active in [(b0, b1, b2)]
                    )
                    assert cycles[0][0] == B and cycles[1][0] == E
                    banks = palettes(cycles)
                    if any(len(bank) != 18 for bank in banks):
                        continue
                    if set(banks[0]) & terminals != {B, E}:
                        continue
                    answer.append({
                        "cycles": cycles,
                        "banks": banks,
                        "parameters": (z, b0, b1, b2, x1, x2, y1, y2),
                    })
    return answer


def compatible(cable, router, q2):
    # E is the sole intended common owner boundary.  All resource vertices
    # must otherwise be distinct.  With q2=True, require the two target decks
    # to be disjoint as well.
    if set(cable["banks"][0]) & set(router["banks"][0]) != {
        cable["cycle"][1]
    }:
        return False
    banks = 5 if q2 else 3
    return all(
        not (set(cable["banks"][index]) & set(router["banks"][index]))
        for index in range(1, banks)
    )


def encode(value):
    if isinstance(value, (set, frozenset, tuple, list)):
        return [encode(item) for item in value]
    return value


def audit_cable_representatives():
    """Check one normalized representative of every rank 4..40."""
    rows = []
    for rank in range(4, 41):
        ground = frozenset(range(2 * rank - 1))
        H = frozenset(range(rank - 1))
        a, x1, x2 = 0, 1, 2
        K = H - {a}
        z, b = rank - 1, rank
        y1, y2 = rank + 1, rank + 2
        C = H | {z}
        E = H | {b}
        cycle = port_cycle(K, x1, x2, y1, y2, z, a, b)
        banks = palettes([cycle])
        assert cycle[0] == C and cycle[1] == E
        assert all(len(bank) == 6 for bank in banks)
        assert cyclic_run_minimum(cycle, ground) == (3, 3)
        assert cyclic_run_minimum(cycle, ground, upper=True) == (4, 2)
        rows.append({
            "rank": rank,
            "ground": len(ground),
            "owners": len(banks[0]),
            "lower_q1": len(banks[1]),
            "upper_q1": len(banks[2]),
            "lower_q2": len(banks[3]),
            "upper_q2": len(banks[4]),
            "owner_minima": [3, 3],
            "upper_minima": [4, 2],
        })
    return rows


def main():
    rank = 7
    ground = frozenset(range(2 * rank - 1))
    core = frozenset(range(rank - 2))
    p, q, r, s = range(rank - 2, rank + 2)
    B = core | {p, q}
    C = core | {r, s}
    T = core | {p, r}
    common = [core | {left, right} for left in (p, q) for right in (r, s)]
    endpoints = [owner for owner in common if owner != T]
    terminals = {T, B, C}
    reports = []
    for E in endpoints:
        cables = cable_candidates(ground, C, E, terminals | {E})
        routers = router_candidates(ground, B, E, terminals | {E})
        witness_q1 = witness_q2 = None
        comparisons = 0
        for cable in cables:
            for router in routers:
                comparisons += 1
                if witness_q1 is None and compatible(cable, router, False):
                    witness_q1 = (cable, router)
                if compatible(cable, router, True):
                    witness_q2 = (cable, router)
                    break
            if witness_q2 is not None:
                break
        reports.append({
            "endpoint": sorted(E),
            "cable_candidates": len(cables),
            "router_candidates": len(routers),
            "comparisons": comparisons,
            "q1_compatible": witness_q1 is not None,
            "q2_deck_compatible": witness_q2 is not None,
            "witness": None if witness_q2 is None else {
                "cable_parameters": encode(witness_q2[0]["parameters"]),
                "router_parameters": encode(witness_q2[1]["parameters"]),
                "cable_cycle": encode(witness_q2[0]["cycle"]),
                "router_cycles": encode(witness_q2[1]["cycles"]),
            },
        })
    assert all(report["q1_compatible"] for report in reports)
    cable_rows = audit_cable_representatives()
    print(json.dumps({
        "status": "PASS",
        "scope": (
            "cut-open interior compatibility; not a closed union and not "
            "a simultaneous 164-row planting"
        ),
        "rank": rank,
        "ground": len(ground),
        "normalized_terminals": {
            "T": sorted(T), "B": sorted(B), "C": sorted(C)
        },
        "universal_cable_representatives": {
            "ranks": [4, 40],
            "cases": len(cable_rows),
            "first": cable_rows[0],
            "last": cable_rows[-1],
        },
        "endpoint_reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
