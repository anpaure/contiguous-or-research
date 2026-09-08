#!/usr/bin/env python3
"""Append targeted reflected-pair witnesses to the sample-0 owner face.

Run substantive commands only on H100.  Input catalogues use the TSV
schema emitted by ``search_q4_k17_owner_targeted_reflection_pairs``:
rows, core, order, owner_ids, status.  The first physical column is stored
literally; its reflected mate is obtained by multiplication by -1.  Build
and decode use the same deterministic deduplication order.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import (
    make_instance,
)
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
    verify_development,
)
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    reflection_action,
)


def values(field):
    return tuple(map(int, field.split(',')))


def reflected_candidate(candidate, orbit_index):
    core = tuple(sorted((-value) % K for value in candidate["core"]))
    order = tuple((-value) % K for value in candidate["order"])
    edge = tuple(sorted(
        orbit_index[canonical_orbit_mask(owner)]
        for owner in deck_masks(core, order)
    ))
    return {"core": core, "order": order, "edge": edge}


def load_augmented(catalogues, base_pair_rows, limit):
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    fixed = {vertex for vertex in range(1430) if reflection[vertex] == vertex}
    nonfixed_representatives = sorted(
        vertex for vertex in range(1430) if vertex < reflection[vertex]
    )
    reduced_index = {}
    for row, vertex in enumerate(nonfixed_representatives):
        reduced_index[vertex] = row
        reduced_index[reflection[vertex]] = row

    seen = set(map(tuple, base_pair_rows))
    augmented = []
    status_counts = {}
    for path in catalogues:
        with open(path, encoding="ascii", newline='') as stream:
            reader = csv.DictReader(stream, delimiter='\t')
            assert {"rows", "core", "order", "owner_ids"} <= set(
                reader.fieldnames or ()
            )
            for record in reader:
                label = record.get("status") or record.get("tier") or "catalogue"
                status_counts[label] = status_counts.get(label, 0) + 1
                if record.get("status") not in (None, "", "new"):
                    continue
                rows = tuple(sorted(values(record["rows"])))
                if len(rows) != 10 or len(set(rows)) != 10 or rows in seen:
                    continue
                core = tuple(sorted(values(record["core"])))
                order = values(record["order"])
                owner_ids = values(record["owner_ids"])
                assert len(core) == 5 and len(order) == len(owner_ids) == 10
                assert len(set(core)) == 5 and len(set(order)) == 10
                assert not (set(core) & set(order))
                edge_in_order = tuple(
                    orbit_index[canonical_orbit_mask(owner)]
                    for owner in deck_masks(core, order)
                )
                assert edge_in_order == owner_ids
                edge = tuple(sorted(edge_in_order))
                reflected_edge = tuple(sorted(reflection[vertex]
                                              for vertex in edge))
                assert not (set(edge) & set(reflected_edge))
                assert not ((set(edge) | set(reflected_edge)) & fixed)
                reconstructed_rows = tuple(sorted({
                    reduced_index[vertex]
                    for vertex in set(edge) | set(reflected_edge)
                }))
                assert reconstructed_rows == rows
                first = {"core": core, "order": order, "edge": edge}
                second = reflected_candidate(first, orbit_index)
                assert second["edge"] == reflected_edge
                if record.get("reflected_core"):
                    assert tuple(sorted(values(record["reflected_core"]))) == second["core"]
                if record.get("reflected_order"):
                    assert values(record["reflected_order"]) == second["order"]
                if record.get("reflected_owner_ids"):
                    assert tuple(sorted(values(record["reflected_owner_ids"]))) == second["edge"]
                seen.add(rows)
                augmented.append(([first, second], rows, path))
                if limit and len(augmented) >= limit:
                    return augmented, status_counts
    return augmented, status_counts


def build(args):
    _, _, base_self, base_pairs = read_instance(args.base_instance)
    augmented, status_counts = load_augmented(
        args.catalog, base_pairs, args.limit
    )
    with open(args.instance, "w", encoding="ascii") as stream:
        stream.write(
            f"680 35 {len(base_self)} {len(base_pairs) + len(augmented)}\n"
        )
        for group, rows in base_self:
            stream.write(" ".join(map(str, (group,) + rows)) + "\n")
        for rows in base_pairs:
            stream.write(" ".join(map(str, rows)) + "\n")
        for _, rows, _ in augmented:
            stream.write(" ".join(map(str, rows)) + "\n")
    print(json.dumps({
        "status": "BUILT",
        "base_instance": args.base_instance,
        "instance": args.instance,
        "catalogues": args.catalog,
        "catalogue_status_counts_until_limit": status_counts,
        "self_options": len(base_self),
        "base_pair_options": len(base_pairs),
        "augmented_pair_options": len(augmented),
        "total_pair_options": len(base_pairs) + len(augmented),
        "limit": args.limit,
    }, indent=2, sort_keys=True))


def decode(args):
    _, self_options, pair_options = make_instance(
        args.map, args.sample, args.seed
    )
    base_pair_rows = [rows for _, rows in pair_options]
    augmented, _ = load_augmented(args.catalog, base_pair_rows, args.limit)
    state = json.load(open(args.solution, encoding="utf-8"))
    assert state["energy"] == 0
    chosen_self = state["self_indices"]
    chosen_pairs = state["pair_indices"]
    assert len(chosen_self) == 35 and len(chosen_pairs) == 54
    chosen = [self_options[index][1] for index in chosen_self]
    for index in chosen_pairs:
        if index < len(pair_options):
            chosen.extend(pair_options[index][0])
        else:
            chosen.extend(augmented[index - len(pair_options)][0])
    assert len(chosen) == 143
    loads = [0] * 1430
    for column in chosen:
        for vertex in column["edge"]:
            loads[vertex] += 1
    assert set(loads) == {1}
    normalized = [
        {"core": tuple(column["core"]),
         "order": tuple(column["order"]),
         "edge": tuple(column["edge"])}
        for column in chosen
    ]
    rails, owners, point = verify_development(normalized)
    print(json.dumps({
        "status": "PASS",
        "selected_rail_orbits": len(chosen),
        "selected_self_columns": 35,
        "selected_paired_configurations": 54,
        "selected_augmented_pairs": sum(
            index >= len(pair_options) for index in chosen_pairs
        ),
        "developed_rails": rails,
        "covered_owners": owners,
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
    subparsers = parser.add_subparsers(dest="command", required=True)
    builder = subparsers.add_parser("build")
    builder.add_argument("--base-instance", required=True)
    builder.add_argument("--instance", required=True)
    decoder = subparsers.add_parser("decode")
    decoder.add_argument("--map", required=True)
    decoder.add_argument("--sample", type=int, default=0)
    decoder.add_argument("--seed", type=int, default=20260814)
    decoder.add_argument("--solution", required=True)
    for subparser in (builder, decoder):
        subparser.add_argument("--catalog", action="append", required=True)
        subparser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    (build if args.command == "build" else decode)(args)


if __name__ == "__main__":
    main()
