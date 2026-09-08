"""Exact local chain-vertex formulation, with no prescribed chain catalogue."""

import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
from random import Random
import time

from ortools.sat.python import cp_model

from q4int_search_20260906_f7a91 import baseline, load, normalize, points, save, trim


GRID = list(product(range(4), repeat=6))


def repair(kept, removed, supports, seconds, seed, threads, target=None):
    covered = set(p for row in kept for p in points(row))
    required = sorted(set(range(4096)) - covered)
    budget = sum(len(c)+len(d) for _, c, _, d in removed)
    if target is None:
        target = budget - 1
    model = cp_model.CpModel()
    selections = []
    used = []
    localpoints = [GRID[p] for p in required]
    for j, left in enumerate(supports):
        right = tuple(i for i in range(6) if i not in left)
        shores = []
        for side, axes in enumerate((left, right)):
            projected = sorted({tuple(p[i] for i in axes) for p in localpoints})
            vertices = {p: model.new_bool_var(f'u{j}_{side}_{p}') for p in projected}
            for p, q in combinations(projected, 2):
                if not all(x <= y for x, y in zip(p, q)):
                    model.add_at_most_one(vertices[p], vertices[q])
            shores.append(vertices)
            used.extend(vertices.values())
        selections.append((left, shores[0], right, shores[1]))
    for p in localpoints:
        options = []
        for j, (left, c, right, d) in enumerate(selections):
            x, y = tuple(p[i] for i in left), tuple(p[i] for i in right)
            v = model.new_bool_var('')
            model.add_implication(v, c[x])
            model.add_implication(v, d[y])
            options.append(v)
        model.add_bool_or(options)
    model.add(sum(used) <= target)
    model.minimize(sum(used))
    # Label same-support rectangles by their first selected shore vertex.
    for i, j in combinations(range(len(supports)), 2):
        if supports[i] == supports[j]:
            cv, dv = selections[i][1], selections[j][1]
            a = model.new_int_var(0, len(cv), '')
            b = model.new_int_var(0, len(dv), '')
            model.add_min_equality(a, [k + len(cv)*(1-v) for k, v in enumerate(cv.values())])
            model.add_min_equality(b, [k + len(dv)*(1-v) for k, v in enumerate(dv.values())])
            model.add(a <= b)
    if len(removed) == len(supports):
        for row, (left, c, right, d) in zip(removed, selections):
            if row[0] != left:
                continue
            for p, v in c.items():
                model.add_hint(v, int(p in row[1]))
            for p, v in d.items():
                model.add_hint(v, int(p in row[3]))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = threads
    solver.parameters.random_seed = seed
    status = solver.solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None, solver.status_name(status), len(required)
    result = []
    for left, c, right, d in selections:
        cc = tuple(p for p, v in c.items() if solver.value(v))
        dd = tuple(p for p, v in d.items() if solver.value(v))
        if cc and dd:
            result.append((left, cc, right, dd))
    assert sum(len(c)+len(d) for _, c, _, d in result) <= target
    assert covered | set(p for row in result for p in points(row)) == set(range(4096))
    return result, solver.status_name(status), len(required)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output', required=True)
    parser.add_argument('--seconds', type=float, default=300)
    parser.add_argument('--per-call', type=float, default=2)
    parser.add_argument('--size', type=int, default=4)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--all-pairs', action='store_true')
    parser.add_argument('--extra', type=int, default=0)
    args = parser.parse_args()
    rng = Random(args.seed)
    rows = list(map(normalize, load(args.input) if args.input else baseline()))
    start = time.monotonic()
    attempts = Counter()
    iteration = 0
    pairs = list(combinations(range(len(rows)), 2))
    rng.shuffle(pairs)
    costs = lambda rr: sum(len(c)+len(d) for _, c, _, d in rr)
    save(rows, args.output, 'initial cover for no-catalogue local search')
    while time.monotonic()-start < args.seconds:
        iteration += 1
        if args.all_pairs:
            if not pairs:
                break
            take = set(pairs.pop())
        else:
            anchor = rng.randrange(len(rows))
            left, c, right, d = rows[anchor]
            ap = set(points(rows[anchor]))
            candidates = [i for i in range(len(rows)) if i != anchor]
            rng.shuffle(candidates)
            candidates.sort(key=lambda i: (bool(set(points(rows[i])) & ap),
                                           rows[i][0] == left, rng.random()), reverse=True)
            nearby = candidates[:max(args.size, len(rows)//3)]
            take = {anchor, *rng.sample(nearby, min(args.size-1, len(nearby)))}
        removed = [row for i, row in enumerate(rows) if i in take]
        kept = [row for i, row in enumerate(rows) if i not in take]
        supports = [row[0] for row in removed]
        for _ in range(args.extra):
            supports.append((0,)+tuple(sorted(rng.sample(range(1, 6), 2))))
        candidate, status, nr = repair(kept, removed, supports, args.per_call,
                                       rng.randrange(2**30), args.threads)
        attempts[status] += 1
        if candidate is not None:
            old = costs(rows)
            rows = trim(kept+candidate, seed=iteration)
            save(rows, args.output, f'no-catalogue exact local replacement, iteration {iteration}')
            print('IMPROVEMENT', old, '->', costs(rows), 'remove', len(removed),
                  'replace', len(candidate), 'required', nr, flush=True)
            pairs = list(combinations(range(len(rows)), 2))
            rng.shuffle(pairs)
        if iteration % 10 == 0:
            print('iteration', iteration, 'elapsed', round(time.monotonic()-start, 2),
                  'cost', costs(rows), 'statuses', dict(attempts), flush=True)
    print('FINISHED', 'iterations', iteration, 'cost', costs(rows), 'statuses', dict(attempts), flush=True)


if __name__ == '__main__':
    main()
