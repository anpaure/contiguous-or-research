#!/usr/bin/env python3
"""Hostile, independent replay of the finite MSW coalesced-port certificate.

Run only on H100.  Unlike the small replay shipped with the solver, this
script reconstructs the Dyck catalogue, MSW tight orders, forced-history
signatures, and highest-valley four-packet DAG before checking the selected
arborescence.
"""

import argparse
from collections import Counter, defaultdict


def dyck_roots(m):
    answer = []

    def visit(position, up, down, word):
        if position == 2 * m:
            answer.append(word)
            return
        if up < m:
            visit(position + 1, up + 1, down, word | (1 << position))
        if down < up:
            visit(position + 1, up, down + 1, word)

    visit(0, 0, 0, 0)
    return answer


def step_heights(word, m):
    before = []
    height = 0
    for position in range(2 * m):
        before.append(height)
        height += 1 if word >> position & 1 else -1
    return before


def g(word, m):
    before = step_heights(word, m)
    down_at_zero = sum(
        not (word >> position & 1) and before[position] == 0
        for position in range(2 * m)
    )
    seen = 0
    for position in range(2 * m):
        if not (word >> position & 1) and before[position] in (0, 1):
            seen += 1
            if seen == down_at_zero + 1:
                return word | (1 << position), position
    raise AssertionError("g is undefined")


def hmap(word, m):
    height = 0
    before = []
    up_at_one = 0
    for position in range(2 * m):
        before.append(height)
        if word >> position & 1 and height == 1:
            up_at_one += 1
        height += 1 if word >> position & 1 else -1
    seen = 0
    for position in range(2 * m):
        if word >> position & 1 and before[position] in (0, 1):
            seen += 1
            if seen == up_at_one:
                return word & ~(1 << position), position
    raise AssertionError("h is undefined")


def tight_order(root, m):
    word = root
    rho = []
    for _ in range(m):
        word, first = g(word, m)
        word, second = hmap(word, m)
        rho.extend((first, second))
    rho.append(2 * m)
    n = 2 * m + 1
    assert sorted(rho) == list(range(n))
    return tuple(rho[(2 * index) % n] for index in range(n))


def signatures(order, d, shift):
    n = len(order)
    return tuple(
        tuple(
            sorted(
                (
                    order[(start + offset) % n],
                    order[(start + shift - 1 + offset) % n],
                )
            )
            for offset in range(d)
        )
        for start in range(n)
    )


def oriented_signatures(root, m, d, shift):
    order = tight_order(root, m)
    return (signatures(order, d, shift), signatures(tuple(reversed(order)), d, shift))


def highest_valley_parents(word, m, root_index):
    before = step_heights(word, m)
    valleys = [
        position
        for position in range(2 * m - 1)
        if not (word >> position & 1) and word >> (position + 1) & 1
    ]
    assert valleys
    maximum = max(before[position] for position in valleys)
    valleys = [position for position in valleys if before[position] == maximum]
    parents = {}
    for valley in valleys:
        moves = [(valley, valley + 1, "01")]
        left = valley > 0 and not (word >> (valley - 1) & 1)
        right = valley + 2 < 2 * m and word >> (valley + 2) & 1
        if left:
            moves.append((valley - 1, valley + 1, "001"))
        if right:
            moves.append((valley, valley + 2, "011"))
        if left and right:
            moves.append((valley - 1, valley + 2, "0011"))
        for first, second, packet in moves:
            assert not (word >> first & 1) and word >> second & 1
            parent_word = word ^ (1 << first) ^ (1 << second)
            parents[root_index[parent_word]] = packet
    return parents


def area(word, m):
    return sum(step_heights(word, m))


def cyclic_distance(first, second, n):
    difference = abs(first - second)
    return min(difference, n - difference)


def parse_header(line):
    fields = {}
    for token in line.split():
        if "=" in token:
            key, value = token.split("=", 1)
            fields[key] = value
    return fields


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csp")
    parser.add_argument("solution")
    args = parser.parse_args()

    options = []
    with open(args.csp, encoding="utf-8") as source:
        tag, m, d, n, vertex_count, root, expected = source.readline().split()
        assert tag == "H"
        m, d, n, vertex_count, root, expected = map(
            int, (m, d, n, vertex_count, root, expected)
        )
        previous = None
        for line in source:
            fields = line.split()
            assert fields[0] == "O" and len(fields) == 7
            option = tuple(map(int, fields[1:]))
            assert previous is None or previous < option
            previous = option
            options.append(option)
    assert len(options) == expected
    assert n == 2 * m + 1 and d >= 1

    roots = dyck_roots(m)
    assert len(roots) == vertex_count
    assert all(
        sum(1 if word >> position & 1 else -1 for position in range(2 * m)) == 0
        and min(step_heights(word, m)) >= 0
        for word in roots
    )
    root_index = {word: index for index, word in enumerate(roots)}
    mountain = (1 << m) - 1
    assert root == root_index[mountain]
    root_area = area(mountain, m)
    assert all(area(word, m) < root_area for index, word in enumerate(roots) if index != root)

    all_signatures = [
        oriented_signatures(word, m, d, m + 1 - d) for word in roots
    ]
    legal_parents = [None] * vertex_count
    packet_hist = Counter()
    children_with_options = set()
    for option in options:
        child, parent, child_orientation, child_start, parent_orientation, parent_start = option
        assert 0 <= child < vertex_count and child != root
        assert 0 <= parent < vertex_count
        assert child_orientation in (0, 1) and parent_orientation in (0, 1)
        assert 0 <= child_start < n and 0 <= parent_start < n
        if legal_parents[child] is None:
            legal_parents[child] = highest_valley_parents(roots[child], m, root_index)
        assert parent in legal_parents[child]
        assert area(roots[parent], m) > area(roots[child], m)
        assert (
            all_signatures[child][child_orientation][child_start]
            == all_signatures[parent][parent_orientation][parent_start]
        )
        children_with_options.add(child)
        packet_hist[legal_parents[child][parent]] += 1
    assert children_with_options == set(range(vertex_count)) - {root}

    selected = []
    selected_indices = set()
    with open(args.solution, encoding="utf-8") as source:
        solution_header = source.readline().strip()
        header = parse_header(solution_header)
        assert header["status"] in ("OPTIMAL", "FEASIBLE")
        assert int(header["m"]) == m and int(header["d"]) == d
        assert int(header["n"]) == n and int(header["vertices"]) == vertex_count
        assert int(header["options"]) == len(options)
        for line in source:
            fields = line.split()
            assert fields[0] == "S" and len(fields) == 8
            index = int(fields[1])
            option = tuple(map(int, fields[2:]))
            assert 0 <= index < len(options) and index not in selected_indices
            assert options[index] == option
            selected_indices.add(index)
            selected.append(option)
    assert int(header["selected"]) == len(selected) == vertex_count - 1

    parent = [-1] * vertex_count
    orientation = [-1] * vertex_count
    children = [[] for _ in range(vertex_count)]
    incident_ports = defaultdict(list)
    selected_packet_hist = Counter()
    for child, par, child_orientation, child_start, parent_orientation, parent_start in selected:
        assert parent[child] == -1
        parent[child] = par
        children[par].append(child)
        selected_packet_hist[legal_parents[child][par]] += 1
        for vertex, value in ((child, child_orientation), (par, parent_orientation)):
            assert orientation[vertex] in (-1, value)
            orientation[vertex] = value
        incident_ports[child].append(child_start)
        incident_ports[par].append(parent_start)

    assert parent[root] == -1
    assert all(parent[vertex] >= 0 for vertex in range(vertex_count) if vertex != root)
    assert all(value in (0, 1) for value in orientation)

    # These pairwise inequalities are exactly what the cyclic-window clauses
    # encode: two starts occur together in a window {s,...,s+d} iff their
    # minimum cyclic distance is at most d.
    for vertex in range(vertex_count):
        distinct = sorted(set(incident_ports[vertex]))
        for index, first in enumerate(distinct):
            for second in distinct[index + 1 :]:
                assert cyclic_distance(first, second, n) >= d + 1

    seen = set()
    stack = [root]
    while stack:
        vertex = stack.pop()
        assert vertex not in seen
        seen.add(vertex)
        stack.extend(children[vertex])
    assert len(seen) == vertex_count

    child_hist = Counter(map(len, children))
    distinct_port_hist = Counter(
        len(set(incident_ports[vertex])) for vertex in range(vertex_count)
    )
    reused_vertices = sum(
        any(count > 1 for count in Counter(incident_ports[vertex]).values())
        for vertex in range(vertex_count)
    )
    maximum_reuse = max(
        max(Counter(incident_ports[vertex]).values(), default=0)
        for vertex in range(vertex_count)
    )
    maximum_distinct = max(
        len(set(incident_ports[vertex])) for vertex in range(vertex_count)
    )
    assert maximum_distinct <= n // (d + 1)

    print(
        f"PASS m={m} d={d} n={n} vertices={vertex_count} "
        f"catalogue_options={len(options)} selected={len(selected)} root={root} "
        f"oriented0={orientation.count(0)} oriented1={orientation.count(1)} "
        f"reused_vertices={reused_vertices} maximum_reuse={maximum_reuse} "
        f"maximum_distinct_ports={maximum_distinct}"
    )
    print("catalogue_packet_hist", dict(sorted(packet_hist.items())))
    print("selected_packet_hist", dict(sorted(selected_packet_hist.items())))
    print("child_hist", dict(sorted(child_hist.items())))
    print("distinct_port_hist", dict(sorted(distinct_port_hist.items())))


if __name__ == "__main__":
    main()
