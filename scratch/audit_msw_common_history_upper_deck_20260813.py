#!/usr/bin/env python3
"""Audit upper-deck survival under one compatible MSW common-history splice.

Substantive runs belong on h100.  For each transposition-adjacent compatible
pair of tight MSW rows, choose its first exact common-history state, splice
the two owner circuits at that history, and compare the global upper support
against the untouched canonical MSW factor.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import math

import audit_msw_inverse_trade_portal_shadow_20260813 as base


def dyck_words(m):
    yield from base.dyck_words(m)


def rank(mask):
    return mask.bit_count()


def intervals(order, size):
    n = len(order)
    ans = []
    for i in range(n):
        x = 0
        for j in range(size):
            x |= 1 << order[(i + j) % n]
        ans.append(x)
    return ans


def state(order, shift, d, R):
    n = len(order)
    s = R - d
    maximal = []
    forced = []
    for j in range(d):
        start = (shift + j) % n
        p = 0
        for z in range(s):
            p |= 1 << order[(start + z) % n]
        maximal.append(p)
        forced.append((1 << order[start]) |
                      (1 << order[(start + s - 1) % n]))
    return maximal, forced


def compatible(x, y):
    mx, fx = x
    my, fy = y
    return all(((a | b) & ~(u & v)) == 0
               for a, b, u, v in zip(fx, fy, mx, my))


def owner_cycle(order, shift, R):
    n = len(order)
    return intervals(order[shift:] + order[:shift], R)


def deck(owners, R, ground):
    """Occurrence Counter of all proper upper unions in one cyclic trace."""
    n = len(owners)
    out = collections.Counter()
    for i in range(n):
        u = 0
        for length in range(1, n):
            u |= owners[(i + length - 1) % n]
            if rank(u) > R and u != ground:
                out[u] += 1
    return out


def audit(m, pair_limit=None, optimize_states=False):
    R = m + 1
    n = 2 * m + 1
    W = math.comb(n, R)
    half = 1 << (n - 1)
    d = 0
    while d * W + d * (d + 1) // 2 < half:
        d += 1
    roots = list(dyck_words(m))
    rows = [list(base.msw_row(root)) for root in roots]
    root_index = {root: i for i, root in enumerate(roots)}
    ground = (1 << n) - 1

    row_decks = []
    global_deck = collections.Counter()
    for row in rows:
        dd = deck(owner_cycle(row, 0, R), R, ground)
        row_decks.append(dd)
        global_deck.update(dd)

    tested = 0
    with_casualty = 0
    forced_casualty_pairs = 0
    casualty_rank_hist = collections.Counter()
    created_missing_rank_hist = collections.Counter()
    created_missing_targets = set()
    missing_state_degree = collections.Counter()
    missing_pair_degree = collections.Counter()
    # Construct the (small at audited m) canonical missing upper ideal by
    # combinations, avoiding a scan of the Boolean cube.
    canonical_missing = set()
    for r in range(R + 1, n):
        for comb in itertools.combinations(range(n), r):
            u = sum(1 << z for z in comb)
            if global_deck[u] == 0:
                canonical_missing.add(u)
    examples = []
    safe_adjacency = [set() for _ in roots]
    safe_witness = {}
    for a, root in enumerate(roots):
        ones = [i for i, x in enumerate(root) if x == "1"]
        zeros = [i for i, x in enumerate(root) if x == "0"]
        for p in ones:
            for q in zeros:
                mate = root[:p] + "0" + root[p + 1:]
                mate = mate[:q] + "1" + mate[q + 1:]
                b = root_index.get(mate)
                if b is None or b <= a:
                    continue
                witnesses = []
                for oa in (rows[a], list(reversed(rows[a]))):
                    for sa in range(n):
                        xa = state(oa, sa, d, R)
                        for ob in (rows[b], list(reversed(rows[b]))):
                            for sb in range(n):
                                xb = state(ob, sb, d, R)
                                if compatible(xa, xb):
                                    witnesses.append((oa, sa, ob, sb))
                                    if not optimize_states:
                                        break
                            if witnesses and not optimize_states:
                                break
                        if witnesses and not optimize_states:
                            break
                    if witnesses and not optimize_states:
                        break
                if not witnesses:
                    continue
                old_pair = row_decks[a] + row_decks[b]
                at_risk = {u for u, count in old_pair.items()
                           if global_deck[u] == count}
                best = None
                pair_created_missing = set()
                for witness in witnesses:
                    oa, sa, ob, sb = witness
                    ca = owner_cycle(oa, sa, R)
                    cb = owner_cycle(ob, sb, R)
                    new_values = set(deck(ca + cb, R, ground))
                    state_created = new_values & canonical_missing
                    pair_created_missing |= state_created
                    missing_state_degree.update(state_created)
                    casualties = sorted(at_risk - new_values)
                    if best is None or len(casualties) < len(best[1]):
                        best = (witness, casualties)
                    if not casualties:
                        break
                witness, casualties = best
                oa, sa, ob, sb = witness
                tested += 1
                created_missing_targets |= pair_created_missing
                missing_pair_degree.update(pair_created_missing)
                if casualties:
                    with_casualty += 1
                    if optimize_states:
                        forced_casualty_pairs += 1
                    casualty_rank_hist.update(rank(u) for u in casualties)
                    if len(examples) < 10:
                        examples.append({
                            "roots": [roots[a], roots[b]],
                            "orientation_shift": [
                                [int(oa != rows[a]), sa],
                                [int(ob != rows[b]), sb],
                            ],
                            "casualty_count": len(casualties),
                            "casualty_ranks": dict(collections.Counter(
                                rank(u) for u in casualties)),
                            "first_casualties": [
                                [z for z in range(n) if u >> z & 1]
                                for u in casualties[:5]
                            ],
                        })
                else:
                    safe_adjacency[a].add(b)
                    safe_adjacency[b].add(a)
                    safe_witness[(a, b)] = (
                        int(oa != rows[a]), sa, int(ob != rows[b]), sb)
                if pair_limit and tested >= pair_limit:
                    break
            if pair_limit and tested >= pair_limit:
                break
        if pair_limit and tested >= pair_limit:
            break
    seen = set()
    safe_components = 0
    for start in range(len(roots)):
        if start in seen:
            continue
        safe_components += 1
        seen.add(start)
        stack = [start]
        while stack:
            x = stack.pop()
            for y in safe_adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)

    # Deterministic BFS spanning tree in the edgewise upper-safe graph.
    tree_parent = [-1] * len(roots)
    tree_edge = [None] * len(roots)
    if safe_components == 1:
        tree_parent[0] = 0
        queue = collections.deque([0])
        while queue:
            a = queue.popleft()
            for b in sorted(safe_adjacency[a]):
                if tree_parent[b] != -1:
                    continue
                tree_parent[b] = a
                key = (a, b) if a < b else (b, a)
                w = safe_witness[key]
                tree_edge[b] = w if a < b else (w[2], w[3], w[0], w[1])
                queue.append(b)
    cuts_by_root = [[] for _ in roots]
    for b in range(1, len(roots)):
        if tree_parent[b] == -1:
            continue
        a = tree_parent[b]
        oa, sa, ob, sb = tree_edge[b]
        cuts_by_root[a].append((oa, sa, b))
        cuts_by_root[b].append((ob, sb, a))
    cut_multiplicity = collections.Counter(len(x) for x in cuts_by_root)
    min_cut_spacing_hist = collections.Counter()
    roots_with_conflicting_same_cut_orientation = 0
    for cuts in cuts_by_root:
        if len(cuts) < 2:
            continue
        by_orientation = collections.defaultdict(list)
        for orient, shift, _ in cuts:
            by_orientation[orient].append(shift)
        if len(by_orientation) > 1:
            roots_with_conflicting_same_cut_orientation += 1
        spacings = []
        for shifts in by_orientation.values():
            if len(shifts) < 2:
                continue
            shifts.sort()
            spacings.extend((shifts[(i + 1) % len(shifts)] - shifts[i]) % n
                            for i in range(len(shifts)))
        if spacings:
            min_cut_spacing_hist[min(spacings)] += 1
    explicit_family = []
    if m >= 6:
        prefix = "110011001111"
        for suffix in dyck_words(m - 6):
            word = prefix + suffix
            u = sum((bit == "1") << i for i, bit in enumerate(word))
            explicit_family.append({
                "word": word,
                "canonical_missing": u in canonical_missing,
                "pair_degree": missing_pair_degree.get(u, 0),
                "state_degree": missing_state_degree.get(u, 0),
            })
    return {
        "m": m,
        "R": R,
        "d": d,
        "roots": len(roots),
        "compatible_transposition_pairs_tested": tested,
        "pairs_with_global_upper_casualty": with_casualty,
        "pairs_whose_every_compatible_state_has_casualty": (
            forced_casualty_pairs if optimize_states else None),
        "upper_safe_transposition_edges": sum(map(len, safe_adjacency)) // 2,
        "upper_safe_graph_components": safe_components,
        "upper_safe_graph_active_roots": sum(bool(x) for x in safe_adjacency),
        "safe_bfs_tree_cut_multiplicity_histogram": dict(cut_multiplicity),
        "safe_bfs_tree_roots_using_both_orientations": (
            roots_with_conflicting_same_cut_orientation),
        "safe_bfs_tree_min_same_orientation_cut_spacing_histogram": dict(
            min_cut_spacing_hist),
        "casualty_rank_histogram": dict(casualty_rank_hist),
        "canonical_missing_upper_targets": len(canonical_missing),
        "canonical_missing_rank_histogram": dict(collections.Counter(
            rank(u) for u in canonical_missing)),
        "missing_targets_created_by_some_tested_state": len(created_missing_targets),
        "created_missing_rank_histogram": dict(collections.Counter(
            rank(u) for u in created_missing_targets)),
        "unhit_canonical_missing_targets": len(canonical_missing - created_missing_targets),
        "missing_target_pair_degree_histogram": dict(collections.Counter(
            missing_pair_degree.get(u, 0) for u in canonical_missing)),
        "missing_target_state_degree_histogram": dict(collections.Counter(
            missing_state_degree.get(u, 0) for u in canonical_missing)),
        "first_unhit_immediate_upper_targets": [
            [z for z in range(n) if u >> z & 1]
            for u in sorted(canonical_missing - created_missing_targets)
            if rank(u) == R + 1
        ][:20],
        "explicit_TV_family_portal_degrees": explicit_family,
        "examples": examples,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--pair-limit", type=int)
    ap.add_argument("--optimize-states", action="store_true")
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = audit(args.m, args.pair_limit, args.optimize_states)
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")


if __name__ == "__main__":
    main()
