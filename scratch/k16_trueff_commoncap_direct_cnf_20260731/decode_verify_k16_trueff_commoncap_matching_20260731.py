#!/usr/bin/env python3
"""Independent decoder and literal verifier for the true-FF common-cap CNF.

The checker does not trust the CNF's letter-bit variables.  It reconstructs
the selected lower matching from y variables, recomputes the maximal common
cap directly, compares it with every mapped a variable, then exhaustively
replays all 65,535 nonempty masks as interval ORs before writing a word.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path


K, R, W, H = 16, 8, 12870, 3
L = W + H
FULL = (1 << K) - 1
PIN = 0x8000
PIN_POSITION = 6389
START_HOLES = (12870, 12871, 12872)
DEADLINE_HOLES = (0, 1, 6388)
TARGET_SHA = "c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable(value: object) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def read_model(path: Path) -> tuple[str, dict[int, bool]]:
    status = "UNKNOWN"
    values: dict[int, bool] = {}
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("s "):
            status = line[2:].strip()
        if not line.startswith("v "):
            continue
        for token in line[2:].split():
            literal = int(token)
            if literal:
                values[abs(literal)] = literal > 0
    return status, values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--map", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--word", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    args = parser.parse_args()
    assert digest(args.targets) == TARGET_SHA
    targets = [int(token) for token in args.targets.read_text().split()]
    assert len(targets) == len(set(targets)) == W
    assert {target.bit_count() for target in targets} == {R}

    status, assignment = read_model(args.model)
    if "SATISFIABLE" not in status or "UNSATISFIABLE" in status:
        raise ValueError(f"model is not SAT: {status}")

    starts = [p for p in range(L) if p not in START_HOLES]
    deadlines = [p for p in range(L) if p not in DEADLINE_HOLES]
    depths = [right - left for left, right in zip(starts, deadlines)]
    assert sum(depths) == 32224 and all(0 <= depth <= H for depth in depths)
    envelope = [FULL] * L
    for target, left, right in zip(targets, starts, deadlines):
        for position in range(left, right + 1):
            envelope[position] &= target
    assert all(envelope)
    envelope[PIN_POSITION] = PIN

    specs: list[tuple[int, int, str]] = []
    lookup: dict[tuple[int, int], int] = {}
    for left, depth in zip(starts, depths):
        for length in range(1, depth + 1):
            lookup[left, length] = len(specs)
            specs.append((left, length, "selected"))
    for left in START_HOLES:
        for length in range(1, min(H, L - left) + 1):
            lookup[left, length] = len(specs)
            specs.append((left, length, "omitted"))
    assert len(specs) == 32230
    reserved = lookup[PIN_POSITION, 1]

    y_rows: dict[int, tuple[int, int, int, int]] = {}
    a_rows: dict[int, tuple[int, int]] = {}
    with args.map.open() as stream:
        header = next(stream).rstrip("\n")
        assert header == "kind\tvar\ttarget\tcell\tstart\tlength\tposition\tbit"
        for line in stream:
            kind, var, target, cell, left, length, position, bit = line.split()
            variable = int(var)
            if kind == "y":
                y_rows[variable] = (int(target), int(cell), int(left), int(length))
            elif kind == "a":
                a_rows[variable] = (int(position), int(bit))
            else:
                raise ValueError(kind)
    # 347734 marginal incidences minus target 0x8000 and every use of its
    # reserved singleton cell leaves the authenticated residual graph.
    assert len(y_rows) == 347677
    assert all(variable in assignment for variable in y_rows)
    assert all(variable in assignment for variable in a_rows)

    selected = [row for variable, row in y_rows.items() if assignment[variable]]
    assert len(selected) == 26331
    by_target = Counter(target for target, _cell, _left, _length in selected)
    by_cell = Counter(cell for _target, cell, _left, _length in selected)
    remaining = {
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < R and mask != PIN
    }
    assert set(by_target) == remaining and set(by_target.values()) == {1}
    assert max(by_cell.values()) == 1 and reserved not in by_cell

    word = envelope[:]
    for target, cell, left, length in selected:
        assert specs[cell][:2] == (left, length)
        for position in range(left, left + length):
            word[position] &= target
    assert all(word)

    # The mapped a variables must equal the independently recomputed cap.
    for variable, (position, bit) in a_rows.items():
        assert assignment[variable] == bool(word[position] & (1 << bit))

    middle_failures = []
    for row, (target, left, right) in enumerate(zip(targets, starts, deadlines)):
        value = 0
        for position in range(left, right + 1):
            value |= word[position]
        if value != target:
            middle_failures.append([row, target, value])
    assert not middle_failures

    lower_failures = []
    assert word[PIN_POSITION] == PIN
    for target, _cell, left, length in selected:
        value = 0
        for position in range(left, left + length):
            value |= word[position]
        if value != target:
            lower_failures.append([target, left, length, value])
    assert not lower_failures

    seen: set[int] = set()
    ending: set[int] = set()
    for letter in word:
        ending = {letter} | {old | letter for old in ending}
        seen.update(ending)
    missing = [mask for mask in range(1, 1 << K) if mask not in seen]
    assert not missing

    args.word.write_text(" ".join(map(str, word)) + "\n")
    core: dict[str, object] = {
        "schema": "k16.trueff.commoncap-direct-cnf.decode.v1",
        "status": "PASS_LITERAL_UNIVERSAL_WORD",
        "inputs": {
            "targets": str(args.targets),
            "targets_sha256": digest(args.targets),
            "map": str(args.map),
            "map_sha256": digest(args.map),
            "model": str(args.model),
            "model_sha256": digest(args.model),
        },
        "selected_lower_incidences": len(selected),
        "reserved_singleton": {
            "target": PIN,
            "position": PIN_POSITION,
            "cell": reserved,
        },
        "middle_failures": 0,
        "lower_failures": 0,
        "covered_nonempty_masks": len(seen),
        "missing_masks": missing,
        "word": str(args.word),
        "word_sha256": digest(args.word),
        "letter_rank_histogram": dict(sorted(Counter(
            letter.bit_count() for letter in word
        ).items())),
    }
    payload = dict(core)
    payload["payload_sha256"] = stable(core)
    args.audit.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "word": str(args.word),
        "word_sha256": payload["word_sha256"],
        "audit": str(args.audit),
        "payload_sha256": payload["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
