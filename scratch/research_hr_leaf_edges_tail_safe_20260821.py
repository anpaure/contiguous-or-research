#!/usr/bin/env python3
"""Compare H_r-conjugated leaf moves with canonical defect-one tail seams."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product

import networkx as nx

from research_dyck_paired_phase_structure_20260821 import build_paths
from research_dyck_safe_seam_context_lifts_20260821 import safe_seams, target


def raw(x, r):
    return "".join("1" if i in x else "0" for i in range(1, 2 * r + 1))


def hr_edges(r, paths):
    roots = set(paths)
    answer = set()
    by_type = Counter()
    for root in roots:
        word = raw(root, r)
        pairs = [word[i:i + 2] for i in range(1, 2 * r - 1, 2)]
        steps = [1 if pair == "11" else -1 if pair == "00" else 0 for pair in pairs]
        # Odd-start colour toggles.
        for i, pair in enumerate(pairs):
            if pair not in ("10", "01"):
                continue
            if i > 0 and steps[i - 1] == -1:
                continue
            if i + 1 < len(pairs) and steps[i + 1] == 1:
                continue
            other = list(word)
            p = 1 + 2 * i
            other[p], other[p + 1] = other[p + 1], other[p]
            mate = target("".join(other))
            assert mate in roots and len(root ^ mate) == 2
            answer.add(frozenset((root, mate)))
            by_type["odd"] += 1
        # Even-start UD <-> any HH decoration.  Generate from UD once.
        for i in range(len(pairs) - 1):
            if pairs[i:i + 2] != ["11", "00"]:
                continue
            for first, second in product(("10", "01"), repeat=2):
                other = word[:1 + 2 * i] + first + second + word[1 + 2 * (i + 2):]
                mate = target(other)
                assert mate in roots and len(root ^ mate) == 2
                answer.add(frozenset((root, mate)))
                by_type[("even", first, second)] += 1
    return answer, by_type


def audit(r):
    paths = build_paths(r)
    edges, raw_types = hr_edges(r, paths)
    safe = {}
    unsafe = []
    coordinate_gap = Counter()
    graph = nx.Graph()
    graph.add_nodes_from(paths)
    for pair in edges:
        left, right = tuple(pair)
        seams = safe_seams(left, right, r, paths)
        gap = abs(next(iter(left - right)) - next(iter(right - left)))
        coordinate_gap[gap] += 1
        if seams:
            safe[pair] = seams
            graph.add_edge(left, right)
        else:
            unsafe.append((raw(left, r), raw(right, r), gap))
    matching = nx.max_weight_matching(graph, maxcardinality=True)
    adjacent_graph = nx.Graph()
    adjacent_graph.add_nodes_from(paths)
    adjacent_graph.add_edges_from(
        tuple(pair) for pair in safe
        if abs(next(iter(tuple(pair)[0] - tuple(pair)[1]))
               - next(iter(tuple(pair)[1] - tuple(pair)[0]))) == 1
    )
    residual = set(paths)
    rounds = []
    for position in range(1, 2 * r):
        pairs = set()
        for root in tuple(residual):
            if (position in root) == (position + 1 in root):
                continue
            mate = frozenset(root ^ {position, position + 1})
            if mate in residual and adjacent_graph.has_edge(root, mate):
                pairs.add(frozenset((root, mate)))
        vertices = set().union(*pairs) if pairs else set()
        residual -= vertices
        rounds.append(len(pairs))
    return {
        "r": r,
        "roots": len(paths),
        "hr_edges": len(edges),
        "raw_type_occurrences": dict(raw_types),
        "coordinate_gap": dict(coordinate_gap),
        "tail_safe": len(safe),
        "tail_unsafe": len(unsafe),
        "unsafe_examples": tuple(unsafe[:20]),
        "safe_matching": len(matching),
        "safe_leave": len(paths) - 2 * len(matching),
        "adjacent_coordinate_rounds": tuple(rounds),
        "adjacent_coordinate_leave": len(residual),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4, 5, 6, 7])
    args = parser.parse_args()
    for r in args.r:
        print("HR_LEAF_TAIL_SAFE", audit(r), flush=True)


if __name__ == "__main__":
    main()
