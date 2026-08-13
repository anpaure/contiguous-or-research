#!/usr/bin/env python3
"""Generate corrected slab-atlas atoms and analyze shared-rail pairing.

All substantial runs belong on h100.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter

import verify_product_scd_diagonal_slab_fan_atlas as base

try:
    import networkx as nx
except ImportError:
    nx = None


def oriented_atoms(nrows, ncols, radius, depth, slab_height, swap=False):
    """Return (cost, atoms) for the exact corrected oriented recurrence.

    Atom fields use original grid coordinates.  An arm is the ordered list
    of coordinate-increment labels traversed by the same-length rectangle
    word, with its core position deleted.
    """
    atoms = []
    cost = 0
    x = 0
    while x < nrows:
        height = min(slab_height, nrows - x)
        width = depth + 2 - height
        y = 0
        full_rectangles = 0
        while (
            y + width <= ncols
            and radius - x - y >= height + width - 2
        ):
            atoms.append(make_atom(x, y, height, width, swap, "rectangle"))
            cost += height + width - 1
            y += width
            full_rectangles += 1

        local_radius = radius - x - y
        if local_radius >= 0 and y < ncols:
            if full_rectangles == 0:
                effective_radius = min(
                    radius - x, (nrows - x - 1) + (ncols - 1)
                )
                if effective_radius <= depth:
                    fan_a = min(nrows - x, radius - x + 1)
                    fan_b = min(ncols, radius - x + 1)
                    atoms.append(make_atom(x, 0, fan_a, fan_b, swap, "stop"))
                    cost += fan_a + fan_b - 1
                    break
            fan_a = min(height, local_radius + 1)
            fan_b = min(ncols - y, local_radius + 1)
            atoms.append(make_atom(x, y, fan_a, fan_b, swap, "tail"))
            cost += fan_a + fan_b - 1
        x += height
    return cost, atoms


def make_atom(x, y, a, b, swap, kind):
    # Oriented local row labels X_1,... and column labels Y_1,... .
    arm = [("X", x + i) for i in range(a - 1, 0, -1)]
    arm += [("Y", y + j) for j in range(1, b)]
    if not swap:
        base_xy = (x, y)
        mapped = tuple(arm)
    else:
        base_xy = (y, x)
        mapped = tuple(("Y" if side == "X" else "X", index) for side, index in arm)
    return {
        "base": base_xy,
        "a": a,
        "b": b,
        "arm": mapped,
        "kind": kind,
    }


def optimized_atoms(a, b, radius, depth):
    candidates = []
    for height in range(1, depth + 2):
        candidates.append(oriented_atoms(a, b, radius, depth, height, False))
        candidates.append(oriented_atoms(b, a, radius, depth, height, True))
    return min(candidates, key=lambda item: (item[0], len(item[1])))


def core_rank(atom, u, v):
    x, y = atom["base"]
    return u + v + x + y


def union_core_rank(first, second, u, v):
    x1, y1 = first["base"]
    x2, y2 = second["base"]
    return u + v + max(x1, x2) + max(y1, y2)


def base_differences(first, second):
    x1, y1 = first["base"]
    x2, y2 = second["base"]
    first_minus_second = x1 > x2 or y1 > y2
    second_minus_first = x2 > x1 or y2 > y1
    return first_minus_second, second_minus_first


def arm_core_disjoint(first, second):
    max_x = max(first["base"][0], second["base"][0])
    max_y = max(first["base"][1], second["base"][1])
    for side, index in set(first["arm"]) | set(second["arm"]):
        if (side == "X" and index <= max_x) or (
            side == "Y" and index <= max_y
        ):
            return False
    return True


def path_components(first, second):
    """Return directed-path component lengths, or None if incompatible."""
    vertices = set(first) | set(second)
    successor = {}
    predecessor = {}
    for sequence in (first, second):
        for left, right in zip(sequence, sequence[1:]):
            if left in successor and successor[left] != right:
                return None
            if right in predecessor and predecessor[right] != left:
                return None
            successor[left] = right
            predecessor[right] = left

    starts = [vertex for vertex in vertices if vertex not in predecessor]
    seen = set()
    lengths = []
    for start in starts:
        length = 0
        vertex = start
        while vertex not in seen:
            seen.add(vertex)
            length += 1
            if vertex not in successor:
                break
            vertex = successor[vertex]
        lengths.append(length)

    if len(seen) != len(vertices):
        # A directed cycle is compatible only when it is the complete final
        # cycle; guards or any other component cannot be inserted.
        cycle_vertices = vertices - seen
        vertex = next(iter(cycle_vertices))
        cycle = set()
        while vertex not in cycle:
            cycle.add(vertex)
            if vertex not in successor:
                return None
            vertex = successor[vertex]
        if cycle != vertices:
            return None
        return ("cycle", [len(vertices)])
    return ("paths", lengths)


def can_pack_components(lengths, bins, capacity):
    if not lengths:
        return True
    if bins <= 0 or max(lengths) > capacity:
        return False
    lengths = sorted(lengths, reverse=True)
    loads = [0] * bins

    def visit(index):
        if index == len(lengths):
            return True
        value = lengths[index]
        tried = set()
        for slot in range(bins):
            if loads[slot] in tried or loads[slot] + value > capacity:
                continue
            tried.add(loads[slot])
            loads[slot] += value
            if visit(index + 1):
                return True
            loads[slot] -= value
        return False

    return visit(0)


def cyclic_embedding(first, second, n, require_union_avoidance=False):
    """Whether two arms embed as arcs of one N-cycle.

    If require_union_avoidance, the complement must hit every cyclic
    (q-1)-interval, where q=N-2.
    """
    if len(set(first) | set(second)) > n:
        return False
    q = n - 2
    for left in (tuple(first), tuple(reversed(first))):
        for right in (tuple(second), tuple(reversed(second))):
            result = path_components(left, right)
            if result is None:
                continue
            kind, lengths = result
            union_size = len(set(left) | set(right))
            guards = n - union_size
            if kind == "cycle":
                if guards == 0 and not require_union_avoidance:
                    return True
                continue
            if not require_union_avoidance:
                return True
            if can_pack_components(lengths, guards, q - 2):
                return True
    return False


def pair_compatible(first, second, u, v, radius, q, level):
    n = q + 2
    if len(first["arm"]) > q - 1 or len(second["arm"]) > q - 1:
        return False
    if not cyclic_embedding(first["arm"], second["arm"], n, False):
        return False
    if level == "cyclic":
        return True

    union_rank = union_core_rank(first, second, u, v)
    core_size = u + v + radius
    if union_rank > core_size:
        return False
    if level == "core_le":
        return True
    if level == "core_eq":
        return union_rank == core_size

    if not arm_core_disjoint(first, second):
        return False
    if level == "core_le_disjoint":
        return True
    if level == "core_eq_disjoint":
        return union_rank == core_size
    first_minus_second, second_minus_first = base_differences(first, second)
    if first_minus_second and len(second["arm"]) >= q - 1:
        return False
    if second_minus_first and len(first["arm"]) >= q - 1:
        return False

    filler = core_size - union_rank
    if filler:
        if core_size + len(set(first["arm"]) | set(second["arm"])) > 2 * (
            core_size + q
        ) - 1:
            return False
        if not cyclic_embedding(first["arm"], second["arm"], n, True):
            return False
    return True


def singleton_exact_feasible(atom, u, v, radius, q):
    length = len(atom["arm"])
    if length > q - 1:
        return False
    core_size = u + v + radius
    filler = core_size - core_rank(atom, u, v)
    return filler == 0 or length <= q - 2


def graph_matching(atoms, u, v, radius, q, level, mandatory=False):
    if nx is None:
        raise RuntimeError("networkx is required for matching census")
    graph = nx.Graph()
    graph.add_nodes_from(range(len(atoms)))
    required = {
        index
        for index, atom in enumerate(atoms)
        if not singleton_exact_feasible(atom, u, v, radius, q)
    }
    big = len(atoms) + 1
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            if pair_compatible(atoms[i], atoms[j], u, v, radius, q, level):
                weight = 1
                if mandatory:
                    weight += big * ((i in required) + (j in required))
                graph.add_edge(i, j, weight=weight)
    matching = nx.max_weight_matching(
        graph, maxcardinality=not mandatory, weight="weight"
    )
    covered = {vertex for edge in matching for vertex in edge}
    feasible = not mandatory or required <= covered
    return len(matching), feasible, len(required), graph.number_of_edges()


def pairing_census(k):
    R, width, d = base.parameters(k)
    q = d + 1
    n = q + 2
    h = k // 2
    totals = Counter()
    infeasible_weight = 0
    max_grid_atoms = 0
    for u, (a, ca) in enumerate(base.chain_types(h)):
        for v, (b, cb) in enumerate(base.chain_types(k - h)):
            radius = R - q - u - v
            if radius < 0:
                continue
            _, atoms_all = optimized_atoms(a, b, radius, d)
            mult = ca * cb
            long_count = sum(len(atom["arm"]) > q - 1 for atom in atoms_all)
            atoms = [atom for atom in atoms_all if len(atom["arm"]) <= q - 1]
            max_grid_atoms = max(max_grid_atoms, len(atoms))
            totals["atoms"] += mult * len(atoms_all)
            totals["long"] += mult * long_count
            totals["short"] += mult * len(atoms)
            for level in (
                "cyclic",
                "core_le",
                "core_eq",
                "core_le_disjoint",
                "core_eq_disjoint",
            ):
                matching, _, _, edges = graph_matching(
                    atoms, u, v, radius, q, level, False
                )
                totals[f"match_{level}"] += mult * matching
                totals[f"edges_{level}"] += mult * edges
            matching, feasible, required, edges = graph_matching(
                atoms, u, v, radius, q, "exact", True
            )
            totals["match_exact"] += mult * matching
            totals["required"] += mult * required
            totals["edges_exact"] += mult * edges
            if not feasible:
                infeasible_weight += mult

    print(
        f"PAIR k={k} q={q} N={n} max-grid-atoms={max_grid_atoms} "
        f"atoms/W={totals['atoms']/width:.12f} "
        f"long-invalid/W={totals['long']/width:.12f} "
        f"infeasible-gridcopies/W={infeasible_weight/width:.12f}",
        flush=True,
    )
    for level in (
        "cyclic",
        "core_le",
        "core_eq",
        "core_le_disjoint",
        "core_eq_disjoint",
        "exact",
    ):
        matches = totals[f"match_{level}"]
        packets = totals["short"] - matches
        print(
            f"  {level}: matching/W={matches/width:.12f} "
            f"conditional-short-packet-charge/W={n*packets/width:.12f} "
            f"edge-incidence-weight/W={totals[f'edges_{level}']/width:.12f}",
            flush=True,
        )
    print(
        f"  exact-mandatory-vertices/W={totals['required']/width:.12f}",
        flush=True,
    )


def basic_census(k):
    R, width, d = base.parameters(k)
    q = d + 1
    n = q + 2
    h = k // 2
    total_atoms = 0
    long_atoms = 0
    arm_hist = Counter()
    kind_hist = Counter()
    max_arm = 0
    for u, (a, ca) in enumerate(base.chain_types(h)):
        for v, (b, cb) in enumerate(base.chain_types(k - h)):
            radius = R - q - u - v
            if radius < 0:
                continue
            _, atoms = optimized_atoms(a, b, radius, d)
            mult = ca * cb
            total_atoms += mult * len(atoms)
            for atom in atoms:
                length = len(atom["arm"])
                max_arm = max(max_arm, length)
                arm_hist[length] += mult
                kind_hist[(atom["kind"], length)] += mult
                if length > q - 1:
                    long_atoms += mult
    print(
        f"k={k} q={q} N={n} atoms/W={total_atoms/width:.12f} "
        f"long-atoms/W={long_atoms/width:.12f} max-arm={max_arm} "
        f"unpaired-charge/W={n*total_atoms/width:.12f}",
        flush=True,
    )
    print(
        "  arm-hist/W",
        [(length, count / width) for length, count in sorted(arm_hist.items())],
        flush=True,
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    ap.add_argument("--pair", action="store_true")
    args = ap.parse_args()
    for k in args.k:
        if args.pair:
            pairing_census(k)
        else:
            basic_census(k)
