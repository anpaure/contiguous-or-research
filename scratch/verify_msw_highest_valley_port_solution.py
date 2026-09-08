#!/usr/bin/env python3
import argparse
from collections import Counter, defaultdict


def cyclic_distance(a, b, n):
    delta = abs(a - b)
    return min(delta, n - delta)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csp")
    parser.add_argument("solution")
    args = parser.parse_args()

    options = []
    with open(args.csp) as source:
        tag, m, d, n, vertices, root, expected = source.readline().split()
        assert tag == "H"
        m, d, n, vertices, root, expected = map(
            int, (m, d, n, vertices, root, expected)
        )
        for line in source:
            tag, child, parent, oc, a, op, b = line.split()
            assert tag == "O"
            options.append(tuple(map(int, (child, parent, oc, a, op, b))))
    assert len(options) == expected

    selected = []
    with open(args.solution) as source:
        header = source.readline().strip()
        assert "status=OPTIMAL" in header or "status=FEASIBLE" in header
        for line in source:
            tag, index, child, parent, oc, a, op, b = line.split()
            assert tag == "S"
            index = int(index)
            option = tuple(map(int, (child, parent, oc, a, op, b)))
            assert options[index] == option
            selected.append(option)

    assert len(selected) == vertices - 1
    parent = [-1] * vertices
    orientation = [-1] * vertices
    incident_ports = defaultdict(list)
    children = [[] for _ in range(vertices)]
    for child, par, oc, a, op, b in selected:
        assert child != root and parent[child] == -1
        parent[child] = par
        children[par].append(child)
        for vertex, value in ((child, oc), (par, op)):
            assert orientation[vertex] in (-1, value)
            orientation[vertex] = value
        incident_ports[child].append(a)
        incident_ports[par].append(b)

    assert parent[root] == -1
    assert all(parent[v] >= 0 for v in range(vertices) if v != root)
    for vertex in range(vertices):
        distinct = sorted(set(incident_ports[vertex]))
        for i, a in enumerate(distinct):
            for b in distinct[i + 1 :]:
                assert cyclic_distance(a, b, n) >= d + 1

    seen = set()
    stack = [root]
    while stack:
        vertex = stack.pop()
        assert vertex not in seen
        seen.add(vertex)
        stack.extend(children[vertex])
    assert len(seen) == vertices

    child_hist = Counter(map(len, children))
    distinct_port_hist = Counter(
        len(set(incident_ports[vertex])) for vertex in range(vertices)
    )
    multiplicity_hist = Counter()
    maximum_distinct_ports = max(
        (len(set(incident_ports[vertex])) for vertex in range(vertices)),
        default=0,
    )
    assert maximum_distinct_ports <= n // (d + 1)
    reused_vertices = 0
    maximum_reuse = 0
    for vertex in range(vertices):
        counts = Counter(incident_ports[vertex])
        maximum_reuse = max(maximum_reuse, max(counts.values(), default=0))
        multiplicity_hist.update(counts.values())
        reused_vertices += any(value > 1 for value in counts.values())

    print(
        f"PASS m={m} d={d} n={n} vertices={vertices} selected={len(selected)} "
        f"root={root} oriented0={orientation.count(0)} oriented1={orientation.count(1)} "
        f"reused_vertices={reused_vertices} maximum_reuse={maximum_reuse}"
        f" maximum_distinct_ports={maximum_distinct_ports}"
    )
    print("child_hist", dict(sorted(child_hist.items())))
    print("distinct_port_hist", dict(sorted(distinct_port_hist.items())))
    print("multiplicity_hist", dict(sorted(multiplicity_hist.items())))


if __name__ == "__main__":
    main()
