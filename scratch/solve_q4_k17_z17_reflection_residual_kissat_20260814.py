#!/usr/bin/env python3
"""Build/decode Kissat CNF for one frozen two-stage residual bank (H100)."""

from __future__ import annotations

import argparse
import json
import random
import sys

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_reflection_two_stage_cpsat_20260814 import choose_disjoint_self
from search_q4_k17_z17_quotient_exact_cover_20260814 import verify_development


def frozen_bank(map_path, sample, seed):
    _, self_options, pairs = make_instance(map_path, sample, seed)
    groups = [[] for _ in range(35)]
    for i, (group, _, rows) in enumerate(self_options):
        groups[group].append((i, frozenset(rows)))
    rng = random.Random(seed)
    bank = None
    for _ in range(100):
        bank = choose_disjoint_self(groups, rng)
        if bank is not None: break
    assert bank is not None
    chosen_self, used = bank
    residual = set(range(680)) - used
    eligible = [i for i, (_, rows) in enumerate(pairs) if set(rows) <= residual]
    return self_options, pairs, chosen_self, residual, eligible


def build(args):
    _, pairs, chosen_self, residual, eligible = frozen_bank(
        args.map, args.sample, args.seed
    )
    incidence = {row: [] for row in residual}
    for variable, pair_index in enumerate(eligible, 1):
        for row in pairs[pair_index][1]: incidence[row].append(variable)
    assert all(incidence.values())
    clauses = []
    next_variable = len(eligible) + 1
    for row in incidence.values():
        clauses.append(tuple(row))
        sequential = list(range(next_variable, next_variable + len(row) - 1))
        next_variable += len(row) - 1
        clauses.append((-row[0], sequential[0]))
        for i in range(1, len(row) - 1):
            clauses.append((-row[i], sequential[i]))
            clauses.append((-sequential[i - 1], sequential[i]))
            clauses.append((-row[i], -sequential[i - 1]))
        clauses.append((-row[-1], -sequential[-1]))
    with open(args.cnf, "w", encoding="ascii") as stream:
        stream.write(f"p cnf {next_variable-1} {len(clauses)}\n")
        for clause in clauses: stream.write(" ".join(map(str, clause)) + " 0\n")
    json.dump({
        "map": args.map, "sample": args.sample, "seed": args.seed,
        "chosen_self": chosen_self, "eligible_pairs": eligible,
        "primary_variables": len(eligible), "rows": len(residual),
    }, open(args.mapping, "w", encoding="utf-8"))
    if args.dlx_instance:
        used = sorted(set(range(680)) - residual)
        with open(args.dlx_instance, "w", encoding="ascii") as stream:
            stream.write(f"680 {len(used)} {len(eligible)}\n")
            stream.write(" ".join(map(str, used)) + "\n")
            for pair_index in eligible:
                stream.write(str(pair_index) + " "
                             + " ".join(map(str, pairs[pair_index][1])) + "\n")
    print(json.dumps({
        "status": "BUILT", "residual_rows": len(residual),
        "eligible_pairs": len(eligible), "variables": next_variable-1,
        "clauses": len(clauses),
    }, sort_keys=True))


def decode(args):
    mapping = json.load(open(args.mapping, encoding="utf-8"))
    self_options, pairs, chosen_self, residual, eligible = frozen_bank(
        mapping["map"], mapping["sample"], mapping["seed"]
    )
    assert chosen_self == mapping["chosen_self"] and eligible == mapping["eligible_pairs"]
    values, status = [], None
    for line in open(args.solution, encoding="ascii", errors="ignore"):
        if line.startswith("s "): status = line.strip()
        elif line.startswith("v "):
            values.extend(int(token) for token in line.split()[1:] if token != "0")
    assert status and "SATISFIABLE" in status and "UNSATISFIABLE" not in status
    selected_variables = [value for value in values
                          if 1 <= value <= len(eligible)]
    chosen_pairs = [eligible[value-1] for value in selected_variables]
    assert len(chosen_pairs) == 54
    chosen = [self_options[i][1] for i in chosen_self]
    for i in chosen_pairs: chosen.extend(pairs[i][0])
    assert len(chosen) == 143
    loads = [0] * 1430
    for column in chosen:
        for vertex in column["edge"]: loads[vertex] += 1
    assert set(loads) == {1}
    normalized = [
        {"core": tuple(column["core"]),
         "order": tuple(column["order"]),
         "edge": tuple(column["edge"])} for column in chosen
    ]
    rails, owners, point = verify_development(normalized)
    print(json.dumps({
        "status": "PASS", "selected_rail_orbits": 143,
        "selected_self_columns": 35, "selected_paired_configurations": 54,
        "developed_rails": rails, "covered_owners": owners,
        "point_degree": sorted(set(point.values())),
        "certificate": [
            {"core": list(column["core"]),
             "order": list(column["order"]),
             "quotient_edge": list(column["edge"])}
            for column in normalized
        ],
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    builder = sub.add_parser("build")
    builder.add_argument("--map", required=True)
    builder.add_argument("--sample", type=int, default=0)
    builder.add_argument("--seed", type=int, default=20260814)
    builder.add_argument("--cnf", required=True)
    builder.add_argument("--mapping", required=True)
    builder.add_argument("--dlx-instance")
    decoder = sub.add_parser("decode")
    decoder.add_argument("--mapping", required=True)
    decoder.add_argument("--solution", required=True)
    args = parser.parse_args()
    (build if args.command == "build" else decode)(args)


if __name__ == "__main__": main()
