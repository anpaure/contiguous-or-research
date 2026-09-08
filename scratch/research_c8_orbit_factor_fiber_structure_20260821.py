#!/usr/bin/env python3
"""Research-only structural census of the universal-C8 factor orbit.

Run on H100.  This is diagnostic: no theorem depends on the output.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from itertools import combinations

from search_b9_c8_switch_path_20260821 import (
    canonical,
    dyck_words,
    msw_row,
    switches,
)


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def enumerate_orbit(r):
    start = tuple(sorted(msw_row(w) for w in dyck_words(r)))
    queue = deque([start])
    states = {start}
    relations = set()
    while queue:
        state = queue.popleft()
        for i, j in combinations(range(len(state)), 2):
            old = tuple(sorted((state[i], state[j])))
            for new_pair in switches(state[i], state[j], r):
                new = tuple(sorted(new_pair))
                relations.add(tuple(sorted((old, new))))
                nxt = tuple(
                    sorted(
                        new
                        + tuple(
                            state[t]
                            for t in range(len(state))
                            if t not in (i, j)
                        )
                    )
                )
                if nxt not in states:
                    states.add(nxt)
                    queue.append(nxt)
    return start, states, relations


def exact_cover_count(rows, targets, row_targets, known_states, limit=None, collect=False):
    by_target = defaultdict(list)
    for i, support in enumerate(row_targets):
        for target in support:
            by_target[target].append(i)

    target_set = frozenset(targets)
    memo = {}
    covers = []

    def rec(uncovered, available):
        if not uncovered:
            if collect:
                # Collection is handled by the separate non-memoized walk below.
                pass
            return 1
        key = (uncovered, available)
        if key in memo:
            return memo[key]
        target = min(
            uncovered,
            key=lambda x: sum(
                1 for i in by_target[x] if (available >> i) & 1
            ),
        )
        candidates = [i for i in by_target[target] if (available >> i) & 1]
        total = 0
        for i in candidates:
            support = row_targets[i]
            if not support <= uncovered:
                continue
            conflict_mask = 0
            for t in support:
                for j in by_target[t]:
                    conflict_mask |= 1 << j
            total += rec(uncovered - support, available & ~conflict_mask)
            if limit is not None and total > limit:
                break
        memo[key] = total
        return total

    count = rec(target_set, (1 << len(rows)) - 1)

    if collect:
        def enumerate_rec(uncovered, available, chosen):
            if not uncovered:
                covers.append(tuple(sorted(chosen)))
                return
            target = min(
                uncovered,
                key=lambda x: sum(
                    1 for i in by_target[x] if (available >> i) & 1
                ),
            )
            for i in by_target[target]:
                if not ((available >> i) & 1):
                    continue
                support = row_targets[i]
                if not support <= uncovered:
                    continue
                conflict_mask = 0
                for t in support:
                    for j in by_target[t]:
                        conflict_mask |= 1 << j
                enumerate_rec(
                    uncovered - support,
                    available & ~conflict_mask,
                    chosen + (i,),
                )

        enumerate_rec(target_set, (1 << len(rows)) - 1, ())
        covers = sorted(set(covers))
        assert len(covers) == count
    return count, len(memo), covers


def run(r, count_covers):
    b = 2 * r + 1
    start, states, relations = enumerate_orbit(r)
    rows = tuple(sorted({row for state in states for row in state}))
    row_id = {row: i for i, row in enumerate(rows)}
    frequencies = Counter(row for state in states for row in state)
    middle_targets = tuple(
        sorted(
            {target for row in rows for target in windows(row, r)},
            key=lambda x: tuple(sorted(x)),
        )
    )
    row_targets = tuple(frozenset(windows(row, r)) for row in rows)
    target_degrees = Counter(
        target for support in row_targets for target in support
    )

    row_graph = {i: set() for i in range(len(rows))}
    relation_degrees = Counter()
    for side0, side1 in relations:
        ids0 = tuple(row_id[x] for x in side0)
        ids1 = tuple(row_id[x] for x in side1)
        for x in ids0:
            row_graph[x].update(ids1)
        for x in ids1:
            row_graph[x].update(ids0)
        relation_degrees.update(ids0 + ids1)

    seen = set()
    component_sizes = []
    for i in range(len(rows)):
        if i in seen:
            continue
        stack = [i]
        seen.add(i)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in row_graph[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        component_sizes.append(len(comp))

    state_row_count = Counter()
    for state in states:
        state_row_count.update(row_id[row] for row in state)

    result = {
        "r": r,
        "b": b,
        "states": len(states),
        "factor_rows": len(start),
        "row_universe": len(rows),
        "trade_relations": len(relations),
        "middle_targets": len(middle_targets),
        "target_degree_hist": sorted(Counter(target_degrees.values()).items()),
        "row_frequency_hist": sorted(Counter(frequencies.values()).items()),
        "relation_degree_hist": sorted(Counter(relation_degrees.values()).items()),
        "row_trade_component_sizes": sorted(component_sizes),
        "canonical_rows_in_universe": all(row in row_id for row in start),
    }
    print(result, flush=True)

    if count_covers:
        collect = r <= 4
        count, memo_states, covers = exact_cover_count(
            rows,
            middle_targets,
            row_targets,
            states,
            limit=max(len(states) + 1, 10_000_000),
            collect=collect,
        )
        if covers:
            relation_index = []
            for side0, side1 in relations:
                relation_index.append(
                    (
                        frozenset(row_id[x] for x in side0),
                        frozenset(row_id[x] for x in side1),
                    )
                )
            cover_set = set(covers)
            adjacency = {cover: [] for cover in covers}
            for cover in covers:
                selected = frozenset(cover)
                for side0, side1 in relation_index:
                    for old, new in ((side0, side1), (side1, side0)):
                        if old <= selected and not (new & selected):
                            nxt = tuple(sorted((selected - old) | new))
                            if nxt in cover_set:
                                adjacency[cover].append(nxt)
            components = []
            remaining = set(covers)
            while remaining:
                root = next(iter(remaining))
                stack = [root]
                remaining.remove(root)
                component = []
                while stack:
                    current = stack.pop()
                    component.append(current)
                    for nxt in adjacency[current]:
                        if nxt in remaining:
                            remaining.remove(nxt)
                            stack.append(nxt)
                components.append(component)

            lower_targets = tuple(
                sorted(
                    {
                        target
                        for row in rows
                        for target in windows(row, r - 1)
                    },
                    key=lambda x: tuple(sorted(x)),
                )
            )
            lower_decks = tuple(windows(row, r - 1) for row in rows)

            def profile(cover):
                loads = Counter(
                    target for i in cover for target in lower_decks[i]
                )
                holes = sum(1 for target in lower_targets if loads[target] == 0)
                energy = sum(v * (v - 1) // 2 for v in loads.values())
                return holes, energy

            component_profile = []
            for component in components:
                profiles = [profile(cover) for cover in component]
                component_profile.append(
                    (
                        len(component),
                        min(profiles),
                        max(profiles),
                        sum(1 for value in profiles if value[0] == 0),
                    )
                )
            print(
                {
                    "r": r,
                    "exact_cover_C8_components": len(components),
                    "component_profiles": sorted(component_profile),
                },
                flush=True,
            )
        print(
            {
                "r": r,
                "exact_covers_from_row_universe": count,
                "orbit_states": len(states),
                "dfs_memo_states": memo_states,
                "fiber_equals_orbit_by_count": count == len(states),
            },
            flush=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--count-covers", action="store_true")
    args = parser.parse_args()
    for value in args.r:
        run(value, args.count_covers)
