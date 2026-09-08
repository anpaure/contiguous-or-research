#!/usr/bin/env python3
"""Hostile replay of the frozen D5 reset-phase spanning-bank certificate.

Substantive execution belongs on H100.  This audit does not trust candidate
indices in the selector output.  It matches every literal selected circuit
against the independently enumerated menu for its prefix phase, checks the
strict-shorter q2-safe counts, verifies the three inclusion-minimal resource
cores recorded along the iterative reset search, and binds all inputs by
SHA-256.  Full incidence, q2, component, and residence replay is deliberately
left to ``verify_t2_suffix_d5_split_tree_selection_20260814.py``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


P0 = "101010001101"
P1 = "100011001101"
MINIMUM_PREFIXES = {"101001010101", "101001001101"}
P1_FILES = {
    3: "d5_fourthphase_cap512_3.out",
    6: "d5_fourthphase_6.out",
    11: "d5_fourthphase_11.out",
    17: "d5_fourthphase_cap512_17.out",
    18: "d5_fourthphase_cap512_18.out",
    23: "d5_fourthphase_23.out",
    28: "d5_fourthphase_28.out",
    29: "d5_fourthphase_29.out",
    33: "d5_fourthphase_33.out",
}


def read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def signature(candidate):
    return tuple(candidate["owners"]), tuple(candidate["new_colours"])


def strict_shorter_safe_count(prefix_row):
    solution = prefix_row["shortest_q2_safe_incidence_length"]
    return sum(
        row["q2_safe_cycles"]
        for row in prefix_row["length_reports"]
        if row["incidence_length"] < solution
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default=".")
    parser.add_argument(
        "--menu-bundle",
        default="t2_suffix_d5_reset_menu_bundle_20260814.h100.out",
    )
    args = parser.parse_args()
    directory = Path(args.directory)

    selector_path = directory / "solve_t2_suffix_d5_topology_cegar_20260814.h100.out"
    verifier_path = directory / "verify_t2_suffix_d5_topology_cegar_selection_20260814.h100.out"
    selector, selector_hash = read(selector_path)
    verifier, verifier_hash = read(verifier_path)
    bundle_path = directory / args.menu_bundle
    bundle, bundle_hash = read(bundle_path)
    assert bundle["status"] == "PASS" and bundle["menu_files"] == 115
    assert selector["status"] == "SAT"
    assert verifier["status"] == "PASS"
    assert verifier["selection_sha256"] == selector_hash
    assert len(selector["selection"]) == 41

    hashes = {
        selector_path.name: selector_hash,
        verifier_path.name: verifier_hash,
        bundle_path.name: bundle_hash,
    }

    def bundled_menu(name):
        entry = bundle["files"][name]
        return entry["data"], entry["sha256"]

    menu_matches = Counter()
    selected_p1_edges = []
    for item in selector["selection"]:
        edge_index = item["edge_index"]
        candidate = item["candidate"]
        prefix = candidate["prefix"]
        wanted = signature(candidate)
        if prefix in MINIMUM_PREFIXES:
            name = f"d5_minimum_candidates_{edge_index}.out"
            menu, digest = bundled_menu(name)
            assert item["selected_incidence_length"] == menu[
                "minimum_incidence_length"
            ]
            assert wanted in {signature(row) for row in menu["candidates"]}
            menu_matches["all-prefix global minimum"] += 1
        elif prefix == P0:
            name = f"d5_thirdphase_all_{edge_index}.out"
            menu, digest = bundled_menu(name)
            assert len(menu["prefixes"]) == 1
            row = menu["prefixes"][0]
            assert row["prefix"] == P0
            assert strict_shorter_safe_count(row) == 0
            assert item["selected_incidence_length"] == row[
                "shortest_q2_safe_incidence_length"
            ]
            assert wanted in {signature(x) for x in row["candidates"]}
            menu_matches["reset phase P0"] += 1
        elif prefix == P1:
            assert edge_index in P1_FILES
            selected_p1_edges.append(edge_index)
            name = P1_FILES[edge_index]
            menu, digest = bundled_menu(name)
            assert len(menu["prefixes"]) == 1
            row = menu["prefixes"][0]
            assert row["prefix"] == P1
            assert strict_shorter_safe_count(row) == 0
            assert item["selected_incidence_length"] == row[
                "shortest_q2_safe_incidence_length"
            ]
            assert wanted in {signature(x) for x in row["candidates"]}
            assert row.get(
                "candidate_enumeration_complete_at_solution", True
            )
            menu_matches["reset phase P1"] += 1
        else:
            raise AssertionError((edge_index, prefix))
        hashes[name] = digest

    assert sorted(selected_p1_edges) == sorted(P1_FILES)
    assert menu_matches == Counter({
        "all-prefix global minimum": 22,
        "reset phase P0": 10,
        "reset phase P1": 9,
    })

    core_specs = [
        (
            "solve_t2_suffix_d5_split_tree_minimum_sdr_20260814.h100.out",
            [35, 38, 39],
        ),
        (
            "solve_t2_suffix_d5_split_tree_optimized_threephase_sdr_20260814.h100.out",
            [22, 27, 33, 37],
        ),
        (
            "solve_t2_suffix_d5_split_tree_fourphase_trial2_20260814.h100.out",
            [7, 11, 13, 22, 23, 27, 28, 29, 33, 35, 37, 38, 39, 40],
        ),
        (
            "solve_t2_suffix_d5_split_tree_iter3_resource_core_20260814.h100.out",
            [1, 17, 18, 21],
        ),
    ]
    cores = {}
    for name, expected in core_specs:
        path = directory / name
        data, digest = read(path)
        assert data["status"] == "UNSAT"
        actual = [row["edge_index"] for row in data["minimal_unsat_core"]]
        assert actual == expected
        assert data.get("unsat_core_inclusion_minimal", True)
        hashes[name] = digest
        cores[name] = {
            "edge_indices": actual,
            "role_histogram": data["core_role_histogram"],
            "split_histogram": data["core_split_histogram"],
        }

    assert selector["rejected_model_count"] == 7
    assert selector["simultaneous"]["q2_support_losses"] == 0
    assert selector["simultaneous"]["output_components_on_touched_owners"] == 1
    assert verifier["simultaneous"]["spanning_gate"]
    assert not verifier["simultaneous"][
        "undilated_two_shore_residence_gate"
    ]

    print(json.dumps({
        "status": "PASS",
        "selector_sha256": selector_hash,
        "verifier_sha256": verifier_hash,
        "menu_bundle_sha256": bundle_hash,
        "menu_matches": dict(sorted(menu_matches.items())),
        "selected_p1_edges": sorted(selected_p1_edges),
        "selected_prefix_histogram": verifier["selected_prefix_histogram"],
        "selected_length_histogram": verifier["selected_length_histogram"],
        "iterative_inclusion_minimal_cores": cores,
        "topology_rejected_models": selector["rejected_model_count"],
        "simultaneous": verifier["simultaneous"],
        "input_sha256": dict(sorted(hashes.items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
