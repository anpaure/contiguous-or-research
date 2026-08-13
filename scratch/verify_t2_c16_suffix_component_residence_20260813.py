#!/usr/bin/env python3
"""Exact verifier for the T2 cross-suffix C16 topology/residence theorem.

The universal statements in the companion note use the MSW concatenation
law.  This program verifies the finite prefix templates exactly and replays
their first three tensor levels m=8,9,10.  It uses only the Python standard
library and the earlier exact T2/C16 builders in this directory.
"""

from __future__ import annotations

import json
import math
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
    g,
    hmap,
)
from verify_t2_cross_suffix_c16_q2_safe_20260813 import (  # noqa:E402
    explicit_cycle,
)


T2_ROOTS = {
    "110101110000",
    "111100110000",
    "111110010000",
    "111110100000",
    "111111000000",
}

SINGLETON_ROOTS = {
    4: {
        "1101101010100010",
        "1101001010101010",
        "1101101010001010",
        "1101101010001100",
        "1101001010111000",
        "1101001010101100",
    },
    6: {
        "1101101100100010",
        "1101100100101010",
        "1101101100001010",
        "1101101100001100",
        "1101100100111000",
        "1101100100101100",
    },
}

CYCLE_SPECS = {
    4: {2, 5, 7, 9, 11, 12},
    6: {2, 5, 8, 9, 11, 12},
}


def catalan(m: int) -> int:
    return math.comb(2 * m, m) // (m + 1)


def tensor_cycle(b: int, word: str):
    suffix = bits(word) << 16
    return [
        (owner | suffix, old | suffix, new | suffix)
        for owner, old, new in explicit_cycle(CYCLE_SPECS[b], b)
    ]


def toggle(selected, cycles):
    out = set(selected)
    for cycle in cycles:
        for owner, old, new in cycle:
            assert (owner, old) in out
            assert (owner, new) not in out
            out.remove((owner, old))
            out.add((owner, new))
    return out


def canonical_root_map(m: int):
    """Map every rank-m owner to its unique canonical Dyck-path root."""
    out = {}
    for word in dyck_words(m):
        root = bits(word)
        x = root
        for _ in range(m):
            assert x not in out
            out[x] = root
            x = hmap(g(x, m), m)
        assert x not in out
        out[x] = root
    assert len(out) == math.comb(2 * m, m)
    return out


def roots_by_component(root_of_owner, which, n):
    out = defaultdict(set)
    for owner, root in root_of_owner.items():
        out[which[owner]].add(bitword(root, n))
    return out


def projected_cycles(edges, owner_rank):
    """Suppress the opposite shore, retaining its vertices as edge labels."""
    by_owner = defaultdict(list)
    by_label = defaultdict(list)
    for x, y in edges:
        if x.bit_count() == owner_rank:
            owner, label = x, y
        else:
            assert y.bit_count() == owner_rank
            owner, label = y, x
        by_owner[owner].append(label)
        by_label[label].append(owner)
    assert all(len(xs) == 2 for xs in by_owner.values())
    assert all(len(xs) == 2 for xs in by_label.values())

    seen = set()
    answer = []
    for start in by_owner:
        if start in seen:
            continue
        owners = []
        labels = []
        owner = start
        previous_label = None
        while True:
            seen.add(owner)
            owners.append(owner)
            label = next(x for x in by_owner[owner] if x != previous_label)
            labels.append(label)
            next_owner = next(x for x in by_label[label] if x != owner)
            previous_label, owner = label, next_owner
            if owner == start:
                break
        answer.append((owners, labels))
    return answer


def cyclic_run_minimum(owners, ground_size, value):
    length = len(owners)
    best = length + 1
    witness = None
    for coordinate in range(ground_size):
        word = [int(bool(owner >> coordinate & 1)) for owner in owners]
        if all(x == word[0] for x in word):
            continue
        for start, bit in enumerate(word):
            if bit != value or word[start - 1] == value:
                continue
            run = 1
            while word[(start + run) % length] == value:
                run += 1
            if run < best:
                best = run
                witness = {
                    "coordinate": coordinate,
                    "run": run,
                    "owners": [
                        bitword(owners[(start + j) % length], ground_size)
                        for j in range(-1, run + 1)
                    ],
                }
    return best, witness


def seam_collar_report(edges, owner_rank, is_new_seam, ground_size):
    """Return exact q=2 collision data at the marked projected seams."""
    reports = []
    cycle_lengths = []
    seam_gaps = []
    for owners, labels in projected_cycles(edges, owner_rank):
        length = len(owners)
        supports = [
            owners[i] ^ owners[(i + 1) % length] for i in range(length)
        ]
        indices = [
            i for i, label in enumerate(labels)
            if is_new_seam(label, {owners[i], owners[(i + 1) % length]})
        ]
        if not indices:
            continue
        cycle_lengths.append(length)
        indices.sort()
        seam_gaps.extend(
            (indices[(i + 1) % len(indices)] - indices[i]) % length
            for i in range(len(indices))
        )
        for i in indices:
            collisions = []
            left = supports[i - 1] & supports[i]
            right = supports[i] & supports[(i + 1) % length]
            for side, repeated, middle in (
                ("left", left, owners[i]),
                ("right", right, owners[(i + 1) % length]),
            ):
                for coordinate in range(ground_size):
                    if repeated >> coordinate & 1:
                        collisions.append({
                            "side": side,
                            "coordinate": coordinate,
                            "singleton_value": int(bool(middle >> coordinate & 1)),
                            "singleton_owner": bitword(middle, ground_size),
                        })
            reports.append({
                "label": bitword(labels[i], ground_size),
                "collisions": collisions,
            })
    return {
        "cycle_lengths": cycle_lengths,
        "seam_gaps": seam_gaps,
        "seams": reports,
    }


def lower_projection_intersection_and_palette(post, b):
    """Common core and rank-(m-1) palette current of the lower projection."""
    by_owner, by_colour = factor_maps(post)
    del by_owner
    cycle = tensor_cycle(b, "")
    all_endpoints = []
    lower_current = Counter()
    for i, (owner, old_colour, new_colour) in enumerate(cycle):
        old_external = next(x for x in by_colour[old_colour] if x != owner)
        next_cycle_owner = cycle[(i + 1) % len(cycle)][0]
        new_external = next(
            x for x in by_colour[new_colour] if x != next_cycle_owner
        )
        all_endpoints.extend((owner, old_external, new_external))
        lower_current[owner & old_external] -= 1
        lower_current[owner & new_external] += 1
    intersection = (1 << 16) - 1
    for owner in all_endpoints:
        intersection &= owner
    losses = sum(-v for v in lower_current.values() if v < 0)
    births = sum(v for v in lower_current.values() if v > 0)
    return bitword(intersection, 16), intersection.bit_count(), losses, births


def q2_support_check(post, b):
    by_owner, _ = factor_maps(post)
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    delta = Counter()
    for owner, old, new in tensor_cycle(b, ""):
        colours = by_owner[owner]
        other = colours[0] if colours[1] == old else colours[1]
        delta[other | old] -= 1
        delta[other | new] += 1
    assert delta
    assert all(loads[t] + d >= 1 for t, d in delta.items() if loads[t])
    return {
        "negative_occurrences": sum(-d for d in delta.values() if d < 0),
        "positive_occurrences": sum(d for d in delta.values() if d > 0),
        "support_losses": 0,
    }


def topology_replay(m: int):
    n = 2 * m
    k = 2 * m + 1
    suffixes = list(dyck_words(m - 6))
    tails = list(dyck_words(m - 8))
    canonical = canonical_edges(m)
    post = set(canonical)
    apply_t2(post, suffixes)

    base_components, base_which = graph_components(lifted_edges(post, canonical, n))
    assert len(base_components) == catalan(m) - 4 * catalan(m - 6)
    assert Counter(map(len, base_components)) == Counter({
        2 * k: catalan(m) - 5 * catalan(m - 6),
        10 * k: catalan(m - 6),
    })

    root_of_owner = canonical_root_map(m)
    base_roots = roots_by_component(root_of_owner, base_which, n)
    hyperedges = {}
    expected_blocks = {}
    for word in tails:
        t2_left = {root + "1100" + word for root in T2_ROOTS}
        t2_right = {root + "1010" + word for root in T2_ROOTS}
        for b in (4, 6):
            cycle = tensor_cycle(b, word)
            component_ids = {base_which[owner] for owner, _, _ in cycle}
            assert len(component_ids) == 8
            actual_root_blocks = {frozenset(base_roots[c]) for c in component_ids}
            expected_root_blocks = {
                frozenset(t2_left),
                frozenset(t2_right),
                *(
                    frozenset({root + word})
                    for root in SINGLETON_ROOTS[b]
                ),
            }
            assert actual_root_blocks == expected_root_blocks
            hyperedges[(word, b)] = component_ids
            expected_blocks[(word, b)] = t2_left | t2_right | {
                root + word for root in SINGLETON_ROOTS[b]
            }
        assert len(hyperedges[(word, 4)] & hyperedges[(word, 6)]) == 2

    for i, word in enumerate(tails):
        union_here = hyperedges[(word, 4)] | hyperedges[(word, 6)]
        assert len(union_here) == 14
        for other in tails[i + 1:]:
            assert not union_here & (
                hyperedges[(other, 4)] | hyperedges[(other, 6)]
            )

    selections = {}
    for name, choices in (
        ("one_b4", [(word, 4) for word in tails]),
        ("one_b6", [(word, 6) for word in tails]),
        ("both", [(word, b) for word in tails for b in (4, 6)]),
    ):
        selected = toggle(post, [tensor_cycle(b, word) for word, b in choices])
        components, which = graph_components(lifted_edges(selected, canonical, n))
        roots = roots_by_component(root_of_owner, which, n)
        reduction = 12 * len(tails) if name == "both" else 7 * len(tails)
        assert len(components) == len(base_components) - reduction

        for word in tails:
            if name == "both":
                union = expected_blocks[(word, 4)] | expected_blocks[(word, 6)]
                ids = {which[bits(root)] for root in union}
                assert len(ids) == 2
                # The two simultaneous trades split two canonical paths, so
                # canonical root labels themselves occur on both outputs.
                # Vertex sizes, rather than root-start counts, give the exact
                # 9-wreath/13-wreath length decomposition.
                assert sorted(len(components[c]) for c in ids) == [18 * k, 26 * k]
            else:
                b = 4 if name == "one_b4" else 6
                block = expected_blocks[(word, b)]
                ids = {which[bits(root)] for root in block}
                assert len(ids) == 1
                assert roots[next(iter(ids))] == block
        selections[name] = {
            "component_count": len(components),
            "reduction": reduction,
        }

    return {
        "m": m,
        "suffix_vertices": len(suffixes),
        "c16_suffix_edges": len(tails),
        "post_t2_components": len(base_components),
        "post_t2_component_histogram": dict(sorted(Counter(
            map(len, base_components)
        ).items())),
        "selections": selections,
    }


def residence_replay():
    m = 8
    n = 16
    ground_size = 17
    k = 17
    canonical = canonical_edges(m)
    post = set(canonical)
    apply_t2(post, list(dyck_words(2)))

    result = {}
    for b in (4, 6):
        cycle = tensor_cycle(b, "")
        selected = toggle(post, [cycle])
        full_edges = lifted_edges(selected, canonical, n)
        changed_lower = {owner for owner, _, _ in cycle}
        added_incidences = {(owner, new) for owner, _, new in cycle}

        post_by_owner, _ = factor_maps(post)
        upper_head_owners = []
        upper_intersection = (1 << n) - 1
        for owner, old, new in cycle:
            other = next(x for x in post_by_owner[owner] if x != old)
            upper_head_owners.extend((other, old))
            upper_intersection &= other & old & new
        assert len(set(upper_head_owners)) == 16
        assert upper_intersection == sum(1 << x for x in CYCLE_SPECS[b])

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
                colour == label and owner in pair
                for owner, colour in added_incidences
            ),
            ground_size,
        )
        assert upper["cycle_lengths"] == [16 * k]
        assert lower["cycle_lengths"] == [16 * k]
        assert Counter(upper["seam_gaps"]) == Counter({k: 6, 5 * k: 2})
        assert Counter(lower["seam_gaps"]) == Counter({k: 6, 5 * k: 2})

        upper_bad = [x for x in upper["seams"] if x["collisions"]]
        lower_bad = [x for x in lower["seams"] if x["collisions"]]
        assert len(upper_bad) == {4: 4, 6: 6}[b]
        assert len(lower_bad) == {4: 2, 6: 5}[b]
        assert all(
            event["singleton_value"] == 0
            for seam in upper_bad for event in seam["collisions"]
        )
        assert all(
            event["singleton_value"] == 1
            for seam in lower_bad for event in seam["collisions"]
        )

        upper_big = next(
            owners for owners, _ in projected_cycles(full_edges, m + 1)
            if len(owners) == 16 * k
        )
        lower_big = next(
            owners for owners, _ in projected_cycles(full_edges, m)
            if len(owners) == 16 * k
        )
        upper_positive = cyclic_run_minimum(upper_big, ground_size, 1)
        upper_zero = cyclic_run_minimum(upper_big, ground_size, 0)
        lower_positive = cyclic_run_minimum(lower_big, ground_size, 1)
        lower_zero = cyclic_run_minimum(lower_big, ground_size, 0)
        assert (upper_positive[0], upper_zero[0]) == (2, 1)
        assert (lower_positive[0], lower_zero[0]) == (1, 2)

        core_word, core_rank, palette_losses, palette_births = (
            lower_projection_intersection_and_palette(post, b)
        )
        assert (core_word, core_rank, palette_losses, palette_births) == {
            4: ("0000000101000000", 2, 7, 7),
            6: ("0000010011000000", 3, 5, 5),
        }[b]

        result[str(b)] = {
            "single_switch_component_owner_length": 16 * k,
            "upper_projection": {
                "bad_2_collars": len(upper_bad),
                "bad_collision_events": sum(
                    len(x["collisions"]) for x in upper_bad
                ),
                "common_intersection": bitword(upper_intersection, n),
                "common_intersection_rank": upper_intersection.bit_count(),
                "minimum_positive_run": upper_positive[0],
                "minimum_zero_run": upper_zero[0],
                "witness": upper_bad[0],
            },
            "lower_projection": {
                "bad_2_collars": len(lower_bad),
                "bad_collision_events": sum(
                    len(x["collisions"]) for x in lower_bad
                ),
                "minimum_positive_run": lower_positive[0],
                "minimum_zero_run": lower_zero[0],
                "witness": lower_bad[0],
                "common_intersection": core_word,
                "common_intersection_rank": core_rank,
                "immediate_lower_palette_losses": palette_losses,
                "immediate_lower_palette_births": palette_births,
            },
            "seam_gap_histogram": dict(sorted(Counter(
                upper["seam_gaps"]
            ).items())),
            "q2": q2_support_check(post, b),
        }

    both_cycles = [tensor_cycle(b, "") for b in (4, 6)]
    both_selected = toggle(post, both_cycles)
    both_edges = lifted_edges(both_selected, canonical, n)
    both_changed_lower = {
        owner for cycle in both_cycles for owner, _, _ in cycle
    }
    both_added = {
        (owner, new) for cycle in both_cycles for owner, _, new in cycle
    }
    both_upper = seam_collar_report(
        both_edges,
        m + 1,
        lambda label, pair: label in both_changed_lower,
        ground_size,
    )
    both_lower = seam_collar_report(
        both_edges,
        m,
        lambda label, pair: any(
            colour == label and owner in pair for owner, colour in both_added
        ),
        ground_size,
    )
    both_upper_bad = [x for x in both_upper["seams"] if x["collisions"]]
    both_lower_bad = [x for x in both_lower["seams"] if x["collisions"]]
    assert sorted(both_upper["cycle_lengths"]) == [9 * k, 13 * k]
    assert sorted(both_lower["cycle_lengths"]) == [9 * k, 13 * k]
    assert Counter(both_upper["seam_gaps"]) == Counter({k: 14, 4 * k: 2})
    assert Counter(both_lower["seam_gaps"]) == Counter({
        k: 12,
        k + 1: 2,
        4 * k - 1: 2,
    })
    assert len(both_upper_bad) == 10
    assert len(both_lower_bad) == 7
    assert all(
        event["singleton_value"] == 0
        for seam in both_upper_bad for event in seam["collisions"]
    )
    assert all(
        event["singleton_value"] == 1
        for seam in both_lower_bad for event in seam["collisions"]
    )
    result["both"] = {
        "component_owner_lengths": sorted(both_upper["cycle_lengths"]),
        "upper_bad_2_collars": len(both_upper_bad),
        "lower_bad_2_collars": len(both_lower_bad),
        "seam_gap_histogram": dict(sorted(Counter(
            both_upper["seam_gaps"]
        ).items())),
    }
    return result


def suffix_matching_replay():
    rows = []
    for s in range(2, 11):
        vertices = list(dyck_words(s))
        edges = [("1100" + word, "1010" + word) for word in dyck_words(s - 2)]
        endpoints = [x for edge in edges for x in edge]
        assert len(endpoints) == len(set(endpoints))
        assert all(x in set(vertices) for x in endpoints)
        if s == 2:
            assert len(endpoints) == len(vertices) == 2
        else:
            assert len(endpoints) < len(vertices)
        rows.append({
            "suffix_semilength": s,
            "vertices": len(vertices),
            "c16_edges": len(edges),
            "covered_vertices": len(endpoints),
        })
    return rows


def main():
    payload = {
        "tensor_topology_replays": [topology_replay(m) for m in (8, 9, 10)],
        "base_residence_replay": residence_replay(),
        "suffix_matching_replay": suffix_matching_replay(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
