#!/usr/bin/env python3
"""Decompose the optimal b=9 shadow repair into universal C8 row switches."""

from __future__ import annotations

import argparse
import heapq
import multiprocessing
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations


REMOVED = [
    (1, 3, 4, 2, 9, 7, 5, 6, 8),
    (1, 4, 3, 7, 2, 6, 5, 8, 9),
    (1, 4, 5, 3, 2, 8, 6, 7, 9),
    (1, 5, 3, 2, 9, 7, 6, 4, 8),
    (1, 6, 4, 3, 2, 8, 7, 5, 9),
]

ADDED = [
    (1, 3, 5, 2, 9, 7, 4, 6, 8),
    (1, 4, 3, 2, 5, 8, 6, 9, 7),
    (1, 4, 3, 8, 2, 6, 7, 9, 5),
    (1, 4, 9, 3, 2, 7, 6, 5, 8),
    (1, 6, 4, 3, 2, 7, 8, 5, 9),
]


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    h = 0
    close = None
    for i, bit in enumerate(word):
        h += 1 if bit == "1" else -1
        if h == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_row(word: str):
    m = len(word) // 2
    b = 2 * m + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def forms(order):
    order = tuple(order)
    b = len(order)
    for base in (order, tuple(reversed(order))):
        for shift in range(b):
            yield base[shift:] + base[:shift]


def switches(row1, row2, r=4):
    answers = set()
    for left, right in ((row1, row2), (row2, row1)):
        right_forms = set(forms(right))
        for R1 in forms(left):
            a, b = R1[:2]
            P = R1[2 : r + 1]
            c, d = R1[r + 1 : r + 3]
            Q = R1[r + 3 :]
            R2 = (c, a) + P + (d, b) + Q
            if R2 not in right_forms:
                continue
            A1 = canonical((a, c) + P + (b, d) + Q)
            A2 = canonical((b, a) + P + (d, c) + Q)
            answer = tuple(sorted((A1, A2)))
            if answer != tuple(sorted((row1, row2))):
                answers.add(answer)
    return answers


@lru_cache(maxsize=None)
def cached_switches(row1, row2):
    if row2 < row1:
        row1, row2 = row2, row1
    return tuple(switches(row1, row2))


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def neighbours(state):
    state = tuple(state)
    for i, j in combinations(range(len(state)), 2):
        for new_pair in cached_switches(state[i], state[j]):
            assert tuple(sorted((state[i], state[j]))) in cached_switches(*new_pair)
            new_state = tuple(sorted(new_pair + tuple(state[k] for k in range(len(state)) if k not in (i, j))))
            if len(set(new_state)) == len(state):
                yield new_state, (state[i], state[j], new_pair)


def repeated_incidence_is_pseudoforest(rows):
    rows = tuple(rows)
    target_rows = {}
    for i, row in enumerate(rows):
        for target in windows(row, 3):
            target_rows.setdefault(target, []).append(i)
    repeated = [(target, owners) for target, owners in target_rows.items() if len(owners) >= 2]
    parent = list(range(len(rows) + len(repeated)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    edge_count = Counter()
    vertices = set(range(len(rows)))
    for j, (_, owners) in enumerate(repeated):
        target_vertex = len(rows) + j
        vertices.add(target_vertex)
        for owner in owners:
            union(owner, target_vertex)
    vertex_count = Counter(find(v) for v in vertices)
    for j, (_, owners) in enumerate(repeated):
        target_vertex = len(rows) + j
        for owner in owners:
            edge_count[find(target_vertex)] += 1
    return all(edge_count[root] <= vertex_count[root] for root in edge_count)


def maximum_pseudoforest_subfamily(factor):
    factor = tuple(sorted(factor))
    for size in range(len(factor), -1, -1):
        for indices in combinations(range(len(factor)), size):
            rows = tuple(factor[i] for i in indices)
            if repeated_incidence_is_pseudoforest(rows):
                return rows
    raise AssertionError


def maximum_pseudoforest_size(factor):
    return len(maximum_pseudoforest_subfamily(factor))


def main(max_states, full, all_pf):
    canonical_factor = {msw_row(w) for w in dyck_words(4)}
    start = tuple(sorted(canonical(x) for x in REMOVED))
    goal = tuple(sorted(canonical(x) for x in ADDED))
    assert set(start) <= canonical_factor
    fixed = canonical_factor - set(start)
    assert len(fixed) == 9

    marked_pairs = []
    for outer in dyck_words(2):
        for gap in range(len(outer) + 1):
            marked_pairs.append(
                frozenset(
                    (
                        msw_row(outer[:gap] + "1100" + outer[gap:]),
                        msw_row(outer[:gap] + "1010" + outer[gap:]),
                    )
                )
            )

    def energy(state):
        factor = set(state) if full else fixed | set(state)
        shadow = Counter(x for row in factor for x in windows(row, 3))
        rank2 = Counter(x for row in factor for x in windows(row, 2))
        holes = 84 - len(shadow)
        e2 = sum(v * (v - 1) // 2 for v in shadow.values())
        untouched_marked = sum(pair <= factor for pair in marked_pairs)
        return {
            "holes": holes,
            "pair_energy": e2,
            "max_mult": max(shadow.values()),
            "rank2_holes": 36 - len(rank2),
            "untouched_marked_pairs": untouched_marked,
            "canonical_rows": len(factor & canonical_factor),
        }

    if full:
        start = tuple(sorted(canonical_factor))
        goal = tuple(sorted(fixed | set(goal)))

    queue = deque([start])
    parent = {start: None}
    move_to = {}
    found = None
    zero = None
    best_state = start
    best_key = (energy(start)["holes"], energy(start)["pair_energy"], 0)
    depth = {start: 0}
    layer_hist = Counter()
    heap = []
    serial = 0
    if full:
        e = energy(start)
        heapq.heappush(heap, ((e["holes"], e["pair_energy"], 0), serial, start))
    while (heap if full else queue) and len(parent) < max_states:
        if full:
            _, _, state = heapq.heappop(heap)
        else:
            state = queue.popleft()
        layer_hist[(depth[state], energy(state)["holes"])] += 1
        state_key = (energy(state)["holes"], energy(state)["pair_energy"], depth[state])
        if state_key < best_key:
            best_key = state_key
            best_state = state
        if state == goal:
            found = state
            break
        if zero is None and energy(state)["holes"] == 0:
            zero = state
        for nxt, move in neighbours(state):
            if nxt in parent:
                continue
            parent[nxt] = state
            move_to[nxt] = move
            depth[nxt] = depth[state] + 1
            if full:
                serial += 1
                e = energy(nxt)
                heapq.heappush(
                    heap,
                    ((e["holes"], e["pair_energy"], depth[nxt]), serial, nxt),
                )
            else:
                queue.append(nxt)
    endpoint = found or zero or best_state
    print(
        {
            "states": len(parent),
            "queue": len(heap) if full else len(queue),
            "found_exact_goal": found is not None,
            "found_zero": zero is not None or (found is not None and energy(found)["holes"] == 0),
            "best": best_key,
            "layer_hole_hist": sorted(layer_hist.items()),
        },
        flush=True,
    )
    path = []
    at = endpoint
    while at != start:
        path.append((at, move_to[at]))
        at = parent[at]
    path.reverse()
    states = [start] + [x for x, _ in path]
    print("path_length", len(path))
    for t, state in enumerate(states):
        print("STATE", t, energy(state))
        if t:
            old_pair, new_pair = path[t - 1][1][:2], path[t - 1][1][2]
            # move_to stores (old1,old2,newpair); print literal transition.
            old1, old2, new_pair = path[t - 1][1]
            print(" MOVE_REMOVE", " | ".join(" ".join(map(str, z)) for z in (old1, old2)))
            print(" MOVE_ADD", " | ".join(" ".join(map(str, z)) for z in new_pair))
    print("goal_equal", endpoint == goal)

    if full:
        energy_cache = {state: energy(state) for state in parent}
        worst = None
        violations = 0
        A = 126
        r = 4
        for state, e in energy_cache.items():
            total_drift = 0
            move_count = 0
            for nxt, _ in neighbours(state):
                total_drift += energy(nxt)["pair_energy"] - e["pair_energy"]
                move_count += 1
            lhs_scaled = r * (total_drift + (e["pair_energy"] - 42)) - A
            item = (lhs_scaled, total_drift, e["pair_energy"] - 42, move_count, state)
            if worst is None or item[:4] > worst[:4]:
                worst = item
            violations += lhs_scaled > 0
        assert worst is not None
        print(
            "drift_gap_test",
            {
                "tested": len(energy_cache),
                "violations_of_total_drift_le_A_over_r_minus_gap": violations,
                "worst_scaled_excess": worst[0],
                "worst_total_drift": worst[1],
                "worst_gap": worst[2],
                "worst_moves": worst[3],
            },
        )
        for label, factor_state in (("canonical", start), ("best_c8", best_state), ("zero_5row", goal)):
            subfamily = maximum_pseudoforest_subfamily(factor_state)
            print(
                "pseudoforest_subfamily",
                {"label": label, "factor_rows": len(factor_state), "maximum_rows": len(subfamily)},
            )
        low_energy_pf = []
        for factor_state, e in energy_cache.items():
            if e["pair_energy"] != 43:
                continue
            subfamily = maximum_pseudoforest_subfamily(factor_state)
            low_energy_pf.append((len(subfamily), e["holes"], factor_state, subfamily))
        assert low_energy_pf
        pf_hist = Counter((size, holes) for size, holes, _, _ in low_energy_pf)
        pf_best = max(low_energy_pf, key=lambda item: (item[0], -item[1]))
        print(
            "low_energy_pseudoforest_profile",
            {
                "states": len(low_energy_pf),
                "size_hole_hist": sorted(pf_hist.items()),
                "maximum_rows": pf_best[0],
                "holes": pf_best[1],
            },
        )
        print("LOW_ENERGY_PF_FACTOR")
        for row in pf_best[2]:
            print(" ", " ".join(map(str, row)), "SELECTED" if row in pf_best[3] else "OMITTED")
        if all_pf:
            process_count = min(64, multiprocessing.cpu_count(), len(parent))
            with multiprocessing.Pool(process_count) as pool:
                all_pf_sizes = pool.map(maximum_pseudoforest_size, parent, chunksize=4)
            profile = Counter(
                (all_pf_sizes[i], energy_cache[state]["holes"], energy_cache[state]["pair_energy"])
                for i, state in enumerate(parent)
            )
            print(
                "whole_component_pseudoforest_profile",
                {
                    "states": len(parent),
                    "maximum_rows": max(all_pf_sizes),
                    "size_hist": sorted(Counter(all_pf_sizes).items()),
                    "size_hole_energy_hist": sorted(profile.items()),
                },
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-states", type=int, default=2_000_000)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--all-pf", action="store_true")
    args = parser.parse_args()
    main(args.max_states, args.full, args.all_pf)
