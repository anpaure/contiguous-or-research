#!/usr/bin/env python3
"""Finite audit for the even-Dyck induced-Johnson perfect-matching corollary.

This checker does not implement or replace the Ruskey--Proskurowski theorem.
It independently enumerates the relevant graph for small r and verifies:

* the Catalan vertex count;
* every adjacent-swap edge is an induced Johnson edge;
* the parity bipartition is valid;
* an exact maximum matching saturates all vertices for each tested even r.
"""

from __future__ import annotations

from collections import deque
from math import comb


def dyck_words(r: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    word = [0] * (2 * r)

    def rec(pos: int, ones: int, zeros: int) -> None:
        if pos == 2 * r:
            assert ones == zeros == r
            out.append(tuple(word))
            return
        if ones < r:
            word[pos] = 1
            rec(pos + 1, ones + 1, zeros)
        if zeros < ones:
            word[pos] = 0
            rec(pos + 1, ones, zeros + 1)

    rec(0, 0, 0)
    return out


def is_dyck(word: tuple[int, ...]) -> bool:
    height = 0
    for bit in word:
        height += 1 if bit else -1
        if height < 0:
            return False
    return height == 0


def adjacent_swap_graph(
    words: list[tuple[int, ...]],
) -> list[list[int]]:
    index = {word: i for i, word in enumerate(words)}
    graph: list[list[int]] = [[] for _ in words]
    for u, word in enumerate(words):
        for pos in range(len(word) - 1):
            if word[pos] == word[pos + 1]:
                continue
            changed = list(word)
            changed[pos], changed[pos + 1] = changed[pos + 1], changed[pos]
            other = tuple(changed)
            v = index.get(other)
            if v is not None:
                graph[u].append(v)
    return graph


def hopcroft_karp(
    graph: list[list[int]], left: list[int], right_set: set[int]
) -> tuple[int, list[int]]:
    """Maximum matching in the parity-bipartite graph."""

    n = len(graph)
    mate = [-1] * n
    dist = [-1] * n

    def bfs() -> bool:
        queue: deque[int] = deque()
        found = False
        for u in left:
            if mate[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                assert v in right_set
                u2 = mate[v]
                if u2 == -1:
                    found = True
                elif dist[u2] == -1:
                    dist[u2] = dist[u] + 1
                    queue.append(u2)
        return found

    def dfs(u: int) -> bool:
        for v in graph[u]:
            u2 = mate[v]
            if u2 == -1 or (dist[u2] == dist[u] + 1 and dfs(u2)):
                mate[u] = v
                mate[v] = u
                return True
        dist[u] = -1
        return False

    size = 0
    while bfs():
        for u in left:
            if mate[u] == -1 and dfs(u):
                size += 1
    return size, mate


def audit(r: int) -> dict[str, int | bool]:
    words = dyck_words(r)
    catalan = comb(2 * r, r) // (r + 1)
    assert len(words) == catalan
    assert len(set(words)) == len(words)
    assert all(is_dyck(word) for word in words)

    graph = adjacent_swap_graph(words)
    edge_twice = sum(map(len, graph))
    assert edge_twice % 2 == 0

    subsets = [{i for i, bit in enumerate(word) if bit} for word in words]
    parity = [sum(subset) & 1 for subset in subsets]
    for u, neighbors in enumerate(graph):
        assert len(neighbors) == len(set(neighbors))
        for v in neighbors:
            assert u in graph[v]
            difference = subsets[u] ^ subsets[v]
            assert len(difference) == 2
            a, b = sorted(difference)
            assert b == a + 1
            assert parity[u] != parity[v]

    left = [u for u in range(len(words)) if parity[u] == 0]
    right = {u for u in range(len(words)) if parity[u] == 1}
    matching_size, mate = hopcroft_karp(graph, left, right)
    assert sum(v != -1 for v in mate) == 2 * matching_size
    for u, v in enumerate(mate):
        if v != -1:
            assert mate[v] == u and v in graph[u]

    if r % 2 == 0:
        # The analytic parity identity used in the note.
        half_binomial = comb(2 * r - 1, r - 1)
        assert half_binomial % (r + 1) == 0
        assert catalan == 2 * (half_binomial // (r + 1))
        assert 2 * matching_size == catalan

    return {
        "r": r,
        "vertices": catalan,
        "edges": edge_twice // 2,
        "left": len(left),
        "right": len(right),
        "matching": matching_size,
        "perfect": 2 * matching_size == catalan,
    }


def main() -> None:
    print("even-Dyck induced-Johnson finite audit")
    for r in range(1, 11):
        record = audit(r)
        print(
            "r={r:2d}  |V|={vertices:6d}  |E|={edges:7d}  "
            "shores=({left:6d},{right:6d})  nu={matching:6d}  "
            "perfect={perfect}".format(**record)
        )
    print("PASS")


if __name__ == "__main__":
    main()
