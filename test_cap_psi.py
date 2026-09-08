#!/usr/bin/env python3
import collections
import re
import sys


def dyck_words(m):
    out = []

    def visit(prefix, up, down):
        if len(prefix) == 2 * m:
            out.append(prefix)
            return
        if up < m:
            visit(prefix + "1", up + 1, down)
        if down < up:
            visit(prefix + "0", up, down + 1)

    visit("", 0, 0)
    return out


def mirror(word):
    return "".join("1" if bit == "0" else "0" for bit in reversed(word))


def read_suffix_graph(path):
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


def connected(graph, support):
    unseen = set(support)
    start = unseen.pop()
    queue = collections.deque([start])
    while queue:
        word = queue.popleft()
        for other in graph[word] & unseen:
            unseen.remove(other)
            queue.append(other)
    return not unseen


def base_patterns(max_rank):
    patterns = []
    for t in range(max_rank - 2):
        for w in dyck_words(t):
            patterns.append(("alpha(" + w + ")", {
                "1" + w + "11000",
                "1" + w + "10100",
                "1" + w + "10010",
            }))
    patterns.extend([
        ("beta", {"111000", "101100", "101010"}),
        ("gamma", {"11001100", "11011000", "11101000"}),
        ("delta", {"111000", "110100", "101100", "101010"}),
    ])
    return patterns


def valid_dyck(word):
    height = 0
    for bit in word:
        height += 1 if bit == "1" else -1
        if height < 0:
            return False
    return height == 0


def all_contexts(rank):
    seen = {}
    for name, pattern in base_patterns(rank):
        base_len = len(next(iter(pattern)))
        if any(len(word) != base_len for word in pattern):
            raise AssertionError(name)
        remainder = 2 * rank - base_len
        if remainder < 0 or remainder % 2:
            continue
        for context in dyck_words(remainder // 2):
            for cut in range(remainder + 1):
                left, right = context[:cut], context[cut:]
                core = pattern if cut % 2 == 0 else {mirror(word) for word in pattern}
                support = frozenset(left + word + right for word in core)
                if not all(valid_dyck(word) for word in support):
                    raise AssertionError((name, context, cut, support))
                seen.setdefault(support, (name, context, cut))
    return seen


graph_path = sys.argv[1]
rank = int(sys.argv[2])
graph = read_suffix_graph(graph_path)
contexts = all_contexts(rank)
bad = []
for support, origin in contexts.items():
    if not connected(graph, support):
        bad.append((origin, support))
print("CAP_PSI rank=%d vertices=%d tuples=%d bad=%d" %
      (rank, len(graph), len(contexts), len(bad)))
for origin, support in bad[:30]:
    print(" BAD", origin, ",".join(sorted(support)))
