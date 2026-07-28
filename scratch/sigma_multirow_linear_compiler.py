#!/usr/bin/env python3
"""Compile a *linear* middle path through a depth-d OR--Pascal sandwich.

Unlike sigma_multirow_compiler.py, this file has no cyclic wrap and no later
cut.  For a middle path T of length W it uses the maximal linear erosion P of
length W+d.  A structural check D^d P=T is necessary and sufficient for some
depth-d preimage to exist.  SAT then chooses A<=P, enforces D^d A=T, and makes
the rows D^0,...,D^(d-1) cover the whole lower ideal.

The local mode starts from a known word and a 2-opt segment reversal.  Only a
small collar around the two reversal seams is released; everything else is
fixed.  This directly tests whether a central cycle-space improvement lifts
through the lower compiler.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations
import json
from math import comb
import os
from pathlib import Path
import subprocess
import tempfile
import time

from sigma_sat_solver import CNF, parse_model


KISSAT = os.environ.get("KISSAT", "/opt/homebrew/bin/kissat")


def derivative(row: list[int]) -> list[int]:
    return [row[i] | row[i + 1] for i in range(len(row) - 1)]


def derive(row: list[int], depth: int) -> list[int]:
    for _ in range(depth):
        row = derivative(row)
    return row


def linear_erosion(middle: list[int], k: int, depth: int) -> list[int]:
    full = (1 << k) - 1
    n = len(middle)
    allowed = []
    for i in range(n + depth):
        value = full
        for j in range(max(0, i - depth), min(i, n - 1) + 1):
            value &= middle[j]
        allowed.append(value)
    return allowed


def all_masks_of_rank(k: int, rank: int):
    for choice in combinations(range(k), rank):
        yield sum(1 << x for x in choice)


def full_coverage(word: list[int], k: int):
    full = (1 << k) - 1
    covered = set()
    for start in range(len(word)):
        value = 0
        for end in range(start, len(word)):
            value |= word[end]
            covered.add(value)
            if value == full:
                break
    missing = [value for value in range(1, 1 << k) if value not in covered]
    return missing


def parse_middle_and_seed(args):
    seed = None
    move = None
    if args.source_word is not None:
        source = [int(token) for token in args.source_word.read_text().split()]
        middle = derive(source, args.depth)
        if args.two_opt is None:
            seed = source
        else:
            i, j = args.two_opt
            if not (0 <= i < j < len(middle) - 1):
                raise SystemExit("invalid --two-opt indices")
            middle = middle[: i + 1] + list(reversed(middle[i + 1 : j + 1])) + middle[j + 1 :]
            seed = source[:]
            seed[i + 1 : j + args.depth + 1] = reversed(
                seed[i + 1 : j + args.depth + 1]
            )
            move = (i, j)
    elif args.certificate is not None:
        data = json.loads(args.certificate.read_text())
        middle = list(map(int, data.get("middle_path", data.get("middle_cycle", []))))
        if not middle and data.get("best"):
            middle = list(map(int, data["best"][0].get("middle_path", [])))
        if not middle:
            raise SystemExit("certificate has no middle_path/middle_cycle")
        if args.seed_word is not None:
            seed = [int(token) for token in args.seed_word.read_text().split()]
    else:
        raise SystemExit("provide --source-word or a certificate")
    return middle, seed, move


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path, nargs="?")
    parser.add_argument("--source-word", type=Path)
    parser.add_argument("--seed-word", type=Path)
    parser.add_argument("--two-opt", type=int, nargs=2, metavar=("I", "J"))
    parser.add_argument(
        "--reverse-middle",
        action="store_true",
        help="reverse the supplied middle certificate before compilation",
    )
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--depth", type=int, required=True)
    parser.add_argument("--local-radius", type=int, default=0)
    parser.add_argument(
        "--auto-expand",
        action="store_true",
        help="release remote envelope windows when a local collar has no witness",
    )
    parser.add_argument("--output-word", type=Path)
    parser.add_argument(
        "--solver",
        default=KISSAT,
        help="SAT solver executable (ignored with --build-only/--model-file)",
    )
    parser.add_argument(
        "--cnf-output",
        type=Path,
        help="keep the deterministic DIMACS instance at this path",
    )
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument(
        "--model-file",
        type=Path,
        help="decode an existing DIMACS solver output instead of solving",
    )
    parser.add_argument("--report-output", type=Path)
    parser.add_argument("--timeout", type=float, default=300.0)
    parser.add_argument(
        "--target-ranks",
        type=int,
        nargs="+",
        help=(
            "diagnostic mode: require coverage only for these lower ranks; "
            "middle realization is still enforced exactly"
        ),
    )
    parser.add_argument(
        "--target-mask-file",
        type=Path,
        help=(
            "diagnostic mode: whitespace/JSON list of exact lower masks whose "
            "coverage clauses are enabled"
        ),
    )
    parser.add_argument(
        "--required-interval-mask-file",
        type=Path,
        help=(
            "whitespace/JSON list of masks that must occur as ORs of arbitrary "
            "contiguous intervals of the compiled word (masks may lie above "
            "the middle rank)"
        ),
    )
    parser.add_argument(
        "--required-interval-max-length",
        type=int,
        default=0,
        help="optional maximum length for required arbitrary-interval witnesses",
    )
    parser.add_argument(
        "--fixed-append-mask",
        type=int,
        default=0,
        help=(
            "append this fixed nonzero mask after the compiled word; required "
            "arbitrary-interval witnesses may cross into it"
        ),
    )
    args = parser.parse_args()

    middle, seed, move = parse_middle_and_seed(args)
    if args.reverse_middle:
        middle.reverse()
        if seed is not None:
            seed.reverse()
    k, depth = args.k, args.depth
    r = (k + 1) // 2
    allowed = linear_erosion(middle, k, depth)
    maximal_middle = derive(allowed[:], depth)
    structural_bad = [
        i for i, (want, got) in enumerate(zip(middle, maximal_middle)) if want != got
    ]
    report: dict[str, object] = {
        "k": k,
        "depth": depth,
        "middle_length": len(middle),
        "word_length": len(allowed),
        "middle_rank_histogram": dict(Counter(value.bit_count() for value in middle)),
        "allowed_rank_histogram": dict(Counter(value.bit_count() for value in allowed)),
        "structural_residence_failures": len(structural_bad),
        "first_structural_failures": structural_bad[:25],
        "mode": "global" if not (seed is not None and args.local_radius) else "local",
        "two_opt": list(move) if move else None,
    }
    if structural_bad:
        report["status"] = "STRUCTURAL_UNSAT"
        print(json.dumps(report, indent=2, sort_keys=True))
        return 2

    if seed is not None and len(seed) != len(allowed):
        raise SystemExit("seed length does not equal W+depth")

    requested_ranks = set(args.target_ranks or range(1, r))
    requested_masks = None
    if args.target_mask_file is not None:
        raw = args.target_mask_file.read_text().strip()
        if raw.startswith("["):
            requested_masks = set(map(int, json.loads(raw)))
        else:
            requested_masks = {int(token) for token in raw.split()}
    required_interval_masks = set()
    if args.required_interval_mask_file is not None:
        raw = args.required_interval_mask_file.read_text().strip()
        if raw.startswith("["):
            required_interval_masks = set(map(int, json.loads(raw)))
        else:
            required_interval_masks = {int(token) for token in raw.split()}

    if seed is not None and args.local_radius:
        if move is None:
            raise SystemExit("local mode currently needs --source-word and --two-opt")
        i, j = move
        centres = (i + 1, j + depth)
        free_positions = {
            p
            for centre in centres
            for p in range(centre - args.local_radius, centre + args.local_radius + 1)
            if 0 <= p < len(allowed)
        }
        # Every seed/envelope violation must be released even if just outside
        # the requested collar.
        free_positions.update(
            p for p, (value, envelope) in enumerate(zip(seed, allowed)) if value & ~envelope
        )
    else:
        free_positions = set(range(len(allowed)))

    expansion_rounds = []

    def coverage_frontier():
        fixed_now = {
            p: seed[p]
            for p in range(len(allowed))
            if seed is not None and p not in free_positions
        }
        if any(value & ~allowed[p] for p, value in fixed_now.items()):
            raise AssertionError("fixed seed entry lies outside maximal erosion")
        fixed_seen_now = set()
        variable_windows_now = []
        for row_depth in range(depth):
            for start in range(len(allowed) - row_depth):
                positions = tuple(range(start, start + row_depth + 1))
                if any(p in free_positions for p in positions):
                    forced = 0
                    envelope = 0
                    for p in positions:
                        forced |= fixed_now.get(p, 0)
                        envelope |= allowed[p]
                    variable_windows_now.append((positions, forced, envelope))
                else:
                    value = 0
                    for p in positions:
                        value |= fixed_now[p]
                    if value and value.bit_count() < r:
                        fixed_seen_now.add(value)
        candidates_now = defaultdict(list)
        for positions, forced, envelope in variable_windows_now:
            free = envelope & ~forced
            subset = free
            while True:
                target = forced | subset
                if target and target.bit_count() < r and target not in fixed_seen_now:
                    candidates_now[target].append((positions, forced, envelope))
                if subset == 0:
                    break
                subset = (subset - 1) & free
        lower_targets_now = [
            value
            for value in range(1, 1 << k)
            if value.bit_count() < r
            and value.bit_count() in requested_ranks
            and (requested_masks is None or value in requested_masks)
            and value not in fixed_seen_now
        ]
        missing_now = [target for target in lower_targets_now if not candidates_now[target]]
        return (
            fixed_now,
            fixed_seen_now,
            variable_windows_now,
            candidates_now,
            lower_targets_now,
            missing_now,
        )

    while True:
        fixed, fixed_seen, variable_windows, candidates, lower_targets, missing_candidates = (
            coverage_frontier()
        )
        if not missing_candidates or not args.auto_expand:
            break
        released = set()
        for target in missing_candidates:
            options = []
            for row_depth in range(depth):
                for start in range(len(allowed) - row_depth):
                    positions = tuple(range(start, start + row_depth + 1))
                    envelope = 0
                    for p in positions:
                        envelope |= allowed[p]
                    if not target & ~envelope:
                        new_positions = set(positions) - free_positions
                        options.append((len(new_positions), start, positions))
            if not options:
                break
            _, _, positions = min(options)
            released.update(positions)
        released -= free_positions
        if not released:
            break
        expansion_rounds.append(
            {
                "missing_targets": len(missing_candidates),
                "released_positions": sorted(released),
            }
        )
        free_positions.update(released)

    cnf = CNF()
    entry: dict[tuple[int, int], int] = {}
    for p in sorted(free_positions):
        variables = []
        for x in range(k):
            if allowed[p] & (1 << x):
                entry[p, x] = cnf.var()
                variables.append(entry[p, x])
        if not variables:
            report.update({"status": "STRUCTURAL_UNSAT", "reason": f"empty envelope at {p}"})
            print(json.dumps(report, indent=2, sort_keys=True))
            return 2
        cnf.add(*variables)  # entries are normalized nonzero

    # Enforce every positive coordinate of every middle cell.  A<=P already
    # enforces all negative coordinates.
    for start, target in enumerate(middle):
        positions = range(start, start + depth + 1)
        forced = 0
        for p in positions:
            forced |= fixed.get(p, 0)
        for x in range(k):
            bit = 1 << x
            if not target & bit or forced & bit:
                continue
            variables = [entry[p, x] for p in positions if (p, x) in entry]
            if not variables:
                report.update(
                    {
                        "status": "STRUCTURAL_UNSAT",
                        "reason": f"middle coordinate ({start},{x}) has no free witness",
                    }
                )
                print(json.dumps(report, indent=2, sort_keys=True))
                return 2
            cnf.add(*variables)

    # Pay a small upper-side debt using arbitrary word intervals rather than
    # only the canonical consecutive-middle windows.  For a requested target,
    # feasible positions form short runs: every variable entry in the chosen
    # interval must retain at least one target bit so it can stay nonzero.
    # A selector forces the interval OR to equal the target exactly.
    required_interval_candidate_counts: dict[int, int] = {}
    required_interval_selector_count = 0
    for target in sorted(required_interval_masks):
        selectors = []
        for start in range(len(allowed)):
            envelope = 0
            forced = 0
            for end in range(start, len(allowed)):
                if (
                    args.required_interval_max_length
                    and end - start + 1 > args.required_interval_max_length
                ):
                    break
                if end in fixed:
                    value = fixed[end]
                    if value & ~target:
                        break
                    forced |= value
                    envelope |= value
                else:
                    feasible = allowed[end] & target
                    if not feasible:
                        break
                    envelope |= feasible
                if target & ~envelope:
                    continue
                selector = cnf.var()
                selectors.append(selector)
                required_interval_selector_count += 1
                positions = range(start, end + 1)
                for x in range(k):
                    bit = 1 << x
                    variables = [entry[p, x] for p in positions if (p, x) in entry]
                    if target & bit:
                        if not forced & bit:
                            cnf.add(-selector, *variables)
                    else:
                        for variable in variables:
                            cnf.add(-selector, -variable)

        # Optional one-cell extension.  This is useful when the conjectured
        # base length misses one nested target S: appending S pays that target
        # directly, while a suffix of the compiled word may combine with S to
        # pay a larger target.  The appended cell is fixed and therefore adds
        # no SAT variables.
        append_mask = args.fixed_append_mask
        if append_mask and not (append_mask & ~target):
            envelope = append_mask
            forced = append_mask
            # The appended singleton interval itself is a candidate when it
            # equals the target.
            if envelope == target:
                selector = cnf.var()
                selectors.append(selector)
                required_interval_selector_count += 1
                cnf.add(selector)
            max_word_cells = (
                args.required_interval_max_length - 1
                if args.required_interval_max_length else len(allowed)
            )
            for word_cells in range(1, min(len(allowed), max_word_cells) + 1):
                start = len(allowed) - word_cells
                p = start
                if p in fixed:
                    value = fixed[p]
                    if value & ~target:
                        break
                    forced |= value
                    envelope |= value
                else:
                    feasible = allowed[p] & target
                    if not feasible:
                        break
                    envelope |= feasible
                if target & ~envelope:
                    continue
                selector = cnf.var()
                selectors.append(selector)
                required_interval_selector_count += 1
                positions = range(start, len(allowed))
                for x in range(k):
                    bit = 1 << x
                    variables = [entry[q, x] for q in positions if (q, x) in entry]
                    if target & bit:
                        if not forced & bit:
                            cnf.add(-selector, *variables)
                    else:
                        for variable in variables:
                            cnf.add(-selector, -variable)
        required_interval_candidate_counts[target] = len(selectors)
        if not selectors:
            report.update(
                {
                    "status": "INTERVAL_ENVELOPE_UNSAT",
                    "required_interval_mask": target,
                    "required_interval_candidate_counts": (
                        required_interval_candidate_counts
                    ),
                }
            )
            print(json.dumps(report, indent=2, sort_keys=True))
            return 4
        cnf.add(*selectors)
    report.update(
        {
            "free_positions": len(free_positions),
            "fixed_lower_targets": len(fixed_seen),
            "sat_lower_targets": len(lower_targets),
            "requested_target_ranks": sorted(requested_ranks),
            "requested_target_masks": (
                None if requested_masks is None else len(requested_masks)
            ),
            "variable_windows": len(variable_windows),
            "targets_without_candidate": len(missing_candidates),
            "first_targets_without_candidate": missing_candidates[:25],
            "auto_expansion_rounds": expansion_rounds,
            "required_interval_masks": len(required_interval_masks),
            "required_interval_candidate_counts": (
                required_interval_candidate_counts
            ),
            "required_interval_selectors": required_interval_selector_count,
        }
    )
    if missing_candidates:
        report["status"] = "LOCAL_ENVELOPE_UNSAT"
        print(json.dumps(report, indent=2, sort_keys=True))
        return 3

    selector_count = 0
    for target in lower_targets:
        selectors = []
        for positions, forced, envelope in candidates[target]:
            selector = cnf.var()
            selector_count += 1
            selectors.append(selector)
            for x in range(k):
                bit = 1 << x
                variables = [entry[p, x] for p in positions if (p, x) in entry]
                if target & bit:
                    if not forced & bit:
                        cnf.add(-selector, *variables)
                else:
                    for variable in variables:
                        cnf.add(-selector, -variable)
        cnf.add(*selectors)

    report.update(
        {
            "variables": cnf.nvars,
            "clauses": len(cnf.clauses),
            "selectors": selector_count,
        }
    )

    temporary_cnf = args.cnf_output is None
    if temporary_cnf:
        with tempfile.NamedTemporaryFile(suffix=".cnf", delete=False) as handle:
            cnf_path = Path(handle.name)
    else:
        cnf_path = args.cnf_output
        cnf_path.parent.mkdir(parents=True, exist_ok=True)
    cnf.write(cnf_path)
    report["cnf"] = str(cnf_path)
    if args.build_only:
        report["status"] = "BUILT"
        rendered = json.dumps(report, indent=2, sort_keys=True)
        if args.report_output is not None:
            args.report_output.write_text(rendered + "\n")
        print(rendered)
        return 0
    started = time.monotonic()
    try:
        if args.model_file is not None:
            status, model = parse_model(args.model_file.read_text())
        else:
            proc = subprocess.run(
                [args.solver, "--sat", "--quiet", str(cnf_path)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=args.timeout,
                check=False,
            )
            status, model = parse_model(proc.stdout)
    except subprocess.TimeoutExpired:
        status, model = "UNKNOWN", set()
    finally:
        if temporary_cnf:
            cnf_path.unlink(missing_ok=True)
    report["solve_seconds"] = time.monotonic() - started
    report["status"] = status

    if status == "SAT":
        word = []
        for p, envelope in enumerate(allowed):
            if p in fixed:
                value = fixed[p]
            else:
                value = sum(
                    1 << x
                    for x in range(k)
                    if (p, x) in entry and entry[p, x] in model
                )
            if not value or value & ~envelope:
                raise AssertionError(f"invalid decoded entry {p}")
            word.append(value)
        if derive(word[:], depth) != middle:
            raise AssertionError("decoded word does not realize middle path")
        if args.fixed_append_mask:
            if not (0 < args.fixed_append_mask < (1 << k)):
                raise AssertionError("invalid --fixed-append-mask")
            word.append(args.fixed_append_mask)
        missing = full_coverage(word, k)
        report.update(
            {
                "full_missing": len(missing),
                "missing_rank_histogram": dict(Counter(x.bit_count() for x in missing)),
                "entry_rank_histogram": dict(Counter(x.bit_count() for x in word)),
                "row_rank_histograms": [
                    dict(Counter(x.bit_count() for x in derive(word[:], q)))
                    for q in range(depth + 1)
                ],
            }
        )
        if args.output_word is not None:
            args.output_word.write_text(" ".join(map(str, word)) + "\n")
            report["output_word"] = str(args.output_word)

    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.report_output is not None:
        args.report_output.write_text(rendered + "\n")
    print(rendered)
    return 0 if status == "SAT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
