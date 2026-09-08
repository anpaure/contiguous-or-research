#!/usr/bin/env python3
import collections
import re
import sys


def suffix_graph(path):
    incidence = collections.defaultdict(set)
    current = None
    with open(path, encoding="utf-8") as source:
        for line in source:
            if line.startswith("ROOT "):
                current = line.split()[1]
            elif line.startswith(" EDGE "):
                other = re.search(r"to=([01]+)", line).group(1)
                if other.startswith("10"):
                    incidence[current].add(other[2:])
    graph = collections.defaultdict(set)
    for support in incidence.values():
        for left in support:
            graph[left]
            for right in support:
                if left != right:
                    graph[left].add(right)
    return graph


def mirror(word):
    return "".join("1" if bit == "0" else "0" for bit in reversed(word))


small = suffix_graph(sys.argv[1])
large = suffix_graph(sys.argv[2])
failures = []
edges = 0
for left in small:
    for right in small[left]:
        if left >= right:
            continue
        edges += 1
        lifted_left = "1" + mirror(left) + "0"
        lifted_right = "1" + mirror(right) + "0"
        if lifted_right not in large[lifted_left]:
            failures.append((left, right, lifted_left, lifted_right))
print("WRAP_HOM edges=%d failures=%d" % (edges, len(failures)))
for row in failures[:30]:
    print(" FAIL", *row)
