#!/usr/bin/env python3
"""Finite audit for the atomwise-menu entropy barrier.

The proof in the companion note is asymptotic and independent of this
script.  This checker verifies the exact small identities and gives one
fixed-seed finite diagnostic comparing sourcewise and whole-atom choices.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import exp, prod
from random import Random


def atoms(n: int, block: int) -> list[tuple[int, ...]]:
    assert n % block == 0
    return [tuple(range(i, i + block)) for i in range(0, n, block)]


def exhaustive_avoidance_identity(n: int, block: int) -> int:
    """Enumerate every atom injection and every S,v at one small size."""
    aa = atoms(n, block)
    local = list(permutations(range(n), block))
    maps = []
    for choices in product(local, repeat=len(aa)):
        f = [None] * n
        for atom, image in zip(aa, choices):
            for u, v in zip(atom, image):
                f[u] = v
        maps.append(tuple(f))

    total = len(maps)
    checks = 0
    for mask in range(1 << n):
        source_set = {u for u in range(n) if mask >> u & 1}
        sizes = [len(source_set.intersection(atom)) for atom in aa]
        predicted = prod(
            (Fraction(n - size, n) for size in sizes), start=Fraction(1)
        )
        for target in range(n):
            avoiding = sum(
                all(f[u] != target for u in source_set)
                for f in maps
            )
            actual = Fraction(avoiding, total)
            assert actual == predicted, (n, block, mask, target, actual, predicted)
            checks += 1
    return checks


def integer_partitions(total: int, cap: int, top: int | None = None):
    """Yield nonincreasing positive integer partitions with parts <= cap."""
    if total == 0:
        yield ()
        return
    if top is None:
        top = min(total, cap)
    for first in range(min(total, cap, top), 0, -1):
        for rest in integer_partitions(total - first, cap, first):
            yield (first,) + rest


def audit_group_profile_bound(max_n: int = 30) -> int:
    checks = 0
    lower = exp(-2.0)
    for n in range(4, max_n + 1):
        for block in range(1, n // 2 + 1):
            for total in range(n + 1):
                for profile in integer_partitions(total, block):
                    p0 = prod(1.0 - size / n for size in profile)
                    assert p0 + 1e-14 >= lower, (n, block, profile, p0)
                    checks += 1
    return checks


def audit_overlap_graph_cut(n: int = 12, block: int = 3, seed: int = 17):
    """Verify D(X,Y)=|boundary Z| for every selection in a crossed pair."""
    rng = Random(seed)
    pp = atoms(n, block)
    order = list(range(n))
    rng.shuffle(order)
    qq = [tuple(order[i : i + block]) for i in range(0, n, block)]
    m = len(pp)

    p_of = [None] * n
    q_of = [None] * n
    for i, atom in enumerate(pp):
        for u in atom:
            p_of[u] = i
    for i, atom in enumerate(qq):
        for u in atom:
            q_of[u] = i

    adjacency = [set() for _ in range(2 * m)]
    for u in range(n):
        p = p_of[u]
        q = m + q_of[u]
        adjacency[p].add(q)
        adjacency[q].add(p)

    seen = set()
    components = 0
    for start in range(2 * m):
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

    checks = 0
    zero_defect = 0
    for xmask in range(1 << m):
        for ymask in range(1 << m):
            defect = 0
            boundary = 0
            for u in range(n):
                x = (xmask >> p_of[u]) & 1
                y = (ymask >> q_of[u]) & 1
                defect += x + y != 1
                z_p = x
                z_q = 1 - y
                boundary += z_p != z_q
            assert defect == boundary
            zero_defect += defect == 0
            checks += 1

    assert zero_defect == 2**components, (zero_defect, components)
    return {
        "N": n,
        "B": block,
        "components": components,
        "selection_checks": checks,
        "zero_defect_selections": zero_defect,
    }


def random_menu(n: int, block: int, banks: int, seed: int):
    rng = Random(seed)
    aa = atoms(n, block)
    maps: list[tuple[int, ...]] = []
    for _ in range(banks):
        f = [None] * n
        for atom in aa:
            image = rng.sample(range(n), block)
            assert len(set(image)) == block
            for u, v in zip(atom, image):
                f[u] = v
        maps.append(tuple(f))
    return aa, maps


def hopcroft_karp_size(adjacency: list[list[int]], n_right: int) -> int:
    n_left = len(adjacency)
    left_match = [-1] * n_left
    right_match = [-1] * n_right
    distance = [0] * n_left

    def bfs() -> bool:
        queue = []
        for u in range(n_left):
            if left_match[u] < 0:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = -1
        found = False
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adjacency[u]:
                mate = right_match[v]
                if mate < 0:
                    found = True
                elif distance[mate] < 0:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        return found

    def dfs(u: int) -> bool:
        for v in adjacency[u]:
            mate = right_match[v]
            if mate < 0 or (distance[mate] == distance[u] + 1 and dfs(mate)):
                left_match[u] = v
                right_match[v] = u
                return True
        distance[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if left_match[u] < 0 and dfs(u):
                matching += 1
    return matching


def best_whole_atom_image(aa, maps) -> tuple[int, tuple[int, ...]]:
    banks = len(maps)
    images = [
        [sum(1 << maps[j][u] for u in atom) for j in range(banks)]
        for atom in aa
    ]
    best = -1
    choice_best = ()
    for choice in product(range(banks), repeat=len(aa)):
        image = 0
        for atom_index, bank in enumerate(choice):
            image |= images[atom_index][bank]
        size = image.bit_count()
        if size > best:
            best = size
            choice_best = choice
    return best, choice_best


def finite_gap_diagnostic():
    # Six atoms and six banks give only 6^6 whole-atom assignments, while
    # the sourcewise graph has one bank choice at each of 36 sources.
    n, block, banks = 36, 6, 6
    for seed in range(200):
        aa, maps = random_menu(n, block, banks, seed)
        adjacency = [sorted({maps[j][u] for j in range(banks)}) for u in range(n)]
        sourcewise = hopcroft_karp_size(adjacency, n)
        whole, choice = best_whole_atom_image(aa, maps)
        assert sourcewise >= whole
        if sourcewise - whole >= 2:
            return {
                "N": n,
                "B": block,
                "K": banks,
                "seed": seed,
                "sourcewise_matching": sourcewise,
                "best_whole_atom_image": whole,
                "best_choice": choice,
            }
    raise AssertionError("fixed-seed search did not find the expected finite gap")


def main() -> None:
    exact_checks = exhaustive_avoidance_identity(4, 2)
    profile_checks = audit_group_profile_bound()
    overlap = audit_overlap_graph_cut()
    diagnostic = finite_gap_diagnostic()

    print("PASS atomwise menu entropy barrier audit")
    print(f"exact avoidance checks: {exact_checks}")
    print(f"integer group-profile checks: {profile_checks}")
    print("overlap-graph cut audit:", overlap)
    print("finite diagnostic:", diagnostic)


if __name__ == "__main__":
    main()
