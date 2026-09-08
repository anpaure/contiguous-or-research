#!/usr/bin/env python3
"""Exact recut search for mirrored Chung--Feller double cycles.

For the canonical first-half phase matchings, form the complement/time-
reversal mirrored Johnson paths.  The closure involution pairs two such
paths into a length-(4r+2) closed walk in the odd graph.  On those pairs
which are simple cycles, enumerate k-edge recuts and ask whether they split
the vertex set into two ordinary length-(2r+1) odd cycles.

This is a research diagnostic.  Substantive runs are on ssh h100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

from research_c8_orbit_phase_normal_form_20260821 import (
    canonical_layers,
    rooted_x_path,
)
from research_msw_c8_shadow_anneal_20260821 import dyck_words, msw_row


def canonical_root_paths(r):
    anchor = 2 * r + 1
    paths = {}
    for word in dyck_words(r):
        row = msw_row(word)
        root = frozenset(i + 1 for i, bit in enumerate(word) if bit == "1")
        paths[root] = rooted_x_path(row, r, root, anchor)
    return paths


def mirrored_johnson_path(root, paths, r):
    ground = frozenset(range(1, 2 * r + 1))
    h = r // 2
    middle_to_root = {path[h]: source for source, path in paths.items()}
    mate = middle_to_root[ground - paths[root][h]]
    left = paths[root][: h + 1]
    right = tuple(ground - paths[mate][r - t] for t in range(h + 1, r + 1))
    answer = left + right
    assert len(answer) == r + 1
    assert answer[-1] == ground - mate
    assert all(len(answer[t] ^ answer[t + 1]) == 2 for t in range(r))
    return answer, mate


def lift_johnson_path(path, r):
    ground = frozenset(range(1, 2 * r + 1))
    anchor = 2 * r + 1
    lifted = [path[0]]
    for left, right in zip(path, path[1:]):
        union_colour = frozenset({anchor}) | (ground - (left | right))
        assert len(union_colour) == r
        assert not (left & union_colour) and not (right & union_colour)
        lifted.extend((union_colour, right))
    return tuple(lifted)


def paired_cycles(r):
    assert r % 2 == 0
    # The call also asserts that the canonical phase classes partition the
    # whole rank-r layer; the returned layer is not otherwise needed here.
    canonical_layers(r)
    paths = canonical_root_paths(r)
    seen = set()
    answer = []
    for root in sorted(paths, key=lambda x: tuple(sorted(x))):
        if root in seen:
            continue
        path, mate = mirrored_johnson_path(root, paths, r)
        mate_path, back = mirrored_johnson_path(mate, paths, r)
        assert back == root and mate != root
        seen.update((root, mate))
        first = lift_johnson_path(path, r)
        second = lift_johnson_path(mate_path, r)
        cycle = first + second
        assert not (first[-1] & second[0])
        assert not (second[-1] & first[0])
        answer.append((root, mate, cycle))
    assert len(seen) == len(paths)
    return answer


def edge(x, y):
    return frozenset((x, y))


def is_odd_edge(x, y):
    return not (x & y)


def components(vertices, edges):
    adjacency = {v: [] for v in vertices}
    for xy in edges:
        x, y = tuple(xy)
        adjacency[x].append(y)
        adjacency[y].append(x)
    if any(len(adjacency[v]) != 2 for v in vertices):
        return None
    result = []
    unseen = set(vertices)
    while unseen:
        start = next(iter(unseen))
        cycle = [start]
        previous = None
        current = start
        while True:
            options = [x for x in adjacency[current] if x != previous]
            if not options:
                return None
            nxt = options[0]
            if nxt == start:
                break
            if nxt in cycle:
                return None
            cycle.append(nxt)
            previous, current = current, nxt
        unseen.difference_update(cycle)
        result.append(tuple(cycle))
    return tuple(result)


def matchings(points, allowed, prefix=()):
    if not points:
        yield prefix
        return
    first = points[0]
    for index in range(1, len(points)):
        second = points[index]
        xy = edge(first, second)
        if xy not in allowed:
            continue
        rest = points[1:index] + points[index + 1 :]
        yield from matchings(rest, allowed, prefix + (xy,))


def shortest_odd_cycle_is_wreath(cycle, full_ground):
    holes = []
    for i, left in enumerate(cycle):
        right = cycle[(i + 1) % len(cycle)]
        gap = full_ground - left - right
        assert len(gap) == 1
        holes.append(next(iter(gap)))
    return len(set(holes)) == len(full_ground)


def induced_two_wreath_factors(cycle, r):
    """Enumerate all two-b-cycle factors in the induced odd subgraph.

    The induced graph is the base 2b-cycle plus a small chord set in the
    cases of interest.  After choosing a chord subset, the degree-two
    equations on the remaining cyclic edges have at most two solutions.
    """
    n = len(cycle)
    b = 2 * r + 1
    vertices = frozenset(cycle)
    base = tuple(edge(cycle[i], cycle[(i + 1) % n]) for i in range(n))
    base_set = frozenset(base)
    chords = tuple(
        edge(x, y)
        for x, y in combinations(cycle, 2)
        if is_odd_edge(x, y) and edge(x, y) not in base_set
    )
    full_ground = frozenset(range(1, 2 * r + 2))
    witnesses = []
    for mask in range(1 << len(chords)):
        chosen = tuple(chords[j] for j in range(len(chords)) if mask >> j & 1)
        chord_degree = Counter(v for xy in chosen for v in xy)
        if any(value > 2 for value in chord_degree.values()):
            continue
        required = [2 - chord_degree[cycle[i]] for i in range(n)]
        if any(value < 0 or value > 2 for value in required):
            continue
        # Let x_i indicate use of cyclic edge (i,i+1).  Equations are
        # x_{i-1}+x_i=required_i.  Try the two possible x_0 values.
        for x0 in (0, 1):
            x = [x0]
            valid = True
            for i in range(1, n):
                value = required[i] - x[i - 1]
                if value not in (0, 1):
                    valid = False
                    break
                x.append(value)
            if not valid or x[-1] + x[0] != required[0]:
                continue
            selected = frozenset(chosen) | frozenset(base[i] for i in range(n) if x[i])
            comps = components(vertices, selected)
            if comps is None or sorted(map(len, comps)) != [b, b]:
                continue
            assert all(shortest_odd_cycle_is_wreath(comp, full_ground) for comp in comps)
            removed = base_set - selected
            added = selected - base_set
            assert len(removed) == len(added)
            witnesses.append(
                {
                    "changes": len(removed),
                    "chosen_chords": len(chosen),
                    "cycle_lengths": tuple(sorted(map(len, comps))),
                }
            )
    return tuple(witnesses), len(chords)


def recuts(cycle, r, cut_count, stop_after_first=False):
    n = len(cycle)
    b = 2 * r + 1
    vertices = frozenset(cycle)
    assert n == 2 * b and len(vertices) == n
    old = tuple(edge(cycle[i], cycle[(i + 1) % n]) for i in range(n))
    old_set = frozenset(old)
    full_ground = frozenset(range(1, 2 * r + 2))
    witnesses = []
    tested_cut_sets = 0
    tested_matchings = 0
    for indices in combinations(range(n), cut_count):
        # Adjacent cuts make one isolated path vertex.  They are legitimate,
        # so do not pre-filter them.
        removed = frozenset(old[i] for i in indices)
        kept = old_set - removed
        endpoints = []
        for i in indices:
            endpoints.extend((cycle[i], cycle[(i + 1) % n]))
        if len(set(endpoints)) != 2 * cut_count:
            # Adjacent removed edges share their intervening vertex; that
            # vertex has degree zero and would need two new incidences, not a
            # perfect matching on endpoints.  This search targets pure
            # alternating 2k-cycle exchanges, so skip that different move.
            continue
        tested_cut_sets += 1
        allowed = set()
        for x, y in combinations(endpoints, 2):
            xy = edge(x, y)
            if xy in kept:
                continue
            if is_odd_edge(x, y):
                allowed.add(xy)
        for added in matchings(tuple(endpoints), frozenset(allowed)):
            tested_matchings += 1
            new_edges = kept | frozenset(added)
            comps = components(vertices, new_edges)
            if comps is None or sorted(map(len, comps)) != [b, b]:
                continue
            assert all(shortest_odd_cycle_is_wreath(comp, full_ground) for comp in comps)
            effective_removed = old_set - new_edges
            effective_added = new_edges - old_set
            assert len(effective_removed) == len(effective_added)
            witnesses.append(
                {
                    "cut_indices": indices,
                    "effective_changes": len(effective_removed),
                    "added_edges": tuple(
                        sorted(
                            (tuple(sorted(x)), tuple(sorted(y)))
                            for xy in effective_added
                            for x, y in [tuple(xy)]
                        )
                    ),
                    "cycle_lengths": tuple(sorted(map(len, comps))),
                }
            )
            if stop_after_first:
                return witnesses, tested_cut_sets, tested_matchings
    return witnesses, tested_cut_sets, tested_matchings


def audit(r, max_cut, stop_after_first):
    pairs = paired_cycles(r)
    overlap_hist = Counter(2 * (2 * r + 1) - len(set(cycle)) for _, _, cycle in pairs)
    simple = [(root, mate, cycle) for root, mate, cycle in pairs if len(set(cycle)) == len(cycle)]
    first_path_hole_defect_hist = Counter()
    simple_hole_defect_hist = Counter()
    full_ground = frozenset(range(1, 2 * r + 2))
    for _, _, cycle in pairs:
        first_path = cycle[: 2 * r + 1]
        holes = []
        for left, right in zip(first_path, first_path[1:]):
            gap = full_ground - left - right
            assert len(gap) == 1
            holes.append(next(iter(gap)))
        assert (2 * r + 1) not in holes
        defect = 2 * r - len(set(holes))
        first_path_hole_defect_hist[defect] += 1
        if len(set(cycle)) == len(cycle):
            simple_hole_defect_hist[defect] += 1
    chord_hist = Counter()
    parity_breaking_chord_hist = Counter()
    parity_breaking_matching_hist = Counter()
    induced_factor_hist = Counter()
    induced_examples = {}
    for _, _, cycle in simple:
        old = {
            edge(cycle[i], cycle[(i + 1) % len(cycle)])
            for i in range(len(cycle))
        }
        index = {vertex: i for i, vertex in enumerate(cycle)}
        chord_edges = [
            edge(x, y)
            for x, y in combinations(cycle, 2)
            if is_odd_edge(x, y) and edge(x, y) not in old
        ]
        chords = len(chord_edges)
        chord_hist[chords] += 1
        breakers = [
            xy for xy in chord_edges
            if len({index[v] % 2 for v in xy}) == 1
        ]
        parity_breaking_chord_hist[len(breakers)] += 1
        max_disjoint = 0
        for subset_mask in range(1 << len(breakers)):
            chosen = [breakers[j] for j in range(len(breakers)) if subset_mask >> j & 1]
            if len(set(v for xy in chosen for v in xy)) == 2 * len(chosen):
                max_disjoint = max(max_disjoint, len(chosen))
        parity_breaking_matching_hist[max_disjoint] += 1
        factors, checked_chords = induced_two_wreath_factors(cycle, r)
        assert checked_chords == chords
        best = min((w["changes"] for w in factors), default=None)
        induced_factor_hist[best] += 1
        if factors and best not in induced_examples:
            induced_examples[best] = min(factors, key=lambda w: w["changes"])
    cut_hist = Counter()
    examples = {}
    work = Counter()
    for pair_index, (root, mate, cycle) in enumerate(simple):
        found = False
        for cut_count in range(2, max_cut + 1):
            witnesses, cut_sets, matching_count = recuts(
                cycle, r, cut_count, stop_after_first=stop_after_first
            )
            work[(cut_count, "cut_sets")] += cut_sets
            work[(cut_count, "matchings")] += matching_count
            if witnesses:
                best = min(w["effective_changes"] for w in witnesses)
                cut_hist[best] += 1
                examples.setdefault(
                    best,
                    {
                        "pair_index": pair_index,
                        "root": tuple(sorted(root)),
                        "mate": tuple(sorted(mate)),
                        "witness": min(witnesses, key=lambda w: w["effective_changes"]),
                    },
                )
                found = True
                break
        if not found:
            cut_hist[None] += 1
    return {
        "r": r,
        "pairs": len(pairs),
        "overlap_hist": dict(overlap_hist),
        "simple_pairs": len(simple),
        "first_path_hole_defect_hist": dict(first_path_hole_defect_hist),
        "simple_hole_defect_hist": dict(simple_hole_defect_hist),
        "induced_chord_hist": dict(chord_hist),
        "parity_breaking_chord_hist": dict(parity_breaking_chord_hist),
        "parity_breaking_matching_hist": dict(parity_breaking_matching_hist),
        "induced_two_wreath_factor_hist": {
            str(k): v for k, v in induced_factor_hist.items()
        },
        "induced_factor_examples": induced_examples,
        "minimum_effective_change_hist": {str(k): v for k, v in cut_hist.items()},
        "examples": examples,
        "work": {str(k): v for k, v in work.items()},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--max-cut", type=int, default=3)
    parser.add_argument("--all-witnesses", action="store_true")
    args = parser.parse_args()
    for r in args.r:
        print(
            "MIRRORED_DOUBLE_CYCLE_RECUT",
            audit(r, args.max_cut, not args.all_witnesses),
            flush=True,
        )


if __name__ == "__main__":
    main()
