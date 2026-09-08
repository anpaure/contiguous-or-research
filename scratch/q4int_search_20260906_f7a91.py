"""Separate expanded integer search; all output covers contain explicit chains."""

import argparse
from collections import Counter
from itertools import combinations, permutations, product
import json
from pathlib import Path
from random import Random
import time

from q4int_verify_20260906_f7a91 import check, weight12


def baseline():
    chains = [tuple((x,) for x in range(4))]
    for _ in range(2):
        chains = [tuple([c[i] + (j,) for i in range(len(c)-j)]
                        + [c[-1-j] + (y,) for y in range(j+1, 4)])
                  for c in chains for j in range(2)]
    orders = [((0, 1, 2), (3, 4, 5)), ((1, 2, 4), (3, 5, 0)),
              ((1, 4, 3), (5, 2, 0)), ((0, 4, 1), (2, 3, 5)),
              ((4, 2, 3), (5, 0, 1))]
    return [(left, c, right, d) for left, right in orders for c, d in product(chains, repeat=2)]


def points(row):
    left, c, right, d = row
    for x, y in product(c, d):
        p = [0] * 6
        for axis, value in zip(left + right, x + y):
            p[axis] = value
        yield sum(value << (2*(5-axis)) for axis, value in enumerate(p))


def normalize(row):
    left, c, right, d = row
    lp, rp = sorted(range(len(left)), key=lambda i: left[i]), sorted(range(len(right)), key=lambda i: right[i])
    left, c = tuple(sorted(left)), tuple(tuple(x[i] for i in lp) for x in c)
    right, d = tuple(sorted(right)), tuple(tuple(x[i] for i in rp) for x in d)
    if len(left) > len(right) or (len(left) == len(right) and left > right):
        left, c, right, d = right, d, left, c
    return left, c, right, d


def save(rows, path, source):
    data = {'q': 4, 'dimension': 6, 'cost': sum(len(c)+len(d) for _, c, _, d in rows),
            'source': source,
            'rectangles': [dict(left=left, C=c, right=right, D=d) for left, c, right, d in rows]}
    check(data)
    Path(path).write_text(json.dumps(data, indent=2) + '\n')


def load(path):
    data = json.loads(Path(path).read_text())
    check(data)
    return [(tuple(row['left']), tuple(map(tuple, row['C'])),
             tuple(row['right']), tuple(map(tuple, row['D']))) for row in data['rectangles']]


def trim(rows, seed=0):
    rng = Random(seed)
    rows = list(rows)
    coverage = Counter(p for row in rows for p in points(row))
    order = list(range(len(rows)))
    rng.shuffle(order)
    for j in order:
        left, c, right, d = rows[j]
        for shore in range(2):
            chain = list(c if shore == 0 else d)
            indices = list(chain)
            rng.shuffle(indices)
            for x in indices:
                row = (left, (x,), right, d) if shore == 0 else (left, c, right, (x,))
                cells = list(points(row))
                if len(chain) > 1 and all(coverage[p] > 1 for p in cells):
                    chain.remove(x)
                    for p in cells:
                        coverage[p] -= 1
            if shore == 0:
                c = tuple(chain)
            else:
                d = tuple(chain)
        rows[j] = left, c, right, d
    return rows


def read_shapes(path):
    result = []
    for line in Path(path).read_text().splitlines():
        a = list(map(int, line.split()))
        r, n = a[:2]
        cids, m, dids = a[2:2+n], a[2+n], a[3+n:]
        assert len(dids) == m
        def decode(x, d):
            return tuple((x >> (2*i)) & 3 for i in reversed(range(d)))
        c, d = tuple(decode(x, r) for x in cids), tuple(decode(x, 6-r) for x in dids)
        result.append((c, d))
    return result


def develop(seeds):
    items = {}
    perms = list(permutations(range(6)))
    for si, (c, d) in enumerate(seeds):
        for reflection in (False, True):
            cc = tuple(tuple(3-x for x in p) for p in reversed(c)) if reflection else c
            dd = tuple(tuple(3-x for x in p) for p in reversed(d)) if reflection else d
            for perm in perms:
                row = normalize((perm[:len(c[0])], cc, perm[len(c[0]):], dd))
                if row not in items:
                    items[row] = tuple(points(row))
        if (si+1) % 100 == 0:
            print('developed', si+1, 'shapes;', len(items), 'columns', flush=True)
    return items


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shapes')
    parser.add_argument('--input')
    parser.add_argument('--output', required=True)
    parser.add_argument('--solver', choices=['trim', 'highs', 'cp'], default='trim')
    parser.add_argument('--seconds', type=float, default=120)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--threads', type=int, default=8)
    parser.add_argument('--target', type=int)
    args = parser.parse_args()
    initial = load(args.input) if args.input else baseline()
    best = initial
    for k in range(100):
        candidate = trim(initial, args.seed+k)
        if sum(len(c)+len(d) for _, c, _, d in candidate) < sum(len(c)+len(d) for _, c, _, d in best):
            best = candidate
    print('trimmed baseline', sum(len(c)+len(d) for _, c, _, d in best), flush=True)
    save(best, args.output, 'exact all-target trimming')
    if args.solver == 'trim':
        return
    if args.shapes:
        seeds = read_shapes(args.shapes)
    else:
        from q4d6_fractional_template_20260906_c52e9 import rows
        seeds = [(c, d) for _, c, d in rows()]
    items = develop(seeds)
    for row in initial + best:
        row = normalize(row)
        items[row] = tuple(points(row))
    rows = list(items)
    costs = [len(c)+len(d) for _, c, _, d in rows]
    owners = [[] for _ in range(4096)]
    for i, cells in enumerate(items.values()):
        for p in cells:
            owners[p].append(i)
    print('model columns', len(rows), 'incidences', sum(map(len, owners)), flush=True)
    initial_set = set(map(normalize, best))
    if args.solver == 'cp':
        from ortools.sat.python import cp_model
        model = cp_model.CpModel()
        variables = [model.new_bool_var(f'x{i}') for i in range(len(rows))]
        for indices in owners:
            model.add(sum(variables[i] for i in indices) >= 1)
        objective = sum(c*x for c, x in zip(costs, variables))
        model.minimize(objective)
        if args.target:
            model.add(objective <= args.target)
        for row, x in zip(rows, variables):
            model.add_hint(x, int(row in initial_set))
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = args.seconds
        solver.parameters.num_search_workers = args.threads
        solver.parameters.random_seed = args.seed
        solver.parameters.log_search_progress = True
        class Incumbent(cp_model.CpSolverSolutionCallback):
            def on_solution_callback(self):
                selected = [row for row, x in zip(rows, variables) if self.value(x)]
                save(selected, args.output, 'CP-SAT expanded integer pool, independently checked')
        status = solver.solve(model, Incumbent())
        print('fresh status', solver.status_name(status), 'bound', solver.best_objective_bound,
              'objective', solver.objective_value, flush=True)
    else:
        import highspy
        import numpy as np
        from scipy.sparse import csc_matrix
        ri, ci = [], []
        for p, indices in enumerate(owners):
            ri.extend([p]*len(indices))
            ci.extend(indices)
        matrix = csc_matrix((np.ones(len(ri)), (ri, ci)), shape=(4096, len(rows)))
        lp = highspy.HighsLp()
        lp.num_col_, lp.num_row_ = len(rows), 4096
        lp.col_cost_, lp.col_lower_, lp.col_upper_ = np.array(costs, dtype=float), np.zeros(len(rows)), np.ones(len(rows))
        lp.row_lower_, lp.row_upper_ = np.ones(4096), np.full(4096, highspy.kHighsInf)
        lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_, lp.a_matrix_.index_, lp.a_matrix_.value_ = matrix.indptr, matrix.indices, matrix.data
        lp.integrality_ = [highspy.HighsVarType.kInteger]*len(rows)
        solver = highspy.Highs()
        solver.setOptionValue('time_limit', args.seconds)
        solver.setOptionValue('mip_rel_gap', 0.0)
        solver.setOptionValue('threads', args.threads)
        solver.setOptionValue('random_seed', args.seed)
        if args.target:
            solver.setOptionValue('objective_bound', float(args.target))
        solver.passModel(lp)
        solution = highspy.HighsSolution()
        solution.col_value = [float(row in initial_set) for row in rows]
        solution.value_valid = True
        solver.setSolution(solution)
        solver.run()
        info = solver.getInfo()
        solution = solver.getSolution()
        print('fresh status', solver.modelStatusToString(solver.getModelStatus()),
              'bound', info.mip_dual_bound, 'objective', info.objective_function_value, flush=True)
        if solution.value_valid and all(abs(x-round(x)) < 1e-6 for x in solution.col_value):
            selected = [row for row, x in zip(rows, solution.col_value) if x > 0.5]
            save(selected, args.output, 'HiGHS expanded integer pool, independently checked')


if __name__ == '__main__':
    main()
