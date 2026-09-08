#!/usr/bin/env python3
"""Build and decode a SAT master for one fixed reflection-matching face.

Run all build, solve, decode, verification, and hashing commands on H100.
The input is the compact instance emitted by
``build_q4_k17_z17_reflection_stochastic_instance_20260814.py``.

There is one primary variable for every self lift and usable reflected
pair.  The exact-cover rows are the 35 self-lift groups followed by the
680 nonfixed owner bracelets.  Every exact-one row uses the linear Sinz
at-most-one encoding plus its at-least-one clause.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_instance(path: str):
    with open(path, encoding="ascii") as stream:
        row_count, group_count, self_count, pair_count = map(
            int, stream.readline().split()
        )
        assert row_count == 680 and group_count == 35
        self_options = []
        pair_options = []
        for _ in range(self_count):
            fields = tuple(map(int, stream.readline().split()))
            assert len(fields) == 5
            group, rows = fields[0], fields[1:]
            assert 0 <= group < group_count
            assert len(set(rows)) == 4
            self_options.append((group, rows))
        for _ in range(pair_count):
            rows = tuple(map(int, stream.readline().split()))
            assert len(rows) == 10 and len(set(rows)) == 10
            pair_options.append(rows)
        assert not stream.read().strip()
    return row_count, group_count, self_options, pair_options


def exact_rows(path: str):
    row_count, group_count, self_options, pair_options = read_instance(path)
    rows = [[] for _ in range(group_count + row_count)]
    for index, (group, owner_rows) in enumerate(self_options):
        variable = 1 + index
        rows[group].append(variable)
        for row in owner_rows:
            rows[group_count + row].append(variable)
    offset = len(self_options)
    for index, owner_rows in enumerate(pair_options):
        variable = 1 + offset + index
        for row in owner_rows:
            rows[group_count + row].append(variable)
    assert all(rows)
    return self_options, pair_options, rows


def build(instance: str, cnf: str, metadata: str) -> None:
    self_options, pair_options, rows = exact_rows(instance)
    primary_count = len(self_options) + len(pair_options)
    auxiliary_count = sum(max(0, len(row) - 1) for row in rows)
    clause_count = sum(1 if len(row) == 1 else 3 * len(row) - 3
                       for row in rows)
    variable_count = primary_count + auxiliary_count

    next_auxiliary = primary_count + 1
    with open(cnf, "w", encoding="ascii") as stream:
        stream.write(f"p cnf {variable_count} {clause_count}\n")
        for variables in rows:
            stream.write(" ".join(map(str, variables)) + " 0\n")
            degree = len(variables)
            if degree == 1:
                continue
            auxiliaries = list(range(next_auxiliary,
                                     next_auxiliary + degree - 1))
            next_auxiliary += degree - 1
            stream.write(f"-{variables[0]} {auxiliaries[0]} 0\n")
            for position in range(1, degree - 1):
                current = variables[position]
                previous_auxiliary = auxiliaries[position - 1]
                current_auxiliary = auxiliaries[position]
                stream.write(f"-{current} {current_auxiliary} 0\n")
                stream.write(
                    f"-{previous_auxiliary} {current_auxiliary} 0\n"
                )
                stream.write(f"-{current} -{previous_auxiliary} 0\n")
            stream.write(f"-{variables[-1]} -{auxiliaries[-1]} 0\n")
    assert next_auxiliary == variable_count + 1

    report = {
        "status": "BUILT",
        "instance": instance,
        "cnf": cnf,
        "exact_rows": len(rows),
        "group_rows": 35,
        "owner_rows": 680,
        "self_variables": len(self_options),
        "pair_variables": len(pair_options),
        "primary_variables": primary_count,
        "auxiliary_variables": auxiliary_count,
        "variables": variable_count,
        "clauses": clause_count,
        "minimum_row_degree": min(map(len, rows)),
        "maximum_row_degree": max(map(len, rows)),
    }
    Path(metadata).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


def decode(instance: str, solver_output: str, state: str) -> None:
    self_options, pair_options, rows = exact_rows(instance)
    primary_count = len(self_options) + len(pair_options)
    status = None
    positive = set()
    with open(solver_output, encoding="ascii", errors="replace") as stream:
        for line in stream:
            if line.startswith("s "):
                status = line.strip()
            elif line.startswith("v "):
                for literal in map(int, line.split()[1:]):
                    if 0 < literal <= primary_count:
                        positive.add(literal)
    assert status == "s SATISFIABLE", status
    selected_self = sorted(
        variable - 1 for variable in positive
        if variable <= len(self_options)
    )
    selected_pairs = sorted(
        variable - 1 - len(self_options) for variable in positive
        if variable > len(self_options)
    )
    assert len(selected_self) == 35
    assert len(selected_pairs) == 54
    assert {self_options[index][0] for index in selected_self} == set(range(35))

    loads = [0] * 680
    for index in selected_self:
        for row in self_options[index][1]:
            loads[row] += 1
    for index in selected_pairs:
        for row in pair_options[index]:
            loads[row] += 1
    assert set(loads) == {1}
    report = {
        "status": "PASS",
        "energy": 0,
        "selected_self_columns": len(selected_self),
        "selected_paired_configurations": len(selected_pairs),
        "owner_load_histogram": {"1": 680},
        "self_indices": selected_self,
        "pair_indices": selected_pairs,
    }
    Path(state).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    builder = subparsers.add_parser("build")
    builder.add_argument("--instance", required=True)
    builder.add_argument("--cnf", required=True)
    builder.add_argument("--metadata", required=True)
    decoder = subparsers.add_parser("decode")
    decoder.add_argument("--instance", required=True)
    decoder.add_argument("--solver-output", required=True)
    decoder.add_argument("--state", required=True)
    args = parser.parse_args()
    if args.command == "build":
        build(args.instance, args.cnf, args.metadata)
    else:
        decode(args.instance, args.solver_output, args.state)


if __name__ == "__main__":
    main()
