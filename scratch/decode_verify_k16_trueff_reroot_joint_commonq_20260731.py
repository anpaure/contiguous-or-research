#!/usr/bin/env python3
"""Fail-closed decoder/replayer for the c7be K16 common-Q compiler.

This file is intentionally independent of the SAT builder.  It can either
verify an already decoded source word or decode Q-bit variables from a strict
JSON map plus a DIMACS-style SAT model.  It then reconstructs all geometry
from the authenticated middle chronology and checks, without trusting any
selector or Hall metadata:

  * the frozen X/Y schedule and maximal envelope;
  * 12,873 nonzero source cells, each inside its envelope;
  * Q[6389] == 0x8000;
  * every scheduled middle interval OR is exactly its rank-eight target;
  * every rank-<8 target occurs in an allowed physical short cell;
  * every one of the 65,535 nonzero K16 masks occurs as an interval OR.

The map is the TSV emitted by
``build_k16_trueff_commoncap_matching_cnf_20260731.cpp`` with header
``kind var target cell start length position bit``.  ``y`` rows map lower
target/cell incidences and ``a`` rows map capped-envelope letter bits.  The
companion metadata JSON is mandatory.  The decoder independently rebuilds
the physical cell catalogue and candidate predicate, requires the TSV to be
the exact 347,677-edge residual graph and exact 70,759-bit capped envelope,
and requires every mapped variable to be explicitly assigned in the model.
An omitted variable is never silently interpreted as false.

Usage:
  decode_verify...py --word candidate.word [--out-audit audit.json]
  decode_verify...py --map model.map.tsv --meta model.meta.json --model solver.out
      [--out-word candidate.word] [--out-audit audit.json]
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word"
TARGET_SHA = "c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906"
META_SCHEMA = "k16.trueff.commoncap-direct-cnf.v1"
K, R, W, L = 16, 8, 12870, 12873
EXPECTED_VARIABLES, EXPECTED_CLAUSES = 1055230, 4513893
FULL = (1 << K) - 1
START_HOLES = (12870, 12871, 12872)
DEADLINE_HOLES = (0, 1, 6388)
PIN_POSITION = 6389
PIN_VALUE = 0x8000


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(raw).hexdigest()


def strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def canonical_word(values: Iterable[int]) -> bytes:
    return (" ".join(map(str, values)) + "\n").encode()


def load_int_word(path: Path, expected_length: int) -> list[int]:
    raw = path.read_text().split()
    if len(raw) != expected_length:
        raise ValueError(
            f"{path}: expected {expected_length} integers, found {len(raw)}"
        )
    values: list[int] = []
    for token in raw:
        # int() accepts signs; the range check below rejects nonpositive data.
        value = int(token, 10)
        if not 1 <= value <= FULL:
            raise ValueError(f"{path}: source cell outside 1..65535: {token}")
        values.append(value)
    return values


def load_targets() -> list[int]:
    if file_sha(TARGET) != TARGET_SHA:
        raise ValueError("authenticated middle chronology SHA mismatch")
    targets = load_int_word(TARGET, W)
    if len(set(targets)) != W:
        raise ValueError("middle chronology is not squarefree")
    if any(value.bit_count() != R for value in targets):
        raise ValueError("middle chronology contains a non-rank-eight mask")
    return targets


def geometry(targets: list[int]) -> tuple[
    list[int], list[int], list[int], list[int], list[tuple[int, int]]
]:
    starts = [p for p in range(L) if p not in START_HOLES]
    deadlines = [p for p in range(L) if p not in DEADLINE_HOLES]
    if len(starts) != W or len(deadlines) != W:
        raise ValueError("schedule cardinality drift")
    depths = [deadline - start for start, deadline in zip(starts, deadlines)]
    if Counter(depths) != Counter({2: 6386, 3: 6484}):
        raise ValueError("unexpected depth profile")
    if sum(depths) != 32224:
        raise ValueError("unexpected selected area")

    envelope = [FULL] * L
    for target, start, deadline in zip(targets, starts, deadlines):
        if not 0 <= start <= deadline < L or deadline - start > 3:
            raise ValueError("invalid middle schedule interval")
        for p in range(start, deadline + 1):
            envelope[p] &= target
    if any(value == 0 for value in envelope):
        raise ValueError("maximal envelope has an empty source cell")
    for row, (target, start, deadline) in enumerate(
        zip(targets, starts, deadlines)
    ):
        joined = 0
        for p in range(start, deadline + 1):
            joined |= envelope[p]
        if joined != target:
            raise ValueError(f"maximal envelope fails middle row {row}")
    if envelope[PIN_POSITION] != 0xC304:
        raise ValueError("unexpected pre-pin envelope at position 6389")
    if PIN_VALUE & ~envelope[PIN_POSITION]:
        raise ValueError("pin lies outside the maximal envelope")

    # All proper prefixes of selected rows, plus only physically present
    # length-at-most-three intervals at omitted tail starts.
    specs: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for start, depth in zip(starts, depths):
        for length in range(1, depth + 1):
            spec = (start, length)
            if spec in seen:
                raise ValueError("duplicate selected short cell")
            seen.add(spec)
            specs.append(spec)
    for start in START_HOLES:
        for length in range(1, min(3, L - start) + 1):
            spec = (start, length)
            if spec in seen:
                raise ValueError("omitted-start cell collides")
            seen.add(spec)
            specs.append(spec)
    if len(specs) != 32230:
        raise ValueError("physical short-cell count != 32230")
    if specs.count((PIN_POSITION, 1)) != 1:
        raise ValueError("pinned singleton is not a unique physical cell")
    return starts, deadlines, depths, envelope, specs


def parse_dimacs_model(path: Path, maximum_variable: int) -> dict[int, bool]:
    status: str | None = None
    assignment: dict[int, bool] = {}
    saw_model_line = False
    for raw_line in path.read_text(errors="strict").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("c"):
            continue
        fields = line.split()
        if fields[0] == "s":
            if len(fields) < 2:
                raise ValueError("malformed SAT status line")
            new_status = fields[1].upper()
            if status is not None and status != new_status:
                raise ValueError("conflicting SAT status lines")
            status = new_status
            continue
        if fields[0].upper() in {"SAT", "SATISFIABLE"}:
            status = "SATISFIABLE"
            continue
        if fields[0].upper() in {"UNSAT", "UNSATISFIABLE", "UNKNOWN"}:
            status = fields[0].upper()
            continue
        if fields[0] == "v":
            fields = fields[1:]
            saw_model_line = True
        elif all(field.lstrip("+-").isdigit() for field in fields):
            # Accept a plain DIMACS assignment line, but still require an
            # independent SAT status somewhere in the file.
            saw_model_line = True
        else:
            continue
        for field in fields:
            literal = int(field)
            if literal == 0:
                continue
            var = abs(literal)
            if not 1 <= var <= maximum_variable:
                raise ValueError(f"model variable {var} exceeds declared range")
            value = literal > 0
            old = assignment.get(var)
            if old is not None and old != value:
                raise ValueError(f"contradictory model literals for var {var}")
            assignment[var] = value
    if status not in {"SAT", "SATISFIABLE"}:
        raise ValueError(f"solver output is not positively SAT: {status!r}")
    if not saw_model_line or not assignment:
        raise ValueError("SAT output contains no model assignment")
    return assignment


def validate_dimacs_header(path: Path) -> None:
    with path.open() as stream:
        for raw in stream:
            line = raw.strip()
            if not line or line.startswith("c"):
                continue
            fields = line.split()
            if fields != ["p", "cnf", str(EXPECTED_VARIABLES), str(EXPECTED_CLAUSES)]:
                raise ValueError(f"unexpected DIMACS header: {line!r}")
            return
    raise ValueError("DIMACS file has no header")


def expected_candidates(
    targets: list[int], starts: list[int], deadlines: list[int],
    envelope: list[int], specs: list[tuple[int, int]],
) -> tuple[int, list[int], list[int]]:
    """Return exact residual edge count and per-cell allowed/mandatory masks."""
    lookup = {spec: cell for cell, spec in enumerate(specs)}
    mandatory = [0] * len(specs)
    for target, row_start, deadline in zip(targets, starts, deadlines):
        for bit in range(K):
            flag = 1 << bit
            if not target & flag:
                continue
            hosts = [
                p for p in range(row_start, deadline + 1)
                if envelope[p] & flag
            ]
            if not hosts:
                raise ValueError("capped envelope loses a middle bit")
            lo, hi = min(hosts), max(hosts)
            for length in range(1, 4):
                for start in range(max(0, hi - length + 1), lo + 1):
                    cell = lookup.get((start, length))
                    if cell is not None:
                        mandatory[cell] |= flag
    allowed = [
        interval_or(envelope, start, length) for start, length in specs
    ]
    reserved = lookup[PIN_POSITION, 1]
    count = 0
    for cell, (start, length) in enumerate(specs):
        if cell == reserved:
            continue
        subset = allowed[cell]
        while subset:
            if (
                subset != PIN_VALUE
                and subset.bit_count() < R
                and not mandatory[cell] & ~subset
                and all(envelope[p] & subset for p in range(start, start + length))
            ):
                count += 1
            subset = (subset - 1) & allowed[cell]
    return count, allowed, mandatory


def valid_candidate(
    target: int, cell: int, specs: list[tuple[int, int]], envelope: list[int],
    allowed: list[int], mandatory: list[int], reserved: int,
) -> bool:
    if cell == reserved or target == PIN_VALUE or not 1 <= target <= FULL:
        return False
    if target.bit_count() >= R or target & ~allowed[cell]:
        return False
    if mandatory[cell] & ~target:
        return False
    start, length = specs[cell]
    return all(envelope[p] & target for p in range(start, start + length))


def decode_q(
    map_path: Path, meta_path: Path, model_path: Path,
    targets: list[int], starts: list[int], deadlines: list[int],
    envelope_uncapped: list[int], specs: list[tuple[int, int]],
) -> list[int]:
    meta = json.loads(meta_path.read_text(), object_pairs_hook=strict_object)
    exact_meta = {
        "schema": META_SCHEMA,
        "target_sha256": TARGET_SHA,
        "variables": EXPECTED_VARIABLES,
        "clauses": EXPECTED_CLAUSES,
        "incidence_variables": 347677,
        "letter_bit_variables": 70759,
        "remaining_lower_targets": 26331,
        "physical_cells": 32230,
        "reserved_singleton": {"target": PIN_VALUE, "position": PIN_POSITION, "cell": 12781},
        "start_holes": list(START_HOLES),
        "deadline_holes": list(DEADLINE_HOLES),
        "selected_area": 32224,
    }
    for key, value in exact_meta.items():
        if meta.get(key) != value:
            raise ValueError(f"metadata mismatch at {key}: {meta.get(key)!r}")

    envelope = envelope_uncapped[:]
    envelope[PIN_POSITION] = PIN_VALUE
    reserved = specs.index((PIN_POSITION, 1))
    if reserved != 12781:
        raise ValueError("reserved cell index drift")
    expected_edge_count, allowed, mandatory = expected_candidates(
        targets, starts, deadlines, envelope, specs
    )
    if expected_edge_count != 347677:
        raise ValueError("independent residual incidence count drift")

    y_rows: dict[int, tuple[int, int, int, int]] = {}
    a_rows: dict[int, tuple[int, int]] = {}
    y_pairs: set[tuple[int, int]] = set()
    a_pairs: set[tuple[int, int]] = set()
    all_vars: set[int] = set()
    with map_path.open() as stream:
        header = stream.readline().rstrip("\n")
        if header != "kind\tvar\ttarget\tcell\tstart\tlength\tposition\tbit":
            raise ValueError("unexpected TSV map header")
        for line_number, raw in enumerate(stream, 2):
            fields = raw.rstrip("\n").split("\t")
            if len(fields) != 8:
                raise ValueError(f"map line {line_number}: expected 8 fields")
            kind = fields[0]
            values = [int(field) for field in fields[1:]]
            variable, target, cell, start, length, position, bit = values
            if not 1 <= variable <= meta["variables"] or variable in all_vars:
                raise ValueError(f"map line {line_number}: invalid/reused variable")
            all_vars.add(variable)
            if kind == "y":
                if position != -1 or bit != -1:
                    raise ValueError("y row has non-placeholder position/bit")
                if not 0 <= cell < len(specs) or specs[cell] != (start, length):
                    raise ValueError("y row cell geometry mismatch")
                if not valid_candidate(
                    target, cell, specs, envelope, allowed, mandatory, reserved
                ):
                    raise ValueError("map contains an invalid lower incidence")
                if (target, cell) in y_pairs:
                    raise ValueError("duplicate target/cell incidence")
                y_pairs.add((target, cell))
                y_rows[variable] = (target, cell, start, length)
            elif kind == "a":
                if (target, cell, start, length) != (-1, -1, -1, -1):
                    raise ValueError("a row has non-placeholder target geometry")
                pair = (position, bit)
                if not (0 <= position < L and 0 <= bit < K):
                    raise ValueError("a row position/bit out of range")
                if not envelope[position] & (1 << bit):
                    raise ValueError("a row lies outside the capped envelope")
                if pair in a_pairs:
                    raise ValueError("duplicate a position/bit")
                a_pairs.add(pair)
                a_rows[variable] = pair
            else:
                raise ValueError(f"unknown map kind {kind!r}")
    if len(y_rows) != expected_edge_count or len(y_pairs) != expected_edge_count:
        raise ValueError("TSV does not contain the complete residual graph")
    if set(y_rows) != set(range(1, 347678)):
        raise ValueError("incidence variable range is not canonical")
    expected_a_pairs = {
        (p, bit) for p, mask in enumerate(envelope) for bit in range(K)
        if mask & (1 << bit)
    }
    if a_pairs != expected_a_pairs or len(a_rows) != 70759:
        raise ValueError("TSV letter-bit map is incomplete")
    if set(a_rows) != set(range(347678, 418437)):
        raise ValueError("letter-bit variable range is not canonical")

    assignment = parse_dimacs_model(model_path, meta["variables"])
    absent = sorted(var for var in all_vars if var not in assignment)
    if absent:
        raise ValueError(
            f"model omits {len(absent)} mapped y/a variables; first={absent[:10]}"
        )
    selected = [row for var, row in y_rows.items() if assignment[var]]
    if len(selected) != 26331:
        raise ValueError(f"selected incidence count {len(selected)} != 26331")
    by_target = Counter(row[0] for row in selected)
    by_cell = Counter(row[1] for row in selected)
    remaining = {
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < R and mask != PIN_VALUE
    }
    if set(by_target) != remaining or set(by_target.values()) != {1}:
        raise ValueError("selected y rows are not exactly one per lower target")
    if by_cell and max(by_cell.values()) > 1:
        raise ValueError("selected y rows reuse a physical cell")
    if reserved in by_cell:
        raise ValueError("selected y row consumes reserved singleton cell")

    # Recompute the maximal common cap from selected incidences; do not trust
    # the model's letter variables or the builder's blocker catalogue.
    word = envelope[:]
    for target, _cell, start, length in selected:
        for p in range(start, start + length):
            word[p] &= target
    if any(value == 0 for value in word):
        raise ValueError("selected incidences empty a source cell")
    if word[PIN_POSITION] != PIN_VALUE:
        raise ValueError("selected incidences corrupt the reserved pin")
    a_by_pair = {pair: var for var, pair in a_rows.items()}
    disagreement = [
        [p, bit, assignment[a_by_pair[p, bit]], bool(word[p] & (1 << bit))]
        for p, bit in sorted(a_pairs)
        if assignment[a_by_pair[p, bit]] != bool(word[p] & (1 << bit))
    ]
    if disagreement:
        raise ValueError(f"mapped a variables disagree with common cap: {disagreement[:10]}")
    return word


def interval_or(values: list[int], start: int, length: int) -> int:
    joined = 0
    for p in range(start, start + length):
        joined |= values[p]
    return joined


def all_interval_coverage(values: list[int]) -> bytearray:
    """Enumerate every distinct interval OR in O(K*L log K) events."""
    n = len(values)
    next_position = [[n] * K for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        next_position[i] = next_position[i + 1].copy()
        for bit in range(K):
            if values[i] & (1 << bit):
                next_position[i][bit] = i
    covered = bytearray(1 << K)
    for i, first in enumerate(values):
        joined = first
        covered[joined] = 1
        events = sorted(
            (next_position[i + 1][bit], bit)
            for bit in range(K)
            if not (first & (1 << bit)) and next_position[i + 1][bit] < n
        )
        cursor = 0
        while cursor < len(events):
            p = events[cursor][0]
            while cursor < len(events) and events[cursor][0] == p:
                joined |= 1 << events[cursor][1]
                cursor += 1
            covered[joined] = 1
    return covered


def verify_word(values: list[int], targets: list[int]) -> dict[str, object]:
    starts, deadlines, depths, envelope, specs = geometry(targets)
    if len(values) != L:
        raise ValueError("decoded source length != 12873")
    if any(not 1 <= value <= FULL for value in values):
        raise ValueError("decoded source contains zero/out-of-range cell")
    outside = [
        [p, values[p], envelope[p]]
        for p in range(L)
        if values[p] & ~envelope[p]
    ]
    if outside:
        raise ValueError(f"decoded source exceeds envelope: {outside[:10]}")
    if values[PIN_POSITION] != PIN_VALUE:
        raise ValueError(
            f"pin mismatch: Q[6389]={values[PIN_POSITION]:#06x}"
        )

    middle_failures = []
    for row, (target, start, deadline) in enumerate(
        zip(targets, starts, deadlines)
    ):
        joined = interval_or(values, start, deadline - start + 1)
        if joined != target:
            middle_failures.append([row, target, joined, start, deadline])
            if len(middle_failures) >= 10:
                break
    if middle_failures:
        raise ValueError(f"middle replay failures: {middle_failures}")

    short_seen = bytearray(1 << K)
    first_short_witness: dict[int, tuple[int, int]] = {}
    for start, length in specs:
        joined = interval_or(values, start, length)
        short_seen[joined] = 1
        first_short_witness.setdefault(joined, (start, length))
    lower_missing = [
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < R and not short_seen[mask]
    ]
    if lower_missing:
        raise ValueError(
            f"short lower replay misses {len(lower_missing)} targets; "
            f"first={[hex(x) for x in lower_missing[:10]]}"
        )

    covered = all_interval_coverage(values)
    missing = [mask for mask in range(1, 1 << K) if not covered[mask]]
    if missing:
        raise ValueError(
            f"literal universal replay misses {len(missing)} masks; "
            f"first={[hex(x) for x in missing[:10]]}"
        )

    return {
        "schema": "k16-trueff-reroot-joint-commonq-decoder-audit-v1",
        "status": "PASS_LITERAL_UNIVERSAL_WORD",
        "target": str(TARGET.relative_to(ROOT)),
        "target_sha256": TARGET_SHA,
        "schedule": {
            "start_holes": list(START_HOLES),
            "deadline_holes": list(DEADLINE_HOLES),
            "selected_area": sum(depths),
            "physical_short_cells": len(specs),
        },
        "pin": {
            "position": PIN_POSITION,
            "value": PIN_VALUE,
            "value_hex": f"0x{PIN_VALUE:04x}",
        },
        "source": {
            "length": len(values),
            "sha256": sha256(canonical_word(values)).hexdigest(),
            "rank_histogram": {
                str(rank): count for rank, count in sorted(
                    Counter(value.bit_count() for value in values).items()
                )
            },
            "zero_cells": 0,
            "outside_envelope": 0,
        },
        "replay": {
            "middle_rows_exact": W,
            "short_lower_targets_covered": 26332,
            "all_nonzero_masks_covered": 65535,
            "missing": [],
        },
        "scope": [
            "Positive witness audit only; an UNSAT/UNKNOWN solver result proves nothing here.",
            "No Hall matching or selector metadata is trusted for final acceptance.",
            "All 65,535 masks are independently replayed from the decoded source word.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--word", type=Path)
    mode.add_argument("--map", type=Path)
    parser.add_argument("--model", type=Path)
    parser.add_argument("--meta", type=Path)
    parser.add_argument("--cnf", type=Path)
    parser.add_argument("--out-word", type=Path)
    parser.add_argument("--out-audit", type=Path)
    args = parser.parse_args()

    targets = load_targets()
    if args.word is not None:
        if args.model is not None or args.meta is not None or args.cnf is not None:
            parser.error("--model/--meta/--cnf are invalid with --word")
        values = load_int_word(args.word, L)
    else:
        if args.model is None or args.meta is None or args.cnf is None:
            parser.error("--map requires --model, --meta, and --cnf")
        validate_dimacs_header(args.cnf)
        starts, deadlines, _depths, envelope, specs = geometry(targets)
        values = decode_q(
            args.map, args.meta, args.model, targets, starts, deadlines,
            envelope, specs,
        )

    audit = verify_word(values, targets)
    audit["checker_sha256"] = file_sha(Path(__file__))
    if args.map is not None:
        audit["artifacts"] = {
            "cnf": {"path": str(args.cnf), "sha256": file_sha(args.cnf)},
            "map": {"path": str(args.map), "sha256": file_sha(args.map)},
            "meta": {"path": str(args.meta), "sha256": file_sha(args.meta)},
            "model": {"path": str(args.model), "sha256": file_sha(args.model)},
        }
    core = dict(audit)
    audit["payload_sha256"] = stable(core)

    if args.out_word is not None:
        if args.out_word.exists():
            raise FileExistsError(f"refusing to overwrite {args.out_word}")
        args.out_word.write_bytes(canonical_word(values))
        if file_sha(args.out_word) != audit["source"]["sha256"]:
            raise AssertionError("written word hash mismatch")
    if args.out_audit is not None:
        if args.out_audit.exists():
            raise FileExistsError(f"refusing to overwrite {args.out_audit}")
        args.out_audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": audit["status"],
        "word_sha256": audit["source"]["sha256"],
        "payload_sha256": audit["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
