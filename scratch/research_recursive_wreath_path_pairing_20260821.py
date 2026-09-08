#!/usr/bin/env python3
"""Research diagnostic for recursively pairing partial odd-graph wreath paths.

Run only on H100.  A path is admissible exactly when its consecutive Kneser
edges have distinct hole colours.  Starting from singleton target blocks, we
repeatedly form a maximum matching in the compatibility graph and concatenate
matched blocks.  When the block length reaches r, we test the stronger closure
relation that two blocks plus one dirty target form a full (2r+1)-wreath.

This is diagnostic code, not a theorem or production constructor.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from math import comb
import random

import networkx as nx


def rank_masks(b: int, r: int) -> list[int]:
    return [sum(1 << x for x in S) for S in combinations(range(b), r)]


@dataclass(frozen=True)
class Block:
    path: tuple[int, ...]
    holes: frozenset[int]


def edge_hole(x: int, y: int, full: int) -> int | None:
    if x & y:
        return None
    z = full ^ (x | y)
    if not z or z & (z - 1):
        return None
    return z.bit_length() - 1


def concat_options(a: Block, b: Block, full: int) -> list[Block]:
    if a.holes & b.holes:
        return []
    ans: dict[tuple[int, ...], Block] = {}
    for pa in (a.path, a.path[::-1]):
        for pb in (b.path, b.path[::-1]):
            h = edge_hole(pa[-1], pb[0], full)
            if h is None or h in a.holes or h in b.holes:
                continue
            path = pa + pb
            block = Block(path, a.holes | b.holes | {h})
            ans[path] = block
    return list(ans.values())


def closing_options(a: Block, b: Block, full: int, r: int):
    """Return (clean path, dirty target) completions to a full wreath."""
    out = []
    for joined in concat_options(a, b, full):
        if len(joined.path) != 2 * r:
            continue
        first, last = joined.path[0], joined.path[-1]
        union = first | last
        if union.bit_count() != r + 1:
            continue
        dirty = full ^ union
        if dirty.bit_count() != r or dirty in joined.path:
            continue
        h1 = edge_hole(last, dirty, full)
        h2 = edge_hole(dirty, first, full)
        if h1 is None or h2 is None or h1 == h2:
            continue
        if h1 in joined.holes or h2 in joined.holes:
            continue
        holes = set(joined.holes) | {h1, h2}
        if len(holes) != 2 * r + 1:
            continue
        out.append((joined.path, dirty))
    return out


def compatibility_graph(blocks: list[Block], full: int, close: bool, r: int):
    owner: dict[int, int] = {}
    for i, block in enumerate(blocks):
        for x in block.path:
            owner[x] = i
    graph = nx.Graph()
    graph.add_nodes_from(range(len(blocks)))
    options: dict[tuple[int, int], list] = {}
    # Generate candidate block pairs from endpoint Kneser neighbours.
    endpoints: dict[int, list[tuple[int, int]]] = {}
    for i, block in enumerate(blocks):
        for side, x in enumerate((block.path[0], block.path[-1])):
            endpoints.setdefault(x, []).append((i, side))
    for i, a in enumerate(blocks):
        candidates = set()
        for x in (a.path[0], a.path[-1]):
            complement = full ^ x
            bits = complement
            while bits:
                bit = bits & -bits
                bits -= bit
                y = complement ^ bit
                j = owner.get(y)
                if j is not None and j != i:
                    candidates.add(j)
        for j in candidates:
            if i >= j:
                continue
            opts = (
                closing_options(a, blocks[j], full, r)
                if close
                else concat_options(a, blocks[j], full)
            )
            if opts:
                options[(i, j)] = opts
                graph.add_edge(i, j)
    return graph, options


def choose_matching(graph: nx.Graph, rng: random.Random):
    if graph.number_of_nodes() > 3000:
        edges = list(graph.edges)
        rng.shuffle(edges)
        used = set()
        chosen = set()
        for u, v in edges:
            if u not in used and v not in used:
                used.add(u)
                used.add(v)
                chosen.add((u, v))
        return chosen
    # Tiny independent jitter gives varied maximum-cardinality matchings.
    for u, v in graph.edges:
        graph[u][v]["weight"] = 1.0 + rng.random() * 1e-6
    return nx.algorithms.matching.max_weight_matching(
        graph, maxcardinality=True, weight="weight"
    )


def one_trial(b: int, seed: int):
    assert b % 2 == 1
    r = (b - 1) // 2
    full = (1 << b) - 1
    rng = random.Random(seed)
    blocks = [Block((x,), frozenset()) for x in rank_masks(b, r)]
    original = len(blocks)
    print("START", b, seed, "TARGETS", original, flush=True)
    while len(blocks[0].path) * 2 <= r:
        length = len(blocks[0].path)
        graph, options = compatibility_graph(blocks, full, False, r)
        matching = choose_matching(graph, rng)
        next_blocks = []
        for i, j in matching:
            key = (min(i, j), max(i, j))
            next_blocks.append(rng.choice(options[key]))
        covered = sum(len(x.path) for x in next_blocks)
        deg = [d for _, d in graph.degree]
        print(
            "PAIR",
            length,
            "BLOCKS",
            len(blocks),
            "EDGES",
            graph.number_of_edges(),
            "DEG_MIN_MEAN_MAX",
            (min(deg, default=0), sum(deg) / len(deg) if deg else 0, max(deg, default=0)),
            "MATCH",
            len(matching),
            "TARGET_COVER",
            covered,
            "TARGET_FRAC",
            covered / original,
            flush=True,
        )
        blocks = next_blocks
        if not blocks:
            return
    if blocks and len(blocks[0].path) == r:
        graph, options = compatibility_graph(blocks, full, True, r)
        matching = choose_matching(graph, rng)
        clean = 2 * r * len(matching)
        deg = [d for _, d in graph.degree]
        print(
            "CLOSE",
            "BLOCKS",
            len(blocks),
            "EDGES",
            graph.number_of_edges(),
            "DEG_MIN_MEAN_MAX",
            (min(deg, default=0), sum(deg) / len(deg) if deg else 0, max(deg, default=0)),
            "WREATHS",
            len(matching),
            "CLEAN_COVER",
            clean,
            "CLEAN_FRAC",
            clean / original,
            flush=True,
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, default=17)
    parser.add_argument("--seeds", type=int, default=3)
    args = parser.parse_args()
    for seed in range(args.seeds):
        one_trial(args.b, seed)


if __name__ == "__main__":
    main()
