#!/usr/bin/env python3
"""CNF builder/decoder for the q4 k17 Z17 quotient exact cover.

Exactly-one rows use a linear sequential encoding.  Build, SAT solve, and
decode only on H100.
"""

from __future__ import annotations

import argparse
import json
import sys

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    generate_candidates,
    generate_group_closed_candidates,
    owner_orbits,
    verify_development,
)


def build(pool_size, seed, group_closed, cnf_path, map_path):
    representatives, orbit_index = owner_orbits()
    generator = generate_group_closed_candidates if group_closed else generate_candidates
    candidates, attempts = generator(pool_size, seed, orbit_index)
    incidence = [[] for _ in representatives]
    for i, candidate in enumerate(candidates, 1):
        for vertex in candidate["edge"]:
            incidence[vertex].append(i)
    assert all(incidence)

    next_variable = len(candidates) + 1
    clauses = []
    for row in incidence:
        clauses.append(tuple(row))
        if len(row) <= 1:
            continue
        sequential = list(range(next_variable, next_variable + len(row) - 1))
        next_variable += len(row) - 1
        clauses.append((-row[0], sequential[0]))
        for i in range(1, len(row) - 1):
            clauses.append((-row[i], sequential[i]))
            clauses.append((-sequential[i - 1], sequential[i]))
            clauses.append((-row[i], -sequential[i - 1]))
        clauses.append((-row[-1], -sequential[-1]))

    with open(cnf_path, "w", encoding="ascii") as stream:
        stream.write(f"p cnf {next_variable - 1} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)) + " 0\n")
    with open(map_path, "w", encoding="utf-8") as stream:
        json.dump({
            "pool_size": len(candidates),
            "attempts": attempts,
            "group_closed": group_closed,
            "owner_orbits": len(representatives),
            "min_degree": min(map(len, incidence)),
            "max_degree": max(map(len, incidence)),
            "candidates": [
                {"core": list(candidate["core"]),
                 "order": list(candidate["order"]),
                 "edge": list(candidate["edge"])}
                for candidate in candidates
            ],
        }, stream)
    print(json.dumps({
        "status": "BUILT",
        "variables": next_variable - 1,
        "clauses": len(clauses),
        "pool_size": len(candidates),
        "attempts": attempts,
        "group_closed": group_closed,
        "min_degree": min(map(len, incidence)),
        "max_degree": max(map(len, incidence)),
    }, sort_keys=True))


def decode(map_path, solution_path):
    data = json.load(open(map_path, encoding="utf-8"))
    values = []
    status = None
    for line in open(solution_path, encoding="ascii", errors="ignore"):
        if line.startswith("s "):
            status = line.strip()
        if line.startswith("v "):
            values.extend(int(token) for token in line.split()[1:] if token != "0")
    assert status is not None and "SATISFIABLE" in status and "UNSATISFIABLE" not in status
    chosen_indices = sorted(
        value - 1 for value in values if 1 <= value <= data["pool_size"]
    )
    assert len(chosen_indices) == 143
    chosen = [data["candidates"][i] for i in chosen_indices]
    normalized = [
        {"core": tuple(item["core"]),
         "order": tuple(item["order"]),
         "edge": tuple(item["edge"])}
        for item in chosen
    ]
    loads = [0] * data["owner_orbits"]
    for item in normalized:
        for vertex in item["edge"]:
            loads[vertex] += 1
    assert set(loads) == {1}
    rails, owners, point = verify_development(normalized)
    print(json.dumps({
        "status": "PASS",
        "selected_rail_orbits": len(normalized),
        "developed_rails": rails,
        "covered_owners": owners,
        "point_degree": sorted(set(point.values())),
        "certificate": [
            {"core": list(item["core"]),
             "order": list(item["order"]),
             "quotient_edge": list(item["edge"])}
            for item in normalized
        ],
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    builder = sub.add_parser("build")
    builder.add_argument("--pool-size", type=int, default=20000)
    builder.add_argument("--seed", type=int, default=20260814)
    builder.add_argument("--group-closed", action="store_true")
    builder.add_argument("--cnf", required=True)
    builder.add_argument("--map", required=True)
    decoder = sub.add_parser("decode")
    decoder.add_argument("--map", required=True)
    decoder.add_argument("--solution", required=True)
    args = parser.parse_args()
    if args.command == "build":
        build(args.pool_size, args.seed, args.group_closed, args.cnf, args.map)
    else:
        decode(args.map, args.solution)


if __name__ == "__main__":
    main()
