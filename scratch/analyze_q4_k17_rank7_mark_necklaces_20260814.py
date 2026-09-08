#!/usr/bin/env python3
"""Enumerate binary marked/unmarked necklaces in the exact q4 five-core automaton.

Substantive execution is intended for H100 only.  A bit is 1 exactly for an
unmarked state (type IDs 0, 3, 6, equivalently k_2=1).  The script checks
literal labelled-state lifts, not merely the nine-type quotient.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


CORE = frozenset(range(5))
TYPES = (
    (1, 5, 2, 1),
    (1, 6, 1, 1),
    (2, 5, 1, 1),
    (3, 3, 2, 1),
    (3, 4, 1, 1),
    (4, 3, 1, 1),
    (5, 1, 2, 1),
    (5, 2, 1, 1),
    (6, 1, 1, 1),
)
UNMARKED_TYPES = frozenset((0, 3, 6))


def partitions(sizes):
    values = tuple(CORE)
    for middle in itertools.combinations(values, sizes[1]):
        middle = frozenset(middle)
        remaining = tuple(x for x in values if x not in middle)
        for old in itertools.combinations(remaining, sizes[2]):
            old = frozenset(old)
            fresh = CORE - middle - old
            yield fresh, middle, old


def catalogue():
    states = []
    for type_id, kind in enumerate(TYPES):
        sizes = tuple(value - 1 for value in kind[:3])
        for parts in partitions(sizes):
            states.append((type_id, parts))
    assert len(states) == 72
    successors = []
    for _, old in states:
        successors.append(tuple(
            j for j, (_, new) in enumerate(states)
            if new[1] <= old[0] and new[2] <= old[1]
        ))
    return states, successors


def canonical_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def canonical_dihedral(word):
    reverse = tuple(reversed(word))
    return min(canonical_rotation(word), canonical_rotation(reverse))


def witness(word, states, successors):
    allowed = [
        tuple(i for i, (type_id, _) in enumerate(states)
              if int(type_id in UNMARKED_TYPES) == bit)
        for bit in word
    ]
    for start in allowed[0]:
        paths = {start: (start,)}
        for position in range(1, len(word)):
            next_paths = {}
            target = set(allowed[position])
            for tail, path in paths.items():
                for nxt in successors[tail]:
                    if nxt in target and nxt not in next_paths:
                        next_paths[nxt] = path + (nxt,)
            paths = next_paths
            if not paths:
                break
        for tail, path in paths.items():
            if start in successors[tail]:
                return path
    return None


def cyclic_runs(word, bit):
    n = len(word)
    if all(value == bit for value in word):
        return (n,)
    start = next(i for i, value in enumerate(word) if value != bit)
    runs = []
    current = 0
    for step in range(1, n + 1):
        value = word[(start + step) % n]
        if value == bit:
            current += 1
        elif current:
            runs.append(current)
            current = 0
    return tuple(runs)


def main():
    source = Path(sys.argv[0]).read_bytes()
    states, successors = catalogue()
    type_arcs = sorted({(states[i][0], states[j][0])
                        for i, row in enumerate(successors) for j in row})
    unmarked_type_arcs = [arc for arc in type_arcs
                          if arc[0] in UNMARKED_TYPES and arc[1] in UNMARKED_TYPES]
    assert unmarked_type_arcs == [(0, 6), (3, 3), (3, 6)]
    universal_pairs = []
    for marked, (marked_type, marked_parts) in enumerate(states):
        if marked_type in UNMARKED_TYPES:
            continue
        for unmarked, (unmarked_type, unmarked_parts) in enumerate(states):
            if unmarked_type not in UNMARKED_TYPES:
                continue
            if all(right in successors[left] for left, right in (
                (marked, marked), (marked, unmarked),
                (unmarked, marked), (unmarked, unmarked),
            )):
                universal_pairs.append({
                    "marked_state": marked,
                    "marked_type": marked_type,
                    "marked_parts": [sorted(part) for part in marked_parts],
                    "unmarked_state": unmarked,
                    "unmarked_type": unmarked_type,
                    "unmarked_parts": [sorted(part) for part in unmarked_parts],
                })
    reports = []
    all_witnesses = {}
    for n in (10, 11):
        feasible = []
        infeasible = []
        by_weight = defaultdict(lambda: Counter(feasible=0, infeasible=0))
        for word in itertools.product((0, 1), repeat=n):
            path = witness(word, states, successors)
            key = "".join(map(str, word))
            bucket = by_weight[sum(word)]
            if path is None:
                infeasible.append(key)
                bucket["infeasible"] += 1
            else:
                feasible.append(key)
                bucket["feasible"] += 1
                all_witnesses[f"{n}:{key}"] = path
        infeasible_necklaces = sorted({
            "".join(map(str, canonical_rotation(tuple(map(int, word)))))
            for word in infeasible
        })
        feasible_necklaces = sorted({
            "".join(map(str, canonical_rotation(tuple(map(int, word)))))
            for word in feasible
        })
        reports.append({
            "period": n,
            "feasible_words": len(feasible),
            "infeasible_words": len(infeasible),
            "feasible_necklaces": len(feasible_necklaces),
            "infeasible_necklaces": len(infeasible_necklaces),
            "by_unmarked_count": {str(k): dict(by_weight[k]) for k in sorted(by_weight)},
            "infeasible_necklace_words": infeasible_necklaces,
            "infeasible_necklace_run_signatures": dict(Counter(
                str(cyclic_runs(tuple(map(int, word)), 1))
                for word in infeasible_necklaces
            )),
        })
    print(json.dumps({
        "status": "PASS",
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "states": len(states),
        "arcs": sum(map(len, successors)),
        "type_arcs": type_arcs,
        "unmarked_to_unmarked_type_arcs": unmarked_type_arcs,
        "universal_two_state_pairs": universal_pairs,
        "bit_convention": "1=unmarked=k2=1=type IDs 0,3,6; 0=marked=k2=0",
        "reports": reports,
        "witnesses_sha256": hashlib.sha256(json.dumps(
            all_witnesses, sort_keys=True, separators=(",", ":")
        ).encode()).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
