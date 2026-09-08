#!/usr/bin/env python3
"""Stress-test exact type/state schedules under prescribed unmarked masks.

Substantive execution is intended for H100 only.  This is a search/audit
tool: it probes structured and random mask families having exactly 286
unmarked positions on each mixed face.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import sys
from pathlib import Path

from ortools.sat.python import cp_model


CORE = frozenset(range(5))
TYPES = (
    (1, 5, 2, 1), (1, 6, 1, 1), (2, 5, 1, 1),
    (3, 3, 2, 1), (3, 4, 1, 1), (4, 3, 1, 1),
    (5, 1, 2, 1), (5, 2, 1, 1), (6, 1, 1, 1),
)
TYPE_COUNTS = (139, 297, 8, 20, 20, 140, 127, 237, 442)
UNMARKED = frozenset((0, 3, 6))


def partitions(sizes):
    for middle in itertools.combinations(CORE, sizes[1]):
        middle = frozenset(middle)
        rest = CORE - middle
        for old in itertools.combinations(rest, sizes[2]):
            old = frozenset(old)
            yield CORE - middle - old, middle, old


def catalogue():
    states = []
    for type_id, kind in enumerate(TYPES):
        for parts in partitions(tuple(x - 1 for x in kind[:3])):
            states.append((type_id, parts))
    arcs = [(i, j) for i, (_, old) in enumerate(states)
            for j, (_, new) in enumerate(states)
            if new[1] <= old[0] and new[2] <= old[1]]
    return states, arcs


def make_masks(t, mode, seed):
    lengths = [10] * (143 - 11 * t) + [11] * (10 * t)
    total = sum(lengths)
    assert total == 1430
    bits = [0] * total
    if mode == "isolated3":
        masks = []
        extras = 2 * t
        for cycle_id, length in enumerate(lengths):
            word = [0] * length
            word[0] = word[3] = 1
            if cycle_id < extras:
                word[6] = 1
            masks.append(tuple(word))
        assert sum(map(sum, masks)) == 286
        return masks
    if mode == "packed":
        for i in range(286):
            bits[i] = 1
    elif mode == "suffix_packed":
        for i in range(total - 286, total):
            bits[i] = 1
    elif mode == "round_robin":
        positions = []
        offset = 0
        for phase in range(11):
            for length in lengths:
                if phase < length:
                    positions.append(offset + phase)
                offset += length
            offset = 0
        for i in positions[:286]:
            bits[i] = 1
    elif mode.startswith("periodic"):
        stride = int(mode.removeprefix("periodic"))
        order = sorted(range(total), key=lambda i: (i % stride, i))
        for i in order[:286]:
            bits[i] = 1
    elif mode == "random":
        rng = random.Random(seed)
        for i in rng.sample(range(total), 286):
            bits[i] = 1
    else:
        raise ValueError(mode)
    masks = []
    offset = 0
    for length in lengths:
        masks.append(tuple(bits[offset:offset + length]))
        offset += length
    assert sum(map(sum, masks)) == 286
    return masks


def solve(masks, time_limit, workers, seed, emit_words=False):
    states, arcs = catalogue()
    model = cp_model.CpModel()
    rows = []
    flat = []
    for cycle_id, mask in enumerate(masks):
        row = []
        for position, bit in enumerate(mask):
            domain = [i for i, (type_id, _) in enumerate(states)
                      if int(type_id in UNMARKED) == bit]
            variable = model.new_int_var_from_domain(
                cp_model.Domain.from_values(domain), f"s_{cycle_id}_{position}")
            row.append(variable)
            flat.append(variable)
        for i in range(len(row)):
            model.add_allowed_assignments([row[i], row[(i + 1) % len(row)]], arcs)
        rows.append(row)
    type_pairs = [(state_id, type_id) for state_id, (type_id, _) in enumerate(states)]
    type_variables = []
    for i, state in enumerate(flat):
        type_var = model.new_int_var(0, 8, f"type_{i}")
        model.add_allowed_assignments([state, type_var], type_pairs)
        type_variables.append(type_var)
    for type_id, demand in enumerate(TYPE_COUNTS):
        flags = []
        for i, variable in enumerate(type_variables):
            flag = model.new_bool_var(f"is_{i}_{type_id}")
            model.add(variable == type_id).only_enforce_if(flag)
            model.add(variable != type_id).only_enforce_if(flag.Not())
            flags.append(flag)
        model.add(sum(flags) == demand)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    status = solver.solve(model)
    result = {
        "status": solver.status_name(status),
        "wall_time": solver.wall_time,
        "conflicts": solver.num_conflicts,
        "branches": solver.num_branches,
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        state_words = [[solver.value(v) for v in row] for row in rows]
        result["type_counts"] = [
            sum(int(solver.value(v) == type_id) for v in type_variables)
            for type_id in range(9)
        ]
        result["state_words_sha256"] = hashlib.sha256(json.dumps(
            state_words, separators=(",", ":")
        ).encode()).hexdigest()
        if emit_words:
            result["state_words"] = state_words
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--faces", default="0,6,13")
    parser.add_argument("--modes", default="packed,round_robin,periodic2,periodic3,random")
    parser.add_argument("--random-trials", type=int, default=3)
    parser.add_argument("--time-limit", type=float, default=120.0)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--emit-words", action="store_true")
    parser.add_argument("--certificate")
    args = parser.parse_args()
    source = Path(sys.argv[0]).read_bytes()
    reports = []
    for t in map(int, args.faces.split(",")):
        for mode in args.modes.split(","):
            trials = args.random_trials if mode == "random" else 1
            for trial in range(trials):
                seed = 20260814 + 100 * t + trial
                masks = make_masks(t, mode, seed)
                report = solve(masks, args.time_limit, args.workers, seed, args.emit_words)
                report.update({
                    "t": t, "mode": mode, "trial": trial,
                    "cycles": len(masks),
                    "mask_multiset_sha256": hashlib.sha256(json.dumps(
                        sorted("".join(map(str, mask)) for mask in masks),
                               separators=(",", ":")
                    ).encode()).hexdigest(),
                })
                reports.append(report)
                print(json.dumps(report), flush=True)
    summary = {
        "summary": "PASS" if all(r["status"] in ("OPTIMAL", "FEASIBLE") for r in reports)
        else "INCOMPLETE",
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "reports": reports,
    }
    if args.certificate:
        Path(args.certificate).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
