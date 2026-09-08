"""Exploratory exact-cover LP/MILP on actual product-chain points.

Requires scipy only for the optional optimization commands. No solver output
is used as an asymptotic theorem. All selected integral rectangles are checked
against the actual grid, not just its rank counts.
"""

import argparse
from itertools import combinations, product


def planar_chains(a, b, saturated):
    def extend(chain):
        yield tuple(chain)
        x, y = chain[-1]
        if saturated:
            successors = [(x + 1, y), (x, y + 1)]
        else:
            successors = [(u, v) for u in range(x, a)
                          for v in range(y, b) if (u, v) != (x, y)]
        for u, v in successors:
            if u < a and v < b:
                yield from extend(chain + [(u, v)])

    for start in product(range(a), range(b)):
        yield from extend([start])


def rectangles(lengths, saturated):
    points = list(product(*(range(a) for a in lengths)))
    index = {point: i for i, point in enumerate(points)}
    catalogue = {}
    for axis in range(3):
        other = [i for i in range(3) if i != axis]
        a, b = (lengths[i] for i in other)
        c = lengths[axis]
        if saturated:
            lines = [tuple(range(lo, hi + 1)) for lo in range(c)
                     for hi in range(lo, c)]
        else:
            lines = [line for size in range(1, c + 1)
                     for line in combinations(range(c), size)]
        for chain in planar_chains(a, b, saturated):
            for line in lines:
                cells = []
                for (x, y), z in product(chain, line):
                    point = [0, 0, 0]
                    point[other[0]], point[other[1]], point[axis] = x, y, z
                    cells.append(index[tuple(point)])
                key = tuple(sorted(cells))
                cost = len(chain) + len(line)
                old = catalogue.get(key)
                if old is None or cost < old[0]:
                    catalogue[key] = (cost, axis, chain, line)
    return points, catalogue


def optimize(lengths, saturated, integral, seconds, target, lp_support):
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, linprog, milp
    from scipy.sparse import csc_matrix

    points, catalogue = rectangles(lengths, saturated)
    keys = list(catalogue)
    costs = np.array([catalogue[key][0] for key in keys], dtype=float)
    rows, cols = [], []
    for j, key in enumerate(keys):
        rows.extend(key)
        cols.extend([j] * len(key))
    matrix = csc_matrix((np.ones(len(rows)), (rows, cols)),
                        shape=(len(points), len(keys)))
    print(f"grid={lengths} saturated={saturated} points={len(points)} "
          f"rectangles={len(keys)} baseline={min(lengths) * (sum(lengths) - min(lengths))}",
          flush=True)
    result = linprog(costs, A_eq=matrix, b_eq=np.ones(len(points)),
                     bounds=(0, None), method="highs")
    print(f"LP success={result.success} cost={result.fun}", flush=True)
    if lp_support:
        for j, weight in enumerate(result.x):
            if weight > 1e-7:
                print(f"  LP weight={weight:.9g} rectangle={catalogue[keys[j]]}")
    if not integral:
        return
    if target is not None:
        gap = target - result.fun
        if gap < -1e-7:
            print("Numerical LP already exceeds the requested integral target.")
            return
        retained = [j for j, reduced in enumerate(result.lower.marginals)
                    if reduced <= gap + 1e-7]
        print(f"Reduced-cost filter: {len(retained)} columns for target={target}",
              flush=True)
        matrix = matrix[:, retained]
        costs = costs[retained]
        keys = [keys[j] for j in retained]
    constraints = [LinearConstraint(matrix, 1, 1)]
    if target is not None:
        constraints.append(LinearConstraint(costs, -np.inf, target))
    result = milp(costs, integrality=np.ones(len(keys)),
                  bounds=Bounds(0, 1),
                  constraints=constraints,
                  options={"time_limit": seconds, "mip_rel_gap": 0})
    print(f"MILP status={result.message} cost={result.fun} "
          f"lower_bound={getattr(result, 'mip_dual_bound', None)}", flush=True)
    if result.x is None:
        return
    chosen = [j for j, value in enumerate(result.x) if value > 0.5]
    assert np.max(np.abs(result.x - np.rint(result.x))) < 1e-5
    covered = [i for j in chosen for i in keys[j]]
    assert sorted(covered) == list(range(len(points)))
    cost = sum(catalogue[keys[j]][0] for j in chosen)
    print(f"CHECKED integral partition: cost={cost}, pieces={len(chosen)}")
    for j in chosen:
        value, axis, chain, line = catalogue[keys[j]]
        print(f"  cost={value} axis={axis} line={line} planar_chain={chain}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lengths", type=int, nargs=3)
    parser.add_argument("--saturated", action="store_true")
    parser.add_argument("--integral", action="store_true")
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--target", type=int)
    parser.add_argument("--lp-support", action="store_true")
    args = parser.parse_args()
    optimize(tuple(args.lengths), args.saturated, args.integral, args.seconds,
             args.target, args.lp_support)
