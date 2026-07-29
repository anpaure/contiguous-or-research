#!/usr/bin/env python3
"""Search every residence-safe arbitrary seam of the audited 6390+45 factor.

Unlike the q1-recycling catalogue, a seam may be non-Johnson.  The two cut
q1 colours can then occupy the two global compiler boundaries.  Exact cyclic
upper losses are represented by target bitsets and must be recreated by a
literal suffix/prefix union across the single seam.  Promising chronologies
are passed to the exact generalized compiler and full verifier.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))
import threadD_seed0_component_seam_endgame_20260729 as base  # noqa: E402


FACTOR = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.best.json"
AUDIT = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.independent.audit.json"


def matching_size(targets: list[int], cells: tuple[int, ...]) -> int:
    adjacency = [[i for i, cell in enumerate(cells) if not (target & ~cell)] for target in targets]
    order = sorted(range(len(targets)), key=lambda i: len(adjacency[i]))
    used = [False] * len(cells)

    def rec(at: int) -> int:
        if at == len(order):
            return at
        best = at
        for cell in adjacency[order[at]]:
            if used[cell]:
                continue
            used[cell] = True
            best = max(best, rec(at + 1))
            used[cell] = False
            if best == len(order):
                break
        return best

    return rec(0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--word", type=Path, required=True)
    parser.add_argument("--compile-top", type=int, default=100)
    parser.add_argument("--compiler-seconds", type=float, default=300.0)
    parser.add_argument("--compiler-workers", type=int, default=2)
    parser.add_argument("--seed", type=int, default=1951)
    args = parser.parse_args()
    started = time.time()

    payload = base.load_json(FACTOR)
    retained = base.load_json(AUDIT)
    factor_sha = sha256(FACTOR.read_bytes()).hexdigest()
    if retained.get("status") != "PASS" or retained.get("candidate_sha256") != factor_sha:
        raise ValueError("two-cycle independent audit/hash mismatch")
    catalogue = base.QuotientCatalogue(base.K)
    selected = catalogue.ids_from_explicit(payload["choices"])
    cycles, _report = base.validate_cycle_cover(catalogue, selected)
    if list(map(len, cycles)) != [6390, 45]:
        raise AssertionError("two-cycle lengths changed")
    states, by_component = base.build_states(cycles)
    first4, last4, prefixes, suffixes, _first8, _last8 = base.boundary_profiles(cycles, states)
    high_cells = [base.state_high_boundary_cells(cycles, state) for state in states]

    upper_targets = sorted(
        target for q in range(1, base.R) for target in base.rank_masks(base.R + q)
    )
    target_index = {target: i for i, target in enumerate(upper_targets)}
    witnesses: dict[int, dict[int, list[set[int]]]] = defaultdict(lambda: defaultdict(list))
    for component, cycle in enumerate(cycles):
        n = len(cycle)
        for q in range(1, base.R):
            for start in range(n):
                value = 0
                for offset in range(q + 1):
                    value |= int(cycle[(start + offset) % n])
                if value.bit_count() == base.R + q:
                    witnesses[value][component].append(
                        {(start + edge) % n for edge in range(q)}
                    )
    if set(witnesses) != set(upper_targets):
        raise AssertionError("two-cycle source lost a cyclic upper target")

    baseline_killed = [0, 0]
    common_cut_rows: list[tuple[int, int, set[int]]] = []
    for target in upper_targets:
        bit = 1 << target_index[target]
        for component in range(2):
            rows = witnesses[target].get(component, ())
            if not rows:
                baseline_killed[component] |= bit
                continue
            common = set(rows[0])
            for row in rows[1:]:
                common.intersection_update(row)
            common_cut_rows.append((component, bit, common))
    killed = [
        [baseline_killed[component]] * len(cycles[component])
        for component in range(2)
    ]
    for component, bit, common in common_cut_rows:
        for cut in common:
            killed[component][cut] |= bit

    qualifying = []
    tested_pairs = 0
    residence_safe = 0
    boundary_q1_safe = 0
    upper_safe = 0
    for source_component, target_component in ((0, 1), (1, 0)):
        for source_serial in by_component[source_component]:
            source = states[source_serial]
            left_cells = high_cells[source_serial][0]
            for target_serial in by_component[target_component]:
                tested_pairs += 1
                target_state = states[target_serial]
                if base.linear_residence_violations(
                    list(last4[source_serial]) + list(first4[target_serial]), base.D
                ):
                    continue
                residence_safe += 1
                right_cells = high_cells[target_serial][1]
                cells = tuple(left_cells) + tuple(right_cells)
                cut_colours = [source.cut_colour, target_state.cut_colour]
                if matching_size(cut_colours, cells) < 2:
                    continue
                boundary_q1_safe += 1

                lost = killed[source_component][source.cut] & killed[target_component][target_state.cut]
                if lost:
                    made = 0
                    for left_union in suffixes[source_serial]:
                        for right_union in prefixes[target_serial]:
                            value = int(left_union) | int(right_union)
                            index = target_index.get(value)
                            if index is not None:
                                made |= 1 << index
                    if lost & ~made:
                        continue
                upper_safe += 1

                chronology = base.oriented_sequence(cycles, source) + base.oriented_sequence(
                    cycles, target_state
                )
                fixed_lower, _fixed_upper = base.fixed_window_targets(
                    [chronology], cyclic=False
                )
                boundary_targets = sorted(
                    (base.rank_masks(base.R - 1) - fixed_lower[1])
                    | (base.rank_masks(base.R - 2) - fixed_lower[2])
                )
                boundary_match = matching_size(boundary_targets, cells)
                if boundary_match < len(boundary_targets):
                    continue
                audit = base.chronology_audit(chronology, cycles, [])
                if any(audit["all_width_upper_holes"].values()):
                    raise AssertionError("bitset-positive seam failed arbitrary upper replay")
                qualifying.append(
                    {
                        "source_state": source_serial,
                        "target_state": target_serial,
                        "component_order": [source_component, target_component],
                        "cuts": [source.cut, target_state.cut],
                        "orientations": [source.reverse, target_state.reverse],
                        "symmetric_difference_size": (source.right ^ target_state.left).bit_count(),
                        "boundary_targets": boundary_targets,
                        "boundary_matching": boundary_match,
                        "lower_holes": audit["lower_holes"],
                        "base_hall": audit["base_literal_hall"],
                        "chronology": chronology,
                    }
                )

    qualifying.sort(
        key=lambda row: (
            row["base_hall"]["deficiency"],
            len(row["boundary_targets"]),
            sum(row["lower_holes"].values()),
            row["symmetric_difference_size"],
            row["source_state"],
            row["target_state"],
        )
    )
    compiled = []
    for index, row in enumerate(qualifying[: args.compile_top]):
        chronology = row.pop("chronology")
        word = args.word.with_name(
            f"{args.word.stem}.s{row['source_state']}.t{row['target_state']}{args.word.suffix}"
        )
        result = base.compiler.exact_compiler_for_opening(
            catalogue,
            chronology,
            base.W - 1,
            args.compiler_seconds,
            args.compiler_workers,
            args.seed + index,
            word,
            True,
        )
        row["compiler"] = result
        row["word"] = str(word)
        compiled.append(row)
        if result.get("status") == "VERIFIED_OPTIMAL":
            break
    # Remove the large chronology from uncompiled retained rows.
    best_rows = []
    for row in qualifying[:100]:
        row = dict(row)
        row.pop("chronology", None)
        best_rows.append(row)
    verified = bool(compiled and compiled[-1]["compiler"].get("status") == "VERIFIED_OPTIMAL")
    result = {
        "schema": "k15-two-cycle-arbitrary-seam-exhaustion-v1",
        "status": "VERIFIED_OPTIMAL" if verified else "EXHAUSTED_ARBITRARY_SEAMS",
        "factor": str(FACTOR),
        "factor_sha256": factor_sha,
        "tested_pairs": tested_pairs,
        "residence_safe_pairs": residence_safe,
        "boundary_q1_safe_pairs": boundary_q1_safe,
        "upper_safe_pairs": upper_safe,
        "compiler_candidate_pairs": len(qualifying),
        "best_rows": best_rows,
        "compiled_rows": compiled,
        "wall_seconds": time.time() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("best_rows",)}, indent=2))
    return 0 if verified else 1


if __name__ == "__main__":
    raise SystemExit(main())
