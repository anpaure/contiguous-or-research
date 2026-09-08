#!/usr/bin/env python3
"""Audit the optimal five-row b=9 switch repairing the first shadow."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product


REMOVED = [
    (1, 3, 4, 2, 9, 7, 5, 6, 8),
    (1, 4, 3, 7, 2, 6, 5, 8, 9),
    (1, 4, 5, 3, 2, 8, 6, 7, 9),
    (1, 5, 3, 2, 9, 7, 6, 4, 8),
    (1, 6, 4, 3, 2, 8, 7, 5, 9),
]

ADDED = [
    (1, 3, 5, 2, 9, 7, 4, 6, 8),
    (1, 4, 3, 2, 5, 8, 6, 9, 7),
    (1, 4, 3, 8, 2, 6, 7, 9, 5),
    (1, 4, 9, 3, 2, 7, 6, 5, 8),
    (1, 6, 4, 3, 2, 7, 8, 5, 9),
]


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
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


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
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


def msw_row(word: str):
    m = len(word) // 2
    n = 2 * m + 1
    q = [x for x in rho(word)] + [n]
    return canonical(tuple(q[(-1 - 2 * j) % n] for j in range(n)))


def windows(order, k):
    b = len(order)
    return frozenset(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def window_cycle(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def cycle_edges(order, k):
    cyc = window_cycle(order, k)
    return frozenset(
        frozenset((cyc[i], cyc[(i + 1) % len(cyc)])) for i in range(len(cyc))
    )


def odd_cycle_edges(order, k):
    vertices = tuple(windows(order, k))
    edges = {
        frozenset((vertices[i], vertices[j]))
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
        if vertices[i].isdisjoint(vertices[j])
    }
    assert len(edges) == len(vertices)
    return frozenset(edges)


def same_start_ribbon(order, k, reverse=False):
    order = tuple(reversed(order)) if reverse else tuple(order)
    b = len(order)
    answer = {}
    for i in range(b):
        middle = frozenset(order[(i + j) % b] for j in range(k))
        lower = frozenset(order[(i + j) % b] for j in range(k - 1))
        assert middle not in answer
        answer[middle] = lower
    return answer


def insert_word(outer, inner, gap):
    return outer[:gap] + inner + outer[gap:]


def fmt_set(s):
    return "".join(map(str, sorted(s)))


def omitted_words_with_last(order, distinguished):
    b = len(order)
    answers = []
    for base in (tuple(order), tuple(reversed(order))):
        for shift in range(b):
            c = base[shift:] + base[:shift]
            q = [None] * b
            for j, value in enumerate(c):
                q[(-1 - 2 * j) % b] = value
            if q[-1] == distinguished:
                answers.append(tuple(q))
    return sorted(set(answers))


def main():
    b, m = 9, 4
    word_of_row = {msw_row(w): w for w in dyck_words(m)}
    canonical_factor = set(word_of_row)
    removed = {canonical(x) for x in REMOVED}
    added = {canonical(x) for x in ADDED}
    assert len(canonical_factor) == 14
    assert removed <= canonical_factor
    assert not (added & canonical_factor)
    switched_factor = canonical_factor - removed | added
    assert len(switched_factor) == 14

    old_middle = Counter(s for row in canonical_factor for s in windows(row, m))
    new_middle = Counter(s for row in switched_factor for s in windows(row, m))
    all_middle = {frozenset(x) for x in combinations(range(1, b + 1), m)}
    assert old_middle == new_middle == Counter({x: 1 for x in all_middle})

    old_trade_middle = Counter(s for row in removed for s in windows(row, m))
    new_trade_middle = Counter(s for row in added for s in windows(row, m))
    assert old_trade_middle == new_trade_middle

    all_shadow = {frozenset(x) for x in combinations(range(1, b + 1), m - 1)}
    old_shadow = Counter(s for row in canonical_factor for s in windows(row, m - 1))
    new_shadow = Counter(s for row in switched_factor for s in windows(row, m - 1))
    old_holes = all_shadow - old_shadow.keys()
    new_holes = all_shadow - new_shadow.keys()
    assert len(old_holes) == 4
    assert not new_holes
    new_shadow_hist = Counter(new_shadow.values())

    old_trade_shadow = Counter(s for row in removed for s in windows(row, m - 1))
    new_trade_shadow = Counter(s for row in added for s in windows(row, m - 1))
    delta = new_trade_shadow.copy()
    delta.subtract(old_trade_shadow)
    delta = Counter({s: v for s, v in delta.items() if v})

    print("old_holes", " ".join(sorted(map(fmt_set, old_holes))))
    print("new_holes", len(new_holes))
    print("shadow_delta")
    for s, v in sorted(delta.items(), key=lambda z: tuple(sorted(z[0]))):
        print(f"  {fmt_set(s)} {v:+d}")
    print("old_shadow_hist", sorted(Counter(old_shadow.values()).items()), "holes", len(old_holes))
    print("new_shadow_hist", sorted(new_shadow_hist.items()), "holes", len(new_holes))

    # The 5x5 intersection matrix is the exact middle-window trade incidence.
    rem = sorted(removed)
    add = sorted(added)
    matrix = [[len(windows(x, m) & windows(y, m)) for y in add] for x in rem]
    print("middle_intersection_matrix")
    for row in matrix:
        print(" ", *row, "sum", sum(row))
    print("column_sums", *[sum(matrix[i][j] for i in range(5)) for j in range(5)])

    graph = defaultdict(set)
    for i in range(5):
        for j in range(5):
            if matrix[i][j]:
                graph[("R", i)].add(("A", j))
                graph[("A", j)].add(("R", i))
    seen = set()
    components = []
    for v in graph:
        if v in seen:
            continue
        queue = deque([v])
        seen.add(v)
        comp = []
        while queue:
            u = queue.popleft()
            comp.append(u)
            for z in graph[u]:
                if z not in seen:
                    seen.add(z)
                    queue.append(z)
        components.append(comp)
    print("trade_components", [len(c) for c in components])
    print("removed_dyck_words", [word_of_row[x] for x in sorted(removed)])
    print("omitted_label_forms")
    for label, collection in (("R", sorted(removed)), ("A", sorted(added))):
        for row in collection:
            print(label, [" ".join(map(str, q)) for q in omitted_words_with_last(row, b)])

    # View the same trade as a red/blue 2-factor switch in J(9,4).
    red_edges = set().union(*(cycle_edges(x, m) for x in removed))
    blue_edges = set().union(*(cycle_edges(x, m) for x in added))
    common_edges = red_edges & blue_edges
    red_only = red_edges - blue_edges
    blue_only = blue_edges - red_edges
    assert len(red_edges) == len(blue_edges) == 45
    assert len(red_only) == len(blue_only)
    coloured = defaultdict(list)
    for edge in red_only:
        u, v = tuple(edge)
        coloured[u].append((v, "R"))
        coloured[v].append((u, "R"))
    for edge in blue_only:
        u, v = tuple(edge)
        coloured[u].append((v, "B"))
        coloured[v].append((u, "B"))
    assert all(
        sum(c == "R" for _, c in inc) == sum(c == "B" for _, c in inc)
        for inc in coloured.values()
    )
    seen_vertices = set()
    switch_components = []
    for v in coloured:
        if v in seen_vertices:
            continue
        queue = deque([v])
        seen_vertices.add(v)
        vertices = []
        while queue:
            u = queue.popleft()
            vertices.append(u)
            for z, _ in coloured[u]:
                if z not in seen_vertices:
                    seen_vertices.add(z)
                    queue.append(z)
        edges = sum(len(coloured[u]) for u in vertices) // 2
        switch_components.append((len(vertices), edges))
    print(
        "johnson_switch",
        {"common_edges": len(common_edges), "each_colour_changed": len(red_only), "components": sorted(switch_components)},
    )

    old_odd_edges = set().union(*(odd_cycle_edges(x, m) for x in removed))
    new_odd_edges = set().union(*(odd_cycle_edges(x, m) for x in added))
    odd_common = old_odd_edges & new_odd_edges
    odd_red = old_odd_edges - new_odd_edges
    odd_blue = new_odd_edges - old_odd_edges
    odd_coloured = defaultdict(list)
    for colour, edges in (("R", odd_red), ("B", odd_blue)):
        for edge in edges:
            u, v = tuple(edge)
            odd_coloured[u].append((v, colour))
            odd_coloured[v].append((u, colour))
    odd_seen = set()
    odd_components = []
    for v in odd_coloured:
        if v in odd_seen:
            continue
        queue = deque([v])
        odd_seen.add(v)
        vertices = []
        while queue:
            u = queue.popleft()
            vertices.append(u)
            for z, _ in odd_coloured[u]:
                if z not in odd_seen:
                    odd_seen.add(z)
                    queue.append(z)
        edges = sum(len(odd_coloured[u]) for u in vertices) // 2
        degrees = Counter(len(odd_coloured[u]) for u in vertices)
        odd_components.append((len(vertices), edges, sorted(degrees.items())))
    print(
        "odd_graph_switch",
        {
            "common_edges": len(odd_common),
            "each_colour_changed": len(odd_red),
            "components": sorted(odd_components),
        },
    )
    assert len(odd_red) == len(odd_blue)

    # Exact punctured-ribbon test.  Orient every row, attach to each middle
    # window its same-start lower prefix, and ask whether one dirty window per
    # old/new row can absorb every changed attachment.
    best = None
    ribbon_certificate = None
    for old_bits in product((0, 1), repeat=5):
        old_maps = [same_start_ribbon(rem[i], m, bool(old_bits[i])) for i in range(5)]
        old_map = {x: y for z in old_maps for x, y in z.items()}
        assert len(old_map) == 45
        for new_bits in product((0, 1), repeat=5):
            new_maps = [same_start_ribbon(add[i], m, bool(new_bits[i])) for i in range(5)]
            new_map = {x: y for z in new_maps for x, y in z.items()}
            assert old_map.keys() == new_map.keys()
            mismatches = {x for x in old_map if old_map[x] != new_map[x]}
            score = len(mismatches)
            if best is None or score < best[0]:
                best = (score, old_bits, new_bits, mismatches)
            if score > 5:
                continue
            old_owner = {x: i for i, z in enumerate(old_maps) for x in z}
            new_owner = {x: i for i, z in enumerate(new_maps) for x in z}
            by_pair = defaultdict(list)
            for x in old_map:
                by_pair[(old_owner[x], new_owner[x])].append(x)
            for perm in permutations(range(5)):
                choices = [by_pair[(i, perm[i])] for i in range(5)]
                if any(not z for z in choices):
                    continue
                for dirty in product(*choices):
                    dirty_set = set(dirty)
                    if len(dirty_set) == 5 and mismatches <= dirty_set:
                        ribbon_certificate = (old_bits, new_bits, dirty_set)
                        break
                if ribbon_certificate is not None:
                    break
            if ribbon_certificate is not None:
                break
        if ribbon_certificate is not None:
            break
    assert best is not None
    print(
        "punctured_ribbon",
        {
            "minimum_changed_attachments": best[0],
            "old_orientations": best[1],
            "new_orientations": best[2],
            "changed_middle": sorted(fmt_set(x) for x in best[3]),
            "exact_one_dirty_each": ribbon_certificate is not None,
        },
    )
    if ribbon_certificate is not None:
        print(
            "ribbon_certificate",
            ribbon_certificate[0],
            ribbon_certificate[1],
            sorted(fmt_set(x) for x in ribbon_certificate[2]),
        )

    depth_changes = []
    for q in range(1, m):
        old_counter = Counter(s for row in removed for s in windows(row, m - q))
        new_counter = Counter(s for row in added for s in windows(row, m - q))
        old_loss = old_counter - new_counter
        new_gain = new_counter - old_counter
        depth_changes.append(
            {
                "q": q,
                "old_occurrences_removed": sum(old_loss.values()),
                "new_occurrences_added": sum(new_gain.values()),
                "old_target_support": len(old_loss),
                "new_target_support": len(new_gain),
            }
        )
    print("depth_target_multiset_changes", depth_changes)

    # Exact r=4 marked-gap ledger: insert 1100/1010 into every gap of every
    # semilength-2 root and count certificate pairs touched by removed rows.
    marked = []
    for outer in dyck_words(m - 2):
        for gap in range(len(outer) + 1):
            rows_pair = (
                msw_row(insert_word(outer, "1100", gap)),
                msw_row(insert_word(outer, "1010", gap)),
            )
            marked.append((outer, gap, sum(x in removed for x in rows_pair)))
    assert len(marked) == (2 * m - 3) * 2
    print(
        "marked_gap_pairs",
        {
            "total": len(marked),
            "touched": sum(t > 0 for _, _, t in marked),
            "both_rows_removed": sum(t == 2 for _, _, t in marked),
            "untouched": sum(t == 0 for _, _, t in marked),
            "ledger": marked,
        },
    )
    print("PASS")


if __name__ == "__main__":
    main()
