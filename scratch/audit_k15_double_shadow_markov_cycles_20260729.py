#!/usr/bin/env python3
"""Exact small alternating-cycle atlas in a fixed-M0 double-shadow fibre.

The input mapping is produced by
``k15_fixed_matching_double_shadow_sat_20260729.py``.  It fixes a perfect
matching M0 and assigns every allowed second-matching edge two immutable
colours: upper-q1 and lower-q2.  The input candidate supplies the current
perfect matching P and is required to cover every colour on both shores.

Relative to P, every alternative edge l--v gives an arc l -> P^{-1}(v) in
the exchange digraph.  Simple directed cycles are exactly the connected
alternating matching exchanges, including quotient two-edge alias cycles at
support one.  This script exhausts all such cycles up to a requested support,
checks the two colour-load inequalities exactly, expands every surviving
factor to all 6,435 physical vertices, and independently recomputes residence
and all three displayed shadows.

Heavy exhaustive invocations belong on the H100 CPU host.  The script uses no
solver and no GPU.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys
from typing import Any


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audit_k15_global_rainbow_factor_candidate_20260729 import (  # noqa: E402
    physical_shadow_audit,
    residence_audit,
)
from graded_quotient_pipeline import (  # noqa: E402
    QuotientCatalogue,
)
from k15_fixed_matching_minimal_residence_motifs_20260729 import (  # noqa: E402
    residence_clauses,
)


MAP_SCHEMA = "k15-fixed-matching-double-shadow-sat-map-v1"
OUTPUT_SCHEMA = "k15-fixed-m0-all-depth-markov-cycle-atlas-v2"


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key {key!r}")
        out[key] = value
    return out


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(), object_pairs_hook=unique_object)
    if type(value) is not dict:
        raise ValueError(f"{path} is not a JSON object")
    return value


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def reconstruct_matching(
    mapping: dict[str, Any], candidate: dict[str, Any]
) -> tuple[list[int], dict[int, dict[str, Any]], list[int]]:
    if mapping.get("schema") != MAP_SCHEMA:
        raise ValueError("mapping schema mismatch")
    annotations = {
        int(raw): value for raw, value in mapping["variable_annotations"].items()
    }
    if sorted(annotations) != list(range(1, len(annotations) + 1)):
        raise ValueError("SAT variable annotations are not consecutive")
    lower_masks = list(map(int, mapping["lower_masks"]))
    if len(lower_masks) != 429 or len(set(lower_masks)) != 429:
        raise ValueError("mapping lower shore is malformed")
    lower_index = {value: i for i, value in enumerate(lower_masks)}
    arcs = mapping["arcs"]
    base_m0 = list(map(int, mapping["base_m0"]))
    if len(base_m0) != 429:
        raise ValueError("base M0 does not have 429 edges")
    base_added = [int(arcs[edge]["added"]) for edge in base_m0]
    variable_by_choice: dict[tuple[int, int], int] = {}
    for variable, edge in annotations.items():
        key = (int(edge["l"]), int(edge["added"]))
        if key in variable_by_choice:
            raise ValueError("duplicate variable for one lower/addition choice")
        variable_by_choice[key] = variable

    choices = candidate.get("choices")
    if type(choices) is not list or len(choices) != 429:
        raise ValueError("candidate does not have 429 explicit choices")
    selected = [-1] * 429
    seen_lower: set[int] = set()
    for raw in choices:
        if type(raw) is not list or len(raw) != 3:
            raise ValueError("malformed candidate choice")
        lower, a, b = map(int, raw)
        if lower not in lower_index or lower in seen_lower or a == b:
            raise ValueError("invalid or duplicate lower choice")
        seen_lower.add(lower)
        l = lower_index[lower]
        if a == base_added[l]:
            added = b
        elif b == base_added[l]:
            added = a
        else:
            raise ValueError("candidate does not contain the frozen M0 edge")
        try:
            selected[l] = variable_by_choice[l, added]
        except KeyError as error:
            raise ValueError("candidate P edge is absent from the fixed-M0 map") from error
    if any(variable < 0 for variable in selected):
        raise ValueError("candidate matching is incomplete")
    endpoints = [int(annotations[variable]["v"]) for variable in selected]
    if len(set(endpoints)) != 429:
        raise ValueError("candidate P is not a perfect matching")
    if any(annotations[variable].get("lower_q2") is None for variable in selected):
        raise ValueError("candidate selects a rank-deficient lower-q2 arc")
    return selected, annotations, base_m0


def choices_from_matching(
    mapping: dict[str, Any],
    selected: list[int],
    annotations: dict[int, dict[str, Any]],
    base_m0: list[int],
) -> list[list[int]]:
    arcs = mapping["arcs"]
    out: list[list[int]] = []
    for l, lower in enumerate(map(int, mapping["lower_masks"])):
        a = int(arcs[base_m0[l]]["added"])
        b = int(annotations[selected[l]]["added"])
        if a == b:
            raise AssertionError("M0 and P coincide at a lower vertex")
        out.append([lower, min(a, b), max(a, b)])
    return out


def quotient_lift_profile(
    mapping: dict[str, Any],
    selected: list[int],
    annotations: dict[int, dict[str, Any]],
    base_m0: list[int],
    k: int,
) -> dict[str, Any]:
    """Compute quotient cycles, voltages, and lifted physical lengths exactly."""
    arcs = mapping["arcs"]
    base_at_v = [int(arcs[edge]["v"]) for edge in base_m0]
    if len(set(base_at_v)) != len(base_at_v):
        raise AssertionError("M0 endpoint inverse is not defined")
    base_inverse = {v: l for l, v in enumerate(base_at_v)}
    successor: list[int] = []
    shift: list[int] = []
    for variable in selected:
        edge = annotations[variable]
        nxt = base_inverse[int(edge["v"])]
        successor.append(nxt)
        shift.append(
            (int(edge["phase"]) - int(arcs[base_m0[nxt]]["phase"])) % k
        )
    seen: set[int] = set()
    rows: list[dict[str, int]] = []
    physical_lengths: list[int] = []
    for start in range(len(selected)):
        if start in seen:
            continue
        length = 0
        voltage = 0
        current = start
        while current not in seen:
            seen.add(current)
            length += 1
            voltage = (voltage + shift[current]) % k
            current = successor[current]
        lift_cycles = gcd(k, voltage)
        physical_length = k * length // lift_cycles
        rows.append({
            "quotient_length": length,
            "voltage": voltage,
            "lift_cycles": lift_cycles,
            "physical_length": physical_length,
        })
        physical_lengths.extend([physical_length] * lift_cycles)
    rows.sort(key=lambda row: (-row["quotient_length"], row["voltage"]))
    physical_lengths.sort(reverse=True)
    return {
        "quotient_components": len(rows),
        "quotient_rows": rows,
        "physical_components": len(physical_lengths),
        "physical_component_lengths": physical_lengths,
    }


def cyclic_interval_unions(
    cycles: list[list[int]], k: int
) -> dict[int, set[int]]:
    """Return every literal union of a nonempty cyclic interval.

    For a fixed start, the union changes only when an as-yet absent
    coordinate next appears.  Thus the first future occurrence of each
    missing coordinate is a complete event list.  This is an exact
    arbitrary-width oracle, not a shortest-window surrogate; the present
    bisect implementation is near-linear in W for fixed k.
    """
    got = {rank: set() for rank in range(k + 1)}
    for raw_cycle in cycles:
        cycle = list(map(int, raw_cycle))
        n = len(cycle)
        positions: list[list[int]] = [[] for _ in range(k)]
        for index, value in enumerate(cycle):
            for coordinate in range(k):
                if value & (1 << coordinate):
                    positions[coordinate].append(index)
        for start, initial in enumerate(cycle):
            value = initial
            got[value.bit_count()].add(value)
            events: dict[int, int] = defaultdict(int)
            for coordinate, occurrences in enumerate(positions):
                bit = 1 << coordinate
                if value & bit or not occurrences:
                    continue
                at = bisect_right(occurrences, start)
                arrival = (
                    occurrences[at]
                    if at < len(occurrences)
                    else occurrences[0] + n
                )
                distance = arrival - start
                if 1 <= distance < n:
                    events[distance] |= bit
            for distance in sorted(events):
                value |= events[distance]
                got[value.bit_count()].add(value)
    return got


def all_depth_shadow_audit(
    cycles: list[list[int]], catalogue: QuotientCatalogue
) -> dict[str, Any]:
    """Audit all proper lower/upper ranks by literal cyclic intervals.

    Upper targets are interval unions.  Lower targets are interval
    intersections, computed as complements of interval unions in the
    complemented cycles.  The range q=1,...,7 is exactly the proper
    all-depth range used by the k=15,r=8 carrier audit.
    """
    k, r = catalogue.k, catalogue.r
    full = (1 << k) - 1
    upper_got = cyclic_interval_unions(cycles, k)
    complement_cycles = [[full ^ value for value in cycle] for cycle in cycles]
    complement_got = cyclic_interval_unions(complement_cycles, k)
    by_depth: dict[str, dict[str, Any]] = {}
    total_physical = 0
    total_orbits = 0
    for depth in range(1, min(r, k - r + 1)):
        lower_rank = r - depth
        upper_rank = r + depth
        lower_got = {
            full ^ value for value in complement_got[k - lower_rank]
        }
        upper_at_rank = upper_got[upper_rank]
        lower_targets = {
            value for value in range(1 << k) if value.bit_count() == lower_rank
        }
        upper_targets = {
            value for value in range(1 << k) if value.bit_count() == upper_rank
        }
        lower_missing = lower_targets - lower_got
        upper_missing = upper_targets - upper_at_rank
        lower_target_reps = set(catalogue.orbit_reps(lower_rank))
        upper_target_reps = set(catalogue.orbit_reps(upper_rank))
        lower_got_reps = {catalogue.canonical(value) for value in lower_got}
        upper_got_reps = {catalogue.canonical(value) for value in upper_at_rank}
        lower_missing_reps = sorted(lower_target_reps - lower_got_reps)
        upper_missing_reps = sorted(upper_target_reps - upper_got_reps)
        total_physical += len(lower_missing) + len(upper_missing)
        total_orbits += len(lower_missing_reps) + len(upper_missing_reps)
        by_depth[str(depth)] = {
            "lower_rank": lower_rank,
            "lower_missing_physical": len(lower_missing),
            "lower_missing_orbits": len(lower_missing_reps),
            "lower_missing_representatives": lower_missing_reps,
            "upper_rank": upper_rank,
            "upper_missing_physical": len(upper_missing),
            "upper_missing_orbits": len(upper_missing_reps),
            "upper_missing_representatives": upper_missing_reps,
        }
    return {
        "semantics": "exact arbitrary-width nonempty cyclic interval unions/intersections",
        "by_depth": by_depth,
        "missing_physical_total": total_physical,
        "missing_orbits_total": total_orbits,
        "complete": total_physical == 0,
    }


def evaluate_matching(
    catalogue: QuotientCatalogue,
    mapping: dict[str, Any],
    selected: list[int],
    annotations: dict[int, dict[str, Any]],
    base_m0: list[int],
) -> tuple[dict[str, Any], list[list[int]]]:
    choices = choices_from_matching(mapping, selected, annotations, base_m0)
    ids = catalogue.ids_from_explicit(choices)
    if len(ids) != catalogue.N or len(set(ids)) != catalogue.N:
        raise AssertionError("matching did not decode to N distinct quotient choices")
    used_lower = [catalogue.choices[index].lower for index in ids]
    if len(set(used_lower)) != len(catalogue.low):
        raise AssertionError("matching lost the exact lower-q1 rainbow")
    # Do not call validate_cycle_cover here: its deliberately simple
    # arbitrary-width upper audit is quadratic in a component length.  The
    # first-arrival oracle below is equivalent and O(kW).
    cycles = catalogue.physical_cycles(ids)
    shadows = physical_shadow_audit(cycles, catalogue.k, catalogue.r)
    if shadows["missing_upper_q1_orbits"] or shadows["missing_lower_q2_orbits"]:
        raise AssertionError("declared deck-safe exchange lost a protected deck")
    residence = residence_audit(cycles, catalogue.k, catalogue.d + 1)
    all_depth = all_depth_shadow_audit(cycles, catalogue)
    quotient_profile = quotient_lift_profile(
        mapping, selected, annotations, base_m0, catalogue.k
    )
    if quotient_profile["physical_component_lengths"] != list(map(len, cycles)):
        raise AssertionError("quotient-voltage ledger disagrees with physical replay")
    lower_q2_missing = catalogue.factor_lower_missing(cycles, 2)
    lower_q3_missing = (
        catalogue.factor_lower_missing(cycles, 3) if catalogue.d >= 3 else []
    )
    carrier_gates = {
        "lower_q1_rainbow": True,
        "lower_q2_missing_representatives": lower_q2_missing,
        "lower_q3_positive_degree_missing_representatives": lower_q3_missing,
        "upper_q2_geodesic_missing_physical": shadows["missing_upper_q2_physical"],
        "upper_q2_geodesic_missing_orbits": shadows["missing_upper_q2_orbits"],
        "upper_arbitrary_width_missing_orbits": sum(
            row["upper_missing_orbits"]
            for row in all_depth["by_depth"].values()
        ),
    }
    carrier_gates["pass_ignoring_connectivity"] = (
        not lower_q2_missing
        and not lower_q3_missing
        and shadows["missing_upper_q2_physical"] == 0
        and carrier_gates["upper_arbitrary_width_missing_orbits"] == 0
        and residence["residence_shortfall"] == 0
    )
    return {
        "components": len(cycles),
        "component_lengths": list(map(len, cycles)),
        "quotient_lift_profile": quotient_profile,
        "residence": residence,
        "shadows": shadows,
        "all_depth_shadows": all_depth,
        "all_depth_holes_physical_total": all_depth["missing_physical_total"],
        "all_depth_holes_orbits_total": all_depth["missing_orbits_total"],
        "carrier_gates": carrier_gates,
    }, choices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mapping", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--max-support", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--best-candidate", type=Path)
    parser.add_argument("--candidate-dir", type=Path)
    parser.add_argument(
        "--hard-residence",
        action="store_true",
        help="filter candidates by the exact fixed-M0 width-2/3 residence ideal before physical replay",
    )
    parser.add_argument(
        "--hard-all-depth",
        action="store_true",
        help="retain only candidates complete for every literal lower/upper cyclic interval rank",
    )
    parser.add_argument(
        "--require-component-improvement",
        action="store_true",
        help="cheaply reject exchanges whose exact quotient-voltage lift does not reduce components",
    )
    args = parser.parse_args()
    if not 1 <= args.max_support <= 20:
        raise ValueError("max support must lie in 1..20")

    mapping = load_json(args.mapping)
    candidate = load_json(args.candidate)
    selected, annotations, base_m0 = reconstruct_matching(mapping, candidate)
    catalogue = QuotientCatalogue(15)
    base_metrics, _base_choices = evaluate_matching(
        catalogue, mapping, selected, annotations, base_m0
    )
    if args.hard_all_depth and (
        base_metrics["all_depth_holes_physical_total"]
        or not base_metrics["carrier_gates"]["pass_ignoring_connectivity"]
    ):
        raise ValueError("--hard-all-depth input fails an all-depth/carrier gate")
    motif_clauses: list[tuple[int, ...]] = []
    motif_report: dict[str, Any] | None = None
    if args.hard_residence:
        motif_clauses, motif_report = residence_clauses(mapping)
        base_positive = set(selected)
        if any(all(-literal in base_positive for literal in clause) for clause in motif_clauses):
            raise ValueError("--hard-residence input violates the exact residence ideal")

    colour_names = ("upper_q1", "lower_q2")
    loads = {
        name: Counter(annotations[variable][name] for variable in selected)
        for name in colour_names
    }
    if any(len(loads[name]) != 335 for name in colour_names):
        raise ValueError("input candidate is not complete on both quotient decks")

    selected_row_at_v = {
        int(annotations[variable]["v"]): l for l, variable in enumerate(selected)
    }
    if len(selected_row_at_v) != 429:
        raise AssertionError("selected matching endpoint inverse is not defined")
    exchange: list[list[tuple[int, int]]] = [[] for _ in range(429)]
    for variable, edge in annotations.items():
        l = int(edge["l"])
        if variable == selected[l] or edge.get("lower_q2") is None:
            continue
        destination = selected_row_at_v[int(edge["v"])]
        exchange[l].append((destination, variable))
    for row in exchange:
        row.sort()

    raw_hist: Counter[int] = Counter()
    safe_hist: Counter[int] = Counter()
    load_balanced_hist: Counter[int] = Counter()
    safe_cycles: list[tuple[list[int], list[int]]] = []

    def deck_safe(rows: list[int], added: list[int]) -> tuple[bool, bool]:
        balanced = True
        for name in colour_names:
            delta: Counter[int] = Counter(
                annotations[variable][name] for variable in added
            )
            delta.subtract(annotations[selected[l]][name] for l in rows)
            if any(loads[name][colour] + change < 1 for colour, change in delta.items()):
                return False, False
            if any(change for change in delta.values()):
                balanced = False
        return True, balanced

    for start in range(429):
        def visit(current: int, rows: list[int], added: list[int]) -> None:
            for destination, variable in exchange[current]:
                if destination == start:
                    support = len(rows)
                    raw_hist[support] += 1
                    safe, balanced = deck_safe(rows, added + [variable])
                    if safe:
                        safe_hist[support] += 1
                        if balanced:
                            load_balanced_hist[support] += 1
                        safe_cycles.append((rows.copy(), added + [variable]))
                elif (
                    destination > start
                    and destination not in rows
                    and len(rows) < args.max_support
                ):
                    visit(destination, rows + [destination], added + [variable])

        visit(start, [start], [])

    records: list[dict[str, Any]] = []
    best_selected: list[int] | None = None
    best_key: tuple[int, ...] | None = None
    best_exchange: dict[str, Any] | None = None
    hard_residence_rejected = 0
    hard_all_depth_rejected = 0
    topology_rejected = 0
    if args.candidate_dir is not None:
        args.candidate_dir.mkdir(parents=True, exist_ok=True)

    def candidate_payload(
        exchange: dict[str, Any] | str,
        metrics: dict[str, Any],
        choices: list[list[int]],
    ) -> dict[str, Any]:
        return {
            "schema": "global-rainbow-factor-candidate-v1",
            "k": 15,
            "r": 8,
            "d": 3,
            "W": 6435,
            "N": 429,
            "seed": int(candidate.get("seed", 0)),
            "iteration": int(candidate.get("iteration", 0)) + 1,
            "markov_cycle_atlas": {
                "source": str(args.candidate),
                "atlas": str(args.output),
                "exchange": exchange,
                "metrics": metrics,
            },
            "exact_audit": {
                "fiber_invariant": True,
                "quotient_loops": 0,
                "physical_cycle_count": metrics["components"],
                **metrics["residence"],
                **metrics["shadows"],
            },
            "choices": choices,
        }

    for rows, added in safe_cycles:
        changed = selected.copy()
        removed = [selected[l] for l in rows]
        for l, variable in zip(rows, added):
            if int(annotations[variable]["l"]) != l:
                raise AssertionError("cycle added edge is assigned to the wrong row")
            changed[l] = variable
        if len({int(annotations[v]["v"]) for v in changed}) != 429:
            raise AssertionError("exchange cycle did not preserve the perfect matching")
        changed_profile = quotient_lift_profile(
            mapping, changed, annotations, base_m0, catalogue.k
        )
        if (
            args.require_component_improvement
            and changed_profile["physical_components"] >= base_metrics["components"]
        ):
            topology_rejected += 1
            continue
        if args.hard_residence:
            positive = set(changed)
            if any(
                all(-literal in positive for literal in clause)
                for clause in motif_clauses
            ):
                hard_residence_rejected += 1
                continue
        metrics, choices = evaluate_matching(
            catalogue, mapping, changed, annotations, base_m0
        )
        if args.hard_residence and metrics["residence"]["residence_shortfall"]:
            raise AssertionError(
                "exact motif prefilter accepted a physical residence violation"
            )
        if args.hard_all_depth and (
            metrics["all_depth_holes_physical_total"]
            or not metrics["carrier_gates"]["pass_ignoring_connectivity"]
        ):
            hard_all_depth_rejected += 1
            continue
        exchange_descriptor = {
            "support": len(rows),
            "rows": rows,
            "removed_variables": removed,
            "added_variables": added,
        }
        deltas: dict[str, dict[str, int]] = {}
        load_balanced = True
        for name in colour_names:
            delta: Counter[int] = Counter(
                annotations[variable][name] for variable in added
            )
            delta.subtract(annotations[variable][name] for variable in removed)
            cleaned = {str(colour): change for colour, change in sorted(delta.items()) if change}
            deltas[name] = cleaned
            load_balanced &= not cleaned
        residence = metrics["residence"]
        shadows = metrics["shadows"]
        record = {
            "support": len(rows),
            "rows": rows,
            "removed_variables": removed,
            "added_variables": added,
            "load_balanced": load_balanced,
            "colour_delta": deltas,
            "components": metrics["components"],
            "component_lengths": metrics["component_lengths"],
            "residence_bad_runs": residence["residence_bad_runs"],
            "residence_shortfall": residence["residence_shortfall"],
            "minimum_run": residence["minimum_run"],
            "collision_floor_excess": shadows["collision_floor_excess"],
            "upper_q2_holes_physical": shadows["missing_upper_q2_physical"],
            "upper_q2_holes_orbits": shadows["missing_upper_q2_orbits"],
            "all_depth_holes_physical_total": metrics["all_depth_holes_physical_total"],
            "all_depth_holes_orbits_total": metrics["all_depth_holes_orbits_total"],
            "all_depth_shadows": metrics["all_depth_shadows"],
            "carrier_gates": metrics["carrier_gates"],
            "quotient_lift_profile": metrics["quotient_lift_profile"],
            "carrier_admissible": metrics["carrier_gates"]["pass_ignoring_connectivity"],
            "bilateral_interval_complete": metrics["all_depth_holes_physical_total"] == 0,
        }
        if args.candidate_dir is not None:
            exchange_hash = sha256(json.dumps(
                exchange_descriptor, sort_keys=True, separators=(",", ":")
            ).encode()).hexdigest()[:16]
            name = f"s{len(rows)}_{exchange_hash}.json"
            path = args.candidate_dir / name
            path.write_text(json.dumps(
                candidate_payload(exchange_descriptor, metrics, choices),
                indent=2,
                sort_keys=True,
            ) + "\n")
            record["candidate"] = str(path)
            record["candidate_sha256"] = digest(path)
        records.append(record)
        if (
            residence["residence_shortfall"] == 0
            and metrics["all_depth_holes_physical_total"] == 0
            and metrics["carrier_gates"]["pass_ignoring_connectivity"]
        ):
            key = (
                0,
                metrics["components"],
                shadows["collision_floor_excess"],
                len(rows),
            )
        elif residence["residence_shortfall"] == 0:
            key = (
                1,
                metrics["all_depth_holes_physical_total"],
                metrics["components"],
                len(rows),
            )
        else:
            key = (
                2,
                residence["residence_shortfall"],
                residence["residence_bad_runs"],
                metrics["components"],
                len(rows),
            )
        if best_key is None or key < best_key:
            best_key = key
            best_selected = changed
            best_exchange = exchange_descriptor

    def record_key(row: dict[str, Any]) -> tuple[Any, ...]:
        if (
            row["residence_shortfall"] == 0
            and row["bilateral_interval_complete"]
            and row["carrier_admissible"]
        ):
            return (0, row["components"], row["collision_floor_excess"], row["support"], row["rows"])
        if row["residence_shortfall"] == 0:
            return (
                1,
                row["all_depth_holes_physical_total"],
                row["components"],
                row["support"],
                row["rows"],
            )
        return (
            2,
            row["residence_shortfall"],
            row["residence_bad_runs"],
            row["components"],
            row["support"],
            row["rows"],
        )

    records.sort(key=record_key)
    base_residence = base_metrics["residence"]
    improving = [
        row for row in records
        if (row["residence_shortfall"], row["residence_bad_runs"])
        < (base_residence["residence_shortfall"], base_residence["residence_bad_runs"])
    ]
    admissible_records = [
        row for row in records
        if row["residence_shortfall"] == 0
        and row["all_depth_holes_physical_total"] == 0
        and row["carrier_gates"]["pass_ignoring_connectivity"]
    ]
    admissible_component_improving = [
        row for row in admissible_records if row["components"] < base_metrics["components"]
    ]
    output = {
        "schema": OUTPUT_SCHEMA,
        "mapping": str(args.mapping),
        "mapping_sha256": digest(args.mapping),
        "candidate": str(args.candidate),
        "candidate_sha256": digest(args.candidate),
        "choice_table_sha256": catalogue.choice_table_sha256,
        "max_support": args.max_support,
        "hard_residence": args.hard_residence,
        "hard_all_depth": args.hard_all_depth,
        "require_component_improvement": args.require_component_improvement,
        "residence_motif_report": motif_report,
        "hard_residence_rejected_cycles": hard_residence_rejected,
        "hard_all_depth_rejected_cycles": hard_all_depth_rejected,
        "topology_rejected_cycles": topology_rejected,
        "base": base_metrics,
        "base_colour_load_histograms": {
            name: {str(load): count for load, count in sorted(Counter(loads[name].values()).items())}
            for name in colour_names
        },
        "raw_cycle_histogram": {str(k): v for k, v in sorted(raw_hist.items())},
        "deck_safe_cycle_histogram": {str(k): v for k, v in sorted(safe_hist.items())},
        "load_balanced_cycle_histogram": {
            str(k): v for k, v in sorted(load_balanced_hist.items())
        },
        "minimum_deck_safe_support": min(safe_hist) if safe_hist else None,
        "deck_safe_cycles": sum(safe_hist.values()),
        "physically_evaluated_cycles": len(records) + hard_all_depth_rejected,
        "residence_improving_cycles": len(improving),
        "resident_all_depth_cycles": len(admissible_records),
        "resident_all_depth_component_improving_cycles": len(admissible_component_improving),
        "best_cycle": records[0] if records else None,
        "records": records,
        "scope": (
            "Exhaustive for connected alternating matching exchanges through max_support "
            "in this frozen fixed-M0 non-loop map. It does not enumerate disconnected "
            "packets, paths leaving fixed M0, or exchanges above max_support."
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")

    if args.best_candidate is not None and best_selected is not None:
        best_metrics, best_choices = evaluate_matching(
            catalogue, mapping, best_selected, annotations, base_m0
        )
        if best_exchange is None:
            raise AssertionError("best matching has no exchange descriptor")
        payload = candidate_payload(best_exchange, best_metrics, best_choices)
        args.best_candidate.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "raw_cycle_histogram": output["raw_cycle_histogram"],
        "deck_safe_cycle_histogram": output["deck_safe_cycle_histogram"],
        "residence_improving_cycles": output["residence_improving_cycles"],
        "resident_all_depth_cycles": output["resident_all_depth_cycles"],
        "resident_all_depth_component_improving_cycles": output["resident_all_depth_component_improving_cycles"],
        "best_cycle": output["best_cycle"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
