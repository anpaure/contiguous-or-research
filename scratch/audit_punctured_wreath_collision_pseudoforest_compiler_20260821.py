#!/usr/bin/env python3
"""Exact finite audit of the collision-pseudoforest puncturing compiler.

Intended execution environment: H100 only.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
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
    m = len(word) // 2
    n = 2 * m + 1
    q = [x for x in rho(word)] + [n]
    return canonical(tuple(q[(-1 - 2 * j) % n] for j in range(n)))


def windows(order, k):
    b = len(order)
    return tuple(
        frozenset(order[(i + j) % b] for j in range(k)) for i in range(b)
    )


def canonical_factor(r):
    rows = tuple(sorted({msw_row(w) for w in dyck_words(r)}))
    middle = Counter(x for row in rows for x in windows(row, r))
    all_middle = {
        frozenset(x) for x in combinations(range(1, 2 * r + 2), r)
    }
    assert middle == Counter({x: 1 for x in all_middle})
    return rows


def collision_data(rows, chosen, r):
    lower_by_row = {i: windows(rows[i], r - 1) for i in chosen}
    owners = defaultdict(list)
    for i, deck in lower_by_row.items():
        assert len(set(deck)) == 2 * r + 1
        for target in deck:
            owners[target].append(i)
    repeated = {t: tuple(v) for t, v in owners.items() if len(v) >= 2}
    vertices = [("R", i) for i in chosen] + [("T", t) for t in repeated]
    adj = {v: set() for v in vertices}
    edge_count = 0
    for target, row_ids in repeated.items():
        tv = ("T", target)
        for i in row_ids:
            rv = ("R", i)
            adj[tv].add(rv)
            adj[rv].add(tv)
            edge_count += 1
    return lower_by_row, owners, repeated, adj, edge_count


def components(adj):
    seen = set()
    answer = []
    for start in adj:
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        verts = set()
        edge_twice = 0
        while queue:
            v = queue.popleft()
            verts.add(v)
            edge_twice += len(adj[v])
            for z in adj[v]:
                if z not in seen:
                    seen.add(z)
                    queue.append(z)
        edges = edge_twice // 2
        beta = edges - len(verts) + 1
        answer.append((verts, edges, beta))
    return answer


def is_pseudoforest(adj):
    return all(beta <= 1 for _, _, beta in components(adj))


def demand_matching(repeated):
    clones = []
    neighbors = {}
    for target, row_ids in repeated.items():
        for j in range(len(row_ids) - 1):
            clone = (target, j)
            clones.append(clone)
            neighbors[clone] = row_ids
    row_mate = {}
    clone_mate = {}

    def augment(clone, seen):
        for row in neighbors[clone]:
            if row in seen:
                continue
            seen.add(row)
            if row not in row_mate or augment(row_mate[row], seen):
                row_mate[row] = clone
                clone_mate[clone] = row
                return True
        return False

    for clone in clones:
        augment(clone, set())
    return clones, clone_mate, row_mate


def materialize_punctures(rows, chosen, r, lower_by_row, clone_mate):
    dirty_target = {}
    for (target, _), row in clone_mate.items():
        assert row not in dirty_target
        dirty_target[row] = target
    dirty_index = {}
    for row in chosen:
        target = dirty_target.get(row, lower_by_row[row][0])
        dirty_index[row] = lower_by_row[row].index(target)
    active_lower = []
    active_middle = []
    for row in chosen:
        j = dirty_index[row]
        active_lower.extend(
            target for i, target in enumerate(lower_by_row[row]) if i != j
        )
        middle = windows(rows[row], r)
        active_middle.extend(target for i, target in enumerate(middle) if i != j)
    assert len(active_lower) == len(set(active_lower))
    assert len(active_middle) == len(set(active_middle))
    assert len(active_lower) == len(active_middle) == 2 * r * len(chosen)


def insertion_formula(rows, chosen, candidate, r, owners, repeated, adj):
    comps = components(adj)
    component_of = {}
    beta_of = {}
    for cid, (verts, _, beta) in enumerate(comps):
        for v in verts:
            component_of[v] = cid
        beta_of[cid] = beta
    attachments = []
    for target in windows(rows[candidate], r - 1):
        old = owners.get(target, ())
        if len(old) == 1:
            attachments.append(("R", old[0]))
        elif len(old) >= 2:
            assert target in repeated
            attachments.append(("T", target))
    hit = {component_of[v] for v in attachments}
    predicted_beta = sum(beta_of[cid] for cid in hit) + len(attachments) - len(hit)
    new_chosen = tuple(sorted(chosen + (candidate,)))
    _, _, _, new_adj, _ = collision_data(rows, new_chosen, r)
    new_comp = next(
        (beta for verts, _, beta in components(new_adj) if ("R", candidate) in verts),
        0,
    )
    assert predicted_beta == new_comp
    assert (predicted_beta <= 1) == is_pseudoforest(new_adj)


def audit_r(r):
    rows = canonical_factor(r)
    subset_count = 0
    pseudo_count = 0
    extension_count = 0
    for mask in range(1 << len(rows)):
        chosen = tuple(i for i in range(len(rows)) if (mask >> i) & 1)
        lower_by_row, owners, repeated, adj, _ = collision_data(rows, chosen, r)
        pseudo = is_pseudoforest(adj)
        clones, clone_mate, _ = demand_matching(repeated)
        assert pseudo == (len(clone_mate) == len(clones))
        if pseudo:
            pseudo_count += 1
            materialize_punctures(
                rows, chosen, r, lower_by_row, clone_mate
            )
            for candidate in range(len(rows)):
                if candidate not in chosen:
                    insertion_formula(
                        rows, chosen, candidate, r, owners, repeated, adj
                    )
                    extension_count += 1
        subset_count += 1
    return {
        "r": r,
        "b": 2 * r + 1,
        "rows": len(rows),
        "subsets": subset_count,
        "pseudoforests": pseudo_count,
        "extensions": extension_count,
    }


def main():
    summaries = [audit_r(r) for r in range(2, 5)]
    print("PUNCTURED_WREATH_COLLISION_PSEUDOFOREST_AUDIT_PASS", summaries)


if __name__ == "__main__":
    main()
