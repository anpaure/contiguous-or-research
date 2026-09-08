#!/usr/bin/env python3
"""Full compatible-pair portal census for canonical missing rank-(R+1) targets.

Heavy runs belong on h100.  Unlike the transposition census, this considers
every pair of tight MSW components.  For a missing target U of rank R+1 it
only needs the states adjacent to the R-subsets of U, so the exact census is
small: U is created iff a new splice adjacency joins two such owners.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import math

import audit_msw_common_history_upper_deck_20260813 as up
import audit_msw_inverse_trade_portal_shadow_20260813 as base


def audit(m, explicit_only=False, d_override=None):
    R = m + 1
    n = 2 * m + 1
    W = math.comb(n, R)
    half = 1 << (n - 1)
    d = 0
    while d * W + d * (d + 1) // 2 < half:
        d += 1
    if d_override is not None:
        d = d_override
    roots = list(base.dyck_words(m))
    rows = [list(base.msw_row(root)) for root in roots]

    owner_component = {}
    states = [[] for _ in roots]
    owner_boundary_states = collections.defaultdict(list)
    canonical_q2 = set()
    for v, row in enumerate(rows):
        for oi, order in enumerate((row, list(reversed(row)))):
            owners = up.owner_cycle(order, 0, R)
            for i, owner in enumerate(owners):
                owner_component.setdefault(owner, v)
                assert owner_component[owner] == v
                canonical_q2.add(owner | owners[(i + 1) % n])
            for shift in range(n):
                st = up.state(order, shift, d, R)
                left = owners[(shift - 1) % n]
                right = owners[shift]
                si = len(states[v])
                states[v].append((oi, shift, st, left, right))
                owner_boundary_states[left].append((v, si, "L"))
                owner_boundary_states[right].append((v, si, "R"))

    prefix = "110011001111"
    explicit_targets = []
    if m >= 6:
        for suffix in base.dyck_words(m - 6):
            word = prefix + suffix
            U = sum((bit == "1") << i for i, bit in enumerate(word))
            explicit_targets.append((word, U))
    if explicit_only:
        missing = {U for _, U in explicit_targets}
        assert not (missing & canonical_q2)
        all_missing_count = None
    else:
        all_q2 = {sum(1 << z for z in comb)
                  for comb in itertools.combinations(range(n), R + 1)}
        missing = all_q2 - canonical_q2
        all_missing_count = len(missing)
    degree = {}
    state_degree = {}
    examples = {}
    for U in missing:
        owners = [U & ~(1 << z) for z in range(n) if U >> z & 1]
        records = set()
        for owner in owners:
            records.update((v, si) for v, si, _ in owner_boundary_states[owner])
        portals = set()
        sportals = 0
        ex = []
        records = sorted(records)
        for ii, (a, ia) in enumerate(records):
            oa, sa, xa, la, ra = states[a][ia]
            for b, ib in records[ii + 1:]:
                if a == b:
                    continue
                ob, sb, xb, lb, rb = states[b][ib]
                if not up.compatible(xa, xb):
                    continue
                if ((la & U) == la and (rb & U) == rb) or (
                        (lb & U) == lb and (ra & U) == ra):
                    portals.add((a, b))
                    sportals += 1
                    if len(ex) < 3:
                        ex.append({"roots": [a, b],
                                   "states": [[oa, sa], [ob, sb]],
                                   "cross_owner_pairs": [
                                       [sorted(z for z in range(n) if la >> z & 1),
                                        sorted(z for z in range(n) if rb >> z & 1)],
                                       [sorted(z for z in range(n) if lb >> z & 1),
                                        sorted(z for z in range(n) if ra >> z & 1)],
                                   ]})
        degree[U] = len(portals)
        state_degree[U] = sportals
        if ex:
            examples[U] = ex

    explicit = []
    for word, U in explicit_targets:
        explicit.append({"word": word,
                         "canonical_missing": U not in canonical_q2,
                         "full_pair_degree": degree.get(U),
                         "full_state_degree": state_degree.get(U),
                         "examples": examples.get(U, [])})
    return {
        "m": m, "R": R, "d": d, "roots": len(roots),
        "canonical_missing_q2": all_missing_count,
        "targets_censused": len(missing),
        "full_compatible_pair_degree_histogram": dict(collections.Counter(
            degree.values())),
        "full_compatible_state_degree_histogram": dict(collections.Counter(
            state_degree.values())),
        "zero_full_pair_degree": sum(x == 0 for x in degree.values()),
        "explicit_TV_family": explicit,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--json")
    ap.add_argument("--explicit-only", action="store_true")
    ap.add_argument("--d", type=int)
    args = ap.parse_args()
    ans = audit(args.m, args.explicit_only, args.d)
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
