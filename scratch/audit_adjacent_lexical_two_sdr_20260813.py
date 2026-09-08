#!/usr/bin/env python3
"""SAT audit for variable adjacent lexical diamonds (run substantial cases remotely)."""

import argparse
import itertools
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        yield sum(1 << i for i in cc)


def lexical_down(word, n, index):
    height, ones = 0, []
    for i in range(n):
        if (word >> i) & 1:
            ones.append((height, i))
            height += 1
        else:
            height -= 1
    ones.sort(key=lambda item: (-item[0], item[1]))
    return word ^ (1 << ones[index][1])


def options(r):
    n = 2 * r - 1
    result = []
    for upper_id, upper in enumerate(masks(n, r + 1)):
        facets = [lexical_down(upper, n, p) for p in range(r + 1)]
        for p in range(r):
            tail, head = facets[p], facets[p + 1]
            result.append((upper_id, p, tail & head, tail, head))
    return result


def directed_cycles(chosen, opts):
    successor, edge_at = {}, {}
    for oi in chosen:
        tail, head = opts[oi][3:]
        assert tail not in successor
        successor[tail], edge_at[tail] = head, oi
    cycles, done = [], set()
    for start in successor:
        if start in done:
            continue
        position, walk, vertex = {}, [], start
        while vertex in successor and vertex not in done:
            if vertex in position:
                cycles.append([edge_at[x] for x in walk[position[vertex]:]])
                break
            position[vertex] = len(walk)
            walk.append(vertex)
            vertex = successor[vertex]
        done.update(walk)
    return cycles


def solve(r, acyclic):
    opts = options(r)
    shores = [defaultdict(list) for _ in range(4)]
    for oi, option in enumerate(opts):
        variable = oi + 1
        for shore, value in zip(shores, (option[0], option[2], option[3], option[4])):
            shore[value].append(variable)
    clauses = []
    for variables in shores[0].values():
        clauses.append(variables)
        clauses.extend([-a, -b] for a, b in itertools.combinations(variables, 2))
    for shore in shores[1:]:
        for variables in shore.values():
            clauses.extend([-a, -b] for a, b in itertools.combinations(variables, 2))
    for round_id in range(100):
        with tempfile.TemporaryDirectory(prefix="adjacent_lexical_") as td:
            formula = Path(td) / "x.cnf"
            formula.write_text(
                f"p cnf {len(opts)} {len(clauses)}\n"
                + "".join(" ".join(map(str, clause)) + " 0\n" for clause in clauses)
            )
            run = subprocess.run(["kissat", str(formula)], capture_output=True,
                                 text=True, check=False)
        if run.returncode == 20:
            return None, opts, round_id, len(clauses)
        if run.returncode != 10:
            raise RuntimeError(f"kissat return {run.returncode}")
        positive = set()
        for line in run.stdout.splitlines():
            if line.startswith("v "):
                positive.update(int(x) for x in line.split()[1:] if int(x) > 0)
        chosen = {x - 1 for x in positive if x <= len(opts)}
        bad = directed_cycles(chosen, opts)
        if not acyclic or not bad:
            return chosen, opts, round_id, len(clauses)
        clauses.extend([[-(oi + 1) for oi in cycle] for cycle in bad])
    raise RuntimeError("cycle-cut round limit")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--acyclic", action="store_true")
    args = parser.parse_args()
    chosen, opts, rounds, clauses = solve(args.r, args.acyclic)
    if chosen is None:
        print("UNSAT", args.r, "rounds", rounds, "clauses", clauses)
        return
    print("SAT", args.r, "variables", len(opts), "rounds", rounds,
          "clauses", clauses, "rules", dict(sorted(Counter(opts[i][1] for i in chosen).items())),
          "cycles", [len(c) for c in directed_cycles(chosen, opts)])


if __name__ == "__main__":
    main()
