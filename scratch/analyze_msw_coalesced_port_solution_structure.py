#!/usr/bin/env python3
import argparse
from collections import Counter, defaultdict


def dyck_roots(m):
    roots = []

    def rec(pos, up, down, mask):
        if pos == 2 * m:
            roots.append(mask)
            return
        if up < m:
            rec(pos + 1, up + 1, down, mask | (1 << pos))
        if down < up:
            rec(pos + 1, up, down + 1, mask)

    rec(0, 0, 0, 0)
    return roots


def bits(mask, m):
    return "".join("1" if mask >> i & 1 else "0" for i in range(2 * m))


def g(mask, m):
    before = []
    height = down_zero = 0
    for i in range(2 * m):
        before.append(height)
        if not (mask >> i & 1) and height == 0:
            down_zero += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if not (mask >> i & 1) and before[i] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return mask | (1 << i), i
    raise AssertionError


def hmap(mask, m):
    before = []
    height = up_one = 0
    for i in range(2 * m):
        before.append(height)
        if mask >> i & 1 and height == 1:
            up_one += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if mask >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == up_one:
                return mask & ~(1 << i), i
    raise AssertionError


def tight_order(mask, m):
    rho = []
    for _ in range(m):
        mask, a = g(mask, m)
        mask, b = hmap(mask, m)
        rho += [a, b]
    rho.append(2 * m)
    n = 2 * m + 1
    return [rho[(2 * j) % n] for j in range(n)]


def highest_valleys(word):
    height = 0
    values = []
    for i in range(len(word) - 1):
        if word[i : i + 2] == "01":
            values.append((height, i))
        height += 1 if word[i] == "1" else -1
    maximum = max(height for height, _ in values)
    return [i for height, i in values if height == maximum]


def matching(word):
    stack = []
    mate = {}
    for i, bit in enumerate(word):
        if bit == "1":
            stack.append(i)
        else:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    return mate


def triple(word, valley):
    mate = matching(word)
    left_open = mate[valley]
    right_close = mate[valley + 1]
    left = (valley - left_open - 1) // 2
    right = (right_close - valley - 2) // 2
    outside = len(word) // 2 - left - right - 2
    return left, right, outside


def pattern(child, parent, m):
    different = [i for i in range(2 * m) if (child >> i & 1) != (parent >> i & 1)]
    assert len(different) == 2
    p, q = different
    assert not (child >> p & 1) and child >> q & 1 and p < q
    names = {(0, 1): "01", (0, 2): "011", (1, 2): "001", (1, 3): "0011"}
    valley = p if q - p in (1, 2) and child >> (p + 1) & 1 else p + 1
    if q - p == 1:
        name = "01"
        valley = p
    elif q - p == 2:
        if child >> (p + 1) & 1:
            name, valley = "011", p
        else:
            name, valley = "001", p + 1
    elif q - p == 3:
        name, valley = "0011", p + 1
    else:
        raise AssertionError((p, q, bits(child, m), bits(parent, m)))
    assert valley in highest_valleys(bits(child, m))
    return name, valley, p, q


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csp")
    parser.add_argument("solution")
    args = parser.parse_args()

    with open(args.csp) as source:
        _, m, d, n, vertices, root, expected = source.readline().split()
    m, d, n, vertices, root, expected = map(int, (m, d, n, vertices, root, expected))
    roots = dyck_roots(m)
    assert len(roots) == vertices
    orders = [tight_order(mask, m) for mask in roots]
    inverse = [{label: pos for pos, label in enumerate(order)} for order in orders]

    selected = []
    with open(args.solution) as source:
        source.readline()
        for line in source:
            _, index, child, parent, oc, a, op, b = line.split()
            selected.append(tuple(map(int, (child, parent, oc, a, op, b))))
    assert len(selected) == vertices - 1

    packet_hist = Counter()
    triple_packet_hist = Counter()
    normalized_hist = Counter()
    port_roles = defaultdict(list)
    edge_rows = []
    for child, parent, oc, a, op, b in selected:
        name, valley, p, q = pattern(roots[child], roots[parent], m)
        geometry = triple(bits(roots[child], m), valley)
        packet_hist[name] += 1
        triple_packet_hist[(name, geometry)] += 1
        child_anchor = inverse[child][p]
        parent_anchor = inverse[parent][q]
        normalized = ((a - child_anchor) % n, (b - parent_anchor) % n)
        normalized_hist[(name, geometry, normalized)] += 1
        port_roles[child].append((a, "up", name, geometry))
        port_roles[parent].append((b, "down", name, geometry))
        edge_rows.append((child, parent, name, geometry, a, b, normalized, p, q))

    reuse_role_hist = Counter()
    coalesced_examples = []
    for vertex, roles in port_roles.items():
        by_port = defaultdict(list)
        for role in roles:
            by_port[role[0]].append(role[1:])
        for port, values in by_port.items():
            signature = tuple(sorted((kind, name) for kind, name, geometry in values))
            reuse_role_hist[signature] += 1
            if len(values) >= 2 and len(coalesced_examples) < 100:
                coalesced_examples.append((vertex, bits(roots[vertex], m), port, values))

    print("packet_hist", dict(packet_hist))
    print("triple_packet_distinct", len(triple_packet_hist))
    print("top_triple_packet")
    for key, count in triple_packet_hist.most_common(100):
        print(key, count)
    print("normalized_distinct", len(normalized_hist))
    print("top_normalized")
    for key, count in normalized_hist.most_common(150):
        print(key, count)
    print("reuse_role_hist")
    for key, count in reuse_role_hist.most_common(100):
        print(key, count)
    print("coalesced_examples")
    for item in coalesced_examples:
        print(item)


if __name__ == "__main__":
    main()
