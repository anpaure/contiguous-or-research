"""Dual-guided expanded exact-cover / integer-cover pool, optionally folded."""

import argparse
from collections import Counter
import ctypes
from itertools import permutations, product
import json
from pathlib import Path
from random import Random
import time

import numpy as np
from ortools.sat.python import cp_model

from q4int_cg_20260906_f7a91 import LIBRARY
from q4int_search_20260906_f7a91 import baseline, develop, normalize, points, read_shapes, save
from q4int_verify_20260906_f7a91 import weight12


GRID = list(product(range(4), repeat=6))
WEIGHT = [weight12(p) for p in GRID]


def transform(row, perm, reflection):
    left, c, right, d = row
    if reflection:
        c = tuple(tuple(3-x for x in p) for p in reversed(c))
        d = tuple(tuple(3-x for x in p) for p in reversed(d))
    return normalize((tuple(perm[i] for i in left), c, tuple(perm[i] for i in right), d))


def automorphism(rows):
    rows = set(map(normalize, rows))
    for perm in permutations(range(6)):
        for reflection in (False, True):
            if perm == tuple(range(6)) and not reflection:
                continue
            if {transform(row, perm, reflection) for row in rows} == rows:
                assert all(perm[perm[i]] == i for i in range(6))
                print('baseline involution', perm, 'reflection', reflection, flush=True)
                return perm, reflection
    raise AssertionError('no baseline involution')


def priced_pool(rounds, per_round, seed):
    lib = ctypes.CDLL(LIBRARY)
    lib.price_q4int.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
                               ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double)]
    lib.price_q4int.restype = ctypes.c_int
    out = (ctypes.c_int * (23*per_round))()
    dual = (ctypes.c_double * 4096)()
    maximum = ctypes.c_double()
    rng = Random(seed)
    rows = set()
    start = time.monotonic()
    for step in range(rounds):
        noise = [rng.uniform(-1, 1) for _ in range(4096)]
        if step % 3 == 1:
            by_orbit = {}
            noise = []
            for p in GRID:
                counts = tuple(p.count(i) for i in range(4))
                key = min(counts, counts[::-1])
                if key not in by_orbit:
                    by_orbit[key] = rng.uniform(-1, 1)
                noise.append(by_orbit[key])
        elif step % 3 == 2:
            row_noise = [rng.uniform(-1, 1) for _ in baseline()]
            noise = [0.1*x for x in noise]
            for row, value in zip(baseline(), row_noise):
                for p in points(row):
                    noise[p] += value
        for p in range(4096):
            dual[p] = max(0, WEIGHT[p]/12 + 1e-5*noise[p])
        n = lib.price_q4int(dual, per_round, rng.randrange(2**30), out, ctypes.byref(maximum))
        for j in range(n):
            data = out[23*j:23*(j+1)]
            mask, nc, nd = data[:3]
            left = tuple(i for i in range(6) if mask >> i & 1)
            right = tuple(i for i in range(6) if not (mask >> i & 1))
            def decode(x, d):
                return tuple(x >> (2*i) & 3 for i in reversed(range(d)))
            c = tuple(decode(x, len(left)) for x in data[3:3+nc])
            d = tuple(decode(x, len(right)) for x in data[3+nc:3+nc+nd])
            row = normalize((left, c, right, d))
            assert sum(WEIGHT[p] for p in points(row)) == 12*(nc+nd)
            rows.add(row)
        if (step+1) % 5 == 0:
            print('priced rounds', step+1, 'new rows', len(rows), 'seconds', round(time.monotonic()-start, 2), flush=True)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--pool-output')
    parser.add_argument('--pool-input')
    parser.add_argument('--mutations', action='store_true')
    parser.add_argument('--balanced-seeds', action='store_true')
    parser.add_argument('--face-filter', action='store_true')
    parser.add_argument('--overlap-ledger', action='store_true')
    parser.add_argument('--rounds', type=int, default=40)
    parser.add_argument('--columns-per-round', type=int, default=1500)
    parser.add_argument('--sample-shapes', type=int, default=0)
    parser.add_argument('--seconds', type=float, default=300)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--threads', type=int, default=8)
    parser.add_argument('--target', type=int, default=1248)
    parser.add_argument('--solver', choices=['cp', 'highs'], default='cp')
    parser.add_argument('--symmetry', choices=['none', 'baseline', 'reflection', 'cycle3', 'cycle5'], default='baseline')
    parser.add_argument('--log', action='store_true')
    args = parser.parse_args()
    base = list(map(normalize, baseline()))
    if args.pool_input:
        data = json.loads(Path(args.pool_input).read_text())
        pool = set((tuple(l), tuple(map(tuple, c)), tuple(r), tuple(map(tuple, d))) for l, c, r, d in data)
    else:
        from q4d6_fractional_template_20260906_c52e9 import rows as fractional
        pool = set(develop([(c, d) for _, c, d in fractional()]))
        pool.update(priced_pool(args.rounds, args.columns_per_round, args.seed))
        if args.sample_shapes:
            rng = Random(args.seed)
            shapes = read_shapes('scratch/q4int_tight_shapes_20260906_f7a91.txt')
            selected = rng.sample(shapes, min(args.sample_shapes, len(shapes)))
            pool.update(develop(selected))
        pool.update(base)
        if args.pool_output:
            Path(args.pool_output).write_text(json.dumps(sorted(pool), separators=(',', ':')) + '\n')
    if args.mutations:
        def neighbors(chain):
            candidates = {chain}
            universe = list(product(range(4), repeat=len(chain[0])))
            for i in range(len(chain)):
                part = chain[:i] + chain[i+1:]
                if part:
                    candidates.add(part)
                for p in universe:
                    if p in part:
                        continue
                    cc = tuple(sorted(part + (p,)))
                    if all(all(x <= y for x, y in zip(a, b)) for a, b in zip(cc, cc[1:])):
                        candidates.add(cc)
            for p in universe:
                if p in chain:
                    continue
                cc = tuple(sorted(chain + (p,)))
                if all(all(x <= y for x, y in zip(a, b)) for a, b in zip(cc, cc[1:])):
                    candidates.add(cc)
            return candidates
        for left, c, right, d in base:
            for cc, dd in product(neighbors(c), neighbors(d)):
                pool.add((left, cc, right, dd))
        print('with actual chain-vertex mutations', len(pool), 'columns', flush=True)
    if args.balanced_seeds:
        from q4int_balanced_fractional_20260906_f7a91 import rows as balanced_rows, check as balanced_check
        balanced_check()
        pool.update(develop([(c, d) for _, c, d in balanced_rows()]))
        print('with balanced fractional support', len(pool), 'columns', flush=True)
    direction = None
    if args.face_filter:
        assert args.target == 1248
        face = json.loads(Path('scratch/q4int_face_direction_20260906_f7a91.json').read_text())
        by_orbit = {tuple(p[:4]): v for p, v in zip(face['populations'], face['direction'])}
        direction = []
        for p in GRID:
            counts = tuple(p.count(i) for i in range(4))
            direction.append(by_orbit[min(counts, counts[::-1])])
    if args.symmetry == 'baseline':
        perm, reflection = automorphism(base)
    elif args.symmetry == 'reflection':
        perm, reflection = tuple(range(6)), True
    elif args.symmetry == 'cycle3':
        perm, reflection = (1, 2, 0, 4, 5, 3), False
    elif args.symmetry == 'cycle5':
        perm, reflection = (1, 2, 3, 4, 0, 5), False
    else:
        perm, reflection = tuple(range(6)), False
    transform_index = []
    for p in GRID:
        q = [0]*6
        for i, x in enumerate(p):
            q[perm[i]] = 3-x if reflection else x
        transform_index.append(sum(x << (2*(5-i)) for i, x in enumerate(q)))
    representatives = []
    for i in range(4096):
        orbit = {i}
        j = transform_index[i]
        while j not in orbit:
            orbit.add(j)
            j = transform_index[j]
        representatives.append(min(orbit))
    point_reps = sorted(set(representatives))
    point_index = {p: i for i, p in enumerate(point_reps)}
    indices = [point_index[p] for p in representatives]
    bundles, costs, slacks, owners, seen = [], [], [], [[] for _ in point_reps], set()
    for row in sorted(pool):
        orbit = {row}
        other = transform(row, perm, reflection)
        while other not in orbit:
            orbit.add(other)
            other = transform(other, perm, reflection)
        key = tuple(sorted(orbit))
        if key in seen:
            continue
        seen.add(key)
        cells = Counter(p for member in key for p in points(member))
        cost = sum(len(c)+len(d) for _, c, _, d in key)
        if args.target == 1248:
            if sum(WEIGHT[p]*v for p, v in cells.items()) != 12*cost:
                continue
            if any(v>1 and WEIGHT[p] for p, v in cells.items()):
                continue
            if direction is not None and sum(direction[p]*v for p, v in cells.items()):
                continue
        bi = len(bundles)
        bundles.append(key)
        costs.append(cost)
        slack = 12*cost - sum(WEIGHT[p] for p in cells)
        assert slack >= 0
        slacks.append(slack)
        for p in {indices[p] for p in cells}:
            owners[p].append(bi)
    print('EXPANDED MODEL', 'raw columns', len(pool), 'bundles', len(bundles), 'point orbits', len(owners),
          'incidences', sum(map(len, owners)), 'target', args.target, flush=True)
    if args.solver == 'highs':
        import highspy
        from scipy.sparse import csc_matrix
        ri, ci = [], []
        for i, columns in enumerate(owners):
            ri.extend([i]*len(columns))
            ci.extend(columns)
        matrix = csc_matrix((np.ones(len(ri)), (ri, ci)), shape=(len(owners), len(bundles)))
        lp = highspy.HighsLp()
        lp.num_col_, lp.num_row_ = len(bundles), len(owners)
        lp.col_cost_ = np.array(costs, dtype=float)
        lp.col_lower_, lp.col_upper_ = np.zeros(len(bundles)), np.ones(len(bundles))
        lp.row_lower_ = np.ones(len(owners))
        lp.row_upper_ = np.array([1 if args.target == 1248 and WEIGHT[p] else highspy.kHighsInf for p in point_reps])
        lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_, lp.a_matrix_.index_, lp.a_matrix_.value_ = matrix.indptr, matrix.indices, matrix.data
        lp.integrality_ = [highspy.HighsVarType.kInteger]*len(bundles)
        solver = highspy.Highs()
        solver.setOptionValue('output_flag', args.log)
        solver.setOptionValue('time_limit', args.seconds)
        solver.setOptionValue('threads', args.threads)
        solver.setOptionValue('random_seed', args.seed)
        solver.setOptionValue('mip_rel_gap', 0.0)
        solver.setOptionValue('mip_heuristic_effort', 0.8)
        solver.passModel(lp)
        solver.addRow(1248, args.target, len(bundles), np.arange(len(bundles), dtype=np.int32), np.array(costs, dtype=float))
        if args.target >= 1280 and args.symmetry in ('none', 'baseline'):
            baseset = set(base)
            solution = highspy.HighsSolution()
            solution.col_value = [float(set(bundle) <= baseset) for bundle in bundles]
            solution.value_valid = True
            solver.setSolution(solution)
        solver.run()
        solution, info = solver.getSolution(), solver.getInfo()
        status = solver.modelStatusToString(solver.getModelStatus())
        result = {'solver': 'highs', 'status': status, 'bound': info.mip_dual_bound,
                  'reported_objective': info.objective_function_value, 'target': args.target,
                  'symmetry': args.symmetry, 'raw_columns': len(pool), 'bundles': len(bundles),
                  'point_orbits': len(owners), 'seconds_limit': args.seconds, 'verified_cost': None}
        if solution.value_valid and all(abs(x-round(x))<1e-6 for x in solution.col_value):
            selected = [row for bundle, x in zip(bundles, solution.col_value) if x>0.5 for row in bundle]
            if set(p for row in selected for p in points(row)) == set(range(4096)):
                save(selected, args.output, f'HiGHS expanded integer pool, symmetry={args.symmetry}, seed={args.seed}')
                result['verified_cost'] = sum(len(c)+len(d) for _, c, _, d in selected)
        Path(args.output + '.status.json').write_text(json.dumps(result, indent=2) + '\n')
        print('FRESH FINAL STATUS', json.dumps(result), flush=True)
        return
    model = cp_model.CpModel()
    variables = [model.new_bool_var(f'x{i}') for i in range(len(bundles))]
    for rep, cols in zip(point_reps, owners):
        if args.target == 1248 and WEIGHT[rep]:
            model.add_exactly_one(variables[i] for i in cols)
        else:
            model.add_bool_or(variables[i] for i in cols)
    objective = sum(c*x for c, x in zip(costs, variables))
    model.add(objective >= 1248)
    model.add(objective <= args.target)
    if args.overlap_ledger and args.target > 1248:
        populations = Counter(representatives)
        charges = [slack*x for slack, x in zip(slacks, variables) if slack]
        for rep, cols in zip(point_reps, owners):
            if not WEIGHT[rep]:
                continue
            repeated = model.new_bool_var(f'repeated{rep}')
            model.add(sum(variables[i] for i in cols) <= 1).only_enforce_if(repeated.Not())
            charges.append(WEIGHT[rep]*populations[rep]*repeated)
        model.add(sum(charges) <= 12*(args.target-1248))
    if args.target > 1248:
        model.minimize(objective)
    if args.target >= 1280:
        baseset = set(base)
        for bundle, x in zip(bundles, variables):
            model.add_hint(x, int(set(bundle) <= baseset))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.threads
    solver.parameters.random_seed = args.seed
    solver.parameters.log_search_progress = args.log
    class Incumbent(cp_model.CpSolverSolutionCallback):
        def on_solution_callback(self):
            selected = [row for bundle, x in zip(bundles, variables) if self.value(x) for row in bundle]
            save(selected, args.output, f'expanded exact integer search; symmetry={args.symmetry}; seed={args.seed}')
    status = solver.solve(model, Incumbent())
    print('FRESH FINAL STATUS', solver.status_name(status), 'objective', solver.objective_value,
          'bound', solver.best_objective_bound, 'walltime', solver.wall_time, flush=True)
    print('SCOPE: status applies only to this finite column pool and symmetry restriction.', flush=True)
    result = {'solver': 'cp-sat', 'status': solver.status_name(status), 'target': args.target,
              'symmetry': args.symmetry, 'raw_columns': len(pool), 'bundles': len(bundles),
              'point_orbits': len(owners), 'walltime': solver.wall_time,
              'verified_cost': None, 'reported_bound': solver.best_objective_bound}
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result['verified_cost'] = sum(cost for cost, x in zip(costs, variables) if solver.value(x))
    Path(args.output + '.status.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
