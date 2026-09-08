#!/usr/bin/env python3
"""Build/decode the certified 8-nondihedral + 27-strong owner face.

Run substantive commands only on H100.  Eight quotient-self owner decks
from the complete fixed-lower catalogue are forced, one per new
Johnson-distance-one fixed edge.  Their 16 endpoints are deleted, and the
certified 27-edge matching completion uses every strong-self lift above
each remaining edge.  Frozen reflected pair configurations complete the
same 680-row nonfixed bracelet master.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    owner_orbits,
    verify_development,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    enumerate_strong_self_columns,
    paired_columns,
    reflection_action,
)


def multiplied_candidate(row, multiplier, orbit_index):
    core = tuple(sorted(multiplier * value % K for value in row["core"]))
    order = tuple(multiplier * value % K for value in row["order"])
    edge = tuple(sorted(
        orbit_index[canonical_orbit_mask(owner)]
        for owner in deck_masks(core, order)
    ))
    assert len(set(edge)) == 10
    return {"core": core, "order": order, "edge": edge}


def make_instance(map_path, primary_path, audit_path):
    pool = json.load(open(map_path, encoding="utf-8"))
    primary = json.load(open(primary_path, encoding="utf-8"))
    audit = json.load(open(audit_path, encoding="utf-8"))
    assert primary["status"] == audit["status"] == "PASS"
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    fixed = {vertex for vertex in range(1430)
             if reflection[vertex] == vertex}
    nonfixed_representatives = sorted(
        vertex for vertex in range(1430) if vertex < reflection[vertex]
    )
    nonfixed_index = {}
    for index, vertex in enumerate(nonfixed_representatives):
        nonfixed_index[vertex] = index
        nonfixed_index[reflection[vertex]] = index
    assert len(nonfixed_representatives) == 680

    # Multiplier development has 16 typed columns but eight owner decks.
    # Keep one literal core/order representative per owner deck; the other
    # lower realization is deferred because this is the owner-only face.
    nondihedral_by_deck = {}
    for row in primary["examples"]:
        for multiplier in range(1, K):
            candidate = multiplied_candidate(row, multiplier, orbit_index)
            reflected = tuple(sorted(reflection[vertex]
                                     for vertex in candidate["edge"]))
            assert reflected == candidate["edge"]
            nondihedral_by_deck.setdefault(candidate["edge"], candidate)
    assert len(nondihedral_by_deck) == 8
    nondihedral_by_signature = {}
    for candidate in nondihedral_by_deck.values():
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        assert len(signature) == 2
        rows = tuple(sorted({nonfixed_index[vertex]
                             for vertex in candidate["edge"]
                             if vertex not in fixed}))
        assert len(rows) == 4
        nondihedral_by_signature[signature] = (candidate, rows)
    expected_new = {
        tuple(edge) for edge in
        audit["new_fixed_face_completion"]["new_nondihedral_edges"]
    }
    assert set(nondihedral_by_signature) == expected_new

    strong_candidates, raw, quotient_simple = enumerate_strong_self_columns(
        orbit_index, reflection
    )
    strong_lifts = defaultdict(list)
    for candidate in strong_candidates:
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        assert len(signature) == 2
        rows = tuple(sorted({nonfixed_index[vertex]
                             for vertex in candidate["edge"]
                             if vertex not in fixed}))
        assert len(rows) == 4
        strong_lifts[signature].append((candidate, rows))
    completion = {
        tuple(edge) for edge in
        audit["new_fixed_face_completion"]["strong_completion_matching"]
    }
    assert len(completion) == 27
    combined = expected_new | completion
    assert len(combined) == 35
    assert len({vertex for edge in combined for vertex in edge}) == 70

    groups = []
    for signature in sorted(expected_new):
        candidate, rows = nondihedral_by_signature[signature]
        groups.append({
            "kind": "nondihedral", "signature": signature,
            "options": [(candidate, rows)],
        })
    for signature in sorted(completion):
        assert signature in strong_lifts
        groups.append({
            "kind": "strong", "signature": signature,
            "options": strong_lifts[signature],
        })
    assert len(groups) == 35

    self_options = []
    for group, record in enumerate(groups):
        for candidate, rows in record["options"]:
            self_options.append((group, candidate, rows))

    pair_options = []
    pair_indices, pool_self = paired_columns(pool["candidates"], reflection)
    assert not pool_self and len(pair_indices) == 27008
    for left, right in pair_indices:
        columns = [pool["candidates"][left], pool["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        assert len(union) == 20 and not (union & fixed)
        rows = tuple(sorted({nonfixed_index[vertex] for vertex in union}))
        assert len(rows) == 10
        pair_options.append((columns, rows))
    report = {
        "status": "BUILT",
        "new_nondihedral_groups": 8,
        "strong_groups": 27,
        "strong_raw_orders": raw,
        "strong_quotient_simple_orders": quotient_simple,
        "self_options": len(self_options),
        "nondihedral_self_options": sum(
            groups[group]["kind"] == "nondihedral"
            for group, _, _ in self_options
        ),
        "strong_self_options": sum(
            groups[group]["kind"] == "strong"
            for group, _, _ in self_options
        ),
        "pair_options": len(pair_options),
        "matching": [list(record["signature"]) for record in groups],
        "group_kinds": [record["kind"] for record in groups],
    }
    return groups, self_options, pair_options, report


def build(args):
    _, self_options, pair_options, report = make_instance(
        args.map, args.primary, args.audit
    )
    with open(args.instance, "w", encoding="ascii") as stream:
        stream.write(f"680 35 {len(self_options)} {len(pair_options)}\n")
        for group, _, rows in self_options:
            stream.write(" ".join(map(str, (group,) + rows)) + "\n")
        for _, rows in pair_options:
            stream.write(" ".join(map(str, rows)) + "\n")
    report["instance"] = args.instance
    print(json.dumps(report, indent=2, sort_keys=True))


def decode(args):
    groups, self_options, pair_options, build_report = make_instance(
        args.map, args.primary, args.audit
    )
    state = json.load(open(args.solution, encoding="utf-8"))
    assert state["energy"] == 0
    selected_self = state["self_indices"]
    selected_pairs = state["pair_indices"]
    assert len(selected_self) == 35 and len(selected_pairs) == 54
    assert {self_options[index][0] for index in selected_self} == set(range(35))
    chosen = [self_options[index][1] for index in selected_self]
    for index in selected_pairs:
        chosen.extend(pair_options[index][0])
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
    report = {
        "status": "PASS",
        "selected_rail_orbits": len(chosen),
        "selected_nondihedral_self_columns": 8,
        "selected_strong_self_columns": 27,
        "selected_paired_configurations": 54,
        "developed_rails": rails,
        "covered_owners": owners,
        "point_degree": sorted(set(point.values())),
        "matching": build_report["matching"],
        "group_kinds": build_report["group_kinds"],
        "certificate": [
            {"core": list(column["core"]),
             "order": list(column["order"]),
             "quotient_edge": list(column["edge"])}
            for column in normalized
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("build", "decode"):
        subparser = subparsers.add_parser(name)
        subparser.add_argument("--map", required=True)
        subparser.add_argument("--primary", required=True)
        subparser.add_argument("--audit", required=True)
        if name == "build":
            subparser.add_argument("--instance", required=True)
        else:
            subparser.add_argument("--solution", required=True)
    args = parser.parse_args()
    (build if args.command == "build" else decode)(args)


if __name__ == "__main__":
    main()
