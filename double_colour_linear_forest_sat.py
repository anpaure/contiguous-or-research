#!/usr/bin/env python3
"""Find an upper-exact/lower-injective degree-two Johnson forest via SAT."""

import argparse
import itertools
import pathlib
import subprocess
import tempfile


class CNF:
    def __init__(self):
        self.nvars = 0
        self.clauses = []

    def var(self):
        self.nvars += 1
        return self.nvars

    def add(self, *lits):
        self.clauses.append(tuple(lits))

    def at_most_one(self, xs):
        # Pairwise is best for the short local lists in this model.
        for a, b in itertools.combinations(xs, 2):
            self.add(-a, -b)

    def at_most_two(self, xs):
        # Sinz-style sequential counter with two columns.
        xs = list(xs)
        if len(xs) <= 2:
            return
        prev1 = prev2 = None
        for i, x in enumerate(xs):
            if i == len(xs) - 1:
                self.add(-x, -prev2)
                break
            cur1, cur2 = self.var(), self.var()
            self.add(-x, cur1)
            if prev1 is not None:
                self.add(-prev1, cur1)
                self.add(-x, -prev1, cur2)
                self.add(-prev2, cur2)
                self.add(-x, -prev2)
            else:
                self.add(-cur2)
            prev1, prev2 = cur1, cur2

    def write(self, path):
        with open(path, "w") as out:
            out.write(f"p cnf {self.nvars} {len(self.clauses)}\n")
            for clause in self.clauses:
                out.write(" ".join(map(str, clause)) + " 0\n")


def masks(n, rank):
    for xs in itertools.combinations(range(n), rank):
        value = 0
        for x in xs:
            value |= 1 << x
        yield value


def solve(r, max_rounds, output):
    n = 2 * r - 1
    owners = list(masks(n, r))
    uppers = list(masks(n, r + 1))
    lowers = list(masks(n, r - 1))
    cnf = CNF()
    data = {}
    by_upper = {u: [] for u in uppers}
    by_lower = {l: [] for l in lowers}
    by_owner = {a: [] for a in owners}
    for u in uppers:
        bits = [x for x in range(n) if (u >> x) & 1]
        for x, y in itertools.combinations(bits, 2):
            l = u & ~(1 << x) & ~(1 << y)
            a = u & ~(1 << x)
            b = u & ~(1 << y)
            v = cnf.var()
            data[v] = (u, l, a, b)
            by_upper[u].append(v)
            by_lower[l].append(v)
            by_owner[a].append(v)
            by_owner[b].append(v)
    for vs in by_upper.values():
        cnf.add(*vs)
        cnf.at_most_one(vs)
    for vs in by_lower.values():
        cnf.at_most_one(vs)
    for vs in by_owner.values():
        cnf.at_most_two(vs)

    with tempfile.TemporaryDirectory(prefix="double_turn_sat_") as td:
        td = pathlib.Path(td)
        formula = td / "problem.cnf"
        model = td / "model.txt"
        for round_no in range(max_rounds):
            cnf.write(formula)
            result = subprocess.run(
                ["kissat", str(formula)], capture_output=True, text=True
            )
            text = result.stdout + "\n" + result.stderr
            if "s UNSATISFIABLE" in text:
                print(f"UNSAT r={r} round={round_no} vars={cnf.nvars} clauses={len(cnf.clauses)}")
                return 1
            if "s SATISFIABLE" not in text:
                print(text)
                raise RuntimeError("kissat gave no SAT status")
            positive = set()
            for line in text.splitlines():
                if line.startswith("v "):
                    positive.update(int(x) for x in line.split()[1:] if int(x) > 0)
            chosen = [v for v in data if v in positive]
            assert len(chosen) == len(uppers)
            graph = {a: [] for a in owners}
            for v in chosen:
                _, _, a, b = data[v]
                graph[a].append((b, v))
                graph[b].append((a, v))
            seen = set()
            cycles = []
            components = 0
            for start in owners:
                if start in seen:
                    continue
                components += 1
                stack = [(start, None)]
                seen.add(start)
                vertices = []
                edge_ids = set()
                while stack:
                    x, parent = stack.pop()
                    vertices.append(x)
                    for y, v in graph[x]:
                        edge_ids.add(v)
                        if y not in seen:
                            seen.add(y)
                            stack.append((y, x))
                if edge_ids and len(edge_ids) == len(vertices):
                    cycles.append(sorted(edge_ids))
            if not cycles:
                print(
                    f"SAT_FOREST r={r} round={round_no} edges={len(chosen)} "
                    f"components={components} vars={cnf.nvars} clauses={len(cnf.clauses)}"
                )
                with open(output, "w") as out:
                    for v in chosen:
                        u, l, a, b = data[v]
                        out.write(f"{u} {l} {a} {b}\n")
                return 0
            print(
                f"SAT_WITH_CYCLES r={r} round={round_no} cycles={len(cycles)} "
                f"sizes={[len(x) for x in cycles[:12]]}"
            )
            for cycle in cycles:
                cnf.add(*(-v for v in cycle))
    print(f"NO_FOREST_WITHIN_ROUNDS r={r} rounds={max_rounds}")
    return 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--rounds", type=int, default=1000)
    parser.add_argument("--output", default="double_colour_linear_forest.txt")
    args = parser.parse_args()
    raise SystemExit(solve(args.r, args.rounds, args.output))


if __name__ == "__main__":
    main()
