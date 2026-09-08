#!/usr/bin/env python3
import collections
import re
import sys


def read_graph(path):
    graph = collections.defaultdict(set)
    current = None
    with open(path, encoding="utf-8") as source:
        for line in source:
            if line.startswith("ROOT "):
                current = line.split()[1]
                graph[current]
            elif line.startswith(" EDGE "):
                other = re.search(r"to=([01]+)", line).group(1)
                graph[current].add(other)
                graph[other].add(current)
    return graph


def read_images(path):
    rows = []
    with open(path, encoding="utf-8") as source:
        for line in source:
            if not line.startswith(" root="):
                continue
            root = re.search(r"root=([01]+)", line).group(1)
            images = set(re.search(r"images=([01,]+)", line).group(1).strip(",").split(","))
            rows.append((root, images))
    return rows


def components(graph, vertices):
    unseen = set(vertices)
    pieces = []
    while unseen:
        start = unseen.pop()
        piece = {start}
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for other in graph[word] & vertices:
                if other in unseen:
                    unseen.remove(other)
                    piece.add(other)
                    queue.append(other)
        pieces.append(piece)
    return pieces


graph = read_graph(sys.argv[1])
bad = 0
for root, images in read_images(sys.argv[2]):
    pieces = components(graph, images)
    if len(pieces) > 1:
        bad += 1
        print("SPLIT", root, "|".join(",".join(sorted(piece)) for piece in pieces))
print("SUMMARY bad=%d" % bad)
