#!/usr/bin/env python3
import collections
import re
import sys
from typing import Dict, Set, Tuple


def metrics(word: str) -> Tuple[int, int, int]:
    height = 0
    returns = 0
    maximum = 0
    area = 0
    for bit in word:
        area += height
        height += 1 if bit == "1" else -1
        maximum = max(maximum, height)
        returns += height == 0
    return returns, maximum, area


def read_graph(path: str):
    graph = collections.defaultdict(set)  # type: Dict[str, Set[str]]
    current = None
    with open(path, encoding="utf-8") as source:
        for line in source:
            if line.startswith("ROOT "):
                current = line.split()[1]
                graph[current]
            elif line.startswith(" EDGE "):
                assert current is not None
                match = re.search(r"to=([01]+)", line)
                assert match
                other = match.group(1)
                graph[current].add(other)
                graph[other].add(current)
    return graph


def primitive(word: str) -> bool:
    height = 0
    for bit in word[:-1]:
        height += 1 if bit == "1" else -1
        if height == 0:
            return False
    return True


def first_return_split(word: str):
    height = 0
    for index, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            return word[1:index], word[index + 1:]
    raise AssertionError(word)


def tamari_descents(word: str):
    if not word:
        return set()
    inside, suffix = first_return_split(word)
    result = {"1" + changed + "0" + suffix
              for changed in tamari_descents(inside)}
    result |= {"1" + inside + "0" + changed
               for changed in tamari_descents(suffix)}
    if inside:
        left, right = first_return_split(inside)
        result.add("1" + left + "0" + "1" + right + "0" + suffix)
    return result


def analyze(path: str):
    graph = read_graph(path)
    m = len(next(iter(graph))) // 2
    flat = "10" * m
    distance = {flat: 0}
    queue = collections.deque([flat])
    while queue:
        word = queue.popleft()
        for other in graph[word]:
            if other not in distance:
                distance[other] = distance[word] + 1
                queue.append(other)

    print(f"FILE {path} m={m} vertices={len(graph)} reached={len(distance)}")
    tests = {
        "more_returns": lambda a, b: metrics(b)[0] > metrics(a)[0],
        "lower_height": lambda a, b: metrics(b)[1] < metrics(a)[1],
        "lower_area": lambda a, b: metrics(b)[2] < metrics(a)[2],
        "lex_smaller": lambda a, b: b < a,
        "lex_larger": lambda a, b: b > a,
    }
    for name, predicate in tests.items():
        bad = [word for word in graph if word != flat
               and not any(predicate(word, other) for other in graph[word])]
        print(f" {name}: bad={len(bad)}", " ".join(sorted(bad)[:12]))

    for word in sorted(graph):
        if word == flat:
            continue
        closer = sorted(other for other in graph[word]
                        if distance.get(other, 10**9) + 1 == distance[word])
        assert closer
        chosen = min(closer, key=lambda z: (-metrics(z)[0], metrics(z)[1],
                                             metrics(z)[2], z))
        print(" DESCENT", word, "->", chosen,
              "dist", distance[word], "metrics", metrics(word), metrics(chosen))

    print(" PRIMITIVE_HUBS")
    for word in sorted(graph):
        if not primitive(word):
            continue
        suffixes = sorted(other[2:] for other in graph[word]
                          if other.startswith("10"))
        print(" HUB", word, "v=" + word[1:-1], "suffixes=" + ",".join(suffixes))

    published = {}
    if m == 4:
        published = {
            "alpha_empty": {"111000", "110100", "110010"},
            "beta": {"111000", "101100", "101010"},
        }
    elif m == 5:
        published = {
            "alpha_10": {"11011000", "11010100", "11010010"},
            "gamma": {"11001100", "11011000", "11101000"},
            "mirror_beta_cap": {"11110000", "11100100", "11010100"},
            "alpha_empty_10": {"11100010", "11010010", "11001010"},
            "beta_10": {"11100010", "10110010", "10101010"},
            "10_alpha_empty": {"10111000", "10110100", "10110010"},
            "10_beta": {"10111000", "10101100", "10101010"},
        }
    if published:
        print(" PUBLISHED_SPANNING_TREE_LIFTS")
        for name, support in published.items():
            containers = []
            for word in graph:
                suffixes = {other[2:] for other in graph[word]
                            if other.startswith("10")}
                if support <= suffixes:
                    containers.append((word, suffixes))
            print(" PATTERN", name, "support=" + ",".join(sorted(support)),
                  "containers=" + ";".join(
                      word + "[" + ",".join(sorted(suffixes)) + "]"
                      for word, suffixes in containers))
            if not containers:
                targets = ["10" + suffix for suffix in sorted(support)]
                base = targets[0]
                for target in targets[1:]:
                    parent = {base: None}
                    queue = collections.deque([base])
                    while queue and target not in parent:
                        word = queue.popleft()
                        for other in graph[word]:
                            if other not in parent:
                                parent[other] = word
                                queue.append(other)
                    path_words = []
                    cursor = target
                    while cursor is not None:
                        path_words.append(cursor)
                        cursor = parent[cursor]
                    print("  REPLACEMENT_PATH", "->".join(reversed(path_words)))

    suffix_graph = collections.defaultdict(set)
    for hub in graph:
        suffixes = [other[2:] for other in graph[hub]
                    if other.startswith("10")]
        for left in suffixes:
            for right in suffixes:
                if left != right:
                    suffix_graph[left].add(right)
    suffix_flat = "10" * (m - 1)
    suffix_distance = {suffix_flat: 0}
    suffix_queue = collections.deque([suffix_flat])
    while suffix_queue:
        word = suffix_queue.popleft()
        for other in suffix_graph[word]:
            if other not in suffix_distance:
                suffix_distance[other] = suffix_distance[word] + 1
                suffix_queue.append(other)
    print(" SUFFIX_TREE reached=%d/%d" % (len(suffix_distance), len(suffix_graph)))
    for word in sorted(suffix_graph):
        if word == suffix_flat:
            continue
        closer = [other for other in suffix_graph[word]
                  if suffix_distance.get(other, 10**9) + 1 == suffix_distance[word]]
        chosen = min(closer, key=lambda z: (-metrics(z)[0], metrics(z)[2], z))
        common_hubs = sorted(hub for hub in graph
                             if "10" + word in graph[hub]
                             and "10" + chosen in graph[hub])
        print("  Q_DESCENT", word, "->", chosen,
              "hub=" + ",".join(common_hubs),
              "dist=" + str(suffix_distance[word]))
    missing_rotations = []
    total_rotations = 0
    for word in suffix_graph:
        for changed in tamari_descents(word):
            total_rotations += 1
            if changed not in suffix_graph[word]:
                missing_rotations.append((word, changed))
    print(" TAMARI_COVERS", "total=" + str(total_rotations),
          "missing=" + str(len(missing_rotations)),
          "examples=" + ",".join(a + "->" + b
                                    for a, b in missing_rotations[:12]))
    for source, target in missing_rotations[:12]:
        parent = {source: None}
        queue = collections.deque([source])
        while queue and target not in parent:
            word = queue.popleft()
            for other in suffix_graph[word]:
                if other not in parent:
                    parent[other] = word
                    queue.append(other)
        path_words = []
        cursor = target
        while cursor is not None:
            path_words.append(cursor)
            cursor = parent[cursor]
        print("  TAMARI_REPLACEMENT", "->".join(reversed(path_words)))


for filename in sys.argv[1:]:
    analyze(filename)
