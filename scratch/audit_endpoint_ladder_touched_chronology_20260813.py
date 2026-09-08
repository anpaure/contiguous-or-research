#!/usr/bin/env python3
"""Audit topology and coordinate-run lengths on endpoint-ladder touched rows."""

from __future__ import annotations

import argparse
import collections
import json

import audit_pbbs_portal_compound_coexistence_20260813 as co
import verify_symbolic_endpoint_ladder_roots_20260813 as sym


def finite_runs(bits, value):
    n = len(bits)
    if all(x == value for x in bits):
        return []
    if all(x != value for x in bits):
        return []
    start = next(i for i in range(n) if bits[i] != value)
    ans = []
    i = (start + 1) % n
    while i != start:
        if bits[i] == value:
            length = 0
            while bits[i] == value:
                length += 1
                i = (i + 1) % n
            ans.append(length)
        else:
            i = (i + 1) % n
    return ans


def finite_run_spans(bits, value):
    """Return (cyclic start,length) for all nontrivial value-runs."""
    n = len(bits)
    if all(x == value for x in bits) or all(x != value for x in bits):
        return []
    ans = []
    for i in range(n):
        if bits[i] == value and bits[(i - 1) % n] != value:
            length = 1
            while bits[(i + length) % n] == value:
                length += 1
            ans.append((i, length))
    return ans


def audit(m, d):
    rec = sym.audit(m, d)
    rows = {}
    row_labels = {}
    for step in rec["roots"]:
        row = step["row"]
        if row is not None:
            row = tuple(row)
            rows[row] = True
            row_labels.setdefault(row, []).append(
                {"circuit": step["circuit"], "step": step["step"],
                 "root": step["root"]})

    adjacency = collections.defaultdict(set)
    old_edges = {}
    owner_row = {}
    for row in rows:
        owners = [co.cyc_window(row, i, m+1) for i in range(2*m+1)]
        for owner in owners:
            assert owner not in owner_row or owner_row[owner] == row
            owner_row[owner] = row
        for i in range(2*m+1):
            a, b = owners[i], owners[(i+1) % (2*m+1)]
            adjacency[a].add(b)
            adjacency[b].add(a)
            old_edges[a & b] = frozenset((a, b))

    changed = {}
    changed_labels = {}
    for step in rec["roots"]:
        facet = frozenset(step["facet"])
        if step["circuit"] == "seam":
            pair = frozenset(frozenset(x) for x in step["to"])
        else:
            pair = frozenset((frozenset(step["stationary"]),
                              frozenset(step["to"])))
        changed[facet] = pair
        changed_labels[facet] = {"circuit": step["circuit"],
                                 "step": step["step"]}

    for facet, new_edge in changed.items():
        old_edge = old_edges[facet]
        a, b = tuple(old_edge)
        adjacency[a].remove(b)
        adjacency[b].remove(a)
        c, e = tuple(new_edge)
        adjacency[c].add(e)
        adjacency[e].add(c)

    bad_degree = {tuple(sorted(x)): len(ns) for x, ns in adjacency.items()
                  if len(ns) != 2}
    assert not bad_degree
    cycles = []
    unseen = set(adjacency)
    while unseen:
        start = next(iter(unseen))
        cycle = [start]
        prev = None
        cur = start
        while True:
            nxt = next(x for x in adjacency[cur] if x != prev)
            if nxt == start:
                break
            cycle.append(nxt)
            prev, cur = cur, nxt
        unseen -= set(cycle)
        cycles.append(cycle)

    run_records = []
    witnesses = []
    min_pos = None
    min_zero = None
    for ci, cycle in enumerate(cycles):
        for z in range(2*m+1):
            bits = [int(z in owner) for owner in cycle]
            for value, name in ((1, "positive"), (0, "zero")):
                runs = finite_runs(bits, value)
                if not runs:
                    continue
                rmin = min(runs)
                if value:
                    min_pos = rmin if min_pos is None else min(min_pos, rmin)
                else:
                    min_zero = rmin if min_zero is None else min(min_zero, rmin)
                if rmin < d + 1:
                    run_records.append({"cycle": ci, "coordinate": z,
                                        "type": name, "runs": runs,
                                        "minimum": rmin,
                                        "cycle_length": len(cycle)})
                if rmin <= 2:
                    for start, length in finite_run_spans(bits, value):
                        if length != rmin or len(witnesses) >= 40:
                            continue
                        around = [cycle[(start - 1 + j) % len(cycle)]
                                  for j in range(length + 2)]
                        witnesses.append({
                            "cycle": ci, "coordinate": z, "type": name,
                            "length": length,
                            "owners": [sorted(x) for x in around],
                            "symmetric_differences": [
                                sorted(around[j] ^ around[j + 1])
                                for j in range(len(around) - 1)
                            ],
                            "edge_labels": [
                                changed_labels.get(around[j] & around[j + 1],
                                                   {"unchanged": True})
                                for j in range(len(around) - 1)
                            ],
                            "old_row_labels": [
                                row_labels.get(owner_row.get(x), [])
                                for x in around
                            ],
                        })
    return {
        "m": m, "d": d, "q": d+1,
        "old_touched_rows": len(rows),
        "touched_owners": len(adjacency),
        "new_cycles": len(cycles),
        "cycle_lengths": sorted(map(len, cycles)),
        "minimum_positive_run": min_pos,
        "minimum_zero_run": min_zero,
        "positive_safe": not any(x["type"] == "positive" for x in run_records),
        "biresident": not run_records,
        "short_run_count": len(run_records),
        "short_runs": run_records[:500],
        "minimum_run_witnesses": witnesses,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+")
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = [audit(*map(int, x.split(":"))) for x in args.pairs]
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
