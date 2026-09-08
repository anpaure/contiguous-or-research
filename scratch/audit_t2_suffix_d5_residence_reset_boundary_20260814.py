#!/usr/bin/env python3
"""Hostile aggregate audit of the frozen D5 residence/reset boundary.

Substantive execution belongs on H100.  This audit consumes the independent
finite replays rather than rebuilding their SAT instances.  It pins their
digests, cross-checks all theorem-facing counts, and rejects any accidental
promotion of the static dilation or conditional three-state gate to a
dynamic residence construction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("provenance")
    parser.add_argument("static_dilation")
    parser.add_argument("state_certificate")
    parser.add_argument("successor_tag")
    parser.add_argument("tag_core")
    parser.add_argument("tag_core_audit")
    parser.add_argument("three_state_audit")
    args = parser.parse_args()
    paths = {key: Path(value) for key, value in vars(args).items()}
    data = {key: load(path) for key, path in paths.items()}
    hashes = {key: digest(path) for key, path in paths.items()}
    selection_sha = hashes["selection"]
    assert selection_sha == (
        "94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32"
    )

    provenance = data["provenance"]
    assert provenance["status"] == "PASS"
    assert provenance["selection_sha256"] == selection_sha
    upper = provenance["shores"]["upper"]
    lower = provenance["shores"]["lower"]
    assert (
        upper["before_bad_windows"],
        upper["after_bad_windows"],
        upper["new_collision_events"],
        upper["literal_inherited_events_retained"],
        upper["resolved_collision_events"],
    ) == (84, 244, 208, 36, 48)
    assert (
        lower["before_bad_windows"],
        lower["after_bad_windows"],
        lower["new_collision_events"],
        lower["literal_inherited_events_retained"],
        lower["resolved_collision_events"],
    ) == (126, 240, 165, 75, 51)

    static = data["static_dilation"]
    assert static["status"] == "PASS"
    assert static["selection_sha256"] == selection_sha
    assert static["scope"] == (
        "static post-switch dilation; no dynamic switch lift"
    )
    assert static["original_touched_output_owner_length"] == 12420
    assert static["expanded_owner_length"] == 37260
    assert static["component_count_on_dilated_touched_bank"] == 1
    assert static["lower_minimum_positive_zero_runs"] == [3, 3]
    assert static["upper_minimum_positive_zero_runs"] == [4, 2]
    assert static["expanded_owner_simple"]
    assert static["expanded_immediate_upper_q1_simple"]
    assert not static["expanded_immediate_lower_colour_distinct"]
    assert static["minimum_run_witnesses"]["upper_zero"]["coordinate"] == 23
    assert static["fresh_coordinate_classes"]["23"] == "p0"

    state = data["state_certificate"]
    assert state["status"] == "PASS"
    assert state["selection_sha256"] == selection_sha
    assert state["odd_touched_components"] == 372
    assert not state["two_phase_cycle_alternation_possible"]
    assert state["orientation_xor"]["status"] == "UNSAT"
    assert state["orientation_xor"]["minimum_inconsistent_cycle_size"] == 2
    graph = state["owner_union_graph"]
    assert graph["vertices"] == 12420
    assert graph["union_edges"] == 12897
    assert graph["minimum_history_states"] == 3
    assert graph["selected_pass_rows"] == 265
    assert graph["selected_nontrivial_reset_rows"] == 212
    assert graph["unoriented_nontrivial_reset_template_types"] == 3

    tag = data["successor_tag"]
    assert tag["status"] == "BOUNDED_TAG_FAILURE"
    assert tag["selection_sha256"] == selection_sha
    assert len(tag["solver_trials"]) == 16
    assert all(row["status"] == "UNSAT" for row in tag["solver_trials"])
    assert {row["post_reverse"] for row in tag["solver_trials"]} == {0, 1}
    assert [row["status"] for row in tag["unrestricted_quotient_tests"]] == [
        "UNSAT", "UNSAT"
    ]
    assert all(
        row["tag_bits"] == 14 for row in tag["unrestricted_quotient_tests"]
    )

    core = data["tag_core"]
    core_audit = data["tag_core_audit"]
    assert core["status"] == core_audit["status"] == "PASS"
    assert core["selection_sha256"] == selection_sha
    assert core_audit["selection_sha256"] == selection_sha
    assert core_audit["core_sha256"] == hashes["tag_core"]
    replay = core_audit["solver_free_quotient_replay"]
    assert [(row["owner_equations"], row["pre_components"]) for row in replay] == [
        (86, 4), (96, 5)
    ]
    assert [row["orientations_tested"] for row in replay] == [16, 32]
    assert all(row["all_orientations_have_quotient_loop"] for row in replay)
    assert all(row["inclusion_minimal"] for row in replay)
    assert [
        row["single_deletions_with_loop_free_orientation"] for row in replay
    ] == [86, 96]

    three = data["three_state_audit"]
    assert three["status"] == "PASS"
    assert three["selection_sha256"] == selection_sha
    assert three["certificate_sha256"] == hashes["state_certificate"]
    assert three["union_graph_chromatic_number"] == 3
    assert three["old_component_length_histogram"] == {"23": 330, "115": 42}
    assert three["selected_pass_rows"] == 265
    assert three["selected_nontrivial_reset_rows"] == 212

    print(json.dumps({
        "status": "PASS",
        "artifact_sha256": hashes,
        "verdicts": {
            "new_upper_collision_events": 208,
            "new_lower_collision_events": 165,
            "static_four_clock_residence": "PASS",
            "static_is_dynamic_switch_lift": False,
            "two_history_common_phase": "UNSAT",
            "unrestricted_variable_successor_tag": "UNSAT",
            "old_new_union_chromatic_number": 3,
            "selected_nontrivial_three_state_resets": 212,
            "three_state_reset_cell_constructed": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
