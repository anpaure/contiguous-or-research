#!/usr/bin/env python3
"""Materialize and fully audit every lifted cycle of a disconnected k=13 sigma selection."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from sigma_sat_solver import SigmaInstance, rotate
from k13_quotient_endpoint_cycle_search import load_selected


def masks_of_rank(k: int, rank: int) -> set[int]:
    return {
        sum(1 << x for x in xs)
        for xs in combinations(range(k), rank)
    }


def traverse_component(instance, choices, component):
    adjacency = {v: [] for v in component}
    for eid, choice in enumerate(choices):
        u, v = choice.endpoint
        adjacency[u].append((v, eid, choice.voltage))
        adjacency[v].append((u, eid, (-choice.voltage) % instance.k))
    start = min(component)
    current = start
    previous_edge = -1
    vertices, phases, edges = [start], [0], []
    phase = 0
    while True:
        options = [x for x in adjacency[current] if x[1] != previous_edge]
        if not options:
            raise AssertionError("component traversal stuck")
        nxt, eid, delta = options[0]
        edges.append(eid)
        phase = (phase + delta) % instance.k
        previous_edge, current = eid, nxt
        if current == start:
            break
        vertices.append(current)
        phases.append(phase)
    if len(set(edges)) != len(choices):
        raise AssertionError("component traversal missed an edge")
    return vertices, phases, edges, phase


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    instance = SigmaInstance(13, True, cap2=False, q2=False, cover_upper=False)
    _, selected_by_lower = load_selected(instance, args.source)
    selected = [selected_by_lower[x] for x in sorted(selected_by_lower)]
    components = instance.components(selected)
    physical_cycles = []
    component_report = []
    for component in components:
        local = [c for c in selected if c.endpoint[0] in component]
        vertices, phases, _, voltage = traverse_component(instance, local, component)
        cycles = []
        if voltage:
            cycle = []
            offset = 0
            for _ in range(instance.k):
                cycle.extend(
                    rotate(instance.middle[v], p + offset, instance.k)
                    for v, p in zip(vertices, phases)
                )
                offset = (offset + voltage) % instance.k
            cycles.append(cycle)
        else:
            for offset in range(instance.k):
                cycles.append(
                    [
                        rotate(instance.middle[v], p + offset, instance.k)
                        for v, p in zip(vertices, phases)
                    ]
                )
        physical_cycles.extend(cycles)
        component_report.append(
            {
                "quotient_vertices": len(component),
                "quotient_voltage": voltage,
                "physical_cycle_lengths": [len(c) for c in cycles],
            }
        )

    middle_load = Counter(x for cycle in physical_cycles for x in cycle)
    shadows = {}
    for q in range(1, 7):
        lower_load = Counter()
        upper_load = Counter()
        for cycle in physical_cycles:
            n = len(cycle)
            for start in range(n):
                lo = (1 << 13) - 1
                hi = 0
                for j in range(q + 1):
                    lo &= cycle[(start + j) % n]
                    hi |= cycle[(start + j) % n]
                if lo.bit_count() == 7 - q:
                    lower_load[lo] += 1
                if hi.bit_count() == 7 + q:
                    upper_load[hi] += 1
        lower_target = masks_of_rank(13, 7 - q)
        upper_target = masks_of_rank(13, 7 + q)
        shadows[str(q)] = {
            "lower": {
                "holes": len(lower_target - lower_load.keys()),
                "hole_masks": sorted(lower_target - lower_load.keys()),
                "load_histogram": dict(Counter(lower_load.values())),
            },
            "upper": {
                "holes": len(upper_target - upper_load.keys()),
                "hole_masks": sorted(upper_target - upper_load.keys()),
                "load_histogram": dict(Counter(upper_load.values())),
            },
        }

    residence = sum(
        len(instance.residence_violations(cycle, 3)) for cycle in physical_cycles
    )
    report = {
        "source": str(args.source),
        "quotient_components": component_report,
        "physical_cycle_count": len(physical_cycles),
        "physical_cycle_lengths": [len(c) for c in physical_cycles],
        "middle_unique": len(middle_load),
        "middle_load_histogram": dict(Counter(middle_load.values())),
        "residence_defects_le3": residence,
        "shadows": shadows,
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
