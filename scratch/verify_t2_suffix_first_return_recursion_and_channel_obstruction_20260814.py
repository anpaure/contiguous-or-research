#!/usr/bin/env python3
"""Verify the symbolic first-return suffix-tree recurrence and its port cut.

Substantive execution belongs on H100.  The recurrence is seeded by the
frozen D3 and D4 suffix trees and then uses the same product construction
as the frozen D5 builder.  The script also verifies the canonical matching
between consecutive first-return blocks and the exact MSW rank signature
of every bridge in that matching.  Other cross-split Johnson edges may
exist; no completeness claim is made for the canonical matching.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product


D3_EDGES = (
    ("111000", "101100"),
    ("111000", "101010"),
    ("110100", "110010"),
    ("110100", "101100"),
)

D4_EDGES = (
    ("11110000", "10111000"),
    ("11110000", "10110010"),
    ("11101000", "10101100"),
    ("10101010", "11101000"),
    ("11100100", "11100010"),
    ("10101100", "11100100"),
    ("11011000", "11001100"),
    ("10111000", "11011000"),
    ("11010100", "11010010"),
    ("10110100", "11010100"),
    ("11010010", "11001010"),
    ("11001010", "10101010"),
    ("10110010", "10110100"),
)


@lru_cache(None)
def dyck_words(s: int) -> tuple[str, ...]:
    if s == 0:
        return ("",)
    out = []

    def rec(prefix: str, ones: int, zeros: int) -> None:
        if ones == zeros == s:
            out.append(prefix)
            return
        if ones < s:
            rec(prefix + "1", ones + 1, zeros)
        if zeros < ones:
            rec(prefix + "0", ones, zeros + 1)

    rec("", 0, 0)
    return tuple(out)


def split(word: str) -> tuple[int, int]:
    height = 0
    for index, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            return (index // 2, (len(word) - index - 1) // 2)
    raise AssertionError(word)


def mountain(s: int) -> str:
    return "1" * s + "0" * s


def zigzag(s: int) -> str:
    return "10" * s


def edge_key(left: str, right: str) -> tuple[str, str]:
    assert left != right
    assert sum(a != b for a, b in zip(left, right)) == 2
    return tuple(sorted((left, right)))


def check_tree(s: int, edges: set[tuple[str, str]]) -> dict:
    vertices = set(dyck_words(s))
    assert len(edges) == len(vertices) - 1
    adjacency = defaultdict(set)
    for left, right in edges:
        assert left in vertices and right in vertices
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = {next(iter(vertices))}
    queue = deque(seen)
    while queue:
        word = queue.popleft()
        for other in adjacency[word]:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    assert seen == vertices
    return {
        "vertices": len(vertices),
        "edges": len(edges),
        "max_degree": max(map(len, adjacency.values()), default=0),
        "mountain_degree": len(adjacency[mountain(s)]),
        "zigzag_degree": len(adjacency[zigzag(s)]),
        "degree_histogram": dict(sorted(Counter(map(len, adjacency.values())).items())),
    }


def build_next(s: int, trees: dict[int, set[tuple[str, str]]]):
    """Build T_s from T_i, i<s, using the frozen-D5 product grammar."""
    edges = set()
    roles = Counter()
    for i in range(s):
        j = s - 1 - i
        # A copy of T_i in every right-child fibre.
        for right in dyck_words(j):
            for left0, left1 in trees[i]:
                key = edge_key("1" + left0 + "0" + right,
                               "1" + left1 + "0" + right)
                assert key not in edges
                edges.add(key)
                roles[f"left_T{i}"] += 1
        # One copy of T_j at the mountain reset anchor in the left child.
        for right0, right1 in trees[j]:
            key = edge_key("1" + mountain(i) + "0" + right0,
                           "1" + mountain(i) + "0" + right1)
            assert key not in edges
            edges.add(key)
            roles[f"right_T{j}"] += 1

    # Lexicographic zigzag bridges between consecutive split blocks.
    bridges = []
    for i in range(s - 1):
        j = s - 1 - i
        left = "1" + zigzag(i) + "0" + zigzag(j)
        right = "1" + zigzag(i + 1) + "0" + zigzag(j - 1)
        key = edge_key(left, right)
        assert key not in edges
        edges.add(key)
        bridges.append(key)
        roles["split_bridge"] += 1
    return edges, roles, bridges


def mu(word: str) -> str:
    return "".join("1" if bit == "0" else "0" for bit in word[::-1])


@lru_cache(None)
def rho(word: str) -> tuple[int, ...]:
    if not word:
        return ()
    height = 0
    for index, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            break
    inside = word[1:index]
    tail = word[index + 1:]
    a = len(inside) + 2
    return ((a,)
            + tuple(a - value for value in rho(mu(inside)))
            + (1,)
            + tuple(a + value for value in rho(tail)))


def half_ranks(word: str):
    order = rho(word)
    insertion = {coordinate: rank for rank, coordinate in enumerate(order[0::2], 1)}
    deletion = {coordinate: rank for rank, coordinate in enumerate(order[1::2], 1)}
    return insertion, deletion


def bridge_pair(i: int, j: int, inside: str, tail: str):
    assert inside in dyck_words(i)
    assert tail in dyck_words(j - 1)
    left = "1" + inside + "0" + "10" + tail
    right = "1" + inside + "10" + "0" + tail
    return left, right


def consecutive_interface(s: int, i: int):
    """Verify the canonical matching inside the split-i/split-(i+1) interface."""
    j = s - 1 - i
    assert j >= 1
    left_block = [word for word in dyck_words(s) if split(word) == (i, j)]
    right_block = [word for word in dyck_words(s) if split(word) == (i + 1, j - 1)]
    actual = {
        edge_key(left, right)
        for left, right in product(left_block, right_block)
        if sum(a != b for a, b in zip(left, right)) == 2
    }
    formula = {
        edge_key(*bridge_pair(i, j, inside, tail))
        for inside, tail in product(dyck_words(i), dyck_words(j - 1))
    }
    assert formula <= actual
    assert len(formula) == len(dyck_words(i)) * len(dyck_words(j - 1))
    endpoints = [endpoint for edge in formula for endpoint in edge]
    assert len(endpoints) == len(set(endpoints))

    # Every member of this complete interface matching has the same four
    # intrinsic MSW ranks.  Coordinates are one-indexed.
    signatures = set()
    for inside, tail in product(dyck_words(i), dyck_words(j - 1)):
        left, right = bridge_pair(i, j, inside, tail)
        p, q = 2 * i + 2, 2 * i + 3
        insert_left, delete_left = half_ranks(left)
        insert_right, delete_right = half_ranks(right)
        signatures.add((
            delete_left[q], insert_left[p],
            delete_right[p], insert_right[q],
        ))
    assert signatures == {(i + 2, 1, 1, 2)}
    return len(formula), len(actual), next(iter(signatures))


def main() -> None:
    trees = {
        0: set(),
        1: set(),
        2: {edge_key("1100", "1010")},
        3: {edge_key(*edge) for edge in D3_EDGES},
        4: {edge_key(*edge) for edge in D4_EDGES},
    }
    summaries = {s: check_tree(s, tree) for s, tree in trees.items()}
    role_summaries = {}
    bridge_summaries = {}
    for s in range(5, 10):
        tree, roles, bridges = build_next(s, trees)
        trees[s] = tree
        summaries[s] = check_tree(s, tree)
        role_summaries[s] = dict(sorted(roles.items()))
        bridge_summaries[s] = bridges

    # This is exactly the D5 role census frozen in the actuator theorem.
    d5_roles = role_summaries[5]
    assert sum(value for key, value in d5_roles.items() if key in {"left_T4", "right_T4"}) == 26
    assert sum(value for key, value in d5_roles.items() if key in {"left_T3", "right_T3"}) == 8
    assert sum(value for key, value in d5_roles.items() if key in {"left_T2", "right_T2"}) == 3
    assert d5_roles["split_bridge"] == 4
    assert [list(edge) for edge in bridge_summaries[5]] == [
        ["1010101010", "1100101010"],
        ["1100101010", "1101001010"],
        ["1101001010", "1101010010"],
        ["1101010010", "1101010100"],
    ]

    # The inherited zigzag port gains one child edge and one new split
    # bridge at every level after D4.
    for s in range(3, 10):
        assert summaries[s]["zigzag_degree"] == s - 2
    assert summaries[8]["zigzag_degree"] == 6
    assert summaries[9]["zigzag_degree"] == 7

    interfaces = {}
    for s in range(2, 9):
        for i in range(s - 1):
            interfaces[(s, i)] = consecutive_interface(s, i)

    print("STATUS PASS")
    print("D5_ROLE_TOTALS child_D4=26 child_D3=8 child_D2=3 split_bridge=4")
    print("D5_BRIDGES", [list(edge) for edge in bridge_summaries[5]])
    print("TREE_SUMMARIES")
    for s in range(2, 10):
        print(s, summaries[s])
    print("INTERFACE_SIGNATURES")
    for key in sorted(interfaces):
        print(key, interfaces[key])
    print("SIX_CHANNEL_CUT first_failure_semilength=9 zigzag_degree=7")


if __name__ == "__main__":
    main()
