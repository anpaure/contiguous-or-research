#!/usr/bin/env python3
"""Verify the complete semilength-three T2 suffix-actuator catalogue.

This is a frozen finite certificate for the context-template escape search.
The four selected alternating circuits are q2-support-safe, vertex-disjoint,
and their suffix edges form a tree on D_3.  The program also computes their
post-T2 component action and exact two-shore residence collars.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from search_t2_cross_suffix_alternating_cycles_20260813 import (  # noqa:E402
    apply_t2,
    bits,
    bitword,
    canonical_edges,
    dyck_words,
    factor_maps,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    projected_cycles,
    seam_collar_report,
    toggle,
)


CATALOGUE = [
    {
        "suffix_edge": ("111000", "101100"),
        "prefix": "101001010101",
        "rows": [
            ("101001010101111000", "101011010101111000", "101001010101111100"),
            ("001001010101111100", "101001010101111100", "001011010101111100"),
            ("001011010101101100", "001011010101111100", "101011010101101100"),
            ("101001010101101100", "101011010101101100", "101001010111101100"),
            ("001001010111101100", "101001010111101100", "001001010111101101"),
            ("001001010111101001", "001001010111101101", "001011010111101001"),
            ("001011010111101000", "001011010111101001", "001011010111111000"),
            ("001011010101111000", "001011010111111000", "101011010101111000"),
        ],
    },
    {
        "suffix_edge": ("111000", "101010"),
        "prefix": "101001001101",
        "rows": [
            ("101001001101111000", "101001011101111000", "101001001111111000"),
            ("001001001111111000", "101001001111111000", "001001101111111000"),
            ("001001101101111000", "001001101111111000", "001001101101111010"),
            ("001001101101101010", "001001101101111010", "101001101101101010"),
            ("101001001101101010", "101001101101101010", "101001001101111010"),
            ("001001001101111010", "101001001101111010", "001001001101111011"),
            ("001001001101111001", "001001001101111011", "001001011101111001"),
            ("001001011101111000", "001001011101111001", "101001011101111000"),
        ],
    },
    {
        "suffix_edge": ("110100", "110010"),
        "prefix": "101001010101",
        "rows": [
            ("101001010101110100", "101001110101110100", "101001010111110100"),
            ("001001010111110100", "101001010111110100", "001011010111110100"),
            ("001011010101110100", "001011010111110100", "001011010101110110"),
            ("001011010101110010", "001011010101110110", "101011010101110010"),
            ("101001010101110010", "101011010101110010", "101001010111110010"),
            ("001001010111110010", "101001010111110010", "001001010111110011"),
            ("001001010111110001", "001001010111110011", "001001110111110001"),
            ("001001110111110000", "001001110111110001", "001001110111110100"),
            ("001001110101110100", "001001110111110100", "101001110101110100"),
        ],
    },
    {
        "suffix_edge": ("110100", "101100"),
        "prefix": "101001001101",
        "rows": [
            ("101001001101110100", "101001011101110100", "101001001101111100"),
            ("001001001101111100", "101001001101111100", "001001101101111100"),
            ("001001101101101100", "001001101101111100", "101001101101101100"),
            ("101001001101101100", "101001101101101100", "101001001111101100"),
            ("001001001111101100", "101001001111101100", "001001011111101100"),
            ("001001011101101100", "001001011111101100", "001001011101101101"),
            ("001001011101100101", "001001011101101101", "001001011101110101"),
            ("001001011101110100", "001001011101110101", "101001011101110100"),
        ],
    },
]


def integer_rows(item):
    return [tuple(bits(word) for word in row) for row in item["rows"]]


def suffix_tree_check():
    vertices = set(dyck_words(3))
    edges = [item["suffix_edge"] for item in CATALOGUE]
    assert len(edges) == len(vertices) - 1
    adjacency = defaultdict(set)
    for u, v in edges:
        assert u in vertices and v in vertices
        assert (bits(u) ^ bits(v)).bit_count() == 2
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    assert seen == vertices
    return {
        "vertices": sorted(vertices),
        "edges": [list(edge) for edge in edges],
        "degree_histogram": dict(sorted(Counter(
            len(adjacency[v]) for v in vertices
        ).items())),
    }


def main():
    m = 9
    n = 18
    ground_size = 19
    canonical = canonical_edges(m)
    post = set(canonical)
    apply_t2(post, list(dyck_words(3)))
    by_owner, by_colour = factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    base_components, base_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    all_owners = set()
    all_colours = set()
    total_delta = Counter()
    reports = []
    cycles = []
    for item in CATALOGUE:
        rows = integer_rows(item)
        cycles.append(rows)
        owners = {owner for owner, _, _ in rows}
        colours = {colour for _, old, new in rows for colour in (old, new)}
        assert not owners & all_owners
        assert not colours & all_colours
        all_owners |= owners
        all_colours |= colours

        delta = Counter()
        for owner, old, new in rows:
            assert (owner, old) in post
            assert (owner, new) not in post
            selected = by_owner[owner]
            other = next(x for x in selected if x != old)
            delta[other | old] -= 1
            delta[other | new] += 1
            total_delta[other | old] -= 1
            total_delta[other | new] += 1
        losses = [t for t, d in delta.items() if loads[t] + d == 0]
        assert not losses

        component_ids = {base_which[owner] for owner, _, _ in rows}
        selected = toggle(post, [rows])
        components, which = graph_components(lifted_edges(selected, canonical, n))
        assert len(components) == len(base_components) - (len(component_ids) - 1)

        changed_lower = {owner for owner, _, _ in rows}
        added = {(owner, new) for owner, _, new in rows}
        full_edges = lifted_edges(selected, canonical, n)
        upper = seam_collar_report(
            full_edges,
            m + 1,
            lambda label, pair: label in changed_lower,
            ground_size,
        )
        lower = seam_collar_report(
            full_edges,
            m,
            lambda label, pair: any(
                colour == label and owner in pair for owner, colour in added
            ),
            ground_size,
        )
        upper_bad = [x for x in upper["seams"] if x["collisions"]]
        lower_bad = [x for x in lower["seams"] if x["collisions"]]
        assert upper_bad and lower_bad
        assert all(
            event["singleton_value"] == 0
            for seam in upper_bad for event in seam["collisions"]
        )
        assert all(
            event["singleton_value"] == 1
            for seam in lower_bad for event in seam["collisions"]
        )

        upper_core = (1 << n) - 1
        lower_core = (1 << n) - 1
        lower_palette = Counter()
        for owner, old, new in rows:
            other = next(x for x in by_owner[owner] if x != old)
            upper_core &= other & old & new
            old_external = next(x for x in by_colour[old] if x != owner)
            new_external = next(
                x for x in by_colour[new]
                if x != owner and (x, new) in selected
            )
            lower_core &= owner & old_external & new_external
            lower_palette[owner & old_external] -= 1
            lower_palette[owner & new_external] += 1

        reports.append({
            "suffix_edge": list(item["suffix_edge"]),
            "prefix": item["prefix"],
            "incidence_length": 2 * len(rows),
            "component_arity": len(component_ids),
            "component_reduction": len(base_components) - len(components),
            "old_component_size_histogram": dict(sorted(Counter(
                len(base_components[c]) for c in component_ids
            ).items())),
            "q2_negative_occurrences": sum(
                -d for d in delta.values() if d < 0
            ),
            "q2_support_losses": 0,
            "upper_bad_2_collars": len(upper_bad),
            "lower_bad_2_collars": len(lower_bad),
            "upper_common_intersection": bitword(upper_core, n),
            "upper_common_intersection_rank": upper_core.bit_count(),
            "lower_common_intersection": bitword(lower_core, n),
            "lower_common_intersection_rank": lower_core.bit_count(),
            "lower_palette_losses": sum(
                -d for d in lower_palette.values() if d < 0
            ),
            "lower_palette_births": sum(
                d for d in lower_palette.values() if d > 0
            ),
        })

    assert all(
        loads[t] + d >= 1 for t, d in total_delta.items() if loads[t]
    )

    simultaneous = toggle(post, cycles)
    simultaneous_components, simultaneous_which = graph_components(
        lifted_edges(simultaneous, canonical, n)
    )
    touched_base = {
        base_which[owner]
        for rows in cycles for owner, _, _ in rows
    }
    touched_after = {
        simultaneous_which[owner]
        for rows in cycles for owner, _, _ in rows
    }
    assert len(touched_base) == 27
    assert len(touched_after) == 1
    assert len(simultaneous_components) == len(base_components) - 26
    assert len(simultaneous_components[next(iter(touched_after))]) == 2 * 47 * ground_size

    changed_lower = {
        owner for rows in cycles for owner, _, _ in rows
    }
    added = {
        (owner, new) for rows in cycles for owner, _, new in rows
    }
    simultaneous_edges = lifted_edges(simultaneous, canonical, n)
    simultaneous_upper = seam_collar_report(
        simultaneous_edges,
        m + 1,
        lambda label, pair: label in changed_lower,
        ground_size,
    )
    simultaneous_lower = seam_collar_report(
        simultaneous_edges,
        m,
        lambda label, pair: any(
            colour == label and owner in pair for owner, colour in added
        ),
        ground_size,
    )
    upper_bad = [
        x for x in simultaneous_upper["seams"] if x["collisions"]
    ]
    lower_bad = [
        x for x in simultaneous_lower["seams"] if x["collisions"]
    ]
    assert len(upper_bad) == 18
    assert len(lower_bad) == 14

    print(json.dumps({
        "m": m,
        "suffix_tree": suffix_tree_check(),
        "owner_disjoint": True,
        "colour_disjoint": True,
        "individual_actuators": reports,
        "simultaneous": {
            "base_components_met": len(touched_base),
            "output_components": len(touched_after),
            "component_reduction": len(base_components) - len(
                simultaneous_components
            ),
            "output_component_owner_length": 47 * ground_size,
            "q2_support_losses": 0,
            "upper_bad_2_collars": len(upper_bad),
            "lower_bad_2_collars": len(lower_bad),
            "minimum_upper_seam_gap": min(simultaneous_upper["seam_gaps"]),
            "minimum_lower_seam_gap": min(simultaneous_lower["seam_gaps"]),
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
