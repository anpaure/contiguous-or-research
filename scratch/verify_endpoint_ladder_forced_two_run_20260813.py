#!/usr/bin/env python3
"""Verify the all-m forced coordinate-2 run in the endpoint-ladder packet.

Substantive ranges belong on h100.  This reconstructs only the O(m) explicit
touched rows, not the Catalan-size MSW factor.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import verify_symbolic_endpoint_ladder_roots_20260813 as sym


def audit(m: int, d: int):
    rec = sym.audit(m, d)
    rows = {tuple(s["row"]) for s in rec["roots"] if s["row"] is not None}

    adjacency = collections.defaultdict(set)
    old_edges = {}
    for row in rows:
        owners = [co.cyc_window(row, i, m + 1) for i in range(2 * m + 1)]
        for i, a in enumerate(owners):
            b = owners[(i + 1) % len(owners)]
            adjacency[a].add(b)
            adjacency[b].add(a)
            old_edges[a & b] = frozenset((a, b))

    changed_labels = {}
    for step in rec["roots"]:
        facet = frozenset(step["facet"])
        old_edge = old_edges[facet]
        if step["circuit"] == "seam":
            new_edge = frozenset(frozenset(x) for x in step["to"])
        else:
            new_edge = frozenset((frozenset(step["stationary"]),
                                  frozenset(step["to"])))
        a, b = tuple(old_edge)
        adjacency[a].remove(b)
        adjacency[b].remove(a)
        c, e = tuple(new_edge)
        adjacency[c].add(e)
        adjacency[e].add(c)
        changed_labels[facet] = (step["circuit"], step["step"])

    assert all(len(ns) == 2 for ns in adjacency.values())
    k = (frozenset({0, 6, 9, 10, 2 * m - 3})
         | frozenset(range(12, 2 * m - 1, 2)))
    quartet = (
        k | {3, 4},
        k | {2, 3},
        k | {2, 2 * m - 1},
        k | {1, 2 * m - 1},
    )
    assert all(len(x) == m + 1 for x in quartet)
    forward = all(quartet[i + 1] in adjacency[quartet[i]] for i in range(3))
    reverse = all(quartet[i] in adjacency[quartet[i + 1]] for i in range(3))
    assert forward and reverse
    facets = tuple(quartet[i] & quartet[i + 1] for i in range(3))
    assert facets == (k | {3}, k | {2}, k | {2 * m - 1})
    assert facets[0] not in changed_labels
    assert changed_labels[facets[1]] == (2, 4)
    assert facets[2] not in changed_labels
    assert [int(2 in x) for x in quartet] == [0, 1, 1, 0]
    return {
        "m": m,
        "d": d,
        "core_rank": len(k),
        "coordinate_two_word": "0110",
        "facets": [sorted(x) for x in facets],
        "edge_status": ["unchanged", "repair-step-4", "unchanged"],
        "pass": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = [audit(*map(int, pair.split(":"))) for pair in args.pairs]
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")


if __name__ == "__main__":
    main()
