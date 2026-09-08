#!/usr/bin/env python3
"""H100-only structural/Hall probes for an MSW parent-port CSP catalogue."""

import argparse
from collections import Counter, defaultdict, deque


def cyclic_distance(first, second, n):
    delta = abs(first - second)
    return min(delta, n - delta)


def hopcroft_karp(adjacency):
    left = list(adjacency)
    pair_left = {u: None for u in left}
    pair_right = {}
    distance = {}

    def bfs():
        queue = deque()
        found = False
        for u in left:
            if pair_left[u] is None:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = -1
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                mate = pair_right.get(v)
                if mate is None:
                    found = True
                elif distance[mate] < 0:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        return found

    def dfs(u):
        for v in adjacency[u]:
            mate = pair_right.get(v)
            if mate is None or (
                distance.get(mate) == distance[u] + 1 and dfs(mate)
            ):
                pair_left[u] = v
                pair_right[v] = u
                return True
        distance[u] = -1
        return False

    matching = 0
    while bfs():
        for u in left:
            if pair_left[u] is None and dfs(u):
                matching += 1
    return matching, pair_left


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csp")
    parser.add_argument("--orientation", type=int, choices=(0, 1))
    args = parser.parse_args()

    by_child = defaultdict(set)
    parent_port_children = defaultdict(set)
    child_parent_ports = defaultdict(set)
    edge_port_pairs = defaultdict(set)
    with open(args.csp, encoding="utf-8") as source:
        head = source.readline().split()
        assert head[0] == "H"
        m, d, n, vertices, root, expected = map(int, head[1:])
        count = 0
        for line in source:
            values = list(map(int, line.split()[1:]))
            if len(values) == 4:
                child, parent, child_start, parent_start = values
            elif len(values) == 6:
                child, parent, child_orientation, child_start, parent_orientation, parent_start = values
                if args.orientation is not None and (
                    child_orientation != args.orientation
                    or parent_orientation != args.orientation
                ):
                    count += 1
                    continue
            else:
                raise AssertionError(values)
            count += 1
            by_child[child].add((parent, parent_start))
            parent_port_children[parent, parent_start].add(child)
            child_parent_ports[child, parent].add(parent_start)
            edge_port_pairs[child, parent].add((child_start, parent_start))
    assert count == expected
    assert set(by_child) == set(range(vertices)) - {root}

    option_hist = Counter(map(len, by_child.values()))
    maximum_option_count = max(option_hist)
    maximum_coalescence = max(map(len, parent_port_children.values()))

    matching_size, matching = hopcroft_karp(by_child)
    unmatched = [child for child, value in matching.items() if value is None]

    parent_children = defaultdict(set)
    for child, choices in by_child.items():
        for parent, _ in choices:
            parent_children[parent].add(child)
    maximum_potential_children = max(map(len, parent_children.values()))

    # This ignores child-side incident-port conflicts and parent-side pairwise
    # separation, so it is a necessary relaxation, not the full theorem.
    print(
        f"SUMMARY m={m} d={d} n={n} vertices={vertices} root={root} "
        f"child_portclass_matching={matching_size}/{vertices - 1} "
        f"unmatched={len(unmatched)} maximum_child_choices={maximum_option_count} "
        f"maximum_children_coalescing_at_one_parent_port={maximum_coalescence} "
        f"maximum_potential_children_of_parent={maximum_potential_children}"
    )
    print("child_choice_hist", dict(sorted(option_hist.items())))

    # For each parent, report whether its available port-class set contains a
    # full maximum separated subset. This is only a local availability census.
    capacity = n // (d + 1)
    portset_hist = Counter()
    for parent in range(vertices):
        ports = sorted(port for par, port in parent_port_children if par == parent)
        portset_hist[len(ports)] += 1
    print(f"raw_capacity={capacity} parent_available_port_count_hist", dict(sorted(portset_hist.items())))


if __name__ == "__main__":
    main()
