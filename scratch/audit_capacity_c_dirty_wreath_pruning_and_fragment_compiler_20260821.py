#!/usr/bin/env python3
"""Finite audit for the capacity-c dirty-wreath pruning theorem.

Intended execution environment: H100 only.  The analytic theorem does not
depend on this script.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations


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
    r = len(word) // 2
    b = 2 * r + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def canonical_factor(r):
    rows = tuple(sorted({msw_row(w) for w in dyck_words(r)}))
    middle = Counter(x for row in rows for x in windows(row, r))
    expected = {frozenset(x) for x in combinations(range(1, 2 * r + 2), r)}
    assert middle == Counter({x: 1 for x in expected})
    return rows


def duplicate_demand(decks, chosen):
    counts = Counter(t for i in chosen for t in decks[i])
    return sum(v - 1 for v in counts.values() if v >= 2)


def row_clone_matching(decks, chosen, c):
    b = len(decks[0])
    clones = [(i, j) for i in chosen for j in range(b - c)]
    target_mate = {}
    clone_mate = {}

    def augment(clone, seen):
        row, _ = clone
        for target in decks[row]:
            if target in seen:
                continue
            seen.add(target)
            if target not in target_mate or augment(target_mate[target], seen):
                target_mate[target] = clone
                clone_mate[clone] = target
                return True
        return False

    for clone in clones:
        augment(clone, set())
    return clones, clone_mate


def hall_holds_exhaustive(decks, chosen, c):
    b = len(decks[0])
    for mask in range(1 << len(chosen)):
        sub = [chosen[j] for j in range(len(chosen)) if (mask >> j) & 1]
        union = set(t for i in sub for t in decks[i])
        q = b * len(sub) - len(union)
        if len(union) < (b - c) * len(sub):
            assert q > c * len(sub)
            return False
        assert q <= c * len(sub)
    return True


def find_violation(decks, chosen, c):
    b = len(decks[0])
    best = None
    for mask in range(1, 1 << len(chosen)):
        sub = tuple(chosen[j] for j in range(len(chosen)) if (mask >> j) & 1)
        q = duplicate_demand(decks, sub)
        if q > c * len(sub):
            excess = q - c * len(sub)
            if best is None or excess > best[0]:
                best = (excess, sub)
    return None if best is None else best[1]


def prune(decks, c):
    chosen = tuple(range(len(decks)))
    q_initial = duplicate_demand(decks, chosen)
    charge = 0
    while True:
        bad = find_violation(decks, chosen, c)
        if bad is None:
            break
        before = duplicate_demand(decks, chosen)
        bad_set = set(bad)
        after_chosen = tuple(i for i in chosen if i not in bad_set)
        after = duplicate_demand(decks, after_chosen)
        internal = duplicate_demand(decks, bad)
        assert before - after >= internal > c * len(bad)
        charge += before - after
        chosen = after_chosen
    removed = len(decks) - len(chosen)
    assert c * removed < q_initial if removed else True
    assert charge <= q_initial
    clones, mate = row_clone_matching(decks, chosen, c)
    assert len(mate) == len(clones)
    return chosen, q_initial, removed, mate


def max_matching_cycle_after_deletion(b, dirty):
    clean = set(range(b)) - set(dirty)
    # In window-start coordinates, disjointness is step +/-r.
    r = (b - 1) // 2
    adj = {i: [j for j in ((i + r) % b, (i - r) % b) if j in clean]
           for i in clean}
    mate = {}

    def augment(v, seen):
        for z in adj[v]:
            edge = tuple(sorted((v, z)))
            if edge in seen:
                continue
            seen.add(edge)
            if z not in mate or augment(mate[z], seen):
                mate[v] = z
                mate[z] = v
                return True
        return False

    # General graph augmenting paths need blossom, but every component here
    # is a path; greedily match along its recovered path order instead.
    seen_vertices = set()
    pairs = []
    for start in clean:
        if start in seen_vertices or len(adj[start]) > 1:
            continue
        prev = None
        cur = start
        path = []
        while cur is not None and cur not in path:
            path.append(cur)
            nxt = [z for z in adj[cur] if z != prev]
            prev, cur = cur, (nxt[0] if nxt else None)
        seen_vertices.update(path)
        for j in range(0, len(path) - 1, 2):
            pairs.append((path[j], path[j + 1]))
    assert seen_vertices == clean
    # If dirty is nonempty there are only paths, including isolated vertices.
    assert dirty
    assert all(x in clean and y in clean for x, y in pairs)
    assert len(clean) - 2 * len(pairs) <= len(dirty)
    return pairs


def materialize(decks, rows, r, chosen, c, clone_mate):
    b = 2 * r + 1
    selected_by_row = {i: set() for i in chosen}
    for (row, _), target in clone_mate.items():
        selected_by_row[row].add(target)
    all_lower = []
    all_middle = []
    paired_flags = 0
    for row_id in chosen:
        assert len(selected_by_row[row_id]) == b - c
        lower = decks[row_id]
        middle = windows(rows[row_id], r)
        clean_idx = [j for j, target in enumerate(lower)
                     if target in selected_by_row[row_id]]
        assert len(clean_idx) == b - c
        dirty = set(range(b)) - set(clean_idx)
        pairs = max_matching_cycle_after_deletion(b, dirty)
        paired_flags += 2 * len(pairs)
        for j in clean_idx:
            all_lower.append(lower[j])
            all_middle.append(middle[j])
    assert len(all_lower) == len(set(all_lower))
    assert len(all_middle) == len(set(all_middle))
    assert paired_flags >= (b - 2 * c) * len(chosen)
    return len(all_lower), paired_flags


def audit_r(r):
    rows = canonical_factor(r)
    decks = tuple(windows(row, r - 1) for row in rows)
    b = 2 * r + 1

    # Exhaust the Hall equivalence on all row subsets for b<=7.  For b=9,
    # the full-factor pruning/materialization tests below cover every c.
    hall_cases = 0
    if r <= 3:
        for mask in range(1 << len(rows)):
            chosen = tuple(i for i in range(len(rows)) if (mask >> i) & 1)
            for c in range(1, b):
                hall = hall_holds_exhaustive(decks, chosen, c)
                clones, mate = row_clone_matching(decks, chosen, c)
                assert hall == (len(mate) == len(clones))
                hall_cases += 1

    pruning = []
    for c in range(1, b):
        chosen, q, removed, mate = prune(decks, c)
        clean, paired = materialize(decks, rows, r, chosen, c, mate)
        assert clean >= b * len(rows) - c * len(rows) - b * q / c - 1e-9
        assert paired >= b * len(rows) - 2 * c * len(rows) - b * q / c - 1e-9
        pruning.append((c, q, removed, len(chosen), clean, paired))

    # Exhaust the purely cyclic pairing assertion independently.
    cycle_cases = 0
    for c in range(1, b):
        for dirty in combinations(range(b), c):
            max_matching_cycle_after_deletion(b, dirty)
            cycle_cases += 1

    # Heavy-row fallback.
    counts = Counter(t for deck in decks for t in deck)
    repeated = {t for t, value in counts.items() if value >= 2}
    q = sum(value - 1 for value in counts.values() if value >= 2)
    repeated_incidence = sum(value for value in counts.values() if value >= 2)
    assert repeated_incidence == q + len(repeated) <= 2 * q
    for c in range(1, b):
        degrees = [sum(t in repeated for t in deck) for deck in decks]
        heavy = [i for i, value in enumerate(degrees) if value > c]
        assert len(heavy) < 2 * q / c if heavy else True
        kept = [i for i in range(len(rows)) if i not in heavy]
        clean_targets = [t for i in kept for t in decks[i] if t not in repeated]
        assert len(clean_targets) == len(set(clean_targets))

    return {
        "r": r,
        "b": b,
        "rows": len(rows),
        "hall_cases": hall_cases,
        "cycle_cases": cycle_cases,
        "pruning": pruning,
    }


def main():
    summaries = [audit_r(r) for r in range(2, 5)]
    print("CAPACITY_C_DIRTY_WREATH_PRUNING_FRAGMENT_AUDIT_PASS", summaries)


if __name__ == "__main__":
    main()
