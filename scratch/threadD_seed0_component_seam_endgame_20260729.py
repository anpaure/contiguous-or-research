#!/usr/bin/env python3
"""Proof-safe component/seam endgame for a resident k=15 factor.

The primary input is an exact 2-cycle, depth-three-resident middle factor with
complete lower and upper decks at every depth q=1,...,7.  This program chooses one
cut and one orientation for every physical cycle, then joins the resulting
paths with one residence-safe Johnson seam.  The seam must recycle one of the
two removed lower-q1 colours.
Hence the final path has exactly one missing lower-q1 colour, which is left to
the exact generalized linear compiler.

For every upper depth q=1,...,7, each target must retain an original literal
(q+1)-window or gain a literal cross-seam (q+1)-window.  In particular q=4 is
hard; the program does not rely on the obsolete q=1,2,3-only joint CNF.
Every decoded chronology is also checked by an independent arbitrary-width
upper oracle.  If that oracle finds any loss, the entire incumbent circuit is
blocked; no unsafe local projection is emitted.

Heavy CP-SAT work belongs on the H100 CPU.  Local uses are limited to exact
artifact replay, catalogue construction, and solver-free tests.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import platform
import socket
import sys
import time
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from audit_k15_global_rainbow_factor_candidate_20260729 import (  # noqa: E402
    physical_shadow_audit,
    residence_audit,
)
from graded_quotient_pipeline import (  # noqa: E402
    QuotientCatalogue,
    stable_json,
    validate_cycle_cover,
)
import threadD_k15_splice_compiler_postprocessor as compiler  # noqa: E402


SCHEMA = "threadD-resident-factor-component-seam-endgame-v2"
INPUT = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.best.json"
INPUT_SHA256 = "0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555"
INPUT_AUDIT = ROOT / "scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.independent.audit.json"
INPUT_AUDIT_SHA256 = "c5f700aef824b93e257957c313a7395eb3d2512c773e6d434f08934ba93ac6f4"
K, R, D, W = 15, 8, 3, 6435
FULL = (1 << K) - 1


def linear_residence_violations(path: Sequence[int], depth: int = D) -> int:
    """Count internal positive runs shorter than ``depth+1`` exactly."""
    bad = 0
    for start in range(len(path) - 1):
        inserted = int(path[start + 1]) & ~int(path[start])
        for delay in range(1, depth + 1):
            at = start + delay
            if at + 1 >= len(path):
                break
            if (int(path[at]) & ~int(path[at + 1])) & inserted:
                bad += 1
                break
    return bad


def derive(row: Sequence[int], depth: int) -> list[int]:
    answer = list(map(int, row))
    for _ in range(depth):
        answer = [answer[index] | answer[index + 1] for index in range(len(answer) - 1)]
    return answer


def linear_erosion(middle: Sequence[int], k: int, depth: int) -> list[int]:
    full = (1 << k) - 1
    values = list(map(int, middle))
    answer = []
    for index in range(len(values) + depth):
        value = full
        for source in range(
            max(0, index - depth), min(index, len(values) - 1) + 1
        ):
            value &= values[source]
        answer.append(value)
    return answer


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable_sha256(value: object) -> str:
    return sha256(stable_json(value)).hexdigest()


def no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer:
            raise ValueError(f"duplicate JSON key: {key}")
        answer[key] = value
    return answer


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(), object_pairs_hook=no_duplicate_object)
    if type(payload) is not dict:
        raise ValueError(f"{path}: expected one JSON object")
    return payload


def rank_masks(rank: int) -> set[int]:
    return {value for value in range(1 << K) if value.bit_count() == rank}


def fixed_window_targets(
    rows: Sequence[Sequence[int]], *, cyclic: bool
) -> tuple[dict[int, set[int]], dict[int, set[int]]]:
    lower = {q: set() for q in range(1, R)}
    upper = {q: set() for q in range(1, R)}
    for row in rows:
        n = len(row)
        for q in range(1, R):
            starts = range(n) if cyclic else range(max(0, n - q))
            for start in starts:
                lo, up = FULL, 0
                for offset in range(q + 1):
                    index = (start + offset) % n if cyclic else start + offset
                    value = int(row[index])
                    lo &= value
                    up |= value
                if lo.bit_count() == R - q:
                    lower[q].add(lo)
                if up.bit_count() == R + q:
                    upper[q].add(up)
    return lower, upper


def arbitrary_width_upper(path: Sequence[int]) -> dict[int, set[int]]:
    """Every nonempty linear interval union, compressed by first arrivals.

    For a fixed start, the interval union changes only at the first future
    occurrence of a currently absent coordinate.  Grouping tied arrivals is
    therefore an exact O(kW) oracle, not a fixed-width surrogate.
    """
    n = len(path)
    infinity = n + 1
    next_at = [[infinity] * K for _ in range(n + 1)]
    current = [infinity] * K
    for index in range(n - 1, -1, -1):
        value = int(path[index])
        for coordinate in range(K):
            if value & (1 << coordinate):
                current[coordinate] = index
        next_at[index] = list(current)
    got = {rank: set() for rank in range(R + 1, K + 1)}
    for start, initial in enumerate(map(int, path)):
        union = initial
        events: dict[int, int] = defaultdict(int)
        following = next_at[start + 1] if start + 1 <= n else [infinity] * K
        for coordinate in range(K):
            bit = 1 << coordinate
            if union & bit:
                continue
            arrival = following[coordinate]
            if arrival <= n - 1:
                events[arrival] |= bit
        for arrival in sorted(events):
            union |= events[arrival]
            if union.bit_count() > R:
                got[union.bit_count()].add(union)
    return got


def input_factor() -> tuple[
    QuotientCatalogue, dict[str, Any], list[list[int]], dict[str, Any]
]:
    if file_sha256(INPUT) != INPUT_SHA256:
        raise ValueError("two-cycle factor artifact hash mismatch")
    if file_sha256(INPUT_AUDIT) != INPUT_AUDIT_SHA256:
        raise ValueError("two-cycle independent-audit hash mismatch")
    payload = load_json(INPUT)
    retained = load_json(INPUT_AUDIT)
    if payload.get("schema") != "global-rainbow-factor-candidate-v1":
        raise ValueError("two-cycle candidate schema mismatch")
    for key, expected in (("k", K), ("r", R), ("d", D), ("W", W), ("N", 429)):
        if type(payload.get(key)) is not int or payload[key] != expected:
            raise ValueError(f"two-cycle factor {key} mismatch")
    catalogue = QuotientCatalogue(K)
    selected = catalogue.ids_from_explicit(payload.get("choices"))
    cycles, report = validate_cycle_cover(catalogue, selected)
    shadows = physical_shadow_audit(cycles, K, R)
    residence = residence_audit(cycles, K, D + 1)
    expected_cycles = list(map(int, retained["exact_fiber"]["physical_cycle_lengths"]))
    if list(map(len, cycles)) != expected_cycles or sum(map(len, cycles)) != W:
        raise AssertionError("resident-factor physical component ledger changed")
    if residence != retained.get("residence"):
        raise AssertionError("two-cycle residence replay disagrees with audit")
    if shadows != retained.get("physical_shadows"):
        raise AssertionError("two-cycle shadow replay disagrees with audit")
    if residence != {
        "residence_bad_runs": 0,
        "residence_shortfall": 0,
        "minimum_run": 4,
    }:
        raise AssertionError("two-cycle factor is not depth-three resident")
    if shadows["missing_upper_q1_physical"] or shadows["missing_lower_q2_physical"]:
        raise AssertionError("two-cycle factor lost a proved double-shadow deck")
    lower, upper = fixed_window_targets(cycles, cyclic=True)
    for q in range(1, R):
        if len(lower[q]) != comb(K, R - q):
            raise AssertionError(f"two-cycle factor lost cyclic lower depth {q}")
        if len(upper[q]) != comb(K, R + q):
            raise AssertionError(f"two-cycle factor lost cyclic upper depth {q}")
    if retained.get("candidate_sha256") != INPUT_SHA256:
        raise AssertionError("two-cycle audit points at another candidate")
    return catalogue, payload, cycles, report


@dataclass(frozen=True)
class State:
    serial: int
    component: int
    cut: int
    reverse: int
    left: int
    right: int
    cut_colour: int


@dataclass(frozen=True)
class Arc:
    serial: int
    source: int
    target: int
    recycled_state: int
    covered_initial_upper: tuple[int, ...]
    fixed_lower_targets: tuple[int, ...]
    fixed_upper_targets: tuple[int, ...]


def oriented_sequence(cycles: Sequence[Sequence[int]], state: State) -> list[int]:
    cycle = cycles[state.component]
    n = len(cycle)
    if not state.reverse:
        return [int(cycle[(state.cut + 1 + offset) % n]) for offset in range(n)]
    return [int(cycle[(state.cut - offset) % n]) for offset in range(n)]


def build_states(cycles: Sequence[Sequence[int]]) -> tuple[list[State], list[list[int]]]:
    states: list[State] = []
    by_component: list[list[int]] = [[] for _ in cycles]
    for component, cycle in enumerate(cycles):
        n = len(cycle)
        for cut in range(n):
            a, b = int(cycle[cut]), int(cycle[(cut + 1) % n])
            colour = a & b
            if colour.bit_count() != R - 1:
                raise AssertionError("factor cut is not a Johnson lower-q1 colour")
            for reverse in (0, 1):
                left, right = (a, b) if reverse else (b, a)
                state = State(
                    len(states), component, cut, reverse, left, right, colour
                )
                states.append(state)
                by_component[component].append(state.serial)
    return states, by_component


def prefix_union_profile(sequence: Sequence[int]) -> tuple[int, ...]:
    answer = []
    value = 0
    for mask in sequence:
        previous = value
        value |= int(mask)
        if value != previous:
            answer.append(value)
        if value == FULL:
            break
    return tuple(answer)


def boundary_profiles(
    cycles: Sequence[Sequence[int]], states: Sequence[State]
) -> tuple[
    list[tuple[int, ...]],
    list[tuple[int, ...]],
    list[tuple[int, ...]],
    list[tuple[int, ...]],
    list[tuple[int, ...]],
    list[tuple[int, ...]],
]:
    first4: list[tuple[int, ...]] = []
    last4: list[tuple[int, ...]] = []
    prefixes: list[tuple[int, ...]] = []
    suffixes: list[tuple[int, ...]] = []
    first7: list[tuple[int, ...]] = []
    last7: list[tuple[int, ...]] = []
    for state in states:
        sequence = oriented_sequence(cycles, state)
        first4.append(tuple(sequence[: D + 1]))
        last4.append(tuple(sequence[-(D + 1) :]))
        first7.append(tuple(sequence[:R]))
        last7.append(tuple(sequence[-R:]))
        prefixes.append(prefix_union_profile(sequence))
        suffixes.append(prefix_union_profile(list(reversed(sequence))))
    return first4, last4, prefixes, suffixes, first7, last7


def fixed_upper_across_seam(
    left: Sequence[int], right: Sequence[int]
) -> tuple[int, ...]:
    answer = set()
    for q in range(1, R):
        lhs, rhs = list(left[-q:]), list(right[:q])
        local = lhs + rhs
        boundary = len(lhs)
        for start in range(max(0, boundary - q), boundary):
            window = local[start : start + q + 1]
            if len(window) != q + 1:
                continue
            value = 0
            for mask in window:
                value |= int(mask)
            if value.bit_count() == R + q:
                answer.add(value)
    return tuple(sorted(answer))


def high_boundary_cells(sequence: Sequence[int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """The six rank-at-least-six cells of the maximal depth-three envelope."""
    if len(sequence) < D:
        raise ValueError("component is too short for a depth-three boundary")
    left = []
    value = FULL
    for mask in sequence[:D]:
        value &= int(mask)
        left.append(value)
    right_reversed = []
    value = FULL
    for mask in reversed(sequence[-D:]):
        value &= int(mask)
        right_reversed.append(value)
    # In physical envelope order these ranks are 6,7,8 at the right end.
    right = list(reversed(right_reversed))
    if sorted(value.bit_count() for value in (*left, *right)) != [6, 6, 7, 7, 8, 8]:
        raise AssertionError("resident state does not have the 6^2,7^2,8^2 boundary profile")
    return tuple(left), tuple(right)


def state_high_boundary_cells(
    cycles: Sequence[Sequence[int]], state: State
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    cycle = cycles[state.component]
    n = len(cycle)
    if state.reverse:
        at = lambda offset: int(cycle[(state.cut - offset) % n])
    else:
        at = lambda offset: int(cycle[(state.cut + 1 + offset) % n])
    collar = [at(offset) for offset in range(D)]
    collar.extend(at(offset) for offset in range(n - D, n))
    return high_boundary_cells(collar)


def contained_rank_masks(mask: int, rank: int) -> Iterable[int]:
    bits = [coordinate for coordinate in range(K) if mask & (1 << coordinate)]
    for chosen in combinations(bits, rank):
        value = 0
        for coordinate in chosen:
            value |= 1 << coordinate
        yield value


def fixed_lower_across_seam(
    left: Sequence[int], right: Sequence[int]
) -> tuple[int, ...]:
    """All correct-rank fixed-width intersections crossing one seam."""
    answer = set()
    for q in range(1, R):
        lhs, rhs = list(left[-q:]), list(right[:q])
        local = lhs + rhs
        boundary = len(lhs)
        for start in range(max(0, boundary - q), boundary):
            window = local[start : start + q + 1]
            if len(window) != q + 1:
                continue
            value = FULL
            for mask in window:
                value &= int(mask)
            if value.bit_count() == R - q:
                answer.add(value)
    return tuple(sorted(answer))


def require_distinct_paths(*paths: Path) -> None:
    resolved = [path.resolve() for path in paths]
    if len(resolved) != len(set(resolved)):
        raise ValueError("input, report, checkpoint, and word paths must be distinct")


def build_arcs(
    cycles: Sequence[Sequence[int]],
    states: Sequence[State],
    initially_missing: set[int],
) -> list[Arc]:
    by_left: dict[int, list[int]] = defaultdict(list)
    for state in states:
        by_left[state.left].append(state.serial)
    first4, last4, prefixes, suffixes, first7, last7 = boundary_profiles(
        cycles, states
    )
    arcs: list[Arc] = []
    for source in states:
        right = source.right
        # A lower-q1-recycling seam must be a Johnson edge.  Enumerating its
        # 8*7 neighbours avoids a quadratic state-pair scan.
        for deleted in range(K):
            if not (right & (1 << deleted)):
                continue
            for inserted in range(K):
                if right & (1 << inserted):
                    continue
                left_mask = right ^ (1 << deleted) ^ (1 << inserted)
                seam_colour = right & left_mask
                for target_serial in by_left.get(left_mask, ()):
                    target = states[target_serial]
                    if source.component == target.component:
                        continue
                    source_hit = seam_colour == source.cut_colour
                    target_hit = seam_colour == target.cut_colour
                    if source_hit == target_hit:
                        # Exactly one removed colour must be recycled here.
                        continue
                    if linear_residence_violations(
                        list(last4[source.serial]) + list(first4[target.serial]), D
                    ):
                        continue
                    covered = {
                        left_union | right_union
                        for left_union in suffixes[source.serial]
                        for right_union in prefixes[target.serial]
                        if (left_union | right_union) in initially_missing
                    }
                    arcs.append(
                        Arc(
                            len(arcs),
                            source.serial,
                            target.serial,
                            source.serial if source_hit else target.serial,
                            tuple(sorted(covered)),
                            fixed_lower_across_seam(
                                last7[source.serial], first7[target.serial]
                            ),
                            fixed_upper_across_seam(
                                last7[source.serial], first7[target.serial]
                            ),
                        )
                    )
    return arcs


def seam_ledger(
    path_states: Sequence[int],
    selected_arcs: Sequence[Arc],
    states: Sequence[State],
) -> list[dict[str, object]]:
    by_pair = {(arc.source, arc.target): arc for arc in selected_arcs}
    answer = []
    for source_serial, target_serial in zip(path_states, path_states[1:]):
        arc = by_pair[source_serial, target_serial]
        source, target = states[source_serial], states[target_serial]
        answer.append(
            {
                "source_state": source_serial,
                "target_state": target_serial,
                "source_component": source.component,
                "target_component": target.component,
                "left_mask": source.right,
                "right_mask": target.left,
                "intersection": source.right & target.left,
                "union": source.right | target.left,
                "symmetric_difference_size": (source.right ^ target.left).bit_count(),
                "recycled_state": arc.recycled_state,
                "recycled_cut_colour": states[arc.recycled_state].cut_colour,
                "covered_initial_upper_targets": list(arc.covered_initial_upper),
                "fixed_lower_targets": list(arc.fixed_lower_targets),
            }
        )
    return answer


def chronology_audit(
    path: Sequence[int], cycles: Sequence[Sequence[int]], seams: Sequence[dict[str, object]]
) -> dict[str, object]:
    if len(path) != W or len(set(map(int, path))) != W:
        raise AssertionError("assembled chronology is not a middle permutation")
    expected = {int(value) for cycle in cycles for value in cycle}
    if set(map(int, path)) != expected:
        raise AssertionError("assembled chronology changed the middle owner deck")
    residence = linear_residence_violations(list(map(int, path)), D)
    envelope = linear_erosion(list(map(int, path)), K, D)
    structural = derive(envelope, D) == list(map(int, path))
    lower, fixed_upper = fixed_window_targets([path], cyclic=False)
    arbitrary = arbitrary_width_upper(path)
    lower_holes = {
        str(q): comb(K, R - q) - len(lower[q]) for q in range(1, R)
    }
    fixed_upper_holes = {
        str(q): comb(K, R + q) - len(fixed_upper[q]) for q in range(1, R)
    }
    all_width_upper_holes = {
        str(rank - R): comb(K, rank) - len(arbitrary[rank])
        for rank in range(R + 1, K + 1)
    }
    hall = compiler.hall_deficiency_certificate(
        *compiler.compiler_adjacency(
            envelope,
            compiler.target_list(K, QuotientCatalogue(K).h),
        )[:1],
        len(envelope),
    )
    # The exact generalized compiler below has a stronger graded target
    # family.  This compact base Hall row is diagnostic only.
    return {
        "middle_length": len(path),
        "middle_sha256": stable_sha256(list(map(int, path))),
        "residence_violations": residence,
        "structural_identity": structural,
        "lower_holes": lower_holes,
        "fixed_width_upper_holes": fixed_upper_holes,
        "all_width_upper_holes": all_width_upper_holes,
        "seams": len(seams),
        "johnson_seams": sum(
            int(row["symmetric_difference_size"] == 2) for row in seams
        ),
        "base_literal_hall_matching": hall[0],
        "base_literal_hall": hall[2],
    }


def solve(args: argparse.Namespace) -> dict[str, object]:
    from ortools import __version__ as ortools_version
    from ortools.sat.python import cp_model

    require_distinct_paths(args.output, args.word, INPUT, INPUT_AUDIT)
    for round_index in range(args.rounds):
        checkpoint = args.output.with_name(
            f"{args.output.stem}.round{round_index:03d}.chronology.json"
        )
        require_distinct_paths(args.word, checkpoint)
    if args.soft_upper:
        raise ValueError("--soft-upper is undefined for an all-depth-complete input")
    if 1 in args.hard_lower_depths:
        raise ValueError("lower q1 cannot be hard-fixed on a W-vertex linear path")
    started = time.time()
    catalogue, payload, cycles, _factor_report = input_factor()
    cyclic_lower, cyclic_upper = fixed_window_targets(cycles, cyclic=True)
    initial_missing = {
        target
        for q in range(1, R)
        for target in rank_masks(R + q) - cyclic_upper[q]
    }
    states, by_component = build_states(cycles)
    arcs = build_arcs(cycles, states, initial_missing)
    supports: dict[int, list[int]] = defaultdict(list)
    recycled_incident: dict[int, list[int]] = defaultdict(list)
    for arc in arcs:
        recycled_incident[arc.recycled_state].append(arc.serial)
        for target in arc.covered_initial_upper:
            supports[target].append(arc.serial)

    model = cp_model.CpModel()
    selected_state = [model.NewBoolVar(f"s{state.serial}") for state in states]
    arc_var = [model.NewBoolVar(f"a{arc.serial}") for arc in arcs]
    start_var = [model.NewBoolVar(f"b{state.serial}") for state in states]
    end_var = [model.NewBoolVar(f"e{state.serial}") for state in states]
    state_by_cut: dict[tuple[int, int], list[int]] = defaultdict(list)
    for state in states:
        state_by_cut[state.component, state.cut].append(state.serial)
    cut_var: dict[tuple[int, int], object] = {}
    for key, serials in state_by_cut.items():
        if len(serials) != 2:
            raise AssertionError("a factor edge does not have two orientations")
        variable = model.NewBoolVar(f"cut_{key[0]}_{key[1]}")
        cut_var[key] = variable
        model.Add(variable == sum(selected_state[serial] for serial in serials))
    dummy = len(states)
    circuit = []
    for state in states:
        circuit.append((state.serial, state.serial, selected_state[state.serial].Not()))
        circuit.append((dummy, state.serial, start_var[state.serial]))
        circuit.append((state.serial, dummy, end_var[state.serial]))
    for arc in arcs:
        circuit.append((arc.source, arc.target, arc_var[arc.serial]))
    model.AddCircuit(circuit)
    for serials in by_component:
        model.AddExactlyOne(selected_state[serial] for serial in serials)
    for state in states:
        hits = [arc_var[index] for index in recycled_incident.get(state.serial, ())]
        if hits:
            model.Add(sum(hits) <= selected_state[state.serial])
        if args.endpoint_unrecycled_q1:
            # One seam recycles one of the two removed q1 colours.  The
            # unique unrecycled colour is compiler-eligible at a global path
            # endpoint: maximal erosion leaves the endpoint envelope equal
            # to its first/last middle mask, and residence protects the one
            # element omitted by the removed cut colour.  Do not permit the
            # unrecycled cut to sit strictly inside the component order.
            model.Add(
                sum(hits) + start_var[state.serial] + end_var[state.serial]
                >= selected_state[state.serial]
            )

    # Exact targetwise upper-window ledger.  A cyclic source witness survives
    # iff none of its q factor edges is cut.  Cross-seam q+1 windows are
    # supplied by the selected arc variables.  This is stronger than the
    # final arbitrary-width gate but every positive is literal and sound.
    upper_support: dict[int, list[object]] = defaultdict(list)
    witness_variables = 0
    witness_implications = 0
    for component, cycle in enumerate(cycles):
        n = len(cycle)
        for q in range(1, R):
            for start in range(n):
                target = 0
                for offset in range(q + 1):
                    target |= int(cycle[(start + offset) % n])
                if target.bit_count() != R + q:
                    continue
                witness = model.NewBoolVar(
                    f"uw_{component}_{q}_{start}"
                )
                witness_variables += 1
                span = [cut_var[component, (start + edge) % n] for edge in range(q)]
                for cut in span:
                    model.AddImplication(witness, cut.Not())
                    witness_implications += 1
                model.AddBoolOr([*span, witness])
                upper_support[target].append(witness)
    for arc in arcs:
        for target in arc.fixed_upper_targets:
            upper_support[target].append(arc_var[arc.serial])
    for rank in range(R + 1, K + 1):
        for target in rank_masks(rank):
            hits = upper_support.get(target, ())
            if not hits:
                impossible = model.NewBoolVar(f"upper_impossible_{target}")
                model.Add(impossible == 0)
                model.Add(impossible == 1)
            else:
                model.AddBoolOr(hits)

    # Optional exact preservation of selected lower shadow depths.  As for
    # the upper ledger, a cyclic witness survives iff none of its q edges is
    # cut, while every cross-seam witness is attached to its selected arc.
    # q=1 is intentionally excluded: a W-vertex linear path has only W-1
    # adjacencies, so exactly one lower-q1 hole is information-theoretically
    # unavoidable and is handled by the boundary compiler.
    lower_witness_variables = 0
    lower_witness_implications = 0
    tracked_lower_depths = set(args.hard_lower_depths)
    # q1/q2 are always needed by the exact special-cell SDR below.
    tracked_lower_depths.update((1, 2))
    lower_support_by_depth: dict[int, dict[int, list[object]]] = {}
    for q in sorted(tracked_lower_depths):
        if q < 1 or q >= R:
            raise ValueError(f"unsupported tracked lower depth {q}")
        lower_support: dict[int, list[object]] = defaultdict(list)
        lower_support_by_depth[q] = lower_support
        for component, cycle in enumerate(cycles):
            n = len(cycle)
            for start in range(n):
                target = FULL
                for offset in range(q + 1):
                    target &= int(cycle[(start + offset) % n])
                if target.bit_count() != R - q:
                    continue
                witness = model.NewBoolVar(f"lw_{q}_{component}_{start}")
                lower_witness_variables += 1
                span = [cut_var[component, (start + edge) % n]
                        for edge in range(q)]
                for cut in span:
                    model.AddImplication(witness, cut.Not())
                    lower_witness_implications += 1
                model.AddBoolOr([*span, witness])
                lower_support[target].append(witness)
        for arc in arcs:
            for target in arc.fixed_lower_targets:
                if target.bit_count() == R - q:
                    lower_support[target].append(arc_var[arc.serial])
        if q in args.hard_lower_depths:
            for target in rank_masks(R - q):
                hits = lower_support.get(target, ())
                if not hits:
                    impossible = model.NewBoolVar(f"lower_impossible_{q}_{target}")
                    model.Add(impossible == 0)
                    model.Add(impossible == 1)
                else:
                    model.AddBoolOr(hits)

    # Exact necessary Hall prefilter for the only high cells of the maximal
    # depth-three envelope.  Every lower-q1/q2 target either remains in its
    # fixed derivative row (internal or seam-crossing), or must be installed
    # literally at one of the six boundary cells.  Those cells have ranks
    # 8,7,6 on each side and each accepts at most one literal target.
    boundary_eligible: list[dict[int, list[object]]] = [
        defaultdict(list) for _ in range(2 * D)
    ]
    for state in states:
        left_cells, right_cells = state_high_boundary_cells(cycles, state)
        for slot, cell in enumerate((*left_cells, *right_cells)):
            endpoint = (
                start_var[state.serial] if slot < D else end_var[state.serial]
            )
            for rank in (R - 2, R - 1):
                if rank > cell.bit_count():
                    continue
                for target in contained_rank_masks(cell, rank):
                    boundary_eligible[slot][target].append(endpoint)

    boundary_assignments_by_slot: list[list[object]] = [
        [] for _ in range(2 * D)
    ]
    boundary_assignment_variables = 0
    boundary_assignment_implications = 0
    for q in (1, 2):
        for target in rank_masks(R - q):
            hits = list(lower_support_by_depth[q].get(target, ()))
            for slot in range(2 * D):
                eligible = boundary_eligible[slot].get(target, ())
                if not eligible:
                    continue
                assignment = model.NewBoolVar(f"boundary_{slot}_{target}")
                boundary_assignment_variables += 1
                model.AddBoolOr(eligible).OnlyEnforceIf(assignment)
                boundary_assignment_implications += 1
                boundary_assignments_by_slot[slot].append(assignment)
                hits.append(assignment)
            if not hits:
                impossible = model.NewBoolVar(f"boundary_impossible_{q}_{target}")
                model.Add(impossible == 0)
                model.Add(impossible == 1)
            else:
                model.AddBoolOr(hits)
    for assignments in boundary_assignments_by_slot:
        model.AddAtMostOne(assignments)
    upper_cover_var: dict[int, object] = {}
    for target in sorted(initial_missing):
        hits = [arc_var[index] for index in supports.get(target, ())]
        if not hits:
            impossible = model.NewBoolVar(f"impossible_{target}")
            model.Add(impossible == 0)
            model.Add(impossible == 1)
        elif args.soft_upper:
            covered = model.NewBoolVar(f"upper_{target}")
            upper_cover_var[target] = covered
            model.AddBoolOr(hits).OnlyEnforceIf(covered)
            for hit in hits:
                model.AddImplication(hit, covered)
        else:
            model.AddBoolOr(hits)
    if args.soft_upper:
        model.Maximize(sum(upper_cover_var.values()))

    # A previously audited near chronology is only a search hint.  Every
    # upper-survival, circuit, residence, and compiler condition remains hard
    # and is independently replayed below, so a stale or incompatible hint
    # cannot weaken the proof boundary.
    hinted_chronology = None
    if args.hint_chronology is not None:
        hint_payload = load_json(args.hint_chronology)
        raw_order = hint_payload.get("state_order")
        if type(raw_order) is not list:
            raise ValueError("hint chronology lacks state_order")
        order = list(map(int, raw_order))
        if len(order) != len(cycles) or len(set(order)) != len(order):
            raise ValueError("hint chronology has the wrong state count")
        if any(state < 0 or state >= len(states) for state in order):
            raise ValueError("hint chronology contains an unknown state")
        selected_hint = set(order)
        arc_hint = {(order[index], order[index + 1])
                    for index in range(len(order) - 1)}
        for state, variable in enumerate(selected_state):
            model.AddHint(variable, int(state in selected_hint))
        for arc in arcs:
            model.AddHint(
                arc_var[arc.serial], int((arc.source, arc.target) in arc_hint)
            )
        for state, variable in enumerate(start_var):
            model.AddHint(variable, int(state == order[0]))
        for state, variable in enumerate(end_var):
            model.AddHint(variable, int(state == order[-1]))
        hinted_chronology = str(args.hint_chronology)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(args.timeout)
    solver.parameters.num_search_workers = int(args.workers)
    solver.parameters.random_seed = int(args.seed)
    if args.log:
        solver.parameters.log_search_progress = True
    rounds = []
    proto = model.Proto()
    for round_index in range(args.rounds):
        round_started = time.time()
        status = solver.Solve(model)
        status_name = solver.StatusName(status)
        record: dict[str, object] = {
            "round": round_index,
            "status": status_name,
            "solver_seconds": time.time() - round_started,
        }
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            record["negative_scope"] = (
                "Solver status only for the explicit two-cycle state/arc model. "
                "No checked CP-SAT proof and no factor-level Benders cut."
            )
            rounds.append(record)
            break

        chosen_states = {
            state.serial for state in states if solver.Value(selected_state[state.serial])
        }
        chosen_arcs = [arc for arc in arcs if solver.Value(arc_var[arc.serial])]
        starts = [state.serial for state in states if solver.Value(start_var[state.serial])]
        if len(chosen_states) != len(cycles) or len(chosen_arcs) != len(cycles) - 1 or len(starts) != 1:
            raise AssertionError("decoded circuit has the wrong path ledger")
        successor = {arc.source: arc.target for arc in chosen_arcs}
        order = [starts[0]]
        while order[-1] in successor:
            order.append(successor[order[-1]])
        if len(order) != len(cycles) or set(order) != chosen_states:
            raise AssertionError("decoded circuit is not one component path")
        chronology = [
            value
            for state_serial in order
            for value in oriented_sequence(cycles, states[state_serial])
        ]
        seams = seam_ledger(order, chosen_arcs, states)
        audit = chronology_audit(chronology, cycles, seams)
        record.update(
            {
                "state_order": order,
                "component_order": [states[state].component for state in order],
                "cuts": [states[state].cut for state in order],
                "orientations": [states[state].reverse for state in order],
                "chronology": audit,
                "seam_ledger": seams,
            }
        )
        if args.soft_upper:
            local_covered = sum(
                int(solver.Value(variable)) for variable in upper_cover_var.values()
            )
            record.update(
                {
                    "initial_upper_local_covered": local_covered,
                    "initial_upper_local_deficiency": len(initial_missing)
                    - local_covered,
                    "initial_upper_objective": float(solver.ObjectiveValue()),
                    "initial_upper_best_bound": float(solver.BestObjectiveBound()),
                    "initial_upper_optimal": status == cp_model.OPTIMAL,
                }
            )
        rounds.append(record)
        checkpoint = args.output.with_name(
            f"{args.output.stem}.round{round_index:03d}.chronology.json"
        )
        checkpoint.write_text(
            json.dumps(
                {
                    "schema": SCHEMA,
                    "status": "AUDITED_CHRONOLOGY",
                    "source": str(INPUT),
                    "source_sha256": INPUT_SHA256,
                    "middle_path": chronology,
                    **record,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
        record["checkpoint"] = str(checkpoint)

        upper_clear = all(value == 0 for value in audit["all_width_upper_holes"].values())
        if audit["residence_violations"] or not audit["structural_identity"]:
            raise AssertionError("model emitted a nonresident chronology")
        if args.score_compiler:
            record["compiler_score"] = compiler.exact_compiler_for_opening(
                catalogue,
                chronology,
                W - 1,
                args.compiler_timeout,
                args.compiler_workers,
                args.seed + 2000 + round_index,
                None,
                False,
            )

        if not upper_clear:
            # Exact but deliberately weak CEGAR: exclude only this complete
            # circuit.  Missing arbitrary-width witnesses are never projected
            # onto a local fixed-width clause.
            model.AddBoolOr([arc_var[arc.serial].Not() for arc in chosen_arcs])
            continue

        compiler_result = compiler.exact_compiler_for_opening(
            catalogue,
            chronology,
            W - 1,
            args.compiler_timeout,
            args.compiler_workers,
            args.seed + 1000 + round_index,
            args.word,
            True,
        )
        record["compiler"] = compiler_result
        if compiler_result.get("status") == "VERIFIED_OPTIMAL":
            if args.word is None or not args.word.is_file():
                raise AssertionError("verified compiler did not retain its word")
            tokens = [int(value) for value in args.word.read_text().split()]
            if len(tokens) != W + D:
                raise AssertionError("verified word length is not 6438")
            record["status"] = "VERIFIED_OPTIMAL"
            break

        if "compiler_score" not in record:
            record["compiler_score"] = compiler.exact_compiler_for_opening(
                catalogue,
                chronology,
                W - 1,
                args.compiler_timeout,
                args.compiler_workers,
                args.seed + 2000 + round_index,
                None,
                False,
            )
        # A compiler failure is chronology-scoped.  Continue the exact seam
        # search, but emit no factor-level cut.
        model.AddBoolOr([arc_var[arc.serial].Not() for arc in chosen_arcs])

    result = {
        "schema": SCHEMA,
        "status": (
            "VERIFIED_OPTIMAL"
            if rounds and rounds[-1].get("status") == "VERIFIED_OPTIMAL"
            else "BOUNDED_NO_VERIFIED_WORD"
        ),
        "source": str(INPUT),
        "source_sha256": INPUT_SHA256,
        "source_audit": str(INPUT_AUDIT),
        "source_audit_sha256": INPUT_AUDIT_SHA256,
        "source_cycles": len(cycles),
        "source_cycle_lengths": list(map(len, cycles)),
        "source_cyclic_lower_holes": {
            str(q): comb(K, R - q) - len(cyclic_lower[q]) for q in range(1, R)
        },
        "source_cyclic_upper_holes": {
            str(q): comb(K, R + q) - len(cyclic_upper[q]) for q in range(1, R)
        },
        "initial_missing_upper_targets": len(initial_missing),
        "state_count": len(states),
        "arc_count": len(arcs),
        "model_variables": len(proto.variables),
        "model_constraints": len(proto.constraints),
        "upper_witness_variables": witness_variables,
        "upper_witness_implications": witness_implications,
        "hard_lower_depths": list(args.hard_lower_depths),
        "endpoint_unrecycled_q1": bool(args.endpoint_unrecycled_q1),
        "compiler_benders_requested": bool(args.compiler_benders),
        "compiler_benders_dynamic_rows": False,
        "lower_witness_variables": lower_witness_variables,
        "lower_witness_implications": lower_witness_implications,
        "boundary_sdr_ranks": [R - 2, R - 1],
        "boundary_sdr_cell_ranks": [8, 7, 6, 6, 7, 8],
        "boundary_assignment_variables": boundary_assignment_variables,
        "boundary_assignment_implications": boundary_assignment_implications,
        "ortools_version": ortools_version,
        "workers": args.workers,
        "soft_upper": args.soft_upper,
        "hint_chronology": hinted_chronology,
        "rounds": rounds,
        "wall_time": time.time() - started,
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "proof_scope": (
            "Positive only: a VERIFIED_OPTIMAL status requires exact two-cycle "
            "artifact replay, one cut per physical component, the exact "
            "component-count-minus-one explicit "
            "residence-safe q1-recycling seams, unrestricted-upper replay, "
            "the exact linear generalized compiler, a retained 6438-entry "
            "word, and the independent literal verifier. UNKNOWN, timeout, "
            "bounded exhaustion, or unproved INFEASIBLE emits no Benders cut. "
            "Any negative is confined to the one-useful-seam, literal "
            "fixed-upper-window face; it does not exclude the sharp face with "
            "a non-recycling but otherwise compiler-compatible seam, nor a solution "
            "whose upper witness requires more than q+1 middle states.  If "
            f"hard_lower_depths={list(args.hard_lower_depths)} is nonempty, "
            "those extra fixed-lower-window restrictions also belong to the "
            "negative scope."
        ),
        "sandwich2_used": False,
        "ready15_used": False,
    }
    result["audit_sha256"] = stable_sha256(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def audit_only() -> dict[str, object]:
    catalogue, _payload, cycles, _report = input_factor()
    lower, upper = fixed_window_targets(cycles, cyclic=True)
    states, _by_component = build_states(cycles)
    missing = {
        target
        for q in range(1, R)
        for target in rank_masks(R + q) - upper[q]
    }
    arcs = build_arcs(cycles, states, missing)
    support = {target: 0 for target in missing}
    for arc in arcs:
        for target in arc.covered_initial_upper:
            support[target] += 1
    return {
        "schema": SCHEMA,
        "status": "SOLVER_FREE_FACTOR_CATALOGUE_AUDIT_PASS",
        "source_sha256": INPUT_SHA256,
        "source_audit_sha256": INPUT_AUDIT_SHA256,
        "choice_table_sha256": catalogue.choice_table_sha256,
        "physical_components": len(cycles),
        "component_lengths": list(map(len, cycles)),
        "lower_holes": {
            str(q): comb(K, R - q) - len(lower[q]) for q in range(1, R)
        },
        "upper_holes": {
            str(q): comb(K, R + q) - len(upper[q]) for q in range(1, R)
        },
        "states": len(states),
        "arcs": len(arcs),
        "initial_missing_upper_targets": len(missing),
        "initial_targets_without_local_seam_support": sum(
            value == 0 for value in support.values()
        ),
        "initial_target_support_histogram": {
            str(value): count for value, count in sorted(Counter(support.values()).items())
        },
        "negative_scope": "None; this command performs no SAT solve.",
    }


def score_chronology(args: argparse.Namespace) -> dict[str, object]:
    require_distinct_paths(args.chronology, args.output, INPUT, INPUT_AUDIT)
    payload = load_json(args.chronology)
    if payload.get("source_sha256") != INPUT_SHA256:
        raise ValueError("chronology was not derived from the frozen primary factor")
    path = payload.get("middle_path")
    if type(path) is not list or len(path) != W:
        raise ValueError("chronology needs exactly 6435 explicit middle masks")
    catalogue, _candidate, cycles, _report = input_factor()
    seams = payload.get("seam_ledger", [])
    audit = chronology_audit(list(map(int, path)), cycles, seams)
    score = compiler.exact_compiler_for_opening(
        catalogue,
        list(map(int, path)),
        W - 1,
        args.timeout,
        args.workers,
        args.seed,
        None,
        False,
    )
    result = {
        "schema": SCHEMA,
        "status": score.get("status"),
        "chronology": str(args.chronology),
        "chronology_sha256": file_sha256(args.chronology),
        "source_sha256": INPUT_SHA256,
        "chronology_audit": audit,
        "compiler_score": score,
        "negative_scope": (
            "An exact OPTIMAL score is for this fixed 6435-state chronology "
            "and the declared generalized linear one-core compiler only."
        ),
    }
    result["audit_sha256"] = stable_sha256(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def compile_chronology(args: argparse.Namespace) -> dict[str, object]:
    require_distinct_paths(
        args.chronology, args.output, args.word, INPUT, INPUT_AUDIT
    )
    """Run only the exact generalized compiler on one audited chronology."""
    payload = load_json(args.chronology)
    if payload.get("source_sha256") != INPUT_SHA256:
        raise ValueError("chronology was not derived from the frozen primary factor")
    path = payload.get("middle_path")
    if type(path) is not list or len(path) != W:
        raise ValueError("chronology needs exactly 6435 explicit middle masks")
    catalogue, _candidate, cycles, _report = input_factor()
    seams = payload.get("seam_ledger", [])
    audit = chronology_audit(list(map(int, path)), cycles, seams)
    if any(audit["all_width_upper_holes"].values()):
        raise ValueError("refuse compiler: chronology has an upper hole")
    if audit["residence_violations"] or not audit["structural_identity"]:
        raise ValueError("refuse compiler: chronology is not structurally valid")
    compiled = compiler.exact_compiler_for_opening(
        catalogue,
        list(map(int, path)),
        W - 1,
        args.timeout,
        args.workers,
        args.seed,
        args.word,
        True,
    )
    result = {
        "schema": SCHEMA,
        "status": compiled.get("status"),
        "chronology": str(args.chronology),
        "chronology_sha256": file_sha256(args.chronology),
        "source_sha256": INPUT_SHA256,
        "chronology_audit": audit,
        "compiler": compiled,
        "negative_scope": (
            "Any negative solver status concerns this fixed audited chronology "
            "and the declared exact generalized compiler only."
        ),
    }
    result["audit_sha256"] = stable_sha256(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    audit_parser = sub.add_parser("audit")
    audit_parser.add_argument("--output", type=Path)
    run = sub.add_parser("solve")
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--word", type=Path, required=True)
    run.add_argument("--timeout", type=float, default=1800.0)
    run.add_argument("--workers", type=int, default=4)
    run.add_argument("--seed", type=int, default=20260729)
    run.add_argument("--rounds", type=int, default=100)
    run.add_argument("--compiler-timeout", type=float, default=1800.0)
    run.add_argument("--compiler-workers", type=int, default=4)
    run.add_argument("--log", action="store_true")
    run.add_argument(
        "--soft-upper",
        action="store_true",
        help="legacy diagnostic; the frozen all-depth factor has no initial upper holes",
    )
    run.add_argument(
        "--score-compiler",
        action="store_true",
        help="solve the exact generalized compiler score on every chronology",
    )
    run.add_argument(
        "--hint-chronology",
        type=Path,
        help="audited near chronology used only as a CP-SAT search hint",
    )
    run.add_argument(
        "--hard-lower-depths",
        default="",
        help="comma-separated exact lower depths to preserve (typically 2,3)",
    )
    run.add_argument(
        "--endpoint-unrecycled-q1",
        action="store_true",
        help="force the unique unrecycled cut colour onto a path endpoint",
    )
    run.add_argument(
        "--compiler-benders",
        action="store_true",
        help=(
            "legacy compatibility flag; the q1/q2 six-boundary-cell SDR is "
            "always hard and no projected Hall-root row is emitted"
        ),
    )
    score_parser = sub.add_parser("score-chronology")
    score_parser.add_argument("chronology", type=Path)
    score_parser.add_argument("--output", type=Path, required=True)
    score_parser.add_argument("--timeout", type=float, default=900.0)
    score_parser.add_argument("--workers", type=int, default=1)
    score_parser.add_argument("--seed", type=int, default=1801)
    compile_parser = sub.add_parser("compile-chronology")
    compile_parser.add_argument("chronology", type=Path)
    compile_parser.add_argument("--output", type=Path, required=True)
    compile_parser.add_argument("--word", type=Path, required=True)
    compile_parser.add_argument("--timeout", type=float, default=900.0)
    compile_parser.add_argument("--workers", type=int, default=1)
    compile_parser.add_argument("--seed", type=int, default=2801)
    args = parser.parse_args()
    if args.command == "solve":
        args.hard_lower_depths = tuple(
            sorted({int(value) for value in args.hard_lower_depths.split(",")
                    if value})
        )
    if args.command == "audit":
        result = audit_only()
        if args.output is not None:
            require_distinct_paths(args.output, INPUT, INPUT_AUDIT)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    elif args.command == "solve":
        result = solve(args)
    elif args.command == "score-chronology":
        result = score_chronology(args)
    else:
        result = compile_chronology(args)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] in (
        "SOLVER_FREE_FACTOR_CATALOGUE_AUDIT_PASS",
        "VERIFIED_OPTIMAL",
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
