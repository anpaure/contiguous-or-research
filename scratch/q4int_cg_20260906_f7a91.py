"""Residual all-column LP pricing followed by an explicit integral repair."""

import argparse
from collections import Counter
import ctypes
from itertools import product
from random import Random
import time

import highspy
import numpy as np

from q4int_search_20260906_f7a91 import baseline, load, normalize, points, save, trim


LIBRARY = '/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_price_f7a91.dylib'


def solve(kept, removed, seconds, seed, rounds, limit, save_path=None, perturb=0):
    rng = Random(seed)
    covered = set(p for row in kept for p in points(row))
    required = sorted(set(range(4096)) - covered)
    index = {p: i for i, p in enumerate(required)}
    lib = ctypes.CDLL(LIBRARY)
    lib.price_q4int.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
                               ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double)]
    lib.price_q4int.restype = ctypes.c_int
    rows, rowset, costs = [], set(), []
    solver = highspy.Highs()
    solver.setOptionValue('output_flag', False)
    solver.setOptionValue('threads', 1)
    solver.setOptionValue('presolve', 'off')
    solver.setOptionValue('random_seed', seed)
    lp = highspy.HighsLp()
    lp.num_col_, lp.num_row_ = 0, len(required)
    lp.row_lower_, lp.row_upper_ = np.ones(len(required)), np.full(len(required), highspy.kHighsInf)
    lp.a_matrix_.start_ = [0]
    solver.passModel(lp)

    def insert(candidates):
        starts, ri, added_costs = [0], [], []
        for row in candidates:
            row = normalize(row)
            if row in rowset:
                continue
            cells = [index[p] for p in points(row) if p in index]
            if not cells:
                continue
            rowset.add(row)
            rows.append(row)
            cost = len(row[1])+len(row[3])
            costs.append(cost)
            added_costs.append(cost + perturb*rng.random())
            ri.extend(cells)
            starts.append(len(ri))
        n = len(added_costs)
        if n:
            solver.addCols(n, np.array(added_costs), np.zeros(n), np.full(n, highspy.kHighsInf),
                           len(ri), np.array(starts, dtype=np.int32), np.array(ri, dtype=np.int32), np.ones(len(ri)))
        return n

    insert(removed)
    out = (ctypes.c_int * (23*limit))()
    dual = (ctypes.c_double * 4096)()
    maximum = ctypes.c_double()
    start = time.monotonic()
    for step in range(rounds):
        solver.run()
        assert solver.getModelStatus() == highspy.HighsModelStatus.kOptimal
        info, sol = solver.getInfo(), solver.getSolution()
        for p, value in zip(required, sol.row_dual):
            dual[p] = value
        n = lib.price_q4int(dual, limit, rng.randrange(2**30), out, ctypes.byref(maximum))
        candidates = []
        for j in range(n):
            data = out[23*j:23*(j+1)]
            mask, nc, nd = data[:3]
            left = tuple(i for i in range(6) if mask >> i & 1)
            right = tuple(i for i in range(6) if not (mask >> i & 1))
            def decode(x, d):
                return tuple(x >> (2*i) & 3 for i in reversed(range(d)))
            c = tuple(decode(x, len(left)) for x in data[3:3+nc])
            d = tuple(decode(x, len(right)) for x in data[3+nc:3+nc+nd])
            candidates.append((left, c, right, d))
        print('CG', step, 'required', len(required), 'cols', len(rows), 'LP', info.objective_function_value,
              'violation', maximum.value, 'time', round(time.monotonic()-start, 2), flush=True)
        if maximum.value < 1e-6:
            break
        added = insert(candidates)
        if not added:
            break
    budget = sum(len(c)+len(d) for _, c, _, d in removed)
    solver.run()
    lower = solver.getInfo().objective_function_value
    if maximum.value < 1e-6 and lower > budget-1+1e-6 and not perturb:
        return None, lower, 'LP-no-improvement', len(rows)
    n = len(rows)
    inds = np.arange(n, dtype=np.int32)
    solver.changeColsCost(n, inds, np.array(costs, dtype=float))
    solver.changeColsIntegrality(n, inds, np.full(n, highspy.HighsVarType.kInteger, dtype=np.uint8))
    solver.changeColsBounds(n, inds, np.zeros(n), np.ones(n))
    solver.setOptionValue('presolve', 'on')
    solver.setOptionValue('mip_rel_gap', 0.0)
    solver.setOptionValue('time_limit', seconds)
    solver.setOptionValue('output_flag', True)
    removedset = set(map(normalize, removed))
    sol = highspy.HighsSolution()
    sol.col_value = [float(row in removedset) for row in rows]
    sol.value_valid = True
    solver.setSolution(sol)
    solver.run()
    sol, info = solver.getSolution(), solver.getInfo()
    status = solver.modelStatusToString(solver.getModelStatus())
    print('MIP fresh status', status, 'objective', info.objective_function_value, 'bound', info.mip_dual_bound, flush=True)
    if sol.value_valid and all(abs(x-round(x))<1e-6 for x in sol.col_value):
        selected = [row for row, x in zip(rows, sol.col_value) if x>0.5]
        assert covered | set(p for row in selected for p in points(row)) == set(range(4096))
        if sum(len(c)+len(d) for _, c, _, d in selected) < budget:
            result = kept + selected
            if save_path:
                save(result, save_path, 'asymmetric all-chain column generation and integer repair')
            return result, lower, status, len(rows)
    return None, lower, status, len(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output', required=True)
    parser.add_argument('--size', type=int, default=16)
    parser.add_argument('--rounds', type=int, default=40)
    parser.add_argument('--columns-per-round', type=int, default=1000)
    parser.add_argument('--mip-seconds', type=float, default=90)
    parser.add_argument('--iterations', type=int, default=5)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--perturb', type=float, default=0)
    args = parser.parse_args()
    rng = Random(args.seed)
    rows = list(map(normalize, load(args.input) if args.input else baseline()))
    save(rows, args.output, 'initial cover before exact asymmetric pricing')
    for iteration in range(args.iterations):
        take = set(rng.sample(range(len(rows)), min(args.size, len(rows))))
        removed = [row for i, row in enumerate(rows) if i in take]
        kept = [row for i, row in enumerate(rows) if i not in take]
        result, lower, status, cols = solve(kept, removed, args.mip_seconds, rng.randrange(2**30),
                                          args.rounds, args.columns_per_round, args.output, args.perturb)
        print('ITERATION', iteration, 'size', len(removed), 'budget', sum(len(c)+len(d) for _, c, _, d in removed),
              'LP', lower, 'status', status, 'columns', cols, flush=True)
        if result:
            rows = trim(result, seed=iteration)
            save(rows, args.output, 'column-generation integral repair plus exact trim')
