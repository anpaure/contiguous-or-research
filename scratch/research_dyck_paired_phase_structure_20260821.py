#!/usr/bin/env python3
"""Structural diagnostics for paired Chung--Feller phase routing.

Research only.  Substantive runs are performed on H100.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

import networkx as nx

from research_c8_orbit_phase_normal_form_20260821 import (
    canonical_layers,
    rooted_x_path,
)
from research_msw_c8_shadow_anneal_20260821 import dyck_words, msw_row, rho


def word(target, r):
    return "".join("1" if i in target else "0" for i in range(1, 2 * r + 1))


def upstep_flaws(target, r):
    height = 0
    flaws = 0
    for i in range(1, 2 * r + 1):
        if i in target:
            if height < 0:
                flaws += 1
            height += 1
        else:
            height -= 1
    assert height == 0
    return flaws


def return_composition(target, r):
    height = 0
    last = 0
    parts = []
    for i in range(1, 2 * r + 1):
        height += 1 if i in target else -1
        if height == 0:
            parts.append((i - last) // 2)
            last = i
    return tuple(parts)


def inversion_cells(target, r):
    ones = zeros = 0
    cells = set()
    for position in range(1, 2 * r + 1):
        if position in target:
            ones += 1
            for zero in range(1, zeros + 1):
                cells.add((ones, zero))
        else:
            zeros += 1
    return frozenset(cells)


def adjacent_leaf_context(peak, valley, r):
    """Return (a,b,c) for valley=A 10 1B0 C, peak=A 110B0 C."""
    xv = word(valley, r)
    xp = word(peak, r)
    changed = [i for i, (x, y) in enumerate(zip(xv, xp)) if x != y]
    assert len(changed) == 2 and changed[1] == changed[0] + 1
    p = changed[0]
    assert xv[p:p + 2] == "01" and xp[p:p + 2] == "10"
    assert p >= 1 and xv[p - 1] == "1"
    A = xv[:p - 1]
    assert len(A) % 2 == 0
    height = 0
    close = None
    for index in range(p + 1, 2 * r):
        height += 1 if xv[index] == "1" else -1
        if height == 0:
            close = index
            break
    assert close is not None
    B = xv[p + 2:close]
    C = xv[close + 1:]
    return len(A) // 2, len(B) // 2, len(C) // 2


def hr_component_key(target, r):
    raw_word = word(target, r)
    pairs = [raw_word[i:i + 2] for i in range(1, 2 * r - 1, 2)]
    steps = ["U" if pair == "11" else "D" if pair == "00" else "H" for pair in pairs]
    normal = list(steps)
    for i in range(len(steps) - 1):
        if steps[i:i + 2] == ["U", "D"]:
            normal[i:i + 2] = ["H", "H"]
    rigid = []
    for i, step in enumerate(normal):
        if step != "H":
            continue
        previous = normal[i - 1] if i else None
        following = normal[i + 1] if i + 1 < len(normal) else None
        if previous == "H" or following == "H":
            continue
        if previous == "D" or following == "U":
            assert steps[i] == "H"
            rigid.append((i, pairs[i]))
    return tuple(normal), tuple(rigid)


def build_paths(r):
    anchor = 2 * r + 1
    result = {}
    for raw in dyck_words(r):
        root = frozenset(i + 1 for i, bit in enumerate(raw) if bit == "1")
        result[root] = rooted_x_path(msw_row(raw), r, root, anchor)
    return result


def audit(r):
    ground = frozenset(range(1, 2 * r + 1))
    layer, _, counts = canonical_layers(r)
    assert all(layer[x] == upstep_flaws(x, r) for x in layer)
    assert all(layer[ground - x] == r - layer[x] for x in layer)
    by_phase = {
        t: tuple(sorted((x for x in layer if layer[x] == t), key=lambda x: tuple(x)))
        for t in range(r + 1)
    }
    indices = {t: set(by_phase[t]) for t in by_phase}
    transition = {}
    for t in range(r):
        left_hist = Counter()
        right_hist = Counter()
        edges = []
        for left in by_phase[t]:
            for deleted in left:
                for added in ground - left:
                    right = frozenset((left - {deleted}) | {added})
                    if right in indices[t + 1]:
                        edges.append((left, right))
                        left_hist[left] += 1
                        right_hist[right] += 1
        transition[t] = {
            "edges": len(edges),
            "left_degree_hist": dict(Counter(left_hist.values())),
            "right_degree_hist": dict(Counter(right_hist.values())),
        }

    canonical = build_paths(r)
    root_adjacent = []
    roots = by_phase[0]
    root_set = set(roots)
    for left in roots:
        for i in range(1, 2 * r):
            if i in left and i + 1 not in left:
                right = frozenset((left - {i}) | {i + 1})
                if right in root_set and tuple(left) < tuple(right):
                    root_adjacent.append((left, right))
    distance_profiles = Counter()
    middle_complement = 0
    endpoint_pair_hist = Counter()
    tail_swap_seams = Counter()
    tail_swap_delta1_edges = 0
    tail_swap_combined_ledger_hist = Counter()
    safe_graph = nx.Graph()
    safe_graph.add_nodes_from(roots)
    safe_seams = {}
    safe_flip_rank_relations = Counter()
    safe_context_hist = Counter()
    unsafe_context_hist = Counter()
    local_safe_type = Counter()
    local_unsafe_type = Counter()
    for left, right in root_adjacent:
        profile = tuple(len(canonical[left][t] - canonical[right][t]) for t in range(r + 1))
        distance_profiles[profile] += 1
        middle_complement += canonical[right][r // 2] == ground - canonical[left][r // 2]
        endpoint_pair_hist[len(canonical[left][-1] - (ground - right))] += 1
        valid = []
        for t in range(1, r + 1):
            if (len(canonical[left][t - 1] ^ canonical[right][t]) == 2
                    and len(canonical[right][t - 1] ^ canonical[left][t]) == 2):
                path = canonical[left][:t] + canonical[right][t:]
                multiplicity = Counter()
                for a, b in zip(path, path[1:]):
                    multiplicity.update(a ^ b)
                delta = sum(max(0, value - 1) for value in multiplicity.values())
                other_path = canonical[right][:t] + canonical[left][t:]
                other_multiplicity = Counter()
                for a, b in zip(other_path, other_path[1:]):
                    other_multiplicity.update(a ^ b)
                other_delta = sum(max(0, value - 1) for value in other_multiplicity.values())
                tail_swap_combined_ledger_hist[
                    tuple(sorted((multiplicity[x] + other_multiplicity[x] for x in ground)))
                ] += 1
                valid.append((t, delta, other_delta))
        changed_position = min(left ^ right)
        left_word = word(left, r)
        if changed_position % 2 == 0:
            pair_index = changed_position // 2 - 1
            pairs = [left_word[i:i + 2] for i in range(1, 2 * r - 1, 2)]
            step = lambda pair: "U" if pair == "11" else "D" if pair == "00" else "H"
            previous = step(pairs[pair_index - 1]) if pair_index else "S"
            following = step(pairs[pair_index + 1]) if pair_index + 1 < len(pairs) else "S"
            local_key = ("within", previous, following)
        else:
            boundary = (changed_position - 1) // 2
            left_pairs = [left_word[i:i + 2] for i in range(1, 2 * r - 1, 2)]
            right_word = word(right, r)
            right_pairs = [right_word[i:i + 2] for i in range(1, 2 * r - 1, 2)]
            def decorated(pair):
                return "U" if pair == "11" else "D" if pair == "00" else "H0" if pair == "10" else "H1"
            before = tuple(map(decorated, left_pairs[boundary - 1:boundary + 1]))
            after = tuple(map(decorated, right_pairs[boundary - 1:boundary + 1]))
            local_key = ("boundary", tuple(sorted((before, after))))
        tail_swap_seams[tuple(valid)] += 1
        tail_swap_delta1_edges += any(delta == other_delta == 1 for _, delta, other_delta in valid)
        if any(delta == other_delta == 1 for _, delta, other_delta in valid):
            local_safe_type[local_key] += 1
            safe_graph.add_edge(left, right)
            safe_seams[frozenset((left, right))] = tuple(
                t for t, delta, other_delta in valid if delta == other_delta == 1
            )
            peak, valley = (left, right)
            u, v = sorted(peak ^ valley)
            if u not in peak:
                peak, valley = valley, peak
            try:
                context = adjacent_leaf_context(peak, valley, r)
            except AssertionError:
                context = (-1, -1, -1)
            safe_context_hist[(context, safe_seams[frozenset((left, right))])] += 1
            rp = rho(word(peak, r))
            rv = rho(word(valley, r))
            pp = {x: index // 2 + 1 for index, x in enumerate(rp)}
            pv = {x: index // 2 + 1 for index, x in enumerate(rv)}
            for seam in safe_seams[frozenset((left, right))]:
                safe_flip_rank_relations[(
                    seam,
                    pp[u], pp[v], pv[u], pv[v],
                    pp[u] - seam, pp[v] - seam,
                    pv[u] - seam, pv[v] - seam,
                )] += 1
        else:
            local_unsafe_type[local_key] += 1
            peak, valley = (left, right)
            u, _ = sorted(peak ^ valley)
            if u not in peak:
                peak, valley = valley, peak
            try:
                context = adjacent_leaf_context(peak, valley, r)
            except AssertionError:
                context = (-1, -1, -1)
            unsafe_context_hist[context] += 1
    safe_matching = nx.max_weight_matching(safe_graph, maxcardinality=True)
    block_involution = {}
    block_fixed = []
    for root in roots:
        mate = None
        for position in range(2, 2 * r, 2):
            if (position in root) != (position + 1 in root):
                mate = frozenset(root ^ {position, position + 1})
                break
        if mate is None:
            block_fixed.append(root)
        else:
            block_involution[root] = mate
    assert all(block_involution.get(mate) == root for root, mate in block_involution.items())
    block_unsafe_pairs = {
        frozenset((root, mate))
        for root, mate in block_involution.items()
        if not safe_graph.has_edge(root, mate)
    }
    block_unsafe_rows = tuple(
        sorted(tuple(sorted(word(x, r) for x in pair)) for pair in block_unsafe_pairs)
    ) if r <= 9 else ()
    coordinate_residual = set(roots)
    coordinate_rounds = []
    for position in range(1, 2 * r):
        pairs = set()
        for root in tuple(coordinate_residual):
            if (position in root) == (position + 1 in root):
                continue
            mate = frozenset(root ^ {position, position + 1})
            if (mate in coordinate_residual and safe_graph.has_edge(root, mate)):
                pairs.add(frozenset((root, mate)))
        vertices = set().union(*pairs) if pairs else set()
        coordinate_rounds.append(len(pairs))
        coordinate_residual -= vertices
    coordinate_residual_words = tuple(sorted(word(x, r) for x in coordinate_residual))
    coordinate_residual_hr_components = Counter(hr_component_key(x, r) for x in coordinate_residual)
    greedy_involution = {}
    for root in roots:
        choices = sorted(
            (
                min(root ^ other),
                tuple(sorted(other)),
                other,
            )
            for other in safe_graph.neighbors(root)
        )
        if choices:
            greedy_involution[root] = choices[0][2]
    greedy_involution_pairs = sum(
        greedy_involution.get(other) == root
        for root, other in greedy_involution.items()
    ) // 2
    residual = safe_graph.copy()
    iterated_minpos_rounds = []
    while residual:
        choice = {}
        for root in residual:
            candidates = sorted(
                (min(root ^ other), tuple(sorted(other)), other)
                for other in residual.neighbors(root)
            )
            if candidates:
                choice[root] = candidates[0][2]
        pairs = {
            frozenset((root, other))
            for root, other in choice.items()
            if choice.get(other) == root
        }
        if not pairs:
            break
        vertices = set().union(*pairs)
        iterated_minpos_rounds.append(len(pairs))
        residual.remove_nodes_from(vertices)
    iterated_minpos_residual_words = tuple(sorted(word(x, r) for x in residual))
    safe_degree_hist = dict(Counter(dict(safe_graph.degree()).values()))
    safe_components = []
    safe_component_rows = []
    safe_interval_components = 0
    safe_induced_interval_components = 0
    inv = {x: inversion_cells(x, r) for x in roots}
    for component in nx.connected_components(safe_graph):
        parity = Counter(
            sum((2 * r + 1 - i) for i in target) % 2 for target in component
        )
        safe_components.append((len(component), tuple(sorted(parity.items()))))
        lower = set.intersection(*(set(inv[x]) for x in component))
        upper = set.union(*(set(inv[x]) for x in component))
        hull = {x for x in roots if lower <= inv[x] <= upper}
        if hull == component:
            safe_interval_components += 1
            if all(
                safe_graph.has_edge(x, y)
                for x in component
                for i in range(1, 2 * r)
                if i in x and i + 1 not in x
                for y in [frozenset((x - {i}) | {i + 1})]
                if y in component
            ):
                safe_induced_interval_components += 1
        if r <= 6:
            safe_component_rows.append(
                (
                    len(component),
                    tuple(sum(i in x for x in component) for i in range(1, 2 * r + 1)),
                    tuple(sorted(Counter(return_composition(x, r) for x in component).items())),
                    tuple(sorted(word(x, r) for x in component)),
                )
            )
    safe_matching_rows = None
    safe_matching_position_seam_hist = None
    if r <= 6:
        safe_matching_rows = tuple(
            (word(left, r), word(right, r), safe_seams[frozenset((left, right))])
            for left, right in safe_matching
        )
        safe_matching_position_seam_hist = dict(Counter(
            (
                min(left ^ right),
                safe_seams[frozenset((left, right))],
            )
            for left, right in safe_matching
        ))

    return {
        "r": r,
        "layer_counts": dict(counts),
        "transition": transition,
        "root_adjacent_edges": len(root_adjacent),
        "canonical_pair_distance_profiles": {str(k): v for k, v in distance_profiles.items()},
        "canonical_middle_complement_edges": middle_complement,
        "canonical_endpoint_target_distance_hist": dict(endpoint_pair_hist),
        "canonical_tail_swap_seam_hist": {str(k): v for k, v in tail_swap_seams.items()},
        "canonical_tail_swap_delta1_edges": tail_swap_delta1_edges,
        "canonical_tail_swap_combined_ledger_hist": dict(tail_swap_combined_ledger_hist),
        "canonical_tail_swap_flip_rank_relations": dict(safe_flip_rank_relations),
        "canonical_tail_swap_safe_context_hist": dict(safe_context_hist),
        "canonical_tail_swap_unsafe_context_hist": dict(unsafe_context_hist),
        "canonical_tail_swap_local_safe_type": dict(local_safe_type),
        "canonical_tail_swap_local_unsafe_type": dict(local_unsafe_type),
        "canonical_tail_swap_matching": len(safe_matching),
        "canonical_tail_swap_block_fixed": len(block_fixed),
        "canonical_tail_swap_block_pairs": len(block_involution) // 2,
        "canonical_tail_swap_block_unsafe_pairs": len(block_unsafe_pairs),
        "canonical_tail_swap_block_unsafe_rows": block_unsafe_rows,
        "canonical_tail_swap_coordinate_rounds": tuple(coordinate_rounds),
        "canonical_tail_swap_coordinate_leave": len(coordinate_residual),
        "canonical_tail_swap_coordinate_residual_words": coordinate_residual_words,
        "canonical_tail_swap_coordinate_residual_hr_component_hist": dict(
            Counter(coordinate_residual_hr_components.values())
        ),
        "canonical_tail_swap_matching_perfect": 2 * len(safe_matching) == len(roots),
        "canonical_tail_swap_matching_rows": safe_matching_rows,
        "canonical_tail_swap_matching_position_seam_hist": safe_matching_position_seam_hist,
        "canonical_tail_swap_degree_hist": safe_degree_hist,
        "canonical_tail_swap_minpos_involution_pairs": greedy_involution_pairs,
        "canonical_tail_swap_minpos_involution_perfect": 2 * greedy_involution_pairs == len(roots),
        "canonical_tail_swap_iterated_minpos_rounds": tuple(iterated_minpos_rounds),
        "canonical_tail_swap_iterated_minpos_leave": residual.number_of_nodes(),
        "canonical_tail_swap_iterated_minpos_residual_words": iterated_minpos_residual_words,
        "canonical_tail_swap_components": tuple(sorted(safe_components)),
        "canonical_tail_swap_interval_components": safe_interval_components,
        "canonical_tail_swap_induced_interval_components": safe_induced_interval_components,
        "canonical_tail_swap_component_rows": tuple(sorted(safe_component_rows)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6, 8])
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        result = audit(r)
        if args.summary:
            keep = (
                "r", "root_adjacent_edges", "canonical_tail_swap_delta1_edges",
                "canonical_tail_swap_matching", "canonical_tail_swap_matching_perfect",
                "canonical_tail_swap_block_fixed", "canonical_tail_swap_block_pairs",
                "canonical_tail_swap_block_unsafe_pairs",
                "canonical_tail_swap_block_unsafe_rows",
                "canonical_tail_swap_coordinate_rounds",
                "canonical_tail_swap_coordinate_leave",
                "canonical_tail_swap_coordinate_residual_words",
                "canonical_tail_swap_coordinate_residual_hr_component_hist",
                "canonical_tail_swap_degree_hist", "canonical_tail_swap_components",
                "canonical_tail_swap_minpos_involution_pairs",
                "canonical_tail_swap_minpos_involution_perfect",
                "canonical_tail_swap_iterated_minpos_rounds",
                "canonical_tail_swap_iterated_minpos_leave",
                "canonical_tail_swap_iterated_minpos_residual_words",
                "canonical_tail_swap_component_rows",
                "canonical_tail_swap_interval_components",
                "canonical_tail_swap_induced_interval_components",
            )
            result = {key: result[key] for key in keep}
        print("DYCK_PAIRED_PHASE_STRUCTURE", result, flush=True)


if __name__ == "__main__":
    main()
