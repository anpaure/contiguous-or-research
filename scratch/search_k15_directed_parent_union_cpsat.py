#!/usr/bin/env python3
"""Search Hamilton paths in a directed union of certified k=15 carriers.

The catalogue contains only directed successor arcs from the supplied parent
paths.  CP-SAT's circuit constraint (with one dummy vertex) enforces one
spanning directed path.  Residence defects are forbidden by their exact
length-2..4 arc motifs.  Upper-shadow coverage is separated lazily: whenever
an audited candidate misses a target, all directed catalogue paths witnessing
that target are added as a disjunctive constraint.  Thus every accepted
candidate is exact, while the model avoids materializing millions of unused
upper witnesses.

This is a search, not a no-go proof when a per-solve time limit expires.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import ortools
from ortools.sat.python import cp_model

from audit_k15_phasefactor_safe_openings import linear_residence_violations
from k15_arc_propagated_dm_channel import (
    add_arc_propagated_compiler_channel,
    add_arc_propagated_dm_constraint,
)
from search_k15_multiroot_seam_sat import chronology_audit


K = 15
R = 8
W = 6435


def stable_object_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()


def load_path(path: Path) -> list[int]:
    payload = json.loads(path.read_text())
    row = payload.get("middle_path") or payload.get("middle_cycle")
    if not row and len(payload.get("middle_components", [])) == 1:
        row = payload["middle_components"][0]
    if not row:
        raise ValueError(f"{path}: no single middle path")
    row = list(map(int, row))
    if len(row) != W or len(set(row)) != W:
        raise ValueError(f"{path}: expected a permutation of {W} vertices")
    if any(value < 0 or value >= (1 << K) for value in row):
        raise ValueError(f"{path}: middle mask outside the 15-bit universe")
    if any(value.bit_count() != R for value in row):
        raise ValueError(f"{path}: middle mask outside rank eight")
    return row


def exact_hall(
    path: list[int], binary: Path,
    fixed_targets_files: list[Path] | None = None,
) -> dict:
    binary = binary.resolve()
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, dir="."
    ) as stream:
        json.dump({"middle_path": path}, stream)
        temp = Path(stream.name)
    try:
        reports = []
        rows = fixed_targets_files or [None]
        for fixed_targets_file in rows:
            command = [str(binary)]
            if fixed_targets_file is not None:
                command += [
                    "--fixed-targets-file", str(fixed_targets_file.resolve())
                ]
            command.append(str(temp))
            process = subprocess.run(
                command, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            if process.returncode:
                raise RuntimeError(process.stderr)
            reports.append(json.loads(process.stdout))
        report = reports[0]
        report["fixed_neighbourhoods"] = [
            row.get("fixed_neighbourhood") for row in reports
        ] if fixed_targets_files else []
        return report
    finally:
        temp.unlink(missing_ok=True)


def exact_fixed_neighbourhood(
    path: list[int], binary: Path, targets: list[int]
) -> int:
    """Independently score one frozen shore with the native Hall auditor."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, dir="."
    ) as stream:
        json.dump({"targets": targets}, stream)
        target_path = Path(stream.name)
    try:
        report = exact_hall(path, binary, [target_path])
        return int(report["fixed_neighbourhoods"][0])
    finally:
        target_path.unlink(missing_ok=True)


def selected_path(
    solver: cp_model.CpSolver,
    normal_arcs: list[tuple[int, int, cp_model.IntVar]],
    dummy_out: list[tuple[int, cp_model.IntVar]],
    dummy_in: list[tuple[int, cp_model.IntVar]],
    masks: list[int],
) -> tuple[list[int], list[int]]:
    successor: dict[int, int] = {}
    selected_indices = []
    for index, (tail, head, lit) in enumerate(normal_arcs):
        if solver.BooleanValue(lit):
            successor[tail] = head
            selected_indices.append(index)
    start = next(node for node, lit in dummy_out if solver.BooleanValue(lit))
    end = next(node for node, lit in dummy_in if solver.BooleanValue(lit))
    order = [start]
    while order[-1] != end:
        nxt = successor.get(order[-1])
        if nxt is None or nxt in order:
            raise AssertionError(("bad circuit projection", start, end, len(order)))
        order.append(nxt)
    if len(order) != W:
        raise AssertionError(("not spanning", len(order)))
    return [masks[node] for node in order], selected_indices


def residence_motifs(
    adjacency: dict[int, list[int]],
    arc_index: dict[tuple[int, int], int],
    masks: list[int],
) -> set[tuple[int, ...]]:
    """Return every directed selected-arc motif that creates a depth-3 defect."""
    forbidden: set[tuple[int, ...]] = set()

    def visit(row: list[int], indices: list[int]):
        if len(indices) >= 2 and linear_residence_violations(
            [masks[node] for node in row], 3
        ):
            forbidden.add(tuple(indices))
        if len(indices) == 4:
            return
        for nxt in adjacency[row[-1]]:
            if nxt in row:
                continue
            visit(row + [nxt], indices + [arc_index[row[-1], nxt]])

    for start in adjacency:
        visit([start], [])
    return forbidden


def target_witnesses(
    target: int,
    q: int,
    adjacency: dict[int, list[int]],
    arc_index: dict[tuple[int, int], int],
    masks: list[int],
) -> set[tuple[int, ...]]:
    """Enumerate exact q-arc directed witnesses for one upper target."""
    allowed = {
        node for node, value in enumerate(masks)
        if not (value & ~target)
    }
    answer: set[tuple[int, ...]] = set()

    def visit(row: list[int], indices: list[int], union: int):
        if len(indices) == q:
            if union == target:
                answer.add(tuple(indices))
            return
        for nxt in adjacency[row[-1]]:
            if nxt not in allowed or nxt in row:
                continue
            visit(
                row + [nxt],
                indices + [arc_index[row[-1], nxt]],
                union | masks[nxt],
            )

    for start in allowed:
        visit([start], [], masks[start])
    return answer


def add_projected_fixed_dm_constraint(
    model: cp_model.CpModel,
    motif_path: Path,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    masks: list[int],
    threshold: int,
    enforce_threshold: bool = True,
):
    """Add the proof-safe projected upper-bound inequality.

    Every true fixed-DM compiler cell projects to one selected motif, while a
    projected motif may be a false positive.  Therefore exact neighbourhood
    <= sum(indicators)+boundary_allowance, and requiring the latter to reach
    ``threshold`` is necessary but deliberately not sufficient.
    """
    lines = motif_path.read_text().splitlines()
    header = lines[0].split("\t")
    if header[0] != "K15_DIRECTED_FIXED_DM_MOTIFS_V1":
        raise ValueError("bad fixed motif header")
    cpp_edges: list[tuple[int, int] | None] = [None] * int(header[1])
    node_of = {value: node for node, value in enumerate(masks)}
    py_index = {pair: index for index, pair in enumerate(arc_pairs)}
    raw_patterns = []
    boundary_allowance = 0
    for line in lines[1:]:
        row = line.split("\t")
        if row[0] == "E":
            cpp_edges[int(row[1])] = (int(row[2]), int(row[3]))
        elif row[0] == "P":
            raw_patterns.append((int(row[1]), tuple(map(int, row[2:]))))
        elif row[0] == "B":
            boundary_allowance = int(row[1])
    if any(edge is None for edge in cpp_edges):
        raise ValueError("incomplete edge table in fixed motif file")
    cpp_to_py = []
    for first, second in cpp_edges:
        pair = (node_of[first], node_of[second])
        if pair not in py_index:
            raise ValueError(("motif edge absent from catalogue", first, second))
        cpp_to_py.append(py_index[pair])
    mapped_edge_set = {
        (node_of[first], node_of[second]) for first, second in cpp_edges
    }
    if mapped_edge_set != set(arc_pairs):
        raise ValueError((
            "fixed projected producer/consumer catalogue mismatch",
            len(mapped_edge_set), len(arc_pairs),
        ))
    indicators = []
    for serial, (depth, pattern) in enumerate(raw_patterns):
        indices = tuple(cpp_to_py[index] for index in pattern)
        indicator = model.NewBoolVar(f"fixed_p_{depth}_{serial}")
        literals = [normal_lits[index] for index in indices]
        for literal in literals:
            model.Add(indicator <= literal)
        model.Add(indicator >= sum(literals) - (len(literals) - 1))
        indicators.append(indicator)
    if enforce_threshold:
        model.Add(sum(indicators) + boundary_allowance >= threshold)
    return {
        "indicators": indicators,
        "boundary_allowance": boundary_allowance,
        "projection": int(header[3]),
        "patterns": len(indicators),
        "threshold": threshold,
        "hard_threshold": enforce_threshold,
    }


def add_projected_multi_dm_constraints(
    model: cp_model.CpModel,
    motif_path: Path,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    masks: list[int],
    thresholds: dict[str, int],
    enforce_threshold: bool = True,
):
    """Add every labelled inequality from one native multi-DM traversal.

    ``fast_k15_directed_multi_dm_projection`` enumerates the same projected
    three-arc palettes for several DM target families in one catalogue DFS.
    Consuming that format directly avoids rebuilding a four-parent catalogue
    once per witness family.
    """
    lines = motif_path.read_text().splitlines()
    header = lines[0].split("\t")
    if header[0] != "K15_DIRECTED_MULTI_DM_PROJECTION_V1":
        raise ValueError("bad multi fixed motif header")
    edge_count = int(header[1])
    witness_count = int(header[2])
    projection = int(header[3])
    cpp_edges: list[tuple[int, int] | None] = [None] * edge_count
    labels: dict[int, str] = {}
    raw: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    boundary: dict[int, int] = defaultdict(int)
    for line in lines[1:]:
        row = line.split("\t")
        if row[0] == "E":
            cpp_edges[int(row[1])] = (int(row[2]), int(row[3]))
        elif row[0] == "W":
            labels[int(row[1])] = row[2]
        elif row[0] == "P":
            raw[int(row[1])].append(
                (int(row[2]), tuple(map(int, row[3:])))
            )
        elif row[0] == "B":
            boundary[int(row[1])] = int(row[2])
    if any(edge is None for edge in cpp_edges):
        raise ValueError("incomplete edge table in multi fixed motif file")
    if set(labels) != set(range(witness_count)):
        raise ValueError("incomplete witness labels in multi fixed motif file")
    missing = set(labels.values()) - set(thresholds)
    extra = set(thresholds) - set(labels.values())
    if missing or extra:
        raise ValueError(("multi threshold labels", sorted(missing), sorted(extra)))

    node_of = {value: node for node, value in enumerate(masks)}
    py_index = {pair: index for index, pair in enumerate(arc_pairs)}
    cpp_to_py = []
    for first, second in cpp_edges:
        pair = (node_of[first], node_of[second])
        if pair not in py_index:
            raise ValueError(("multi motif edge absent", first, second))
        cpp_to_py.append(py_index[pair])
    mapped_edge_set = {
        (node_of[first], node_of[second]) for first, second in cpp_edges
    }
    if mapped_edge_set != set(arc_pairs):
        raise ValueError((
            "multi fixed producer/consumer catalogue mismatch",
            len(mapped_edge_set), len(arc_pairs),
        ))

    answer = []
    for witness in range(witness_count):
        label = labels[witness]
        indicators = []
        for serial, (depth, pattern) in enumerate(raw[witness]):
            indices = tuple(cpp_to_py[index] for index in pattern)
            indicator = model.NewBoolVar(
                f"multi_fixed_{label}_{depth}_{serial}"
            )
            literals = [normal_lits[index] for index in indices]
            for literal in literals:
                model.Add(indicator <= literal)
            model.Add(indicator >= sum(literals) - (len(literals) - 1))
            indicators.append(indicator)
        threshold = thresholds[label]
        allowance = boundary[witness]
        if enforce_threshold:
            model.Add(sum(indicators) + allowance >= threshold)
        answer.append({
            "indicators": indicators,
            "label": label,
            "boundary_allowance": allowance,
            "projection": projection,
            "patterns": len(indicators),
            "threshold": threshold,
            "hard_threshold": enforce_threshold,
            "source": str(motif_path),
        })
    return answer


def add_required_target_motifs(
    model: cp_model.CpModel,
    motif_path: Path,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    masks: list[int],
    dummy_out: list[tuple[int, cp_model.IntVar]],
    dummy_in: list[tuple[int, cp_model.IntVar]],
):
    """Require one exact interior/endpoint compiler witness per target."""
    lines = motif_path.read_text().splitlines()
    header = lines[0].split("\t")
    if header[0] != "K15_DIRECTED_FIXED_DM_MOTIFS_V1":
        raise ValueError("bad target motif header")
    cpp_edges: list[tuple[int, int] | None] = [None] * int(header[1])
    raw = []
    required_targets = []
    for line in lines[1:]:
        row = line.split("\t")
        if row[0] == "E":
            cpp_edges[int(row[1])] = (int(row[2]), int(row[3]))
        elif row[0] == "Q":
            required_targets.append(int(row[1]))
        elif row[0] == "T":
            raw.append(("I", int(row[1]), None, tuple(map(int, row[3:]))))
        elif row[0] == "TL":
            raw.append(("L", int(row[1]), int(row[2]), tuple(map(int, row[3:]))))
        elif row[0] == "TR":
            raw.append(("R", int(row[1]), int(row[2]), tuple(map(int, row[3:]))))
    if any(edge is None for edge in cpp_edges):
        raise ValueError("incomplete edge table in target motif file")
    node_of = {value: node for node, value in enumerate(masks)}
    py_index = {pair: index for index, pair in enumerate(arc_pairs)}
    cpp_to_py = []
    for first, second in cpp_edges:
        pair = (node_of[first], node_of[second])
        if pair not in py_index:
            raise ValueError(("target motif edge absent", first, second))
        cpp_to_py.append(py_index[pair])
    mapped_edge_set = {
        (node_of[first], node_of[second]) for first, second in cpp_edges
    }
    if mapped_edge_set != set(arc_pairs):
        raise ValueError((
            "required-target producer/consumer catalogue mismatch",
            len(mapped_edge_set), len(arc_pairs),
        ))
    start_lit = {masks[node]: lit for node, lit in dummy_out}
    end_lit = {masks[node]: lit for node, lit in dummy_in}
    by_target: dict[int, list[cp_model.IntVar]] = defaultdict(list)
    for target in required_targets:
        by_target[target] = []
    by_kind = Counter()
    for serial, (kind, target, endpoint, pattern) in enumerate(raw):
        witness = model.NewBoolVar(f"target_{target}_{kind}_{serial}")
        for index in pattern:
            model.AddImplication(witness, normal_lits[cpp_to_py[index]])
        if kind == "L":
            model.AddImplication(witness, start_lit[endpoint])
        elif kind == "R":
            model.AddImplication(witness, end_lit[endpoint])
        by_target[target].append(witness)
        by_kind[kind] += 1
    for target, witnesses in by_target.items():
        model.AddBoolOr(witnesses)
    return {
        "targets": len(by_target),
        "patterns": len(raw),
        "by_kind": dict(sorted(by_kind.items())),
        "per_target": {str(target): len(rows) for target, rows in by_target.items()},
    }


def add_exact_fixed_dm_constraint(
    model: cp_model.CpModel,
    motif_path: Path,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    masks: list[int],
    dummy_out: list[tuple[int, cp_model.IntVar]],
    dummy_in: list[tuple[int, cp_model.IntVar]],
    threshold: int,
    interior_only: bool = False,
    boundary_upper_only: bool = False,
    enforce_threshold: bool = True,
):
    """Encode an exact fixed-DM neighbourhood lower bound.

    Native ``projection=0, per_target=0`` files contain one full local motif
    for every positive interior compiler cell and weighted complete endpoint
    palettes.  In a selected Hamilton path each such motif occurs at most
    once, while exactly one left and right endpoint palette is active.  The
    resulting weighted sum is therefore the exact neighbourhood size, unlike
    the deliberately one-sided short projections consumed above.
    """
    lines = motif_path.read_text().splitlines()
    header = lines[0].split("\t")
    if header[0] != "K15_DIRECTED_FIXED_DM_MOTIFS_V1":
        raise ValueError("bad exact fixed motif header")
    if int(header[3]) != 0 or int(header[4]) != 0:
        raise ValueError("exact fixed motif file must use projection=per_target=0")
    cpp_edges: list[tuple[int, int] | None] = [None] * int(header[1])
    raw: list[tuple[str, int, int | None, tuple[int, ...]]] = []
    boundary_max: dict[str, dict[int, int]] = {
        "L": defaultdict(int), "R": defaultdict(int)
    }
    for line in lines[1:]:
        row = line.split("\t")
        if row[0] == "E":
            cpp_edges[int(row[1])] = (int(row[2]), int(row[3]))
        elif row[0] == "I":
            raw.append(("I", 1, None, tuple(map(int, row[2:]))))
        elif row[0] in {"L", "R"}:
            if not interior_only:
                if boundary_upper_only:
                    boundary_max[row[0]][int(row[2])] = max(
                        boundary_max[row[0]][int(row[2])], int(row[1])
                    )
                else:
                    raw.append((
                        row[0], int(row[1]), int(row[2]),
                        tuple(map(int, row[3:])),
                    ))
    if any(edge is None for edge in cpp_edges):
        raise ValueError("incomplete edge table in exact fixed motif file")
    node_of = {value: node for node, value in enumerate(masks)}
    py_index = {pair: index for index, pair in enumerate(arc_pairs)}
    cpp_to_py = []
    mapped_edge_set = set()
    for first, second in cpp_edges:
        pair = (node_of[first], node_of[second])
        if pair not in py_index:
            raise ValueError(("exact fixed motif edge absent", first, second))
        mapped_edge_set.add(pair)
        cpp_to_py.append(py_index[pair])
    # A full exact motif table is relative to one directed catalogue.  Mere
    # containment is insufficient: a table generated on a pair face omits
    # positive mixed-parent words and its endpoint maxima range over the wrong
    # collar language.  Restricted-face tables remain valid when consumed on
    # that same face, but must never masquerade as exact in a larger union.
    consumer_edge_set = set(arc_pairs)
    if mapped_edge_set != consumer_edge_set:
        raise ValueError((
            "exact fixed motif catalogue mismatch",
            len(mapped_edge_set), len(consumer_edge_set),
            len(mapped_edge_set - consumer_edge_set),
            len(consumer_edge_set - mapped_edge_set),
        ))
    start_lit = {masks[node]: lit for node, lit in dummy_out}
    end_lit = {masks[node]: lit for node, lit in dummy_in}
    weighted_terms = []
    by_kind = Counter()
    for serial, (kind, weight, endpoint, pattern) in enumerate(raw):
        indicator = model.NewBoolVar(f"exact_fixed_{kind}_{serial}")
        literals = [normal_lits[cpp_to_py[index]] for index in pattern]
        if kind == "L":
            literals.append(start_lit[endpoint])
        elif kind == "R":
            literals.append(end_lit[endpoint])
        for literal in literals:
            model.Add(indicator <= literal)
        model.Add(indicator >= sum(literals) - (len(literals) - 1))
        weighted_terms.append(weight * indicator)
        by_kind[kind] += 1
    if boundary_upper_only and not interior_only:
        for endpoint, weight in boundary_max["L"].items():
            weighted_terms.append(weight * start_lit[endpoint])
        for endpoint, weight in boundary_max["R"].items():
            weighted_terms.append(weight * end_lit[endpoint])
        by_kind["L_upper_endpoints"] = len(boundary_max["L"])
        by_kind["R_upper_endpoints"] = len(boundary_max["R"])
    if enforce_threshold:
        model.Add(sum(weighted_terms) >= threshold)
    return {
        "weighted_terms": weighted_terms,
        "threshold": threshold,
        "patterns": len(raw),
        "by_kind": dict(sorted(by_kind.items())),
        "source": str(motif_path),
        "hard_threshold": enforce_threshold,
    }


def _equivalent_and(model: cp_model.CpModel, output, inputs) -> None:
    """Encode output iff the conjunction of Boolean literals in inputs."""
    model.AddBoolAnd(inputs).OnlyEnforceIf(output)
    model.AddBoolOr([literal.Not() for literal in inputs] + [output])


def _equivalent_or(model: cp_model.CpModel, output, inputs) -> None:
    """Encode output iff the disjunction of Boolean literals in inputs."""
    model.AddBoolOr(inputs).OnlyEnforceIf(output)
    for literal in inputs:
        model.AddImplication(literal, output)


def add_compact_order_channel(
    model: cp_model.CpModel,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    dummy_out: list[tuple[int, cp_model.IntVar]],
    dummy_in: list[tuple[int, cp_model.IntVar]],
    masks: list[int],
    global_compiler: bool = False,
):
    """Share one inverse-order channel with the selected directed circuit.

    The circuit contains one dummy, hence one linear Hamilton path on the W
    physical vertices.  ``position[node]`` and ``node_at[position]`` are exact
    inverse permutations.  Only the first/last nine masks are decomposed for
    the endpoint compiler; the same order supplies the two-layer interior
    guards.
    """
    start_lits = [None] * W
    end_lits = [None] * W
    for node, literal in dummy_out:
        start_lits[node] = literal
    for node, literal in dummy_in:
        end_lits[node] = literal
    if any(literal is None for literal in start_lits + end_lits):
        raise ValueError("incomplete dummy endpoint literal table")

    position = [
        model.NewIntVar(0, W - 1, f"compact_position_{node}")
        for node in range(W)
    ]
    node_at = [
        model.NewIntVar(0, W - 1, f"compact_node_at_{index}")
        for index in range(W)
    ]
    model.AddInverse(position, node_at)
    for (tail, head), literal in zip(arc_pairs, normal_lits):
        model.Add(position[head] == position[tail] + 1).OnlyEnforceIf(literal)
    for node, literal in dummy_out:
        model.Add(position[node] == 0).OnlyEnforceIf(literal)
    for node, literal in dummy_in:
        model.Add(position[node] == W - 1).OnlyEnforceIf(literal)

    middle_bits = None
    if global_compiler:
        middle_bits = []
        for index in range(W):
            mask = model.NewIntVar(
                0, (1 << K) - 1, f"global_middle_mask_{index}"
            )
            model.AddElement(node_at[index], masks, mask)
            bits = [
                model.NewBoolVar(f"global_middle_{index}_{coordinate}")
                for coordinate in range(K)
            ]
            model.Add(mask == sum(
                (1 << coordinate) * bits[coordinate]
                for coordinate in range(K)
            ))
            middle_bits.append(bits)

    endpoint_bits: dict[str, list[list[cp_model.IntVar]]] = {"L": [], "R": []}
    for side in ("L", "R"):
        for offset in range(9):
            index = offset if side == "L" else W - 1 - offset
            if middle_bits is not None:
                endpoint_bits[side].append(middle_bits[index])
                continue
            mask = model.NewIntVar(0, (1 << K) - 1,
                                   f"compact_{side}_mask_{offset}")
            model.AddElement(node_at[index], masks, mask)
            bits = [
                model.NewBoolVar(f"compact_{side}_middle_{offset}_{coordinate}")
                for coordinate in range(K)
            ]
            model.Add(mask == sum(
                (1 << coordinate) * bits[coordinate]
                for coordinate in range(K)
            ))
            endpoint_bits[side].append(bits)

    endpoint_allowed: dict[str, list[list[cp_model.IntVar]]] = {"L": [], "R": []}
    for side in ("L", "R"):
        for letter in range(9):
            row = []
            for coordinate in range(K):
                value = model.NewBoolVar(
                    f"compact_{side}_allowed_{letter}_{coordinate}"
                )
                _equivalent_and(
                    model, value,
                    [endpoint_bits[side][middle][coordinate]
                     for middle in range(max(0, letter - 3), letter + 1)],
                )
                row.append(value)
            endpoint_allowed[side].append(row)

    left_guard = []
    right_guard = []
    for node in range(W):
        left = model.NewBoolVar(f"compact_not_first_two_{node}")
        model.Add(position[node] >= 2).OnlyEnforceIf(left)
        model.Add(position[node] <= 1).OnlyEnforceIf(left.Not())
        left_guard.append(left)
        right = model.NewBoolVar(f"compact_not_last_two_{node}")
        model.Add(position[node] <= W - 3).OnlyEnforceIf(right)
        model.Add(position[node] >= W - 2).OnlyEnforceIf(right.Not())
        right_guard.append(right)

    # The envelope and mandatory masks depend only on the endpoint chronology,
    # not on the target shore, so all compact exact models share them.
    boundary_state = {"L": {}, "R": {}}
    for side in ("L", "R"):
        allowed = endpoint_allowed[side]
        for depth in range(3):
            for start in range(6):
                envelope = []
                mandatory = []
                for coordinate in range(K):
                    env = model.NewBoolVar(
                        f"compact_{side}_envelope_{depth}_{start}_{coordinate}"
                    )
                    _equivalent_or(
                        model, env,
                        [allowed[p][coordinate]
                         for p in range(start, start + depth + 1)],
                    )
                    envelope.append(env)
                    if start + depth < 3:
                        blocker = allowed[start + depth + 1][coordinate]
                    else:
                        blocker = model.NewBoolVar(
                            f"compact_{side}_blocker_{depth}_{start}_{coordinate}"
                        )
                        _equivalent_and(model, blocker, [
                            allowed[start - 1][coordinate],
                            allowed[start + depth + 1][coordinate],
                        ])
                    mand = model.NewBoolVar(
                        f"compact_{side}_mandatory_{depth}_{start}_{coordinate}"
                    )
                    _equivalent_and(model, mand, [env, blocker.Not()])
                    mandatory.append(mand)
                boundary_state[side][depth, start] = (envelope, mandatory)

    answer = {
        "position": position,
        "node_at": node_at,
        "allowed": endpoint_allowed,
        "boundary_state": boundary_state,
        "start_lits": start_lits,
        "end_lits": end_lits,
        "left_guard": left_guard,
        "right_guard": right_guard,
    }
    if not global_compiler:
        return answer

    # The authoritative depth-three erosion has W+3 positions.  Its three
    # compiler rows therefore contain (W+3)+(W+2)+(W+1)=19,311 cells.
    allowed = []
    for erosion_position in range(W + 3):
        row = []
        for coordinate in range(K):
            value = model.NewBoolVar(
                f"global_allowed_{erosion_position}_{coordinate}"
            )
            _equivalent_and(model, value, [
                middle_bits[middle_position][coordinate]
                for middle_position in range(
                    max(0, erosion_position - 3),
                    min(erosion_position, W - 1) + 1,
                )
            ])
            row.append(value)
        allowed.append(row)

    cells = []
    for depth in range(3):
        for start in range(W + 3 - depth):
            envelope = []
            mandatory = []
            for coordinate in range(K):
                env = model.NewBoolVar(
                    f"global_envelope_{depth}_{start}_{coordinate}"
                )
                _equivalent_or(model, env, [
                    allowed[position][coordinate]
                    for position in range(start, start + depth + 1)
                ])
                envelope.append(env)

                mand = model.NewBoolVar(
                    f"global_mandatory_{depth}_{start}_{coordinate}"
                )
                if start + depth < 3:
                    # No occurrence lies far enough to the left to supply a
                    # carrier escaping through the left boundary.
                    blocker = allowed[start + depth + 1][coordinate]
                    _equivalent_and(model, mand, [env, blocker.Not()])
                elif start >= W:
                    # The reversed statement at the right boundary.
                    blocker = allowed[start - 1][coordinate]
                    _equivalent_and(model, mand, [env, blocker.Not()])
                else:
                    # Interior/cross-boundary identity:
                    # M = E ∩ ¬(Q_{b-1} ∩ Q_{b+h+1}).  Encoding this
                    # directly saves one Boolean blocker per coordinate.
                    left = allowed[start - 1][coordinate]
                    right = allowed[start + depth + 1][coordinate]
                    model.AddImplication(mand, env)
                    model.AddBoolOr([mand.Not(), left.Not(), right.Not()])
                    model.AddBoolOr([env.Not(), left, mand])
                    model.AddBoolOr([env.Not(), right, mand])
                mandatory.append(mand)
            cells.append({
                "depth": depth,
                "start": start,
                "allowed": allowed[start:start + depth + 1],
                "envelope": envelope,
                "mandatory": mandatory,
            })
    if len(cells) != 19311:
        raise AssertionError(("bad global compiler cell count", len(cells)))
    answer["global_middle"] = middle_bits
    answer["global_allowed"] = allowed
    answer["global_cells"] = cells
    return answer


def _compact_boundary_score(path: list[int], targets: list[int], reverse=False) -> int:
    """Deterministically evaluate the exact 18-cell endpoint contribution."""
    row = path[:9] if not reverse else list(reversed(path[-9:]))
    full = (1 << K) - 1
    allowed = []
    for letter in range(9):
        value = full
        for middle in range(max(0, letter - 3), letter + 1):
            value &= row[middle]
        allowed.append(value)
    score = 0
    for depth in range(3):
        for start in range(6):
            envelope = 0
            for letter in range(start, start + depth + 1):
                envelope |= allowed[letter]
            if start + depth < 3:
                mandatory = envelope & ~allowed[start + depth + 1]
            else:
                mandatory = envelope & ~(
                    allowed[start - 1] & allowed[start + depth + 1]
                )
            mandatory &= full
            if any(
                not (mandatory & ~target)
                and not (target & ~envelope)
                and all(
                    allowed[letter] & target
                    for letter in range(start, start + depth + 1)
                )
                for target in targets
            ):
                score += 1
    return score


def evaluate_adaptive_exact_model(path: list[int], row: dict) -> dict:
    """Evaluate one adaptive-exact shore without consulting solver auxiliaries."""
    selected = set(zip(path, path[1:]))
    position = {value: index for index, value in enumerate(path)}
    by_depth = [0, 0, 0]
    for depth, pairs, first, last in row["pattern_pairs"]:
        if (
            position[first] >= 2
            and position[last] <= W - 3
            and all(pair in selected for pair in pairs)
        ):
            by_depth[depth] += 1
    left = _compact_boundary_score(path, row["targets"], False)
    right = _compact_boundary_score(path, row["targets"], True)
    return {
        "interior_by_depth": by_depth,
        "interior": sum(by_depth),
        "left_boundary": left,
        "right_boundary": right,
        "total": sum(by_depth) + left + right,
    }


def add_adaptive_exact_multi_dm_constraints(
    model: cp_model.CpModel,
    motif_path: Path,
    normal_lits: list[cp_model.IntVar],
    arc_pairs: list[tuple[int, int]],
    masks: list[int],
    thresholds: dict[str, int],
    order_channel: dict,
    enforce_threshold: bool = True,
):
    """Consume exact centered 5/6/7 states plus exact 8-edge endpoints.

    The file is self-contained: every fixed shore target is serialized as a
    Q row.  Interior indicators are exact conjunctions with the two-layer
    endpoint guards.  Each of the 36 boundary claims chooses one fitting shore
    target; this one-way certificate is equisatisfiable with the exact Hall
    inequality and cannot receive blanket or endpoint-only credit.
    """
    lines = motif_path.read_text().splitlines()
    header = lines[0].split("\t")
    if (
        len(header) != 3
        or header[0] != "K15_DIRECTED_MULTI_DM_CENTERED_EXACT_V2"
    ):
        raise ValueError("bad adaptive exact motif header")
    edge_count = int(header[1])
    witness_count = int(header[2])
    if edge_count <= 0 or witness_count <= 0:
        raise ValueError(("nonpositive adaptive exact dimensions", header))
    cpp_edges: list[tuple[int, int] | None] = [None] * edge_count
    labels: dict[int, str] = {}
    target_counts: dict[int, int] = {}
    witness_sources: dict[int, str] = {}
    targets: dict[int, list[int]] = defaultdict(list)
    raw: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    locality = {}
    declared_counts = {}
    z_row = None
    for line_number, line in enumerate(lines[1:], 2):
        fields = line.split("\t")
        if fields[0] == "D":
            if len(fields) != 5:
                raise ValueError(("bad D row", line_number))
            depth = int(fields[1])
            if depth in locality:
                raise ValueError(("duplicate D row", depth, line_number))
            locality[depth] = tuple(map(int, fields[2:]))
        elif fields[0] == "E":
            if len(fields) != 4:
                raise ValueError(("bad E row", line_number))
            edge = int(fields[1])
            if not 0 <= edge < edge_count:
                raise ValueError(("E index out of range", edge, line_number))
            if cpp_edges[edge] is not None:
                raise ValueError(("duplicate E row", edge, line_number))
            cpp_edges[edge] = (int(fields[2]), int(fields[3]))
        elif fields[0] == "W":
            if len(fields) != 5:
                raise ValueError(("bad W row", line_number))
            witness = int(fields[1])
            if not 0 <= witness < witness_count:
                raise ValueError(("W index out of range", witness, line_number))
            if witness in labels:
                raise ValueError(("duplicate W row", witness, line_number))
            labels[witness] = fields[2]
            target_counts[witness] = int(fields[3])
            witness_sources[witness] = fields[4]
            if (
                not labels[witness]
                or target_counts[witness] <= 0
                or not witness_sources[witness]
            ):
                raise ValueError(("bad W payload", witness, line_number))
        elif fields[0] == "Q":
            if len(fields) != 3:
                raise ValueError(("bad Q row", line_number))
            witness = int(fields[1])
            if not 0 <= witness < witness_count:
                raise ValueError(("Q witness out of range", witness, line_number))
            targets[witness].append(int(fields[2]))
        elif fields[0] == "P":
            if len(fields) < 4:
                raise ValueError(("bad P row", line_number))
            witness = int(fields[1])
            if not 0 <= witness < witness_count:
                raise ValueError(("P witness out of range", witness, line_number))
            raw[witness].append((
                int(fields[2]), tuple(map(int, fields[3:]))
            ))
        elif fields[0] == "C":
            if len(fields) != 4:
                raise ValueError(("bad C row", line_number))
            witness = int(fields[1])
            depth = int(fields[2])
            if not 0 <= witness < witness_count or depth not in (0, 1, 2):
                raise ValueError(("C index out of range", witness, depth, line_number))
            key = (witness, depth)
            if key in declared_counts:
                raise ValueError(("duplicate C row", key, line_number))
            declared_counts[key] = int(fields[3])
            if declared_counts[key] < 0:
                raise ValueError(("negative C count", key, line_number))
        elif fields[0] == "Z":
            if len(fields) != 3 or z_row is not None:
                raise ValueError(("bad or duplicate Z row", line_number))
            z_row = tuple(map(int, fields[1:]))
        else:
            raise ValueError(("unknown adaptive exact row", fields[0], line_number))
    if locality != {0: (5, 2, 2), 1: (6, 2, 2), 2: (7, 2, 2)}:
        raise ValueError(("adaptive exact locality metadata", locality))
    if any(edge is None for edge in cpp_edges):
        raise ValueError("incomplete adaptive exact edge table")
    if len(set(cpp_edges)) != edge_count:
        raise ValueError("duplicate adaptive exact catalogue edge")
    if set(labels) != set(range(witness_count)):
        raise ValueError("incomplete adaptive exact witness labels")
    if len(set(labels.values())) != witness_count:
        raise ValueError(("duplicate adaptive exact witness label", labels))
    if set(labels.values()) != set(thresholds):
        raise ValueError(("adaptive exact thresholds", labels, thresholds))
    for witness in range(witness_count):
        if len(targets[witness]) != target_counts[witness]:
            raise ValueError(("adaptive exact target count", witness))
        if len(set(targets[witness])) != len(targets[witness]):
            raise ValueError(("duplicate adaptive exact target", witness))
        if any(
            not (0 < target < (1 << K) and 0 < target.bit_count() < R)
            for target in targets[witness]
        ):
            raise ValueError(("adaptive exact target outside lower universe", witness))
        if thresholds[labels[witness]] != len(targets[witness]):
            raise ValueError((
                "adaptive exact threshold must equal shore size",
                labels[witness], thresholds[labels[witness]], len(targets[witness]),
            ))
        observed = Counter(depth for depth, unused in raw[witness])
        for depth in range(3):
            if declared_counts.get((witness, depth)) != observed[depth]:
                raise ValueError(("adaptive exact declared count", witness, depth))
    if z_row is None or len(z_row) != 2:
        raise ValueError("missing adaptive exact Z row")
    if z_row[1] != sum(len(rows) for rows in raw.values()):
        raise ValueError("adaptive exact Z total mismatch")

    if any(
        not (0 <= value < (1 << K) and value.bit_count() == R)
        for value in masks
    ):
        raise ValueError("consumer middle catalogue is not rank eight on [15]")
    node_of = {value: node for node, value in enumerate(masks)}
    py_index = {pair: index for index, pair in enumerate(arc_pairs)}
    cpp_to_py = []
    for first, second in cpp_edges:
        if first not in node_of or second not in node_of:
            raise ValueError(("adaptive exact edge has noncatalogue endpoint", first, second))
        pair = (node_of[first], node_of[second])
        if pair not in py_index:
            raise ValueError(("adaptive exact edge absent", first, second))
        cpp_to_py.append(py_index[pair])
    mapped_edge_set = {
        (node_of[first], node_of[second]) for first, second in cpp_edges
    }
    if mapped_edge_set != set(arc_pairs):
        raise ValueError((
            "adaptive exact catalogue does not equal consumer catalogue",
            len(mapped_edge_set), len(arc_pairs),
        ))

    answer = []
    for witness in range(witness_count):
        label = labels[witness]
        safe_label = f"w{witness}_" + "".join(
            ch if ch.isalnum() else "_" for ch in label
        )
        interior = []
        pattern_pairs = []
        pattern_histogram = Counter()
        seen_patterns = set()
        for serial, (depth, pattern) in enumerate(raw[witness]):
            if depth not in (0, 1, 2) or len(pattern) != 5 + depth:
                raise ValueError(("bad adaptive exact pattern", depth, len(pattern)))
            if any(not 0 <= edge < edge_count for edge in pattern):
                raise ValueError(("adaptive exact P edge out of range", witness, depth))
            key = (depth, pattern)
            if key in seen_patterns:
                raise ValueError(("duplicate adaptive exact pattern", witness, depth))
            seen_patterns.add(key)
            pairs = [cpp_edges[index] for index in pattern]
            if any(
                pairs[index][1] != pairs[index + 1][0]
                for index in range(len(pairs) - 1)
            ):
                raise ValueError(("non-chain adaptive exact pattern", witness, depth))
            vertices = [pairs[0][0]] + [pair[1] for pair in pairs]
            if len(set(vertices)) != len(vertices):
                raise ValueError(("repeated adaptive exact vertex", witness, depth))
            indices = tuple(cpp_to_py[index] for index in pattern)
            first_mask = cpp_edges[pattern[0]][0]
            last_mask = cpp_edges[pattern[-1]][1]
            first_node = node_of[first_mask]
            last_node = node_of[last_mask]
            literals = [normal_lits[index] for index in indices] + [
                order_channel["left_guard"][first_node],
                order_channel["right_guard"][last_node],
            ]
            indicator = model.NewBoolVar(
                f"adaptive_{safe_label}_interior_{depth}_{serial}"
            )
            _equivalent_and(model, indicator, literals)
            interior.append(indicator)
            pattern_pairs.append((
                depth,
                tuple(cpp_edges[index] for index in pattern),
                first_mask,
                last_mask,
            ))
            pattern_histogram[depth] += 1

        boundary_claims = []
        target_values = targets[witness]
        for side in ("L", "R"):
            allowed = order_channel["allowed"][side]
            for depth in range(3):
                for start in range(6):
                    claim = model.NewBoolVar(
                        f"adaptive_{safe_label}_{side}_claim_{depth}_{start}"
                    )
                    target_index = model.NewIntVar(
                        0, len(target_values) - 1,
                        f"adaptive_{safe_label}_{side}_target_index_{depth}_{start}",
                    )
                    target_mask = model.NewIntVar(
                        0, (1 << K) - 1,
                        f"adaptive_{safe_label}_{side}_target_mask_{depth}_{start}",
                    )
                    model.AddElement(target_index, target_values, target_mask)
                    target_bits = [
                        model.NewBoolVar(
                            f"adaptive_{safe_label}_{side}_target_{depth}_{start}_{x}"
                        )
                        for x in range(K)
                    ]
                    model.Add(target_mask == sum(
                        (1 << coordinate) * target_bits[coordinate]
                        for coordinate in range(K)
                    ))
                    envelope, mandatory = order_channel["boundary_state"][side][
                        depth, start
                    ]
                    for coordinate in range(K):
                        model.AddBoolOr([
                            claim.Not(), target_bits[coordinate].Not(),
                            envelope[coordinate],
                        ])
                        model.AddBoolOr([
                            claim.Not(), mandatory[coordinate].Not(),
                            target_bits[coordinate],
                        ])
                    for letter in range(start, start + depth + 1):
                        meets = []
                        for coordinate in range(K):
                            meet = model.NewBoolVar(
                                f"adaptive_{safe_label}_{side}_meet_"
                                f"{depth}_{start}_{letter}_{coordinate}"
                            )
                            _equivalent_and(model, meet, [
                                target_bits[coordinate],
                                allowed[letter][coordinate],
                            ])
                            meets.append(meet)
                        model.AddBoolOr([claim.Not()] + meets)
                    boundary_claims.append(claim)

        threshold = thresholds[label]
        terms = interior + boundary_claims
        if enforce_threshold:
            model.Add(sum(terms) >= threshold)
        answer.append({
            "label": label,
            "threshold": threshold,
            "interior_indicators": interior,
            "boundary_claims": boundary_claims,
            "terms": terms,
            "patterns": len(interior),
            "pattern_histogram": dict(sorted(pattern_histogram.items())),
            "targets": target_values,
            "pattern_pairs": pattern_pairs,
            "source": str(motif_path),
            "target_source": witness_sources[witness],
            "interface": "adaptive_exact_5_6_7_plus_endpoint_8",
            "hard_threshold": enforce_threshold,
        })
    return answer


def fixed_dm_score(row: dict):
    """Return the encoded score expression for any fixed-shore row."""
    if "weighted_terms" in row:
        return sum(row["weighted_terms"])
    if "terms" in row:
        return sum(row["terms"])
    if "indicators" in row:
        return sum(row["indicators"]) + row.get("boundary_allowance", 0)
    raise ValueError(("fixed row has no score expression", sorted(row)))


def enforce_fixed_dm_threshold(model: cp_model.CpModel, row: dict) -> None:
    """Install one suppressed hard row after the soft homotopy solve."""
    if row.get("hard_threshold"):
        raise ValueError(("fixed threshold already enforced", row.get("label")))
    model.Add(fixed_dm_score(row) >= int(row["threshold"]))
    row["hard_threshold"] = True


def replace_path_hints(
    model: cp_model.CpModel,
    path: list[int],
    node_of: dict[int, int],
    arc_pairs: list[tuple[int, int]],
    normal_lits: list[cp_model.IntVar],
    dummy_out: list[tuple[int, cp_model.IntVar]],
    dummy_in: list[tuple[int, cp_model.IntVar]],
) -> None:
    """Replace all earlier hints by the supplied complete Hamilton path."""
    nodes = [node_of[value] for value in path]
    selected = set(zip(nodes, nodes[1:]))
    model.ClearHints()
    for pair, literal in zip(arc_pairs, normal_lits):
        model.AddHint(literal, int(pair in selected))
    for node, literal in dummy_out:
        model.AddHint(literal, int(node == nodes[0]))
    for node, literal in dummy_in:
        model.AddHint(literal, int(node == nodes[-1]))


def evaluate_global_exact_shore(path: list[int], targets: list[int]) -> dict:
    """Evaluate one shore by both exact mandatory-mask definitions.

    ``formula_cells`` uses the compact left/interior/right identity encoded in
    CP-SAT.  ``carrier_cells`` independently reconstructs every complete
    occurrence carrier, as the native Hall auditor does.  Equality of the two
    cell lists is a mandatory calibration, not a heuristic comparison.
    """
    if len(path) != W or len(set(path)) != W:
        raise ValueError("global exact shore evaluator needs one Hamilton path")
    shore = set(map(int, targets))
    if not shore or len(shore) != len(targets):
        raise ValueError("global exact shore must be nonempty and duplicate-free")
    if any(
        not (0 < target < (1 << K) and 0 < target.bit_count() < R)
        for target in shore
    ):
        raise ValueError("global exact shore target outside the lower universe")
    full = (1 << K) - 1
    allowed = []
    for position in range(W + 3):
        value = full
        for middle in range(
            max(0, position - 3), min(position, W - 1) + 1
        ):
            value &= path[middle]
        allowed.append(value)

    # This is the literal carrier_required table in fast_k15_hall_dm.cpp.
    carrier_required: dict[tuple[int, ...], int] = defaultdict(int)
    for occurrence, middle_mask in enumerate(path):
        value = middle_mask
        while value:
            bit = value & -value
            value -= bit
            carrier = tuple(
                position for position in range(occurrence, occurrence + 4)
                if allowed[position] & bit
            )
            if not carrier:
                raise AssertionError((
                    "empty complete carrier", occurrence, bit.bit_length() - 1,
                ))
            carrier_required[carrier] |= bit

    def fits(envelope: int, mandatory: int, masks_in_cell: list[int]) -> bool:
        candidate = envelope
        while candidate:
            if (
                candidate in shore
                and not (mandatory & ~candidate)
                and all(candidate & mask for mask in masks_in_cell)
            ):
                return True
            candidate = (candidate - 1) & envelope
        return False

    formula_cells = []
    carrier_cells = []
    depth_histogram = Counter()
    cell_index = 0
    for depth in range(3):
        for start in range(W + 3 - depth):
            positions = list(range(start, start + depth + 1))
            envelope = 0
            for position in positions:
                envelope |= allowed[position]
            if start + depth < 3:
                formula_mandatory = envelope & ~allowed[start + depth + 1]
            elif start >= W:
                formula_mandatory = envelope & ~allowed[start - 1]
            else:
                formula_mandatory = envelope & ~(
                    allowed[start - 1] & allowed[start + depth + 1]
                )
            formula_mandatory &= full

            carrier_mandatory = 0
            for subset_bits in range(1, 1 << len(positions)):
                subset = tuple(
                    positions[index] for index in range(len(positions))
                    if (subset_bits >> index) & 1
                )
                carrier_mandatory |= carrier_required.get(subset, 0)
            if formula_mandatory != carrier_mandatory:
                raise AssertionError((
                    "mandatory identity mismatch", depth, start,
                    formula_mandatory, carrier_mandatory,
                ))

            formula_fit = fits(
                envelope, formula_mandatory,
                [allowed[position] for position in positions],
            )
            carrier_fit = fits(
                envelope, carrier_mandatory,
                [allowed[position] for position in positions],
            )
            if formula_fit:
                formula_cells.append(cell_index)
                depth_histogram[depth] += 1
            if carrier_fit:
                carrier_cells.append(cell_index)
            cell_index += 1
    if cell_index != 19311:
        raise AssertionError(("bad evaluated compiler cell count", cell_index))
    if formula_cells != carrier_cells:
        raise AssertionError((
            "formula/carrier neighbourhood mismatch",
            len(formula_cells), len(carrier_cells),
        ))
    return {
        "targets": len(shore),
        "cells": cell_index,
        "total": len(formula_cells),
        "formula_cells": formula_cells,
        "carrier_cells": carrier_cells,
        "depth_histogram": dict(sorted(depth_histogram.items())),
    }


def add_global_exact_dm_constraint(
    model: cp_model.CpModel,
    order_channel: dict,
    targets: list[int],
    allowance: int,
    cut_index: int,
) -> dict:
    """Add one exact Hall-shore inequality over the shared compiler channel.

    A claim is only allowed to be true when its chosen target fits that cell.
    Conversely, all auxiliary meet bits are free to take their witnessing
    values, so a fitting cell can be claimed.  Therefore

        sum(cell claims) >= |A| - allowance

    is equisatisfiable with |N(A)| >= |A| - allowance.
    """
    if "global_cells" not in order_channel:
        raise ValueError("global exact DM cuts need the global compiler channel")
    target_values = list(map(int, targets))
    if not target_values or len(set(target_values)) != len(target_values):
        raise ValueError("global exact DM shore must be nonempty and unique")
    if any(
        not (0 < target < (1 << K) and 0 < target.bit_count() < R)
        for target in target_values
    ):
        raise ValueError("global exact DM target outside the lower universe")
    threshold = len(target_values) - allowance
    if threshold <= 0:
        raise ValueError(("vacuous global exact DM threshold", threshold))

    claims = []
    meet_count = 0
    for cell_index, cell in enumerate(order_channel["global_cells"]):
        claim = model.NewBoolVar(f"allshore_{cut_index}_claim_{cell_index}")
        target_index = model.NewIntVar(
            0, len(target_values) - 1,
            f"allshore_{cut_index}_target_index_{cell_index}",
        )
        target_mask = model.NewIntVar(
            0, (1 << K) - 1,
            f"allshore_{cut_index}_target_mask_{cell_index}",
        )
        model.AddElement(target_index, target_values, target_mask)
        target_bits = []
        for coordinate in range(K):
            bit = model.NewBoolVar(
                f"allshore_{cut_index}_target_{cell_index}_{coordinate}"
            )
            target_bits.append(bit)
            # Under a true claim, T is contained in the envelope and contains
            # the complete-carrier mandatory mask.
            model.AddBoolOr([
                claim.Not(), bit.Not(), cell["envelope"][coordinate],
            ])
            model.AddBoolOr([
                claim.Not(), cell["mandatory"][coordinate].Not(), bit,
            ])
        model.Add(target_mask == sum(
            (1 << coordinate) * target_bits[coordinate]
            for coordinate in range(K)
        ))

        for offset, allowed in enumerate(cell["allowed"]):
            # A single chosen coordinate witnesses Q_p \cap T != empty.  This
            # is exactly the same existential condition as fifteen AND gates,
            # but replaces 579,300 per-cut meet Booleans by 38,620 selectors.
            witness_coordinate = model.NewIntVar(
                0, K - 1,
                f"allshore_{cut_index}_meet_coordinate_{cell_index}_{offset}",
            )
            target_meet = model.NewBoolVar(
                f"allshore_{cut_index}_target_meet_{cell_index}_{offset}"
            )
            allowed_meet = model.NewBoolVar(
                f"allshore_{cut_index}_allowed_meet_{cell_index}_{offset}"
            )
            model.AddElement(witness_coordinate, target_bits, target_meet)
            model.AddElement(witness_coordinate, allowed, allowed_meet)
            model.AddImplication(claim, target_meet)
            model.AddImplication(claim, allowed_meet)
            meet_count += 1
        claims.append(claim)

    model.Add(sum(claims) >= threshold)
    return {
        "cut": cut_index,
        "targets": target_values,
        "target_count": len(target_values),
        "allowance": allowance,
        "threshold": threshold,
        "claims": claims,
        "target_bit_variables": len(claims) * K,
        "meet_coordinate_selectors": meet_count,
        "interface": "global_exact_19311_position_channel",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path, nargs="+")
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--hall-bin", type=Path, default=Path("./fast_k15_hall_dm"))
    ap.add_argument("--seconds", type=float, default=300.0)
    ap.add_argument("--workers", type=int, default=24)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--rounds", type=int, default=100)
    ap.add_argument("--include-reverses", action="store_true")
    ap.add_argument(
        "--parent-dummy-only", action="store_true",
        help=(
            "restrict dummy->start and end->dummy arcs to augmented arcs "
            "present in the supplied parent circuits"
        ),
    )
    ap.add_argument(
        "--escape-parent-subset", action="append", default=[],
        metavar="I,J,...",
        help=(
            "require at least one selected augmented arc whose complete "
            "parent support is disjoint from the listed nonempty proper "
            "subset; repeat for pair/hierarchical escape cuts"
        ),
    )
    ap.add_argument(
        "--restrict-parent-subset",
        metavar="I,J,...",
        help=(
            "restrict every selected augmented arc to the union of these "
            "zero-based parents while retaining the full input catalogue"
        ),
    )
    ap.add_argument(
        "--minimal-parent-cover", action="store_true",
        help=(
            "with --restrict-parent-subset, require a selected augmented "
            "arc uniquely supplied (within the subset) by each listed parent"
        ),
    )
    ap.add_argument("--save-all", action="store_true")
    ap.add_argument("--fixed-motif-file", type=Path, action="append", default=[])
    ap.add_argument("--multi-fixed-motif-file", type=Path)
    ap.add_argument(
        "--multi-fixed-threshold", action="append", default=[],
        metavar="LABEL=VALUE",
        help="labelled threshold for --multi-fixed-motif-file",
    )
    ap.add_argument("--fixed-targets-file", type=Path, action="append", default=[])
    ap.add_argument("--fixed-threshold", type=int, action="append", default=[])
    ap.add_argument("--maximize-fixed-upper-bound", action="store_true")
    ap.add_argument(
        "--maximize-fixed-min-slack", action="store_true",
        help=(
            "maximize the minimum surplus over every projected and exact "
            "fixed-DM threshold inside the existing hard-feasible region"
        ),
    )
    ap.add_argument(
        "--soft-fixed-homotopy", action="store_true",
        help=(
            "first suppress every fixed-DM hard threshold, maximize their "
            "signed minimum margin, then restore the hard rows and use the "
            "soft incumbent only as a solver hint"
        ),
    )
    ap.add_argument(
        "--hint-path", type=Path,
        help="write the soft-homotopy incumbent used to hint the hard phase",
    )
    ap.add_argument(
        "--maximize-parent-arcs", type=int, default=-1,
        help="maximize overlap with this parent (overrides fixed-bound objective)",
    )
    ap.add_argument(
        "--min-parent-arcs", action="append", default=[], metavar="INDEX=COUNT",
        help=(
            "hard lower bound on selected normal arcs belonging to a parent; "
            "for the H29 parent this gives an exact finite successor-support "
            "budget up to the separately audited dummy endpoint"
        ),
    )
    ap.add_argument("--require-target-motif-file", type=Path)
    ap.add_argument(
        "--exact-fixed-motif-file", type=Path, action="append", default=[]
    )
    ap.add_argument(
        "--exact-fixed-threshold", type=int, action="append", default=[]
    )
    ap.add_argument(
        "--exact-fixed-interior-only", action="store_true",
        help="ignore exact endpoint palettes (stronger but much smaller model)",
    )
    ap.add_argument(
        "--exact-fixed-interior-only-index", type=int, action="append", default=[],
        help="zero-based exact fixed model index whose endpoint palettes are ignored",
    )
    ap.add_argument(
        "--exact-fixed-boundary-upper", action="store_true",
        help=(
            "replace full endpoint motifs by the proof-safe maximum boundary "
            "weight conditional on the selected start/end vertex"
        ),
    )
    ap.add_argument("--adaptive-exact-motif-file", type=Path)
    ap.add_argument(
        "--adaptive-exact-threshold", action="append", default=[],
        metavar="LABEL=VALUE",
        help=(
            "exact labelled Hall row from one self-contained centered "
            "5/6/7 plus endpoint-8 motif file"
        ),
    )
    ap.add_argument(
        "--dynamic-exact-dm", action="store_true",
        help=(
            "run an exact all-shore Benders loop over one shared 19,311-cell "
            "arc-propagated compiler channel"
        ),
    )
    ap.add_argument(
        "--legacy-position-exact-dm", action="store_true",
        help=(
            "use the old all-position AddInverse/AddElement exact-DM channel "
            "for regression; the default exact channel propagates erosion "
            "masks directly on selected catalogue arcs"
        ),
    )
    ap.add_argument(
        "--global-exact-dm-shore", type=Path, action="append", default=[],
        help=(
            "repeatable saved moving-DM shore JSON; impose its target list "
            "as a hard allowance-zero position-indexed Hall row over this "
            "consumer catalogue"
        ),
    )
    ap.add_argument(
        "--global-exact-allowance-shore",
        type=Path,
        action="append",
        default=[],
        help=(
            "repeatable, independently versioned exact position-indexed "
            "shore row with an explicit nonnegative allowance; unlike "
            "--global-exact-dm-shore this may encode |N(A)|>=|A|-a"
        ),
    )
    ap.add_argument(
        "--dynamic-dm-allowance", type=int, default=28,
        help=(
            "require |N(A)| >= |A|-ALLOWANCE for every dynamically returned "
            "DM shore (28 asks for a certified improvement below Hall 29)"
        ),
    )
    ap.add_argument(
        "--dynamic-dm-continue", action="store_true",
        help=(
            "after reaching the requested allowance, exclude the incumbent "
            "and continue looking for Hall zero until --rounds is exhausted"
        ),
    )
    ap.add_argument(
        "--hint-parent", type=int, default=0,
        help="seed CP-SAT with this parent path; use -1 for no hint",
    )
    ap.add_argument(
        "--initial-hint-path", type=Path,
        help=(
            "replace the parent hint by this already audited Hamilton path; "
            "every normal arc must belong to the current consumer catalogue"
        ),
    )
    ap.add_argument(
        "--fix-parent", type=int,
        help="fix the complete circuit to this parent index (regression only)",
    )
    ap.add_argument("--force-start-mask", type=int)
    ap.add_argument("--force-end-mask", type=int)
    ap.add_argument("--force-tuple-json", type=Path)
    ap.add_argument(
        "--min-parent-windows", action="append", default=[],
        metavar="INDEX=COUNT",
        help="require COUNT selected full windows inherited from parent INDEX",
    )
    ap.add_argument("--parent-window-length", type=int, default=11)
    ap.add_argument(
        "--balance-parent-windows", default="",
        help="comma-separated parent indices; maximize their minimum window count",
    )
    ap.add_argument(
        "--skip-residence", action="store_true",
        help="exploratory mode: do not encode or reject residence defects",
    )
    ap.add_argument(
        "--stop-after-first-candidate", action="store_true",
        help="stop after the first residence/upper-complete Hall-audited path",
    )
    args = ap.parse_args()

    if args.soft_fixed_homotopy != (args.hint_path is not None):
        raise ValueError(
            "--soft-fixed-homotopy and --hint-path must be supplied together"
        )
    if args.soft_fixed_homotopy and (
        args.maximize_fixed_upper_bound
        or args.maximize_fixed_min_slack
        or args.maximize_parent_arcs >= 0
        or bool(args.balance_parent_windows)
    ):
        raise ValueError(
            "--soft-fixed-homotopy is incompatible with other objectives"
        )
    objective_modes = sum((
        bool(args.maximize_fixed_upper_bound),
        bool(args.maximize_fixed_min_slack),
        bool(args.soft_fixed_homotopy),
        args.maximize_parent_arcs >= 0,
        bool(args.balance_parent_windows),
    ))
    if objective_modes > 1:
        raise ValueError("choose at most one CP-SAT objective mode")

    parents = [load_path(path) for path in args.source]
    masks = sorted(parents[0])
    if any(sorted(row) != masks for row in parents[1:]):
        raise ValueError("parent paths do not span the same middle layer")
    node_of = {mask: node for node, mask in enumerate(masks)}

    def parse_parent_indices(
        specification: str, option: str, *, proper: bool,
    ) -> tuple[int, ...]:
        fields = specification.split(",")
        if not fields or any(not field.strip() for field in fields):
            raise ValueError((f"{option} must be comma-separated", specification))
        try:
            listed = [int(field.strip()) for field in fields]
        except ValueError as error:
            raise ValueError((f"noninteger {option} index", specification)) from error
        if len(set(listed)) != len(listed):
            raise ValueError((f"duplicate {option} index", specification))
        if any(not 0 <= index < len(parents) for index in listed):
            raise ValueError((f"out-of-range {option} index", specification))
        subset = tuple(sorted(listed))
        if not subset or (proper and len(subset) == len(parents)):
            raise ValueError((f"{option} has invalid size", specification))
        return subset

    restricted_parent_subset = (
        parse_parent_indices(
            args.restrict_parent_subset, "--restrict-parent-subset", proper=False,
        )
        if args.restrict_parent_subset is not None else None
    )
    if args.minimal_parent_cover and restricted_parent_subset is None:
        raise ValueError(
            "--minimal-parent-cover requires --restrict-parent-subset"
        )
    if (
        restricted_parent_subset is not None
        or args.minimal_parent_cover
        or args.escape_parent_subset
    ) and not args.parent_dummy_only:
        raise ValueError(
            "parent support branching/escape cuts require --parent-dummy-only"
        )
    if (
        restricted_parent_subset is not None or args.escape_parent_subset
    ) and args.include_reverses:
        raise ValueError(
            "parent support branching/escape cuts require ordinary orientations"
        )
    if args.escape_parent_subset and args.skip_residence:
        raise ValueError(
            "certified pair-escape cuts cannot be used with --skip-residence"
        )

    arc_sources: dict[tuple[int, int], set[int]] = defaultdict(set)
    parent_starts: set[int] = set()
    parent_ends: set[int] = set()
    parent_start_sources: dict[int, set[int]] = defaultdict(set)
    parent_end_sources: dict[int, set[int]] = defaultdict(set)
    for parent_index, row in enumerate(parents):
        oriented_rows = [row]
        if args.include_reverses:
            oriented_rows.append(list(reversed(row)))
        for oriented in oriented_rows:
            parent_starts.add(node_of[oriented[0]])
            parent_ends.add(node_of[oriented[-1]])
            parent_start_sources[node_of[oriented[0]]].add(parent_index)
            parent_end_sources[node_of[oriented[-1]]].add(parent_index)
            for first, second in zip(oriented, oriented[1:]):
                arc_sources[node_of[first], node_of[second]].add(parent_index)
    arc_pairs = sorted(arc_sources)
    arc_index = {arc: index for index, arc in enumerate(arc_pairs)}
    # Reconstruct the literal mask-edge catalogue independently of the
    # node-indexed consumer table.  The exact-DM channel requires equality
    # with this set; containment would unsoundly admit a restricted pair-face
    # motif language in the full five-parent union.
    expected_full_mask_catalogue = set()
    for row in parents:
        oriented_rows = [row]
        if args.include_reverses:
            oriented_rows.append(list(reversed(row)))
        for oriented in oriented_rows:
            expected_full_mask_catalogue.update(zip(oriented, oriented[1:]))
    adjacency: dict[int, list[int]] = {node: [] for node in range(W)}
    for tail, head in arc_pairs:
        adjacency[tail].append(head)

    model = cp_model.CpModel()
    normal_lits = [model.NewBoolVar(f"a_{tail}_{head}") for tail, head in arc_pairs]
    normal_arcs = [
        (tail, head, normal_lits[index])
        for index, (tail, head) in enumerate(arc_pairs)
    ]
    dummy = W
    dummy_out = [
        (node, model.NewBoolVar(f"start_{node}")) for node in range(W)
    ]
    dummy_in = [
        (node, model.NewBoolVar(f"end_{node}")) for node in range(W)
    ]
    if args.parent_dummy_only:
        for node, literal in dummy_out:
            if node not in parent_starts:
                model.Add(literal == 0)
        for node, literal in dummy_in:
            if node not in parent_ends:
                model.Add(literal == 0)
    circuit = list(normal_arcs)
    circuit.extend((dummy, node, lit) for node, lit in dummy_out)
    circuit.extend((node, dummy, lit) for node, lit in dummy_in)
    model.AddCircuit(circuit)

    # Parent support is attached to the augmented successor arc, including
    # the dummy cut.  This is essential: a path can otherwise appear to leave
    # a pair face only by choosing another parent's endpoint.
    augmented_parent_arcs = []
    for pair, literal in zip(arc_pairs, normal_lits):
        augmented_parent_arcs.append((
            "normal", pair, frozenset(arc_sources[pair]), literal,
        ))
    for node, literal in dummy_out:
        augmented_parent_arcs.append((
            "start", node, frozenset(parent_start_sources[node]), literal,
        ))
    for node, literal in dummy_in:
        augmented_parent_arcs.append((
            "end", node, frozenset(parent_end_sources[node]), literal,
        ))

    restricted_parent_model = None
    if restricted_parent_subset is not None:
        allowed = frozenset(restricted_parent_subset)
        forbidden_augmented = [
            literal for unused_kind, unused_key, support, literal
            in augmented_parent_arcs
            if support.isdisjoint(allowed)
        ]
        for literal in forbidden_augmented:
            model.Add(literal == 0)
        minimal_witness_counts = {}
        if args.minimal_parent_cover:
            for parent in restricted_parent_subset:
                witnesses = [
                    literal for unused_kind, unused_key, support, literal
                    in augmented_parent_arcs
                    if parent in support
                    and support.intersection(allowed) == {parent}
                ]
                model.AddBoolOr(witnesses)
                minimal_witness_counts[str(parent)] = len(witnesses)
        restricted_parent_model = {
            "parent_indices": list(restricted_parent_subset),
            "forbidden_augmented_arcs": len(forbidden_augmented),
            "minimal_parent_cover": args.minimal_parent_cover,
            "minimal_witness_counts": minimal_witness_counts,
        }

    escape_parent_subset_models = []
    seen_escape_parent_subsets: set[tuple[int, ...]] = set()
    for specification in args.escape_parent_subset:
        subset = parse_parent_indices(
            specification, "--escape-parent-subset", proper=True,
        )
        if subset in seen_escape_parent_subsets:
            raise ValueError((
                "duplicate --escape-parent-subset", specification, subset,
            ))
        seen_escape_parent_subsets.add(subset)
        subset_set = frozenset(subset)
        escape_entries = [
            (kind, key, literal)
            for kind, key, support, literal in augmented_parent_arcs
            if support and support.isdisjoint(subset_set)
        ]
        if not escape_entries:
            raise ValueError((
                "--escape-parent-subset has no augmented arc outside its "
                "parent-face union", specification, subset,
            ))
        model.AddBoolOr([literal for unused_kind, unused_key, literal in escape_entries])
        kind_counts = Counter(kind for kind, unused_key, unused_lit in escape_entries)
        escape_parent_subset_models.append({
            "specification": specification,
            "parent_indices": list(subset),
            "escape_augmented_arc_count": len(escape_entries),
            "escape_by_kind": dict(sorted(kind_counts.items())),
        })

    if args.force_start_mask is not None:
        forced = node_of[args.force_start_mask]
        model.Add(dict(dummy_out)[forced] == 1)
    if args.force_end_mask is not None:
        forced = node_of[args.force_end_mask]
        model.Add(dict(dummy_in)[forced] == 1)
    forced_tuple = None
    if args.force_tuple_json is not None:
        forced_tuple = json.loads(args.force_tuple_json.read_text())
        tuple_arcs = set()
        for motif in forced_tuple["motifs"]:
            vertices = list(map(int, motif["vertices"]))
            tuple_arcs.update(zip(vertices, vertices[1:]))
        for first, second in tuple_arcs:
            pair = (node_of[first], node_of[second])
            if pair not in arc_index:
                raise ValueError(("forced tuple arc absent", first, second))
            model.Add(normal_lits[arc_index[pair]] == 1)
        model.Add(dict(dummy_out)[node_of[int(forced_tuple["start_mask"])]] == 1)
        model.Add(dict(dummy_in)[node_of[int(forced_tuple["end_mask"])]] == 1)
    if args.hint_parent >= 0:
        hinted = parents[args.hint_parent]
        hinted_nodes = [node_of[value] for value in hinted]
        hinted_arcs = set(zip(hinted_nodes, hinted_nodes[1:]))
        for index, pair in enumerate(arc_pairs):
            model.AddHint(normal_lits[index], int(pair in hinted_arcs))
        for node, lit in dummy_out:
            model.AddHint(lit, int(node == hinted_nodes[0]))
        for node, lit in dummy_in:
            model.AddHint(lit, int(node == hinted_nodes[-1]))
    if args.fix_parent is not None:
        if not 0 <= args.fix_parent < len(parents):
            raise ValueError("bad --fix-parent index")
        fixed_nodes = [node_of[value] for value in parents[args.fix_parent]]
        fixed_arcs = set(zip(fixed_nodes, fixed_nodes[1:]))
        for pair, literal in zip(arc_pairs, normal_lits):
            model.Add(literal == int(pair in fixed_arcs))
        for node, literal in dummy_out:
            model.Add(literal == int(node == fixed_nodes[0]))
        for node, literal in dummy_in:
            model.Add(literal == int(node == fixed_nodes[-1]))
    if args.initial_hint_path is not None:
        if args.fix_parent is not None:
            raise ValueError("--initial-hint-path is incompatible with --fix-parent")
        external_hint = load_path(args.initial_hint_path)
        if sorted(external_hint) != masks:
            raise ValueError("initial hint does not span the current middle layer")
        external_pairs = set(zip(external_hint, external_hint[1:]))
        catalogue_mask_pairs = {
            (masks[tail], masks[head]) for tail, head in arc_pairs
        }
        absent = external_pairs - catalogue_mask_pairs
        if absent:
            raise ValueError(("initial hint arc absent from catalogue", len(absent)))
        replace_path_hints(
            model, external_hint, node_of, arc_pairs, normal_lits,
            dummy_out, dummy_in,
        )

    if args.dynamic_dm_allowance < 0:
        raise ValueError("--dynamic-dm-allowance must be nonnegative")
    if args.dynamic_dm_continue and not args.dynamic_exact_dm:
        raise ValueError("--dynamic-dm-continue requires --dynamic-exact-dm")
    preloaded_dm_shores = []
    seen_preloaded_shores: set[tuple[int, ...]] = set()

    def load_preloaded_global_shore(
        shore_path: Path,
        *,
        expected_format: str,
        hard_zero: bool,
        interface: str,
    ) -> dict:
        payload = json.loads(shore_path.read_text())
        raw_targets = payload.get("dm_targets", payload.get("targets"))
        if raw_targets is None:
            raise ValueError((
                "global exact DM shore has no dm_targets/targets", shore_path,
            ))
        targets = tuple(map(int, raw_targets))
        if not targets or len(set(targets)) != len(targets):
            raise ValueError(("invalid global exact DM target list", shore_path))
        shore_key = tuple(sorted(targets))
        if shore_key in seen_preloaded_shores:
            raise ValueError(("duplicate global exact DM shore", shore_path))
        seen_preloaded_shores.add(shore_key)
        declared_threshold = payload.get("threshold")
        declared_allowance = payload.get("allowance")
        if declared_allowance is None:
            allowance = (
                len(targets) - int(declared_threshold)
                if declared_threshold is not None else 0
            )
        else:
            allowance = int(declared_allowance)
        threshold = len(targets) - allowance
        if allowance < 0 or threshold <= 0:
            raise ValueError(("invalid global exact DM allowance", shore_path))
        if declared_threshold is not None and int(declared_threshold) != threshold:
            raise ValueError(("inconsistent global exact DM threshold", shore_path))
        if payload.get("format") != expected_format:
            raise ValueError(("unversioned global exact DM shore", shore_path))
        if hard_zero and (allowance != 0 or threshold != len(targets)):
            raise ValueError((
                "persisted moving-DM shores must be hard allowance zero",
                shore_path, allowance, threshold,
            ))
        source_candidate = Path(payload.get("candidate", ""))
        if not source_candidate.is_file():
            raise ValueError(("global shore source candidate is missing", shore_path))
        source_digest = hashlib.sha256(source_candidate.read_bytes()).hexdigest()
        if source_digest != payload.get("candidate_sha256"):
            raise ValueError(("global shore source hash mismatch", shore_path))
        saved_cells = list(map(int, payload.get("dm_cell_indices", [])))
        if (
            len(set(saved_cells)) != len(saved_cells)
            or any(not 0 <= cell < 19311 for cell in saved_cells)
        ):
            raise ValueError(("invalid saved DM cell list", shore_path))
        source_row = load_path(source_candidate)
        if hard_zero:
            # A persisted moving-DM separator must literally be the canonical
            # deficient shore returned on its source chronology.
            source_native = exact_hall(source_row, args.hall_bin)
            if tuple(sorted(map(int, source_native.get("dm_targets", [])))) != tuple(
                sorted(targets)
            ):
                raise ValueError(("saved/native DM target-list mismatch", shore_path))
            if sorted(map(int, source_native.get("dm_cell_indices", []))) != sorted(
                saved_cells
            ):
                raise ValueError(("saved/native DM cell-list mismatch", shore_path))
        else:
            # An allowance shore can be any frozen target family.  The old
            # degree-zero portal family is not the source chronology's DM
            # shore, so certify its neighbourhood with the independent
            # fixed-target native interface instead.
            source_native_total = exact_fixed_neighbourhood(
                source_row, args.hall_bin, list(targets)
            )
            if source_native_total != len(saved_cells):
                raise ValueError((
                    "saved/native allowance-shore cell-count mismatch",
                    shore_path, len(saved_cells), source_native_total,
                ))
        source_evaluation = evaluate_global_exact_shore(
            source_row, list(targets)
        )
        if sorted(source_evaluation["formula_cells"]) != sorted(saved_cells):
            raise ValueError((
                "saved native/formula DM cell-list mismatch", shore_path,
                len(saved_cells), source_evaluation["total"],
            ))
        if sorted(source_evaluation["carrier_cells"]) != sorted(saved_cells):
            raise ValueError((
                "saved native/carrier DM cell-list mismatch", shore_path,
                len(saved_cells), source_evaluation["total"],
            ))
        if (
            int(payload.get("deficiency", -1))
            != len(targets) - len(saved_cells)
        ):
            raise ValueError(("saved DM deficiency mismatch", shore_path))
        return {
            "path": str(shore_path.resolve()),
            "path_sha256": hashlib.sha256(shore_path.read_bytes()).hexdigest(),
            "label": payload.get("label", shore_path.stem),
            "targets": targets,
            "allowance": allowance,
            "threshold": threshold,
            "source_candidate": str(source_candidate.resolve()),
            "source_candidate_sha256": source_digest,
            "source_cell_count": len(saved_cells),
            "source_deficiency": len(targets) - len(saved_cells),
            "source_cell_indices_sha256": hashlib.sha256(
                json.dumps(sorted(saved_cells), separators=(",", ":")).encode()
            ).hexdigest(),
            "preload_interface": interface,
        }

    for shore_path in args.global_exact_dm_shore:
        preloaded_dm_shores.append(load_preloaded_global_shore(
            shore_path,
            expected_format="K15_POSITION_EXACT_DM_SHORE_V1",
            hard_zero=True,
            interface="hard_zero_moving_dm",
        ))
    for shore_path in args.global_exact_allowance_shore:
        preloaded_dm_shores.append(load_preloaded_global_shore(
            shore_path,
            expected_format="K15_POSITION_EXACT_ALLOWANCE_SHORE_V1",
            hard_zero=False,
            interface="explicit_static_allowance",
        ))
    exact_dm_requested = bool(args.dynamic_exact_dm or preloaded_dm_shores)
    if args.legacy_position_exact_dm and not exact_dm_requested:
        raise ValueError(
            "--legacy-position-exact-dm needs a dynamic/preloaded exact shore"
        )
    order_channel = None
    if (
        args.adaptive_exact_motif_file is not None
        or (exact_dm_requested and args.legacy_position_exact_dm)
    ):
        order_channel = add_compact_order_channel(
            model, normal_lits, arc_pairs, dummy_out, dummy_in, masks,
            global_compiler=bool(
                exact_dm_requested and args.legacy_position_exact_dm
            ),
        )
    elif args.adaptive_exact_threshold:
        raise ValueError(
            "--adaptive-exact-threshold requires --adaptive-exact-motif-file"
        )

    arc_propagated_channel = None
    if exact_dm_requested and not args.legacy_position_exact_dm:
        arc_propagated_channel = add_arc_propagated_compiler_channel(
            model, normal_lits, arc_pairs, dummy_out, dummy_in, masks,
            coordinate_count=K,
            expected_catalogue_mask_edges=expected_full_mask_catalogue,
        )

    def add_exact_dm_shore(
        targets: list[int], allowance: int, cut_index: int,
    ) -> dict:
        if args.legacy_position_exact_dm:
            return add_global_exact_dm_constraint(
                model, order_channel, targets, allowance, cut_index,
            )
        if arc_propagated_channel is None:
            raise AssertionError("missing arc-propagated exact-DM channel")
        return add_arc_propagated_dm_constraint(
            model, arc_propagated_channel, targets, allowance, cut_index,
            coordinate_count=K, middle_rank=R,
        )

    preloaded_dm_models = []
    for cut_index, shore in enumerate(preloaded_dm_shores):
        encoded = add_exact_dm_shore(
            list(shore["targets"]), int(shore["allowance"]), cut_index,
        )
        encoded.update({
            "path": shore["path"],
            "path_sha256": shore["path_sha256"],
            "label": shore["label"],
            "preloaded": True,
            "source_candidate": shore["source_candidate"],
            "source_candidate_sha256": shore["source_candidate_sha256"],
            "source_cell_count": shore["source_cell_count"],
            "source_deficiency": shore["source_deficiency"],
            "source_cell_indices_sha256": shore[
                "source_cell_indices_sha256"
            ],
            "preload_interface": shore["preload_interface"],
        })
        preloaded_dm_models.append(encoded)

    parent_window_models = []
    if args.parent_window_length < 2:
        raise ValueError("parent window length must be at least two vertices")
    window_requirements: dict[int, int] = {}
    for specification in args.min_parent_windows:
        if "=" not in specification:
            raise ValueError("parent window requirements must be INDEX=COUNT")
        parent_text, count_text = specification.split("=", 1)
        parent_index = int(parent_text)
        count = int(count_text)
        if not (0 <= parent_index < len(parents)) or count <= 0:
            raise ValueError(("bad parent window requirement", specification))
        if parent_index in window_requirements:
            raise ValueError(("duplicate parent window requirement", parent_index))
        window_requirements[parent_index] = count
    balanced_parents = set()
    if args.balance_parent_windows:
        balanced_parents = {
            int(value) for value in args.balance_parent_windows.split(",")
            if value != ""
        }
        if any(not (0 <= parent < len(parents)) for parent in balanced_parents):
            raise ValueError("bad --balance-parent-windows index")
    window_sums = {}
    for parent_index in sorted(set(window_requirements) | balanced_parents):
        count = window_requirements.get(parent_index)
        row = parents[parent_index]
        length = args.parent_window_length
        indicators = []
        for start in range(len(row) - length + 1):
            indices = [
                arc_index[(node_of[row[at]], node_of[row[at + 1]])]
                for at in range(start, start + length - 1)
            ]
            indicator = model.NewBoolVar(
                f"parent_window_{parent_index}_{start}"
            )
            literals = [normal_lits[index] for index in indices]
            for literal in literals:
                model.Add(indicator <= literal)
            model.Add(indicator >= sum(literals) - (len(literals) - 1))
            indicators.append(indicator)
        window_sum = sum(indicators)
        window_sums[parent_index] = window_sum
        if count is not None:
            model.Add(window_sum >= count)
        parent_window_models.append({
            "parent": parent_index,
            "count": count,
            "length": length,
            "indicators": indicators,
        })
    balanced_window_min = None
    if balanced_parents:
        balanced_window_min = model.NewIntVar(0, W, "balanced_window_min")
        for parent_index in sorted(balanced_parents):
            model.Add(balanced_window_min <= window_sums[parent_index])
        model.Maximize(balanced_window_min)

    forbidden = set() if args.skip_residence else residence_motifs(
        adjacency, arc_index, masks
    )
    for motif in forbidden:
        model.AddBoolOr([normal_lits[index].Not() for index in motif])

    fixed_models = []
    if len(args.fixed_motif_file) != len(args.fixed_threshold):
        raise ValueError("each --fixed-motif-file needs one --fixed-threshold")
    for motif_file, threshold in zip(
        args.fixed_motif_file, args.fixed_threshold
    ):
        if threshold <= 0:
            raise ValueError("fixed thresholds must be positive")
        row = add_projected_fixed_dm_constraint(
            model, motif_file, normal_lits, arc_pairs, masks, threshold,
            enforce_threshold=not args.soft_fixed_homotopy,
        )
        row["threshold"] = threshold
        row["source"] = str(motif_file)
        fixed_models.append(row)
    if args.multi_fixed_motif_file is not None:
        thresholds = {}
        for specification in args.multi_fixed_threshold:
            if "=" not in specification:
                raise ValueError("multi thresholds must be LABEL=VALUE")
            label, value = specification.split("=", 1)
            if label in thresholds:
                raise ValueError(("duplicate multi threshold", label))
            thresholds[label] = int(value)
        if not thresholds or any(value <= 0 for value in thresholds.values()):
            raise ValueError("positive --multi-fixed-threshold values required")
        fixed_models.extend(add_projected_multi_dm_constraints(
            model, args.multi_fixed_motif_file, normal_lits,
            arc_pairs, masks, thresholds,
            enforce_threshold=not args.soft_fixed_homotopy,
        ))
    elif args.multi_fixed_threshold:
        raise ValueError(
            "--multi-fixed-threshold requires --multi-fixed-motif-file"
        )
    if args.fixed_targets_file and (
        len(args.fixed_targets_file) != len(fixed_models)
    ):
        raise ValueError(
            "fixed target files must align with all single/multi fixed models"
        )
    target_motif_model = None
    if args.require_target_motif_file is not None:
        target_motif_model = add_required_target_motifs(
            model, args.require_target_motif_file, normal_lits, arc_pairs,
            masks, dummy_out, dummy_in,
        )
    if len(args.exact_fixed_motif_file) != len(args.exact_fixed_threshold):
        raise ValueError(
            "each --exact-fixed-motif-file needs one --exact-fixed-threshold"
        )
    exact_fixed_models = []
    interior_only_indices = set(args.exact_fixed_interior_only_index)
    if any(index < 0 or index >= len(args.exact_fixed_motif_file)
           for index in interior_only_indices):
        raise ValueError("bad --exact-fixed-interior-only-index")
    for exact_index, (motif_file, threshold) in enumerate(zip(
        args.exact_fixed_motif_file, args.exact_fixed_threshold
    )):
        if threshold <= 0:
            raise ValueError("exact fixed thresholds must be positive")
        exact_fixed_models.append(add_exact_fixed_dm_constraint(
            model, motif_file, normal_lits, arc_pairs, masks,
            dummy_out, dummy_in, threshold,
            args.exact_fixed_interior_only or exact_index in interior_only_indices,
            args.exact_fixed_boundary_upper,
            enforce_threshold=not args.soft_fixed_homotopy,
        ))
    adaptive_exact_models = []
    if args.adaptive_exact_motif_file is not None:
        adaptive_thresholds = {}
        for specification in args.adaptive_exact_threshold:
            if "=" not in specification:
                raise ValueError("adaptive exact thresholds must be LABEL=VALUE")
            label, value = specification.split("=", 1)
            if label in adaptive_thresholds:
                raise ValueError(("duplicate adaptive exact threshold", label))
            adaptive_thresholds[label] = int(value)
        if not adaptive_thresholds or any(
            value <= 0 for value in adaptive_thresholds.values()
        ):
            raise ValueError("positive adaptive exact thresholds required")
        adaptive_exact_models = add_adaptive_exact_multi_dm_constraints(
            model, args.adaptive_exact_motif_file,
            normal_lits, arc_pairs, masks, adaptive_thresholds, order_channel,
            enforce_threshold=not args.soft_fixed_homotopy,
        )
    all_fixed_rows = fixed_models + exact_fixed_models + adaptive_exact_models
    if args.maximize_fixed_upper_bound and args.maximize_fixed_min_slack:
        raise ValueError(
            "choose at most one fixed-DM maximization objective"
        )
    if args.soft_fixed_homotopy and not all_fixed_rows:
        raise ValueError("--soft-fixed-homotopy needs a fixed-DM model")

    soft_homotopy = None
    if args.soft_fixed_homotopy:
        # Unlike the legacy hard-feasible max-min objective below, this phase
        # intentionally omits every fixed-shore threshold.  Negative margins
        # must therefore remain representable.  The incumbent is only a hint:
        # accepted paths are found after all hard rows have been restored.
        # Every score is nonnegative, so -max_i(threshold_i) is a valid common
        # lower bound for every signed margin.  The former -W lower bound
        # silently imposed score >= threshold-W on rows with threshold>W, so
        # the purportedly soft phase could discard legal base-model paths.
        # Deriving the floor from the actual rows also keeps this interface
        # sound for deliberately overlarge exploratory thresholds.
        soft_margin_floor = -max(
            int(row["threshold"]) for row in all_fixed_rows
        )
        soft_margin = model.NewIntVar(
            soft_margin_floor, W, "soft_fixed_homotopy_margin"
        )
        for row in all_fixed_rows:
            model.Add(
                soft_margin
                <= fixed_dm_score(row) - int(row["threshold"])
            )
        model.Maximize(soft_margin)
        soft_solver = cp_model.CpSolver()
        soft_solver.parameters.max_time_in_seconds = args.seconds
        soft_solver.parameters.num_search_workers = args.workers
        soft_solver.parameters.random_seed = args.seed
        soft_solver.parameters.randomize_search = True
        soft_status = soft_solver.Solve(model)
        soft_status_name = soft_solver.StatusName(soft_status)
        if soft_status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            args.hint_path.parent.mkdir(parents=True, exist_ok=True)
            args.hint_path.write_text(json.dumps({
                "status": "K15_SOFT_FIXED_HOMOTOPY_NO_INCUMBENT",
                "solver_status": soft_status_name,
                "sources": list(map(str, args.source)),
            }, indent=2, sort_keys=True) + "\n")
            raise RuntimeError(
                f"soft fixed homotopy returned {soft_status_name}"
            )
        soft_path, _ = selected_path(
            soft_solver, normal_arcs, dummy_out, dummy_in, masks
        )
        soft_rows = []
        for index, row in enumerate(all_fixed_rows):
            score = int(soft_solver.Value(fixed_dm_score(row)))
            soft_rows.append({
                "index": index,
                "label": row.get("label"),
                "source": row.get("source"),
                "score": score,
                "threshold": int(row["threshold"]),
                "margin": score - int(row["threshold"]),
            })
        soft_homotopy = {
            "status": "K15_SOFT_FIXED_HOMOTOPY_HINT",
            "solver_status": soft_status_name,
            "objective_value": soft_solver.ObjectiveValue(),
            "best_objective_bound": soft_solver.BestObjectiveBound(),
            "minimum_margin": int(soft_solver.Value(soft_margin)),
            "sources": list(map(str, args.source)),
            "fixed_rows": soft_rows,
            "middle_path": soft_path,
            "middle_components": [soft_path],
            "component_cyclic": [False],
        }
        args.hint_path.parent.mkdir(parents=True, exist_ok=True)
        args.hint_path.write_text(
            json.dumps(soft_homotopy, indent=2, sort_keys=True) + "\n"
        )

        model.ClearObjective()
        for row in all_fixed_rows:
            enforce_fixed_dm_threshold(model, row)
        replace_path_hints(
            model, soft_path, node_of, arc_pairs, normal_lits,
            dummy_out, dummy_in,
        )

    fixed_min_slack = None
    if args.maximize_fixed_min_slack:
        if not all_fixed_rows:
            raise ValueError(
                "--maximize-fixed-min-slack needs a fixed-DM model"
            )
        # Every row is already hard-enforced by its builder.  Consequently
        # each surplus is nonnegative and [0,W] preserves the original hard
        # max-min semantics exactly.
        fixed_min_slack = model.NewIntVar(0, W, "fixed_min_slack")
        for row in all_fixed_rows:
            model.Add(
                fixed_min_slack
                <= fixed_dm_score(row) - int(row["threshold"])
            )
        model.Maximize(fixed_min_slack)
    elif fixed_models and args.maximize_fixed_upper_bound:
        model.Maximize(sum(
            literal
            for row in fixed_models for literal in row["indicators"]
        ))
    parent_arc_lower_bounds: dict[int, int] = {}
    for specification in args.min_parent_arcs:
        if "=" not in specification:
            raise ValueError("parent arc lower bounds must be INDEX=COUNT")
        parent_text, count_text = specification.split("=", 1)
        parent = int(parent_text)
        count = int(count_text)
        if not 0 <= parent < len(parents) or not 0 <= count <= W - 1:
            raise ValueError(("bad parent arc lower bound", specification))
        if parent in parent_arc_lower_bounds:
            raise ValueError(("duplicate parent arc lower bound", parent))
        overlap_literals = [
            normal_lits[index]
            for index, pair in enumerate(arc_pairs)
            if parent in arc_sources[pair]
        ]
        model.Add(sum(overlap_literals) >= count)
        parent_arc_lower_bounds[parent] = count

    if args.maximize_parent_arcs >= 0:
        parent = args.maximize_parent_arcs
        model.Maximize(sum(
            normal_lits[index]
            for index, pair in enumerate(arc_pairs)
            if parent in arc_sources[pair]
        ))

    adaptive_parent_regressions = []
    for adaptive in adaptive_exact_models:
        parent_rows = []
        for index, parent in enumerate(parents):
            evaluation = evaluate_adaptive_exact_model(parent, adaptive)
            native = exact_fixed_neighbourhood(
                parent, args.hall_bin, adaptive["targets"]
            )
            if evaluation["total"] != native:
                raise AssertionError((
                    "adaptive parent regression mismatch",
                    adaptive["label"], index, evaluation, native,
                ))
            parent_rows.append({
                "index": index,
                "source": str(args.source[index]),
                **evaluation,
                "native_fixed_neighbourhood": native,
            })
        adaptive_parent_regressions.append({
            "label": adaptive["label"],
            "threshold": adaptive["threshold"],
            "parents": parent_rows,
        })

    upper_encoded: set[tuple[int, int]] = set()
    upper_witness_count: dict[str, int] = {}
    census = []
    best = None
    best_key = None
    dynamic_dm_models = []
    dynamic_dm_shores: set[tuple[int, ...]] = {
        tuple(sorted(shore["targets"])) for shore in preloaded_dm_shores
    }
    terminal_solver_status = None
    terminal_round = None
    termination_reason = "ROUND_LIMIT"
    started = time.monotonic()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    for round_no in range(args.rounds):
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.seconds
        solver.parameters.num_search_workers = args.workers
        solver.parameters.random_seed = args.seed + round_no
        solver.parameters.randomize_search = True
        status = solver.Solve(model)
        status_name = solver.StatusName(status)
        terminal_solver_status = status_name
        terminal_round = round_no
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            census.append({"round": round_no, "status": status_name})
            termination_reason = status_name
            break
        path, chosen = selected_path(
            solver, normal_arcs, dummy_out, dummy_in, masks
        )
        selected_parent_arc_counts = {
            str(parent): sum(
                parent in arc_sources[arc_pairs[index]] for index in chosen
            )
            for parent in range(len(parents))
        }
        path_sha256 = stable_object_sha256(path)
        audit = chronology_audit(path)
        if audit["residence_bad_motifs"] and not args.skip_residence:
            raise AssertionError(("residence encoding incomplete", audit))

        missing = []
        for q_text, count in audit["upper_holes"].items():
            if not count:
                continue
            q = int(q_text)
            loads = Counter()
            for start in range(W - q):
                value = 0
                for offset in range(q + 1):
                    value |= path[start + offset]
                if value.bit_count() == R + q:
                    loads[value] += 1
            for target in range(1 << K):
                if target.bit_count() == R + q and not loads[target]:
                    missing.append((q, target))
        if missing:
            if args.save_all:
                incomplete = {
                    "status": "K15_DIRECTED_PARENT_UNION_UPPER_INCOMPLETE",
                    "sources": list(map(str, args.source)),
                    "middle_path": path,
                    "middle_components": [path],
                    "component_cyclic": [False],
                    "missing_upper_targets": [list(item) for item in missing],
                    "parent_window_counts": {
                        str(item["parent"]): sum(
                            solver.BooleanValue(lit)
                            for lit in item["indicators"]
                        )
                        for item in parent_window_models
                    },
                    "balanced_window_min": (
                        solver.Value(balanced_window_min)
                        if balanced_window_min is not None else None
                    ),
                    **audit,
                }
                args.output.with_name(
                    f"{args.output.stem}.round{round_no}.upper{len(missing)}.json"
                ).write_text(
                    json.dumps(incomplete, indent=2, sort_keys=True) + "\n"
                )
            added = 0
            impossible = []
            for q, target in missing:
                key = (q, target)
                if key in upper_encoded:
                    raise AssertionError(("encoded target still missing", key))
                motifs = target_witnesses(
                    target, q, adjacency, arc_index, masks
                )
                if not motifs:
                    impossible.append(key)
                    continue
                witness_lits = []
                for motif_no, motif in enumerate(sorted(motifs)):
                    witness = model.NewBoolVar(
                        f"u_{q}_{target}_{motif_no}"
                    )
                    for index in motif:
                        model.AddImplication(witness, normal_lits[index])
                    witness_lits.append(witness)
                model.AddBoolOr(witness_lits)
                upper_encoded.add(key)
                upper_witness_count[f"{q}:{target}"] = len(motifs)
                added += 1
            census.append({
                "round": round_no,
                "status": "UPPER_CUTS",
                "missing": len(missing),
                "missing_targets": [
                    [int(depth), int(target)] for depth, target in missing
                ],
                "added": added,
                "impossible": impossible,
            })
            print(json.dumps(census[-1]), flush=True)
            if impossible:
                termination_reason = "UNREALIZABLE_UPPER_TARGET"
                break
            continue

        hall = exact_hall(path, args.hall_bin, args.fixed_targets_file)
        dynamic_calibration = None
        if args.dynamic_exact_dm and hall["deficiency"]:
            dm_targets = list(map(int, hall["dm_targets"]))
            dynamic_calibration_full = evaluate_global_exact_shore(
                path, dm_targets
            )
            native_cells = list(map(int, hall["dm_cell_indices"]))
            if dynamic_calibration_full["formula_cells"] != native_cells:
                raise AssertionError((
                    "global formula/native DM cell mismatch",
                    len(dynamic_calibration_full["formula_cells"]),
                    len(native_cells),
                ))
            if dynamic_calibration_full["carrier_cells"] != native_cells:
                raise AssertionError((
                    "complete-carrier/native DM cell mismatch",
                    len(dynamic_calibration_full["carrier_cells"]),
                    len(native_cells),
                ))
            if (
                len(dm_targets) != int(hall["dm_left"])
                or dynamic_calibration_full["total"] != int(hall["dm_right"])
                or len(dm_targets) - dynamic_calibration_full["total"]
                   != int(hall["deficiency"])
            ):
                raise AssertionError((
                    "global exact DM cardinality calibration failed",
                    len(dm_targets), dynamic_calibration_full["total"], hall,
                ))
            dynamic_calibration = {
                key: value for key, value in dynamic_calibration_full.items()
                if key not in {"formula_cells", "carrier_cells"}
            }
        preloaded_dm_evaluations = []
        for shore in preloaded_dm_shores:
            targets = list(shore["targets"])
            evaluation_full = evaluate_global_exact_shore(path, targets)
            native_total = exact_fixed_neighbourhood(
                path, args.hall_bin, targets
            )
            if evaluation_full["total"] != native_total:
                raise AssertionError((
                    "preloaded position/native shore mismatch",
                    shore["path"], evaluation_full["total"], native_total,
                ))
            if native_total < int(shore["threshold"]):
                raise AssertionError((
                    "hard preloaded exact DM shore admitted a violation",
                    shore["path"], native_total, shore["threshold"],
                ))
            preloaded_dm_evaluations.append({
                "path": shore["path"],
                "label": shore["label"],
                "targets": len(targets),
                "allowance": int(shore["allowance"]),
                "threshold": int(shore["threshold"]),
                "position_score": int(evaluation_full["total"]),
                "native_score": int(native_total),
                "depth_histogram": evaluation_full["depth_histogram"],
            })
        fixed_neighbourhoods = hall.get("fixed_neighbourhoods", [])
        fixed_gaps = [
            max(row["threshold"] - neighbourhood, 0)
            for row, neighbourhood in zip(fixed_models, fixed_neighbourhoods)
        ]
        adaptive_evaluations = [
            evaluate_adaptive_exact_model(path, item)
            for item in adaptive_exact_models
        ]
        adaptive_native_scores = [
            exact_fixed_neighbourhood(path, args.hall_bin, item["targets"])
            for item in adaptive_exact_models
        ]
        for item, evaluation, native in zip(
            adaptive_exact_models, adaptive_evaluations, adaptive_native_scores
        ):
            if evaluation["total"] != native:
                raise AssertionError((
                    "adaptive exact postsolve mismatch",
                    item["label"], evaluation, native,
                ))
        adaptive_gaps = [
            max(item["threshold"] - evaluation["total"], 0)
            for item, evaluation in zip(
                adaptive_exact_models, adaptive_evaluations
            )
        ]
        if any(adaptive_gaps):
            raise AssertionError((
                "adaptive exact encoding admitted a deficient chronology",
                adaptive_gaps, adaptive_evaluations,
            ))
        fixed_gap = sum(fixed_gaps) + sum(adaptive_gaps)
        if (
            args.dynamic_exact_dm
            and hall["deficiency"] > args.dynamic_dm_allowance
        ):
            shore = tuple(map(int, hall["dm_targets"]))
            shore_key = tuple(sorted(shore))
            if shore_key in dynamic_dm_shores:
                raise AssertionError((
                    "a previously encoded exact DM shore remains violated",
                    len(shore), hall["dm_right"], args.dynamic_dm_allowance,
                ))
            cut = add_exact_dm_shore(
                list(shore), args.dynamic_dm_allowance,
                len(preloaded_dm_models) + len(dynamic_dm_models),
            )
            dynamic_dm_shores.add(shore_key)
            dynamic_dm_models.append(cut)
            cut_row = {
                "round": round_no,
                "status": "DYNAMIC_EXACT_DM_CUT",
                "hall_deficiency": int(hall["deficiency"]),
                "dm_left": int(hall["dm_left"]),
                "dm_right": int(hall["dm_right"]),
                "allowance": args.dynamic_dm_allowance,
                "threshold": cut["threshold"],
                "cut_index": cut["cut"],
                "calibration": dynamic_calibration,
                "upper_constraints": len(upper_encoded),
                "path_sha256": path_sha256,
                "selected_parent_arc_counts": selected_parent_arc_counts,
            }
            census.append(cut_row)
            print(json.dumps(cut_row), flush=True)
            if args.save_all:
                cut_candidate = {
                    "status": "K15_GLOBAL_EXACT_DM_CUT_INCUMBENT",
                    "sources": list(map(str, args.source)),
                    "middle_path": path,
                    "middle_components": [path],
                    "component_cyclic": [False],
                    "hall": hall,
                    "dynamic_exact_calibration": dynamic_calibration,
                    "preloaded_exact_dm_evaluations": preloaded_dm_evaluations,
                    "dynamic_dm_allowance": args.dynamic_dm_allowance,
                    "dynamic_dm_cut_index": cut["cut"],
                    **audit,
                }
                args.output.with_name(
                    f"{args.output.stem}.round{round_no}.dmcut"
                    f"{cut['cut']}.hall{hall['deficiency']}.json"
                ).write_text(
                    json.dumps(cut_candidate, indent=2, sort_keys=True) + "\n"
                )
            # The exact shore row is the relocation-proof separator.  This
            # additional incumbent no-good is redundant mathematically but
            # gives CP-SAT an immediate propagation reason not to reconsider
            # the same 6,434-arc chronology while the existential target
            # witnesses of the new Hall row are still weakly propagated.
            model.AddBoolOr([
                normal_lits[index].Not() for index in chosen
            ])
            continue
        key = (
            fixed_gap, hall["deficiency"], hall["zero_candidates"],
            audit["residence_bad_motifs"],
            audit["lower_q1_holes"], audit["lower_q2_holes"],
            audit["lower_q3_holes"],
        )
        row = {
            "round": round_no,
            "status": "CANDIDATE",
            "key": list(key),
            "hall_deficiency": hall["deficiency"],
            "hall_zero_candidates": hall["zero_candidates"],
            "fixed_neighbourhoods": fixed_neighbourhoods,
            "fixed_gaps": fixed_gaps,
            "fixed_gap": fixed_gap,
            "adaptive_exact_scores": adaptive_evaluations,
            "adaptive_exact_gaps": adaptive_gaps,
            "adaptive_exact_native_scores": adaptive_native_scores,
            "dynamic_exact_calibration": dynamic_calibration,
            "preloaded_exact_dm_evaluations": preloaded_dm_evaluations,
            "path_sha256": path_sha256,
            "selected_parent_arc_counts": selected_parent_arc_counts,
            "fixed_projected_upper_bounds": [
                sum(solver.BooleanValue(lit) for lit in item["indicators"])
                + item["boundary_allowance"]
                for item in fixed_models
            ],
            "upper_constraints": len(upper_encoded),
            "parent_window_counts": {
                str(item["parent"]): sum(
                    solver.BooleanValue(lit) for lit in item["indicators"]
                )
                for item in parent_window_models
            },
            "balanced_window_min": (
                solver.Value(balanced_window_min)
                if balanced_window_min is not None else None
            ),
            "fixed_min_slack": (
                solver.Value(fixed_min_slack)
                if fixed_min_slack is not None else None
            ),
        }
        census.append(row)
        print(json.dumps(row), flush=True)
        candidate = {
            "status": "K15_DIRECTED_PARENT_UNION_CHECKPOINT",
            "sources": list(map(str, args.source)),
            "middle_path": path,
            "middle_components": [path],
            "component_cyclic": [False],
            "hall": hall,
            "hall_deficiency": hall["deficiency"],
            "hall_zero_candidates": hall["zero_candidates"],
            "fixed_neighbourhoods": fixed_neighbourhoods,
            "fixed_gaps": fixed_gaps,
            "fixed_gap": fixed_gap,
            "adaptive_exact_scores": adaptive_evaluations,
            "adaptive_exact_gaps": adaptive_gaps,
            "adaptive_exact_native_scores": adaptive_native_scores,
            "dynamic_exact_calibration": dynamic_calibration,
            "preloaded_exact_dm_evaluations": preloaded_dm_evaluations,
            "path_sha256": path_sha256,
            "selected_parent_arc_counts": selected_parent_arc_counts,
            **audit,
        }
        if args.save_all:
            args.output.with_name(
                f"{args.output.stem}.round{round_no}.hall{hall['deficiency']}.json"
            ).write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n")
        if best_key is None or key < best_key:
            best_key = key
            best = candidate
            args.output.write_text(
                json.dumps(candidate, indent=2, sort_keys=True) + "\n"
            )
        if hall["deficiency"] == 0:
            termination_reason = "HALL_ZERO_CANDIDATE"
            break
        if args.stop_after_first_candidate:
            termination_reason = "FIRST_CANDIDATE_STOP"
            break
        if args.dynamic_exact_dm and not args.dynamic_dm_continue:
            termination_reason = "DYNAMIC_DM_STOP"
            break
        model.AddBoolOr([normal_lits[index].Not() for index in chosen])

    raw_infeasible = termination_reason == "INFEASIBLE" and best is None
    interior_only_strengthening = bool(
        args.exact_fixed_interior_only or interior_only_indices
    )
    certified_infeasible = raw_infeasible and not interior_only_strengthening
    exploratory_infeasible = raw_infeasible and interior_only_strengthening
    if certified_infeasible:
        summary_status = "CERTIFIED_INFEASIBLE"
    elif exploratory_infeasible:
        summary_status = "EXPLORATORY_INFEASIBLE"
    elif termination_reason == "MODEL_INVALID":
        summary_status = "MODEL_INVALID"
    elif best is not None:
        summary_status = "CANDIDATE_FOUND"
    else:
        summary_status = "INCOMPLETE"

    full_normal_catalogue = sorted(
        (masks[tail], masks[head]) for tail, head in arc_pairs
    )
    active_parent_indices = frozenset(
        restricted_parent_subset
        if restricted_parent_subset is not None else range(len(parents))
    )
    active_normal_catalogue = sorted(
        (masks[tail], masks[head])
        for tail, head in arc_pairs
        if arc_sources[tail, head].intersection(active_parent_indices)
    )

    def augmented_catalogue(
        normal: list[tuple[int, int]],
        starts: list[int],
        ends: list[int],
    ) -> list[list[int | str]]:
        return (
            [["normal", first, second] for first, second in normal]
            + [["start", 1 << K, start] for start in starts]
            + [["end", end, 1 << K] for end in ends]
        )

    full_starts = sorted(masks[node] for node in parent_starts)
    full_ends = sorted(masks[node] for node in parent_ends)
    active_starts = sorted(
        masks[node] for node in parent_starts
        if parent_start_sources[node].intersection(active_parent_indices)
    )
    active_ends = sorted(
        masks[node] for node in parent_ends
        if parent_end_sources[node].intersection(active_parent_indices)
    )
    runtime_catalogue_contract = {
        "full_normal_arcs": len(full_normal_catalogue),
        "full_normal_sha256": stable_object_sha256(full_normal_catalogue),
        "full_augmented_arcs": (
            len(full_normal_catalogue) + len(full_starts) + len(full_ends)
        ),
        "full_augmented_sha256": stable_object_sha256(augmented_catalogue(
            full_normal_catalogue, full_starts, full_ends
        )),
        "active_parent_indices": sorted(active_parent_indices),
        "active_normal_arcs": len(active_normal_catalogue),
        "active_normal_sha256": stable_object_sha256(active_normal_catalogue),
        "active_augmented_arcs": (
            len(active_normal_catalogue) + len(active_starts) + len(active_ends)
        ),
        "active_augmented_sha256": stable_object_sha256(augmented_catalogue(
            active_normal_catalogue, active_starts, active_ends
        )),
        "active_starts": active_starts,
        "active_ends": active_ends,
    }
    residual_exhausted = termination_reason == "INFEASIBLE"
    candidate_nogood_path_sha256 = [
        row["path_sha256"] for row in census
        if row.get("status") == "CANDIDATE"
    ] if residual_exhausted else []
    dynamic_cut_path_sha256 = [
        row["path_sha256"] for row in census
        if row.get("status") == "DYNAMIC_EXACT_DM_CUT"
    ] if residual_exhausted else []

    summary = {
        "status": summary_status,
        "command_argv": list(sys.argv),
        "ortools_version": ortools.__version__,
        "terminal_solver_status": terminal_solver_status,
        "terminal_round": terminal_round,
        "termination_reason": termination_reason,
        "certified_infeasible": certified_infeasible,
        "exploratory_infeasible": exploratory_infeasible,
        # There is no sound scope-free Hall-transfer bit: branch restrictions,
        # forced motifs/windows, and caller-supplied fixed rows can all make an
        # exact CP-SAT INFEASIBLE result strictly narrower than the full loaded
        # catalogue.  Consumers must inspect certified_infeasible_scope (and,
        # for the canonical 16-branch theorem, the external hash/branch
        # manifest) instead of treating one Boolean as a global no-go.
        "hall_transfer_safe_infeasible": False,
        "residual_exhausted": residual_exhausted,
        "residual_candidate_nogood_path_sha256": candidate_nogood_path_sha256,
        "residual_dynamic_cut_path_sha256": dynamic_cut_path_sha256,
        "certified_infeasible_scope": (
            {
                "sources": list(map(str, args.source)),
                "hard_fixed_rows": [
                    {
                        "label": row.get("label"),
                        "source": row.get("source"),
                        "threshold": int(row["threshold"]),
                        "interface": row.get("interface"),
                    }
                    for row in all_fixed_rows if row.get("hard_threshold")
                ],
                "residence_enforced": not args.skip_residence,
                "upper_constraints_added": len(upper_encoded),
                "dynamic_dm_constraints_added": len(dynamic_dm_models),
                "preloaded_dm_constraints": len(preloaded_dm_models),
                "exact_dm_channel": (
                    "legacy_position_indexed_19311"
                    if args.legacy_position_exact_dm
                    else (
                        "arc_propagated_exact_3w_plus_6"
                        if exact_dm_requested else None
                    )
                ),
                "restricted_parent_subset": restricted_parent_model,
                "escape_parent_subsets": escape_parent_subset_models,
                "parent_dummy_only": args.parent_dummy_only,
                "include_reverses": args.include_reverses,
                "fix_parent": args.fix_parent,
                "force_start_mask": args.force_start_mask,
                "force_end_mask": args.force_end_mask,
                "force_tuple_json": (
                    str(args.force_tuple_json)
                    if args.force_tuple_json is not None else None
                ),
                "min_parent_windows": dict(sorted(window_requirements.items())),
                "min_parent_arcs": dict(sorted(parent_arc_lower_bounds.items())),
                "parent_window_length": args.parent_window_length,
                "require_target_motif_file": (
                    str(args.require_target_motif_file)
                    if args.require_target_motif_file is not None else None
                ),
                "exact_fixed_interior_only": args.exact_fixed_interior_only,
                "exact_fixed_interior_only_indices": sorted(interior_only_indices),
                "exact_fixed_boundary_upper": args.exact_fixed_boundary_upper,
                "adaptive_exact_motif_file": (
                    str(args.adaptive_exact_motif_file)
                    if args.adaptive_exact_motif_file is not None else None
                ),
                "global_exact_dm_shores": [
                    str(path) for path in args.global_exact_dm_shore
                ],
                "global_exact_allowance_shores": [
                    str(path) for path in args.global_exact_allowance_shore
                ],
                "fixed_targets_files": [
                    str(path) for path in args.fixed_targets_file
                ],
            }
            if certified_infeasible else None
        ),
        "sources": list(map(str, args.source)),
        "source_sha256": [
            hashlib.sha256(path.read_bytes()).hexdigest() for path in args.source
        ],
        "solver_script_sha256": hashlib.sha256(
            Path(__file__).resolve().read_bytes()
        ).hexdigest(),
        "runtime_catalogue_contract": runtime_catalogue_contract,
        "parent_count": len(parents),
        "parent_dummy_only": args.parent_dummy_only,
        "parent_dummy_starts": sorted(masks[node] for node in parent_starts),
        "parent_dummy_ends": sorted(masks[node] for node in parent_ends),
        "directed_arcs": len(arc_pairs),
        "arc_source_multiplicity": dict(sorted(Counter(
            len(value) for value in arc_sources.values()
        ).items())),
        "restricted_parent_subset": restricted_parent_model,
        "escape_parent_subsets": escape_parent_subset_models,
        "residence_forbidden_motifs": len(forbidden),
        "upper_constraints": len(upper_encoded),
        "upper_witness_count": upper_witness_count,
        "fixed_models": [
            {key: value for key, value in row.items() if key != "indicators"}
            for row in fixed_models
        ],
        "target_motif_model": target_motif_model,
        "maximize_fixed_min_slack": args.maximize_fixed_min_slack,
        "soft_fixed_homotopy": (
            {
                key: value for key, value in soft_homotopy.items()
                if key not in {"middle_path", "middle_components"}
            }
            if soft_homotopy is not None else None
        ),
        "hint_path": str(args.hint_path) if args.hint_path is not None else None,
        "parent_window_models": [
            {key: value for key, value in row.items() if key != "indicators"}
            for row in parent_window_models
        ],
        "parent_arc_lower_bounds": dict(sorted(parent_arc_lower_bounds.items())),
        "balanced_parent_windows": sorted(balanced_parents),
        "exact_fixed_models": [
            {key: value for key, value in row.items() if key != "weighted_terms"}
            for row in exact_fixed_models
        ],
        "adaptive_exact_models": [
            {
                key: value for key, value in row.items()
                if key not in {
                    "interior_indicators", "boundary_claims", "terms",
                    "targets", "pattern_pairs",
                }
            }
            for row in adaptive_exact_models
        ],
        "adaptive_parent_regressions": adaptive_parent_regressions,
        "dynamic_exact_dm": args.dynamic_exact_dm,
        "exact_dm_channel": (
            "legacy_position_indexed_19311"
            if args.legacy_position_exact_dm
            else (
                "arc_propagated_exact_3w_plus_6"
                if exact_dm_requested else None
            )
        ),
        "exact_dm_channel_catalogue": (
            {
                key: arc_propagated_channel[key]
                for key in (
                    "catalogue_edges", "catalogue_sha256",
                    "catalogue_equality_asserted", "cell_count", "interface",
                )
            }
            if arc_propagated_channel is not None else None
        ),
        "dynamic_dm_allowance": args.dynamic_dm_allowance,
        "dynamic_dm_continue": args.dynamic_dm_continue,
        "save_all": args.save_all,
        "preloaded_exact_dm_models": [
            {
                key: value for key, value in row.items()
                if key not in {"claims", "targets"}
            }
            for row in preloaded_dm_models
        ],
        "global_exact_dm_shores": [
            str(path) for path in args.global_exact_dm_shore
        ],
        "global_exact_allowance_shores": [
            str(path) for path in args.global_exact_allowance_shore
        ],
        "dynamic_dm_models": [
            {
                key: value for key, value in row.items()
                if key != "claims"
            }
            for row in dynamic_dm_models
        ],
        "stop_after_first_candidate": args.stop_after_first_candidate,
        "initial_hint_path": (
            str(args.initial_hint_path) if args.initial_hint_path is not None
            else None
        ),
        "forced_tuple": {
            "source": str(args.force_tuple_json),
            "targets": forced_tuple.get("covered_targets"),
            "unique_selected_arcs": forced_tuple.get("unique_selected_arcs"),
        } if forced_tuple is not None else None,
        "best_key": list(best_key) if best_key is not None else None,
        "elapsed": time.monotonic() - started,
        "census": census,
    }
    args.output.with_suffix(".summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary), flush=True)
    if best is not None:
        return 0
    if certified_infeasible:
        return 1
    return 3 if termination_reason == "MODEL_INVALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
