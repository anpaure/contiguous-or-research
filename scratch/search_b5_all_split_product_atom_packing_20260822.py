#!/usr/bin/env python3
"""Heuristic packing search for the b=5 all-split product-atom hypergraph.

This is evidence only, not part of any proof.  By transitivity we fix one
canonical atom and use randomized depth-first search for nine further
disjoint atoms, which would cover 250 of the 252 middle vertices.
"""

from argparse import ArgumentParser
from itertools import combinations, permutations
from random import Random
from time import monotonic


B = 5
OMEGA = tuple(range(2 * B))
VERTICES = list(combinations(OMEGA, B))
VID = {s: i for i, s in enumerate(VERTICES)}
FULL_VERTEX_MASK = (1 << len(VERTICES)) - 1


def undirected_cycles(points: tuple[int, ...]) -> list[tuple[int, ...]]:
    first = min(points)
    rest = tuple(x for x in points if x != first)
    out = []
    for tail in permutations(rest):
        cycle = (first,) + tail
        if cycle[1] < cycle[-1]:
            out.append(cycle)
    return out


def cycle_edges(cycle: tuple[int, ...]) -> list[frozenset[int]]:
    return [
        frozenset((cycle[i], cycle[(i + 1) % B])) for i in range(B)
    ]


def atom_mask(
    a_cycle: tuple[int, ...], b_cycle: tuple[int, ...]
) -> int:
    b_set = frozenset(b_cycle)
    mask = 0
    for x in cycle_edges(a_cycle):
        for omitted in cycle_edges(b_cycle):
            target = tuple(sorted(x | (b_set - omitted)))
            mask |= 1 << VID[target]
    assert mask.bit_count() == B * B
    return mask


def all_atoms() -> list[int]:
    masks: set[int] = set()
    for a_tuple in combinations(OMEGA, B):
        a_set = frozenset(a_tuple)
        b_tuple = tuple(x for x in OMEGA if x not in a_set)
        a_cycles = undirected_cycles(a_tuple)
        b_cycles = undirected_cycles(b_tuple)
        for ca in a_cycles:
            for cb in b_cycles:
                masks.add(atom_mask(ca, cb))
    return sorted(masks)


def randomized_search(atoms: list[int], seconds: float = 45.0) -> list[int]:
    rng = Random(20260822)
    fixed = atoms[0]
    compatible = [x for x in atoms if not (x & fixed)]
    best = [fixed]
    deadline = monotonic() + seconds

    # Randomized DFS.  At each node sample candidates and prefer a candidate
    # leaving many future compatible choices.
    def descend(chosen: list[int], used: int, pool: list[int]) -> bool:
        nonlocal best
        if len(chosen) > len(best):
            best = chosen.copy()
            print(
                f"new_best={len(best)} covered={used.bit_count()} "
                f"remaining={len(VERTICES)-used.bit_count()}"
            )
        if len(chosen) == 10:
            return True
        if monotonic() >= deadline:
            return False
        need = 10 - len(chosen)
        if len(pool) < need:
            return False

        sample = rng.sample(pool, min(48, len(pool)))
        scored = []
        probe = rng.sample(pool, min(384, len(pool)))
        for edge in sample:
            score = sum(1 for other in probe if not (edge & other))
            scored.append((score, rng.random(), edge))
        scored.sort(reverse=True)
        for _, _, edge in scored[:18]:
            new_pool = [x for x in pool if x > edge and not (x & edge)]
            if descend(chosen + [edge], used | edge, new_pool):
                return True
        return False

    while monotonic() < deadline:
        pool = compatible.copy()
        rng.shuffle(pool)
        # The integer ordering restriction in descend removes permutation
        # duplicates; sorting restores that canonical branch order.
        pool.sort()
        if descend([fixed], fixed, pool):
            return best
    return best


def milp_search(
    atoms: list[int], seconds: float, relax: bool = False
) -> list[int]:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import csc_matrix

    rows: list[int] = []
    cols: list[int] = []
    for j, edge in enumerate(atoms):
        bits = edge
        while bits:
            low = bits & -bits
            rows.append(low.bit_length() - 1)
            cols.append(j)
            bits ^= low
    matrix = csc_matrix(
        (np.ones(len(rows)), (rows, cols)),
        shape=(len(VERTICES), len(atoms)),
    )
    # Atom transitivity permits fixing the first atom.
    lower = np.zeros(len(atoms))
    upper = np.ones(len(atoms))
    lower[0] = 1.0
    result = milp(
        c=-np.ones(len(atoms)),
        integrality=np.zeros(len(atoms)) if relax else np.ones(len(atoms)),
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(matrix, -np.inf, 1.0),
        options={"time_limit": seconds, "mip_rel_gap": 0.0},
    )
    print(
        f"milp_status={result.status} success={result.success} "
        f"message={result.message!r} objective={None if result.fun is None else -result.fun}"
    )
    if result.x is None:
        return []
    return [atoms[j] for j, value in enumerate(result.x) if value > 0.5]


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--milp", action="store_true")
    parser.add_argument("--seconds", type=float, default=45.0)
    parser.add_argument("--relax", action="store_true")
    args = parser.parse_args()
    atoms = all_atoms()
    print(f"vertices={len(VERTICES)} distinct_atoms={len(atoms)}")
    assert all(x.bit_count() == B * B for x in atoms)
    packing = (
        milp_search(atoms, args.seconds, args.relax)
        if args.milp
        else randomized_search(atoms, args.seconds)
    )
    used = 0
    for edge in packing:
        assert not (used & edge)
        used |= edge
    print(
        f"B5_ALL_SPLIT_PACKING_RESULT size={len(packing)} "
        f"covered={used.bit_count()} holes={len(VERTICES)-used.bit_count()}"
    )
    if len(packing) == 10:
        print("B5_250_OF_252_CERTIFICATE_FOUND")


if __name__ == "__main__":
    main()
