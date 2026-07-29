#!/usr/bin/env python3
"""Exact quotient-factor splice/compiler postprocessor for task D.

The program has deliberately separated scopes.

``audit`` and ``fixed`` never alter the supplied owner choices.  Their
rejections are fixed-selector statements.  ``search`` uses a supplied factor
as a baseline: replacing its choice at a lower owner is exactly a cut, and
the selected nonbaseline choice at that owner is the replacement seam.  The
full directed quotient-arc model restores degree, orients the retained paths,
and joins them by AddCircuit.

Upper depths q >= 3 are *only* separated by accumulated-union reachability.
No fixed-q upper witness is used there.

Heavy ``search`` and exact compiler solves belong on the H100 CPU.  The
solver-free audits and regression tests are suitable for a laptop.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
import json
from math import gcd
import os
from pathlib import Path
import platform
import socket
import sys
import time
from typing import Iterable, Sequence

from graded_quotient_pipeline import (
    QuotientCatalogue,
    build_cp_sat_model,
    cyclic_runs,
    linear_derivative,
    maximum_matching,
    serialize_carrier,
    stable_json,
    target_list,
    validate_carrier,
    validate_cycle_cover,
)


SCHEMA = "threadD-k15-splice-compiler-postprocessor-v1"
DEFAULT_INPUTS = (
    "scratch/k15_resident_q1factor_d83_snapshot.json",
    "scratch/k15_joint_q1factor_d86_snapshot.json",
    "scratch/k15_joint_q1factor_d92_snapshot.json",
    "scratch/k15_joint_q1ham_d93_snapshot.json",
    "scratch/k15_joint_scaffold_degree_atmost96_q1inc.json",
)
ALIASES = {
    "d83": DEFAULT_INPUTS[0],
    "d86": DEFAULT_INPUTS[1],
    "d92": DEFAULT_INPUTS[2],
    "d93": DEFAULT_INPUTS[3],
    "d94": DEFAULT_INPUTS[4],
}


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable_sha256(value: object) -> str:
    return sha256(stable_json(value)).hexdigest()


def resolve_input(raw: str | Path) -> Path:
    text = str(raw)
    return Path(ALIASES.get(text, text))


@dataclass(frozen=True)
class Snapshot:
    path: Path
    payload: dict[str, object]
    catalogue: QuotientCatalogue
    selected: tuple[int, ...]
    sha256: str


def load_snapshot(raw_path: str | Path) -> Snapshot:
    path = resolve_input(raw_path)
    payload = json.loads(path.read_text())
    k = int(payload.get("k", 15))
    catalogue = QuotientCatalogue(k)
    if "choices" not in payload:
        raise ValueError(f"{path}: explicit choices are required")
    selected = tuple(catalogue.ids_from_explicit(payload["choices"]))
    if len(selected) != catalogue.N or len(set(selected)) != catalogue.N:
        raise ValueError(f"{path}: expected {catalogue.N} distinct choices")
    if len({catalogue.choices[index].lower for index in selected}) != catalogue.N:
        raise ValueError(f"{path}: choices are not one-per-lower-owner")
    if "choice_ids" in payload and list(map(int, payload["choice_ids"])) != list(selected):
        raise ValueError(f"{path}: explicit choices disagree with choice_ids")
    declared_table = payload.get("choice_table_sha256")
    if declared_table is not None and declared_table != catalogue.choice_table_sha256:
        raise ValueError(f"{path}: choice-table digest mismatch")
    return Snapshot(path, payload, catalogue, selected, file_sha256(path))


def choice_endpoints(catalogue: QuotientCatalogue, choice: int) -> tuple[int, int]:
    arcs = catalogue.arcs_by_choice[choice]
    if len(arcs) != 2:
        raise AssertionError("strict choice must have two directed darts")
    _ci, source, target, _shift, _deleted, _inserted = catalogue.arc_data[arcs[0]]
    return source, target


@dataclass(frozen=True)
class QuotientComponent:
    vertices: tuple[int, ...]
    choices: tuple[int, ...]
    oriented_arcs: tuple[int, ...]
    voltage: int


def quotient_components(
    catalogue: QuotientCatalogue, selected: Sequence[int]
) -> list[QuotientComponent]:
    adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for choice in selected:
        u, v = choice_endpoints(catalogue, int(choice))
        adjacency[u].append((v, int(choice)))
        adjacency[v].append((u, int(choice)))
    if set(adjacency) != set(range(catalogue.N)):
        raise ValueError("factor does not span every quotient upper root")
    if any(len(edges) != 2 for edges in adjacency.values()):
        raise ValueError("factor is not quotient degree two")

    unseen = set(range(catalogue.N))
    answer: list[QuotientComponent] = []
    while unseen:
        start = min(unseen)
        first_neighbor, first_choice = min(adjacency[start], key=lambda item: (item[1], item[0]))
        vertices = [start]
        choices = []
        arcs = []
        current = start
        previous_choice: int | None = None
        forced = (first_neighbor, first_choice)
        while True:
            if previous_choice is None:
                neighbor, choice = forced
            else:
                options = [item for item in adjacency[current] if item[1] != previous_choice]
                if len(options) != 1:
                    raise AssertionError("factor traversal lost its unique continuation")
                neighbor, choice = options[0]
            matches = [
                arc
                for arc in catalogue.arcs_by_choice[choice]
                if catalogue.arc_data[arc][1] == current
                and catalogue.arc_data[arc][2] == neighbor
            ]
            if len(matches) != 1:
                raise AssertionError("oriented quotient factor edge is ambiguous")
            choices.append(choice)
            arcs.append(matches[0])
            previous_choice = choice
            current = neighbor
            if current == start:
                break
            if current in vertices:
                raise AssertionError("factor traversal closed at the wrong root")
            vertices.append(current)
        unseen.difference_update(vertices)
        voltage = sum(catalogue.arc_data[arc][3] for arc in arcs) % catalogue.k
        answer.append(
            QuotientComponent(
                tuple(vertices), tuple(choices), tuple(arcs), voltage
            )
        )
    answer.sort(key=lambda component: (-len(component.vertices), component.vertices))
    return answer


def upper_missing_by_depth(
    catalogue: QuotientCatalogue, missing: Iterable[int]
) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for target in map(int, missing):
        result[str(target.bit_count() - catalogue.r)].append(target)
    return {depth: sorted(values) for depth, values in sorted(result.items(), key=lambda x: int(x[0]))}


def upper_q1_load_histogram(
    catalogue: QuotientCatalogue, selected: Sequence[int]
) -> dict[str, int]:
    loads = Counter()
    for choice_id in selected:
        choice = catalogue.choices[int(choice_id)]
        target = catalogue.canonical(
            choice.lower | (1 << choice.a) | (1 << choice.b)
        )
        loads[target] += 1
    return {str(load): count for load, count in sorted(Counter(loads.values()).items())}


def audit_snapshot(snapshot: Snapshot) -> dict[str, object]:
    catalogue = snapshot.catalogue
    selected = list(snapshot.selected)
    components = quotient_components(catalogue, selected)
    physical_cycles, report = validate_cycle_cover(catalogue, selected)
    upper_by_depth = upper_missing_by_depth(catalogue, report["upper_missing"])
    q1_missing = upper_by_depth.get("1", [])
    fixed_reasons = []
    if len(physical_cycles) != 1:
        fixed_reasons.append("physical_cycle_count")
    component_rows = []
    for component in components:
        v = component.voltage
        component_rows.append(
            {
                "quotient_vertices": len(component.vertices),
                "voltage": v,
                "reverse_voltage": (-v) % catalogue.k,
                "voltage_gcd": gcd(v, catalogue.k),
                "choice_ids_sha256": stable_sha256(sorted(component.choices)),
            }
        )
    if len(components) == 1 and gcd(components[0].voltage, catalogue.k) != 1:
        fixed_reasons.append("nonunit_voltage")
    if report["residence_violations"]:
        fixed_reasons.append("residence")
    if report["lower_q2_missing"]:
        fixed_reasons.append("lower_q2")
    if report["lower_q3_positive_degree_missing"]:
        fixed_reasons.append("lower_q3")
    if q1_missing:
        fixed_reasons.append("upper_q1")
    if any(values for depth, values in upper_by_depth.items() if depth != "1"):
        fixed_reasons.append("unrestricted_upper")
    declared_changes = snapshot.payload.get("choice_changes")
    alias_warning = None
    if snapshot.path.name == "k15_resident_q1factor_d83_snapshot.json" and declared_changes != 83:
        alias_warning = (
            "filename d83 is a centre label; payload choice_changes is "
            f"{declared_changes}"
        )
    return {
        "schema": SCHEMA,
        "mode": "fixed-factor-audit",
        "input": str(snapshot.path),
        "input_sha256": snapshot.sha256,
        "input_schema": snapshot.payload.get("schema"),
        "choice_table_sha256": catalogue.choice_table_sha256,
        "choice_set_sha256": stable_sha256(sorted(selected)),
        "declared_choice_changes": declared_changes,
        "alias_warning": alias_warning,
        "k": catalogue.k,
        "N": catalogue.N,
        "quotient_component_count": len(components),
        "quotient_components": component_rows,
        "physical_cycle_count": len(physical_cycles),
        "physical_cycle_lengths": list(map(len, physical_cycles)),
        "residence_violation_count": len(report["residence_violations"]),
        "residence_violations_sha256": stable_sha256(report["residence_violations"]),
        "lower_q2_missing": list(map(int, report["lower_q2_missing"])),
        "lower_q3_missing": list(map(int, report["lower_q3_positive_degree_missing"])),
        "upper_missing_by_depth": upper_by_depth,
        "upper_q1_load_histogram": upper_q1_load_histogram(catalogue, selected),
        "fixed_selector_pass": not fixed_reasons,
        "fixed_selector_rejection_reasons": fixed_reasons,
        "fixed_selector_scope": (
            "The supplied undirected owner choices and their component reversals only; "
            "no owner replacement seam is allowed."
        ),
    }


def bad_run_cut_rows(
    catalogue: QuotientCatalogue, selected: Sequence[int]
) -> list[tuple[int, ...]]:
    """Owner-choice rows which must be cut to destroy every old short run."""
    rows = set()
    for cycle in catalogue.physical_cycles(selected):
        n = len(cycle)
        for coordinate in range(catalogue.k):
            runs = cyclic_runs([bool(value & (1 << coordinate)) for value in cycle])
            for run in runs:
                if len(run) > catalogue.d:
                    continue
                start = run[0]
                edge_positions = [
                    (start - 1 + offset) % n for offset in range(len(run) + 1)
                ]
                row = frozenset(
                    catalogue.edge_choice(cycle[pos], cycle[(pos + 1) % n])
                    for pos in edge_positions
                )
                if row:
                    rows.add(row)
    return sorted((tuple(sorted(row)) for row in rows), key=lambda row: (len(row), row))


def oriented_factor_hint(snapshot: Snapshot) -> list[int]:
    return sorted(
        arc
        for component in quotient_components(snapshot.catalogue, snapshot.selected)
        for arc in component.oriented_arcs
    )


def selected_arcs_by_choice(
    catalogue: QuotientCatalogue, selected_arcs: Iterable[int]
) -> dict[int, int]:
    result = {}
    for arc in selected_arcs:
        choice = catalogue.arc_data[int(arc)][0]
        if choice in result:
            raise ValueError("directed selector uses both orientations of one choice")
        result[choice] = int(arc)
    return result


def overlay_report(
    catalogue: QuotientCatalogue,
    baseline: Sequence[int],
    final: Sequence[int],
    final_arcs: Sequence[int],
) -> dict[str, object]:
    old = set(map(int, baseline))
    new = set(map(int, final))
    cuts = sorted(old - new)
    seams = sorted(new - old)
    if len(cuts) != len(seams):
        raise AssertionError("ownerwise factor replacement must balance cuts and seams")
    common = old & new
    adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for choice in common:
        u, v = choice_endpoints(catalogue, choice)
        adjacency[u].append((v, choice))
        adjacency[v].append((u, choice))
    seen = set()
    component_sizes = []
    component_types = Counter()
    for vertex in range(catalogue.N):
        if vertex in seen:
            continue
        queue = [vertex]
        seen.add(vertex)
        vertices = 0
        edges = set()
        while queue:
            u = queue.pop()
            vertices += 1
            for v, choice in adjacency.get(u, []):
                edges.add(choice)
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        component_sizes.append(vertices)
        if len(edges) == vertices:
            component_types["cycle"] += 1
        elif len(edges) == max(0, vertices - 1):
            component_types["path"] += 1
        else:
            component_types["other"] += 1
    arc_map = selected_arcs_by_choice(catalogue, final_arcs)
    return {
        "owner_changes": len(cuts),
        "cut_choice_ids": cuts,
        "seam_choice_ids": seams,
        "cut_choice_ids_sha256": stable_sha256(cuts),
        "seam_choice_ids_sha256": stable_sha256(seams),
        "retained_component_count": len(component_sizes),
        "retained_component_size_histogram": {
            str(size): count for size, count in sorted(Counter(component_sizes).items())
        },
        "retained_component_types": dict(sorted(component_types.items())),
        "directed_final_arc_sha256": stable_sha256(sorted(final_arcs)),
        "directed_choice_count": len(arc_map),
    }


def linear_maximal_envelope(
    cycle: Sequence[int], start: int, k: int, depth: int
) -> tuple[list[int], list[int]]:
    n = len(cycle)
    chronology = [int(cycle[(start + i) % n]) for i in range(n)]
    full = (1 << k) - 1
    envelope = []
    for position in range(n + depth):
        lo = max(0, position - depth)
        hi = min(n - 1, position)
        value = full
        for index in range(lo, hi + 1):
            value &= chronology[index]
        envelope.append(value)
    row = envelope
    for _ in range(depth):
        row = linear_derivative(row)
    if row != chronology:
        raise ValueError("linear maximal envelope does not differentiate to carrier")
    return chronology, envelope


def compiler_adjacency(
    envelope: Sequence[int], targets: Sequence[int]
) -> tuple[list[list[int]], list[list[int]], dict[tuple[int, int], int]]:
    target_index = {int(target): index for index, target in enumerate(targets)}
    by_target = [[] for _ in targets]
    by_position = [[] for _ in envelope]
    pair_target: dict[tuple[int, int], int] = {}
    for position, high in enumerate(map(int, envelope)):
        subset = high
        while subset:
            if subset in target_index:
                target = target_index[subset]
                by_target[target].append(position)
                by_position[position].append(target)
                pair_target[(target, position)] = subset
            subset = (subset - 1) & high
    return by_target, by_position, pair_target


def graded_boundary_requirements(
    envelope: Sequence[int], k: int, h: int, r: int, depth: int
) -> tuple[list[list[int]], list[int]]:
    """Fixed graded rows and the higher targets they leave for literals.

    For every eventual word A with DA=DP, all positive derivative rows of A
    equal those of P.  Every rank in (h,r) absent from those fixed rows joins
    the literal residual matching and may be placed at any position S<=P_p.
    """
    rows = [list(map(int, envelope))]
    for _ in range(depth):
        rows.append(linear_derivative(rows[-1]))
    fixed = set()
    for row in rows[1:depth]:
        fixed.update(value for value in row if h < value.bit_count() < r)
    missing = []
    for target in range(1, 1 << k):
        if not h < target.bit_count() < r:
            continue
        if target in fixed:
            continue
        missing.append(target)
    return rows, missing


def hall_deficiency_certificate(
    adjacency: list[list[int]], right_size: int
) -> tuple[int, list[int], dict[str, object]]:
    left_match = maximum_matching(adjacency, right_size)
    right_match = [-1] * right_size
    for left, right in enumerate(left_match):
        if right >= 0:
            right_match[right] = left
    unmatched = [left for left, right in enumerate(left_match) if right < 0]
    if not unmatched:
        return len(left_match), left_match, {
            "deficiency": 0,
            "deficient_left": [],
            "deficient_right": [],
        }
    left_seen = set(unmatched)
    right_seen = set()
    queue = deque((0, left) for left in unmatched)
    while queue:
        side, vertex = queue.popleft()
        if side == 0:
            matched_right = left_match[vertex]
            for right in adjacency[vertex]:
                if right == matched_right or right in right_seen:
                    continue
                right_seen.add(right)
                queue.append((1, right))
        else:
            left = right_match[vertex]
            if left >= 0 and left not in left_seen:
                left_seen.add(left)
                queue.append((0, left))
    return len(left_match) - len(unmatched), left_match, {
        "deficiency": len(unmatched),
        "deficient_left": sorted(left_seen),
        "deficient_right": sorted(right_seen),
        "hall_gap": len(left_seen) - len(right_seen),
    }


def exact_compiler_for_opening(
    catalogue: QuotientCatalogue,
    cycle: Sequence[int],
    cut_edge: int,
    timeout: float,
    workers: int,
    seed: int,
    output_word: Path | None,
    require_all_targets: bool = True,
    output_suffix: Sequence[int] = (),
) -> dict[str, object]:
    from ortools import __version__ as ortools_version
    from ortools.sat.python import cp_model

    start = (int(cut_edge) + 1) % len(cycle)
    chronology, envelope = linear_maximal_envelope(
        cycle, start, catalogue.k, catalogue.d
    )
    base_targets = target_list(catalogue.k, catalogue.h)
    graded_rows, missing_graded = graded_boundary_requirements(
        envelope,
        catalogue.k,
        catalogue.h,
        catalogue.r,
        catalogue.d,
    )
    # Every higher lower target absent from the fixed positive derivative
    # rows joins the literal residual family.  This is the exact endpoint
    # correction: it may be placed at any source position S<=P_p, not only
    # at a position with P_p=S.
    targets = base_targets + missing_graded
    adjacency, by_position, _pairs = compiler_adjacency(envelope, targets)
    matched, hall_matching, hall = hall_deficiency_certificate(
        adjacency, len(envelope)
    )
    base = {
        "cut_edge": int(cut_edge),
        "start": start,
        "envelope_length": len(envelope),
        "envelope_rank_histogram": {
            str(rank): count
            for rank, count in sorted(Counter(map(int.bit_count, envelope)).items())
        },
        "target_count": len(targets),
        "incidence_count": sum(map(len, adjacency)),
        "ordinary_hall_matching": matched,
        "ordinary_hall": hall,
        "graded_row_rank_histograms": [
            {
                str(rank): count
                for rank, count in sorted(Counter(map(int.bit_count, row)).items())
            }
            for row in graded_rows
        ],
        "base_literal_target_count": len(base_targets),
        "boundary_residual_target_count": len(missing_graded),
        "boundary_residual_targets": missing_graded,
    }
    if require_all_targets and matched != len(targets):
        deficient_targets = [targets[index] for index in hall["deficient_left"]]
        return {
            **base,
            "status": "FIXED_OPENING_HALL_INFEASIBLE",
            "deficient_target_masks": deficient_targets,
            "deficient_target_masks_sha256": stable_sha256(deficient_targets),
            "certificate_scope": "This fixed directed carrier and physical opening.",
        }

    model = cp_model.CpModel()
    match_vars: dict[tuple[int, int], object] = {}
    for target, positions in enumerate(adjacency):
        for position in positions:
            match_vars[(target, position)] = model.NewBoolVar(
                f"m{target}_{position}"
            )
    for target, positions in enumerate(adjacency):
        variables = [match_vars[(target, position)] for position in positions]
        if require_all_targets:
            model.AddExactlyOne(variables)
        else:
            model.AddAtMostOne(variables)
    for position, target_ids in enumerate(by_position):
        model.AddAtMostOne(
            [match_vars[(target, position)] for target in target_ids]
        )

    omission_rows = 0
    for position in range(len(envelope) - 1):
        left_high = envelope[position]
        right_high = envelope[position + 1]
        union = left_high | right_high
        for coordinate in range(catalogue.k):
            bit = 1 << coordinate
            if not (union & bit):
                continue
            constant = int(not (left_high & bit)) + int(not (right_high & bit))
            variables = []
            if left_high & bit:
                variables.extend(
                    match_vars[(target, position)]
                    for target in by_position[position]
                    if not (targets[target] & bit)
                )
            if right_high & bit:
                variables.extend(
                    match_vars[(target, position + 1)]
                    for target in by_position[position + 1]
                    if not (targets[target] & bit)
                )
            model.Add(sum(variables) <= 1 - constant)
            omission_rows += 1

    if not require_all_targets:
        model.Maximize(sum(match_vars.values()))
    # The ordinary Hall matching is a useful, though pair-conflict-blind, hint.
    for target, position in enumerate(hall_matching):
        if position >= 0:
            model.AddHint(match_vars[(target, position)], 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(timeout)
    solver.parameters.num_search_workers = int(workers)
    solver.parameters.random_seed = int(seed)
    started = time.time()
    status = solver.Solve(model)
    elapsed = time.time() - started
    status_name = solver.StatusName(status)
    proto = model.Proto()
    result = {
        **base,
        "status": status_name,
        "ortools_version": ortools_version,
        "variables": len(proto.variables),
        "constraints": len(proto.constraints),
        "assignment_variables": len(match_vars),
        "adjacent_omission_rows": omission_rows,
        "protected_endpoint_rows": 0,
        "wall_time": elapsed,
        "workers": workers,
        "require_all_targets": require_all_targets,
        "certificate_scope": "This fixed directed carrier and physical opening.",
    }
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        if status == cp_model.INFEASIBLE:
            result["status"] = "FIXED_OPENING_ADAPTIVE_CORE_INFEASIBLE"
        return result

    assigned_at: dict[int, int] = {}
    assigned_targets = 0
    for (target, position), variable in match_vars.items():
        if solver.Value(variable):
            assigned_at[position] = targets[target]
            assigned_targets += 1
    result["assigned_targets"] = assigned_targets
    # The objective is exactly the number of selected assignment literals;
    # count those literals instead of rounding the solver's float API.
    result["objective"] = assigned_targets
    if not require_all_targets:
        result["solver_status"] = status_name
        result["status"] = (
            "FIXED_OPENING_COMPILER_SCORE_OPTIMAL"
            if status == cp_model.OPTIMAL
            else "FIXED_OPENING_COMPILER_SCORE_FEASIBLE"
        )
        result["compiler_deficiency"] = len(targets) - assigned_targets
        # Keep CP-SAT's floating-point bound verbatim on a timed FEASIBLE
        # solve.  Only OPTIMAL supplies an exact integral score certificate.
        objective_bound = float(solver.BestObjectiveBound())
        result["best_objective_bound_raw"] = objective_bound
        result["compiler_deficiency_lower_bound_raw"] = (
            len(targets) - objective_bound
        )
        if status == cp_model.OPTIMAL:
            result["best_objective_bound_exact"] = assigned_targets
            result["compiler_deficiency_lower_bound_exact"] = (
                len(targets) - assigned_targets
            )
        return result

    word = [assigned_at.get(position, envelope[position]) for position in range(len(envelope))]
    row = word
    for _ in range(catalogue.d):
        row = linear_derivative(row)
    if row != chronology:
        raise AssertionError("adaptive compiler assignment changed the middle chronology")
    if output_word is None:
        result["status"] = "FIXED_OPENING_COMPILER_FEASIBLE"
        result["word_sha256"] = stable_sha256(word)
        return result

    output_word.parent.mkdir(parents=True, exist_ok=True)
    suffix = list(map(int, output_suffix))
    if any(value <= 0 or value >= (1 << catalogue.k) for value in suffix):
        raise ValueError("compiler suffix contains a non-mask or the empty mask")
    verified_word = [*word, *suffix]
    payload = " ".join(map(str, verified_word)) + "\n"
    output_word.write_text(payload)
    # Independent verifier lives in a different source file.
    from verify_exact_or_word import verify as verify_exact_word

    verification = verify_exact_word(
        output_word,
        catalogue.k,
        not suffix,
        bool(suffix),
    )
    result.update(
        {
            "status": (
                "VERIFIED_OPTIMAL" if not suffix else "VERIFIED_SUFFIX_UPPER_BOUND"
            ),
            "output_word": str(output_word),
            "output_sha256": sha256(payload.encode()).hexdigest(),
            "compiled_prefix_length": len(word),
            "output_suffix": suffix,
            "verified_word_length": len(verified_word),
            "verification": verification,
        }
    )
    return result


def compiler_score_better(
    candidate: dict[str, object], incumbent: dict[str, object] | None
) -> bool:
    """Compare opening scores by uncovered targets, never raw objectives."""
    if incumbent is None:
        return True
    candidate_defect = int(candidate["compiler_deficiency"])
    incumbent_defect = int(incumbent["compiler_deficiency"])
    if candidate_defect != incumbent_defect:
        return candidate_defect < incumbent_defect
    candidate_proved = (
        candidate["status"] == "FIXED_OPENING_COMPILER_SCORE_OPTIMAL"
    )
    incumbent_proved = (
        incumbent["status"] == "FIXED_OPENING_COMPILER_SCORE_OPTIMAL"
    )
    return candidate_proved and not incumbent_proved


def exact_compiler_for_carrier(
    catalogue: QuotientCatalogue,
    cycle: Sequence[int],
    timeout: float,
    workers: int,
    seed: int,
    output_word: Path | None,
    max_openings: int,
    require_all_targets: bool = True,
) -> dict[str, object]:
    started = time.time()
    safe_cuts = catalogue.upper_safe_cuts(list(cycle))
    complete = max_openings <= 0 or max_openings >= len(safe_cuts)
    tested = safe_cuts if complete else safe_cuts[:max_openings]
    attempts = []
    saw_unknown = False
    best_score: dict[str, object] | None = None
    for offset, cut in enumerate(tested):
        attempt = exact_compiler_for_opening(
            catalogue,
            cycle,
            cut,
            timeout,
            workers,
            seed + offset,
            output_word,
            require_all_targets,
        )
        attempts.append(attempt)
        if not require_all_targets and attempt["status"] in (
            "FIXED_OPENING_COMPILER_SCORE_OPTIMAL",
            "FIXED_OPENING_COMPILER_SCORE_FEASIBLE",
        ):
            if compiler_score_better(attempt, best_score):
                best_score = attempt
            continue
        if attempt["status"] in ("VERIFIED_OPTIMAL", "FIXED_OPENING_COMPILER_FEASIBLE"):
            return {
                "status": attempt["status"],
                "safe_opening_count": len(safe_cuts),
                "tested_openings": len(attempts),
                "opening_search_complete": complete,
                "winner": attempt,
                "wall_time": time.time() - started,
            }
        if attempt["status"] not in (
            "FIXED_OPENING_HALL_INFEASIBLE",
            "FIXED_OPENING_ADAPTIVE_CORE_INFEASIBLE",
        ):
            saw_unknown = True
    if not require_all_targets and best_score is not None:
        all_optimal = all(
            attempt["status"] == "FIXED_OPENING_COMPILER_SCORE_OPTIMAL"
            for attempt in attempts
        )
        return {
            "status": (
                "FIXED_CARRIER_COMPILER_SCORE_OPTIMAL"
                if complete and all_optimal
                else "FIXED_CARRIER_COMPILER_SCORE_BOUNDED"
            ),
            "safe_opening_count": len(safe_cuts),
            "tested_openings": len(attempts),
            "opening_search_complete": complete,
            "best": best_score,
            "attempts": attempts,
            "wall_time": time.time() - started,
            "certificate_scope": (
                "The tested upper-safe openings of this fixed directed carrier; "
                "the score is globally exact only when opening_search_complete "
                "and every opening solve is optimal."
            ),
        }
    if not safe_cuts:
        status = "NO_UPPER_SAFE_CARRIER_OPENING"
    elif not complete or saw_unknown:
        status = "COMPILER_OPENING_SEARCH_INCOMPLETE"
    else:
        status = "ALL_SAFE_OPENINGS_COMPILER_INFEASIBLE"
    return {
        "status": status,
        "safe_opening_count": len(safe_cuts),
        "tested_openings": len(attempts),
        "opening_search_complete": complete,
        "attempts": attempts,
        "wall_time": time.time() - started,
        "certificate_scope": (
            "The fixed directed carrier within the upper-safe carrier-opening, "
            "linear adaptive one-core architecture."
        ),
    }


def add_exact_shadow_for_candidate(
    catalogue: QuotientCatalogue,
    report: dict[str, object],
    selected_arcs: Sequence[int],
    lazy: list[tuple[str, object]],
    shadow_keys: set[tuple[str, int, int]],
    boundary_keys: set[tuple[int, tuple[int, ...]]],
    cut_ledger: list[dict[str, object]],
) -> int:
    added = 0
    for target in report["lower_q2_missing"]:
        key = ("intersection", 2, int(target))
        if key not in shadow_keys:
            shadow_keys.add(key)
            lazy.append(("shadow-state-path", key))
            cut_ledger.append(
                {
                    "kind": "shadow-state-path",
                    "mode": "intersection",
                    "depth": 2,
                    "target": int(target),
                }
            )
            added += 1
    for target in report["lower_q3_positive_degree_missing"]:
        key = ("intersection", 3, int(target))
        if key not in shadow_keys:
            shadow_keys.add(key)
            lazy.append(("shadow-state-path", key))
            cut_ledger.append(
                {
                    "kind": "shadow-state-path",
                    "mode": "intersection",
                    "depth": 3,
                    "target": int(target),
                }
            )
            added += 1
    chosen = set(map(int, selected_arcs))
    for target in report["upper_missing"]:
        target = int(target)
        depth = target.bit_count() - catalogue.r
        if depth <= 1:
            continue
        if depth == 2:
            key = ("union", 2, target)
            if key not in shadow_keys:
                shadow_keys.add(key)
                lazy.append(("shadow-state-path", key))
                cut_ledger.append(
                    {
                        "kind": "shadow-state-path",
                        "mode": "union",
                        "depth": 2,
                        "target": target,
                    }
                )
                added += 1
            continue
        # This is the only upper q>=3 branch.  Never replace it by a
        # fixed-q shadow-state-path.
        covered, boundary = catalogue.upper_reachability_boundary(
            target, selected_arcs
        )
        if covered:
            raise AssertionError(
                f"audit says upper target {target} is missing but reachability covers it"
            )
        key = (target, tuple(boundary))
        if key in boundary_keys:
            continue
        if chosen.intersection(boundary):
            raise AssertionError("reachability boundary contains an incumbent arc")
        boundary_keys.add(key)
        lazy.append(("upper-reachability-boundary", key))
        cut_ledger.append(
            {
                "kind": "upper-accumulated-union-boundary",
                "target": target,
                "depth": depth,
                "boundary_size": len(boundary),
                "boundary_arc_ids": boundary,
                "boundary_sha256": stable_sha256(boundary),
                "incumbent_intersection": 0,
            }
        )
        added += 1
    return added


def solve_splice_search(args: argparse.Namespace) -> dict[str, object]:
    from ortools import __version__ as ortools_version
    from ortools.sat.python import cp_model

    args.output.parent.mkdir(parents=True, exist_ok=True)
    snapshot = load_snapshot(args.factor)
    catalogue = snapshot.catalogue
    baseline = list(snapshot.selected)
    components = quotient_components(catalogue, baseline)
    component_cut_rows = [component.choices for component in components] if len(components) > 1 else []
    run_cut_rows = bad_run_cut_rows(catalogue, baseline)
    hint_arcs = oriented_factor_hint(snapshot)

    lazy: list[tuple[str, object]] = []
    shadow_keys: set[tuple[str, int, int]] = set()
    boundary_keys: set[tuple[int, tuple[int, ...]]] = set()
    cut_ledger: list[dict[str, object]] = []
    arc_nogoods: list[dict[str, object]] = []
    rounds = []
    started = time.time()

    for round_index in range(args.max_rounds):
        model, arc_vars, choice_vars = build_cp_sat_model(
            catalogue,
            lazy,
            hint_choices=baseline,
            hint_arcs=hint_arcs,
            max_choice_changes=args.radius,
            allow_cycle_cover=False,
            partial_arc_hint=True,
        )
        overlap = sum(choice_vars[index] for index in baseline)
        if args.min_changes:
            model.Add(overlap <= catalogue.N - args.min_changes)
        for row in component_cut_rows:
            model.Add(sum(choice_vars[index] for index in row) <= len(row) - 1)
        if args.add_run_cut_rows:
            for row in run_cut_rows:
                model.Add(sum(choice_vars[index] for index in row) <= len(row) - 1)
        for nogood in arc_nogoods:
            model.AddBoolOr(
                [
                    arc_vars[index].Not()
                    for index in nogood["directed_arc_ids"]
                ]
            )
        if args.maximize_overlap:
            model.Maximize(overlap)

        proto = model.Proto()
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.timeout
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed + round_index
        solve_started = time.time()
        status = solver.Solve(model)
        solve_time = time.time() - solve_started
        status_name = solver.StatusName(status)
        round_report: dict[str, object] = {
            "round": round_index,
            "status": status_name,
            "variables": len(proto.variables),
            "constraints": len(proto.constraints),
            "lazy_constraints": len(lazy),
            "arc_nogoods": len(arc_nogoods),
            "solve_time": solve_time,
        }
        rounds.append(round_report)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            base_scope = (
                "full strict quotient catalogue"
                if args.radius is None
                else f"owner-Hamming radius <= {args.radius} around the supplied factor"
            )
            if args.min_changes:
                base_scope += f", owner-Hamming distance >= {args.min_changes}"
            if arc_nogoods:
                base_scope += (
                    f", excluding {len(arc_nogoods)} directed carriers proved "
                    "infeasible for every upper-safe opening of the linear "
                    "adaptive one-core compiler"
                )
            result = {
                "schema": SCHEMA,
                "mode": "factor-splice-search",
                "status": (
                    "SPLICE_SEARCH_RELAXATION_INFEASIBLE"
                    if status == cp_model.INFEASIBLE
                    else status_name
                ),
                "certificate_scope": base_scope,
                "input": str(snapshot.path),
                "input_sha256": snapshot.sha256,
                "choice_table_sha256": catalogue.choice_table_sha256,
                "radius": args.radius,
                "min_changes": args.min_changes,
                "compiler_arc_nogoods": arc_nogoods,
                "rounds": rounds,
                "cut_ledger": cut_ledger,
                "wall_time": time.time() - started,
                "ortools_version": ortools_version,
                "hostname": socket.gethostname(),
            }
            args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            return result

        selected = [
            index for index, variable in enumerate(choice_vars) if solver.Value(variable)
        ]
        selected_arcs = [
            index for index, variable in enumerate(arc_vars) if solver.Value(variable)
        ]
        cycle, carrier_report = validate_carrier(catalogue, selected)
        overlay = overlay_report(catalogue, baseline, selected, selected_arcs)
        round_report["overlay"] = overlay
        round_report["carrier"] = carrier_report

        if not carrier_report["carrier_pass"]:
            added = add_exact_shadow_for_candidate(
                catalogue,
                carrier_report,
                selected_arcs,
                lazy,
                shadow_keys,
                boundary_keys,
                cut_ledger,
            )
            round_report["cuts_added"] = added
            if added == 0:
                # Residence, q1, connectivity and voltage are eager.  Reaching
                # this branch indicates an implementation mismatch, not a
                # license to add an unsound generic no-good.
                raise AssertionError("failed candidate produced no exact separating cut")
            continue

        carrier_payload = serialize_carrier(catalogue, selected, carrier_report)
        carrier_payload["physical_cycle"] = cycle
        carrier_payload["selected_arcs"] = selected_arcs
        carrier_payload["overlay"] = overlay
        carrier_payload["baseline"] = str(snapshot.path)
        carrier_path = args.output.with_suffix(".carrier.json")
        carrier_path.write_text(json.dumps(carrier_payload, indent=2, sort_keys=True) + "\n")

        compiler = exact_compiler_for_carrier(
            catalogue,
            cycle,
            args.compiler_timeout,
            args.workers,
            args.seed + 100000 + round_index,
            args.word,
            args.max_openings,
        )
        round_report["compiler"] = compiler
        if compiler["status"] == "VERIFIED_OPTIMAL":
            result = {
                "schema": SCHEMA,
                "mode": "factor-splice-search",
                "status": "VERIFIED_OPTIMAL",
                "input": str(snapshot.path),
                "input_sha256": snapshot.sha256,
                "choice_table_sha256": catalogue.choice_table_sha256,
                "carrier": str(carrier_path),
                "overlay": overlay,
                "carrier_report": carrier_report,
                "compiler": compiler,
                "rounds": rounds,
                "cut_ledger": cut_ledger,
                "compiler_arc_nogoods": arc_nogoods,
                "radius": args.radius,
                "min_changes": args.min_changes,
                "wall_time": time.time() - started,
                "ortools_version": ortools_version,
                "hostname": socket.gethostname(),
            }
            args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            return result

        compiler_complete_failure = compiler["status"] in (
            "NO_UPPER_SAFE_CARRIER_OPENING",
            "ALL_SAFE_OPENINGS_COMPILER_INFEASIBLE",
        )
        if compiler_complete_failure and args.exclude_compiler_failures:
            # This no-good is deliberately directed and candidate-specific.
            # No sampled-core or fixed-carrier Hall cut is promoted to a
            # global factor cut.
            directed = tuple(sorted(selected_arcs))
            arc_nogoods.append(
                {
                    "source_round": round_index,
                    "directed_arc_ids": directed,
                    "directed_arc_ids_sha256": stable_sha256(directed),
                    "compiler_audit_sha256": stable_sha256(compiler),
                    "compiler_status": compiler["status"],
                    "safe_opening_count": compiler["safe_opening_count"],
                    "tested_openings": compiler["tested_openings"],
                    "opening_search_complete": compiler["opening_search_complete"],
                }
            )
            continue

        result = {
            "schema": SCHEMA,
            "mode": "factor-splice-search",
            "status": compiler["status"],
            "input": str(snapshot.path),
            "input_sha256": snapshot.sha256,
            "choice_table_sha256": catalogue.choice_table_sha256,
            "carrier": str(carrier_path),
            "overlay": overlay,
            "carrier_report": carrier_report,
            "compiler": compiler,
            "rounds": rounds,
            "cut_ledger": cut_ledger,
            "compiler_arc_nogoods": arc_nogoods,
            "radius": args.radius,
            "min_changes": args.min_changes,
            "wall_time": time.time() - started,
            "ortools_version": ortools_version,
            "hostname": socket.gethostname(),
        }
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        return result

    result = {
        "schema": SCHEMA,
        "mode": "factor-splice-search",
        "status": "MAX_ROUNDS",
        "input": str(snapshot.path),
        "input_sha256": snapshot.sha256,
        "rounds": rounds,
        "cut_ledger": cut_ledger,
        "compiler_arc_nogoods": arc_nogoods,
        "radius": args.radius,
        "min_changes": args.min_changes,
        "wall_time": time.time() - started,
        "hostname": socket.gethostname(),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def command_audit(args: argparse.Namespace) -> None:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    rows = [audit_snapshot(load_snapshot(path)) for path in args.factors]
    result = {
        "schema": SCHEMA,
        "mode": "snapshot-audit",
        "status": "AUDITED",
        "rows": rows,
        "host": socket.gethostname(),
        "python": platform.python_version(),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


def command_fixed(args: argparse.Namespace) -> None:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    snapshot = load_snapshot(args.factor)
    audit = audit_snapshot(snapshot)
    result: dict[str, object] = {
        "schema": SCHEMA,
        "mode": "fixed-factor",
        "input": str(snapshot.path),
        "input_sha256": snapshot.sha256,
        "audit": audit,
    }
    if not audit["fixed_selector_pass"]:
        result["status"] = "FIXED_FACTOR_REJECTED"
        result["certificate_scope"] = audit["fixed_selector_scope"]
    else:
        cycle, carrier_report = validate_carrier(
            snapshot.catalogue, list(snapshot.selected)
        )
        result["carrier_report"] = carrier_report
        if args.solve_compiler or args.score:
            result["compiler"] = exact_compiler_for_carrier(
                snapshot.catalogue,
                cycle,
                args.timeout,
                args.workers,
                args.seed,
                args.word,
                args.max_openings,
                not args.score,
            )
            result["status"] = result["compiler"]["status"]
        else:
            result["status"] = "FIXED_FACTOR_CARRIER_READY"
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


def command_compile(args: argparse.Namespace) -> None:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not args.score and args.word is None:
        raise ValueError("--word is required unless --score is used")
    snapshot = load_snapshot(args.carrier)
    cycle, report = validate_carrier(snapshot.catalogue, list(snapshot.selected))
    if not report["carrier_pass"]:
        raise ValueError("compile input is not a resident all-shadow Hamilton carrier")
    result = exact_compiler_for_carrier(
        snapshot.catalogue,
        cycle,
        args.timeout,
        args.workers,
        args.seed,
        args.word,
        args.max_openings,
        not args.score,
    )
    payload = {
        "schema": SCHEMA,
        "mode": "fixed-carrier-exact-compiler",
        "input": str(snapshot.path),
        "input_sha256": snapshot.sha256,
        "carrier_report": report,
        "compiler": result,
        "status": result["status"],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit")
    audit.add_argument("factors", nargs="*", default=list(DEFAULT_INPUTS))
    audit.add_argument("--output", type=Path, required=True)

    fixed = sub.add_parser("fixed")
    fixed.add_argument("factor")
    fixed.add_argument("--output", type=Path, required=True)
    fixed.add_argument("--solve-compiler", action="store_true")
    fixed.add_argument("--word", type=Path)
    fixed.add_argument("--timeout", type=float, default=300.0)
    fixed.add_argument("--workers", type=int, default=8)
    fixed.add_argument("--seed", type=int, default=0)
    fixed.add_argument("--max-openings", type=int, default=0)
    fixed.add_argument("--score", action="store_true")

    compile_parser = sub.add_parser("compile")
    compile_parser.add_argument("carrier")
    compile_parser.add_argument("--output", type=Path, required=True)
    compile_parser.add_argument("--word", type=Path)
    compile_parser.add_argument("--timeout", type=float, default=300.0)
    compile_parser.add_argument("--workers", type=int, default=8)
    compile_parser.add_argument("--seed", type=int, default=0)
    compile_parser.add_argument("--max-openings", type=int, default=0)
    compile_parser.add_argument("--score", action="store_true")

    search = sub.add_parser("search")
    search.add_argument("factor")
    search.add_argument("--output", type=Path, required=True)
    search.add_argument("--word", type=Path, required=True)
    search.add_argument("--radius", type=int)
    search.add_argument("--min-changes", type=int, default=0)
    search.add_argument("--max-rounds", type=int, default=500)
    search.add_argument("--timeout", type=float, default=3600.0)
    search.add_argument("--compiler-timeout", type=float, default=3600.0)
    search.add_argument("--workers", type=int, default=8)
    search.add_argument("--seed", type=int, default=0)
    search.add_argument("--max-openings", type=int, default=0)
    search.add_argument("--maximize-overlap", action="store_true")
    search.add_argument("--add-run-cut-rows", action="store_true")
    search.add_argument("--exclude-compiler-failures", action="store_true")

    args = parser.parse_args()
    if args.command == "audit":
        command_audit(args)
    elif args.command == "fixed":
        command_fixed(args)
    elif args.command == "compile":
        command_compile(args)
    else:
        result = solve_splice_search(args)
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
