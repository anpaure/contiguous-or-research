#!/usr/bin/env python3
"""Independent verifier for the frozen D_4 spanning-actuator certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    seam_collar_report,
    toggle,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="scratch/search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out",
    )
    args = parser.parse_args()
    certificate_path = Path(args.certificate)
    raw = certificate_path.read_bytes()
    certificate = json.loads(raw)

    m, n = 10, 20
    assert certificate["m"] == m
    suffixes = list(base.dyck_words(4))
    assert certificate["suffix_vertices"] == suffixes
    assert len(certificate["edge_minimums"]) == 47
    assert Counter(row["shortest_q2_safe_incidence_length"] for row in certificate[
        "edge_minimums"
    ]) == Counter({14: 3, 16: 15, 18: 11, 20: 9, 22: 8, 24: 1})

    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    base_components, base_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    selected_edges = []
    all_owners = set()
    all_colours = set()
    cycles = []
    individual_reports = []
    q2_delta = Counter()
    for item in certificate["selection"]:
        left, right = item["suffix_edge"]
        source, target = item["orientation"]
        assert {left, right} == {source, target}
        assert left in suffixes and right in suffixes
        assert (base.bits(left) ^ base.bits(right)).bit_count() == 2
        selected_edges.append((source, target))

        owners = tuple(base.bits(word) for word in item["owners"])
        new_colours = tuple(base.bits(word) for word in item["new_colours"])
        assert len(owners) == len(new_colours)
        assert 2 * len(owners) == item["incidence_length"]
        assert len(set(owners)) == len(owners)
        assert len(set(new_colours)) == len(new_colours)
        assert not all_owners & set(owners)
        assert not all_colours & set(new_colours)
        all_owners.update(owners)
        all_colours.update(new_colours)

        endpoint_a = base.bits(item["prefix"]) | (base.bits(left) << 12)
        endpoint_b = base.bits(item["prefix"]) | (base.bits(right) << 12)
        assert endpoint_a in owners and endpoint_b in owners
        assert all(len(by_owner[owner]) == 2 for owner in owners)

        cycle = [
            (owners[i], new_colours[i - 1], new_colours[i])
            for i in range(len(owners))
        ]
        for owner, old, new in cycle:
            assert (owner, old) in post
            assert (owner, new) not in post
            assert owner & ~old == 0 and owner & ~new == 0
            other = next(x for x in by_owner[owner] if x != old)
            q2_delta[other | old] -= 1
            q2_delta[other | new] += 1
        component_ids = {base_which[owner] for owner in owners}
        assert len(component_ids) == item["component_arity"]
        cycles.append(cycle)

        individual = toggle(post, [cycle])
        individual_components, individual_which = graph_components(
            lifted_edges(individual, canonical, n)
        )
        individual_outputs = {
            individual_which[owner] for owner in owners
        }
        endpoints_joined = (
            individual_which[endpoint_a] == individual_which[endpoint_b]
        )
        individual_edges = lifted_edges(individual, canonical, n)
        changed_lower = set(owners)
        added = {(owner, new) for owner, _, new in cycle}
        upper = seam_collar_report(
            individual_edges,
            m + 1,
            lambda label, pair: label in changed_lower,
            n + 1,
        )
        lower = seam_collar_report(
            individual_edges,
            m,
            lambda label, pair: any(
                colour == label and owner in pair for owner, colour in added
            ),
            n + 1,
        )
        upper_bad = [x for x in upper["seams"] if x["collisions"]]
        lower_bad = [x for x in lower["seams"] if x["collisions"]]
        upper_core = (1 << n) - 1
        lower_core = (1 << n) - 1
        lower_palette = Counter()
        for owner, old, new in cycle:
            other = next(x for x in by_owner[owner] if x != old)
            upper_core &= other & old & new
            old_external = next(x for x in by_colour[old] if x != owner)
            new_external = next(
                x for x in by_colour[new]
                if x != owner and (x, new) in individual
            )
            lower_core &= owner & old_external & new_external
            lower_palette[owner & old_external] -= 1
            lower_palette[owner & new_external] += 1
        individual_reports.append({
            "suffix_edge": item["suffix_edge"],
            "incidence_length": item["incidence_length"],
            "component_arity": len(component_ids),
            "component_reduction": len(base_components) - len(
                individual_components
            ),
            "old_component_owner_length_histogram": dict(sorted(Counter(
                len(base_components[component]) // 2
                for component in component_ids
            ).items())),
            "output_components_on_touched_set": len(individual_outputs),
            "output_component_owner_lengths": sorted(
                len(individual_components[component]) // 2
                for component in individual_outputs
            ),
            "suffix_endpoint_output_component_owner_lengths": sorted(
                len(individual_components[component]) // 2
                for component in {
                    individual_which[endpoint_a], individual_which[endpoint_b]
                }
            ),
            "suffix_endpoint_representatives_joined": endpoints_joined,
            "upper_common_intersection_rank": upper_core.bit_count(),
            "lower_common_intersection_rank": lower_core.bit_count(),
            "lower_palette_losses": sum(
                -delta for delta in lower_palette.values() if delta < 0
            ),
            "upper_bad_2_collars": len(upper_bad),
            "lower_bad_2_collars": len(lower_bad),
        })

    assert len(selected_edges) == len(suffixes) - 1
    assert all(
        loads[target] + delta >= 1
        for target, delta in q2_delta.items() if loads[target]
    )

    # The selected orientations form a rooted arborescence at the mountain.
    root = suffixes[0]
    incoming = Counter(target for _, target in selected_edges)
    assert incoming[root] == 0
    assert all(incoming[word] == 1 for word in suffixes if word != root)
    adjacency = defaultdict(list)
    for source, target in selected_edges:
        adjacency[source].append(target)
    seen = {root}
    queue = deque([root])
    while queue:
        source = queue.popleft()
        for target in adjacency[source]:
            assert target not in seen
            seen.add(target)
            queue.append(target)
    assert seen == set(suffixes)

    simultaneous = toggle(post, cycles)
    after_components, after_which = graph_components(
        lifted_edges(simultaneous, canonical, n)
    )
    touched_base = {
        base_which[owner] for cycle in cycles for owner, _, _ in cycle
    }
    touched_after = {
        after_which[owner] for cycle in cycles for owner, _, _ in cycle
    }
    assert len(touched_base) == 82
    assert len(touched_after) == 1
    assert len(after_components) == len(base_components) - 81
    output = next(iter(touched_after))
    assert len(after_components[output]) // 2 == 2898
    suffix_outputs = {
        after_which[
            base.bits(item["prefix"])
            | (base.bits(suffix) << 12)
        ]
        for item in certificate["selection"]
        for suffix in item["suffix_edge"]
    }
    assert suffix_outputs == {output}

    changed_lower = {owner for cycle in cycles for owner, _, _ in cycle}
    added = {(owner, new) for cycle in cycles for owner, _, new in cycle}
    full_edges = lifted_edges(simultaneous, canonical, n)
    upper = seam_collar_report(
        full_edges,
        m + 1,
        lambda label, pair: label in changed_lower,
        n + 1,
    )
    lower = seam_collar_report(
        full_edges,
        m,
        lambda label, pair: any(
            colour == label and owner in pair for owner, colour in added
        ),
        n + 1,
    )
    upper_bad = [x for x in upper["seams"] if x["collisions"]]
    lower_bad = [x for x in lower["seams"] if x["collisions"]]
    assert len(upper_bad) == 51
    assert len(lower_bad) == 40
    assert min(upper["seam_gaps"]) == min(lower["seam_gaps"]) == 1
    assert all(
        event["singleton_value"] == 0
        for seam in upper_bad for event in seam["collisions"]
    )
    assert all(
        event["singleton_value"] == 1
        for seam in lower_bad for event in seam["collisions"]
    )

    print(json.dumps({
        "status": "PASS",
        "certificate": str(certificate_path),
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "suffix_tree_edges": len(selected_edges),
        "incidence_length_histogram": dict(sorted(Counter(
            item["incidence_length"] for item in certificate["selection"]
        ).items())),
        "base_components_met": len(touched_base),
        "output_components": len(touched_after),
        "output_component_owner_length": len(after_components[output]) // 2,
        "q2_support_losses": 0,
        "individual_actuators": individual_reports,
        "upper_bad_2_collars": len(upper_bad),
        "lower_bad_2_collars": len(lower_bad),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
