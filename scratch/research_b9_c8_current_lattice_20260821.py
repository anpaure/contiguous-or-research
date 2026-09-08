#!/usr/bin/env python3
"""Exact reachable C8 shadow-current span for small canonical factors.

This tests the precise conjecture that reachable C8 currents span the full
uniform-matroid square-current space.  Intended execution: H100 only.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import combinations


def dyck_words(m):
    def rec(pos, ones, word):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()
    yield from rec(0, 0, [])


def mu(word):
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word):
    if not word:
        return []
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_row(word):
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def forms(order):
    order = tuple(order)
    for base in (order, tuple(reversed(order))):
        for shift in range(len(order)):
            yield base[shift:] + base[:shift]


def switches(row1, row2, r):
    answers = set()
    for left, right in ((row1, row2), (row2, row1)):
        right_forms = set(forms(right))
        for old1 in forms(left):
            a, b0 = old1[:2]
            p = old1[2 : r + 1]
            c, d = old1[r + 1 : r + 3]
            q = old1[r + 3 :]
            old2 = (c, a) + p + (d, b0) + q
            if old2 not in right_forms:
                continue
            new1 = canonical((a, c) + p + (b0, d) + q)
            new2 = canonical((b0, a) + p + (d, c) + q)
            answer = tuple(sorted((new1, new2)))
            if answer != tuple(sorted((row1, row2))):
                answers.add(answer)
    return tuple(answers)


def windows(order, k):
    b = len(order)
    return tuple(frozenset(order[(i + j) % b] for j in range(k))
                 for i in range(b))


def neighbours(state, cache, r):
    for i, j in combinations(range(len(state)), 2):
        key = tuple(sorted((state[i], state[j])))
        if key not in cache:
            cache[key] = switches(*key, r)
        for new_pair in cache[key]:
            nxt = tuple(sorted(new_pair + tuple(state[k] for k in range(len(state))
                                                 if k not in (i, j))))
            if len(set(nxt)) == len(state):
                yield nxt, key, new_pair


def mod_rank(columns, nrows, prime):
    basis = {}
    for sparse in columns:
        v = {i: value % prime for i, value in sparse.items() if value % prime}
        while v:
            pivot = min(v)
            if pivot not in basis:
                inv = pow(v[pivot], prime - 2, prime)
                v = {i: value * inv % prime for i, value in v.items()}
                basis[pivot] = v
                break
            scale = v[pivot]
            row = basis[pivot]
            for i, value in row.items():
                z = (v.get(i, 0) - scale * value) % prime
                if z:
                    v[i] = z
                elif i in v:
                    del v[i]
    assert all(0 <= pivot < nrows for pivot in basis)
    return len(basis), tuple(sorted(basis))


def main(r, max_states):
    b = 2 * r + 1
    start = tuple(sorted(msw_row(word) for word in dyck_words(r)))
    targets = tuple(frozenset(x) for x in combinations(range(1, b + 1), r - 1))
    target_index = {target: i for i, target in enumerate(targets)}
    cache = {}
    queue = deque([start])
    seen = {start}
    currents = {}
    edge_count = 0
    while queue and len(seen) <= max_states:
        state = queue.popleft()
        for nxt, old_pair, new_pair in neighbours(state, cache, r):
            edge_count += 1
            old_shadow = Counter(target for row in old_pair for target in windows(row, r - 1))
            new_shadow = Counter(target for row in new_pair for target in windows(row, r - 1))
            current = new_shadow.copy()
            current.subtract(old_shadow)
            sparse = {target_index[target]: value for target, value in current.items() if value}
            assert sorted(sparse.values()) == [-1, -1, 1, 1]
            # Every current preserves total and every coordinate marginal.
            assert sum(sparse.values()) == 0
            for x in range(1, b + 1):
                assert sum(value for i, value in sparse.items() if x in targets[i]) == 0
            key = tuple(sorted(sparse.items()))
            currents[key] = sparse
            neg = tuple(sorted((i, -value) for i, value in sparse.items()))
            currents[neg] = {i: -value for i, value in sparse.items()}
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

    columns = list(currents.values())
    ranks = {p: mod_rank(columns, len(targets), p) for p in (2, 3, 5, 1000003)}

    # Full abstract square-current set on rank-(r-1) subsets.
    abstract = {}
    for core in combinations(range(1, b + 1), r - 3):
        rest = sorted(set(range(1, b + 1)) - set(core))
        for four in combinations(rest, 4):
            a, bb, c, d = four
            for pairing in (((a, bb), (c, d)), ((a, c), (bb, d)), ((a, d), (bb, c))):
                (u, v), (x, y) = pairing
                sets = [frozenset(core + (u, x)), frozenset(core + (v, y)),
                        frozenset(core + (u, y)), frozenset(core + (v, x))]
                sparse = {target_index[sets[0]]: -1, target_index[sets[1]]: -1,
                          target_index[sets[2]]: 1, target_index[sets[3]]: 1}
                abstract[tuple(sorted(sparse.items()))] = sparse
    abstract_columns = list(abstract.values())
    abstract_ranks = {p: mod_rank(abstract_columns, len(targets), p)
                      for p in (2, 3, 5, 1000003)}

    reachable_support = set().union(*(set(v) for v in columns))
    start_shadow = Counter(target for row in start for target in windows(row, r - 1))
    untouched = [targets[i] for i in range(len(targets)) if i not in reachable_support]
    untouched_mult = Counter(start_shadow[target] for target in untouched)
    touched_mult = Counter(start_shadow[targets[i]] for i in reachable_support)
    distinguished = b
    untouched_by_distinguished = Counter(
        (distinguished in target, start_shadow[target]) for target in untouched
    )

    # Union of fixed-anchor Johnson edges over every move seen anywhere in
    # the physical C8 component.
    anchored_edges = {a: set() for a in range(1, b)}
    for sparse in columns:
        support = tuple(targets[i] for i in sparse)
        core = set.intersection(*(set(target) for target in support))
        if len(core) != r - 3 or distinguished in core:
            continue
        anchored = tuple(target for target in support if distinguished in target)
        nonanchored = tuple(target for target in support if distinguished not in target)
        if len(anchored) != 2 or len(nonanchored) != 2:
            continue
        extra = (set(nonanchored[0]) & set(nonanchored[1])) - core
        if len(extra) != 1:
            continue
        a = next(iter(extra))
        edge = tuple(sorted((frozenset(set(target) - {distinguished})
                             for target in anchored),
                            key=lambda item: tuple(sorted(item))))
        if len(set(edge)) == 2:
            anchored_edges[a].add(edge)

    anchored_component_counts = {}
    anchored_component_excess = 0
    for a in range(1, b):
        vertices = tuple(frozenset(vertex) for vertex in combinations(
            (point for point in range(1, b) if point != a), r - 2
        ))
        adjacency = {vertex: set() for vertex in vertices}
        for left, right in anchored_edges[a]:
            adjacency[left].add(right)
            adjacency[right].add(left)
        unseen = set(vertices)
        sizes = []
        while unseen:
            stack = [unseen.pop()]
            size = 0
            while stack:
                vertex = stack.pop()
                size += 1
                for neighbour in adjacency[vertex]:
                    if neighbour in unseen:
                        unseen.remove(neighbour)
                        stack.append(neighbour)
            sizes.append(size)
        anchored_component_counts[a] = {
            "edges": len(anchored_edges[a]),
            "components": len(sizes),
            "largest": max(sizes),
            "isolated": sum(size == 1 for size in sizes),
        }
        anchored_component_excess += len(sizes) - 1
    print("B9_C8_CURRENT_LATTICE_PROFILE", {
        "states": len(seen),
        "directed_edges_seen": edge_count,
        "oriented_currents": len(columns),
        "targets_touched": len(reachable_support),
        "reachable_ranks": ranks,
        "abstract_currents": len(abstract_columns),
        "abstract_ranks": abstract_ranks,
        "expected_kernel_dimension": len(targets) - b,
        "untouched_start_multiplicities": dict(untouched_mult),
        "touched_start_multiplicities": dict(touched_mult),
        "untouched_by_distinguished": dict(untouched_by_distinguished),
        "anchored_component_excess": anchored_component_excess,
        "anchored_component_counts": anchored_component_counts,
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=4)
    parser.add_argument("--max-states", type=int, default=10_000_000)
    args = parser.parse_args()
    main(args.r, args.max_states)
