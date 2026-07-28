#!/usr/bin/env python3
"""Search a genuinely new k=15 carrier inside two relabelled path matchings.

For a spanning path P, adjoin a dummy vertex and orient

    dummy -> P[0] -> ... -> P[-1] -> dummy.

This is a perfect matching from a source copy of the vertices to a target
copy.  Two such matchings decompose into alternating assignment cycles.  On
each nontrivial cycle we may take all arcs from the first matching or all
arcs from the second, independently, and still retain indegree=outdegree=1.
This is a much richer move than cutting/reversing fixed segments: a single
choice can replace thousands of non-contiguous carrier edges.

The model below chooses those alternating components, requires the resulting
permutation to be one cycle through the dummy (hence a Hamilton path), forbids
every local depth-three residence defect, and preserves every upper target by
retaining at least one *original* witness window from either parent.  The last
condition is sufficient rather than necessary, but exact and compact.  Every
candidate is independently audited, including the full compiler Hall graph.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import reduce
import json
from math import comb
from operator import or_
from pathlib import Path
import random
import subprocess
import sys
import time

from ortools.sat.python import cp_model

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from audit_k15_phasefactor_safe_openings import linear_residence_violations
from search_k15_component_seam_sat import exact_candidate_audit, lower_loads, upper_loads
from sigma_multirow_linear_compiler import derive, linear_erosion


K, R, DEPTH = 15, 8, 3
DUMMY = 1 << K


def load_path(path: Path) -> list[int]:
    data = json.loads(path.read_text())
    middle = data.get("middle_path")
    if not middle and len(data.get("middle_components", [])) == 1:
        middle = data["middle_components"][0]
    if not middle:
        raise ValueError(f"no one-path chronology in {path}")
    answer = list(map(int, middle))
    if len(answer) != comb(K, R) or len(set(answer)) != len(answer):
        raise ValueError("source is not the complete middle layer")
    return answer


def permute_mask(value: int, permutation: list[int]) -> int:
    answer = 0
    for old, new in enumerate(permutation):
        if value >> old & 1:
            answer |= 1 << new
    return answer


def successor(path: list[int]) -> dict[int, int]:
    answer = {DUMMY: path[0], path[-1]: DUMMY}
    answer.update(zip(path, path[1:]))
    return answer


def assignment_components(first: dict[int, int], second: dict[int, int]):
    """Return component id on sources in the union of two matchings."""
    inverse_second = {target: source for source, target in second.items()}
    permutation = {source: inverse_second[target]
                   for source, target in first.items()}
    component: dict[int, int] = {}
    rows: list[list[int]] = []
    for source in sorted(permutation):
        if source in component:
            continue
        row = []
        current = source
        while current not in component:
            component[current] = len(rows)
            row.append(current)
            current = permutation[current]
        if current != source:
            raise AssertionError("assignment permutation did not close locally")
        rows.append(row)
    return component, rows


def requirements_for_arcs(
    arcs: list[tuple[int, int]],
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
) -> tuple[tuple[int, int], ...] | None:
    """Map an arc motif to consistent (variable-index, value) requirements."""
    requirements: dict[int, int] = {}
    for source, target in arcs:
        a = first[source] == target
        b = second[source] == target
        if not a and not b:
            return None
        if a and b:
            continue
        cid = component[source]
        index = variable_component.get(cid)
        if index is None:
            raise AssertionError((source, target, cid, "nonfixed arc in fixed component"))
        value = int(b)
        old = requirements.setdefault(index, value)
        if old != value:
            return None
    return tuple(sorted(requirements.items()))


def add_pattern_indicator(
    model: cp_model.CpModel,
    variables: list[cp_model.IntVar],
    pattern: tuple[tuple[int, int], ...],
    cache: dict[tuple[tuple[int, int], ...], cp_model.IntVar],
):
    if not pattern:
        return None
    if len(pattern) == 1:
        index, value = pattern[0]
        return variables[index] if value else variables[index].Not()
    if pattern in cache:
        return cache[pattern]
    witness = model.NewBoolVar(f"pat_{len(cache)}")
    for index, value in pattern:
        literal = variables[index] if value else variables[index].Not()
        model.AddImplication(witness, literal)
    cache[pattern] = witness
    return witness


def original_upper_patterns(
    path: list[int],
    parent: int,
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
):
    answer: dict[tuple[int, int], set[tuple[tuple[int, int], ...]]] = defaultdict(set)
    for q in range(1, R):
        for start in range(len(path) - q):
            window = path[start:start + q + 1]
            target = reduce(or_, window, 0)
            if target.bit_count() != R + q:
                continue
            arcs = list(zip(window, window[1:]))
            pattern = requirements_for_arcs(
                arcs, first, second, component, variable_component
            )
            if pattern is None:
                raise AssertionError((parent, q, start, "parent motif unavailable"))
            answer[q, target].add(pattern)
    return answer


def mixed_upper_patterns(
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
):
    """Enumerate every consistent upper witness path in the two-parent union.

    Each source has at most two outgoing arcs, so this is at most
    ``(W+1)(2+...+2^7)`` path prefixes before consistency pruning.  It gives
    an exact upper-shadow encoding for the trade cube, including genuinely
    mixed windows absent from either parent.
    """
    choices = {
        source: sorted({first[source], second[source]})
        for source in first if source != DUMMY
    }
    answer: dict[tuple[int, int], set[tuple[tuple[int, int], ...]]] = defaultdict(set)
    prefixes = 0
    for start in choices:
        # vertices, arcs, accumulated union
        stack = [([start], [], start)]
        while stack:
            vertices, arcs, target = stack.pop()
            q = len(arcs)
            if q:
                prefixes += 1
                if target.bit_count() == R + q:
                    pattern = requirements_for_arcs(
                        arcs, first, second, component, variable_component
                    )
                    if pattern is not None:
                        answer[q, target].add(pattern)
            if q == R - 1:
                continue
            source = vertices[-1]
            if source == DUMMY or source not in choices:
                continue
            for nxt in choices[source]:
                if nxt == DUMMY or nxt in vertices:
                    continue
                trial_arcs = arcs + [(source, nxt)]
                if requirements_for_arcs(
                    trial_arcs, first, second, component, variable_component
                ) is None:
                    continue
                stack.append((vertices + [nxt], trial_arcs, target | nxt))
    return answer, prefixes


def local_fixed_hit(
    middle: list[int], row_depth: int, targets: set[int]
) -> bool:
    """Exact fixed-target hit for the canonical interior cell at start 6."""
    full = (1 << K) - 1
    allowed = []
    for position in range(len(middle) + DEPTH):
        value = full
        for index in range(
            max(0, position - DEPTH), min(position, len(middle) - 1) + 1
        ):
            value &= middle[index]
        allowed.append(value)
    carrier_required: dict[tuple[int, ...], int] = defaultdict(int)
    for start, target in enumerate(middle):
        for coordinate in range(K):
            if not (target >> coordinate) & 1:
                continue
            carriers = tuple(
                position for position in range(start, start + DEPTH + 1)
                if (allowed[position] >> coordinate) & 1
            )
            carrier_required[carriers] |= 1 << coordinate
    positions = tuple(range(6, 6 + row_depth + 1))
    envelope = reduce(or_, (allowed[position] for position in positions), 0)
    mandatory = 0
    for bits in range(1, 1 << len(positions)):
        subset = tuple(
            positions[index] for index in range(len(positions))
            if bits >> index & 1
        )
        mandatory |= carrier_required.get(subset, 0)
    target = envelope
    while target:
        if (
            target in targets
            and not (mandatory & ~target)
            and all(allowed[position] & target for position in positions)
        ):
            return True
        target = (target - 1) & envelope
    return False


def fixed_interior_patterns(
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
    targets: set[int],
):
    """Enumerate exact hit patterns for every bounded interior compiler cell."""
    choices = {
        source: sorted({first[source], second[source]})
        for source in first if source != DUMMY
    }
    answer: dict[tuple[int, int], set[tuple[tuple[int, int], ...]]] = defaultdict(set)
    prefixes = 0
    for row_depth in range(DEPTH):
        length = row_depth + 10
        for start in choices:
            stack = [([start], [])]
            while stack:
                vertices, arcs = stack.pop()
                if len(vertices) == length:
                    prefixes += 1
                    pattern = requirements_for_arcs(
                        arcs, first, second, component, variable_component
                    )
                    if pattern is not None and local_fixed_hit(
                        vertices, row_depth, targets
                    ):
                        answer[row_depth, start].add(pattern)
                    continue
                source = vertices[-1]
                if source == DUMMY or source not in choices:
                    continue
                for nxt in choices[source]:
                    if nxt == DUMMY or nxt in vertices:
                        continue
                    trial_arcs = arcs + [(source, nxt)]
                    if requirements_for_arcs(
                        trial_arcs, first, second, component, variable_component
                    ) is not None:
                        stack.append((vertices + [nxt], trial_arcs))
    return answer, prefixes


def read_fixed_targets(path: Path) -> set[int]:
    payload = json.loads(path.read_text())
    for key in ("witness_targets", "dm_targets", "targets"):
        row = payload.get(key)
        if isinstance(row, list):
            return set(map(int, row))
    raise ValueError(f"no fixed target array in {path}")


def native_fixed_payload(
    binary: Path, source: Path, permutation: list[int], witness: Path
):
    command = [
        str(binary.resolve()), str(source), ",".join(map(str, permutation)),
        str(witness),
    ]
    process = subprocess.run(
        command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if process.returncode:
        raise RuntimeError((command, process.returncode, process.stderr))
    return json.loads(process.stdout)


def native_bundle_payload(
    binary: Path, source: Path, permutation: list[int],
    fixed_witness: Path | None = None,
):
    command = [
        str(binary.resolve()), "--bundle", str(source),
        ",".join(map(str, permutation)),
    ]
    if fixed_witness is not None:
        command.append(str(fixed_witness))
    process = subprocess.run(
        command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if process.returncode:
        raise RuntimeError((command, process.returncode, process.stderr))
    return json.loads(process.stdout)


def decode_signed_pattern(row):
    return tuple((abs(int(value)) - 1, int(value) > 0) for value in row)


def add_native_weighted_patterns(
    model: cp_model.CpModel,
    variables: list[cp_model.IntVar],
    payload: dict,
    prefix: str,
):
    if payload["variable_components"] != len(variables):
        raise AssertionError((payload["variable_components"], len(variables)))
    indicators = []
    terms = []
    for serial, row in enumerate(payload["patterns"]):
        weight, signed = int(row[0]), list(map(int, row[1:]))
        witness = model.NewBoolVar(f"{prefix}_{serial}")
        for value in signed:
            index = abs(value) - 1
            literal = variables[index] if value > 0 else variables[index].Not()
            model.AddImplication(witness, literal)
        indicators.append(witness)
        terms.append(weight * witness)
    return int(payload["constant"]), indicators, terms


def enumerate_bad_residence_patterns(
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
):
    """Enumerate every bad selected path on two through four arcs."""
    choices = {
        source: sorted({first[source], second[source]})
        for source in first if source != DUMMY
    }
    bad: set[tuple[tuple[int, int], ...]] = set()
    for start in choices:
        stack = [([start], [])]
        while stack:
            vertices, arcs = stack.pop()
            if len(arcs) >= 2:
                pattern = requirements_for_arcs(
                    arcs, first, second, component, variable_component
                )
                if pattern is not None and linear_residence_violations(vertices, DEPTH):
                    if not pattern:
                        raise AssertionError("a parent contains a residence defect")
                    bad.add(pattern)
            if len(arcs) == 4:
                continue
            source = vertices[-1]
            if source == DUMMY or source not in choices:
                continue
            for target in choices[source]:
                if target == DUMMY or target in vertices:
                    continue
                trial_arcs = arcs + [(source, target)]
                if requirements_for_arcs(
                    trial_arcs, first, second, component, variable_component
                ) is not None:
                    stack.append((vertices + [target], trial_arcs))
    return bad


def selected_path(
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
    values: list[int],
) -> list[int]:
    following = {}
    for source in first:
        cid = component[source]
        index = variable_component.get(cid)
        use_second = bool(values[index]) if index is not None else False
        following[source] = second[source] if use_second else first[source]
    answer = []
    current = following[DUMMY]
    while current != DUMMY:
        if current in answer:
            raise AssertionError("selected circuit failed to pass through dummy")
        answer.append(current)
        current = following[current]
    if len(answer) != comb(K, R):
        raise AssertionError((len(answer), "not Hamilton"))
    return answer


def selected_cover(
    first: dict[int, int],
    second: dict[int, int],
    component: dict[int, int],
    variable_component: dict[int, int],
    values: list[int],
):
    following = {}
    for source in first:
        cid = component[source]
        index = variable_component.get(cid)
        following[source] = (
            second[source] if index is not None and values[index]
            else first[source]
        )
    unseen = set(following)
    cycles = []
    while unseen:
        start = next(iter(unseen))
        row = []
        current = start
        while current not in row:
            row.append(current)
            unseen.discard(current)
            current = following[current]
        if current != start:
            raise AssertionError("permutation component did not close")
        cycles.append(row)
    physical = []
    dummy_path = None
    for row in cycles:
        if DUMMY not in row:
            physical.append(row)
            continue
        at = row.index(DUMMY)
        rotated = row[at + 1:] + row[:at]
        dummy_path = rotated
    if dummy_path is None:
        raise AssertionError("dummy disappeared")
    return dummy_path, physical


def native_candidate_audit(
    path: list[int], binary: Path, input_path: Path,
    fixed_witness: Path | None,
):
    input_path.write_text(json.dumps({"middle_path": path}) + "\n")
    command = [str(binary.resolve())]
    if fixed_witness is not None:
        command += ["--fixed-targets-file", str(fixed_witness)]
    command.append(str(input_path))
    process = subprocess.run(
        command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if process.returncode:
        raise RuntimeError((command, process.returncode, process.stderr))
    hall = json.loads(process.stdout.splitlines()[-1])
    if hall["status"] == "NOT_FACTORABLE":
        return {
            "residence_bad_motifs": linear_residence_violations(path, DEPTH),
            "structural_identity": False,
            "upper_holes": {},
            "lower_q1_holes": -1,
            "lower_q1_repeats": -1,
            "lower_q2_holes": -1,
            "lower_q3_holes": -1,
            "hall_deficiency": 1 << 30,
            "hall_zero_candidates": -1,
            "hall_zero_targets": [],
        }, hall
    upper = upper_loads([path])
    lower = {q: lower_loads([path], q) for q in (1, 2, 3)}
    audit = {
        "residence_bad_motifs": linear_residence_violations(path, DEPTH),
        "structural_identity": derive(linear_erosion(path, K, DEPTH), DEPTH) == path,
        "upper_holes": {
            str(q): comb(K, R + q) - len(upper[q]) for q in range(1, R)
        },
        "lower_q1_holes": comb(K, R - 1) - len(lower[1]),
        "lower_q1_repeats": sum(max(count - 1, 0) for count in lower[1].values()),
        "lower_q2_holes": comb(K, R - 2) - len(lower[2]),
        "lower_q3_holes": comb(K, R - 3) - len(lower[3]),
        "hall_deficiency": hall["deficiency"],
        "hall_zero_candidates": hall["zero_candidates"],
        "hall_zero_targets": hall["zero_targets"],
    }
    return audit, hall


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--permutation", help="comma-separated old->new coordinates")
    ap.add_argument("--permutation-seed", type=int, default=1)
    ap.add_argument("--seconds", type=float, default=300)
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--solutions", type=int, default=100)
    ap.add_argument(
        "--mixed-upper", action="store_true",
        help="encode all mixed union paths rather than only parent windows",
    )
    ap.add_argument("--no-upper", action="store_true", help="diagnostic only")
    ap.add_argument("--no-residence", action="store_true", help="diagnostic only")
    ap.add_argument(
        "--allow-cycle-cover", action="store_true",
        help="drop one-cycle connectivity and emit resident assignment covers",
    )
    ap.add_argument("--native-hall-bin", type=Path)
    ap.add_argument("--fixed-witness", type=Path)
    ap.add_argument(
        "--maximize-fixed-witness", action="store_true",
        help="maximize the exact bounded-interior N(A) contribution",
    )
    ap.add_argument("--fixed-patterns-file", type=Path)
    ap.add_argument("--native-fixed-pattern-bin", type=Path)
    ap.add_argument("--native-pattern-bundle", type=Path)
    ap.add_argument("--native-pattern-bundle-bin", type=Path)
    ap.add_argument("--hint-certificate", type=Path)
    ap.add_argument(
        "--hamming-radius", type=int,
        help="restrict trade bits to this Hamming radius around --hint-certificate",
    )
    ap.add_argument(
        "--hamming-min", type=int, default=0,
        help="optional minimum Hamming distance from --hint-certificate",
    )
    ap.add_argument(
        "--free-hint-zero-only", action="store_true",
        help="fix every hint-one trade and leave only hint-zero trades free",
    )
    ap.add_argument(
        "--benders-rounds", type=int, default=0,
        help="after each Hall failure, add a necessary bounded-interior DM cut",
    )
    ap.add_argument(
        "--boundary-cell-allowance", type=int, default=36,
        help="maximum non-interior cells credited in each necessary DM cut",
    )
    ap.add_argument(
        "--benders-balance", action="store_true",
        help="maximize the minimum priced slack across all accumulated cuts",
    )
    args = ap.parse_args()

    parent_a = load_path(args.source)
    if args.permutation:
        permutation = list(map(int, args.permutation.split(",")))
    else:
        rng = random.Random(args.permutation_seed)
        permutation = list(range(K))
        rng.shuffle(permutation)
    if sorted(permutation) != list(range(K)):
        raise SystemExit("permutation must contain 0,...,14")
    parent_b = [permute_mask(value, permutation) for value in parent_a]
    first, second = successor(parent_a), successor(parent_b)
    component, rows = assignment_components(first, second)

    variable_components = [index for index, row in enumerate(rows)
                           if len(row) > 1]
    variable_component = {cid: index for index, cid in enumerate(variable_components)}
    model = cp_model.CpModel()
    variables = [model.NewBoolVar(f"trade_{cid}") for cid in variable_components]

    # Matching-component choices already force indegree=outdegree=1.  AddCircuit
    # contributes only the global one-cycle requirement.
    nodes = sorted(first)
    node_index = {value: index for index, value in enumerate(nodes)}
    circuit = []
    for source in nodes:
        cid = component[source]
        index = variable_component.get(cid)
        if first[source] == second[source]:
            circuit.append((node_index[source], node_index[first[source]], 1))
        else:
            if index is None:
                raise AssertionError((source, cid))
            circuit.append((
                node_index[source], node_index[first[source]], variables[index].Not()
            ))
            circuit.append((
                node_index[source], node_index[second[source]], variables[index]
            ))
    if not args.allow_cycle_cover:
        model.AddCircuit(circuit)

    # Exclude the two inert parents.
    model.Add(sum(variables) >= 1)
    model.Add(sum(variables) <= len(variables) - 1)

    bundle_payload = None
    if args.native_pattern_bundle_bin:
        bundle_payload = native_bundle_payload(
            args.native_pattern_bundle_bin, args.source, permutation,
            args.fixed_witness if args.maximize_fixed_witness else None,
        )
    elif args.native_pattern_bundle:
        bundle_payload = json.loads(args.native_pattern_bundle.read_text())
    if bundle_payload is not None:
        if bundle_payload["variable_components"] != len(variables):
            raise AssertionError((
                bundle_payload["variable_components"], len(variables)
            ))
        native_bundle = bundle_payload["bundle"]
        bad_patterns = {
            decode_signed_pattern(row)
            for row in native_bundle["bad_residence_patterns"]
        }
    else:
        bad_patterns = enumerate_bad_residence_patterns(
            first, second, component, variable_component
        )
    if not args.no_residence:
        for pattern in bad_patterns:
            clause = []
            for index, value in pattern:
                clause.append(variables[index].Not() if value else variables[index])
            model.AddBoolOr(clause)

    mixed_prefixes = 0
    if args.mixed_upper:
        if bundle_payload is not None:
            mixed_prefixes = native_bundle["mixed_path_prefixes"]
            upper_patterns = defaultdict(set)
            for q, target, patterns in native_bundle["upper_patterns"]:
                upper_patterns[int(q), int(target)] = {
                    decode_signed_pattern(row) for row in patterns
                }
        else:
            upper_patterns, mixed_prefixes = mixed_upper_patterns(
                first, second, component, variable_component
            )
    else:
        upper_a = original_upper_patterns(
            parent_a, 0, first, second, component, variable_component
        )
        upper_b = original_upper_patterns(
            parent_b, 1, first, second, component, variable_component
        )
        upper_patterns = defaultdict(set)
        for key in set(upper_a) | set(upper_b):
            upper_patterns[key] = upper_a.get(key, set()) | upper_b.get(key, set())
    indicator_cache = {}
    upper_pattern_histogram = {}
    for q in range(1, R):
        counts = Counter()
        for target in range(1 << K):
            if target.bit_count() != R + q:
                continue
            patterns = upper_patterns.get((q, target), set())
            if not patterns:
                raise AssertionError((q, target, "parents do not cover target"))
            counts[len(patterns)] += 1
            if args.no_upper or () in patterns:
                continue
            literals = [
                add_pattern_indicator(model, variables, pattern, indicator_cache)
                for pattern in sorted(patterns)
            ]
            model.AddBoolOr(literals)
        upper_pattern_histogram[str(q)] = dict(sorted(counts.items()))

    fixed_pattern_indicators = []
    fixed_constant = 0
    fixed_prefixes = 0
    fixed_pattern_count = 0
    balance_slack = None
    priced_expressions = []
    if args.maximize_fixed_witness:
        if args.fixed_witness is None:
            raise SystemExit("--maximize-fixed-witness requires --fixed-witness")
        fixed_objective_terms = []
        native_payload = None
        if bundle_payload is not None and "patterns" in bundle_payload:
            native_payload = bundle_payload
        elif args.native_fixed_pattern_bin:
            native_payload = native_fixed_payload(
                args.native_fixed_pattern_bin, args.source, permutation,
                args.fixed_witness,
            )
        elif args.fixed_patterns_file:
            native_payload = json.loads(args.fixed_patterns_file.read_text())
        if native_payload is not None:
            fixed_prefixes = native_payload["completed_prefixes"]
            fixed_pattern_count = len(native_payload["patterns"])
            (fixed_constant, fixed_pattern_indicators,
             fixed_objective_terms) = add_native_weighted_patterns(
                model, variables, native_payload, "fixed_native"
            )
        else:
            fixed_patterns, fixed_prefixes = fixed_interior_patterns(
                first, second, component, variable_component,
                read_fixed_targets(args.fixed_witness),
            )
            for key, patterns in fixed_patterns.items():
                for serial, pattern in enumerate(sorted(patterns)):
                    fixed_pattern_count += 1
                    if not pattern:
                        fixed_constant += 1
                        continue
                    witness = model.NewBoolVar(
                        f"fixed_{key[0]}_{key[1]}_{serial}"
                    )
                    for index, value in pattern:
                        literal = variables[index] if value else variables[index].Not()
                        model.AddImplication(witness, literal)
                    fixed_pattern_indicators.append(witness)
                    fixed_objective_terms.append(witness)
        model.Maximize(sum(fixed_objective_terms))
        initial_expression = fixed_constant + sum(fixed_objective_terms)
        priced_expressions.append((
            initial_expression, len(read_fixed_targets(args.fixed_witness))
        ))
        if args.benders_rounds:
            initial_allowance = (
                0 if native_payload and native_payload.get("includes_boundary")
                else args.boundary_cell_allowance
            )
            initial_threshold = (
                len(read_fixed_targets(args.fixed_witness))
                - initial_allowance
            )
            model.Add(
                fixed_constant + sum(fixed_objective_terms) >= initial_threshold
            )
            if args.benders_balance:
                balance_slack = model.NewIntVar(-20000, 20000, "min_dm_slack")
                model.Add(
                    balance_slack
                    <= initial_expression + initial_allowance
                    - len(read_fixed_targets(args.fixed_witness))
                )
                model.ClearObjective()
                model.Maximize(balance_slack)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.randomize_search = True

    if args.hint_certificate:
        hint_payload = json.loads(args.hint_certificate.read_text())
        hint_values = list(map(int, hint_payload.get("trade_values", [])))
        if len(hint_values) != len(variables):
            raise ValueError(("hint trade dimension", len(hint_values), len(variables)))
        differences = []
        for variable, value in zip(variables, hint_values):
            model.AddHint(variable, value)
            differences.append(variable.Not() if value else variable)
            if args.free_hint_zero_only and value:
                model.Add(variable == 1)
        if args.hamming_radius is not None:
            model.Add(sum(differences) <= args.hamming_radius)
        if args.hamming_min:
            model.Add(sum(differences) >= args.hamming_min)
    elif args.hamming_radius is not None or args.hamming_min:
        raise SystemExit("Hamming bounds require --hint-certificate")

    best_hall = 1 << 30
    census = []
    terminal = "SOLUTIONS_EXHAUSTED"
    benders_cuts = []
    started = time.perf_counter()
    for serial in range(args.solutions):
        status = solver.Solve(model)
        status_name = solver.StatusName(status)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            terminal = status_name
            break
        values = [int(solver.BooleanValue(variable)) for variable in variables]
        dummy_path, physical_cycles = selected_cover(
            first, second, component, variable_component, values
        )
        path = dummy_path + [value for row in physical_cycles for value in row]
        if args.allow_cycle_cover:
            # The concatenation is only a diagnostic linearization.  The hard
            # constraints were checked on the genuine directed cycles; seams
            # are deliberately left for the component compiler.
            audit = {
                "residence_bad_motifs": sum(
                    linear_residence_violations(row + row[:4], DEPTH)
                    for row in physical_cycles
                ) + linear_residence_violations(dummy_path, DEPTH),
                "upper_holes": {},
                "lower_q1_holes": -1,
                "lower_q1_repeats": -1,
                "lower_q2_holes": -1,
                "lower_q3_holes": -1,
            }
            hall = {"deficiency": 1 << 30, "zero_candidates": -1}
        else:
            if args.native_hall_bin:
                audit, hall = native_candidate_audit(
                    path, args.native_hall_bin,
                    args.output.with_suffix(".native_input.json"),
                    args.fixed_witness,
                )
            else:
                audit, hall = exact_candidate_audit(path)
        if ((not args.no_residence and audit["residence_bad_motifs"])
                or (not args.no_upper and any(audit["upper_holes"].values()))):
            raise AssertionError(audit)
        row = {
            "serial": serial,
            "trades_selected": sum(values),
            "physical_cycles": len(physical_cycles),
            "dummy_path_vertices": len(dummy_path),
            "hall_deficiency": hall["deficiency"],
            "hall_zero_candidates": hall["zero_candidates"],
            "lower_q1_holes": audit["lower_q1_holes"],
            "lower_q1_repeats": audit["lower_q1_repeats"],
            "lower_q2_holes": audit["lower_q2_holes"],
            "lower_q3_holes": audit["lower_q3_holes"],
            "fixed_neighbourhood": hall.get("fixed_neighbourhood"),
            "fixed_objective_bound": (
                fixed_constant + round(solver.ObjectiveValue())
                if args.maximize_fixed_witness else None
            ),
        }
        census.append(row)
        print(json.dumps({"status": "CANDIDATE", **row}), flush=True)
        if args.allow_cycle_cover:
            checkpoint = args.output.with_name(
                f"{args.output.stem}.cover{serial}.json"
            )
            checkpoint.write_text(json.dumps({
                "status": "K15_RELABEL_TRADE_CYCLE_COVER",
                "source": str(args.source),
                "permutation": permutation,
                "trade_values": values,
                "middle_components": [dummy_path] + physical_cycles,
                "component_cyclic": [False] + [True] * len(physical_cycles),
                **row,
            }, indent=2, sort_keys=True) + "\n")
        elif hall["deficiency"] < best_hall:
            best_hall = hall["deficiency"]
            checkpoint = args.output.with_name(
                f"{args.output.stem}.hall{best_hall}.json"
            )
            checkpoint.write_text(json.dumps({
                "status": "K15_RELABEL_TRADE_CHECKPOINT",
                "source": str(args.source),
                "permutation": permutation,
                "trade_values": values,
                "middle_path": path,
                "middle_components": [path],
                "component_cyclic": [False],
                "hall": hall,
                **audit,
            }, indent=2, sort_keys=True) + "\n")
            print(json.dumps({
                "status": "HALL_IMPROVEMENT",
                "hall": best_hall,
                "checkpoint": str(checkpoint),
            }), flush=True)
            if best_hall == 0:
                terminal = "HALL_PASS"
                break
        if (
            args.benders_rounds
            and serial < args.benders_rounds
            and hall.get("deficiency", 0) > 0
        ):
            if args.native_fixed_pattern_bin is None:
                raise SystemExit("Benders mode requires --native-fixed-pattern-bin")
            witness_path = args.output.with_name(
                f"{args.output.stem}.dm{serial}.json"
            )
            witness_path.write_text(json.dumps({
                "dm_targets": hall["dm_targets"],
            }) + "\n")
            build_started = time.perf_counter()
            payload = native_fixed_payload(
                args.native_fixed_pattern_bin, args.source, permutation,
                witness_path,
            )
            constant, indicators, terms = add_native_weighted_patterns(
                model, variables, payload, f"benders_{serial}"
            )
            allowance = (
                0 if payload.get("includes_boundary")
                else args.boundary_cell_allowance
            )
            threshold = len(hall["dm_targets"]) - allowance
            model.Add(constant + sum(terms) >= threshold)
            expression = constant + sum(terms)
            priced_expressions.append((expression, len(hall["dm_targets"])))
            model.ClearObjective()
            if args.benders_balance:
                model.Add(
                    balance_slack
                    <= expression + allowance
                    - len(hall["dm_targets"])
                )
                model.Maximize(balance_slack)
            else:
                model.Maximize(sum(terms))
            cut = {
                "serial": serial,
                "dm_left": len(hall["dm_targets"]),
                "dm_right": len(hall["dm_cell_indices"]),
                "threshold": threshold,
                "boundary_allowance": allowance,
                "includes_boundary": bool(payload.get("includes_boundary")),
                "constant": constant,
                "patterns": len(payload["patterns"]),
                "prefixes": payload["completed_prefixes"],
                "build_seconds": time.perf_counter() - build_started,
            }
            benders_cuts.append(cut)
            print(json.dumps({"status": "BENDERS_INTERIOR_CUT", **cut}), flush=True)
        # Exact no-good on the component assignment.
        model.ClearHints()
        for variable, value in zip(variables, values):
            model.AddHint(variable, value)
        model.AddBoolOr([
            variable.Not() if value else variable
            for variable, value in zip(variables, values)
        ])

    summary = {
        "status": terminal,
        "source": str(args.source),
        "permutation": permutation,
        "assignment_components": len(rows),
        "fixed_components": sum(len(row) == 1 for row in rows),
        "variable_components": len(variables),
        "component_size_histogram": dict(Counter(map(len, rows))),
        "bad_residence_patterns": len(bad_patterns),
        "upper_pattern_histogram": upper_pattern_histogram,
        "mixed_upper": args.mixed_upper,
        "no_upper": args.no_upper,
        "no_residence": args.no_residence,
        "allow_cycle_cover": args.allow_cycle_cover,
        "mixed_path_prefixes": mixed_prefixes,
        "native_pattern_bundle": bundle_payload is not None,
        "pattern_indicators": len(indicator_cache),
        "fixed_pattern_count": fixed_pattern_count,
        "fixed_pattern_indicators": len(fixed_pattern_indicators),
        "fixed_constant": fixed_constant,
        "fixed_path_prefixes": fixed_prefixes,
        "benders_cuts": benders_cuts,
        "hint_certificate": str(args.hint_certificate) if args.hint_certificate else None,
        "hamming_radius": args.hamming_radius,
        "hamming_min": args.hamming_min,
        "enumerated": len(census),
        "best_hall": best_hall,
        "seconds": time.perf_counter() - started,
        "census": census,
    }
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in summary.items()
                      if key not in {"census", "upper_pattern_histogram"}},
                     sort_keys=True), flush=True)
    return 0 if best_hall == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
