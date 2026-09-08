#!/usr/bin/env python3
"""Extract exact whole-rail polarity UNSAT cores for the q4/k17 states.

Run on H100 only.  A variable is true when its closed rail is lifted through
upper unions and false for the physical lower-intersection lift.  Every
same-resource collision gives one binary clause.  Lower collisions require
at least one incident rail to be upper; upper collisions require at least
one to be lower.  q1 and q2 clauses are retained with occurrence provenance.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_q4_k17_recoupled_typed_rail_ledgers_20260814 as base  # noqa:E402


def clauses_for(rails, banks):
    names = [name for name, _ in rails]
    index = {name: i for i, name in enumerate(names)}
    clauses = []
    seen = set()
    for bank in ("lower_q1", "lower_q2", "upper_q1", "upper_q2"):
        providers = defaultdict(list)
        for resource, rail, occurrence in banks[bank]:
            providers[resource].append((rail, occurrence))
        wants_upper = bank.startswith("lower")
        for resource, where in providers.items():
            if len(where) < 2:
                continue
            for left, right in itertools.combinations(where, 2):
                a, b = index[left[0]], index[right[0]]
                if a == b:
                    literals = ((a, wants_upper),)
                else:
                    literals = tuple(sorted(((a, wants_upper), (b, wants_upper))))
                key = (literals, bank, resource, left, right)
                if key in seen:
                    continue
                seen.add(key)
                clauses.append({
                    "literals": literals,
                    "bank": bank,
                    "resource": resource,
                    "providers": (left, right),
                })
    return names, clauses


def satisfiable(names, clauses):
    n = len(names)
    graph = [[] for _ in range(2 * n)]

    def node(variable, value):
        return 2 * variable + int(value)

    for clause in clauses:
        literals = clause["literals"]
        if len(literals) == 1:
            a = literals[0]
            graph[node(a[0], not a[1])].append(node(a[0], a[1]))
            continue
        a, b = literals
        graph[node(a[0], not a[1])].append(node(b[0], b[1]))
        graph[node(b[0], not b[1])].append(node(a[0], a[1]))

    index_counter = 0
    stack = []
    on_stack = set()
    indices = [-1] * (2 * n)
    low = [0] * (2 * n)
    component = [-1] * (2 * n)
    component_counter = 0

    def visit(v):
        nonlocal index_counter, component_counter
        indices[v] = low[v] = index_counter
        index_counter += 1
        stack.append(v)
        on_stack.add(v)
        for w in graph[v]:
            if indices[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component[w] = component_counter
                if w == v:
                    break
            component_counter += 1

    for v in range(2 * n):
        if indices[v] < 0:
            visit(v)
    return all(component[node(v, False)] != component[node(v, True)] for v in range(n))


def smallest_cores(names, clauses, max_cores=100):
    assert not satisfiable(names, clauses)
    # First obtain a small inclusion-minimal upper bound.
    core = list(clauses)
    changed = True
    while changed:
        changed = False
        for clause in tuple(core):
            trial = [item for item in core if item is not clause]
            if not satisfiable(names, trial):
                core = trial
                changed = True
    upper = len(core)
    answers = []
    for size in range(1, upper + 1):
        for indices in itertools.combinations(range(len(clauses)), size):
            trial = [clauses[i] for i in indices]
            if not satisfiable(names, trial):
                answers.append(trial)
                if len(answers) >= max_cores:
                    return size, answers, upper
        if answers:
            return size, answers, upper
    raise AssertionError("UNSAT core not found")


def active_collision_score(names, by_rail, bits):
    scores = {}
    for bank in ("lower_q1", "upper_q1", "lower_q2", "upper_q2"):
        values = []
        wants_upper = bank.startswith("upper")
        for name, upper in zip(names, bits):
            if upper == wants_upper:
                values.extend(by_rail[name][bank])
        scores[bank] = len(values) - len(set(values))
    return scores


def encode_set(value):
    return "".join("1" if i in value else "0" for i in range(17))


def encode_clause(clause, names):
    return {
        "bank": clause["bank"],
        "resource": encode_set(clause["resource"]),
        "providers": [[rail, occurrence] for rail, occurrence in clause["providers"]],
        "clause": [
            {"rail": names[variable], "must_be": "upper" if value else "lower"}
            for variable, value in clause["literals"]
        ],
    }


def main():
    source_path = Path(sys.argv[1])
    source_raw = source_path.read_bytes()
    reports = []
    for state_name, rails in base.rail_states():
        by_rail, banks = base.occurrences(rails)
        names, clauses = clauses_for(rails, banks)
        size, cores, deletion_upper = smallest_cores(names, clauses)
        best_score = None
        best = []
        for bits in itertools.product((False, True), repeat=len(names)):
            scores = active_collision_score(names, by_rail, bits)
            total = sum(scores.values())
            if best_score is None or total < best_score:
                best_score = total
                best = [(bits, scores)]
            elif total == best_score:
                best.append((bits, scores))
        reports.append({
            "state": state_name,
            "rails": names,
            "clauses": len(clauses),
            "clause_bank_histogram": dict(Counter(clause["bank"] for clause in clauses)),
            "smallest_unsat_core_size": size,
            "smallest_unsat_cores_returned": len(cores),
            "deletion_minimal_upper_bound": deletion_upper,
            "cores": [[encode_clause(clause, names) for clause in core] for core in cores],
            "minimum_active_collision_excess": best_score,
            "minimum_assignments": len(best),
            "first_minimum_assignment": {
                "lower_rails": [name for name, bit in zip(names, best[0][0]) if not bit],
                "upper_rails": [name for name, bit in zip(names, best[0][0]) if bit],
                "collision_excess": best[0][1],
            },
        })
    print(json.dumps({
        "status": "PASS",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
