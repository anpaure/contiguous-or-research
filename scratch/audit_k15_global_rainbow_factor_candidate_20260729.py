#!/usr/bin/env python3
"""Fail-closed independent audit for the global rainbow-factor C++ engine.

For a one-component non-loop candidate this also emits the repository's
stable ``graded-quotient-carrier-v1`` format, which is the direct input to
``graded_quotient_pipeline.py compile``.  Multi-component candidates remain
valid exact rainbow 2-factors and are never silently linearized.  They may be
exported explicitly as cyclic components for the separate, exact opening and
seam-ordering models.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path
from typing import Any

from graded_quotient_pipeline import (
    QuotientCatalogue,
    serialize_carrier,
    stable_json,
    validate_carrier,
    validate_cycle_cover,
)


SCHEMA = "global-rainbow-factor-candidate-v1"
AUDIT_SCHEMA = "global-rainbow-factor-independent-audit-v1"


def no_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(), object_pairs_hook=no_duplicate_pairs)
    if type(value) is not dict:
        raise ValueError("candidate must be a JSON object")
    return value


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def physical_shadow_audit(cycles: list[list[int]], k: int, r: int) -> dict[str, int]:
    full = (1 << k) - 1
    got_upper_q1: set[int] = set()
    got_lower_q2: set[int] = set()
    got_upper_q2: set[int] = set()
    upper_q1_labels: Counter[int] = Counter()
    lower_q2_labels: Counter[int] = Counter()
    catalogue = QuotientCatalogue(k)
    for cycle in cycles:
        n = len(cycle)
        for i, value in enumerate(cycle):
            previous = cycle[(i - 1) % n]
            following = cycle[(i + 1) % n]
            upper_q1 = value | following
            lower_q2 = previous & value & following
            upper_q2 = previous | value | following
            if upper_q1.bit_count() == r + 1:
                got_upper_q1.add(upper_q1)
                upper_q1_labels[catalogue.canonical(upper_q1)] += 1
            if lower_q2.bit_count() == r - 2:
                got_lower_q2.add(lower_q2)
                lower_q2_labels[catalogue.canonical(lower_q2)] += 1
            if upper_q2.bit_count() == r + 2:
                got_upper_q2.add(upper_q2)

    if any(value % k for value in upper_q1_labels.values()):
        raise AssertionError("upper-q1 label counts do not descend to quotient")
    if any(value % k for value in lower_q2_labels.values()):
        raise AssertionError("lower-q2 label counts do not descend to quotient")
    upper_pairs = sum((value // k) * (value // k - 1) // 2 for value in upper_q1_labels.values())
    lower_pairs = sum((value // k) * (value // k - 1) // 2 for value in lower_q2_labels.values())
    missing_upper_q1 = {
        mask for mask in range(1, full + 1)
        if mask.bit_count() == r + 1 and mask not in got_upper_q1
    }
    missing_lower_q2 = {
        mask for mask in range(1, full + 1)
        if mask.bit_count() == r - 2 and mask not in got_lower_q2
    }
    missing_upper_q2 = {
        mask for mask in range(1, full + 1)
        if mask.bit_count() == r + 2 and mask not in got_upper_q2
    }
    return {
        "missing_upper_q1_physical": len(missing_upper_q1),
        "missing_lower_q2_physical": len(missing_lower_q2),
        "missing_upper_q2_physical": len(missing_upper_q2),
        "missing_upper_q1_orbits": len({catalogue.canonical(x) for x in missing_upper_q1}),
        "missing_lower_q2_orbits": len({catalogue.canonical(x) for x in missing_lower_q2}),
        "missing_upper_q2_orbits": len({catalogue.canonical(x) for x in missing_upper_q2}),
        "upper_q1_pair_collisions": upper_pairs,
        "lower_q2_pair_collisions": lower_pairs,
        "collision_floor_excess": upper_pairs + lower_pairs - 188,
    }


def residence_audit(cycles: list[list[int]], k: int, required: int) -> dict[str, int]:
    bad = 0
    shortfall = 0
    minimum = max(map(len, cycles)) + 1
    for cycle in cycles:
        n = len(cycle)
        for coordinate in range(k):
            bits = [bool(value & (1 << coordinate)) for value in cycle]
            if not any(bits):
                continue
            if all(bits):
                runs = [n]
            else:
                zero = bits.index(False)
                runs = []
                run = 0
                for step in range(1, n + 1):
                    if bits[(zero + step) % n]:
                        run += 1
                    elif run:
                        runs.append(run)
                        run = 0
            minimum = min(minimum, *runs)
            for run in runs:
                if run < required:
                    bad += 1
                    shortfall += required - run
    return {
        "residence_bad_runs": bad,
        "residence_shortfall": shortfall,
        "minimum_run": minimum,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--carrier-output", type=Path)
    parser.add_argument(
        "--components-output",
        type=Path,
        help=(
            "export the independently reconstructed physical cycles without "
            "choosing cuts, orientations, or seams"
        ),
    )
    args = parser.parse_args()

    payload = load_json(args.candidate)
    if payload.get("schema") != SCHEMA:
        raise ValueError("unsupported candidate schema")
    expected_scalars = {"k": 15, "r": 8, "d": 3, "W": 6435, "N": 429}
    for key, expected in expected_scalars.items():
        if type(payload.get(key)) is not int or payload[key] != expected:
            raise ValueError(f"candidate {key} mismatch")
    choices = payload.get("choices")
    if type(choices) is not list or len(choices) != 429:
        raise ValueError("candidate must contain exactly 429 explicit choices")

    catalogue = QuotientCatalogue(15)
    selected = catalogue.ids_from_explicit(choices)
    # The stable repository catalogue excludes quotient self-loops.  Failure
    # here is deliberate: loop candidates need a separately audited compiler
    # adapter and are never coerced into the non-loop schema.
    cycles, factor_report = validate_cycle_cover(catalogue, selected)
    physical = physical_shadow_audit(cycles, catalogue.k, catalogue.r)
    if physical["collision_floor_excess"] < (
        physical["missing_upper_q1_orbits"] + physical["missing_lower_q2_orbits"]
    ):
        raise AssertionError("collision-floor excess does not dominate quotient holes")
    if physical["collision_floor_excess"] == 0 and (
        physical["missing_upper_q1_orbits"] or physical["missing_lower_q2_orbits"]
    ):
        raise AssertionError("zero collision-floor excess has a shadow hole")
    residence = residence_audit(cycles, catalogue.k, catalogue.d + 1)
    engine = payload.get("exact_audit")
    if type(engine) is not dict:
        raise ValueError("candidate lacks exact_audit")
    required_physical = {
        "missing_upper_q1_physical", "missing_lower_q2_physical",
        "missing_upper_q2_physical", "missing_upper_q1_orbits",
        "missing_lower_q2_orbits", "missing_upper_q2_orbits",
    }
    for key, observed in physical.items():
        if key not in required_physical and key not in engine:
            continue
        if type(engine.get(key)) is not int or engine[key] != observed:
            raise ValueError(f"engine/independent mismatch at {key}: {engine.get(key)} != {observed}")
    comparisons = {
        "physical_cycle_count": len(cycles),
        "quotient_loops": 0,
        **residence,
    }
    for key, observed in comparisons.items():
        if type(engine.get(key)) is not int or engine[key] != observed:
            raise ValueError(f"engine/independent mismatch at {key}: {engine.get(key)} != {observed}")
    if engine.get("fiber_invariant") is not True:
        raise ValueError("engine did not certify its exact fiber invariant")

    carrier_path = None
    carrier_sha256 = None
    components_path = None
    components_sha256 = None
    compiler_eligible = (
        len(cycles) == 1
        and not factor_report["residence_violations"]
        and engine["quotient_loops"] == 0
    )
    if args.carrier_output is not None:
        if not compiler_eligible:
            raise ValueError("refuse compiler export: candidate is not one resident non-loop cycle")
        _cycle, report = validate_carrier(catalogue, selected)
        serialized = serialize_carrier(catalogue, selected, report)
        rendered = json.dumps(serialized, indent=2, sort_keys=True) + "\n"
        args.carrier_output.write_text(rendered)
        # Replay the serialized artifact through the stable explicit choices.
        replay = load_json(args.carrier_output)
        replay_selected = catalogue.ids_from_explicit(replay["choices"])
        replay_cycle, replay_report = validate_carrier(catalogue, replay_selected)
        if replay_cycle != cycles[0] or replay_report != report:
            raise AssertionError("serialized carrier replay changed the candidate")
        carrier_path = str(args.carrier_output)
        carrier_sha256 = digest(args.carrier_output)

    if args.components_output is not None:
        component_payload = {
            "schema": "k15-middle-component-cover-v1",
            "k": catalogue.k,
            "r": catalogue.r,
            "d": catalogue.d,
            "candidate": str(args.candidate),
            "candidate_sha256": digest(args.candidate),
            "choice_table_sha256": catalogue.choice_table_sha256,
            "middle_components": cycles,
            "component_cyclic": [True] * len(cycles),
        }
        args.components_output.write_text(
            json.dumps(component_payload, indent=2, sort_keys=True) + "\n"
        )
        components_path = str(args.components_output)
        components_sha256 = digest(args.components_output)

    audit = {
        "schema": AUDIT_SCHEMA,
        "status": "PASS",
        "candidate": str(args.candidate),
        "candidate_sha256": digest(args.candidate),
        "choice_table_sha256": catalogue.choice_table_sha256,
        "exact_fiber": {
            "lower_colour_orbits": len({catalogue.choices[i].lower for i in selected}),
            "selected_edge_orbits": len(selected),
            "physical_middle_vertices": sum(map(len, cycles)),
            "physical_cycle_count": len(cycles),
            "physical_cycle_lengths": list(map(len, cycles)),
            "degree_histogram": {"2": catalogue.W},
        },
        "physical_shadows": physical,
        "graded_shadows": {
            "lower_q2_missing_orbits": len(factor_report["lower_q2_missing"]),
            "lower_q3_positive_degree_missing_orbits": len(
                factor_report["lower_q3_positive_degree_missing"]
            ),
            "upper_missing_orbits": len(factor_report["upper_missing"]),
            "upper_missing_by_rank": {
                str(rank): count
                for rank, count in sorted(Counter(
                    value.bit_count() for value in factor_report["upper_missing"]
                ).items())
            },
            "carrier_pass_ignoring_connectivity": bool(factor_report["carrier_pass"]),
            "connectivity_pending": bool(factor_report["connectivity_pending"]),
        },
        "residence": residence,
        "compiler_eligible": compiler_eligible,
        "compiler_interface": {
            "command": (
                "python3 scratch/graded_quotient_pipeline.py compile CARRIER "
                "--word WORD --audit AUDIT"
            ),
            "carrier_output": carrier_path,
            "carrier_sha256": carrier_sha256,
            "components_output": components_path,
            "components_sha256": components_sha256,
        },
        "scope": (
            "PASS proves the exact non-loop rainbow 2-factor, physical component, "
            "residence, and q1/q2 counts. It does not prove compiler SAT or full-word coverage."
        ),
    }
    args.audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
