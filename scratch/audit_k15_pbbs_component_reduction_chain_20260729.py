#!/usr/bin/env python3
"""Independent replay of the exact PBBS fixed-M0 9->4->3->2 chain."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import audit_k15_double_shadow_markov_cycles_20260729 as core  # noqa: E402
from graded_quotient_pipeline import QuotientCatalogue, validate_cycle_cover  # noqa: E402


ROOT = HERE.parent
DATA = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729"
MAP = DATA / "seed0.mapping.json"

STAGES = [
    (
        "u2u3l3_s801.engine.json",
        "886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83",
        [1890, 774, 774, 774, 774, 774, 555, 75, 45],
    ),
    (
        "s801_markov_s5.best.json",
        "8e1af84ce459f825f6c4f41fcb8dce00bc40d8b40c1515dfef4741ac9668240d",
        [5715, 600, 75, 45],
    ),
    (
        "from4_markov_s7_merge.best.json",
        "ad4cada7a193acaf275349ec90ab264178cb9106277b29e5a3d38c4b658e5b3d",
        [5790, 600, 45],
    ),
    (
        "from3_markov_s7_merge.best.json",
        "0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555",
        [6390, 45],
    ),
]

SEPARATION = {
    "atlas": (
        "from2_markov_s8_merge.audit.json",
        "0d0419dfa6cc1fc1d111e90fe09df50783fb99f52b2e0aee482952b35d71d2f7",
    ),
    "packet4": (
        "from2_packet4.audit.json",
        "eabcdbdcc3bf11b113234173ae54f10c2aa459d1f9b92d3db4920a0a3f2b122c",
    ),
    "packet5": (
        "from2_packet5.audit.json",
        "bafd5a2b963aa508424af5f23346ce2a458c2d0ab87ec04556bc49b7e18c63cb",
    ),
    "packet6": (
        "from2_packet6.audit.json",
        "b6aacf3bc9f40e842efe485b6576c5ec06e83cca4fdbb50e1b8064431dde44f6",
    ),
    "neutral": (
        "from2_markov_s5_neutral.audit.json",
        "db103b3024778de7ba154163f9ab276af5b80f62df36eef2052ca4740f81f0ac",
    ),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text())
    if type(value) is not dict:
        raise ValueError(f"{path}: expected object")
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def exchange_cycle(
    source: list[int], target: list[int], annotations: dict[int, dict]
) -> dict:
    changed = [row for row in range(len(source)) if source[row] != target[row]]
    inverse = {int(annotations[var]["v"]): row for row, var in enumerate(source)}
    successor = {
        row: inverse[int(annotations[target[row]]["v"])] for row in changed
    }
    require(set(successor.values()) == set(changed), "exchange support is not closed")
    cycles = []
    seen = set()
    for start in changed:
        if start in seen:
            continue
        row = []
        current = start
        while current not in seen:
            seen.add(current)
            row.append(current)
            current = successor[current]
        cycles.append(row)
    require(len(cycles) == 1, "stage difference is not one alternating cycle")
    colour_delta = {}
    for name in ("upper_q1", "lower_q2"):
        delta = Counter(annotations[target[row]][name] for row in changed)
        delta.subtract(annotations[source[row]][name] for row in changed)
        colour_delta[name] = {str(k): v for k, v in sorted(delta.items()) if v}
    return {
        "support": len(changed),
        "rows_sorted": changed,
        "cycle_order": cycles[0],
        "removed_variables": [source[row] for row in cycles[0]],
        "added_variables": [target[row] for row in cycles[0]],
        "colour_delta": colour_delta,
    }


def fixed_window_tower(cycles: list[list[int]]) -> dict[str, dict[str, int]]:
    full = (1 << 15) - 1
    report = {}
    for depth in range(1, 8):
        lower = set()
        upper = set()
        for cycle in cycles:
            n = len(cycle)
            for start in range(n):
                lo, up = full, 0
                for offset in range(depth + 1):
                    value = cycle[(start + offset) % n]
                    lo &= value
                    up |= value
                if lo.bit_count() == 8 - depth:
                    lower.add(lo)
                if up.bit_count() == 8 + depth:
                    upper.add(up)
        lower_target = len(catalogue_rank_masks(8 - depth))
        upper_target = len(catalogue_rank_masks(8 + depth))
        report[str(depth)] = {
            "lower_missing_physical": lower_target - len(lower),
            "upper_missing_physical": upper_target - len(upper),
        }
    return report


def catalogue_rank_masks(rank: int) -> list[int]:
    return [value for value in range(1 << 15) if value.bit_count() == rank]


def main() -> int:
    mapping = core.load_json(MAP)
    catalogue = QuotientCatalogue(15)
    stage_rows = []
    selections = []
    annotations = None
    base_m0 = None
    for name, expected_sha, expected_lengths in STAGES:
        path = DATA / name
        require(digest(path) == expected_sha, f"stage hash mismatch: {name}")
        candidate = core.load_json(path)
        selected, current_annotations, current_m0 = core.reconstruct_matching(
            mapping, candidate
        )
        if annotations is None:
            annotations, base_m0 = current_annotations, current_m0
        else:
            require(current_annotations == annotations, "annotation map changed")
            require(current_m0 == base_m0, "M0 changed")
        metrics, _ = core.evaluate_matching(
            catalogue, mapping, selected, current_annotations, current_m0
        )
        require(metrics["component_lengths"] == expected_lengths, f"component ledger: {name}")
        require(metrics["residence"]["residence_shortfall"] == 0, f"residence: {name}")
        require(metrics["carrier_gates"]["pass_ignoring_connectivity"], f"carrier gate: {name}")
        require(metrics["all_depth_holes_physical_total"] == 0, f"all-depth gate: {name}")
        cycles, authoritative = validate_cycle_cover(
            catalogue, catalogue.ids_from_explicit(candidate["choices"])
        )
        require(list(map(len, cycles)) == expected_lengths, f"physical replay: {name}")
        require(authoritative["carrier_pass"], f"authoritative carrier replay: {name}")
        fixed_tower = fixed_window_tower(cycles)
        require(
            all(
                row["lower_missing_physical"] == 0
                and row["upper_missing_physical"] == 0
                for row in fixed_tower.values()
            ),
            f"fixed-window tower: {name}",
        )
        stage_rows.append({
            "file": str(path),
            "sha256": expected_sha,
            "physical_component_lengths": expected_lengths,
            "quotient_lift_profile": metrics["quotient_lift_profile"],
            "residence": metrics["residence"],
            "carrier_gates": metrics["carrier_gates"],
            "bilateral_all_depth_holes_physical": metrics[
                "all_depth_holes_physical_total"
            ],
            "fixed_window_tower": fixed_tower,
            "collision_floor_excess": metrics["shadows"]["collision_floor_excess"],
        })
        selections.append(selected)

    require(annotations is not None and base_m0 is not None, "no stages")
    exchanges = []
    expected_supports = [4, 6, 4]
    for index in range(3):
        row = exchange_cycle(selections[index], selections[index + 1], annotations)
        require(row["support"] == expected_supports[index], "switch support changed")
        require(not row["colour_delta"]["upper_q1"], "upper-q1 delta is nonzero")
        require(not row["colour_delta"]["lower_q2"], "lower-q2 delta is nonzero")
        exchanges.append(row)

    separation_rows = {}
    for key, (name, expected_sha) in SEPARATION.items():
        path = DATA / name
        require(digest(path) == expected_sha, f"separation hash mismatch: {name}")
        separation_rows[key] = {
            "file": str(path),
            "sha256": expected_sha,
            "payload": load(path),
        }
    atlas = separation_rows["atlas"]["payload"]
    require(atlas["candidate_sha256"] == STAGES[-1][1], "atlas source mismatch")
    require(atlas["max_support"] == 8, "atlas radius mismatch")
    require(atlas["deck_safe_cycles"] == 11518, "deck-safe census changed")
    require(atlas["topology_rejected_cycles"] == 11518, "topology census changed")
    require(atlas["physically_evaluated_cycles"] == 0, "unexpected topology survivor")
    packet6 = separation_rows["packet6"]["payload"]
    require(packet6["counters"]["pairs"] == 52998660, "packet-pair census changed")
    require(packet6["counters"]["deck_safe"] == 8, "packet deck census changed")
    require(packet6["counters"]["topology_rejected"] == 8, "packet topology census changed")

    router_summary = DATA / "routed_s6.summary.json"
    summary = load(router_summary)
    require(summary["status"] == "PASS_NO_CONNECTED_SUCCESSOR", "router summary failed")
    require(summary["two_component_sources"] == 10, "router source count changed")
    require(
        summary["two_component_sources_with_connected_successor"] == 0,
        "router batch contains connected successor",
    )

    output = {
        "schema": "k15-pbbs-fixed-m0-component-reduction-chain-audit-v1",
        "mapping": str(MAP),
        "mapping_sha256": digest(MAP),
        "stages": stage_rows,
        "exchanges": exchanges,
        "final_support_at_most_8_separation": {
            "raw_cycle_histogram": atlas["raw_cycle_histogram"],
            "deck_safe_cycle_histogram": atlas["deck_safe_cycle_histogram"],
            "deck_safe_cycles": atlas["deck_safe_cycles"],
            "topology_rejected_cycles": atlas["topology_rejected_cycles"],
            "audit_sha256": SEPARATION["atlas"][1],
        },
        "two_packet_support_at_most_6_separation": {
            "counters": packet6["counters"],
            "audit_sha256": SEPARATION["packet6"][1],
        },
        "neutral_router_support5_then_support6": {
            "summary": str(router_summary),
            "summary_sha256": digest(router_summary),
            "status": summary["status"],
            "two_component_sources": summary["two_component_sources"],
        },
        "scope": (
            "PASS proves the explicit fixed-M0 9->4->3->2 chain and the "
            "listed finite separation classes at its final state. It does not "
            "exclude larger/overlapping compound switches and does not itself "
            "compile a literal OR word."
        ),
        "status": "PASS",
    }
    output_path = DATA / "pbbs_component_reduction_chain.audit.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "stage_components": [len(row["physical_component_lengths"]) for row in stage_rows],
        "switch_supports": [row["support"] for row in exchanges],
        "output": str(output_path),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
