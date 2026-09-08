#!/usr/bin/env python3
"""Audit the cyclic-unmatched triangle selector reduction.

For every upper word U of weight r+1 in length 2r-1, cyclic parenthesis
matching leaves three unmatched ones f[0],f[1],f[2].  Option i deletes
f[i],f[i+1] and orients the resulting Johnson edge from the facet obtained
by restoring f[i] to the facet obtained by restoring f[i+1].

The optional SAT run asks for one option per upper, distinct tails, and
distinct heads.  It then audits lower-colour injectivity and directed
cycles.  Kissat is required only for --solve.
"""

import argparse
import itertools
import math
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        yield sum(1 << i for i in cc)


def cyclic_free_ones(word, n):
    height = 0
    values = [0]
    for i in range(n):
        height += 1 if (word >> i) & 1 else -1
        values.append(height)
    start = max(i for i, value in enumerate(values[:-1])
                if value == max(values[:-1])) % n
    stack, free = [], []
    for offset in range(n):
        i = (start + offset) % n
        if not ((word >> i) & 1):
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free.append(i)
    assert not stack and len(free) == 3
    return free


def cyclic_free_zero(word, n):
    """Unique survivor under cyclic 01 cancellation for zero excess one."""
    height = 0
    values = [0]
    for i in range(n):
        height += 1 if not ((word >> i) & 1) else -1
        values.append(height)
    assert values[-1] == 1
    minimum = min(values[:-1])
    return max(i for i, value in enumerate(values[:-1]) if value == minimum)


def build_options(r):
    n = 2 * r - 1
    result = []
    for upper_id, upper in enumerate(masks(n, r + 1)):
        free = cyclic_free_ones(upper, n)
        for rule in range(3):
            x, y = free[rule], free[(rule + 1) % 3]
            lower = upper ^ (1 << x) ^ (1 << y)
            tail = lower | (1 << x)
            head = lower | (1 << y)
            result.append((upper_id, rule, lower, tail, head))
    return result


def directed_cycles(selected, options):
    successor, edge_at = {}, {}
    for oi in selected:
        tail, head = options[oi][3:]
        assert tail not in successor
        successor[tail] = head
        edge_at[tail] = oi
    cycles, done = [], set()
    for start in successor:
        if start in done:
            continue
        position, walk = {}, []
        vertex = start
        while vertex in successor and vertex not in done:
            if vertex in position:
                cycles.append([edge_at[x] for x in walk[position[vertex]:]])
                break
            position[vertex] = len(walk)
            walk.append(vertex)
            vertex = successor[vertex]
        done.update(walk)
    return cycles


def solve_two_sdr(r):
    options = build_options(r)
    by_upper, by_tail, by_head = (defaultdict(list) for _ in range(3))
    for oi, option in enumerate(options):
        variable = oi + 1
        by_upper[option[0]].append(variable)
        by_tail[option[3]].append(variable)
        by_head[option[4]].append(variable)
    clauses = []
    for variables in by_upper.values():
        clauses.append(variables)
        clauses.extend([-a, -b] for a, b in itertools.combinations(variables, 2))
    for shore in (by_tail, by_head):
        for variables in shore.values():
            clauses.extend([-a, -b] for a, b in itertools.combinations(variables, 2))
    with tempfile.TemporaryDirectory(prefix="cyclic_triangle_") as td:
        formula = Path(td) / "instance.cnf"
        formula.write_text(
            f"p cnf {len(options)} {len(clauses)}\n"
            + "".join(" ".join(map(str, clause)) + " 0\n" for clause in clauses)
        )
        run = subprocess.run(["kissat", str(formula)], capture_output=True,
                             text=True, check=False)
    if run.returncode == 20:
        return None, options, len(clauses)
    if run.returncode != 10:
        raise RuntimeError("kissat returned neither SAT nor UNSAT")
    positive = set()
    for line in run.stdout.splitlines():
        if line.startswith("v "):
            positive.update(int(x) for x in line.split()[1:] if int(x) > 0)
    chosen = {x - 1 for x in positive if x <= len(options)}
    assert len(chosen) == len(options) // 3
    return chosen, options, len(clauses)


def audit_rainbow_pentagon(r, options):
    """Replay the all-r directed C5 obstruction from the theorem note."""
    if r < 3:
        return False
    n = 2 * r - 1
    uppers = list(masks(n, r + 1))
    option_at = {(uppers[x[0]], x[1]): x for x in options}
    if r == 3:
        specs = [({0, 1, 2, 3}, 0), ({0, 2, 3, 4}, 2),
                 ({0, 1, 2, 4}, 0), ({1, 2, 3, 4}, 1),
                 ({0, 1, 3, 4}, 0)]
    else:
        base = set(range(r - 3))
        a, b, c, d, e = range(r - 3, r + 2)
        specs = [(base | {a, b, c, d}, 0),
                 (base | {a, c, d, e}, 1),
                 (base | {a, b, c, e}, 0),
                 (base | {b, c, d, e}, 0),
                 (base | {a, b, d, e}, 2)]
    chosen = [option_at[(sum(1 << i for i in upper), rule)]
              for upper, rule in specs]
    assert all(chosen[i][4] == chosen[(i + 1) % 5][3] for i in range(5))
    for coordinate in (0, 2, 3, 4):
        assert len({x[coordinate] for x in chosen}) == 5
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--solve", action="store_true")
    args = parser.parse_args()
    options = build_options(args.r)
    n = 2 * args.r - 1
    tau = {}
    for lower in masks(n, args.r - 1):
        tau[lower] = lower | (1 << cyclic_free_zero(lower, n))
    assert len(set(tau.values())) == len(tau)
    by_upper = defaultdict(dict)
    for option in options:
        by_upper[option[0]][option[1]] = option
        assert tau[option[2]] == option[3]
    inverse_tau = {owner: lower for lower, owner in tau.items()}
    for choices in by_upper.values():
        for rule, option in choices.items():
            assert inverse_tau[option[4]] == choices[(rule + 2) % 3][2]
    lower_degree = Counter(Counter(x[2] for x in options).values())
    expected_degree = {}
    for degree in range(1, args.r):
        m = args.r - 1
        expected_degree[degree] = (
            n * degree * math.comb(2 * m - degree, m)
            // (2 * m - degree)
        )
    assert lower_degree == Counter(expected_degree)
    vertices = math.comb(n, args.r - 1)
    faces = len(options) // 3
    singletons = lower_degree[1]
    mandatory_omissions = 3 * faces - 2 * vertices + singletons
    omission_margin = faces - mandatory_omissions
    expected_margin = (
        math.comb(2 * args.r, args.r) // (args.r + 1)
        * (-args.r * args.r + 15 * args.r - 24)
        // (4 * (2 * args.r - 3))
    )
    assert omission_margin == expected_margin
    print("INCIDENCE", args.r, "uppers", len(options) // 3,
          "options", len(options), "lower_degree", dict(sorted(lower_degree.items())),
          "omission_margin", omission_margin,
          "rainbow_C5", audit_rainbow_pentagon(args.r, options))
    if args.solve:
        chosen, options, clauses = solve_two_sdr(args.r)
        if chosen is None:
            print("TWO_SDR_UNSAT", args.r, "clauses", clauses)
            return
        lowers = [options[i][2] for i in chosen]
        tails = [options[i][3] for i in chosen]
        heads = [options[i][4] for i in chosen]
        cycles = directed_cycles(chosen, options)
        print("TWO_SDR_SAT", args.r, "clauses", clauses,
              "lower_distinct", len(set(lowers)),
              "tail_distinct", len(set(tails)),
              "head_distinct", len(set(heads)),
              "cycles", [len(cycle) for cycle in cycles],
              "rules", dict(sorted(Counter(options[i][1] for i in chosen).items())))


if __name__ == "__main__":
    main()
