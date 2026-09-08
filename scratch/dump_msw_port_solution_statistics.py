#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csp")
    parser.add_argument("solution")
    parser.add_argument("output")
    args = parser.parse_args()

    options = []
    with open(args.csp) as source:
        head = source.readline().split()
        _, m, d, n, vertices, root, expected = head
        m, d, n, vertices, root, expected = map(
            int, (m, d, n, vertices, root, expected)
        )
        for line in source:
            _, child, parent, oc, a, op, b = line.split()
            options.append(tuple(map(int, (child, parent, oc, a, op, b))))
    assert len(options) == expected

    selected = []
    with open(args.solution) as source:
        header = source.readline().strip()
        for line in source:
            fields = list(map(int, line.split()[1:]))
            index, option = fields[0], tuple(fields[1:])
            assert options[index] == option
            selected.append(option)

    by_vertex = defaultdict(list)
    children = Counter()
    for child, parent, oc, a, op, b in selected:
        by_vertex[child].append(a)
        by_vertex[parent].append(b)
        children[parent] += 1

    distinct_port_hist = Counter()
    port_pattern_hist = Counter()
    child_port_pattern_hist = Counter()
    for vertex in range(vertices):
        ports = sorted(set(by_vertex[vertex]))
        distinct_port_hist[len(ports)] += 1
        if ports:
            normalized = tuple((port - ports[0]) % n for port in ports)
            port_pattern_hist[normalized] += 1
        child_port_pattern_hist[(children[vertex], len(ports))] += 1

    report = {
        "header": header,
        "m": m,
        "d": d,
        "n": n,
        "vertices": vertices,
        "root": root,
        "child_hist": dict(sorted(Counter(children.values()).items())),
        "distinct_port_hist": dict(sorted(distinct_port_hist.items())),
        "child_port_pattern_hist": {
            str(key): value for key, value in sorted(child_port_pattern_hist.items())
        },
        "top_port_patterns": [
            [list(pattern), count] for pattern, count in port_pattern_hist.most_common(100)
        ],
    }
    with open(args.output, "w") as out:
        json.dump(report, out, indent=2, sort_keys=True)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
