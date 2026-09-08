#!/usr/bin/env python3
"""Build/decode a leaf-specific exact-cover CNF for a removal patch."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)
from search_q4_k17_z17_reflection_sampled_root_direct_patch_20260814 import (
    row_mask,
)


def leaf(instance, incumbent_path, removal_text):
    _, _, self_options, pair_options = read_instance(instance)
    incumbent = json.loads(Path(incumbent_path).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    removal = int(removal_text, 0)
    outside = [0] * 680
    retained_self = set()
    retained_pairs = set()
    for position, vertex in enumerate(vertices):
        if removal >> position & 1:
            continue
        (retained_self if vertex[0] == "self" else retained_pairs).add(vertex[1])
        for row in vertex[3]:
            outside[row] += 1
    if max(outside) > 1:
        raise ValueError("removal is not a defect vertex cover")
    free_rows = tuple(row for row, load in enumerate(outside) if load == 0)
    free_mask = row_mask(free_rows)
    removed = [vertices[position] for position in range(len(vertices))
               if removal >> position & 1]
    removed_groups = tuple(sorted({group for kind, _, group, _ in removed
                                   if kind == "self"}))
    removed_pairs = sum(kind == "pair" for kind, _, _, _ in removed)
    eligible_self = tuple(index for index, (group, rows) in enumerate(self_options)
                          if group in removed_groups
                          and not (row_mask(rows) & ~free_mask))
    eligible_pairs = tuple(index for index, rows in enumerate(pair_options)
                           if not (row_mask(rows) & ~free_mask))
    if len(free_rows) != 4 * len(removed_groups) + 10 * removed_pairs:
        raise ValueError("free-row mass mismatch")
    return (self_options, pair_options, removal, free_rows, removed_groups,
            removed_pairs, eligible_self, eligible_pairs,
            retained_self, retained_pairs)


def build(args):
    (self_options, pair_options, removal, free_rows, removed_groups,
     removed_pairs, eligible_self, eligible_pairs,
     retained_self, retained_pairs) = leaf(
        args.instance, args.incumbent, args.removal_mask)
    self_variable = {index: 1 + local for local, index in enumerate(eligible_self)}
    pair_variable = {index: 1 + len(eligible_self) + local
                     for local, index in enumerate(eligible_pairs)}
    rows = []
    labels = []
    for group in removed_groups:
        rows.append([self_variable[index] for index in eligible_self
                     if self_options[index][0] == group])
        labels.append(f"group:{group}")
    for row in free_rows:
        variables = [self_variable[index] for index in eligible_self
                     if row in self_options[index][1]]
        variables += [pair_variable[index] for index in eligible_pairs
                      if row in pair_options[index]]
        rows.append(variables)
        labels.append(f"row:{row}")
    if not all(rows):
        raise ValueError("structural zero in leaf CNF")
    primary = len(eligible_self) + len(eligible_pairs)
    auxiliary = sum(max(0, len(values) - 1) for values in rows)
    clauses = sum(1 if len(values) == 1 else 3 * len(values) - 3
                  for values in rows)
    next_auxiliary = primary + 1
    with open(args.cnf, "w", encoding="ascii") as stream:
        stream.write(f"p cnf {primary + auxiliary} {clauses}\n")
        for values in rows:
            stream.write(" ".join(map(str, values)) + " 0\n")
            if len(values) == 1:
                continue
            aux = list(range(next_auxiliary,
                             next_auxiliary + len(values) - 1))
            next_auxiliary += len(values) - 1
            stream.write(f"-{values[0]} {aux[0]} 0\n")
            for position in range(1, len(values) - 1):
                current = values[position]
                previous = aux[position - 1]
                following = aux[position]
                stream.write(f"-{current} {following} 0\n")
                stream.write(f"-{previous} {following} 0\n")
                stream.write(f"-{current} -{previous} 0\n")
            stream.write(f"-{values[-1]} -{aux[-1]} 0\n")
    metadata = {
        "status": "BUILT", "instance": args.instance,
        "incumbent": args.incumbent, "removal_mask_hex": hex(removal),
        "free_rows": list(free_rows), "removed_groups": list(removed_groups),
        "removed_pairs": removed_pairs,
        "eligible_self_indices": list(eligible_self),
        "eligible_pair_indices": list(eligible_pairs),
        "retained_self_indices": sorted(retained_self),
        "retained_pair_indices": sorted(retained_pairs),
        "primary_variables": primary, "auxiliary_variables": auxiliary,
        "variables": primary + auxiliary, "clauses": clauses,
        "exact_rows": len(rows), "row_labels": labels,
        "minimum_row_degree": min(map(len, rows)),
        "maximum_row_degree": max(map(len, rows)), "cnf": args.cnf,
    }
    Path(args.metadata).write_text(json.dumps(metadata, indent=2,
                                             sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in metadata.items()
                      if key not in ("eligible_self_indices",
                                     "eligible_pair_indices",
                                     "retained_self_indices",
                                     "retained_pair_indices", "free_rows",
                                     "row_labels")}, indent=2, sort_keys=True))


def decode(args):
    metadata = json.loads(Path(args.metadata).read_text())
    _, _, self_options, pair_options = read_instance(metadata["instance"])
    status = None
    positive = set()
    with open(args.solver_output, encoding="ascii", errors="replace") as stream:
        for line in stream:
            if line.startswith("s "):
                status = line.strip()
            elif line.startswith("v "):
                positive.update(literal for literal in map(int, line.split()[1:])
                                if 0 < literal <= metadata["primary_variables"])
    if status != "s SATISFIABLE":
        raise ValueError(f"solver output is not SAT: {status}")
    self_count = len(metadata["eligible_self_indices"])
    selected_self = set(metadata["retained_self_indices"])
    selected_pairs = set(metadata["retained_pair_indices"])
    for variable in positive:
        if variable <= self_count:
            selected_self.add(metadata["eligible_self_indices"][variable - 1])
        else:
            selected_pairs.add(
                metadata["eligible_pair_indices"][variable - 1 - self_count])
    if len(selected_self) != 35 or len(selected_pairs) != 54:
        raise ValueError("decoded cardinality mismatch")
    if len({self_options[index][0] for index in selected_self}) != 35:
        raise ValueError("decoded self-group mismatch")
    loads = [0] * 680
    for index in selected_self:
        for row in self_options[index][1]: loads[row] += 1
    for index in selected_pairs:
        for row in pair_options[index]: loads[row] += 1
    if set(loads) != {1}:
        raise ValueError("decoded owner exact-cover replay failed")
    state = {"status": "PASS", "energy": 0,
             "self_indices": sorted(selected_self),
             "pair_indices": sorted(selected_pairs),
             "owner_load_histogram": {"1": 680}}
    Path(args.state).write_text(json.dumps(state, indent=2,
                                          sort_keys=True) + "\n")
    print(json.dumps(state, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build")
    builder.add_argument("--instance", required=True)
    builder.add_argument("--incumbent", required=True)
    builder.add_argument("--removal-mask", required=True)
    builder.add_argument("--cnf", required=True)
    builder.add_argument("--metadata", required=True)
    decoder = commands.add_parser("decode")
    decoder.add_argument("--metadata", required=True)
    decoder.add_argument("--solver-output", required=True)
    decoder.add_argument("--state", required=True)
    args = parser.parse_args()
    (build if args.command == "build" else decode)(args)


if __name__ == "__main__":
    main()
