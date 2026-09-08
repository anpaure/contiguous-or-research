#!/usr/bin/env python3
"""Z17 owner exact cover enriched by random images of the q4 unit atom.

Each relabelled seven-by-seven atom contributes fourteen correlated pure
rail columns whose signed quotient current is a single owner-orbit unit.
This tests whether the proved local semigroup atom supplies the missing
repair connectivity in the global quotient pool.  H100 only.
"""

from __future__ import annotations

import argparse
import json
import random
import sys

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K, canonical_orbit_mask, deck_masks, owner_orbits,
)
from solve_q4_k17_z17_quotient_mixed_sat_20260814 import (
    generate_period, write_cnf, verify,
)
from verify_q4_v13_seven_by_seven_atom_20260814 import BASE, EXTRA


ATOM_C0 = (13, 14, 15, 16)


def edge_for(core, order, orbit_index):
    edge = tuple(sorted(
        orbit_index[canonical_orbit_mask(owner)]
        for owner in deck_masks(core, order)
    ))
    return edge if len(set(edge)) == len(order) else None


def generate_atom_columns(groups, seed, orbit_index):
    rng = random.Random(seed + 424242)
    candidates = []
    seen = set()
    accepted_groups = 0
    attempts = 0
    literal = BASE + EXTRA
    while accepted_groups < groups:
        attempts += 1
        permutation = list(range(K))
        rng.shuffle(permutation)
        group = []
        valid = True
        for name, sign, center, order in literal:
            core = tuple(sorted(permutation[x] for x in (*ATOM_C0, center)))
            moved_order = tuple(permutation[x] for x in order)
            edge = edge_for(core, moved_order, orbit_index)
            if edge is None:
                valid = False
                break
            group.append({
                "period": len(order), "core": core, "order": moved_order,
                "edge": edge, "atom_sign": sign,
            })
        if not valid:
            continue
        accepted_groups += 1
        for candidate in group:
            key = (candidate["period"], candidate["edge"])
            if key in seen: continue
            seen.add(key); candidates.append(candidate)
    return candidates, attempts


def build(pool10, pool11, atom_groups, seed, cnf_path, map_path):
    reps, orbit_index = owner_orbits()
    c10, a10 = generate_period(pool10, 10, seed, orbit_index)
    c11, a11 = generate_period(pool11, 11, seed, orbit_index)
    atoms, aa = generate_atom_columns(atom_groups, seed, orbit_index)
    candidates = []
    seen = set()
    for candidate in c10 + c11 + atoms:
        key = (candidate["period"], tuple(candidate["edge"]))
        if key in seen: continue
        seen.add(key); candidates.append(candidate)
    variables, clauses, minimum, maximum = write_cnf(
        candidates, len(reps), cnf_path
    )
    with open(map_path, "w", encoding="utf-8") as stream:
        json.dump({
            "owner_orbits": len(reps), "candidates": [
                {"period": c["period"], "core": list(c["core"]),
                 "order": list(c["order"]), "edge": list(c["edge"]),
                 "atom_sign": c.get("atom_sign")}
                for c in candidates
            ]}, stream)
    print(json.dumps({
        "status": "BUILT", "variables": variables, "clauses": clauses,
        "candidates": len(candidates), "random10": len(c10),
        "random11": len(c11), "atom_columns": len(atoms),
        "atom_groups": atom_groups, "attempts10": a10,
        "attempts11": a11, "atom_attempts": aa,
        "min_degree": minimum, "max_degree": maximum,
    }, sort_keys=True))


def decode(map_path, solution_path):
    data = json.load(open(map_path, encoding="utf-8"))
    status = None; values = []
    for line in open(solution_path, encoding="ascii", errors="ignore"):
        if line.startswith("s "): status = line.strip()
        if line.startswith("v "):
            values.extend(int(x) for x in line.split()[1:] if x != "0")
    assert status and "SATISFIABLE" in status and "UNSATISFIABLE" not in status
    indices = sorted(v - 1 for v in values if 1 <= v <= len(data["candidates"]))
    chosen = [data["candidates"][i] for i in indices]
    loads = [0] * data["owner_orbits"]
    for c in chosen:
        for v in c["edge"]: loads[v] += 1
    assert set(loads) == {1}
    counts = {p: sum(c["period"] == p for c in chosen) for p in (10, 11)}
    assert 10 * counts[10] + 11 * counts[11] == 1430
    rails = verify(chosen)
    print(json.dumps({
        "status": "PASS", "period_counts": counts,
        "selected_rail_orbits": len(chosen), "developed_rails": rails,
        "covered_owners": 24310, "point_degree": [12870],
        "selected_atom_sourced": sum(c.get("atom_sign") is not None for c in chosen),
        "certificate": [
            {"period": c["period"], "core": c["core"],
             "order": c["order"], "quotient_edge": c["edge"]}
            for c in chosen],
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--pool10", type=int, default=20000)
    b.add_argument("--pool11", type=int, default=20000)
    b.add_argument("--atom-groups", type=int, default=10000)
    b.add_argument("--seed", type=int, default=20260814)
    b.add_argument("--cnf", required=True); b.add_argument("--map", required=True)
    d = sub.add_parser("decode"); d.add_argument("--map", required=True); d.add_argument("--solution", required=True)
    args = parser.parse_args()
    if args.cmd == "build": build(args.pool10, args.pool11, args.atom_groups, args.seed, args.cnf, args.map)
    else: decode(args.map, args.solution)


if __name__ == "__main__": main()
