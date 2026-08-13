#!/usr/bin/env python3
"""Build the split-aware D5 suffix label tree from frozen child atlases.

Substantive execution belongs on H100.  The extreme first-return blocks use
the thirteen frozen D4 suffix-tree edges under ``10`` and primitive wrapping.
The (1,3) and (3,1) blocks use the four frozen D3 tree edges in the appropriate
left/right contexts.  The (2,2) block uses the Cartesian D2 square minus one
edge.  One lexicographically first Johnson edge bridges each consecutive pair
of split blocks.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from verify_t2_suffix_s3_actuator_catalogue_20260813 import CATALOGUE  # noqa:E402


def split(word):
    height = 0
    for index, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            return ((index - 1) // 2, (len(word) - index - 1) // 2)
    raise AssertionError(word)


def edge(left, right, role, child=None):
    assert left != right
    assert (base.bits(left) ^ base.bits(right)).bit_count() == 2
    return {
        "suffix_edge": [left, right],
        "split_pair": [list(split(left)), list(split(right))],
        "role": role,
        "child": child,
    }


def main():
    certificate_path = Path(
        sys.argv[1] if len(sys.argv) > 1
        else "search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out"
    )
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    vertices = list(base.dyck_words(5))
    by_split = defaultdict(list)
    for word in vertices:
        by_split[split(word)].append(word)
    assert Counter(map(len, by_split.values())) == Counter({14: 2, 5: 2, 4: 1})

    tree = []
    d4_edges = [item["suffix_edge"] for item in certificate["selection"]]
    for left, right in d4_edges:
        tree.append(edge("10" + left, "10" + right, "child_D4", "10"))
        tree.append(edge("1" + left + "0", "1" + right + "0", "child_D4", "wrap"))

    d3_edges = [item["suffix_edge"] for item in CATALOGUE]
    for left, right in d3_edges:
        tree.append(edge("1100" + left, "1100" + right, "child_D3", "right"))
        tree.append(edge("1" + left + "010", "1" + right + "010", "child_D3", "wrap_tail"))

    d2 = list(base.dyck_words(2))
    assert d2 == ["1100", "1010"]
    square = {
        (u, v): "1" + u + "0" + v for u in d2 for v in d2
    }
    tree.extend([
        edge(square[(d2[0], d2[0])], square[(d2[1], d2[0])], "child_D2", "left"),
        edge(square[(d2[0], d2[1])], square[(d2[1], d2[1])], "child_D2", "left"),
        edge(square[(d2[0], d2[0])], square[(d2[0], d2[1])], "child_D2", "right"),
    ])

    # Add one bridge between each consecutive first-return split.
    split_order = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
    for first, second in zip(split_order, split_order[1:]):
        candidates = sorted(
            (left, right)
            for left in by_split[first]
            for right in by_split[second]
            if (base.bits(left) ^ base.bits(right)).bit_count() == 2
        )
        assert candidates, (first, second)
        left, right = candidates[0]
        tree.append(edge(left, right, "split_bridge", f"{first}->{second}"))

    assert len(tree) == len(vertices) - 1 == 41
    edge_keys = [tuple(sorted(item["suffix_edge"])) for item in tree]
    assert len(set(edge_keys)) == len(edge_keys)
    adjacency = defaultdict(list)
    for item in tree:
        left, right = item["suffix_edge"]
        adjacency[left].append(right)
        adjacency[right].append(left)
    seen = {vertices[0]}
    queue = deque(seen)
    while queue:
        word = queue.popleft()
        for other in adjacency[word]:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    assert seen == set(vertices)

    print(json.dumps({
        "status": "PASS",
        "suffix_semilength": 5,
        "vertices": vertices,
        "split_sizes": {
            str(key): len(value) for key, value in sorted(by_split.items())
        },
        "tree_edges": tree,
        "role_histogram": dict(sorted(Counter(
            item["role"] for item in tree
        ).items())),
        "degree_histogram": dict(sorted(Counter(
            len(adjacency[word]) for word in vertices
        ).items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
